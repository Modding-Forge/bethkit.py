"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitNativeError,
    Record,
    SubRecord,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class _OpenOwner:
    """Supplies an always-live owner for isolated borrowed-handle tests."""

    def _check_borrowed(self) -> None:
        """Accepts access without loading a native library."""

        return None


class TestRecord:
    """Tests ``bethkit.plugin.plugin.Record``."""

    def test_absent_editor_id_ignores_stale_error(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps absence distinct from a previous unrelated native error."""

        # given
        mock_lib.bethkit_record_editor_id_status.return_value = 1
        mock_lib.bethkit_last_error.return_value = b"an earlier failure"
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when / then
        assert record.editor_id is None
        mock_lib.bethkit_last_error.assert_not_called()
        mock_lib.bethkit_record_editor_id_free.assert_not_called()

    def test_editor_id_error_is_not_absence(self, mock_lib: MagicMock) -> None:
        """Raises an actual decoder failure instead of returning None."""

        # given
        mock_lib.bethkit_record_editor_id_status.return_value = -1
        mock_lib.bethkit_last_error.return_value = b"malformed EDID"
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when / then
        with pytest.raises(BethkitNativeError, match="malformed EDID"):
            _ = record.editor_id
        mock_lib.bethkit_record_editor_id_free.assert_not_called()

    def test_editor_id_returns_none_when_absent(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that editor_id returns None when FFI returns a null pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_editor_id_status.return_value = 1
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sentinel_parent = _OpenOwner()
        record = Record._from_native(0xDEAD, sentinel_parent)

        # when
        result = record.editor_id

        # then
        assert result is None

    def test_editor_id_decodes_bytes(self, mocker: MockerFixture) -> None:
        """Tests that editor_id decodes the FFI string and frees the pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        fake_ptr = 0xBEEF

        def write_editor_id(_pointer: int, output: ctypes.c_void_p) -> int:
            """Populates the status function's owned string result."""

            ctypes.cast(output, ctypes.POINTER(ctypes.c_void_p))[0] = fake_ptr
            return 0

        mock_lib.bethkit_record_editor_id_status.side_effect = write_editor_id
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        mocker.patch("ctypes.string_at", return_value=b"TestNPC")
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when
        result = record.editor_id

        # then
        assert result == "TestNPC"
        mock_lib.bethkit_record_editor_id_free.assert_called_once()
        assert (
            mock_lib.bethkit_record_editor_id_free.call_args.args[0].value
            == fake_ptr
        )

    def test_form_id_delegates_to_native(self, mocker: MockerFixture) -> None:
        """Tests that form_id returns the value from bethkit_record_form_id."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_form_id.return_value = 0x000D62
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when
        result = record.form_id

        # then
        assert result == 0x000D62

    def test_signature_returns_four_bytes(self, mocker: MockerFixture) -> None:
        """Tests that signature copies four bytes from the native buffer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()

        def fake_sig(ptr: int, buf: ctypes.Array[ctypes.c_uint8]) -> int:
            """Fills a native output buffer with the fixture signature."""

            for i, b in enumerate(b"NPC_"):
                buf[i] = b
            return 0

        mock_lib.bethkit_record_signature.side_effect = fake_sig
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when
        sig = record.signature

        # then
        assert sig == b"NPC_"

    def test_find_subrecord_returns_none_when_absent(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_subrecord() returns None when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_subrecord_find.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when
        result = record.find_subrecord(b"EDID")

        # then
        assert result is None

    def test_find_subrecord_returns_subrecord(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_subrecord() wraps a non-null FFI pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_subrecord_find.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when
        result = record.find_subrecord(b"EDID")

        # then
        assert isinstance(result, SubRecord)

    def test_find_subrecord_validates_signature_length(self) -> None:
        """Rejects subrecord signatures with an incorrect length."""

        # given
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when / then
        with pytest.raises(ValueError):
            record.find_subrecord(b"ED")

    def test_flags_delegates_to_native(self, mocker: MockerFixture) -> None:
        """Tests that flags reads from bethkit_record_flags."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_flags.return_value = 0x00000020
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when
        result = record.flags

        # then
        assert result == 0x00000020

    def test_form_version_delegates_to_native(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that form_version reads from bethkit_record_form_version."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_form_version.return_value = 44
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record._from_native(0xDEAD, _OpenOwner())

        # when
        result = record.form_version

        # then
        assert result == 44
