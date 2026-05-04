"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
from collections.abc import Iterator
from pathlib import Path
from typing import Optional

from .. import _ffi
from .._error import BethkitClosedError, BethkitNotFoundError
from ..enums import Ba2Version, BsaVersion


def _buf_from_bytes(data: bytes) -> ctypes.Array[ctypes.c_uint8]:
    """
    Wrap *data* in a ctypes ``c_uint8`` array for FFI calls.

    Args:
        data (bytes): Byte sequence to wrap.

    Returns:
        ctypes.Array: A ``c_uint8`` array backed by a copy of *data*.
    """

    return (ctypes.c_uint8 * len(data)).from_buffer_copy(data)


class ArchiveEntry:
    """
    A single file entry inside an open archive.

    Instances borrow their data from the parent :class:`Archive` and
    become invalid once the archive is closed or freed.
    """

    _ptr: int
    _parent: Archive

    def __init__(self, ptr: int, parent: Archive) -> None:
        """
        Args:
            ptr (int): Native pointer to the underlying entry object.
            parent (Archive): Owning archive that keeps native memory alive.
        """

        self._ptr = ptr
        self._parent = parent

    @property
    def path(self) -> str:
        """
        Virtual path of the entry as stored in the archive.

        Returns:
            str: Path string, or an empty string when unavailable.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_archive_entry_path(self._ptr)
        if not ptr:
            return ""
        return _ffi.copy_and_free_str(
            ptr, lib.bethkit_archive_entry_path_free, lib
        )

    @property
    def uncompressed_size(self) -> int:
        """
        Uncompressed size of the entry data in bytes.

        Returns:
            int: Byte count of the decompressed content.
        """

        return _ffi.load_lib().bethkit_archive_entry_uncompressed_size(
            self._ptr
        )

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation showing the entry path.
        """

        return f"<ArchiveEntry {self.path!r}>"


class Archive:
    """
    An open Bethesda archive (BSA or BA2) in read-only mode.

    Use as a context manager to guarantee that the native handle is
    freed even on error::

        with Archive.open(path) as arc:
            data = arc.extract("meshes/foo.nif")
    """

    __ptr: int

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI open call.
        """

        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

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
        """
        Open an archive file from disk.

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
        return cls(ptr)

    def close(self) -> None:
        """
        Release the native archive handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_archive_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> Archive:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Close the archive when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    @property
    def format_name(self) -> str:
        """
        Human-readable name of the archive format (e.g. ``"BSA"`` or
        ``"BA2"``).

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
        """
        Total number of file entries in the archive.

        Returns:
            int: Entry count.

        Raises:
            BethkitClosedError: If the archive has been closed.
        """

        return _ffi.load_lib().bethkit_archive_file_count(
            self.__check_open()
        )

    def entry_at(self, index: int) -> ArchiveEntry:
        """
        Return the entry at the given index.

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
        return ArchiveEntry(ptr, self)

    def entries(self) -> Iterator[ArchiveEntry]:
        """
        Iterate over all entries in the archive.

        Yields:
            ArchiveEntry: Each entry in insertion order.

        Raises:
            BethkitClosedError: If the archive has been closed.
        """

        for i in range(self.file_count):
            yield self.entry_at(i)

    def extract(self, path: str) -> Optional[bytes]:
        """
        Extract a single file from the archive by its virtual path.

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
        ptr = lib.bethkit_archive_extract(
            self.__check_open(), _ffi.senc(path), ctypes.byref(out_len)
        )
        if not ptr:
            return None
        try:
            return bytes(ctypes.string_at(ptr, out_len.value))
        finally:
            lib.bethkit_bytes_free(ptr, out_len.value)

    def extract_required(self, path: str) -> bytes:
        """
        Extract a single file, raising when the path is not found.

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
        """
        Extract a single entry and write it to *dest* on disk.

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
        """
        Returns:
            str: Developer-friendly representation showing format and count.
        """

        if not self.__ptr:
            return "<Archive closed>"
        return (
            f"<Archive format={self.format_name!r} files={self.file_count}>"
        )


class BsaWriter:
    """
    Builder for Bethesda Softworks Archive (BSA) files.

    Create a writer, add files, then call :meth:`write_to` to produce
    the BSA on disk.  Use as a context manager to ensure the native
    handle is released::

        with BsaWriter(BsaVersion.SSE) as w:
            w.add("meshes/foo.nif", data)
            w.write_to(output_path)
    """

    __ptr: int

    def __init__(self, version: BsaVersion) -> None:
        """
        Args:
            version (BsaVersion): BSA format version to write.

        Raises:
            BethkitNativeError: If the native writer cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_bsa_writer_new(int(version))
        if not ptr:
            _ffi.raise_last_error(lib)
        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the writer has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("BsaWriter is closed")
        return self.__ptr

    def close(self) -> None:
        """
        Release the native writer handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_bsa_writer_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> BsaWriter:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the writer when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def set_compress(self, compress: bool) -> None:
        """
        Enable or disable default compression for entries.

        Args:
            compress (bool): ``True`` to enable compression by default.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        if lib.bethkit_bsa_writer_set_compress(
            self.__check_open(), compress
        ) != 0:
            _ffi.raise_last_error(lib)

    def set_embed_names(self, embed: bool) -> None:
        """
        Enable or disable embedded file-name strings in the archive.

        Args:
            embed (bool): ``True`` to embed file names.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        if lib.bethkit_bsa_writer_set_embed_names(
            self.__check_open(), embed
        ) != 0:
            _ffi.raise_last_error(lib)

    def add(self, path: str, data: bytes) -> None:
        """
        Add a file to the archive.

        Args:
            path (str): Virtual path used to store the file inside the
                archive.
            data (bytes): File contents.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the entry cannot be added.
        """

        lib = _ffi.load_lib()
        buf = _buf_from_bytes(data)
        if lib.bethkit_bsa_writer_add(
            self.__check_open(), _ffi.senc(path), buf, len(data)
        ) != 0:
            _ffi.raise_last_error(lib)

    def write_to(self, dest: Path) -> None:
        """
        Finalise and write the archive to disk.

        Args:
            dest (Path): Destination file path.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If serialisation or the write fails.
        """

        lib = _ffi.load_lib()
        if lib.bethkit_bsa_writer_write_to(
            self.__check_open(), _ffi.enc(dest)
        ) != 0:
            _ffi.raise_last_error(lib)


class Ba2GnrlWriter:
    """
    Builder for Fallout 4 BA2 general (non-texture) archives.

    Use this for non-texture assets packed in the general BA2 format.
    The interface mirrors :class:`BsaWriter`.
    """

    __ptr: int

    def __init__(self, version: Ba2Version) -> None:
        """
        Args:
            version (Ba2Version): BA2 format version to write.

        Raises:
            BethkitNativeError: If the native writer cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_ba2_gnrl_writer_new(int(version))
        if not ptr:
            _ffi.raise_last_error(lib)
        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the writer has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("Ba2GnrlWriter is closed")
        return self.__ptr

    def close(self) -> None:
        """
        Release the native writer handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_ba2_gnrl_writer_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> Ba2GnrlWriter:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the writer when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def add(self, path: str, data: bytes) -> None:
        """
        Add a file to the archive.

        Args:
            path (str): Virtual path inside the archive.
            data (bytes): File contents.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the entry cannot be added.
        """

        lib = _ffi.load_lib()
        buf = _buf_from_bytes(data)
        if lib.bethkit_ba2_gnrl_writer_add(
            self.__check_open(), _ffi.senc(path), buf, len(data)
        ) != 0:
            _ffi.raise_last_error(lib)

    def write_to(self, dest: Path) -> None:
        """
        Finalise and write the archive to disk.

        Args:
            dest (Path): Destination file path.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If serialisation or the write fails.
        """

        lib = _ffi.load_lib()
        if lib.bethkit_ba2_gnrl_writer_write_to(
            self.__check_open(), _ffi.enc(dest)
        ) != 0:
            _ffi.raise_last_error(lib)


class Ba2Dx10Writer:
    """
    Builder for Fallout 4 BA2 DX10 (texture) archives.

    Use this for texture assets packed in the DX10 BA2 format used by
    Fallout 4.
    """

    __ptr: int

    def __init__(self, version: Ba2Version) -> None:
        """
        Args:
            version (Ba2Version): BA2 format version to write.

        Raises:
            BethkitNativeError: If the native writer cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_ba2_dx10_writer_new(int(version))
        if not ptr:
            _ffi.raise_last_error(lib)
        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the writer has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("Ba2Dx10Writer is closed")
        return self.__ptr

    def close(self) -> None:
        """
        Release the native writer handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_ba2_dx10_writer_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> Ba2Dx10Writer:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the writer when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def add(self, path: str, data: bytes) -> None:
        """
        Add a texture file to the archive.

        Args:
            path (str): Virtual path inside the archive.
            data (bytes): Raw DDS texture data.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the entry cannot be added.
        """

        lib = _ffi.load_lib()
        buf = _buf_from_bytes(data)
        if lib.bethkit_ba2_dx10_writer_add(
            self.__check_open(), _ffi.senc(path), buf, len(data)
        ) != 0:
            _ffi.raise_last_error(lib)

    def write_to(self, dest: Path) -> None:
        """
        Finalise and write the archive to disk.

        Args:
            dest (Path): Destination file path.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If serialisation or the write fails.
        """

        lib = _ffi.load_lib()
        if lib.bethkit_ba2_dx10_writer_write_to(
            self.__check_open(), _ffi.enc(dest)
        ) != 0:
            _ffi.raise_last_error(lib)
