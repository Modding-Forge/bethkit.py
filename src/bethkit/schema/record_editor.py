"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, ClassVar, TypeVar, cast, overload

import pydantic

from .. import _ffi
from .._error import BethkitClosedError, UnsupportedEditError
from .._ownership import finalize
from ..records import _base, _wire
from . import _editor_operations, _editor_values
from ._adoption import adopt_native
from ._record_handle import RecordHandle

_T = TypeVar("_T")

if TYPE_CHECKING:
    from ..plugin.writer import WritableRecord
    from .semantic_context import SemanticContext


class RecordEditor:
    """Owned lossless editor for one schema-covered record."""

    log: ClassVar[logging.Logger] = logging.getLogger("RecordEditor")
    __pointer: int = 0

    def __init__(self) -> None:
        """Rejects direct construction; use the documented native factories.

        Raises:
            TypeError: Native ownership can only originate from a factory.
        """

        raise TypeError("Use RecordEditor factory methods instead.")

    @classmethod
    def _from_native(cls, pointer: int) -> RecordEditor:
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
    def new(
        cls,
        context: SemanticContext,
        record: RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordEditor:
        """Creates an independently owned editor from a live source record.

        Args:
            context: Open semantic runtime used for decoding and validation.
            record: Source record whose owner is open during this call.
            localized: Whether the plugin uses external string tables.

        Returns:
            An editor retaining its own native record and schema ownership.

        Raises:
            BethkitClosedError: The context or source record owner is closed.
            BethkitNativeError: The record cannot be decoded for editing.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_editor_new(
            context._native_pointer(),
            record._native_pointer(),
            localized,
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return adopt_native(
            pointer, cls._from_native, lib.bethkit_record_editor_free
        )

    def __check_open(self) -> int:
        """Checks editor lifetime before borrowing its private pointer.

        Returns:
            The live pointer, still owned by this editor.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
        """

        if not self.__pointer:
            raise BethkitClosedError("RecordEditor has already been closed.")
        return self.__pointer

    @overload
    def set(
        self,
        path: _base.FieldRef[_T],
        value: _T,
        *,
        occurrence: int = 0,
    ) -> None:
        """Sets a generated field using its concrete type and exact address."""

        ...

    @overload
    def set(
        self,
        path: str,
        value: int | float | str | bytes,
        *,
        occurrence: int = 0,
    ) -> None:
        """Sets a legacy schema-path occurrence."""

        ...

    def set(
        self,
        path: str | _base.FieldReference,
        value: object,
        *,
        occurrence: int = 0,
    ) -> None:
        """Replaces one addressed typed value or one legacy path occurrence.

        Args:
            path: Generated FieldRef with an exact address, or a schema path.
            value: Value of the generated field's type; legacy paths accept
                only int, float, str, or bytes, excluding bool.
            occurrence: Zero-based match of a legacy path across the record.
                Must be zero for a FieldRef, which already identifies its scope.

        Raises:
            BethkitClosedError: The editor is closed or consumed by finish().
            TypeError: The path or replacement has an unsupported Python type.
            ValueError: The occurrence, integer range, or JSON value is invalid.
            UnsupportedEditError: The field has no address, its structural
                guard is stale, or the replacement violates the schema.
            BethkitNativeError: A legacy-path replacement fails validation.
            pydantic.ValidationError: A typed field rejects the replacement.
        """

        if isinstance(path, _base.FieldRef):
            if occurrence:
                raise ValueError(
                    "An addressed field already identifies its occurrence."
                )
            reference = cast(_base.FieldRef[object], path)
            if reference.address is None:
                raise UnsupportedEditError(
                    "Select an individual field within the group."
                )
            self._set_json(
                reference.address, _base.encode_replacement(reference, value)
            )
            return
        _editor_operations.set_legacy(
            self.__check_open(), path, value, occurrence
        )

    def snapshot(self) -> _wire.RecordSnapshot:
        """Returns an independent copy with current structural addresses.

        Returns:
            A complete semantic tree, including the current topology guard.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
            RecordDecodeError: Native values could not be decoded.
            pydantic.ValidationError: Native JSON violates the snapshot model.
        """

        return _editor_values.snapshot(self.__check_open())

    def strings_snapshot(self) -> _wire.RecordSnapshot:
        """Returns addressed text leaves from the current edited record.

        Returns:
            A strings-only snapshot with the full record's topology guard.

        Raises:
            BethkitClosedError: The editor has been closed or consumed.
            RecordDecodeError: Native values could not be decoded.
            pydantic.ValidationError: Native JSON violates the snapshot model.
        """

        return _editor_values.snapshot(self.__check_open(), strings_only=True)

    def insert(
        self,
        path: str,
        value: _editor_values.InsertValue,
    ) -> None:
        """Adds a missing optional subrecord through native grammar validation.

        Args:
            path: Exact schema path of the new subrecord.
            value: Scalar, generated payload model, or tagged native value.

        Raises:
            BethkitClosedError: The editor has been closed or consumed.
            UnsupportedEditError: The value or grammar location is invalid.
            TypeError: The replacement contains an unsupported Python value.
            ValueError: A floating-point value is not JSON-representable.
        """

        _editor_values.insert(self.__check_open(), path, value)

    def _set_json(
        self,
        address: _wire.FieldAddress,
        value: dict[str, pydantic.JsonValue],
    ) -> None:
        """Sends an exact-address replacement through native validation.

        Args:
            address: Current location and topology guard.
            value: JSON-compatible tagged replacement.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
            UnsupportedEditError: The address or replacement is invalid.
            ValueError: A floating-point value is not JSON-representable.
        """

        _editor_values.set_json(self.__check_open(), address, value)

    def set_at(
        self, address: _wire.FieldAddress, value: _wire.WireValue
    ) -> None:
        """Replaces an exact scalar, struct, or array through the generic API.

        Args:
            address: Current structural address from an editor or read snapshot.
            value: Tagged replacement subject to native schema validation.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
            UnsupportedEditError: The address is stale or the value is invalid.
            ValueError: A floating-point value is not JSON-representable.
        """

        self._set_json(
            address, value.model_dump(mode="json", exclude_none=True)
        )

    def insert_at(
        self, address: _wire.FieldAddress, value: _wire.WireValue
    ) -> None:
        """Inserts before a sibling without guessing group boundaries.

        Args:
            address: Existing anchor at the intended structural position.
            value: Tagged value of the schema-declared sibling type.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
            UnsupportedEditError: The insertion or repetition scope is invalid.
        """

        _editor_values.insert_at(self.__check_open(), address, value)

    def set_form_id(
        self,
        path: str,
        value: int,
        *,
        occurrence: int = 0,
    ) -> None:
        """Replaces a FormID through the legacy schema-path API.

        Args:
            path: Schema path of a FormID field.
            value: File-local unsigned 32-bit record identity, excluding bool.
            occurrence: Zero-based match of the path across the record.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
            ValueError: The FormID or occurrence is out of range.
            BethkitNativeError: Native validation rejected the replacement.
        """

        _editor_operations.set_form_id(
            self.__check_open(), path, value, occurrence
        )

    def remove(
        self,
        path: str | _wire.FieldAddress | _base.FieldReference,
        *,
        occurrence: int = 0,
    ) -> None:
        """Removes one value where the native schema allows its omission.

        Args:
            path: Legacy schema path, exact FieldAddress, or generated field
                reference. Addresses retain repeated-group and array scope.
            occurrence: Zero-based legacy path match; must be zero when path
                already provides an exact address.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
            ValueError: The occurrence is negative or conflicts with an address.
            UnsupportedEditError: The reference has no address, its guard is
                stale, or removing the addressed value violates the schema.
            BethkitNativeError: Native validation rejected a legacy-path edit.
        """

        _editor_operations.remove(self.__check_open(), path, occurrence)

    def finish(self) -> WritableRecord:
        """Finishes editing and transfers the result into a writable record.

        After success this editor is closed; close() remains safe and all
        editing or snapshot methods raise BethkitClosedError. On a native
        failure the editor remains open, retaining its pending changes.

        Returns:
            An independently owned writable record with the edited content.

        Raises:
            BethkitClosedError: The editor is already closed or consumed.
            BethkitNativeError: Native validation or record encoding failed.
        """

        from ..plugin.writer import WritableRecord

        lib = _ffi.load_lib()
        editor_pointer = self.__check_open()
        pointer = lib.bethkit_record_editor_finish(editor_pointer)
        if not pointer:
            _ffi.raise_last_error(lib)
        self.__pointer = 0
        try:
            lib.bethkit_record_editor_free(editor_pointer)
        except BaseException:
            lib.bethkit_writable_record_free(pointer)
            raise
        return adopt_native(
            pointer,
            WritableRecord._from_native,
            lib.bethkit_writable_record_free,
        )

    def close(self) -> None:
        """Discards pending changes; repeated calls are safe no-ops."""

        if self.__pointer:
            lib = _ffi.load_lib()
            pointer = self.__pointer
            self.__pointer = 0
            lib.bethkit_record_editor_free(pointer)

    def __enter__(self) -> RecordEditor:
        """Returns this open editor for scoped resource management.

        Returns:
            This editor, closed automatically when leaving the context.

        Raises:
            BethkitClosedError: The editor is closed or consumed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Discards pending changes when leaving the context.

        Args:
            *_: Exception context supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Discards any remaining owned editor during finalization."""

        finalize(self.close, self.log)
