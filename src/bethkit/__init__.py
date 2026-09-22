"""
Copyright (c) Modding Forge
"""

# bethkit — Python bindings for the bethkit Bethesda plugin and archive toolkit.
#
# Place ``bethkit_ffi.dll`` (Windows), ``libbethkit_ffi.so`` (Linux), or
# ``libbethkit_ffi.dylib`` (macOS) next to this package, or set the
# ``BETHKIT_LIB`` environment variable to the full path of the library before
# importing.
#
# Quick example::
#
#     from bethkit import Plugin, Game
#
#     with Plugin.open(Path("MyMod.esp"), Game.SKYRIM_SE) as p:
#         for master in p.masters:
#             print(master)
#         for group in p:
#             for child in group:
#                 if hasattr(child, "form_id"):
#                     print(f"0x{child.form_id:08X}", child.editor_id)

from __future__ import annotations

from ._error import (
    BethkitClosedError,
    BethkitError,
    BethkitLibraryNotFoundError,
    BethkitNativeError,
    BethkitNotFoundError,
    BethkitOwnershipError,
    RecordDecodeError,
    SchemaMismatchError,
    StringTableError,
    UnsupportedEditError,
)
from .archive import (
    Archive,
    ArchiveEntry,
    Ba2Dx10Writer,
    Ba2GnrlWriter,
    BsaWriter,
)
from .enums import (
    Ba2Version,
    BsaVersion,
    FieldValueKind,
    Game,
    PluginKind,
    StringFileKind,
)
from .load_order import GlobalFormId, LoadOrder
from .plugin import (
    CacheHit,
    Group,
    Plugin,
    PluginCache,
    PluginPatcher,
    PluginWriter,
    Record,
    SubRecord,
    WritableGroup,
    WritableRecord,
)
from .records import FieldAddress, FieldRef, RecordModel, RecordSnapshot
from .records._wire import ValidationDiagnostic, ValidationReport
from .schema import (
    Conflict,
    DecoderRequirement,
    Diagnostic,
    EnumVal,
    FlagsVal,
    HandlerRequirement,
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
from .strings import (
    LocalizationEditor,
    LocalizationSet,
    StringIdentity,
    StringReference,
    StringTable,
    iter_strings,
)

__all__ = [
    "FieldAddress",
    "FieldRef",
    "RecordModel",
    "RecordSnapshot",
    "RecordDecodeError",
    "SchemaMismatchError",
    "StringTableError",
    "UnsupportedEditError",
    "ValidationDiagnostic",
    "ValidationReport",
    "PluginPatcher",
    "LocalizationEditor",
    "StringIdentity",
    "StringReference",
    "iter_strings",
    # Exceptions
    "BethkitError",
    "BethkitLibraryNotFoundError",
    "BethkitNativeError",
    "BethkitClosedError",
    "BethkitOwnershipError",
    "BethkitNotFoundError",
    # Enums
    "Game",
    "PluginKind",
    "StringFileKind",
    "BsaVersion",
    "Ba2Version",
    "FieldValueKind",
    # Plugin reading
    "Plugin",
    "Group",
    "Record",
    "SubRecord",
    # Archives
    "Archive",
    "ArchiveEntry",
    "BsaWriter",
    "Ba2GnrlWriter",
    "Ba2Dx10Writer",
    # Schema
    "SchemaCatalog",
    "SchemaPackage",
    "SchemaManifest",
    "SemanticContext",
    "RecordView",
    "RecordEditor",
    "NamedField",
    "TypedFormId",
    "EnumVal",
    "FlagsVal",
    "HandlerRequirement",
    "DecoderRequirement",
    "Diagnostic",
    "Conflict",
    "ReferenceEdge",
    # Load order & cache
    "LoadOrder",
    "GlobalFormId",
    "PluginCache",
    "CacheHit",
    # Strings
    "StringTable",
    "LocalizationSet",
    # Writing
    "PluginWriter",
    "WritableGroup",
    "WritableRecord",
]
