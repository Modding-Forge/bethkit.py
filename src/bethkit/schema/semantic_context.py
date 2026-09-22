"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from typing import ClassVar

from .. import _ffi
from .._error import BethkitClosedError, RecordDecodeError
from .._ownership import finalize
from ..records import _wire
from ._record_handle import RecordHandle
from .record_editor import RecordEditor
from .record_view import RecordView
from .schema_package import SchemaPackage


class SemanticContext:
    """Owned semantic runtime for a schema package."""

    log: ClassVar[logging.Logger] = logging.getLogger("SemanticContext")
    __pointer: int = 0

    def __init__(self, package: SchemaPackage) -> None:
        """Creates a runtime that retains its own schema ownership.

        Args:
            package: Validated, open native schema package.

        Raises:
            BethkitClosedError: The package is already closed.
            BethkitNativeError: The native runtime cannot be created.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_semantic_context_new(package._native_pointer())
        if not pointer:
            _ffi.raise_last_error(lib)
        self.__pointer = pointer

    def _native_pointer(self) -> int:
        """Checks runtime lifetime before borrowing its private pointer.

        Returns:
            The live pointer, still owned by this runtime.

        Raises:
            BethkitClosedError: The runtime has already been closed.
        """

        if not self.__pointer:
            raise BethkitClosedError("SemanticContext has already been closed.")
        return self.__pointer

    def view(
        self,
        record: RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordView:
        """Creates an independently owned generic record view.

        Args:
            record: Source record with an open owner during this call.
            localized: Whether the plugin uses external string tables.

        Returns:
            A lazily decoded view that outlives the source record and runtime.

        Raises:
            BethkitClosedError: The runtime or record owner is closed.
            BethkitNativeError: The record cannot be decoded with this schema.
        """

        return RecordView.new(self, record, localized=localized)

    def edit(
        self,
        record: RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordEditor:
        """Creates an independently owned lossless editor for a record.

        Args:
            record: Source record with an open owner during this call.
            localized: Whether the plugin uses external string tables.

        Returns:
            An editor retaining its own record and schema ownership.

        Raises:
            BethkitClosedError: The runtime or record owner is closed.
            BethkitNativeError: The record cannot be decoded for editing.
        """

        return RecordEditor.new(self, record, localized=localized)

    def snapshot(
        self,
        record: RecordHandle,
        *,
        localized: bool = False,
    ) -> _wire.RecordSnapshot:
        """Copies one complete semantic value tree with structural addresses.

        Args:
            record: Source record whose owner must remain open for this call.
            localized: Whether the source plugin uses external string tables.

        Returns:
            An immutable snapshot independent of all native handle lifetimes.

        Raises:
            BethkitClosedError: A required handle or its owner is closed.
            RecordDecodeError: The native runtime cannot decode this record.
            pydantic.ValidationError: Native JSON violates the snapshot model.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_semantic_snapshot_json(
            self._native_pointer(),
            record._native_pointer(),
            localized,
        )
        if not pointer:
            raise RecordDecodeError(_ffi.last_error(lib))
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return _wire.RecordSnapshot.model_validate_json(text)

    def strings_snapshot(
        self,
        record: RecordHandle,
        *,
        localized: bool = False,
    ) -> _wire.RecordSnapshot:
        """Copies translatable leaves without exporting unrelated payloads.

        Args:
            record: Source record whose owner remains open for this call.
            localized: Whether text uses external string tables.

        Returns:
            A strings-only snapshot retaining exact native editing addresses.

        Raises:
            BethkitClosedError: A required handle or its owner is closed.
            RecordDecodeError: The native runtime cannot decode this record.
            pydantic.ValidationError: Native JSON violates the snapshot model.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_semantic_strings_snapshot_json(
            self._native_pointer(), record._native_pointer(), localized
        )
        if not pointer:
            raise RecordDecodeError(_ffi.last_error(lib))
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return _wire.RecordSnapshot.model_validate_json(text)

    def validate(
        self,
        record: RecordHandle,
        *,
        localized: bool = False,
        xedit_compatible: bool = False,
    ) -> _wire.ValidationReport:
        """Validates strict or xEdit-compatible required-field rules.

        Args:
            record: Source record with a live owner.
            localized: Whether strings use external tables.
            xedit_compatible: Report missing required fields as warnings.

        Returns:
            A structured report without discarding warnings or source errors.

        Raises:
            BethkitClosedError: A required handle is closed.
            BethkitNativeError: The schema or validation request is invalid.
            pydantic.ValidationError: Native JSON violates the report contract.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_semantic_validate_json(
            self._native_pointer(),
            record._native_pointer(),
            localized,
            int(xedit_compatible),
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return _wire.ValidationReport.model_validate_json(text)

    def close(self) -> None:
        """Releases the native context; repeated calls are safe no-ops."""

        if self.__pointer:
            lib = _ffi.load_lib()
            pointer = self.__pointer
            self.__pointer = 0
            lib.bethkit_semantic_context_free(pointer)

    def __enter__(self) -> SemanticContext:
        """Returns this open runtime for scoped resource management.

        Returns:
            This runtime, closed automatically on context exit.

        Raises:
            BethkitClosedError: The runtime has already been closed.
        """

        self._native_pointer()
        return self

    def __exit__(self, *_: object) -> None:
        """Closes this runtime when leaving its context.

        Args:
            *_: Exception context supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned runtime during finalization."""

        finalize(self.close, self.log)
