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
from ..records import _schema
from ._adoption import adopt_native
from .schema_manifest import SchemaManifest


class SchemaPackage:
    """Owned validated schema package for one game."""

    log: ClassVar[logging.Logger] = logging.getLogger("SchemaPackage")
    __pointer: int = 0

    def __init__(self) -> None:
        """Rejects direct construction; use the documented native factories.

        Raises:
            TypeError: Native ownership can only originate from a factory.
        """

        raise TypeError("Use SchemaPackage factory methods instead.")

    @classmethod
    def _from_native(cls, pointer: int) -> SchemaPackage:
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
    def open(cls, path: Path) -> SchemaPackage:
        """Loads and validates one game's `.bkschema` package.

        Args:
            path: Schema package file to read.

        Returns:
            An owned package accepted by the native schema validator.

        Raises:
            BethkitNativeError: The package cannot be read or validated.
            BethkitLibraryNotFoundError: No compatible native library is found.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_package_open(_ffi.enc(path))
        if not pointer:
            _ffi.raise_last_error(lib)
        return adopt_native(
            pointer, cls._from_native, lib.bethkit_schema_package_free
        )

    def _native_pointer(self) -> int:
        """Checks package lifetime before borrowing its private pointer.

        Returns:
            The live pointer, still owned by this package.

        Raises:
            BethkitClosedError: The package has already been closed.
        """

        if not self.__pointer:
            raise BethkitClosedError("SchemaPackage has already been closed.")
        return self.__pointer

    def manifest(self) -> SchemaManifest:
        """Returns release provenance independently of this native handle.

        Returns:
            An immutable copy of the package's provenance and requirements.

        Raises:
            BethkitClosedError: The package has already been closed.
            BethkitNativeError: The manifest cannot be exported.
            pydantic.ValidationError: Native JSON violates the manifest model.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_package_manifest_json(
            self._native_pointer()
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return SchemaManifest.model_validate_json(text)

    def graph(self) -> _schema.SchemaGraph:
        """Exports the validated graph for offline model generation.

        Returns:
            An independent schema graph, including record and value nodes.

        Raises:
            BethkitClosedError: The package has already been closed.
            BethkitNativeError: The graph cannot be exported.
            pydantic.ValidationError: Native JSON violates the graph contract.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_package_graph_json(self._native_pointer())
        if not pointer:
            _ffi.raise_last_error(lib)
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return _schema.SchemaGraph.model_validate_json(text)

    def close(self) -> None:
        """Releases the native package; repeated calls are safe no-ops."""

        if self.__pointer:
            lib = _ffi.load_lib()
            pointer = self.__pointer
            self.__pointer = 0
            lib.bethkit_schema_package_free(pointer)

    def __enter__(self) -> SchemaPackage:
        """Returns this open package for scoped resource management.

        Returns:
            This package, closed automatically on context exit.

        Raises:
            BethkitClosedError: The package has already been closed.
        """

        self._native_pointer()
        return self

    def __exit__(self, *_: object) -> None:
        """Closes this package when leaving its context.

        Args:
            *_: Exception context supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned package during finalization."""

        finalize(self.close, self.log)
