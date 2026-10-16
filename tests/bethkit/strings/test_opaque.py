"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pydantic
import pytest

from bethkit import Plugin
from bethkit.strings import StringScanDiagnostic, _batch

from .test_batch import configure

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestOpaqueDiagnostics:
    """Keeps diagnostic validation and owned-cursor cleanup mandatory."""

    def test_observer_failure_frees_cursor(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Propagates an observer failure without leaking its cursor.

        Args:
            mock_lib: Mocked ctypes library.
            mocker: Active mock manager.
        """

        diagnostic = StringScanDiagnostic(
            record_signature="NAVM",
            form_id=0x800,
            source_size=22,
            message="Invalid source",
        )
        context = configure(
            mock_lib,
            mocker,
            payload=json.dumps(
                {
                    "values": [],
                    "done": True,
                    "diagnostics": [diagnostic.model_dump()],
                }
            ),
        )
        constructor = MagicMock(return_value=0x700)
        mock_lib.bethkit_string_cursor_new_preserving_nontext = constructor
        observer = MagicMock(side_effect=RuntimeError("Observer failed"))
        with Plugin._from_native(0x100) as plugin:
            with pytest.raises(RuntimeError, match="Observer failed"):
                list(
                    _batch.iter_values(
                        plugin,
                        context,
                        preserve_opaque_nontext=True,
                        on_diagnostic=observer,
                    )
                )
        observer.assert_called_once_with(diagnostic)
        mock_lib.bethkit_string_cursor_new.assert_not_called()
        mock_lib.bethkit_string_cursor_free.assert_called_once_with(0x700)

    def test_invalid_diagnostic_frees_cursor(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Rejects malformed native diagnostics at the model boundary.

        Args:
            mock_lib: Mocked ctypes library.
            mocker: Active mock manager.
        """

        context = configure(
            mock_lib,
            mocker,
            payload=json.dumps(
                {
                    "values": [],
                    "done": True,
                    "diagnostics": [{"form_id": -1}],
                }
            ),
        )
        with Plugin._from_native(0x100) as plugin:
            with pytest.raises(pydantic.ValidationError):
                list(_batch.iter_values(plugin, context))
        mock_lib.bethkit_string_cursor_free.assert_called_once_with(0x700)
