"""
Copyright (c) Modding Forge
"""

# Generates statically typed record views from a native schema export.

from __future__ import annotations

import argparse
import hashlib
import keyword
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

from bethkit import _ffi
from bethkit.records import _schema

_HEADER = '''"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values

'''
_NAMES = {
    "QUST": "QuestRecord",
    "INFO": "InfoRecord",
    "PERK": "PerkRecord",
    "NPC_": "NpcRecord",
    "WEAP": "WeaponRecord",
    "ARMO": "ArmorRecord",
}


def identifier(name: str, *, upper: bool = False) -> str:
    """Converts schema labels to stable Python identifiers.

    Args:
        name: Original schema label.
        upper: Whether to produce an enumeration member name.

    Returns:
        A non-keyword identifier.
    """

    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    text = text.upper() if upper else text.lower()
    if not text:
        text = "VALUE" if upper else "value"
    if text[0].isdigit():
        text = ("VALUE_" if upper else "value_") + text
    if keyword.iskeyword(text) or text.startswith("model_"):
        text += "_value"
    if text in {
        "field",
        "signature",
        "schema_sha256",
        "from_record",
        "l",
        "I",
        "O",
    }:
        text += "_value"
    if len(text) > 54:
        suffix = hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]
        text = text[:45] + "_" + suffix
    return text


def class_name(name: str) -> str:
    """Converts a schema name into a compact class name.

    Args:
        name: Schema label.

    Returns:
        A valid UpperCamelCase identifier.
    """

    result = "".join(part.title() for part in identifier(name).split("_"))
    return result[:48] or "Value"


def literal(value: str, indent: int = 4) -> str:
    """Splits long string constants without changing their content.

    Args:
        value: String to represent in generated source.
        indent: Indentation for continued chunks.

    Returns:
        A Python string literal expression.
    """

    encoded = repr(value)
    if len(encoded) + indent < 64:
        return encoded
    width = 54
    parts = [repr(value[i : i + width]) for i in range(0, len(value), width)]
    padding = " " * indent
    return "(\n" + "\n".join(padding + p for p in parts) + "\n)"


class RecordGenerator:
    """Compiles one record grammar and all of its payload classes."""

    def __init__(self, record: _schema.RecordDefinition, digest: str) -> None:
        """Indexes nodes and initializes deterministic output.

        Args:
            record: Complete main-record definition.
            digest: Native schema payload hash.
        """

        self.record = record
        self.digest = digest
        self.signature = bytes(record.signature).decode("ascii")
        self.names: dict[str, str] = {}
        self.blocks: list[str] = []
        self.nodes: dict[str, _schema.SchemaNode] = {}
        self.active: set[str] = set()
        self.variants: set[str] = set()
        self._index(record.root)

    def _index(self, node: _schema.SchemaNode) -> None:
        """Indexes nested definitions by authoritative schema path."""

        self.nodes[node.path] = node
        for child in (
            *node.children,
            *node.fields,
            *node.alternatives,
            *node.variants,
        ):
            self._index(child)
        for child in (node.child, node.payload, node.element):
            if child is not None:
                self._index(child)

    def _required(
        self, child: Optional[_schema.SchemaNode], node: _schema.SchemaNode
    ) -> _schema.SchemaNode:
        """Rejects malformed nodes instead of generating unknown types."""

        if child is None:
            raise ValueError(f"Missing child for {node.path}")
        return child

    def _enum(self, node: _schema.SchemaNode, flags: bool) -> str:
        """Generates named enums while retaining unknown on-disk values."""

        if node.path in self.names:
            return self.names[node.path]
        primitive = node.primitive
        if primitive is None:
            raise ValueError(f"Missing primitive for {node.path}")
        name = class_name(node.name) + str(node.id)
        self.names[node.path] = name
        base = "enum.IntFlag" if flags else "_values.OpenIntEnum"
        members = primitive.bits if flags else primitive.values
        used: set[str] = set()
        lines = [
            f"class {name}({base}):",
            '    """Named values from the pinned schema."""',
            "",
        ]
        for index, (value, label) in enumerate(members):
            member = identifier(label, upper=True)
            if member in used:
                member += f"_{index}"
            used.add(member)
            number = 1 << value if flags else value
            lines.append(f"    {member} = {number}")
        if not members:
            lines.append("    NONE = 0")
        self.blocks.append("\n".join(lines))
        return name

    def _variant(self, node: _schema.SchemaNode) -> str:
        """Shares immutable variant identities between generated annotations."""

        name = f"_VARIANT_{node.id}"
        if node.path not in self.variants:
            self.variants.add(node.path)
            self.blocks.append(
                f"{name}: _base.Variant = _base.Variant(\n"
                f"    path={literal(node.path, 8)}\n)"
            )
        return name

    def annotation(self, node: _schema.SchemaNode) -> str:
        """Maps every supported schema node to a concrete Python type."""

        kind = node.kind
        if kind == "subrecord":
            return self.annotation(self._required(node.payload, node))
        if kind == "primitive":
            primitive = node.primitive
            if primitive is None:
                raise ValueError(f"Missing primitive for {node.path}")
            if primitive.type == "integer":
                integer = primitive.integer
                if integer is None:
                    raise ValueError(f"Missing integer layout: {node.path}")
                bits = integer.width * 8
                low = -(1 << (bits - 1)) if integer.signed else 0
                high = (1 << (bits - int(integer.signed))) - 1
                bounds = f"strict=True, ge={low}, le={high}"
                return f"Annotated[int, pydantic.Field({bounds})]"
            if primitive.type == "packed_unsigned":
                return "Annotated[int, pydantic.Field(ge=0, le=1073741823)]"
            if primitive.type == "float":
                return "float"
            if primitive.type == "string":
                localized = primitive.string.get("localized", False)
                return "str | _values.UInt32" if localized else "str"
            if primitive.type == "form_id":
                return "_values.FormId"
            if primitive.type in {"bytes", "unused"}:
                return "bytes"
            if primitive.type == "enumeration":
                return self._enum(node, False)
            if primitive.type == "flags":
                return self._enum(node, True)
            raise ValueError(f"Unsupported primitive at {node.path}")
        if kind in {"struct", "optional_struct", "sequence", "unordered"}:
            return self.model(node)
        if kind == "array":
            element = self.annotation(self._required(node.element, node))
            return f"tuple[{element}, ...]"
        if kind == "repeat":
            child_type = self.annotation(self._required(node.child, node))
            return f"tuple[{child_type}, ...]"
        if kind in {"union", "choice", "selected_choice"}:
            variants = node.variants or node.alternatives
            types = [
                f"Annotated[{self.annotation(n)}, {self._variant(n)}]"
                for n in variants
            ]
            if not types:
                raise ValueError(f"Empty union at {node.path}")
            return " | ".join(types)
        if kind in {"compressed", "terminated"}:
            return self.annotation(self._required(node.child, node))
        if kind == "reference":
            if node.target not in self.nodes:
                raise ValueError(f"Unresolved reference at {node.path}")
            return self.annotation(self.nodes[node.target])
        if kind == "custom" and node.decoder == "xedit.dtinteger":
            return "Literal[0]"
        raise ValueError(f"Unsupported node {kind}: {node.path}")

    def model(self, node: _schema.SchemaNode, root: bool = False) -> str:
        """Generates a hierarchical class with typed field references."""

        if node.path in self.names:
            return self.names[node.path]
        if node.path in self.active:
            raise ValueError(
                f"Recursive schema requires explicit support: {node.path}"
            )
        self.active.add(node.path)
        if root:
            name = _NAMES.get(
                self.signature, class_name(self.record.name) + "Record"
            )
        else:
            name = class_name(node.name) + str(node.id)
        self.names[node.path] = name
        members = node.fields or node.children
        grammar = node.kind in {"sequence", "unordered"}
        definitions: list[tuple[str, str, str]] = []
        bindings: list[str] = []
        used: set[str] = set()
        for index, child in enumerate(members):
            key = identifier(child.name)
            if key in used:
                key += f"_{child.id}"
            used.add(key)
            typ = self.annotation(child)
            repeated = child.kind == "repeat"
            optional = (
                grammar
                and not repeated
                or child.condition is not None
                or node.kind == "optional_struct"
                and index >= node.optional_from
            )
            if optional:
                typ = f"Optional[{typ}]"
            default = "()" if repeated else "None" if optional else "..."
            definitions.append((key, typ, default))
            path_literal = literal(child.path, 12)
            lines = [
                f"        {key!r}: _base.Binding(",
                f"            path={path_literal},",
                f"            kind={child.kind!r},",
                f"            name={literal(child.name, 12)},",
            ]
            if repeated and child.child is not None:
                lines.append(
                    "            repeated_path="
                    f"{literal(child.child.path, 12)},"
                )
                lines.append(f"            child_kind={child.child.kind!r},")
            lines.append("        ),")
            bindings.extend(lines)
        base = "_base.RecordModel" if root else "_base.StructModel"
        lines = [
            f"class {name}({base}, frozen=True):",
            '    """Schema-generated immutable structural view."""',
            "",
            f"    _schema_path: ClassVar[str] = {literal(node.path, 8)}",
            f"    _grammar: ClassVar[bool] = {grammar!r}",
        ]
        if root:
            lines.extend(
                [
                    f"    signature: ClassVar[str] = {self.signature!r}",
                    "    schema_sha256: ClassVar[str] = "
                    f"{literal(self.digest, 8)}",
                ]
            )
        lines.extend(
            [
                "    _bindings: ClassVar[dict[str, _base.Binding]] = {",
                *bindings,
                "    }",
                "",
            ]
        )
        for key, typ, default in definitions:
            lines.extend(
                [
                    f"    {key}: {typ}"
                    + (f" = {default}" if default != "..." else ""),
                    '    """Value decoded from this schema node."""',
                    "",
                ]
            )
        for key, typ, _ in definitions:
            lines.extend(
                [
                    "    @overload",
                    f"    def field(self, name: Literal[{key!r}])"
                    f" -> _base.FieldRef[{typ}]:",
                    '        """Returns the typed field reference."""',
                    "",
                    "        ...",
                    "",
                ]
            )
        if definitions:
            lines.extend(
                [
                    "    @overload",
                    "    def field(self, name: str) -> _base.FieldReference:",
                    '        """Returns a dynamically selected reference."""',
                    "",
                    "        ...",
                    "",
                    "    def field(self, name: str) -> _base.FieldReference:",
                    '        """Returns the snapshot field reference."""',
                    "",
                    "        return super().field(name)",
                ]
            )
        self.blocks.append("\n".join(lines))
        self.active.remove(node.path)
        return name

    def render(self) -> tuple[str, str]:
        """Returns the root class name and deterministic module source."""

        name = self.model(self.record.root, root=True)
        return name, _HEADER + "\n\n\n".join(self.blocks) + "\n"


def generate(graph: _schema.SchemaGraph) -> dict[str, str]:
    """Compiles a complete game package without any dynamic type fallback.

    Args:
        graph: Validated, versioned native schema graph.

    Returns:
        Relative module filenames and deterministic source code.

    Raises:
        ValueError: A node cannot retain its full type information.
    """

    if graph.manifest.get("game") != "skyrim_se":
        raise ValueError(
            "This generator currently targets the Skyrim SE package."
        )
    files: dict[str, str] = {}
    exports: dict[str, str] = {}
    for record in sorted(graph.records, key=lambda r: r.signature):
        generator = RecordGenerator(record, graph.payload_sha256)
        name, source = generator.render()
        module = bytes(record.signature).decode("ascii").lower().rstrip("_")
        files[module + ".py"] = source
        if name in exports:
            raise ValueError(f"Duplicate public record class {name}")
        exports[name] = module
    init = [
        '"""',
        "Copyright (c) Modding Forge",
        '"""',
        "",
        "# Lazily loaded Skyrim SE record models generated from xEdit.",
        "",
        "from __future__ import annotations",
        "",
        "import importlib",
        "from typing import TYPE_CHECKING",
        "",
        "if TYPE_CHECKING:",
    ]
    for name, module in sorted(exports.items()):
        init.append(f"    from .{module} import {name} as {name}")
    init.extend(["", "_EXPORTS: dict[str, str] = {"])
    for name, module in sorted(exports.items()):
        init.append(f"    {name!r}: {module!r},")
    init.extend(
        [
            "}",
            "",
            "__all__ = " + repr(sorted(exports)),
            "",
            "",
            "def __getattr__(name: str) -> object:",
            '    """Loads only the requested record module.',
            "",
            "    Args:",
            "        name: Record class exported by this game package.",
            "",
            "    Returns:",
            "        The requested generated class.",
            "",
            "    Raises:",
            "        AttributeError: The class is not part of this schema.",
            '    """',
            "",
            "    if name not in _EXPORTS:",
            "        raise AttributeError(name)",
            "    module = importlib.import_module("
            'f"{__name__}.{_EXPORTS[name]}")',
            "    value: object = getattr(module, name)",
            "    globals()[name] = value",
            "    return value",
            "",
        ]
    )
    files["__init__.py"] = "\n".join(init)
    return files


def normalized_files(files: dict[str, str], ruff: Path) -> dict[str, str]:
    """Formats deterministic generated code using the project's Ruff rules.

    Args:
        files: Unformatted generated sources indexed by relative filename.
        ruff: Installed Ruff executable used both for generation and checks.

    Returns:
        Sources with unused imports removed and stable formatting applied.

    Raises:
        subprocess.CalledProcessError: Formatting or lint validation fails.
    """

    config = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with tempfile.TemporaryDirectory(prefix="bethkit_models_") as directory:
        staging = Path(directory)
        for filename, source in files.items():
            (staging / filename).write_text(
                source, encoding="utf-8", newline="\n"
            )
        subprocess.run(
            [
                str(ruff),
                "check",
                "--config",
                str(config),
                "--select",
                "F401,I",
                "--fix",
                str(staging),
            ],
            check=True,
        )
        subprocess.run(
            [str(ruff), "format", "--config", str(config), str(staging)],
            check=True,
        )
        subprocess.run(
            [str(ruff), "check", "--config", str(config), str(staging)],
            check=True,
        )
        return {
            filename: (staging / filename).read_text("utf-8")
            for filename in files
        }


def main() -> None:
    """Loads one native schema and regenerates or verifies its Python models."""

    parser = argparse.ArgumentParser(
        description="Generate typed record views from a pinned native schema."
    )
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--ruff", type=Path, default=shutil.which("ruff"))
    arguments = parser.parse_args()
    schema_path: Path = arguments.schema
    output: Path = arguments.output
    lib = _ffi.load_lib()
    package = lib.bethkit_schema_package_open(_ffi.enc(schema_path))
    if not package:
        _ffi.raise_last_error(lib)
    try:
        pointer = lib.bethkit_schema_package_graph_json(package)
        if not pointer:
            _ffi.raise_last_error(lib)
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
    finally:
        lib.bethkit_schema_package_free(package)
    graph = _schema.SchemaGraph.model_validate_json(text)
    if arguments.ruff is None:
        raise SystemExit(
            "Install the development Ruff dependency or pass --ruff."
        )
    files = normalized_files(generate(graph), Path(arguments.ruff))
    for filename, source in files.items():
        destination = output / filename
        if arguments.check:
            if (
                not destination.exists()
                or destination.read_text("utf-8") != source
            ):
                raise SystemExit(f"Generated model differs: {destination}")
        else:
            output.mkdir(parents=True, exist_ok=True)
            destination.write_text(source, encoding="utf-8", newline="\n")
    digest = hashlib.sha256(schema_path.read_bytes()).hexdigest()
    print(
        f"{len(graph.records)} records; schema file SHA-256 {digest}; "
        f"payload {graph.payload_sha256}"
    )


if __name__ == "__main__":
    main()
