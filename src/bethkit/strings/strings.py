"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
from pathlib import Path
from typing import Optional

from .. import _ffi
from .._error import BethkitClosedError
from ..enums import StringFileKind


def _buf_from_bytes(data: bytes) -> ctypes.Array[ctypes.c_uint8]:
    """
    Wrap *data* in a ctypes ``c_uint8`` array for FFI calls.

    Args:
        data (bytes): Byte sequence to wrap.

    Returns:
        ctypes.Array: A ``c_uint8`` array backed by a copy of *data*.
    """

    return (ctypes.c_uint8 * len(data)).from_buffer_copy(data)


class StringTable:
    """
    A Bethesda string localisation table (``.STRINGS``, ``.DLSTRINGS``,
    or ``.ILSTRINGS`` files).

    String tables map numeric IDs to UTF-8 string payloads.  They can be
    loaded from disk with :meth:`open`, or created fresh with :meth:`new`
    and written back with :meth:`write_to_file`.

    Use as a context manager to guarantee that the native handle is
    freed::

        with StringTable.open(path) as tbl:
            text = tbl.get_str(0x0001)
    """

    __ptr: int

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI open/new call.
        """

        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

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
        Create an empty string table of the given kind.

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
        return cls(ptr)

    @classmethod
    def open(cls, path: Path) -> StringTable:
        """
        Open a string table file from disk.

        Args:
            path (Path): Filesystem path to the string file.

        Returns:
            StringTable: A new ``StringTable`` loaded from *path*.

        Raises:
            BethkitNativeError: If the file cannot be opened or parsed.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_string_table_open(_ffi.enc(path))
        if not ptr:
            _ffi.raise_last_error(lib)
        return cls(ptr)

    def close(self) -> None:
        """
        Release the native string-table handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_string_table_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> StringTable:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the table when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

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
        """
        Returns:
            int: Number of entries in the table.
        """

        return _ffi.load_lib().bethkit_string_table_len(
            self.__check_open()
        )

    def get(self, id: int) -> Optional[bytes]:
        """
        Retrieve a string entry as raw bytes by its ID.

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
        Retrieve a string entry decoded as UTF-8 by its ID.

        Args:
            id (int): Numeric string ID.

        Returns:
            Optional[str]: Decoded string without trailing null, or
            ``None`` if not found.
        """

        raw = self.get(id)
        if raw is None:
            return None
        return raw.rstrip(b"\x00").decode("utf-8")

    def insert(self, id: int, data: bytes) -> None:
        """
        Insert or overwrite an entry with the given ID.

        Args:
            id (int): Numeric string ID.
            data (bytes): String payload (may include trailing null).

        Raises:
            BethkitClosedError: If the table has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = _buf_from_bytes(data)
        if lib.bethkit_string_table_insert(
            self.__check_open(), id, buf, len(data)
        ) != 0:
            _ffi.raise_last_error(lib)

    def insert_new(self, data: bytes) -> int:
        """
        Insert a new entry and return the auto-assigned ID.

        Args:
            data (bytes): String payload.

        Returns:
            int: The ID assigned to the new entry.

        Raises:
            BethkitClosedError: If the table has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = _buf_from_bytes(data)
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
        Remove the entry with the given ID.

        Args:
            id (int): Numeric string ID to remove.

        Returns:
            bool: ``True`` if the entry existed and was removed.
        """

        return bool(
            _ffi.load_lib().bethkit_string_table_remove(
                self.__check_open(), id
            )
        )

    def write_to_file(self, path: Path) -> None:
        """
        Serialise the table and write it to *path* on disk.

        Args:
            path (Path): Destination file path.

        Raises:
            BethkitClosedError: If the table has been closed.
            BethkitNativeError: If serialisation or the write fails.
        """

        lib = _ffi.load_lib()
        if lib.bethkit_string_table_write_to_file(
            self.__check_open(), _ffi.enc(path)
        ) != 0:
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with kind and entry
            count.
        """

        try:
            return f"<StringTable kind={self.kind.name} len={len(self)}>"
        except BethkitClosedError:
            return "<StringTable closed>"


class LocalizationSet:
    """
    A combined set of all three localisation tables for a single plugin.

    A :class:`LocalizationSet` bundles the ``.STRINGS``, ``.DLSTRINGS``,
    and ``.ILSTRINGS`` files for a given language.  Load them together
    with :meth:`open`, or create an empty set with :meth:`new` and
    populate it manually.
    """

    __ptr: int

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI open/new call.
        """

        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the set has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("LocalizationSet is closed")
        return self.__ptr

    @classmethod
    def new(cls) -> LocalizationSet:
        """
        Create an empty localisation set.

        Returns:
            LocalizationSet: A new, empty set with no strings loaded.

        Raises:
            BethkitNativeError: If the native set cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_localization_set_new()
        if not ptr:
            _ffi.raise_last_error(lib)
        return cls(ptr)

    @classmethod
    def open(
        cls, plugin_path: Path, language: str
    ) -> LocalizationSet:
        """
        Load all localisation files for the given plugin and language.

        The method looks for ``<plugin_stem>_<language>.STRINGS`` and
        sibling ``.DLSTRINGS`` / ``.ILSTRINGS`` files next to the plugin.

        Args:
            plugin_path (Path): Filesystem path to the plugin file.
            language (str): BCP 47-style language code
                (e.g. ``"english"``).

        Returns:
            LocalizationSet: The loaded set.

        Raises:
            BethkitNativeError: If any required string file cannot be
                opened.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_localization_set_open(
            _ffi.enc(plugin_path), _ffi.senc(language)
        )
        if not ptr:
            _ffi.raise_last_error(lib)
        return cls(ptr)

    def close(self) -> None:
        """
        Release the native localisation-set handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_localization_set_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> LocalizationSet:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the set when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def get(
        self, kind: StringFileKind, id: int
    ) -> Optional[bytes]:
        """
        Retrieve a string from the specified sub-table by its ID.

        Args:
            kind (StringFileKind): Which sub-table to query.
            id (int): Numeric string ID.

        Returns:
            Optional[bytes]: Raw string bytes, or ``None`` if not found.

        Raises:
            BethkitClosedError: If the set has been closed.
        """

        lib = _ffi.load_lib()
        out_len = ctypes.c_size_t(0)
        ptr = lib.bethkit_localization_set_get(
            self.__check_open(), int(kind), id, ctypes.byref(out_len)
        )
        if not ptr:
            return None
        return bytes(ctypes.string_at(ptr, out_len.value))

    def get_str(
        self, kind: StringFileKind, id: int
    ) -> Optional[str]:
        """
        Retrieve a string from the specified sub-table decoded as UTF-8.

        Args:
            kind (StringFileKind): Which sub-table to query.
            id (int): Numeric string ID.

        Returns:
            Optional[str]: Decoded string without trailing null, or
            ``None`` if not found.
        """

        raw = self.get(kind, id)
        if raw is None:
            return None
        return raw.rstrip(b"\x00").decode("utf-8")

    def set(
        self, kind: StringFileKind, id: int, data: bytes
    ) -> None:
        """
        Insert or overwrite an entry in the specified sub-table.

        Args:
            kind (StringFileKind): Which sub-table to modify.
            id (int): Numeric string ID.
            data (bytes): String payload.

        Raises:
            BethkitClosedError: If the set has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = _buf_from_bytes(data)
        if (
            lib.bethkit_localization_set_set(
                self.__check_open(), int(kind), id, buf, len(data)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def write(
        self, plugin_path: Path, language: str
    ) -> None:
        """
        Write all sub-tables to disk next to *plugin_path*.

        Args:
            plugin_path (Path): Path to the plugin file whose name is
                used to derive the output file names.
            language (str): BCP 47-style language code
                (e.g. ``"english"``).

        Raises:
            BethkitClosedError: If the set has been closed.
            BethkitNativeError: If any write fails.
        """

        lib = _ffi.load_lib()
        if (
            lib.bethkit_localization_set_write(
                self.__check_open(),
                _ffi.enc(plugin_path),
                _ffi.senc(language),
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation of the set.
        """

        return "<LocalizationSet>"
