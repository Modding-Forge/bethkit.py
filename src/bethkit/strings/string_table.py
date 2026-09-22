"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import logging
from pathlib import Path
from typing import ClassVar, Optional

from .. import _ffi, _ownership
from .._error import BethkitClosedError
from ..enums import StringFileKind
from . import _buffer


class StringTable:
    """
    A Bethesda localization table in one of three supported string formats.

    Supported files are ``.STRINGS``, ``.DLSTRINGS``, and ``.ILSTRINGS``.

    String tables map numeric IDs to UTF-8 string payloads.  They can be
    loaded from disk with :meth:`open`, or created fresh with :meth:`new`
    and written back with :meth:`write_to_file`.

    Use as a context manager to guarantee that the native handle is
    freed::

        with StringTable.open(path) as tbl:
            text = tbl.get_str(0x0001)
    """

    log: ClassVar[logging.Logger] = logging.getLogger("StringTable")
    __ptr: int = 0

    def __init__(self) -> None:
        """Rejects direct construction; use open() or new() instead.

        Raises:
            TypeError: This class requires a public factory method.
        """

        raise TypeError("Use StringTable.open() or StringTable.new().")

    @classmethod
    def _from_native(cls, pointer: int) -> StringTable:
        """Adopts a newly allocated, privately owned native handle.

        Args:
            pointer: Valid nonzero handle with ownership transferred here.

        Returns:
            The sole Python owner of the supplied handle.

        Raises:
            ValueError: The supplied pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot adopt a null StringTable handle.")
        instance = cls.__new__(cls)
        instance.__ptr = pointer
        return instance

    def __check_open(self) -> int:
        """
        Returns the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the table has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("StringTable is closed")
        return self.__ptr

    @classmethod
    def new(cls, kind: StringFileKind) -> StringTable:
        """
        Creates an empty string table of the given kind.

        Args:
            kind (StringFileKind): Type of string file to create.

        Returns:
            StringTable: A new, empty ``StringTable``.

        Raises:
            BethkitNativeError: If the native table cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_string_table_new(int(kind))
        if not ptr:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_string_table_free
        )

    @classmethod
    def open(cls, path: Path) -> StringTable:
        """
        Opens a string table file from disk.

        Args:
            path (Path): Filesystem path to the string file.

        Returns:
            StringTable: A new ``StringTable`` loaded from *path*.

        Raises:
            BethkitNativeError: If the file cannot be opened or parsed.
            ValueError: The path contains a NUL character.
            UnicodeEncodeError: The path contains an unpaired surrogate.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_string_table_open(_ffi.enc(path))
        if not ptr:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_string_table_free
        )

    def close(self) -> None:
        """
        Releases the native string-table handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_string_table_free(pointer)

    def __enter__(self) -> StringTable:
        """Returns this open table for context-managed cleanup.

        Returns:
            This string table.

        Raises:
            BethkitClosedError: This table is closed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Frees the table when exiting the context.

        Args:
            *_: Exception information supplied by the context manager.
        """

        self.close()

    def __del__(self) -> None:
        """Frees the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    @property
    def kind(self) -> StringFileKind:
        """
        The string-file format of this table.

        Returns:
            StringFileKind: ``STRINGS``, ``DL_STRINGS``, or
            ``IL_STRINGS``.

        Raises:
            BethkitClosedError: If the table has been closed.
        """

        return StringFileKind(
            _ffi.load_lib().bethkit_string_table_kind(self.__check_open())
        )

    def __len__(self) -> int:
        """Returns the number of entries in this table.

        Returns:
            int: Number of entries in the table.

        Raises:
            BethkitClosedError: This table is closed.
        """

        return _ffi.load_lib().bethkit_string_table_len(self.__check_open())

    def get(self, id: int) -> Optional[bytes]:
        """
        Retrieves a string entry as raw bytes by its ID.

        Args:
            id (int): Numeric string ID.

        Returns:
            Optional[bytes]: Raw string bytes, or ``None`` if not found.

        Raises:
            BethkitClosedError: If the table has been closed.
        """

        lib = _ffi.load_lib()
        out_len = ctypes.c_size_t(0)
        ptr = lib.bethkit_string_table_get(
            self.__check_open(), id, ctypes.byref(out_len)
        )
        if not ptr:
            return None
        return bytes(ctypes.string_at(ptr, out_len.value))

    def get_str(self, id: int) -> Optional[str]:
        """
        Retrieves a string entry decoded as UTF-8 by its ID.

        Args:
            id (int): Numeric string ID.

        Returns:
            Optional[str]: Decoded string without trailing null, or
            ``None`` if not found.

        Raises:
            BethkitClosedError: This table is closed.
            UnicodeDecodeError: The stored bytes are not valid UTF-8.
        """

        raw = self.get(id)
        if raw is None:
            return None
        return raw.rstrip(b"\x00").decode("utf-8")

    def insert(self, id: int, data: bytes) -> None:
        """
        Inserts or overwrite an entry with the given ID.

        Args:
            id (int): Numeric string ID.
            data (bytes): String payload (may include trailing null).

        Raises:
            BethkitClosedError: If the table has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = _buffer.from_bytes(data)
        if (
            lib.bethkit_string_table_insert(
                self.__check_open(), id, buf, len(data)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def insert_new(self, data: bytes) -> int:
        """
        Inserts a new entry and return the auto-assigned ID.

        Args:
            data (bytes): String payload.

        Returns:
            int: The ID assigned to the new entry.

        Raises:
            BethkitClosedError: If the table has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = _buffer.from_bytes(data)
        out_id = ctypes.c_uint32(0)
        if (
            lib.bethkit_string_table_insert_new(
                self.__check_open(), buf, len(data), ctypes.byref(out_id)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out_id.value

    def remove(self, id: int) -> bool:
        """
        Removes the entry with the given ID.

        Args:
            id (int): Numeric string ID to remove.

        Returns:
            bool: ``True`` if the entry existed and was removed.

        Raises:
            BethkitClosedError: This table is closed.
        """

        return bool(
            _ffi.load_lib().bethkit_string_table_remove(self.__check_open(), id)
        )

    def write_to_file(self, path: Path) -> None:
        """
        Serializes the table and write it to *path* on disk.

        Args:
            path (Path): Destination file path.

        Raises:
            BethkitClosedError: If the table has been closed.
            BethkitNativeError: If serialisation or the write fails.
            ValueError: The path contains a NUL character.
            UnicodeEncodeError: The path contains an unpaired surrogate.
        """

        lib = _ffi.load_lib()
        if (
            lib.bethkit_string_table_write_to_file(
                self.__check_open(), _ffi.enc(path)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """Returns the table format and entry count or its closed state.

        Returns:
            str: Developer-friendly representation with kind and entry
            count.
        """

        try:
            return f"<StringTable kind={self.kind.name} len={len(self)}>"
        except BethkitClosedError:
            return "<StringTable closed>"
