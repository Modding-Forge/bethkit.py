"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import uuid
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    Plugin,
    SchemaPackage,
    SemanticContext,
    _ffi,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestPluginEncoding:
    """Checks the ctypes ownership boundary without loading native code."""

    def test_factory_passes_path_and_frees_context(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Passes an explicit path and releases the adopted context once.

        Args:
            mocker: Restored ctypes boundary mocks.
            tmp_path: Example override path with spaces.
        """

        # given
        package = MagicMock(spec=SchemaPackage)
        package._native_pointer.return_value = 100
        plugin = MagicMock(spec=Plugin)
        plugin._native_pointer.return_value = 200
        plugin._reference_identity.return_value = uuid.uuid4()
        lib = MagicMock()
        lib.bethkit_semantic_context_new_for_plugin.return_value = 300
        mocker.patch.object(_ffi, "load_lib", return_value=lib)
        override = tmp_path / "A mod.cpoverride"

        # when
        context = SemanticContext.for_plugin(
            package, plugin, cpoverride=override
        )
        context.close()
        context.close()

        # then
        lib.bethkit_semantic_context_new_for_plugin.assert_called_once_with(
            100, 200, _ffi.senc(str(override))
        )
        lib.bethkit_semantic_context_free.assert_called_once_with(300)
        with pytest.raises(BethkitClosedError):
            _ = context.encoding_decision

    def test_closed_plugin_prevents_native_creation(
        self, mocker: MockerFixture
    ) -> None:
        """Checks source lifetime before loading or calling native functions.

        Args:
            mocker: Restored native-loader mock.
        """

        package = MagicMock(spec=SchemaPackage)
        plugin = MagicMock(spec=Plugin)
        plugin._native_pointer.side_effect = BethkitClosedError("Closed")
        load = mocker.patch.object(_ffi, "load_lib")
        with pytest.raises(BethkitClosedError):
            SemanticContext.for_plugin(package, plugin)
        load.assert_not_called()

    def test_decision_copies_and_frees_native_json(
        self, mocker: MockerFixture
    ) -> None:
        """Validates metadata after copying and freeing its owned native JSON.

        Args:
            mocker: Restored native-boundary mocks.
        """

        package = MagicMock(spec=SchemaPackage)
        plugin = MagicMock(spec=Plugin)
        lib = MagicMock()
        lib.bethkit_semantic_context_new_for_plugin.return_value = 300
        lib.bethkit_semantic_context_encoding_json.return_value = 400
        mocker.patch.object(_ffi, "load_lib", return_value=lib)
        copy = mocker.patch.object(
            _ffi,
            "copy_and_free_str",
            return_value='{"encoding":"windows-1251","source":"detector",'
            '"sample_bytes":120,"sample_strings":3,"scanned_records":3,'
            '"skipped_records":0}',
        )
        with SemanticContext.for_plugin(package, plugin) as context:
            decision = context.encoding_decision
            assert decision is not None
            assert decision.encoding == "windows-1251"
            copy.assert_called_once_with(400, lib.bethkit_string_free, lib)
