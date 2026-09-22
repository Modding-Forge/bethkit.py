"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitOwnershipError,
    WritableRecord,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestWritableRecord:
    """Tests ``bethkit.plugin.writer.WritableRecord``."""

    def test_new_creates_writable_record(self, mocker: MockerFixture) -> None:
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

    def test_new_accepts_str_signature(self, mocker: MockerFixture) -> None:
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

    def test_new_with_explicit_flags_form_id_form_version(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that new() passes flags, form_id and form_version to FFI."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with WritableRecord.new(
            b"NPC_", flags=0x40, form_id=0x000D62, form_version=44
        ):
            pass

        # then
        call_args = mock_lib.bethkit_writable_record_new.call_args
        _sig, flags, form_id, form_version = call_args.args
        assert flags == 0x40
        assert form_id == 0x000D62
        assert form_version == 44

    def test_transfer_ptr_returns_and_zeroes_handle(
        self, mocker: MockerFixture
    ) -> None:
        """Transfers the native pointer and invalidates its wrapper."""

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

    def test_add_subrecord_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that subrecord insertion delegates to the native record."""

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
        """Rejects subrecord insertion after closing the record."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        rec = WritableRecord.new(b"NPC_")
        rec.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            rec.add_subrecord(b"EDID", b"data")

    def test_context_manager_frees_on_exit(self, mocker: MockerFixture) -> None:
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
        """Does not free a native pointer after ownership transfers."""

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
