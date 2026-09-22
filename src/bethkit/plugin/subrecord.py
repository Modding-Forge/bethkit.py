"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes

from .. import _ffi, _ownership
from .._error import BethkitNativeError


class SubRecord(_ownership.BorrowedHandle):
    """A single sub-record field inside a :class:`Record`.

    Sub-records are borrowed from the parent ``Record`` and become
    invalid once the record is closed or freed.
    """

    def __init__(self) -> None:
        """Rejects direct construction of borrowed native views.

        Raises:
            TypeError: Always; retrieve this view from its owning object.
        """

        raise TypeError("SubRecord must be obtained from its owning object.")

    @classmethod
    def _from_native(
        cls, pointer: int, owner: _ownership.BorrowOwner
    ) -> SubRecord:
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
            raise ValueError("Cannot borrow a null SubRecord pointer.")
        result = cls.__new__(cls)
        _ownership.BorrowedHandle.__init__(result, pointer, owner)
        return result

    @property
    def signature(self) -> bytes:
        """Four-byte ASCII signature identifying the sub-record type.

        Returns:
            bytes: Four-byte signature (e.g. ``b"EDID"``).

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * 4)()
        if lib.bethkit_subrecord_signature(self._native_pointer(), buf) != 0:
            _ffi.raise_last_error(lib)
        return bytes(buf)

    @property
    def raw_bytes(self) -> bytes:
        """Raw byte content of the sub-record as stored in the plugin.

        Returns:
            bytes: Sub-record data, or ``b""`` if empty.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        lib = _ffi.load_lib()
        sl = lib.bethkit_subrecord_bytes(self._native_pointer())
        if not sl.ptr:
            return b""
        return bytes(ctypes.string_at(sl.ptr, sl.len))

    def as_u8(self) -> int:
        """Interpret the sub-record data as an unsigned 8-bit integer.

        Returns:
            int: Decoded value.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_uint8()
        if (
            lib.bethkit_subrecord_as_u8(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_u16(self) -> int:
        """Interpret the sub-record data as an unsigned 16-bit integer.

        Returns:
            int: Decoded value.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_uint16()
        if (
            lib.bethkit_subrecord_as_u16(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_u32(self) -> int:
        """Interpret the sub-record data as an unsigned 32-bit integer.

        Returns:
            int: Decoded value.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_uint32()
        if (
            lib.bethkit_subrecord_as_u32(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_f32(self) -> float:
        """Interpret the sub-record data as a 32-bit float.

        Returns:
            float: Decoded value.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_float()
        if (
            lib.bethkit_subrecord_as_f32(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_str(self) -> str:
        """Interpret the sub-record data as a null-terminated UTF-8 string.

        Returns:
            str: Decoded string.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the data is not a valid null-terminated
                string.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_subrecord_as_zstring(self._native_pointer())
        if not ptr:
            _ffi.raise_last_error(lib)
        try:
            return ctypes.string_at(ptr).decode("utf-8")
        finally:
            lib.bethkit_zstring_free(ptr)

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation showing the signature.

        Raises:
            BethkitClosedError: The native owner is closed.
        """

        try:
            sig = self.signature.decode("ascii", errors="replace")
        except BethkitNativeError:
            sig = "?"
        return f"<SubRecord {sig!r}>"
