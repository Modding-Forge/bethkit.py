"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import struct
import zlib
from unittest.mock import MagicMock

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import BethkitClosedError, BethkitNativeError, Game, Plugin, Record


class _Owner:
    """Control borrowed lifetime without allocating any native memory."""

    closed: bool = False

    def _check_borrowed(self) -> None:
        """Reject reads after simulated ownership ends.

        Raises:
            BethkitClosedError: The simulated owner has closed.
        """

        if self.closed:
            raise BethkitClosedError("Owner is closed.")


class TestSubrecordSignatures:
    """Retain ordering, ownership and failures across the bulk FFI path."""

    def test_copies_ordered_signatures(self, mock_lib: MagicMock) -> None:
        """Return independent bytes, including unknown and repeated fields.

        Args:
            mock_lib: Mocked native library.
        """

        # given
        owner = _Owner()
        record = Record._from_native(0xDEAD, owner)
        mock_lib.bethkit_record_subrecord_count.return_value = 3

        def copy(
            pointer: int, output: ctypes.Array[ctypes.c_uint8], capacity: int
        ) -> int:
            """Fill the caller's bounded buffer as the native function does.

            Args:
                pointer: Borrowed record pointer.
                output: Caller-owned signature storage.
                capacity: Writable byte count.

            Returns:
                Number of copied signatures.
            """

            assert pointer == 0xDEAD and capacity == 12
            output[:] = b"FULLZZZZFULL"
            return 3

        mock_lib.bethkit_record_subrecord_signatures.side_effect = copy

        # when
        result = record.subrecord_signatures()
        owner.closed = True

        # then
        assert result == (b"FULL", b"ZZZZ", b"FULL")
        mock_lib.bethkit_record_subrecord_get.assert_not_called()
        with pytest.raises(BethkitClosedError):
            record.subrecord_signatures()
        mock_lib.bethkit_record_subrecord_signatures.assert_called_once()

    def test_empty_does_not_copy(self, mock_lib: MagicMock) -> None:
        """Avoid allocating a native output buffer for an empty record.

        Args:
            mock_lib: Mocked native library.
        """

        mock_lib.bethkit_record_subrecord_count.return_value = 0
        record = Record._from_native(0xDEAD, _Owner())
        assert record.subrecord_signatures() == ()
        mock_lib.bethkit_record_subrecord_signatures.assert_not_called()

    @pytest.mark.parametrize("copied", [-1, 1])
    def test_failures_are_not_partial_results(
        self, mock_lib: MagicMock, copied: int
    ) -> None:
        """Reject native failures and impossible count changes.

        Args:
            mock_lib: Mocked native library.
            copied: Failed or inconsistent native return value.
        """

        mock_lib.bethkit_record_subrecord_count.return_value = 2
        mock_lib.bethkit_record_subrecord_signatures.return_value = copied
        mock_lib.bethkit_last_error.return_value = b"Invalid signature buffer"
        record = Record._from_native(0xDEAD, _Owner())
        with pytest.raises(BethkitNativeError):
            record.subrecord_signatures()

    def test_older_library_uses_existing_reads(
        self, mock_lib: MagicMock
    ) -> None:
        """Keep older native libraries usable without the new symbol.

        Args:
            mock_lib: Mocked native library without the optional function.
        """

        del mock_lib.bethkit_record_subrecord_signatures
        mock_lib.bethkit_record_subrecord_count.return_value = 1
        mock_lib.bethkit_record_subrecord_get.return_value = 0xBEEF

        def copy(pointer: int, output: ctypes.Array[ctypes.c_uint8]) -> int:
            """Populate one old-style borrowed signature.

            Args:
                pointer: Borrowed subrecord pointer.
                output: Four-byte destination.

            Returns:
                Native success code.
            """

            assert pointer == 0xBEEF
            output[:] = b"FULL"
            return 0

        mock_lib.bethkit_subrecord_signature.side_effect = copy
        record = Record._from_native(0xDEAD, _Owner())
        assert record.subrecord_signatures() == (b"FULL",)


@pytest.mark.integration
class TestNativeSubrecordSignatures:
    """Compare actual bulk copies with the established borrowed iterator."""

    def test_extended_payload_keeps_source_positions(self) -> None:
        """Treat XXXX length markers exactly like the borrowed iterator."""

        # given
        large = b"x" * 0x10000
        payload = (
            build_subrecord(b"FULL", b"Name\0")
            + build_subrecord(b"XXXX", struct.pack("<I", len(large)))
            + b"ZZZZ\0\0"
            + large
            + build_subrecord(b"FULL", b"Again\0")
        )
        source = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr())
        ) + build_grup(b"CLAS", 0, build_record(b"CLAS", 0x800, 0, payload))
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = plugin.find_record(0x800)
            assert record is not None

            # when
            signatures = record.subrecord_signatures()

            # then
            assert signatures == tuple(value.signature for value in record)
            assert signatures == (b"FULL", b"ZZZZ", b"FULL")
            assert record.subrecord_at(1).raw_bytes == large

    @pytest.mark.parametrize("malformed", [False, True])
    def test_empty_and_malformed_payloads(self, malformed: bool) -> None:
        """Keep parsing failures distinct from valid empty record contents.

        Args:
            malformed: Whether the payload has a truncated subrecord.
        """

        payload = b"FULL\x10\x00short" if malformed else b""
        source = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr())
        ) + build_grup(b"CLAS", 0, build_record(b"CLAS", 0x800, 0, payload))
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = plugin.find_record(0x800)
            assert record is not None
            if malformed:
                with pytest.raises(BethkitNativeError):
                    record.subrecord_signatures()
            else:
                assert record.subrecord_signatures() == ()

    @pytest.mark.parametrize("compressed", [False, True])
    def test_order_and_lifetime(self, compressed: bool) -> None:
        """Copy identical signatures from compressed and plain records.

        Args:
            compressed: Whether the test record uses a zlib payload.
        """

        # given
        payload = b"".join(
            build_subrecord(signature, b"text\0")
            for signature in (b"FULL", b"ZZZZ", b"FULL")
        )
        flags = 0
        if compressed:
            flags = 0x40000
            payload = struct.pack("<I", len(payload)) + zlib.compress(payload)
        source = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr())
        ) + build_grup(b"CLAS", 0, build_record(b"CLAS", 0x800, flags, payload))
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = plugin.find_record(0x800)
            assert record is not None

            # when
            result = record.subrecord_signatures()

            # then
            assert result == tuple(value.signature for value in record)
            assert result == (b"FULL", b"ZZZZ", b"FULL")
        assert result == (b"FULL", b"ZZZZ", b"FULL")
        with pytest.raises(BethkitClosedError):
            record.subrecord_signatures()
