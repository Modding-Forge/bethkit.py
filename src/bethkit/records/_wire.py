"""
Copyright (c) Modding Forge

Validated, immutable semantic snapshots at the native JSON boundary.
"""

from __future__ import annotations

from typing import Annotated, Literal, Optional

import pydantic


class RepeatScope(pydantic.BaseModel, frozen=True):
    """One occurrence in a native grammar repetition."""

    path: str
    """Schema path of the repeated child."""
    occurrence: int = pydantic.Field(ge=0)
    """Zero-based occurrence within its containing scope."""


class ValueStep(pydantic.BaseModel, frozen=True):
    """One exact step through a packed struct or array."""

    kind: Literal["field", "index"]
    """Whether this step selects a named member or array item."""
    index: int = pydantic.Field(ge=0)
    """Native member or element index."""
    path: Optional[str] = None
    """Schema path of a named member, absent for array indexes."""


class FieldAddress(pydantic.BaseModel, frozen=True):
    """Structural field position, guarded against stale record layouts.

    Neither the current text nor any other scalar value is part of this
    address. The structure hash is a mutation guard, not a string identity.
    """

    schema_payload_sha256: str
    """Identity of the authoritative schema payload."""
    structure_hash: str
    """Native structural revision; changes invalidate old edit addresses."""
    record_signature: tuple[int, int, int, int]
    """Containing record's four-byte signature."""
    form_id: int = pydantic.Field(ge=0, le=0xFFFFFFFF)
    """File-local identifier of the containing record."""
    subrecord_index: int = pydantic.Field(ge=0)
    """Absolute position of the containing source subrecord."""
    subrecord_path: str
    """Matched schema subrecord path."""
    repeat_scopes: tuple[RepeatScope, ...] = ()
    """Nested repetitions supplied by the native grammar interpreter."""
    value_steps: tuple[ValueStep, ...] = ()
    """Exact traversal within the subrecord payload."""


class ByteSpan(pydantic.BaseModel, frozen=True):
    """Half-open byte range within a subrecord payload."""

    start: int = pydantic.Field(ge=0)
    """First byte included in the field."""
    end: int = pydantic.Field(ge=0)
    """First byte after the field."""


class WireScalar(pydantic.BaseModel, frozen=True):
    """Tagged scalar, retaining representation details for native edits."""

    schema_path: Optional[str] = None
    """Exact effective schema node selected by the native decoder."""
    kind: Literal[
        "int",
        "uint",
        "float",
        "string",
        "bytes",
        "enum",
        "flags",
        "form_id",
        "absent",
    ]
    """Native semantic value kind."""
    address: FieldAddress
    """Exact guarded address of this scalar."""
    value: int | float | str | tuple[int, ...] | None
    """Scalar payload; nonfinite floats use their canonical string spelling."""
    allowed_signatures: tuple[tuple[int, int, int, int], ...] = ()
    """Permitted FormID target record types."""
    names: tuple[str, ...] = ()
    """Schema labels for enumeration values or active flag bits."""
    translatable: bool = False
    """Whether the schema marks this value as translatable text."""
    string_table: Optional[Literal["strings", "dl_strings", "il_strings"]] = (
        None
    )
    """Schema-declared external table kind for localized strings."""


class WireStruct(pydantic.BaseModel, frozen=True):
    """Packed struct with named, independently addressed children."""

    schema_path: Optional[str] = None
    """Exact effective schema node selected by the native decoder."""
    kind: Literal["struct"]
    """Native semantic value kind."""
    address: FieldAddress
    """Exact guarded address of the whole struct."""
    fields: tuple[WireField, ...]
    """Ordered members, including explicit absent values."""


class WireArray(pydantic.BaseModel, frozen=True):
    """Homogeneous payload array with addressed elements."""

    schema_path: Optional[str] = None
    """Exact effective schema node selected by the native decoder."""
    kind: Literal["array"]
    """Native semantic value kind."""
    address: FieldAddress
    """Exact guarded address of the whole array."""
    items: tuple[WireValue, ...]
    """Ordered elements."""


WireValue = Annotated[
    WireScalar | WireStruct | WireArray, pydantic.Field(discriminator="kind")
]


class WireField(pydantic.BaseModel, frozen=True):
    """One decoded native field with provenance."""

    name: str
    """Human-readable schema name."""
    node_id: int
    """Stable identifier within the schema package."""
    path: str
    """Authoritative schema path."""
    effective_path: Optional[str] = None
    """Selected dynamic union alternative, when present."""
    span: ByteSpan
    """Encoded byte range in the containing subrecord."""
    origin: str
    """Schema, custom decoder, or preserved unknown-field provenance."""
    address: FieldAddress
    """Exact guarded field position."""
    value: WireValue
    """Fully typed native value tree."""


class RecordSnapshot(pydantic.BaseModel, frozen=True):
    """Owned record snapshot independent of all native handle lifetimes."""

    format_version: Literal[1]
    """Version of the native snapshot interchange contract."""
    projection: Literal["full", "strings"] = "full"
    """Whether all values or only translatable text leaves are included."""
    schema_payload_sha256: str
    """Exact schema payload identity."""
    structure_hash: str
    """Native structural revision of this snapshot."""
    record_signature: str
    """Four-character record signature."""
    form_id: int
    """File-local record identifier."""
    fields: tuple[WireField, ...]
    """Decoded source subrecords in their original order."""


WireStruct.model_rebuild()
WireArray.model_rebuild()
WireField.model_rebuild()
RecordSnapshot.model_rebuild()


class ValidationDiagnostic(pydantic.BaseModel, frozen=True):
    """One actionable diagnostic produced by native semantic validation."""

    severity: Literal["information", "warning", "error"]
    """Diagnostic severity under the selected validation mode."""
    code: str
    """Stable native diagnostic code."""
    message: str
    """Human-readable explanation."""
    record_signature: str
    """Containing record type."""
    form_id: int
    """Containing file-local record identifier."""
    node_id: Optional[int] = None
    """Schema node identity, if the diagnostic concerns a declared node."""
    path: Optional[str] = None
    """Relevant schema path."""
    span: Optional[ByteSpan] = None
    """Affected payload byte range, when known."""


class ValidationReport(pydantic.BaseModel, frozen=True):
    """A complete native validation result, including nonfatal warnings."""

    format_version: Literal[1]
    """Validation interchange contract version."""
    has_errors: bool
    """Whether any diagnostic is an error in the selected mode."""
    diagnostics: tuple[ValidationDiagnostic, ...]
    """Ordered native diagnostics."""
