"""
Copyright (c) Modding Forge

Mapping from Python classes/methods to C ABI functions.

Used by ``gen_stubs.py`` to generate ``.pyi`` stub files.
Each :class:`MethodDef` ties a Python method to its backing C function so the
generator can look up the correct docstring from ``bethkit.h``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MethodDef:
    """Definition of a single Python method for stub generation."""

    name: str
    """Python method name."""

    params: str
    """
    Parameter list, excluding *self*/*cls*, e.g.
    ``'path: str | Path, game: Game'``.
    """

    ret: str
    """Return-type annotation as a string, e.g. ``'Plugin'``."""

    c_func: Optional[str] = None
    """
    Name of the backing C function.

    ``None`` for pure-Python lifecycle methods whose docstring is
    supplied via *manual_doc*.
    """

    kind: str = "instance"
    """
    Method kind: ``'instance'``, ``'classmethod'``,
    ``'property'``, or ``'staticmethod'``.
    """

    manual_doc: Optional[str] = None
    """
    Override docstring used when *c_func* is ``None`` or when the
    C header doc is too low-level to be useful as-is.
    """


@dataclass
class ClassDef:
    """Definition of a single Python class for stub generation."""

    name: str
    """Python class name."""

    c_typedef: Optional[str] = None
    """
    Name of the C typedef whose ``/** */`` comment becomes the
    class-level docstring.  ``None`` for pure-Python data classes.
    """

    context_manager: bool = False
    """When ``True`` the emitter adds ``__enter__`` / ``__exit__``."""

    methods: list[MethodDef] = field(default_factory=list)
    """Ordered list of method definitions."""


@dataclass
class ModuleDef:
    """Definition of a ``.pyi`` stub module."""

    file: str
    """Output filename relative to ``src/bethkit/``, e.g. ``'plugin.pyi'``."""

    imports: list[str]
    """Import lines written verbatim at the top of the stub."""

    classes: list[ClassDef]
    """Classes emitted into this stub."""


_CLOSE_DOC = "Free this handle. Safe to call multiple times."
_TRANSFER_DOC = (
    "**Transfers ownership** of *{arg}*."
    " Do not use *{arg}* after this call."
)


MODULES: dict[str, ModuleDef] = {
    # ------------------------------------------------------------------
    # plugin.pyi
    # ------------------------------------------------------------------
    "plugin": ModuleDef(
        file="plugin.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from pathlib import Path",
            "from typing import Iterator, Optional, Self",
            "",
            "from ._error import BethkitError",
            "from .enums import Game, PluginKind",
        ],
        classes=[
            ClassDef(
                name="SubRecord",
                c_typedef="BethkitSubRecord",
                methods=[
                    MethodDef(
                        "signature",
                        "",
                        "bytes",
                        "bethkit_subrecord_signature",
                        "property",
                    ),
                    MethodDef(
                        "raw_bytes",
                        "",
                        "bytes",
                        "bethkit_subrecord_bytes",
                        "property",
                        manual_doc=(
                            "The raw subrecord payload as an immutable"
                            " bytes object."
                        ),
                    ),
                    MethodDef(
                        "as_u8",
                        "",
                        "int",
                        "bethkit_subrecord_as_u8",
                    ),
                    MethodDef(
                        "as_u16",
                        "",
                        "int",
                        "bethkit_subrecord_as_u16",
                    ),
                    MethodDef(
                        "as_u32",
                        "",
                        "int",
                        "bethkit_subrecord_as_u32",
                    ),
                    MethodDef(
                        "as_f32",
                        "",
                        "float",
                        "bethkit_subrecord_as_f32",
                    ),
                    MethodDef(
                        "as_str",
                        "",
                        "str",
                        "bethkit_subrecord_as_zstring",
                        manual_doc=(
                            "Decode the payload as a NUL-terminated"
                            " UTF-8 string.\n\n"
                            "Raises:\n"
                            "    BethkitError: When the payload is not"
                            " valid UTF-8."
                        ),
                    ),
                ],
            ),
            ClassDef(
                name="Record",
                c_typedef="BethkitRecord",
                methods=[
                    MethodDef(
                        "signature",
                        "",
                        "bytes",
                        "bethkit_record_signature",
                        "property",
                    ),
                    MethodDef(
                        "form_id",
                        "",
                        "int",
                        "bethkit_record_form_id",
                        "property",
                    ),
                    MethodDef(
                        "flags",
                        "",
                        "int",
                        "bethkit_record_flags",
                        "property",
                    ),
                    MethodDef(
                        "form_version",
                        "",
                        "int",
                        "bethkit_record_form_version",
                        "property",
                    ),
                    MethodDef(
                        "editor_id",
                        "",
                        "Optional[str]",
                        "bethkit_record_editor_id",
                        "property",
                    ),
                    MethodDef(
                        "subrecord_count",
                        "",
                        "int",
                        "bethkit_record_subrecord_count",
                        manual_doc=(
                            "Return the number of subrecords.\n\n"
                            "Raises:\n"
                            "    BethkitError: When subrecords cannot"
                            " be decoded."
                        ),
                    ),
                    MethodDef(
                        "subrecord_at",
                        "index: int",
                        "SubRecord",
                        "bethkit_record_subrecord_get",
                        manual_doc=(
                            "Return the :class:`SubRecord` at *index*.\n\n"
                            "Raises:\n"
                            "    BethkitError: When *index* is out of"
                            " bounds or decoding fails."
                        ),
                    ),
                    MethodDef(
                        "find_subrecord",
                        "sig: bytes | str",
                        "Optional[SubRecord]",
                        "bethkit_record_subrecord_find",
                    ),
                    MethodDef(
                        "__iter__",
                        "",
                        "Iterator[SubRecord]",
                        manual_doc=(
                            "Iterate over all subrecords."
                        ),
                    ),
                ],
            ),
            ClassDef(
                name="Group",
                c_typedef="BethkitGroup",
                methods=[
                    MethodDef(
                        "group_type",
                        "",
                        "int",
                        "bethkit_group_type",
                        "property",
                        manual_doc=(
                            "The numeric Bethesda group type"
                            " (0 = top-level by signature, ...)."
                        ),
                    ),
                    MethodDef(
                        "child_count",
                        "",
                        "int",
                        "bethkit_group_child_count",
                        "property",
                        manual_doc=(
                            "The number of direct children"
                            " (records and sub-groups)."
                        ),
                    ),
                    MethodDef(
                        "child_is_record",
                        "index: int",
                        "bool",
                        "bethkit_group_child_is_record",
                    ),
                    MethodDef(
                        "child_as_record",
                        "index: int",
                        "Optional[Record]",
                        "bethkit_group_child_as_record",
                    ),
                    MethodDef(
                        "child_as_group",
                        "index: int",
                        "Optional[Group]",
                        "bethkit_group_child_as_group",
                    ),
                    MethodDef(
                        "__iter__",
                        "",
                        "Iterator[Record | Group]",
                        manual_doc=(
                            "Iterate over all children as"
                            " :class:`Record` or :class:`Group`."
                        ),
                    ),
                ],
            ),
            ClassDef(
                name="Plugin",
                c_typedef="BethkitPlugin",
                context_manager=True,
                methods=[
                    MethodDef(
                        "open",
                        "path: Path, game: Game",
                        "Plugin",
                        "bethkit_plugin_open",
                        "classmethod",
                    ),
                    MethodDef(
                        "from_bytes",
                        "data: bytes, game: Game",
                        "Plugin",
                        "bethkit_plugin_open_from_bytes",
                        "classmethod",
                        manual_doc=(
                            "Parse a plugin from an in-memory *data*"
                            " buffer.\n\n"
                            "Raises:\n"
                            "    BethkitError: When *data* cannot be"
                            " parsed as a valid plugin."
                        ),
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "kind",
                        "",
                        "PluginKind",
                        "bethkit_plugin_kind",
                        "property",
                    ),
                    MethodDef(
                        "is_localized",
                        "",
                        "bool",
                        "bethkit_plugin_is_localized",
                        "property",
                    ),
                    MethodDef(
                        "description",
                        "",
                        "Optional[str]",
                        "bethkit_plugin_description",
                        "property",
                    ),
                    MethodDef(
                        "master_count",
                        "",
                        "int",
                        "bethkit_plugin_master_count",
                        "property",
                    ),
                    MethodDef(
                        "masters",
                        "",
                        "list[str]",
                        None,
                        "property",
                        manual_doc=(
                            "Return the ordered list of master file"
                            " names declared in the plugin header."
                        ),
                    ),
                    MethodDef(
                        "group_count",
                        "",
                        "int",
                        "bethkit_plugin_group_count",
                        "property",
                    ),
                    MethodDef(
                        "groups",
                        "",
                        "Iterator[Group]",
                        None,
                        "property",
                        manual_doc=(
                            "Iterate lazily over all top-level record groups."
                        ),
                    ),
                    MethodDef(
                        "__iter__",
                        "",
                        "Iterator[Group]",
                        manual_doc=(
                            "Iterate over all top-level groups."
                            " Equivalent to :attr:`groups`."
                        ),
                    ),
                    MethodDef(
                        "find_record",
                        "form_id: int",
                        "Optional[Record]",
                        "bethkit_plugin_find_record",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # archive.pyi
    # ------------------------------------------------------------------
    "archive": ModuleDef(
        file="archive.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from pathlib import Path",
            "from typing import Self",
            "",
            "from ._error import BethkitError",
            "from .enums import Ba2Version, BsaVersion",
        ],
        classes=[
            ClassDef(
                name="ArchiveEntry",
                c_typedef="BethkitArchiveEntry",
                methods=[
                    MethodDef(
                        "path",
                        "",
                        "str",
                        "bethkit_archive_entry_path",
                        "property",
                    ),
                    MethodDef(
                        "uncompressed_size",
                        "",
                        "int",
                        "bethkit_archive_entry_uncompressed_size",
                        "property",
                    ),
                ],
            ),
            ClassDef(
                name="Archive",
                c_typedef="BethkitArchive",
                context_manager=True,
                methods=[
                    MethodDef(
                        "open",
                        "path: str | Path",
                        "Archive",
                        "bethkit_archive_open",
                        "classmethod",
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "format_name",
                        "",
                        "str",
                        "bethkit_archive_format_name",
                        "property",
                    ),
                    MethodDef(
                        "file_count",
                        "",
                        "int",
                        "bethkit_archive_file_count",
                        "property",
                        manual_doc=(
                            "The total number of files in the archive."
                        ),
                    ),
                    MethodDef(
                        "entry_at",
                        "index: int",
                        "ArchiveEntry",
                        "bethkit_archive_entry_get",
                        manual_doc=(
                            "Return the :class:`ArchiveEntry` at"
                            " *index*.\n\n"
                            "Raises:\n"
                            "    BethkitError: When *index* is out of"
                            " bounds."
                        ),
                    ),
                    MethodDef(
                        "extract",
                        "path: str",
                        "bytes",
                        "bethkit_archive_extract",
                    ),
                    MethodDef(
                        "extract_to_file",
                        "path: str, dest: str | Path",
                        "None",
                        "bethkit_archive_extract_to_file",
                    ),
                ],
            ),
            ClassDef(
                name="BsaWriter",
                c_typedef="BethkitBsaWriter",
                context_manager=True,
                methods=[
                    MethodDef(
                        "__init__",
                        "version: BsaVersion",
                        "None",
                        "bethkit_bsa_writer_new",
                        manual_doc=(
                            "Create a new BSA archive writer.\n\n"
                            "Args:\n"
                            "    version (BsaVersion): The BSA format"
                            " version to produce."
                        ),
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "set_compress",
                        "compress: bool",
                        "None",
                        "bethkit_bsa_writer_set_compress",
                    ),
                    MethodDef(
                        "set_embed_names",
                        "embed: bool",
                        "None",
                        "bethkit_bsa_writer_set_embed_names",
                    ),
                    MethodDef(
                        "add",
                        "path: str, data: bytes",
                        "None",
                        "bethkit_bsa_writer_add",
                    ),
                    MethodDef(
                        "write_to",
                        "dest: str | Path",
                        "None",
                        "bethkit_bsa_writer_write_to",
                    ),
                ],
            ),
            ClassDef(
                name="Ba2GnrlWriter",
                c_typedef="BethkitBa2GnrlWriter",
                context_manager=True,
                methods=[
                    MethodDef(
                        "__init__",
                        "version: Ba2Version",
                        "None",
                        "bethkit_ba2_gnrl_writer_new",
                        manual_doc=(
                            "Create a new BA2 general-content archive"
                            " writer.\n\n"
                            "Args:\n"
                            "    version (Ba2Version): The BA2 format"
                            " version to produce."
                        ),
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "add",
                        "path: str, data: bytes",
                        "None",
                        "bethkit_ba2_gnrl_writer_add",
                    ),
                    MethodDef(
                        "write_to",
                        "dest: str | Path",
                        "None",
                        "bethkit_ba2_gnrl_writer_write_to",
                    ),
                ],
            ),
            ClassDef(
                name="Ba2Dx10Writer",
                c_typedef="BethkitBa2Dx10Writer",
                context_manager=True,
                methods=[
                    MethodDef(
                        "__init__",
                        "version: Ba2Version",
                        "None",
                        "bethkit_ba2_dx10_writer_new",
                        manual_doc=(
                            "Create a new BA2 DX10 (texture) archive"
                            " writer.\n\n"
                            "Args:\n"
                            "    version (Ba2Version): The BA2 format"
                            " version to produce."
                        ),
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "add",
                        "path: str, data: bytes",
                        "None",
                        "bethkit_ba2_dx10_writer_add",
                    ),
                    MethodDef(
                        "write_to",
                        "dest: str | Path",
                        "None",
                        "bethkit_ba2_dx10_writer_write_to",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # cache.pyi
    # ------------------------------------------------------------------
    "cache": ModuleDef(
        file="cache.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from typing import Optional, Self",
            "",
            "from ._error import BethkitError",
            "from .load_order import GlobalFormId",
            "from .plugin import Plugin, Record",
        ],
        classes=[
            ClassDef(
                name="PluginCache",
                c_typedef="BethkitPluginCache",
                context_manager=True,
                methods=[
                    MethodDef(
                        "__init__",
                        "",
                        "None",
                        "bethkit_plugin_cache_new",
                        manual_doc=(
                            "Create a new, empty plugin cache."
                        ),
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "add",
                        "name: str, plugin: Plugin",
                        "None",
                        "bethkit_plugin_cache_add",
                    ),
                    MethodDef(
                        "__len__",
                        "",
                        "int",
                        "bethkit_plugin_cache_len",
                    ),
                    MethodDef(
                        "record_count",
                        "",
                        "int",
                        "bethkit_plugin_cache_record_count",
                        "property",
                    ),
                    MethodDef(
                        "resolve",
                        "plugin_name: str, object_id: int",
                        "Optional[Record]",
                        "bethkit_plugin_cache_resolve",
                    ),
                    MethodDef(
                        "find_by_editor_id",
                        "edid: str",
                        "Optional[tuple[Record, GlobalFormId]]",
                        "bethkit_plugin_cache_find_by_editor_id",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # load_order.pyi
    # ------------------------------------------------------------------
    "load_order": ModuleDef(
        file="load_order.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from dataclasses import dataclass",
            "from typing import Optional, Self",
            "",
            "from ._error import BethkitError",
            "from .enums import PluginKind",
        ],
        classes=[
            ClassDef(
                name="GlobalFormId",
                c_typedef="BethkitGlobalFormId",
                methods=[
                    MethodDef(
                        "plugin_name",
                        "",
                        "str",
                        "property",
                        manual_doc=(
                            "The source plugin file name."
                        ),
                    ),
                    MethodDef(
                        "object_id",
                        "",
                        "int",
                        "property",
                        manual_doc=(
                            "The 24-bit object ID component."
                        ),
                    ),
                ],
            ),
            ClassDef(
                name="LoadOrder",
                c_typedef="BethkitLoadOrder",
                context_manager=True,
                methods=[
                    MethodDef(
                        "__init__",
                        "",
                        "None",
                        "bethkit_load_order_new",
                        manual_doc=(
                            "Create a new, empty load order."
                        ),
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "push",
                        "name: str, kind: PluginKind",
                        "None",
                        "bethkit_load_order_push",
                    ),
                    MethodDef(
                        "__len__",
                        "",
                        "int",
                        "bethkit_load_order_len",
                    ),
                    MethodDef(
                        "resolve",
                        "form_id: int, source_plugin: str",
                        "Optional[GlobalFormId]",
                        "bethkit_load_order_resolve",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # strings.pyi
    # ------------------------------------------------------------------
    "strings": ModuleDef(
        file="strings.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from pathlib import Path",
            "from typing import Optional, Self",
            "",
            "from ._error import BethkitError",
            "from .enums import StringFileKind",
        ],
        classes=[
            ClassDef(
                name="StringTable",
                c_typedef="BethkitStringTable",
                context_manager=True,
                methods=[
                    MethodDef(
                        "new",
                        "kind: StringFileKind",
                        "StringTable",
                        "bethkit_string_table_new",
                        "classmethod",
                        manual_doc=(
                            "Create a new, empty string table of the"
                            " given *kind*."
                        ),
                    ),
                    MethodDef(
                        "open",
                        "path: str | Path",
                        "StringTable",
                        "bethkit_string_table_open",
                        "classmethod",
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "kind",
                        "",
                        "StringFileKind",
                        "bethkit_string_table_kind",
                        "property",
                    ),
                    MethodDef(
                        "__len__",
                        "",
                        "int",
                        "bethkit_string_table_len",
                    ),
                    MethodDef(
                        "get",
                        "id: int",
                        "Optional[bytes]",
                        "bethkit_string_table_get",
                    ),
                    MethodDef(
                        "get_str",
                        "id: int",
                        "Optional[str]",
                        manual_doc=(
                            "Return entry *id* decoded as UTF-8, or"
                            " ``None`` if absent."
                        ),
                    ),
                    MethodDef(
                        "insert",
                        "id: int, data: bytes",
                        "None",
                        "bethkit_string_table_insert",
                    ),
                    MethodDef(
                        "insert_new",
                        "data: bytes",
                        "int",
                        "bethkit_string_table_insert_new",
                    ),
                    MethodDef(
                        "remove",
                        "id: int",
                        "bool",
                        "bethkit_string_table_remove",
                    ),
                    MethodDef(
                        "write_to_file",
                        "path: str | Path",
                        "None",
                        "bethkit_string_table_write_to_file",
                    ),
                ],
            ),
            ClassDef(
                name="LocalizationSet",
                c_typedef="BethkitLocalizationSet",
                context_manager=True,
                methods=[
                    MethodDef(
                        "new",
                        "",
                        "LocalizationSet",
                        "bethkit_localization_set_new",
                        "classmethod",
                        manual_doc=(
                            "Create a new, empty localization set."
                        ),
                    ),
                    MethodDef(
                        "open",
                        "plugin_path: str | Path, language: str",
                        "LocalizationSet",
                        "bethkit_localization_set_open",
                        "classmethod",
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "get",
                        "kind: StringFileKind, id: int",
                        "Optional[bytes]",
                        "bethkit_localization_set_get",
                    ),
                    MethodDef(
                        "set",
                        "kind: StringFileKind, id: int, data: bytes",
                        "None",
                        "bethkit_localization_set_set",
                    ),
                    MethodDef(
                        "write",
                        "plugin_path: str | Path, language: str",
                        "None",
                        "bethkit_localization_set_write",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # schema.pyi
    # ------------------------------------------------------------------
    "schema": ModuleDef(
        file="schema.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from dataclasses import dataclass",
            "from typing import Any, Optional, Self, Union",
            "",
            "from ._error import BethkitError",
            "from .enums import FieldValueKind",
            "from .plugin import Record",
        ],
        classes=[
            ClassDef(
                name="TypedFormId",
                methods=[
                    MethodDef(
                        "raw",
                        "",
                        "int",
                        "property",
                        manual_doc="The raw file-local FormID value.",
                    ),
                    MethodDef(
                        "allowed_sigs",
                        "",
                        "tuple[bytes, ...]",
                        "property",
                        manual_doc=(
                            "The record signatures this FormID is"
                            " allowed to reference."
                        ),
                    ),
                ],
            ),
            ClassDef(
                name="EnumVal",
                methods=[
                    MethodDef(
                        "value",
                        "",
                        "int",
                        "property",
                        manual_doc="The raw integer value.",
                    ),
                    MethodDef(
                        "name",
                        "",
                        "Optional[str]",
                        "property",
                        manual_doc=(
                            "The enum variant name, or ``None`` if"
                            " the value is unknown."
                        ),
                    ),
                ],
            ),
            ClassDef(
                name="FlagsVal",
                methods=[
                    MethodDef(
                        "raw_value",
                        "",
                        "int",
                        "property",
                        manual_doc="The raw integer flags value.",
                    ),
                    MethodDef(
                        "active_names",
                        "",
                        "tuple[str, ...]",
                        "property",
                        manual_doc=(
                            "Names of all active (set) flag bits."
                        ),
                    ),
                ],
            ),
            ClassDef(
                name="NamedField",
                methods=[
                    MethodDef(
                        "name",
                        "",
                        "str",
                        "property",
                        manual_doc=(
                            "The human-readable field name from the"
                            " schema."
                        ),
                    ),
                    MethodDef(
                        "value",
                        "",
                        "FieldValue",
                        "property",
                        manual_doc="The decoded field value.",
                    ),
                ],
            ),
            ClassDef(
                name="SchemaRegistry",
                c_typedef="BethkitSchemaRegistry",
                methods=[
                    MethodDef(
                        "sse",
                        "",
                        "SchemaRegistry",
                        "bethkit_schema_registry_sse",
                        "classmethod",
                    ),
                    MethodDef(
                        "has",
                        "sig: bytes | str",
                        "bool",
                        "bethkit_schema_registry_has",
                    ),
                ],
            ),
            ClassDef(
                name="RecordView",
                c_typedef="BethkitRecordView",
                context_manager=True,
                methods=[
                    MethodDef(
                        "new",
                        "record: Record, sig: bytes | str, *,"
                        " localized: bool = ...",
                        "RecordView",
                        "bethkit_record_view_new",
                        "classmethod",
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "__len__",
                        "",
                        "int",
                        "bethkit_record_view_field_count",
                    ),
                    MethodDef(
                        "field_at",
                        "index: int",
                        "NamedField",
                        "bethkit_record_view_field_get",
                        manual_doc=(
                            "Return the :class:`NamedField` at"
                            " *index*.\n\n"
                            "Raises:\n"
                            "    BethkitError: When *index* is out"
                            " of bounds."
                        ),
                    ),
                    MethodDef(
                        "fields",
                        "",
                        "list[NamedField]",
                        manual_doc=(
                            "Return all decoded fields as a list."
                        ),
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # writer.pyi
    # ------------------------------------------------------------------
    "writer": ModuleDef(
        file="writer.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from pathlib import Path",
            "from typing import Self",
            "",
            "from ._error import BethkitError",
            "from .enums import Game",
        ],
        classes=[
            ClassDef(
                name="WritableRecord",
                c_typedef="BethkitWritableRecord",
                context_manager=True,
                methods=[
                    MethodDef(
                        "new",
                        "signature: bytes | str, flags: int = ...,"
                        " form_id: int = ...,"
                        " form_version: int = ...",
                        "WritableRecord",
                        "bethkit_writable_record_new",
                        "classmethod",
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "add_subrecord",
                        "signature: bytes | str, data: bytes",
                        "None",
                        "bethkit_writable_record_add_subrecord",
                    ),
                ],
            ),
            ClassDef(
                name="WritableGroup",
                c_typedef="BethkitWritableGroup",
                context_manager=True,
                methods=[
                    MethodDef(
                        "new",
                        "label: bytes | str, group_type: int = ...",
                        "WritableGroup",
                        "bethkit_writable_group_new",
                        "classmethod",
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "add_record",
                        "record: WritableRecord",
                        "None",
                        "bethkit_writable_group_add_record",
                    ),
                    MethodDef(
                        "add_group",
                        "child: WritableGroup",
                        "None",
                        "bethkit_writable_group_add_group",
                    ),
                ],
            ),
            ClassDef(
                name="PluginWriter",
                c_typedef="BethkitPluginWriter",
                context_manager=True,
                methods=[
                    MethodDef(
                        "__init__",
                        "game: Game, form_version: float = ...",
                        "None",
                        "bethkit_plugin_writer_new",
                        manual_doc=(
                            "Create a new plugin writer.\n\n"
                            "Args:\n"
                            "    game (Game): Target game.\n"
                            "    form_version (float): Plugin form"
                            " version (e.g. ``44.0`` for Skyrim SE)."
                        ),
                    ),
                    MethodDef(
                        "close",
                        "",
                        "None",
                        manual_doc=_CLOSE_DOC,
                    ),
                    MethodDef(
                        "add_group",
                        "group: WritableGroup",
                        "None",
                        "bethkit_plugin_writer_add_group",
                    ),
                    MethodDef(
                        "write_to_file",
                        "path: str | Path",
                        "None",
                        "bethkit_plugin_writer_write_to_file",
                    ),
                    MethodDef(
                        "write_to_bytes",
                        "",
                        "bytes",
                        "bethkit_plugin_writer_write_to_bytes",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------
    # enums.pyi  (values come directly from bethkit.h enum definitions)
    # ------------------------------------------------------------------
    "enums": ModuleDef(
        file="enums.pyi",
        imports=[
            "from __future__ import annotations",
            "",
            "from enum import IntEnum",
        ],
        classes=[
            ClassDef(
                name="Game",
                c_typedef="BethkitGame",
                methods=[],
            ),
            ClassDef(
                name="PluginKind",
                c_typedef="BethkitPluginKind",
                methods=[],
            ),
            ClassDef(
                name="StringFileKind",
                c_typedef="BethkitStringFileKind",
                methods=[],
            ),
            ClassDef(
                name="BsaVersion",
                c_typedef="BethkitBsaVersion",
                methods=[],
            ),
            ClassDef(
                name="Ba2Version",
                c_typedef="BethkitBa2Version",
                methods=[],
            ),
            ClassDef(
                name="FieldValueKind",
                c_typedef="BethkitFieldValueKind",
                methods=[],
            ),
        ],
    ),
}
