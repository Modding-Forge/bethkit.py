"""Validated schema graph consumed by the offline model generator.

Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Literal, Optional

import pydantic


class IntegerSpec(pydantic.BaseModel, frozen=True):
    """Width and signedness of a schema integer."""

    width: int
    """Encoded byte width."""
    signed: bool
    """Whether the highest bit represents a sign."""


class PrimitiveSpec(pydantic.BaseModel, frozen=True):
    """Type information needed to generate one primitive annotation."""

    type: str
    """Native primitive kind."""
    integer: Optional[IntegerSpec] = None
    """Integer layout when present."""
    length: Optional[int] = None
    """Exact byte count for fixed binary fields."""
    string: dict[str, pydantic.JsonValue] = {}
    """Encoding, localization and string-layout metadata."""
    targets: tuple[tuple[int, int, int, int], ...] = ()
    """Permitted four-byte FormID target signatures."""
    values: tuple[tuple[int, str], ...] = ()
    """Named enumeration values."""
    bits: tuple[tuple[int, str], ...] = ()
    """Named flag bit positions."""


class SchemaNode(pydantic.BaseModel, frozen=True):
    """A structural node from the authoritative Bethkit grammar."""

    id: int
    """Stable identifier inside the pinned schema."""
    path: str
    """Exact schema path."""
    name: str
    """Human-readable xEdit label."""
    kind: str
    """Grammar or payload node kind."""
    required: bool = False
    """Whether native validation requires this node."""
    condition: pydantic.JsonValue = None
    """Native inclusion expression, interpreted only by Rust."""
    children: tuple[SchemaNode, ...] = ()
    """Ordered or unordered grammar members."""
    fields: tuple[SchemaNode, ...] = ()
    """Packed structure members."""
    alternatives: tuple[SchemaNode, ...] = ()
    """Grammar choice alternatives."""
    variants: tuple[SchemaNode, ...] = ()
    """Payload union variants."""
    child: Optional[SchemaNode] = None
    """Repeated, terminated or compressed child."""
    payload: Optional[SchemaNode] = None
    """Typed subrecord payload."""
    element: Optional[SchemaNode] = None
    """Array element definition."""
    primitive: Optional[PrimitiveSpec] = None
    """Primitive representation."""
    optional_from: int = 0
    """First optional trailing structure member."""
    decoder: Optional[str] = None
    """Custom decoder identifier."""
    target: Optional[str] = None
    """Reference target path."""


class RecordDefinition(pydantic.BaseModel, frozen=True):
    """One schema-covered main-record definition."""

    signature: tuple[int, int, int, int]
    """Four-byte record signature."""
    name: str
    """Record label from xEdit."""
    root: SchemaNode
    """Authoritative record grammar."""


class SchemaGraph(pydantic.BaseModel, frozen=True):
    """Versioned native schema export accepted by the generator."""

    format_version: Literal[1]
    """JSON export contract version."""
    payload_sha256: str
    """Identity of the exact schema package payload."""
    manifest: dict[str, pydantic.JsonValue]
    """Provenance and game metadata."""
    records: tuple[RecordDefinition, ...]
    """Every exported record definition."""
