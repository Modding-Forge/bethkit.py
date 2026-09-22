"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import logging
from typing import ClassVar

from .. import _ffi, _ownership
from .._error import BethkitClosedError, BethkitOwnershipError
from ._signature import signature_buffer


class WritableRecord:
    r"""A plugin record under construction.

    Create via :meth:`new`, add sub-records with :meth:`add_subrecord`,
    then hand the record off to a :class:`WritableGroup` with
    :meth:`WritableGroup.add_record`.  Ownership transfers on that call
    and this wrapper becomes invalid.

    Use as a context manager to free the handle if the record is never
    added to a group::

        with WritableRecord.new(b"NPC_") as rec:
            rec.add_subrecord(b"EDID", b"MyNPC\x00")
            group.add_record(rec)
    """

    log: ClassVar[logging.Logger] = logging.getLogger("WritableRecord")
    __ptr: int = 0

    def __init__(self) -> None:
        """Rejects direct construction of an owned native handle.

        Raises:
            TypeError: Always; use this class's public creation methods.
        """

        raise TypeError("Use WritableRecord's public creation methods.")

    @classmethod
    def _from_native(cls, pointer: int) -> WritableRecord:
        """Adopts a native allocation returned by a successful FFI call.

        Args:
            pointer: Nonzero native pointer whose ownership is transferred.

        Returns:
            A wrapper responsible for freeing the allocation exactly once.

        Raises:
            ValueError: The supplied native pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot adopt a null WritableRecord pointer.")
        result = cls.__new__(cls)
        result.__ptr = pointer
        return result

    def __check_open(self) -> int:
        """Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the record has been closed or transferred.
        """

        if not self.__ptr:
            raise BethkitClosedError("WritableRecord is closed or transferred")
        return self.__ptr

    def _native_pointer(self) -> int:
        """Returns a borrowed pointer without transferring this record.

        Returns:
            The pointer owned by this open record wrapper.

        Raises:
            BethkitClosedError: The record was closed or transferred.
        """

        return self.__check_open()

    def _transfer_ptr(self) -> int:
        """Transfer ownership to the caller.

        Returns:
            int: The raw native pointer.

        Raises:
            BethkitOwnershipError: If the record has already been transferred
                or closed.
        """

        if not self.__ptr:
            raise BethkitOwnershipError(
                "WritableRecord has already been transferred or closed"
            )
        ptr = self.__ptr
        self.__ptr = 0
        return ptr

    @classmethod
    def new(
        cls,
        signature: bytes | str,
        flags: int = 0,
        form_id: int = 0,
        form_version: int = 44,
    ) -> WritableRecord:
        """Create a new writable record with the given header fields.

        Args:
            signature (bytes | str): Four-byte record type signature.
            flags (int): Record header flags bitmask. Defaults to ``0``.
            form_id (int): Raw FormID. Defaults to ``0``.
            form_version (int): Form version. Defaults to ``44``.

        Returns:
            WritableRecord: A new, empty record.

        Raises:
            BethkitNativeError: If the native record cannot be created.
            ValueError: If *signature* is not exactly 4 bytes.
        """

        buf = signature_buffer(signature)
        lib = _ffi.load_lib()
        ptr = lib.bethkit_writable_record_new(buf, flags, form_id, form_version)
        if not ptr:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_writable_record_free
        )

    def close(self) -> None:
        """Release the native record handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_writable_record_free(pointer)

    def __enter__(self) -> WritableRecord:
        """Returns this open owner for use as a context manager.

        Returns:
            This instance, valid until the context exits or it is closed.

        Raises:
            BethkitClosedError: This owner is already closed or transferred.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Free the record when exiting the context.

        Args:
            *_: Exception details supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    def add_subrecord(self, signature: bytes | str, data: bytes) -> None:
        """Append a sub-record to this record.

        Args:
            signature (bytes | str): Four-byte sub-record type signature.
            data (bytes): Raw sub-record payload.

        Raises:
            BethkitClosedError: If the record has been closed or transferred.
            BethkitNativeError: If the native call fails.
            ValueError: If *signature* is not exactly 4 bytes.
        """

        lib = _ffi.load_lib()
        sig_buf = signature_buffer(signature)
        data_buf = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
        if (
            lib.bethkit_writable_record_add_subrecord(
                self.__check_open(), sig_buf, data_buf, len(data)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly ownership state without native handles.
        """

        if not self.__ptr:
            return "<WritableRecord transferred>"
        return "<WritableRecord open>"
