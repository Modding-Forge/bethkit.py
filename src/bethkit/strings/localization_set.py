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


class LocalizationSet:
    """
    A combined set of all three localisation tables for a single plugin.

    A :class:`LocalizationSet` bundles the ``.STRINGS``, ``.DLSTRINGS``,
    and ``.ILSTRINGS`` files for a given language.  Load them together
    with :meth:`open`, or create an empty set with :meth:`new` and
    populate it manually.
    """

    log: ClassVar[logging.Logger] = logging.getLogger("LocalizationSet")
    __ptr: int = 0

    def __init__(self) -> None:
        """Rejects direct construction; use open() or new() instead.

        Raises:
            TypeError: This class requires a public factory method.
        """

        raise TypeError("Use LocalizationSet.open() or LocalizationSet.new().")

    @classmethod
    def _from_native(cls, pointer: int) -> LocalizationSet:
        """Adopts a newly allocated, privately owned native handle.

        Args:
            pointer: Valid nonzero handle with ownership transferred here.

        Returns:
            The sole Python owner of the supplied handle.

        Raises:
            ValueError: The supplied pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot adopt a null LocalizationSet handle.")
        instance = cls.__new__(cls)
        instance.__ptr = pointer
        return instance

    def __check_open(self) -> int:
        """
        Returns the native pointer, raising if the handle has been closed.

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
        Creates an empty localisation set.

        Returns:
            LocalizationSet: A new, empty set with no strings loaded.

        Raises:
            BethkitNativeError: If the native set cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_localization_set_new()
        if not ptr:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_localization_set_free
        )

    @classmethod
    def open(cls, plugin_path: Path, language: str) -> LocalizationSet:
        """
        Loads available localisation files for the plugin and language.

        Files are read from the plugin's sibling ``Strings`` directory:
        ``Strings/<plugin_stem>_<language>.{STRINGS,DLSTRINGS,ILSTRINGS}``.
        Each absent file becomes an empty table, allowing partial language
        packs. Existing but unreadable or malformed files raise an error.

        Args:
            plugin_path (Path): Filesystem path to the plugin file.
            language (str): Bethesda filename suffix, such as ``"english"``;
                this is not a BCP 47 language code.

        Returns:
            LocalizationSet: The loaded set.

        Raises:
            BethkitNativeError: An existing string file cannot be read
                or parsed.
            ValueError: The path or language contains a NUL character.
            UnicodeEncodeError: The path or language is not UTF-8 encodable.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_localization_set_open(
            _ffi.enc(plugin_path), _ffi.senc(language)
        )
        if not ptr:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_localization_set_free
        )

    def close(self) -> None:
        """
        Releases the native localisation-set handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_localization_set_free(pointer)

    def clone(self) -> LocalizationSet:
        """Copies all tables into an independently owned localization set.

        Returns:
            A mutable copy whose changes never affect this set.

        Raises:
            BethkitClosedError: This set is closed.
            BethkitNativeError: The native tables could not be copied.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        result = lib.bethkit_localization_set_clone(pointer)
        if not result:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            result,
            LocalizationSet._from_native,
            lib.bethkit_localization_set_free,
        )

    def insert_new(self, kind: StringFileKind, data: bytes) -> int:
        """Allocates a fresh string ID without overwriting existing entries.

        Args:
            kind: Destination string table.
            data: String bytes, without an embedded NUL character.

        Returns:
            The newly allocated unsigned string identifier.

        Raises:
            BethkitClosedError: This set is closed.
            BethkitNativeError: Insertion failed or IDs are exhausted.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        buffer = _buffer.from_bytes(data)
        result = ctypes.c_uint32()
        if (
            lib.bethkit_localization_set_insert_new(
                pointer, int(kind), buffer, len(data), ctypes.byref(result)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return result.value

    def remove(self, kind: StringFileKind, string_id: int) -> bool:
        """Removes one entry, distinguishing absence from native failure.

        Args:
            kind: Table containing the entry.
            string_id: Identifier of the entry to remove.

        Returns:
            Whether an existing entry was removed.

        Raises:
            BethkitClosedError: This set is closed.
            BethkitNativeError: Removal failed.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        status = lib.bethkit_localization_set_remove(
            pointer, int(kind), string_id
        )
        if status == 1:
            return False
        if status != 0:
            _ffi.raise_last_error(lib)
        return True

    def table_to_bytes(self, kind: StringFileKind) -> bytes:
        """Serializes one complete table for coordinated output staging.

        Args:
            kind: Table to serialize.

        Returns:
            Encoded Bethesda string-table bytes.

        Raises:
            BethkitClosedError: This set is closed.
            BethkitNativeError: Serialization failed.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        result = ctypes.c_void_p()
        length = ctypes.c_size_t()
        if (
            lib.bethkit_localization_set_table_to_bytes(
                pointer, int(kind), ctypes.byref(result), ctypes.byref(length)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        try:
            return bytes(ctypes.string_at(result, length.value))
        finally:
            lib.bethkit_bytes_free(
                ctypes.cast(result, ctypes.POINTER(ctypes.c_uint8)),
                length.value,
            )

    def __enter__(self) -> LocalizationSet:
        """Returns this open set for context-managed cleanup.

        Returns:
            This localization set.

        Raises:
            BethkitClosedError: This set is closed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Frees the set when exiting the context.

        Args:
            *_: Exception information supplied by the context manager.
        """

        self.close()

    def __del__(self) -> None:
        """Frees the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    def get(self, kind: StringFileKind, id: int) -> Optional[bytes]:
        """
        Retrieves a string from the specified sub-table by its ID.

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

    def get_str(self, kind: StringFileKind, id: int) -> Optional[str]:
        """
        Retrieves a string from the specified sub-table decoded as UTF-8.

        Args:
            kind (StringFileKind): Which sub-table to query.
            id (int): Numeric string ID.

        Returns:
            Optional[str]: Decoded string without trailing null, or
            ``None`` if not found.

        Raises:
            BethkitClosedError: This set is closed.
            UnicodeDecodeError: The stored bytes are not valid UTF-8.
        """

        raw = self.get(kind, id)
        if raw is None:
            return None
        return raw.rstrip(b"\x00").decode("utf-8")

    def set(self, kind: StringFileKind, id: int, data: bytes) -> None:
        """
        Inserts or overwrite an entry in the specified sub-table.

        Args:
            kind (StringFileKind): Which sub-table to modify.
            id (int): Numeric string ID.
            data (bytes): String payload.

        Raises:
            BethkitClosedError: If the set has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = _buffer.from_bytes(data)
        if (
            lib.bethkit_localization_set_set(
                self.__check_open(), int(kind), id, buf, len(data)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def write(self, plugin_path: Path, language: str) -> None:
        """
        Writes all tables into the plugin's sibling Strings directory.

        Output names follow the layout documented by ``open()``. Missing
        directories are created; existing table files are overwritten. These
        three writes are not atomic. Use ``LocalizationEditor.save_bundle()``
        to publish a plugin and its tables together in a new directory.

        Args:
            plugin_path (Path): Path to the plugin file whose name is
                used to derive the output file names.
            language (str): Bethesda filename suffix, such as ``"english"``.

        Raises:
            BethkitClosedError: If the set has been closed.
            BethkitNativeError: If any write fails.
            ValueError: The path or language contains a NUL character.
            UnicodeEncodeError: The path or language is not UTF-8 encodable.
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
        """Returns a developer-friendly representation of this set.

        Returns:
            str: Developer-friendly representation of the set.
        """

        return "<LocalizationSet>"
