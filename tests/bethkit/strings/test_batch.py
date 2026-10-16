"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import json
from collections.abc import Generator
from typing import TYPE_CHECKING, cast
from unittest.mock import MagicMock

import pydantic
import pytest

from bethkit import BethkitClosedError, Plugin, SemanticContext
from bethkit.records import _wire
from bethkit.strings import _batch

from ._fixtures import snapshot

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def configure(
    lib: MagicMock, mocker: MockerFixture, *, payload: str
) -> SemanticContext:
    """Configures a batch-capable mock without loading native code.

    Args:
        lib: Mocked library to receive lifecycle functions.
        mocker: Active mock manager.
        payload: Independently copied native JSON.

    Returns:
        Borrowed mock semantic context.
    """

    lib.bethkit_string_cursor_new = MagicMock(return_value=0x700)
    lib.bethkit_string_cursor_next_json = MagicMock(return_value=0x800)
    lib.bethkit_string_cursor_free = MagicMock()
    mocker.patch("bethkit._ffi.copy_and_free_str", return_value=payload)
    context = cast(
        SemanticContext, mocker.create_autospec(SemanticContext, instance=True)
    )
    return context


class TestStringBatch:
    """Preserves owned JSON, cursor cleanup, laziness and source lifetimes."""

    def test_close_owner_inside_batch(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Does not expose buffered references after their source closes.

        Args:
            mock_lib: Patched native functions.
            mocker: Active mock manager.
        """

        # given
        payload = json.dumps(
            {
                "values": [
                    field.value.model_dump() for field in snapshot().fields
                ],
                "done": True,
            }
        )
        context = configure(mock_lib, mocker, payload=payload)
        with Plugin._from_native(0x100) as plugin:
            iterator = cast(
                Generator[_wire.WireScalar, None, None],
                _batch.iter_values(plugin, context),
            )
            mock_lib.bethkit_string_cursor_new.assert_not_called()
            next(iterator)
            # when
            plugin.close()
            # then
            with pytest.raises(BethkitClosedError):
                next(iterator)
        mock_lib.bethkit_string_cursor_free.assert_called_once_with(0x700)

    def test_invalid_batch_releases_cursor(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Retains Pydantic validation and cleanup on invalid native data.

        Args:
            mock_lib: Patched native functions.
            mocker: Active mock manager.
        """

        context = configure(mock_lib, mocker, payload='{"values":42}')
        with Plugin._from_native(0x100) as plugin:
            with pytest.raises(pydantic.ValidationError):
                list(_batch.iter_values(plugin, context))
        mock_lib.bethkit_string_cursor_free.assert_called_once_with(0x700)

    def test_explicit_generator_close_releases_cursor(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Releases the native cursor when iteration stops early.

        Args:
            mock_lib: Patched native functions.
            mocker: Active mock manager.
        """

        payload = json.dumps(
            {
                "values": [snapshot().fields[0].value.model_dump()],
                "done": False,
            }
        )
        context = configure(mock_lib, mocker, payload=payload)
        with Plugin._from_native(0x100) as plugin:
            iterator = cast(
                Generator[_wire.WireScalar, None, None],
                _batch.iter_values(plugin, context),
            )
            next(iterator)
            iterator.close()
        mock_lib.bethkit_string_cursor_free.assert_called_once_with(0x700)
