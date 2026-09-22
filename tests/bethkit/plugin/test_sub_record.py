"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

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


class TestSubRecord:
    """Tests ``bethkit.plugin.plugin.SubRecord``."""

    def test_as_u8_calls_native_and_returns_int(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_u8() delegates to bethkit_subrecord_as_u8."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u8.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord._from_native(
            0xBEEF, Record._from_native(0xDEAD, _OpenOwner())
        )

        # when
        result = sub.as_u8()

        # then
        assert isinstance(result, int)
        mock_lib.bethkit_subrecord_as_u8.assert_called_once()

    def test_as_u16_calls_native_and_returns_int(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_u16() delegates to bethkit_subrecord_as_u16."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u16.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord._from_native(
            0xBEEF, Record._from_native(0xDEAD, _OpenOwner())
        )

        # when
        result = sub.as_u16()

        # then
        assert isinstance(result, int)
        mock_lib.bethkit_subrecord_as_u16.assert_called_once()

    def test_as_u32_calls_native_and_returns_int(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_u32() delegates to bethkit_subrecord_as_u32."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u32.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord._from_native(
            0xBEEF, Record._from_native(0xDEAD, _OpenOwner())
        )

        # when
        result = sub.as_u32()

        # then
        assert isinstance(result, int)
        mock_lib.bethkit_subrecord_as_u32.assert_called_once()

    def test_as_f32_calls_native_and_returns_float(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_f32() delegates to bethkit_subrecord_as_f32."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_f32.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord._from_native(
            0xBEEF, Record._from_native(0xDEAD, _OpenOwner())
        )

        # when
        result = sub.as_f32()

        # then
        assert isinstance(result, float)
        mock_lib.bethkit_subrecord_as_f32.assert_called_once()

    def test_as_str_decodes_utf8_and_frees_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Decodes the native string and frees its allocation."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        fake_ptr: int = 0xCCCC
        mock_lib.bethkit_subrecord_as_zstring.return_value = fake_ptr
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        mocker.patch("ctypes.string_at", return_value=b"TestValue")
        sub = SubRecord._from_native(
            0xBEEF, Record._from_native(0xDEAD, _OpenOwner())
        )

        # when
        result = sub.as_str()

        # then
        assert result == "TestValue"
        mock_lib.bethkit_zstring_free.assert_called_once_with(fake_ptr)

    def test_as_str_raises_on_null_ptr(self, mocker: MockerFixture) -> None:
        """Tests that as_str() raises BethkitNativeError when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_zstring.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"type mismatch"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord._from_native(
            0xBEEF, Record._from_native(0xDEAD, _OpenOwner())
        )

        # when / then
        with pytest.raises(BethkitNativeError):
            sub.as_str()

    def test_as_u8_raises_on_native_error(self, mocker: MockerFixture) -> None:
        """Raises a native error when the unsigned byte decode fails."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u8.return_value = 1
        mock_lib.bethkit_last_error.return_value = b"size mismatch"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord._from_native(
            0xBEEF, Record._from_native(0xDEAD, _OpenOwner())
        )

        # when / then
        with pytest.raises(BethkitNativeError):
            sub.as_u8()
