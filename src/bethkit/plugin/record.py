"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
from collections.abc import Iterator
from typing import Optional

from .. import _ffi, _ownership
from .._error import BethkitNativeError
from .subrecord import SubRecord


class Record(_ownership.BorrowedHandle):
    """A single plugin record containing sub-records.

    Records are owned by their parent :class:`Group` or
    :class:`PluginCache` and must not outlive it.

    Access after the native owner closes raises ``BethkitClosedError``.
    """

    def __init__(self) -> None:
        """Rejects direct construction of borrowed native views.

        Raises:
            TypeError: Always; retrieve this view from its owning object.
        """

        raise TypeError("Record must be obtained from its owning object.")

    @classmethod
    def _from_native(
        cls, pointer: int, owner: _ownership.BorrowOwner
    ) -> Record:
        """Wraps a borrowed pointer without taking ownership.

        Args:
            pointer: Nonzero native pointer borrowed from the owner.
            owner: Object that keeps the native allocation alive.

        Returns:
            A borrowed view that validates its owner's lifetime.

        Raises:
            ValueError: The supplied native pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot borrow a null Record pointer.")
        result = cls.__new__(cls)
        _ownership.BorrowedHandle.__init__(result, pointer, owner)
        return result

    @property
    def signature(self) -> bytes:
        """Four-byte ASCII record type signature.

        Returns:
            bytes: Four-byte signature (e.g. ``b"NPC_"``).

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * 4)()
        if lib.bethkit_record_signature(self._native_pointer(), buf) != 0:
            _ffi.raise_last_error(lib)
        return bytes(buf)

    @property
    def form_id(self) -> int:
        """Raw 32-bit FormID of the record as stored in the plugin.

        Returns:
            int: FormID value.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        return _ffi.load_lib().bethkit_record_form_id(self._native_pointer())

    @property
    def flags(self) -> int:
        """Record header flags bitmask.

        Returns:
            int: Flags value.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        return _ffi.load_lib().bethkit_record_flags(self._native_pointer())

    @property
    def form_version(self) -> int:
        """Form version stored in the record header.

        Returns:
            int: Form version number.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        return _ffi.load_lib().bethkit_record_form_version(
            self._native_pointer()
        )

    @property
    def editor_id(self) -> Optional[str]:
        """Editor ID string (EDID sub-record), if present.

        Returns:
            Optional[str]: The editor ID, or ``None`` if absent.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: The native operation failed.
        """

        lib = _ffi.load_lib()
        ptr = ctypes.c_void_p()
        status = lib.bethkit_record_editor_id_status(
            self._native_pointer(), ctypes.byref(ptr)
        )
        if status == 1:
            return None
        if status != 0:
            _ffi.raise_last_error(lib)
        try:
            return ctypes.string_at(ptr).decode("utf-8")
        finally:
            lib.bethkit_record_editor_id_free(ptr)

    def subrecord_count(self) -> int:
        """Return the number of sub-records in this record.

        Returns:
            int: Sub-record count.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        n = lib.bethkit_record_subrecord_count(self._native_pointer())
        if n < 0:
            _ffi.raise_last_error(lib)
        return n

    def subrecord_at(self, index: int) -> SubRecord:
        """Return the sub-record at the given index.

        Args:
            index (int): Zero-based sub-record index.

        Returns:
            SubRecord: Borrowed sub-record.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If *index* is out of range.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_record_subrecord_get(self._native_pointer(), index)
        if not ptr:
            _ffi.raise_last_error(lib)
        return SubRecord._from_native(ptr, self)

    def find_subrecord(self, sig: bytes | str) -> Optional[SubRecord]:
        """Find the first sub-record matching the given 4-byte signature.

        Args:
            sig (bytes | str): Four-byte signature to search for.

        Returns:
            Optional[SubRecord]: The first matching sub-record, or ``None``.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            ValueError: If *sig* is not exactly 4 bytes.
        """

        if isinstance(sig, str):
            sig = sig.encode("ascii")
        if len(sig) != 4:
            raise ValueError("sig must be exactly 4 bytes")
        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * 4)(*sig)
        ptr = lib.bethkit_record_subrecord_find(self._native_pointer(), buf)
        if not ptr:
            return None
        return SubRecord._from_native(ptr, self)

    def __iter__(self) -> Iterator[SubRecord]:
        """Iterate over all sub-records in this record.

        Yields:
            SubRecord: Each sub-record in order.

        Raises:
            BethkitClosedError: The native owner closes during iteration.
            BethkitNativeError: A subrecord cannot be read.
        """

        for i in range(self.subrecord_count()):
            yield self.subrecord_at(i)

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation with signature and FormID.

        Raises:
            BethkitClosedError: The native owner is closed.
        """

        try:
            sig = self.signature.decode("ascii", errors="replace")
            fid = self.form_id
        except BethkitNativeError:
            return "<Record ?>"
        return f"<Record {sig!r} FormID=0x{fid:08X}>"
