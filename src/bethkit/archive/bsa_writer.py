"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import ClassVar

from .. import _ffi, _ownership
from .._error import BethkitClosedError
from ..enums import BsaVersion
from ._buffer import buffer_from_bytes


class BsaWriter:
    """Builder for Bethesda Softworks Archive (BSA) files.

    Create a writer, add files, then call :meth:`write_to` to produce
    the BSA on disk.  Use as a context manager to ensure the native
    handle is released::

        with BsaWriter(BsaVersion.SSE) as w:
            w.add("meshes/foo.nif", data)
            w.write_to(output_path)
    """

    log: ClassVar[logging.Logger] = logging.getLogger("BsaWriter")
    __ptr: int = 0

    def __init__(self, version: BsaVersion) -> None:
        """Creates an empty native owner with the requested configuration.

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
        """Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the writer has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("BsaWriter is closed")
        return self.__ptr

    def close(self) -> None:
        """Release the native writer handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_bsa_writer_free(pointer)

    def __enter__(self) -> BsaWriter:
        """Returns this open owner for use as a context manager.

        Returns:
            This instance, valid until the context exits or it is closed.

        Raises:
            BethkitClosedError: This owner is already closed or transferred.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Free the writer when exiting the context.

        Args:
            *_: Exception details supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    def set_compress(self, compress: bool) -> None:
        """Enable or disable default compression for entries.

        Args:
            compress (bool): ``True`` to enable compression by default.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        if (
            lib.bethkit_bsa_writer_set_compress(self.__check_open(), compress)
            != 0
        ):
            _ffi.raise_last_error(lib)

    def set_embed_names(self, embed: bool) -> None:
        """Enable or disable embedded file-name strings in the archive.

        Args:
            embed (bool): ``True`` to embed file names.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        if (
            lib.bethkit_bsa_writer_set_embed_names(self.__check_open(), embed)
            != 0
        ):
            _ffi.raise_last_error(lib)

    def add(self, path: str, data: bytes) -> None:
        """Add a file to the archive.

        Args:
            path (str): Virtual path used to store the file inside the
                archive.
            data (bytes): File contents.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the entry cannot be added.
        """

        lib = _ffi.load_lib()
        buf = buffer_from_bytes(data)
        if (
            lib.bethkit_bsa_writer_add(
                self.__check_open(), _ffi.senc(path), buf, len(data)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def write_to(self, dest: Path) -> None:
        """Finalise and write the archive to disk.

        Args:
            dest (Path): Destination file path.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If serialisation or the write fails.
        """

        lib = _ffi.load_lib()
        if (
            lib.bethkit_bsa_writer_write_to(self.__check_open(), _ffi.enc(dest))
            != 0
        ):
            _ffi.raise_last_error(lib)
