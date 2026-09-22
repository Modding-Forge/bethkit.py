"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import ClassVar

from .. import _ffi, _ownership
from .._error import BethkitClosedError
from ..enums import Ba2Version
from ._buffer import buffer_from_bytes


class Ba2Dx10Writer:
    """Builder for Fallout 4 BA2 DX10 (texture) archives.

    Use this for texture assets packed in the DX10 BA2 format used by
    Fallout 4.
    """

    log: ClassVar[logging.Logger] = logging.getLogger("Ba2Dx10Writer")
    __ptr: int = 0

    def __init__(self, version: Ba2Version) -> None:
        """Creates an empty native owner with the requested configuration.

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
        """Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the writer has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("Ba2Dx10Writer is closed")
        return self.__ptr

    def close(self) -> None:
        """Release the native writer handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_ba2_dx10_writer_free(pointer)

    def __enter__(self) -> Ba2Dx10Writer:
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

    def add(self, path: str, data: bytes) -> None:
        """Add a texture file to the archive.

        Args:
            path (str): Virtual path inside the archive.
            data (bytes): Raw DDS texture data.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If the entry cannot be added.
        """

        lib = _ffi.load_lib()
        buf = buffer_from_bytes(data)
        if (
            lib.bethkit_ba2_dx10_writer_add(
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
            lib.bethkit_ba2_dx10_writer_write_to(
                self.__check_open(), _ffi.enc(dest)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
