"""Versioned schema packages and semantic record views."""

from __future__ import annotations

import ctypes
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, Optional, Protocol

from pydantic import BaseModel, ConfigDict

from .. import _ffi
from .._error import BethkitClosedError
from .._ffi import BethkitFieldValue
from ..enums import FieldValueKind, Game

if TYPE_CHECKING:
    from ..plugin.writer import WritableRecord


class TypedFormId(BaseModel, frozen=True):
    """A FormID and the record signatures it may reference."""

    raw: int
    allowed_sigs: tuple[bytes, ...]


class EnumVal(BaseModel, frozen=True):
    """A decoded enumeration value."""

    value: int
    name: Optional[str]


class FlagsVal(BaseModel, frozen=True):
    """A decoded bit-flags value."""

    raw_value: int
    active_names: tuple[str, ...]


class DecoderRequirement(BaseModel, frozen=True):
    """One custom decoder required by a schema package."""

    id: str
    minimum_version: int


class SchemaManifest(BaseModel, frozen=True):
    """Immutable release provenance for one schema package."""

    format_version: int
    game: str
    package_version: str
    source_repository: str
    source_tag: str
    source_commit: str
    source_archive_sha256: str
    exporter_version: str
    exporter_binary_sha256: str
    exporter_patch_sha256: str
    exporter_build_sha256: str
    conversion_rules_sha256: str
    minimum_bethkit_version: str
    minimum_abi_version: int
    validation_status: str
    corpus_sha256: str
    validated_records: int
    byte_coverage: float
    callbacks_total: int
    callbacks_classified: int
    required_decoders: tuple[DecoderRequirement, ...]


class Diagnostic(BaseModel, frozen=True):
    """Immutable semantic validation diagnostic."""

    severity: Literal["information", "warning", "error"]
    code: str
    message: str
    record_signature: bytes
    form_id: int
    schema_path: Optional[str] = None
    byte_start: Optional[int] = None
    byte_end: Optional[int] = None


class Conflict(BaseModel, frozen=True):
    """Immutable semantic conflict result."""

    object_id: int
    signature: bytes
    plugins: tuple[str, ...]
    winner: str
    classification: Literal["identical", "override", "conflict"]
    paths: tuple[str, ...]


class ReferenceEdge(BaseModel, frozen=True):
    """Immutable directed reference edge."""

    source_plugin: str
    source_object_id: int
    target_plugin: str
    target_object_id: int
    schema_path: str


FieldValue = (
    int | float | str | bytes | TypedFormId | EnumVal | FlagsVal | list[Any] | None
)
"""Union of values returned by semantic field decoding."""


class NamedField(BaseModel, frozen=True):
    """A named field in a semantic record snapshot."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    value: FieldValue


NamedField.model_rebuild()


class _RecordHandle(Protocol):
    _ptr: int


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
        return bytes(ctypes.string_at(value.ptr, value.len)) if value.ptr else b""
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

    def __init__(self, pointer: int) -> None:
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
        pointer = lib.bethkit_schema_catalog_package(self.__check_open(), int(game))
        if not pointer:
            _ffi.raise_last_error(lib)
        return SchemaPackage(pointer)

    def __check_open(self) -> int:
        if not self.__pointer:
            raise BethkitClosedError("SchemaCatalog has already been closed.")
        return self.__pointer

    def close(self) -> None:
        """Release the native catalog."""
        if self.__pointer:
            _ffi.load_lib().bethkit_schema_catalog_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> SchemaCatalog:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


class SchemaPackage:
    """Owned validated schema package for one game."""

    def __init__(self, pointer: int) -> None:
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
        if not self.__pointer:
            raise BethkitClosedError("SchemaPackage has already been closed.")
        return self.__pointer

    def close(self) -> None:
        """Release the native package."""
        if self.__pointer:
            _ffi.load_lib().bethkit_schema_package_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> SchemaPackage:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


class SemanticContext:
    """Owned semantic runtime for a schema package."""

    def __init__(self, package: SchemaPackage) -> None:
        lib = _ffi.load_lib()
        pointer = lib.bethkit_semantic_context_new(package._native_pointer())
        if not pointer:
            _ffi.raise_last_error(lib)
        self.__pointer = pointer

    def _native_pointer(self) -> int:
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

    def close(self) -> None:
        """Release the native semantic context."""
        if self.__pointer:
            _ffi.load_lib().bethkit_semantic_context_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> SemanticContext:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


class RecordView:
    """Owned semantic snapshot of one plugin record."""

    def __init__(self, pointer: int) -> None:
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
        if not record._ptr:
            raise BethkitClosedError("Record is closed or has no native pointer.")
        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_view_new(
            context._native_pointer(),
            record._ptr,
            localized,
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return cls(pointer)

    def __check_open(self) -> int:
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
                field_pointer = lib.bethkit_record_view_field_get(pointer, index)
                if field_pointer:
                    field = field_pointer.contents
                    encoded_name: Optional[bytes] = field.name
                    result.append(
                        NamedField(
                            name=(encoded_name.decode("utf-8") if encoded_name else ""),
                            value=_decode_field_value(field.value, lib),
                        )
                    )
            self.__fields = tuple(result)
        return self.__fields

    def field_count(self) -> int:
        """Return the number of decoded top-level fields."""
        return int(_ffi.load_lib().bethkit_record_view_field_count(self.__check_open()))

    def close(self) -> None:
        """Release the native view."""
        if self.__pointer:
            _ffi.load_lib().bethkit_record_view_free(self.__pointer)
            self.__pointer = 0
            self.__fields = None

    def __enter__(self) -> RecordView:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


class RecordEditor:
    """Owned lossless editor for one schema-covered record."""

    def __init__(self, pointer: int) -> None:
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
        if not record._ptr:
            raise BethkitClosedError("Record is closed or has no native pointer.")
        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_editor_new(
            context._native_pointer(),
            record._ptr,
            localized,
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return cls(pointer)

    def __check_open(self) -> int:
        if not self.__pointer:
            raise BethkitClosedError("RecordEditor has already been closed.")
        return self.__pointer

    def set(
        self,
        path: str,
        value: int | float | str | bytes,
        *,
        occurrence: int = 0,
    ) -> None:
        """Replace a typed field occurrence."""
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

    def set_form_id(
        self,
        path: str,
        value: int,
        *,
        occurrence: int = 0,
    ) -> None:
        """Replace a FormID field occurrence."""
        lib = _ffi.load_lib()
        result = lib.bethkit_record_editor_set_form_id(
            self.__check_open(),
            _ffi.senc(path),
            occurrence,
            value,
        )
        if result != 0:
            _ffi.raise_last_error(lib)

    def remove(self, path: str, *, occurrence: int = 0) -> None:
        """Remove a top-level field occurrence."""
        lib = _ffi.load_lib()
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

        pointer = _ffi.load_lib().bethkit_record_editor_finish(self.__check_open())
        if not pointer:
            _ffi.raise_last_error(_ffi.load_lib())
        self.__pointer = 0
        return WritableRecord(pointer)

    def close(self) -> None:
        """Release the editor without keeping its changes."""
        if self.__pointer:
            _ffi.load_lib().bethkit_record_editor_free(self.__pointer)
            self.__pointer = 0

    def __enter__(self) -> RecordEditor:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass
