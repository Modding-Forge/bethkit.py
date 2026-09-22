"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import ClassVar

from .. import _ffi
from .._error import BethkitClosedError
from .._ownership import finalize
from ..enums import Game
from ._adoption import adopt_native
from .schema_package import SchemaPackage


class SchemaCatalog:
    """Owned catalog containing zero or more game schema packages."""

    log: ClassVar[logging.Logger] = logging.getLogger("SchemaCatalog")
    __pointer: int = 0

    def __init__(self) -> None:
        """Rejects direct construction; use the documented native factories.

        Raises:
            TypeError: Native ownership can only originate from a factory.
        """

        raise TypeError("Use SchemaCatalog factory methods instead.")

    @classmethod
    def _from_native(cls, pointer: int) -> SchemaCatalog:
        """Adopts a non-null allocation returned by a trusted native factory.

        Args:
            pointer: Newly allocated native handle transferred to this wrapper.

        Returns:
            A wrapper owning the native allocation.

        Raises:
            ValueError: The pointer is null.
        """

        if not pointer:
            raise ValueError("A native factory returned a null handle.")
        instance = cls.__new__(cls)
        instance.__pointer = pointer
        return instance

    @classmethod
    def embedded(cls) -> SchemaCatalog:
        """Loads the catalog embedded in an official native library.

        Returns:
            An owned catalog containing the library's bundled game packages.

        Raises:
            BethkitNativeError: The embedded catalog cannot be loaded.
            BethkitLibraryNotFoundError: No compatible native library is found.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_catalog_embedded()
        if not pointer:
            _ffi.raise_last_error(lib)
        return adopt_native(
            pointer, cls._from_native, lib.bethkit_schema_catalog_free
        )

    @classmethod
    def open(cls, path: Path) -> SchemaCatalog:
        """Loads a `.bkschemas` catalog from disk.

        Args:
            path: Catalog file containing one or more game schema packages.

        Returns:
            An owned validated catalog.

        Raises:
            BethkitNativeError: The file cannot be read or validated.
            BethkitLibraryNotFoundError: No compatible native library is found.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_catalog_open(_ffi.enc(path))
        if not pointer:
            _ffi.raise_last_error(lib)
        return adopt_native(
            pointer, cls._from_native, lib.bethkit_schema_catalog_free
        )

    def package(self, game: Game) -> SchemaPackage:
        """Returns an independently owned package handle for a game.

        Args:
            game: Game whose schema package must be present in this catalog.

        Returns:
            A package that remains valid after closing this catalog.

        Raises:
            BethkitClosedError: The catalog has already been closed.
            BethkitNativeError: The catalog does not contain the requested game.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_catalog_package(
            self.__check_open(), int(game)
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return adopt_native(
            pointer, SchemaPackage._from_native, lib.bethkit_schema_package_free
        )

    def __check_open(self) -> int:
        """Checks catalog lifetime before borrowing its private pointer.

        Returns:
            The live pointer, still owned by this catalog.

        Raises:
            BethkitClosedError: The catalog has already been closed.
        """

        if not self.__pointer:
            raise BethkitClosedError("SchemaCatalog has already been closed.")
        return self.__pointer

    def close(self) -> None:
        """Releases the native catalog; repeated calls are safe no-ops."""

        if self.__pointer:
            lib = _ffi.load_lib()
            pointer = self.__pointer
            self.__pointer = 0
            lib.bethkit_schema_catalog_free(pointer)

    def __enter__(self) -> SchemaCatalog:
        """Returns this open catalog for scoped resource management.

        Returns:
            This catalog, closed automatically on context exit.

        Raises:
            BethkitClosedError: The catalog has already been closed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Closes this catalog when leaving its context.

        Args:
            *_: Exception context supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned catalog during finalization."""

        finalize(self.close, self.log)
