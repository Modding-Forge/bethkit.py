"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitNativeError,
    BethkitOwnershipError,
    Game,
    PluginWriter,
    WritableGroup,
    WritableRecord,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestWritableRecord:
    """Tests ``bethkit.plugin.writer.WritableRecord``."""

    def test_new_creates_writable_record(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that WritableRecord.new() calls the FFI and wraps the ptr."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        rec = WritableRecord.new(b"NPC_")

        # then
        assert isinstance(rec, WritableRecord)
        rec.close()

    def test_new_raises_value_error_for_short_signature(self) -> None:
        """Tests that new() raises ValueError when sig is not 4 bytes."""

        # when / then
        with pytest.raises(ValueError):
            WritableRecord.new(b"NP")

    def test_new_raises_value_error_for_long_signature(self) -> None:
        """Tests that new() raises ValueError when sig is more than 4 bytes."""

        # when / then
        with pytest.raises(ValueError):
            WritableRecord.new(b"NPC_X")

    def test_new_accepts_str_signature(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that new() accepts a str signature and encodes it."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        rec = WritableRecord.new("NPC_")

        # then
        assert isinstance(rec, WritableRecord)
        rec.close()

    def test_transfer_ptr_returns_and_zeroes_handle(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that _transfer_ptr() returns the ptr and invalidates the handle."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        rec = WritableRecord.new(b"NPC_")

        # when
        ptr = rec._transfer_ptr()

        # then
        assert ptr == 0xABCD
        with pytest.raises(BethkitOwnershipError):
            rec._transfer_ptr()

    def test_add_subrecord_calls_native(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_subrecord() delegates to
        bethkit_writable_record_add_subrecord."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mock_lib.bethkit_writable_record_add_subrecord.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with WritableRecord.new(b"NPC_") as rec:
            rec.add_subrecord(b"EDID", b"MyNPC\x00")

        # then
        mock_lib.bethkit_writable_record_add_subrecord.assert_called_once()

    def test_add_subrecord_raises_after_close(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_subrecord() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        rec = WritableRecord.new(b"NPC_")
        rec.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            rec.add_subrecord(b"EDID", b"data")

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls bethkit_writable_record_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with WritableRecord.new(b"NPC_"):
            pass

        # then
        mock_lib.bethkit_writable_record_free.assert_called_once_with(0xABCD)

    def test_close_skips_free_after_transfer(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that close() is a no-op after _transfer_ptr() has been called."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        rec = WritableRecord.new(b"NPC_")
        rec._transfer_ptr()

        # when
        rec.close()

        # then
        mock_lib.bethkit_writable_record_free.assert_not_called()


class TestWritableGroup:
    """Tests ``bethkit.plugin.writer.WritableGroup``."""

    def test_new_creates_group(self, mocker: MockerFixture) -> None:
        """Tests that WritableGroup.new() calls the FFI and wraps the ptr."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        group = WritableGroup.new(b"NPC_")

        # then
        assert isinstance(group, WritableGroup)
        group.close()

    def test_add_record_transfers_ownership(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_record() takes ownership of the WritableRecord."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mock_lib.bethkit_writable_group_add_record.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        rec = WritableRecord.new(b"NPC_")

        # when
        with WritableGroup.new(b"NPC_") as group:
            group.add_record(rec)

        # then — second _transfer_ptr must fail (already zeroed)
        with pytest.raises(BethkitOwnershipError):
            rec._transfer_ptr()

    def test_add_record_raises_after_close(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_record() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        group = WritableGroup.new(b"NPC_")
        group.close()
        rec = WritableRecord.new(b"NPC_")

        # when / then
        with pytest.raises(BethkitClosedError):
            group.add_record(rec)
        rec.close()

    def test_transfer_ptr_invalidates_group(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that _transfer_ptr() zeroes the group handle."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = WritableGroup.new(b"NPC_")

        # when
        ptr = group._transfer_ptr()

        # then
        assert ptr == 0xBEEF
        with pytest.raises(BethkitOwnershipError):
            group._transfer_ptr()


class TestPluginWriter:
    """Tests ``bethkit.plugin.writer.PluginWriter``."""

    def test_constructor_calls_writer_new(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __init__ calls bethkit_plugin_writer_new."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        writer = PluginWriter(Game.SKYRIM_SE)

        # then
        mock_lib.bethkit_plugin_writer_new.assert_called_once()
        writer.close()

    def test_constructor_raises_on_null_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __init__ raises BethkitNativeError when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"writer error"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with pytest.raises(BethkitNativeError):
            PluginWriter(Game.SKYRIM_SE)

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls bethkit_plugin_writer_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginWriter(Game.SKYRIM_SE):
            pass

        # then
        mock_lib.bethkit_plugin_writer_free.assert_called_once_with(0xCCCC)

    def test_add_group_transfers_group_ownership(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_group() takes ownership of the WritableGroup."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mock_lib.bethkit_plugin_writer_add_group.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        group = WritableGroup.new(b"NPC_")

        # when
        with PluginWriter(Game.SKYRIM_SE) as writer:
            writer.add_group(group)

        # then — group must be invalidated
        with pytest.raises(BethkitOwnershipError):
            group._transfer_ptr()

    def test_close_prevents_add_group(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_group() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        writer = PluginWriter(Game.SKYRIM_SE)
        writer.close()
        group = WritableGroup.new(b"NPC_")

        # when / then
        with pytest.raises(BethkitClosedError):
            writer.add_group(group)
        group.close()
