"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Optional

from bethkit.records import _schema

if __package__:
    from . import _generation_names
else:
    import _generation_names


class RecordGenerator:
    """Compiles one record grammar and all of its payload classes."""

    __record: _schema.RecordDefinition
    __digest: str
    __signature: str
    __names: dict[str, str]
    __blocks: list[str]
    __nodes: dict[str, _schema.SchemaNode]
    __active: set[str]
    __variants: set[str]

    def __init__(self, record: _schema.RecordDefinition, digest: str) -> None:
        """Indexes nodes and initializes deterministic output.

        Args:
            record: Complete main-record definition.
            digest: Native schema payload hash.

        Raises:
            ValueError: The record signature cannot be represented as bytes.
            UnicodeDecodeError: The record signature contains non-ASCII bytes.
        """

        self.__record = record
        self.__digest = digest
        self.__signature = bytes(record.signature).decode("ascii")
        self.__names = {}
        self.__blocks = []
        self.__nodes = {}
        self.__active = set()
        self.__variants = set()
        self.__index(record.root)

    def __index(self, node: _schema.SchemaNode) -> None:
        """Indexes nested definitions by authoritative schema path.

        Args:
            node: Root of the structural subtree to register.
        """

        self.__nodes[node.path] = node
        for child in (
            *node.children,
            *node.fields,
            *node.alternatives,
            *node.variants,
        ):
            self.__index(child)
        for child in (node.child, node.payload, node.element):
            if child is not None:
                self.__index(child)

    def __required(
        self, child: Optional[_schema.SchemaNode], node: _schema.SchemaNode
    ) -> _schema.SchemaNode:
        """Rejects malformed nodes instead of generating unknown types.

        Args:
            child: Nested definition required by the enclosing node kind.
            node: Enclosing node used to identify an invalid schema path.

        Returns:
            The required nested definition.

        Raises:
            ValueError: The required child definition is absent.
        """

        if child is None:
            raise ValueError(f"Missing child for {node.path}")
        return child

    def __enum(self, node: _schema.SchemaNode, flags: bool) -> str:
        """Generates named enums while retaining unknown on-disk values.

        Args:
            node: Primitive enumeration or flag definition.
            flags: Whether values represent bit positions rather than numbers.

        Returns:
            The generated enumeration class name.

        Raises:
            ValueError: Primitive metadata is missing or a bit is negative.
        """

        if node.path in self.__names:
            return self.__names[node.path]
        primitive = node.primitive
        if primitive is None:
            raise ValueError(f"Missing primitive for {node.path}")
        name = _generation_names.class_name(node.name) + str(node.id)
        self.__names[node.path] = name
        base = "enum.IntFlag" if flags else "_values.OpenIntEnum"
        members = primitive.bits if flags else primitive.values
        used: set[str] = set()
        lines = [
            f"class {name}({base}):",
            '    """Named values from the pinned schema."""',
            "",
        ]
        for index, (value, label) in enumerate(members):
            member = _generation_names.identifier(label, upper=True)
            if member in used:
                member += f"_{index}"
            used.add(member)
            number = 1 << value if flags else value
            lines.append(f"    {member} = {number}")
        if not members:
            lines.append("    NONE = 0")
        self.__blocks.append("\n".join(lines))
        return name

    def __variant(self, node: _schema.SchemaNode) -> str:
        """Shares immutable variant identities between generated annotations.

        Args:
            node: Alternative identified by its authoritative schema path.

        Returns:
            Name of the generated shared variant marker.
        """

        name = f"_VARIANT_{node.id}"
        if node.path not in self.__variants:
            self.__variants.add(node.path)
            self.__blocks.append(
                f"{name}: _base.Variant = _base.Variant(\n"
                f"    path={_generation_names.literal(node.path, 8)}\n)"
            )
        return name

    def annotation(self, node: _schema.SchemaNode) -> str:
        """Maps every supported schema node to a concrete Python type.

        Args:
            node: Grammar or payload node whose value type is needed.

        Returns:
            A concrete Python annotation expression for this node.

        Raises:
            ValueError: A required definition is absent or unsupported.
        """

        kind = node.kind
        if kind == "subrecord":
            return self.annotation(self.__required(node.payload, node))
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
                return self.__enum(node, False)
            if primitive.type == "flags":
                return self.__enum(node, True)
            raise ValueError(f"Unsupported primitive at {node.path}")
        if kind in {"struct", "optional_struct", "sequence", "unordered"}:
            return self.model(node)
        if kind == "array":
            element = self.annotation(self.__required(node.element, node))
            return f"tuple[{element}, ...]"
        if kind == "repeat":
            child_type = self.annotation(self.__required(node.child, node))
            return f"tuple[{child_type}, ...]"
        if kind in {"union", "choice", "selected_choice"}:
            variants = node.variants or node.alternatives
            types = [
                f"Annotated[{self.annotation(n)}, {self.__variant(n)}]"
                for n in variants
            ]
            if not types:
                raise ValueError(f"Empty union at {node.path}")
            return " | ".join(types)
        if kind in {"compressed", "terminated"}:
            return self.annotation(self.__required(node.child, node))
        if kind == "reference":
            if node.target not in self.__nodes:
                raise ValueError(f"Unresolved reference at {node.path}")
            return self.annotation(self.__nodes[node.target])
        if kind == "custom" and node.decoder == "xedit.dtinteger":
            return "Literal[0]"
        raise ValueError(f"Unsupported node {kind}: {node.path}")

    def model(self, node: _schema.SchemaNode, root: bool = False) -> str:
        """Generates a hierarchical class with typed field references.

        Args:
            node: Record grammar or payload structure to compile.
            root: Whether this is the public top-level record model.

        Returns:
            Name of the generated immutable model class.

        Raises:
            ValueError: Nested type information is missing or unsupported.
        """

        if node.path in self.__names:
            return self.__names[node.path]
        if node.path in self.__active:
            raise ValueError(
                f"Recursive schema requires explicit support: {node.path}"
            )
        self.__active.add(node.path)
        if root:
            name = _generation_names.NAMES.get(
                self.__signature,
                _generation_names.class_name(self.__record.name) + "Record",
            )
        else:
            name = _generation_names.class_name(node.name) + str(node.id)
        self.__names[node.path] = name
        members = node.fields or node.children
        grammar = node.kind in {"sequence", "unordered"}
        definitions: list[tuple[str, str, str]] = []
        bindings: list[str] = []
        used: set[str] = set()
        for index, child in enumerate(members):
            key = _generation_names.identifier(child.name)
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
            path_literal = _generation_names.literal(child.path, 12)
            lines = [
                f"        {key!r}: _base.Binding(",
                f"            path={path_literal},",
                f"            kind={child.kind!r},",
                "            name="
                f"{_generation_names.literal(child.name, 12)},",
            ]
            if repeated and child.child is not None:
                lines.append(
                    "            repeated_path="
                    f"{_generation_names.literal(child.child.path, 12)},"
                )
                lines.append(f"            child_kind={child.child.kind!r},")
            lines.append("        ),")
            bindings.extend(lines)
        base = "_base.RecordModel" if root else "_base.StructModel"
        lines = [
            f"class {name}({base}, frozen=True):",
            '    """Schema-generated immutable structural view."""',
            "",
            "    _schema_path: ClassVar[str] = "
            f"{_generation_names.literal(node.path, 8)}",
            f"    _grammar: ClassVar[bool] = {grammar!r}",
        ]
        if root:
            lines.extend(
                [
                    f"    signature: ClassVar[str] = {self.__signature!r}",
                    "    schema_sha256: ClassVar[str] = "
                    f"{_generation_names.literal(self.__digest, 8)}",
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
        self.__blocks.append("\n".join(lines))
        self.__active.remove(node.path)
        return name

    def render(self) -> tuple[str, str]:
        """Returns the root class name and deterministic module source.

        Returns:
            Public record class name paired with its complete module source.

        Raises:
            ValueError: The record contains unsupported or missing definitions.
        """

        name = self.model(self.__record.root, root=True)
        return name, _generation_names.HEADER + "\n\n\n".join(
            self.__blocks
        ) + "\n"
