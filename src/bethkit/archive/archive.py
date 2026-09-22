"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import logging
from collections.abc import Iterator
from pathlib import Path
from typing import ClassVar, Optional

from .. import _ffi, _ownership
from .._error import BethkitClosedError, BethkitNotFoundError
from .ba2_dx10_writer import Ba2Dx10Writer as Ba2Dx10Writer
from .ba2_gnrl_writer import Ba2GnrlWriter as Ba2GnrlWriter
from .bsa_writer import BsaWriter as BsaWriter
from .entry import ArchiveEntry as ArchiveEntry


class Archive:
    """An open Bethesda archive (BSA or BA2) in read-only mode.

    Use as a context manager to guarantee that the native handle is
    freed even on error::

        with Archive.open(path) as arc:
            data = arc.extract("meshes/foo.nif")
    """

    log: ClassVar[logging.Logger] = logging.getLogger("Archive")
    __ptr: int = 0

    def __init__(self) -> None:
        """Rejects direct construction of an owned native handle.

        Raises:
            TypeError: Always; use this class's public creation methods.
        """

        raise TypeError("Use Archive's public creation methods.")

    @classmethod
    def _from_native(cls, pointer: int) -> Archive:
        """Adopts a native allocation returned by a successful FFI call.

        Args:
            pointer: Nonzero native pointer whose ownership is transferred.

        Returns:
            A wrapper responsible for freeing the allocation exactly once.

        Raises:
            ValueError: The supplied native pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot adopt a null Archive pointer.")
        result = cls.__new__(cls)
        result.__ptr = pointer
        return result

    def __check_open(self) -> int:
        """Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the archive has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("Archive is closed")
        return self.__ptr

    @classmethod
    def open(cls, path: Path) -> Archive:
        """Open an archive file from disk.

        Args:
            path (Path): Filesystem path to the ``.bsa`` or ``.ba2`` file.

        Returns:
            Archive: A new ``Archive`` wrapping the open file.

        Raises:
            BethkitNativeError: If the file cannot be opened or parsed.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_archive_open(_ffi.enc(path))
        if not ptr:
            _ffi.raise_last_error(lib)
        return _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_archive_free
        )

    def close(self) -> None:
        """Release the native archive handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_archive_free(pointer)

    def _check_borrowed(self) -> None:
        """Checks whether the archive still owns its borrowed entries.

        Raises:
            BethkitClosedError: If the archive has already been closed.
        """

        self.__check_open()

    def __enter__(self) -> Archive:
        """Returns this open owner for use as a context manager.

        Returns:
            This instance, valid until the context exits or it is closed.

        Raises:
            BethkitClosedError: This owner is already closed or transferred.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Close the archive when exiting the context.

        Args:
            *_: Exception details supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    @property
    def format_name(self) -> str:
        """Human-readable archive format, such as ``"BSA"`` or ``"BA2"``.

        Returns:
            str: Format identifier string.

        Raises:
            BethkitClosedError: If the archive has been closed.
        """

        lib = _ffi.load_lib()
        raw: Optional[bytes] = lib.bethkit_archive_format_name(
            self.__check_open()
        )
        return raw.decode("utf-8") if raw else ""

    @property
    def file_count(self) -> int:
        """Total number of file entries in the archive.

        Returns:
            int: Entry count.

        Raises:
            BethkitClosedError: If the archive has been closed.
        """

        return _ffi.load_lib().bethkit_archive_file_count(self.__check_open())

    def entry_at(self, index: int) -> ArchiveEntry:
        """Return the entry at the given index.

        Args:
            index (int): Zero-based entry index.

        Returns:
            ArchiveEntry: Borrowed entry for the given index.

        Raises:
            BethkitClosedError: If the archive has been closed.
            BethkitNativeError: If *index* is out of range.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_archive_entry_get(self.__check_open(), index)
        if not ptr:
            _ffi.raise_last_error(lib)
        return ArchiveEntry._from_native(ptr, self)

    def entries(self) -> Iterator[ArchiveEntry]:
        """Iterate over all entries in the archive.

        Yields:
            ArchiveEntry: Each entry in insertion order.

        Raises:
            BethkitClosedError: If the archive has been closed.
        """

        for i in range(self.file_count):
            yield self.entry_at(i)

    def extract(self, path: str) -> Optional[bytes]:
        """Extract a single file from the archive by its virtual path.

        Returns ``None`` when the path is not found.

        Args:
            path (str): Virtual path of the entry to extract.

        Returns:
            Optional[bytes]: Decompressed file data, or ``None`` if the
            path does not exist in the archive.

        Raises:
            BethkitClosedError: If the archive has been closed.
            BethkitNativeError: If extraction fails for a reason other than
                a missing path.
        """

        lib = _ffi.load_lib()
        out_len = ctypes.c_size_t(0)
        ptr = ctypes.POINTER(ctypes.c_uint8)()
        status = lib.bethkit_archive_extract_status(
            self.__check_open(),
            _ffi.senc(path),
            ctypes.byref(ptr),
            ctypes.byref(out_len),
        )
        if status == 1:
            return None
        if status != 0:
            _ffi.raise_last_error(lib)
        try:
            return bytes(ctypes.string_at(ptr, out_len.value))
        finally:
            lib.bethkit_bytes_free(ptr, out_len.value)

    def extract_required(self, path: str) -> bytes:
        """Extract a single file, raising when the path is not found.

        Args:
            path (str): Virtual path of the entry to extract.

        Returns:
            bytes: Decompressed file data.

        Raises:
            BethkitClosedError: If the archive has been closed.
            BethkitNotFoundError: If the path is not in the archive.
            BethkitNativeError: If extraction fails.
        """

        data = self.extract(path)
        if data is None:
            raise BethkitNotFoundError(f"Entry not found in archive: {path!r}")
        return data

    def extract_to_file(self, path: str, dest: Path) -> None:
        """Extract a single entry and write it to *dest* on disk.

        Args:
            path (str): Virtual path of the entry to extract.
            dest (Path): Destination file path.

        Raises:
            BethkitClosedError: If the archive has been closed.
            BethkitNativeError: If the path is not found or the write fails.
        """

        lib = _ffi.load_lib()
        rc = lib.bethkit_archive_extract_to_file(
            self.__check_open(), _ffi.senc(path), _ffi.enc(dest)
        )
        if rc != 0:
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation showing format and count.
        """

        if not self.__ptr:
            return "<Archive closed>"
        return f"<Archive format={self.format_name!r} files={self.file_count}>"
