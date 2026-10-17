"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
from io import BytesIO, StringIO
from typing import TYPE_CHECKING, BinaryIO, cast
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitNativeError,
    StringFileKind,
    StringTable,
)
from bethkit._ffi import _declare_strings

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestStringTableInput:
    """Checks input ownership, binary streams and native error propagation."""

    @pytest.mark.parametrize("kind", list(StringFileKind))
    def test_bytes_are_forwarded_without_string_conversion(
        self, mock_lib: MagicMock, kind: StringFileKind
    ) -> None:
        """Passes binary contents, including NULs, with an explicit format."""

        # given
        data = b"header\0\xffpayload"
        mock_lib.bethkit_string_table_from_bytes.return_value = 0xAAAA

        # when
        with StringTable.from_bytes(data, kind) as table:
            buffer, size, actual_kind = (
                mock_lib.bethkit_string_table_from_bytes.call_args.args
            )
            assert ctypes.string_at(buffer, size) == data
            assert size == len(data)
            assert actual_kind == int(kind)
            table.close()

        # then
        mock_lib.bethkit_string_table_free.assert_called_once_with(0xAAAA)
        with pytest.raises(BethkitClosedError):
            table.get(17)
        mock_lib.bethkit_string_table_get.assert_not_called()
        mock_lib.bethkit_string_table_open.assert_not_called()

    def test_stream_reads_remaining_bytes_without_closing(
        self, mock_lib: MagicMock
    ) -> None:
        """Consumes the current position, leaving ownership with the caller."""

        # given
        stream = BytesIO(b"prefixpayload")
        stream.seek(6)
        mock_lib.bethkit_string_table_from_bytes.return_value = 0xAAAA

        # when
        with StringTable.from_stream(stream, StringFileKind.STRINGS):
            pass

        # then
        buffer, size, _ = (
            mock_lib.bethkit_string_table_from_bytes.call_args.args
        )
        assert ctypes.string_at(buffer, size) == b"payload"
        assert stream.tell() == len(b"prefixpayload")
        assert not stream.closed

    def test_short_reads_do_not_require_seeking(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Collects short reads until EOF without seeking or closing."""

        stream = mocker.MagicMock(spec=BinaryIO)
        stream.read.side_effect = [b"ab", b"c\0", b"de", b""]
        mock_lib.bethkit_string_table_from_bytes.return_value = 0xAAAA
        with StringTable.from_stream(stream, StringFileKind.DL_STRINGS):
            pass
        buffer, size, _ = (
            mock_lib.bethkit_string_table_from_bytes.call_args.args
        )
        assert ctypes.string_at(buffer, size) == b"abc\0de"
        assert stream.read.call_count == 4
        stream.seek.assert_not_called()
        stream.close.assert_not_called()

    def test_malformed_bytes_copy_native_error(
        self, mock_lib: MagicMock
    ) -> None:
        """Raises immediately without adopting or freeing a null handle."""

        mock_lib.bethkit_string_table_from_bytes.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"invalid string table"
        with pytest.raises(BethkitNativeError, match="invalid string table"):
            StringTable.from_bytes(b"", StringFileKind.STRINGS)
        mock_lib.bethkit_string_table_free.assert_not_called()

    def test_missing_native_support_is_clear(self, mock_lib: MagicMock) -> None:
        """Keeps old native libraries usable for existing APIs."""

        del mock_lib.bethkit_string_table_from_bytes
        with pytest.raises(BethkitNativeError, match="in-memory string tables"):
            StringTable.from_bytes(b"data", StringFileKind.STRINGS)
        _declare_strings.declare(mock_lib)
        assert mock_lib.bethkit_string_table_open.restype is ctypes.c_void_p

    def test_wrapper_failure_frees_allocation(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Releases the allocation if constructing the Python owner fails."""

        mock_lib.bethkit_string_table_from_bytes.return_value = 0xAAAA
        mocker.patch.object(
            StringTable, "_from_native", side_effect=ValueError("owner")
        )
        with pytest.raises(ValueError, match="owner"):
            StringTable.from_bytes(b"data", StringFileKind.STRINGS)
        mock_lib.bethkit_string_table_free.assert_called_once_with(0xAAAA)

    def test_invalid_inputs_do_not_call_native(
        self, mock_lib: MagicMock
    ) -> None:
        """Rejects text streams and text byte arguments before parsing."""

        with pytest.raises(TypeError, match="must be bytes"):
            StringTable.from_bytes(cast(bytes, "text"), StringFileKind.STRINGS)
        with StringIO("text") as stream:
            with pytest.raises(TypeError, match="must be bytes"):
                StringTable.from_stream(
                    cast(BinaryIO, stream), StringFileKind.STRINGS
                )
        mock_lib.bethkit_string_table_from_bytes.assert_not_called()

    def test_stream_errors_leave_source_open(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Propagates source I/O errors without attempting native parsing."""

        stream = mocker.MagicMock(spec=BinaryIO)
        stream.read.side_effect = OSError("read failed")
        with pytest.raises(OSError, match="read failed"):
            StringTable.from_stream(stream, StringFileKind.STRINGS)
        stream.close.assert_not_called()
        mock_lib.bethkit_string_table_from_bytes.assert_not_called()

    def test_closed_stream_fails_before_native(
        self, mock_lib: MagicMock
    ) -> None:
        """Preserves the binary stream's standard closed-state exception."""

        stream = BytesIO(b"data")
        stream.close()
        with pytest.raises(ValueError, match="closed"):
            StringTable.from_stream(stream, StringFileKind.STRINGS)
        mock_lib.bethkit_string_table_from_bytes.assert_not_called()

    def test_invalid_format_never_crosses_ffi(
        self, mock_lib: MagicMock
    ) -> None:
        """Rejects invalid enum values before calling the native enum ABI."""

        with pytest.raises(ValueError):
            StringTable.from_bytes(b"data", cast(StringFileKind, 99))
        mock_lib.bethkit_string_table_from_bytes.assert_not_called()
