"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from typing import ClassVar

from .. import _ffi, _ownership
from .._error import BethkitClosedError, BethkitOwnershipError
from ._signature import signature_buffer
from .writable_record import WritableRecord


class WritableGroup:
    """A plugin group under construction.

    Add records with :meth:`add_record` and sub-groups with
    :meth:`add_group`, then hand the group off to a
    :class:`PluginWriter` with :meth:`PluginWriter.add_group`.
    Ownership transfers on that call.
    """

    log: ClassVar[logging.Logger] = logging.getLogger("WritableGroup")
    __ptr: int = 0

    def __init__(self) -> None:
        """Rejects direct construction of an owned native handle.

        Raises:
            TypeError: Always; use this class's public creation methods.
        """

        raise TypeError("Use WritableGroup's public creation methods.")

    @classmethod
    def _from_native(cls, pointer: int) -> WritableGroup:
        """Adopts a native allocation returned by a successful FFI call.

        Args:
            pointer: Nonzero native pointer whose ownership is transferred.

        Returns:
            A wrapper responsible for freeing the allocation exactly once.

        Raises:
            ValueError: The supplied native pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot adopt a null WritableGroup pointer.")
        result = cls.__new__(cls)
        result.__ptr = pointer
        return result

    def __check_open(self) -> int:
        """Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the group has been closed or transferred.
        """

        if not self.__ptr:
            raise BethkitClosedError("WritableGroup is closed or transferred")
        return self.__ptr

    def _transfer_ptr(self) -> int:
        """Transfer ownership to the caller.

        Returns:
            int: The raw native pointer.

        Raises:
            BethkitOwnershipError: If the group has already been transferred
                or closed.
        """

        if not self.__ptr:
            raise BethkitOwnershipError(
                "WritableGroup has already been transferred or closed"
            )
        ptr = self.__ptr
        self.__ptr = 0
        return ptr

    @classmethod
    def new(cls, label: bytes | str, group_type: int = 0) -> WritableGroup:
        """Create a new writable group.

        Args:
            label (bytes | str): Four-byte group label (top-level
                groups use a record-type signature).
            group_type (int): Numeric group type. Defaults to ``0``
                (top-level).

        Returns:
            WritableGroup: A new, empty group.

        Raises:
            BethkitNativeError: If the native group cannot be created.
            ValueError: If *label* is not exactly 4 bytes.
        """

        lib = _ffi.load_lib()
        buf = signature_buffer(label)
        ptr = lib.bethkit_writable_group_new(buf, group_type)
        if not ptr:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_writable_group_free
        )

    def close(self) -> None:
        """Release the native group handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_writable_group_free(pointer)

    def __enter__(self) -> WritableGroup:
        """Returns this open owner for use as a context manager.

        Returns:
            This instance, valid until the context exits or it is closed.

        Raises:
            BethkitClosedError: This owner is already closed or transferred.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Free the group when exiting the context.

        Args:
            *_: Exception details supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    def add_record(self, record: WritableRecord) -> None:
        """Append a record to this group, transferring ownership.

        After this call *record* is invalid.

        Args:
            record (WritableRecord): The record to add.

        Raises:
            BethkitClosedError: If this group has been closed or transferred.
            BethkitOwnershipError: If *record* has already been transferred
                or closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        group_ptr = self.__check_open()
        rec_ptr = record._transfer_ptr()
        if lib.bethkit_writable_group_add_record(group_ptr, rec_ptr) != 0:
            _ffi.raise_last_error(lib)

    def add_group(self, child: WritableGroup) -> None:
        """Append a sub-group to this group, transferring ownership.

        After this call *child* is invalid.

        Args:
            child (WritableGroup): The sub-group to add.

        Raises:
            BethkitClosedError: If this group has been closed or transferred.
            BethkitOwnershipError: If *child* has already been transferred
                or closed.
            BethkitNativeError: If the native call fails.
            ValueError: The child is this same group.
        """

        lib = _ffi.load_lib()
        group_ptr = self.__check_open()
        if child is self:
            raise ValueError("A writable group cannot contain itself.")
        child_ptr = child._transfer_ptr()
        if lib.bethkit_writable_group_add_group(group_ptr, child_ptr) != 0:
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly ownership state without native handles.
        """

        if not self.__ptr:
            return "<WritableGroup transferred>"
        return "<WritableGroup open>"
