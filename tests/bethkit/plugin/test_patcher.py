"""
Copyright (c) Modding Forge
"""

# Tests native patcher ownership and minimal-change serialization.

from __future__ import annotations

import ctypes
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest
from conftest import build_minimal_plugin

from bethkit import BethkitClosedError, BethkitNativeError, Game, Plugin
from bethkit.plugin import PluginPatcher, WritableRecord

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestPluginPatcher:
    """Checks patcher calls without loading a native library."""

    def test_snapshot_does_not_consume_source(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps independent source and patcher ownership."""

        # given
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        source = Plugin(0x100)

        # when
        patcher = PluginPatcher(source)
        source.close()
        patcher.close()
        patcher.close()

        # then
        mock_lib.bethkit_plugin_patcher_new.assert_called_once_with(0x100)
        mock_lib.bethkit_plugin_free.assert_called_once_with(0x100)
        mock_lib.bethkit_plugin_patcher_free.assert_called_once_with(0x200)

    def test_replacement_remains_owned_by_caller(
        self, mock_lib: MagicMock
    ) -> None:
        """Borrows a writable record and frees it only through its owner."""

        # given
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        mock_lib.bethkit_plugin_patcher_replace_record.return_value = 0
        with Plugin(0x100) as source:
            with PluginPatcher(source) as patcher:
                replacement = WritableRecord(0x300)

                # when
                patcher.replace_record(0x800, replacement)
                replacement.close()

        # then
        mock_lib.bethkit_plugin_patcher_replace_record.assert_called_once_with(
            0x200, 0x800, 0x300
        )
        mock_lib.bethkit_writable_record_free.assert_called_once_with(0x300)

    def test_failed_replacement_retains_ownership(
        self, mock_lib: MagicMock
    ) -> None:
        """Copies an error immediately without consuming the replacement."""

        # given
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        mock_lib.bethkit_plugin_patcher_replace_record.return_value = -1
        mock_lib.bethkit_last_error.return_value = b"record not found"
        with Plugin(0x100) as source:
            with PluginPatcher(source) as patcher:
                with WritableRecord(0x300) as replacement:
                    # when / then
                    with pytest.raises(BethkitNativeError, match="not found"):
                        patcher.replace_record(0x800, replacement)

        mock_lib.bethkit_writable_record_free.assert_called_once_with(0x300)

    def test_write_bytes_copies_and_frees_allocation(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Releases an owned output buffer after copying its bytes."""

        # given
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        storage = (ctypes.c_uint8 * 4)(1, 2, 3, 4)

        def write_bytes(
            _pointer: int,
            output: ctypes.c_void_p,
            length: ctypes.c_void_p,
        ) -> int:
            """Supplies a borrowed test buffer as a fake native allocation."""

            ctypes.cast(output, ctypes.POINTER(ctypes.c_void_p))[0] = (
                ctypes.addressof(storage)
            )
            ctypes.cast(length, ctypes.POINTER(ctypes.c_size_t))[0] = 4
            return 0

        mock_lib.bethkit_plugin_patcher_write_to_bytes.side_effect = write_bytes
        with Plugin(0x100) as source:
            with PluginPatcher(source) as patcher:
                # when
                result = patcher.write_to_bytes()

        # then
        assert result == b"\x01\x02\x03\x04"
        mock_lib.bethkit_bytes_free.assert_called_once()
        assert mock_lib.bethkit_bytes_free.call_args.args[1] == 4

    def test_write_bytes_frees_when_copy_raises(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Does not leak the buffer when Python fails to copy it."""

        # given
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        mock_lib.bethkit_plugin_patcher_write_to_bytes.return_value = 0
        mocker.patch("ctypes.string_at", side_effect=MemoryError)
        with Plugin(0x100) as source:
            with PluginPatcher(source) as patcher:
                # when / then
                with pytest.raises(MemoryError):
                    patcher.write_to_bytes()
        mock_lib.bethkit_bytes_free.assert_called_once()

    def test_closed_patcher_rejects_access(
        self, mock_lib: MagicMock, tmp_path: Path
    ) -> None:
        """Fails before serialization or replacement touches native memory."""

        # given
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        with Plugin(0x100) as source:
            patcher = PluginPatcher(source)
        patcher.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            patcher.write_to_bytes()
        with pytest.raises(BethkitClosedError):
            patcher.write_to_file(tmp_path / "test.esp")
        with WritableRecord(0x300) as replacement:
            with pytest.raises(BethkitClosedError):
                patcher.replace_record(0x800, replacement)
        mock_lib.bethkit_plugin_patcher_write_to_bytes.assert_not_called()
        mock_lib.bethkit_plugin_patcher_write_to_file.assert_not_called()
        mock_lib.bethkit_plugin_patcher_replace_record.assert_not_called()

    def test_closed_source_rejected(self, mock_lib: MagicMock) -> None:
        """Prevents constructing a patcher from freed source memory."""

        # given
        source = Plugin(0x100)
        source.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            PluginPatcher(source)
        mock_lib.bethkit_plugin_patcher_new.assert_not_called()

    def test_write_to_file_encodes_path(
        self, mock_lib: MagicMock, tmp_path: Path
    ) -> None:
        """Passes an explicit destination path to the native writer."""

        # given
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        mock_lib.bethkit_plugin_patcher_write_to_file.return_value = 0
        path = tmp_path / "test.esp"
        with Plugin(0x100) as source:
            with PluginPatcher(source) as patcher:
                # when
                patcher.write_to_file(path)

        # then
        mock_lib.bethkit_plugin_patcher_write_to_file.assert_called_once_with(
            0x200, str(path).encode("utf-8")
        )


@pytest.mark.integration
class TestNativePluginPatcher:
    """Proves round-trip behavior through the compiled C ABI."""

    def test_unmodified_bytes_are_identical_after_source_close(self) -> None:
        """Preserves an unchanged input exactly with an independent snapshot."""

        # given
        original = build_minimal_plugin()
        with Plugin.from_bytes(original, Game.SKYRIM_SE) as source:
            patcher = PluginPatcher(source)

        # when
        with patcher:
            patched = patcher.write_to_bytes()

        # then
        assert patched == original

    def test_replacement_round_trip(self) -> None:
        """Changes the requested record and leaves the source unchanged."""

        # given
        original = build_minimal_plugin()
        with Plugin.from_bytes(original, Game.SKYRIM_SE) as source:
            with PluginPatcher(source) as patcher:
                with WritableRecord.new("NPC_", form_id=0xD62) as replacement:
                    replacement.add_subrecord("EDID", b"ChangedNPC\x00")

                    # when
                    patcher.replace_record(0xD62, replacement)
                    patched = patcher.write_to_bytes()

            # then
            source_record = source.find_record(0xD62)
            assert source_record is not None
            assert source_record.editor_id == "TestNPC"
        with Plugin.from_bytes(patched, Game.SKYRIM_SE) as result:
            record = result.find_record(0xD62)
            assert record is not None
            assert record.editor_id == "ChangedNPC"
