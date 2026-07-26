"""
Copyright (c) Modding Forge

Schema subpackage — schema-driven record field decoding and type information.
"""

from __future__ import annotations

from .schema import (
    Conflict,
    DecoderRequirement,
    Diagnostic,
    EnumVal,
    FieldValue,
    FlagsVal,
    NamedField,
    RecordEditor,
    RecordView,
    ReferenceEdge,
    SchemaCatalog,
    SchemaManifest,
    SchemaPackage,
    SemanticContext,
    TypedFormId,
)

__all__ = [
    "Conflict",
    "DecoderRequirement",
    "Diagnostic",
    "EnumVal",
    "FieldValue",
    "FlagsVal",
    "NamedField",
    "RecordEditor",
    "RecordView",
    "ReferenceEdge",
    "SchemaCatalog",
    "SchemaManifest",
    "SchemaPackage",
    "SemanticContext",
    "TypedFormId",
]
