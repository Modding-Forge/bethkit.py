"""
Copyright (c) Modding Forge

Versioned schema packages and semantic record views.
"""

from __future__ import annotations

import ctypes
import json
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    Optional,
    Protocol,
    TypeVar,
    cast,
    overload,
)

import pydantic
from pydantic import BaseModel, ConfigDict

from .. import _ffi
from .._error import BethkitClosedError, RecordDecodeError, UnsupportedEditError
from .._ffi import BethkitFieldValue
from ..enums import FieldValueKind, Game
from ..records import _base, _schema, _values, _wire

_T = TypeVar("_T")

if TYPE_CHECKING:
    from ..plugin.writer import WritableRecord


class TypedFormId(BaseModel, frozen=True):
    """A FormID and the record signatures it may reference."""

    raw: int
    """File-local unsigned record identifier."""
    allowed_sigs: tuple[bytes, ...]
    """Schema-declared target record signatures."""


class EnumVal(BaseModel, frozen=True):
    """A decoded enumeration value."""

    value: int
    """Encoded enumeration value, including unknown values."""
    name: Optional[str]
    """Declared value label, when known."""


class FlagsVal(BaseModel, frozen=True):
    """A decoded bit-flags value."""

    raw_value: int
    """Complete encoded bitmask, including unknown bits."""
    active_names: tuple[str, ...]
    """Labels of active schema-declared flag bits."""


class DecoderRequirement(BaseModel, frozen=True):
    """One custom decoder required by a schema package."""

    id: str
    """Stable decoder identifier."""

    minimum_version: int
    """Minimum compatible decoder implementation version."""


class HandlerRequirement(BaseModel, frozen=True):
    """One semantic callback handler required by a schema package."""

    id: str
    """Stable semantic handler identifier."""

    minimum_version: int
    """Minimum compatible handler implementation version."""


class SchemaManifest(BaseModel, frozen=True):
    """Immutable release provenance for one schema package."""

    format_version: int
    """Binary schema package format version."""

    game: str
    """Canonical game mode name."""

    package_version: str
    """Semantic version of the generated schema package."""

    source_repository: str
    """Repository containing the pinned xEdit source."""

    source_tag: str
    """Pinned xEdit release tag."""

    source_commit: str
    """Full pinned xEdit source commit."""

    source_archive_sha256: str
    """SHA-256 of the pinned xEdit source archive."""

    exporter_version: str
    """Version of the Bethkit xEdit exporter contract."""

    exporter_binary_sha256: str
    """SHA-256 of the exporter executable."""

    exporter_map_sha256: str
    """SHA-256 of the detailed Delphi MAP file."""

    exporter_patch_sha256: str
    """SHA-256 of the applied Bethkit exporter patch series."""

    exporter_build_sha256: str
    """SHA-256 of the reproducible exporter build inputs."""

    conversion_rules_sha256: str
    """SHA-256 of the reviewed callback conversion rules."""

    minimum_bethkit_version: str
    """Minimum compatible Bethkit library version."""

    minimum_abi_version: int
    """Minimum compatible Bethkit C ABI version."""

    validation_status: str
    """Release validation state for this package."""

    corpus_sha256: str
    """SHA-256 identifying the protected differential corpus."""

    validated_records: int
    """Number of records covered by differential validation."""

    byte_coverage: float
    """Fraction of validated payload bytes accounted for by the schema."""

    callbacks_total: int
    """Number of exported semantic callback bindings."""

    callbacks_classified: int
    """Number of reviewed and implemented callback bindings."""

    required_decoders: tuple[DecoderRequirement, ...]
    """Payload decoders required to open the package."""

    required_handlers: tuple[HandlerRequirement, ...]
    """Semantic callback handlers required to open the package."""


class Diagnostic(BaseModel, frozen=True):
    """Immutable semantic validation diagnostic."""

    severity: Literal["information", "warning", "error"]
    """Severity assigned by semantic validation."""
    code: str
    """Stable diagnostic category."""
    message: str
    """Human-readable description of the issue."""
    record_signature: bytes
    """Four-byte signature of the affected record."""
    form_id: int
    """File-local identity of the affected record."""
    schema_path: Optional[str] = None
    """Affected schema node, when known."""
    byte_start: Optional[int] = None
    """First affected payload byte, when known."""
    byte_end: Optional[int] = None
    """Exclusive end of the affected payload range."""


class Conflict(BaseModel, frozen=True):
    """Immutable semantic conflict result."""

    object_id: int
    """Resolved identity shared by the compared records."""
    signature: bytes
    """Four-byte record type."""
    plugins: tuple[str, ...]
    """Participating source plugins in load order."""
    winner: str
    """Plugin supplying the winning override."""
    classification: Literal["identical", "override", "conflict"]
    """Semantic relationship between the compared records."""
    paths: tuple[str, ...]
    """Schema paths involved in this result."""


class ReferenceEdge(BaseModel, frozen=True):
    """Immutable directed reference edge."""

    source_plugin: str
    """Plugin containing the reference."""
    source_object_id: int
    """Resolved identity of the referring record."""
    target_plugin: str
    """Plugin defining the reference target."""
    target_object_id: int
    """Resolved identity of the referenced record."""
    schema_path: str
    """Structural location of the reference."""


FieldValue = (
    int
    | float
    | str
    | bytes
    | TypedFormId
    | EnumVal
    | FlagsVal
    | list[Any]
    | None
)
"""Union of values returned by semantic field decoding."""


class NamedField(BaseModel, frozen=True):
    """A named field in a semantic record snapshot."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    """Schema-provided field label."""
    value: FieldValue
    """Generic decoded scalar or nested payload."""


NamedField.model_rebuild()


class _RecordHandle(Protocol):
    """A lifetime-checked borrowed native record."""

    def _native_pointer(self) -> int:
        """Checks the entire owner chain before returning a borrowed pointer."""

        ...


def _decode_field_value(raw: BethkitFieldValue, lib: ctypes.CDLL) -> FieldValue:
    """Decode one native tagged field value."""

    kind = FieldValueKind(raw.kind)
    payload = raw.payload
    if kind == FieldValueKind.INT:
        return int(payload.int_val)
    if kind == FieldValueKind.UINT:
        return int(payload.uint_val)
    if kind == FieldValueKind.FLOAT:
        return float(payload.float_val)
    if kind == FieldValueKind.STR:
        encoded: Optional[bytes] = payload.str_val
        return encoded.decode("utf-8") if encoded else ""
    if kind == FieldValueKind.FORM_ID:
        return int(payload.form_id)
    if kind == FieldValueKind.FORM_ID_TYPED:
        form_id = payload.form_id_typed
        signatures: tuple[bytes, ...] = ()
        if form_id.allowed_sigs and form_id.allowed_count:
            pointer = ctypes.cast(
                form_id.allowed_sigs,
                ctypes.POINTER(ctypes.c_uint8 * 4),
            )
            signatures = tuple(
                bytes(pointer[index]) for index in range(form_id.allowed_count)
            )
        return TypedFormId(raw=form_id.raw, allowed_sigs=signatures)
    if kind == FieldValueKind.BYTES:
        value = payload.bytes
        return (
            bytes(ctypes.string_at(value.ptr, value.len)) if value.ptr else b""
        )
    if kind == FieldValueKind.ENUM:
        value = payload.enum_val
        encoded_name: Optional[bytes] = value.name
        return EnumVal(
            value=value.value,
            name=encoded_name.decode("utf-8") if encoded_name else None,
        )
    if kind == FieldValueKind.FLAGS:
        value = payload.flags_val
        names: tuple[str, ...] = ()
        if value.active_names and value.active_count:
            names = tuple(
                value.active_names[index].decode("utf-8")
                for index in range(value.active_count)
                if value.active_names[index]
            )
        return FlagsVal(raw_value=value.raw_value, active_names=names)
    if kind == FieldValueKind.STRUCT:
        return _decode_entries(payload.struct_entries, lib)
    if kind == FieldValueKind.ARRAY:
        return _decode_values(payload.array_values, lib)
    return None


def _decode_entries(pointer: int, lib: ctypes.CDLL) -> list[NamedField]:
    """Decode a native struct-field list."""

    if not pointer:
        return []
    result: list[NamedField] = []
    for index in range(lib.bethkit_field_entries_len(pointer)):
        field_pointer = lib.bethkit_field_entries_get(pointer, index)
        if field_pointer:
            field = field_pointer.contents
            encoded_name: Optional[bytes] = field.name
            result.append(
                NamedField(
                    name=encoded_name.decode("utf-8") if encoded_name else "",
                    value=_decode_field_value(field.value, lib),
                )
            )
    return result


def _decode_values(pointer: int, lib: ctypes.CDLL) -> list[FieldValue]:
    """Decode a native array-value list."""

    if not pointer:
        return []
    result: list[FieldValue] = []
    for index in range(lib.bethkit_field_values_len(pointer)):
        value_pointer = lib.bethkit_field_values_get(pointer, index)
        if value_pointer:
            result.append(_decode_field_value(value_pointer.contents, lib))
    return result


class SchemaCatalog:
    """Owned catalog containing zero or more game schema packages."""

    __pointer: int

    def __init__(self, pointer: int) -> None:
        """Adopts the owned catalog returned by a native factory.

        Args:
            pointer: Native allocation transferred to this wrapper.
        """

        self.__pointer = pointer

    @classmethod
    def embedded(cls) -> SchemaCatalog:
        """Load the catalog embedded in an official native library."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_catalog_embedded()
        if not pointer:
            _ffi.raise_last_error(lib)
        return cls(pointer)

    @classmethod
    def open(cls, path: Path) -> SchemaCatalog:
        """Load a `.bkschemas` catalog from disk."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_catalog_open(_ffi.enc(path))
        if not pointer:
            _ffi.raise_last_error(lib)
        return cls(pointer)

    def package(self, game: Game) -> SchemaPackage:
        """Return an independently owned package handle for a game."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_catalog_package(
            self.__check_open(), int(game)
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return SchemaPackage(pointer)

    def __check_open(self) -> int:
        """Checks catalog lifetime before borrowing its private pointer."""

        if not self.__pointer:
            raise BethkitClosedError("SchemaCatalog has already been closed.")
        return self.__pointer

    def close(self) -> None:
        """Release the native catalog."""

        if self.__pointer:
            _ffi.load_lib().bethkit_schema_catalog_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> SchemaCatalog:
        """Returns this catalog for scoped resource management."""

        return self

    def __exit__(self, *_: object) -> None:
        """Closes this catalog when leaving its context."""

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned catalog during finalization."""

        try:
            self.close()
        except Exception:
            pass


class SchemaPackage:
    """Owned validated schema package for one game."""

    __pointer: int

    def __init__(self, pointer: int) -> None:
        """Adopts the owned package returned by a native factory.

        Args:
            pointer: Native allocation transferred to this wrapper.
        """

        self.__pointer = pointer

    @classmethod
    def open(cls, path: Path) -> SchemaPackage:
        """Load one `.bkschema` file."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_package_open(_ffi.enc(path))
        if not pointer:
            _ffi.raise_last_error(lib)
        return cls(pointer)

    def _native_pointer(self) -> int:
        """Checks package lifetime before borrowing its private pointer."""

        if not self.__pointer:
            raise BethkitClosedError("SchemaPackage has already been closed.")
        return self.__pointer

    def manifest(self) -> SchemaManifest:
        """Returns validated release provenance independently of this handle."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_package_manifest_json(
            self._native_pointer()
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return SchemaManifest.model_validate_json(text)

    def graph(self) -> _schema.SchemaGraph:
        """Exports the validated graph for offline model generation."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_schema_package_graph_json(self._native_pointer())
        if not pointer:
            _ffi.raise_last_error(lib)
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return _schema.SchemaGraph.model_validate_json(text)

    def close(self) -> None:
        """Release the native package."""

        if self.__pointer:
            _ffi.load_lib().bethkit_schema_package_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> SchemaPackage:
        """Returns this package for scoped resource management."""

        return self

    def __exit__(self, *_: object) -> None:
        """Closes this package when leaving its context."""

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned package during finalization."""

        try:
            self.close()
        except Exception:
            pass


class SemanticContext:
    """Owned semantic runtime for a schema package."""

    __pointer: int

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
        """Checks runtime lifetime before borrowing its private pointer."""

        if not self.__pointer:
            raise BethkitClosedError("SemanticContext has already been closed.")
        return self.__pointer

    def view(
        self,
        record: _RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordView:
        """Create an owned semantic snapshot of a record."""

        return RecordView.new(self, record, localized=localized)

    def edit(
        self,
        record: _RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordEditor:
        """Create a lossless typed editor for a record."""

        return RecordEditor.new(self, record, localized=localized)

    def snapshot(
        self,
        record: _RecordHandle,
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
        record: _RecordHandle,
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
        record: _RecordHandle,
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
        """Release the native semantic context."""

        if self.__pointer:
            _ffi.load_lib().bethkit_semantic_context_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> SemanticContext:
        """Returns this runtime for scoped resource management."""

        return self

    def __exit__(self, *_: object) -> None:
        """Closes this runtime when leaving its context."""

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned runtime during finalization."""

        try:
            self.close()
        except Exception:
            pass


class RecordView:
    """Owned semantic snapshot of one plugin record."""

    __pointer: int
    __fields: Optional[tuple[NamedField, ...]]

    def __init__(self, pointer: int) -> None:
        """Adopts the owned snapshot returned by the native decoder.

        Args:
            pointer: Native allocation transferred to this wrapper.
        """

        self.__pointer = pointer
        self.__fields: Optional[tuple[NamedField, ...]] = None

    @classmethod
    def new(
        cls,
        context: SemanticContext,
        record: _RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordView:
        """Decode a record with the supplied semantic context."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_view_new(
            context._native_pointer(),
            record._native_pointer(),
            localized,
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return cls(pointer)

    def __check_open(self) -> int:
        """Checks snapshot lifetime before borrowing its private pointer."""

        if not self.__pointer:
            raise BethkitClosedError("RecordView has already been closed.")
        return self.__pointer

    def fields(self) -> tuple[NamedField, ...]:
        """Return immutable decoded top-level fields."""

        pointer = self.__check_open()
        if self.__fields is None:
            lib = _ffi.load_lib()
            result: list[NamedField] = []
            for index in range(lib.bethkit_record_view_field_count(pointer)):
                field_pointer = lib.bethkit_record_view_field_get(
                    pointer, index
                )
                if field_pointer:
                    field = field_pointer.contents
                    encoded_name: Optional[bytes] = field.name
                    result.append(
                        NamedField(
                            name=(
                                encoded_name.decode("utf-8")
                                if encoded_name
                                else ""
                            ),
                            value=_decode_field_value(field.value, lib),
                        )
                    )
            self.__fields = tuple(result)
        return self.__fields

    def field_count(self) -> int:
        """Return the number of decoded top-level fields."""

        return int(
            _ffi.load_lib().bethkit_record_view_field_count(self.__check_open())
        )

    def close(self) -> None:
        """Release the native view."""

        if self.__pointer:
            _ffi.load_lib().bethkit_record_view_free(self.__pointer)
            self.__pointer = 0
            self.__fields = None

    def __enter__(self) -> RecordView:
        """Returns this snapshot for scoped resource management."""

        return self

    def __exit__(self, *_: object) -> None:
        """Closes this snapshot when leaving its context."""

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned snapshot during finalization."""

        try:
            self.close()
        except Exception:
            pass


class RecordEditor:
    """Owned lossless editor for one schema-covered record."""

    __pointer: int

    def __init__(self, pointer: int) -> None:
        """Adopts the owned editor returned by the native runtime.

        Args:
            pointer: Native allocation transferred to this wrapper.
        """

        self.__pointer = pointer

    @classmethod
    def new(
        cls,
        context: SemanticContext,
        record: _RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordEditor:
        """Create an editor from a semantic context and record."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_editor_new(
            context._native_pointer(),
            record._native_pointer(),
            localized,
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return cls(pointer)

    def __check_open(self) -> int:
        """Checks editor lifetime before borrowing its private pointer."""

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
        """Replace a typed field occurrence."""

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
        if not isinstance(path, str):
            raise TypeError("Use a generated FieldRef or a schema path string.")
        if occurrence < 0:
            raise ValueError("An occurrence must be nonnegative.")
        if isinstance(value, bool) or not isinstance(
            value, (int, float, str, bytes)
        ):
            raise TypeError(
                "A legacy edit requires an integer, float, string, or bytes."
            )
        if isinstance(value, int) and not -(1 << 63) <= value < (1 << 64):
            raise ValueError("An integer must fit a native 64-bit value.")
        lib = _ffi.load_lib()
        pointer = self.__check_open()
        encoded_path = _ffi.senc(path)
        if isinstance(value, bytes):
            data = (ctypes.c_uint8 * len(value)).from_buffer_copy(value)
            result = lib.bethkit_record_editor_set_bytes(
                pointer,
                encoded_path,
                occurrence,
                data,
                len(value),
            )
        elif isinstance(value, str):
            result = lib.bethkit_record_editor_set_string(
                pointer,
                encoded_path,
                occurrence,
                _ffi.senc(value),
            )
        elif isinstance(value, float):
            result = lib.bethkit_record_editor_set_f64(
                pointer,
                encoded_path,
                occurrence,
                value,
            )
        elif value < 0:
            result = lib.bethkit_record_editor_set_i64(
                pointer,
                encoded_path,
                occurrence,
                value,
            )
        else:
            result = lib.bethkit_record_editor_set_u64(
                pointer,
                encoded_path,
                occurrence,
                value,
            )
        if result != 0:
            _ffi.raise_last_error(lib)

    def snapshot(self) -> _wire.RecordSnapshot:
        """Returns fresh structural addresses after any editing operation."""

        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_editor_snapshot_json(self.__check_open())
        if not pointer:
            raise RecordDecodeError(_ffi.last_error(lib))
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return _wire.RecordSnapshot.model_validate_json(text)

    def strings_snapshot(self) -> _wire.RecordSnapshot:
        """Returns addressed text leaves from the current edited record.

        Returns:
            A strings-only snapshot with the full record's topology guard.

        Raises:
            BethkitClosedError: The editor has been closed or consumed.
            RecordDecodeError: Native values could not be decoded.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_editor_strings_snapshot_json(
            self.__check_open()
        )
        if not pointer:
            raise RecordDecodeError(_ffi.last_error(lib))
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
        return _wire.RecordSnapshot.model_validate_json(text)

    def insert(
        self,
        path: str,
        value: (
            _wire.WireValue
            | int
            | float
            | str
            | bytes
            | _base.StructModel
            | _values.FormId
        ),
    ) -> None:
        """Adds a missing optional subrecord through native grammar validation.

        Args:
            path: Exact schema path of the new subrecord.
            value: Scalar, generated payload model, or tagged native value.

        Raises:
            BethkitClosedError: The editor has been closed or consumed.
            UnsupportedEditError: The value or grammar location is invalid.
        """

        encoded = (
            value.model_dump(mode="json", exclude_none=True)
            if isinstance(
                value, (_wire.WireScalar, _wire.WireStruct, _wire.WireArray)
            )
            else _base._encode(value)
        )
        lib = _ffi.load_lib()
        result = lib.bethkit_record_editor_insert_json(
            self.__check_open(),
            _ffi.senc(path),
            _ffi.senc(json.dumps(encoded, allow_nan=False)),
        )
        if result != 0:
            raise UnsupportedEditError(_ffi.last_error(lib))

    def _set_json(
        self,
        address: _wire.FieldAddress,
        value: dict[str, pydantic.JsonValue],
    ) -> None:
        """Sends an addressed edit through native validation and callbacks."""

        lib = _ffi.load_lib()
        result = lib.bethkit_record_editor_set_at_json(
            self.__check_open(),
            _ffi.senc(address.model_dump_json()),
            _ffi.senc(json.dumps(value, allow_nan=False)),
        )
        if result != 0:
            raise UnsupportedEditError(_ffi.last_error(lib))

    def set_at(
        self, address: _wire.FieldAddress, value: _wire.WireValue
    ) -> None:
        """Replaces an exact scalar, struct, or array through the generic API.

        Args:
            address: Current structural address from an editor or read snapshot.
            value: Tagged replacement subject to native schema validation.

        Raises:
            UnsupportedEditError: The address is stale or the value is invalid.
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
            UnsupportedEditError: The insertion or repetition scope is invalid.
        """

        lib = _ffi.load_lib()
        result = lib.bethkit_record_editor_insert_at_json(
            self.__check_open(),
            _ffi.senc(address.model_dump_json()),
            _ffi.senc(value.model_dump_json()),
        )
        if result != 0:
            raise UnsupportedEditError(_ffi.last_error(lib))

    def set_form_id(
        self,
        path: str,
        value: int,
        *,
        occurrence: int = 0,
    ) -> None:
        """Replace a FormID field occurrence."""

        if isinstance(value, bool) or not 0 <= value <= 0xFFFFFFFF:
            raise ValueError("A FormID must fit an unsigned 32-bit integer.")
        if occurrence < 0:
            raise ValueError("An occurrence must be nonnegative.")
        lib = _ffi.load_lib()
        result = lib.bethkit_record_editor_set_form_id(
            self.__check_open(),
            _ffi.senc(path),
            occurrence,
            value,
        )
        if result != 0:
            _ffi.raise_last_error(lib)

    def remove(
        self,
        path: str | _wire.FieldAddress | _base.FieldReference,
        *,
        occurrence: int = 0,
    ) -> None:
        """Remove a top-level field occurrence."""

        if occurrence < 0:
            raise ValueError("An occurrence must be nonnegative.")
        lib = _ffi.load_lib()
        if isinstance(path, _base.FieldReference):
            if path.address is None:
                raise UnsupportedEditError(
                    "Select an individual field within the group."
                )
            path = path.address
        if isinstance(path, _wire.FieldAddress):
            if occurrence:
                raise ValueError(
                    "An addressed field already identifies its occurrence."
                )
            result = lib.bethkit_record_editor_remove_at_json(
                self.__check_open(),
                _ffi.senc(path.model_dump_json()),
            )
            if result != 0:
                raise UnsupportedEditError(_ffi.last_error(lib))
            return
        result = lib.bethkit_record_editor_remove(
            self.__check_open(),
            _ffi.senc(path),
            occurrence,
        )
        if result != 0:
            _ffi.raise_last_error(lib)

    def finish(self) -> WritableRecord:
        """Consume the editor and return a writable record."""

        from ..plugin.writer import WritableRecord

        lib = _ffi.load_lib()
        editor_pointer = self.__check_open()
        pointer = lib.bethkit_record_editor_finish(editor_pointer)
        if not pointer:
            _ffi.raise_last_error(lib)
        lib.bethkit_record_editor_free(editor_pointer)
        self.__pointer = 0
        return WritableRecord(pointer)

    def close(self) -> None:
        """Release the editor without keeping its changes."""

        if self.__pointer:
            _ffi.load_lib().bethkit_record_editor_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> RecordEditor:
        """Returns this editor for scoped resource management."""

        return self

    def __exit__(self, *_: object) -> None:
        """Discards the editor's changes when leaving its context."""

        self.close()

    def __del__(self) -> None:
        """Discards any remaining owned editor during finalization."""

        try:
            self.close()
        except Exception:
            pass
