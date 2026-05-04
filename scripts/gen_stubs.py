"""
Copyright (c) Modding Forge

Generate ``.pyi`` stub files for the bethkit Python package.

The stubs are derived from ``bethkit.h`` (produced by cbindgen) and
the mapping table in :mod:`stub_map`.  Running this script keeps the
Python type annotations in sync with the Rust source without touching
the hand-written ``.py`` files.

Usage::

    python scripts/gen_stubs.py [--header PATH] [--out-dir PATH]

Default paths (relative to the ``bethkit.py/`` workspace root):

* ``--header``:  ``../../bethkit/crates/bethkit-ffi/bethkit.h``
* ``--out-dir``: ``src/bethkit``
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from enum import Enum, auto
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Resolve the scripts/ directory so we can import stub_map even when the
# script is invoked from a different working directory.
# ---------------------------------------------------------------------------
_SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPTS_DIR))

from stub_map import ClassDef, MethodDef, ModuleDef, MODULES  # noqa: E402

# ---------------------------------------------------------------------------
# Default paths
# ---------------------------------------------------------------------------

_REPO_ROOT = _SCRIPTS_DIR.parent.parent
_DEFAULT_HEADER = (
    _REPO_ROOT / "bethkit" / "crates" / "bethkit-ffi" / "bethkit.h"
)
_DEFAULT_OUT = _SCRIPTS_DIR.parent / "src" / "bethkit"

# ---------------------------------------------------------------------------
# Header parser
# ---------------------------------------------------------------------------


class _State(Enum):
    """State machine states for the C header parser."""

    SCAN = auto()
    IN_DOC = auto()
    AFTER_DOC = auto()


def parse_header(path: Path) -> dict[str, str]:
    """
    Parse ``bethkit.h`` and return a mapping of C identifier to raw docstring.

    The raw docstring has ``/**``, ``*/``, and leading ``" * "`` stripped but
    is otherwise unchanged (section headers like ``# Errors`` are preserved).

    Args:
        path (Path): Absolute path to ``bethkit.h``.

    Returns:
        dict[str, str]: Mapping from C name (function or type) to docstring.

    Raises:
        FileNotFoundError: When *path* does not exist.
        OSError: When the file cannot be read.
    """

    docs: dict[str, str] = {}
    state: _State = _State.SCAN
    current_lines: list[str] = []

    with path.open(encoding="utf-8") as fh:
        lines = fh.readlines()

    for line in lines:
        stripped: str = line.strip()

        if state == _State.SCAN:
            if stripped == "/**":
                state = _State.IN_DOC
                current_lines = []

        elif state == _State.IN_DOC:
            if stripped == "*/":
                state = _State.AFTER_DOC
            elif stripped.startswith("* "):
                current_lines.append(stripped[2:])
            elif stripped == "*":
                current_lines.append("")
            # ignore lines that don't match expected patterns

        elif state == _State.AFTER_DOC:
            if stripped:
                name: Optional[str] = _extract_c_name(stripped)
                if name:
                    docs[name] = "\n".join(current_lines).strip()
                state = _State.SCAN
                current_lines = []

    return docs


def _extract_c_name(decl: str) -> Optional[str]:
    """
    Extract a C identifier from a declaration line.

    Handles function declarations, ``typedef enum/struct``, enum values, and
    simple type aliases.

    Args:
        decl (str): A single line from the C header.

    Returns:
        Optional[str]: The extracted identifier, or ``None`` when not found.
    """

    # typedef … Name;  →  the last word before semicolon is the typedef name
    if "typedef" in decl:
        m_semi = re.search(r"(\w+)\s*;", decl)
        if m_semi:
            return m_semi.group(1)
        # typedef enum Name {
        m_enum = re.search(
            r"typedef\s+(?:enum|struct|union)\s+(\w+)\s*\{", decl
        )
        if m_enum:
            return m_enum.group(1)

    # Function declaration: ReturnType name(…)
    m_func = re.search(r"(\w+)\s*\(", decl)
    if m_func:
        return m_func.group(1)

    # Enum variant: Name = value,  or  Name,
    m_variant = re.match(r"\s*(\w+)\s*(?:=|,)", decl)
    if m_variant:
        return m_variant.group(1)

    return None


# ---------------------------------------------------------------------------
# Docstring adaptation
# ---------------------------------------------------------------------------

# Sentences/phrases that are only relevant at the C level.
_REMOVE_PATTERNS: list[re.Pattern[str]] = [
    re.compile(
        r"[^.]*\bmust be freed with[^.]*\.\s*",
        re.IGNORECASE,
    ),
    re.compile(
        r"[^.]*\bCreated by[^.]*\.\s*",
        re.IGNORECASE,
    ),
    re.compile(
        r"[^.]*(?:The caller (?:owns|must not free)"
        r"|Passing a null pointer is a no-op"
        r"|caller takes ownership)[^.]*\.\s*",
        re.IGNORECASE,
    ),
    re.compile(r"\s*\(call \[`?\w+`?\] for details\)", re.IGNORECASE),
    re.compile(r"\bBorrows\.\s*", re.IGNORECASE),
    re.compile(r"\bOwnership transferred\.\s*", re.IGNORECASE),
    re.compile(r"NUL-terminated\s+", re.IGNORECASE),
]


def _clean_text(text: str) -> str:
    """
    Remove C-specific phrases and replace C terminology with Python equivalents.

    Args:
        text (str): Raw text from the C header docstring.

    Returns:
        str: Cleaned text suitable for Python docstrings.
    """

    for pattern in _REMOVE_PATTERNS:
        text = pattern.sub("", text)

    text = text.replace("null", "None")

    # [`name`] or `name` → *name* (reStructuredText italic)
    text = re.sub(r"\[`(\w+)`\]", r"*\1*", text)
    text = re.sub(r"`(\w+)`", r"*\1*", text)

    # Collapse runs of spaces (but preserve newlines)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def _parse_c_args(
    arg_lines: list[str],
) -> list[tuple[str, str]]:
    """
    Parse C-style argument list lines into (name, description) pairs.

    Args:
        arg_lines (list[str]): Lines from the ``# Arguments`` section.

    Returns:
        list[tuple[str, str]]: Pairs of (param_name, cleaned_description).
    """

    pairs: list[tuple[str, str]] = []
    for line in arg_lines:
        m = re.match(r"\*\s+[`*]?(\w+)[`*]?\s+[—\-–]+\s+(.+)", line)
        if not m:
            continue
        param_name: str = m.group(1)
        desc: str = _clean_text(m.group(2))
        if desc:
            pairs.append((param_name, desc))
    return pairs


def adapt_docstring(
    raw: str,
    method: MethodDef,
) -> str:
    """
    Adapt a raw C header docstring to Python Google-style format.

    Extracts the summary paragraph, adapts argument descriptions using the
    Python parameter types from *method*, and converts the ``# Errors``
    section to a ``Raises`` block.

    Args:
        raw (str): Raw docstring extracted from the C header.
        method (MethodDef): Python method definition (for parameter types).

    Returns:
        str: A formatted Python docstring body (without the outer quotes).
    """

    if not raw:
        return ""

    # Split into sections keyed by lowercase section name.
    sections: dict[str, list[str]] = {"": []}
    current_key: str = ""
    for line in raw.split("\n"):
        m = re.match(r"^# (.+)$", line)
        if m:
            current_key = m.group(1).lower()
            sections[current_key] = []
        else:
            sections.setdefault(current_key, []).append(line)

    # Summary: first paragraph only.
    preamble_raw: str = "\n".join(sections.get("", [])).strip()
    first_blank = preamble_raw.find("\n\n")
    if first_blank > 0:
        preamble_raw = preamble_raw[:first_blank].strip()
    summary: str = _clean_text(preamble_raw)

    parts: list[str] = []
    if summary:
        parts.append(summary)

    # Args section: use C descriptions + Python types from MethodDef.
    c_arg_pairs = _parse_c_args(sections.get("arguments", []))
    if c_arg_pairs:
        # Build a name→type map from the Python params string.
        param_types: dict[str, str] = {}
        if method.params:
            for segment in _split_params(method.params):
                if ": " in segment:
                    pname, ptype = segment.split(": ", 1)
                    param_types[pname.strip().lstrip("*")] = ptype.strip()

        arg_lines: list[str] = []
        for pname, desc in c_arg_pairs:
            ptype: str = param_types.get(pname, "")
            if not ptype:
                # Skip C-only parameters (e.g. self-pointer 'lo', output 'out')
                # that have no counterpart in the Python signature.
                continue
            # Strip trailing punctuation before appending the sentence dot.
            desc_clean = desc.rstrip(". ")
            arg_lines.append(f"    {pname} ({ptype}): {desc_clean}.")
        if arg_lines:
            parts.append("Args:\n" + "\n".join(arg_lines))

    # Returns section (only when meaningful).
    returns_lines: list[str] = sections.get("returns", [])
    if returns_lines and method.ret not in ("None", ""):
        ret_text: str = _clean_text(
            " ".join(l.strip() for l in returns_lines if l.strip())
        )
        # Strip "Returns X on success" boilerplate.
        ret_text = re.sub(
            r"^Returns (?:a pointer to )?(?:the )?",
            "",
            ret_text,
            flags=re.IGNORECASE,
        )
        if ret_text:
            parts.append(
                f"Returns:\n    {method.ret}: {ret_text}"
            )

    # Raises section from # Errors.
    error_lines: list[str] = sections.get("errors", [])
    if error_lines:
        err_raw: str = " ".join(
            l.strip() for l in error_lines if l.strip()
        )
        # Remove "Returns X and sets the last error when/if"
        err_raw = re.sub(
            r"^Returns (?:null|None|-1) and sets the last error "
            r"(?:when|if)\s+",
            "",
            err_raw,
            flags=re.IGNORECASE,
        )
        err_text: str = _clean_text(err_raw)
        if err_text:
            # Capitalise first character.
            err_text = err_text[0].upper() + err_text[1:]
            wrapped = textwrap.fill(
                err_text,
                width=72,
                subsequent_indent="        ",
            )
            parts.append(f"Raises:\n    BethkitError: {wrapped}")

    return "\n\n".join(parts)


def _split_params(params: str) -> list[str]:
    """
    Split a parameter string on top-level commas (not inside brackets).

    Args:
        params (str): Parameter string, e.g.
            ``'path: str | Path, game: Game'``.

    Returns:
        list[str]: Individual parameter segments.
    """

    segments: list[str] = []
    depth: int = 0
    current: str = ""
    for ch in params:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            segments.append(current.strip())
            current = ""
        else:
            current += ch
    if current.strip():
        segments.append(current.strip())
    return segments


# ---------------------------------------------------------------------------
# Enum value extractor
# ---------------------------------------------------------------------------


def extract_enum_values(
    docs: dict[str, str],
    c_enum_name: str,
) -> list[tuple[str, str]]:
    """
    Return (variant_name, docstring) pairs for a C enum.

    Scans *docs* for keys that match variant names inside the given
    *c_enum_name* by checking all single-word uppercase or mixed-case keys
    that are not typedef/function names.

    Args:
        docs (dict[str, str]): Full parsed docs from :func:`parse_header`.
        c_enum_name (str): The C enum typedef name, e.g. ``'BethkitGame'``.

    Returns:
        list[tuple[str, str]]: Ordered list of (variant_name, docstring).
    """

    # We need to re-parse the header to get ordered enum variants.
    # Since we only have the docs dict here, we return what we can.
    # The emitter will use this to produce class body with value docs.
    # Variant names in bethkit.h are simple PascalCase/UPPER words.
    variants: list[tuple[str, str]] = []
    # known enum variant names per typedef
    _ENUM_VARIANTS: dict[str, list[str]] = {
        "BethkitGame": [
            "SkyrimSe",
            "Fallout4",
            "Skyrim",
            "Fallout3",
            "FalloutNv",
        ],
        "BethkitPluginKind": ["Full", "Light", "Overlay"],
        "BethkitStringFileKind": ["Strings", "DlStrings", "IlStrings"],
        "BethkitBsaVersion": ["Tes3", "Tes4", "Fo3", "Sse"],
        "BethkitBa2Version": ["V1", "V7", "V8"],
        "BethkitFieldValueKind": [
            "Int",
            "Float",
            "Str",
            "FormId",
            "FormIdTyped",
            "Bytes",
            "Enum",
            "Flags",
            "Struct",
            "Array",
            "LocalizedId",
            "Missing",
        ],
    }
    for variant in _ENUM_VARIANTS.get(c_enum_name, []):
        doc: str = docs.get(variant, "")
        variants.append((variant, _clean_text(doc)))
    return variants


# ---------------------------------------------------------------------------
# Stub emitter
# ---------------------------------------------------------------------------

_STUB_HEADER = (
    "# generated by scripts/gen_stubs.py - do not edit by hand\n"
    "# source: crates/bethkit-ffi/bethkit.h\n"
)


def _indent(text: str, spaces: int) -> str:
    """
    Indent every non-empty line of *text* by *spaces* spaces.

    Args:
        text (str): Multi-line text to indent.
        spaces (int): Number of spaces.

    Returns:
        str: Indented text.
    """

    pad: str = " " * spaces
    return "\n".join(
        pad + line if line.strip() else line for line in text.split("\n")
    )


def _format_docstring(body: str, indent_spaces: int) -> str:
    """
    Wrap *body* in triple-quotes and indent for *indent_spaces* nesting.

    Args:
        body (str): Docstring content without surrounding quotes.
        indent_spaces (int): Indentation level of the surrounding code.

    Returns:
        str: Complete ``\"\"\"…\"\"\"`` block.
    """

    if not body:
        return ""
    pad: str = " " * indent_spaces
    if "\n" in body:
        indented = _indent(body, indent_spaces)
        return f'{pad}"""\n{indented}\n{pad}"""\n'
    return f'{pad}"""{body}"""\n'


def emit_module(
    mod: ModuleDef,
    docs: dict[str, str],
    out_dir: Path,
) -> None:
    """
    Write a single ``.pyi`` stub file for *mod*.

    Args:
        mod (ModuleDef): Module definition from :mod:`stub_map`.
        docs (dict[str, str]): Parsed C header docs.
        out_dir (Path): Directory to write the ``.pyi`` file into.
    """

    lines: list[str] = [_STUB_HEADER]

    # Imports
    lines.extend(f"{imp}\n" for imp in mod.imports)
    lines.append("\n")

    # Extra type alias needed in schema.pyi
    if mod.file == "schema.pyi":
        lines.append(
            "# Union of all possible decoded field value types.\n"
        )
        lines.append(
            "FieldValue = Union[\n"
            "    int,\n"
            "    float,\n"
            "    str,\n"
            "    bytes,\n"
            "    TypedFormId,\n"
            "    EnumVal,\n"
            "    FlagsVal,\n"
            "    list[NamedField],\n"
            "    list[Any],\n"
            "    None,\n"
            "]\n\n"
        )

    # GlobalFormId is a dataclass, emit it as such in load_order.pyi
    if mod.file == "load_order.pyi":
        lines.append(
            "@dataclass(frozen=True)\n"
            "class GlobalFormId:\n"
        )
        gfid_doc = _clean_text(docs.get("BethkitGlobalFormId", ""))
        if gfid_doc:
            lines.append(_format_docstring(gfid_doc, 4))
        else:
            lines.append(
                '    """A globally unique FormID (plugin name + object ID)."""\n'
            )
        lines.append("\n")
        lines.append("    plugin_name: str\n")
        lines.append('    """The source plugin file name."""\n\n')
        lines.append("    object_id: int\n")
        lines.append('    """The 24-bit object ID component."""\n\n\n')

    for cls in mod.classes:
        # Skip GlobalFormId here — handled above.
        if mod.file == "load_order.pyi" and cls.name == "GlobalFormId":
            continue
        # Enums get special treatment.
        if mod.file == "enums.pyi":
            _emit_enum(lines, cls, docs)
            continue
        # Dataclasses in schema (TypedFormId, EnumVal, FlagsVal, NamedField)
        if mod.file == "schema.pyi" and cls.name in (
            "TypedFormId",
            "EnumVal",
            "FlagsVal",
            "NamedField",
        ):
            _emit_dataclass(lines, cls, docs)
            continue
        _emit_class(lines, cls, docs)

    out_path = out_dir / mod.file
    out_path.write_text("".join(lines), encoding="utf-8")
    print(f"  wrote {out_path.relative_to(out_dir.parent.parent)}")


def _emit_enum(
    lines: list[str],
    cls: ClassDef,
    docs: dict[str, str],
) -> None:
    """
    Emit an ``IntEnum`` stub class for *cls*.

    Args:
        lines (list[str]): Output buffer to append to.
        cls (ClassDef): Enum class definition.
        docs (dict[str, str]): Parsed C header docs.
    """

    lines.append(f"class {cls.name}(IntEnum):\n")
    # Class-level docstring from C typedef.
    raw_class_doc: str = docs.get(cls.c_typedef or "", "")
    class_doc: str = _clean_text(raw_class_doc)
    if class_doc:
        lines.append(_format_docstring(class_doc, 4))
    lines.append("\n")

    variants = extract_enum_values(docs, cls.c_typedef or "")
    if variants:
        for i, (vname, vdoc) in enumerate(variants):
            lines.append(f"    {vname}: int\n")
            if vdoc:
                lines.append(_format_docstring(vdoc, 4))
    else:
        lines.append("    ...\n")

    lines.append("\n\n")


def _emit_dataclass(
    lines: list[str],
    cls: ClassDef,
    docs: dict[str, str],
) -> None:
    """
    Emit a frozen ``@dataclass`` stub class for simple value types.

    Args:
        lines (list[str]): Output buffer to append to.
        cls (ClassDef): Class definition from stub_map.
        docs (dict[str, str]): Parsed C header docs.
    """

    # Derive fields from method defs with kind == "property"
    fields: list[tuple[str, str, str]] = []
    for m in cls.methods:
        if m.kind == "property":
            fdoc = m.manual_doc or _clean_text(
                docs.get(m.c_func or "", "")
            )
            fields.append((m.name, m.ret, fdoc))

    lines.append("@dataclass(frozen=True)\n")
    lines.append(f"class {cls.name}:\n")
    raw_class_doc = docs.get(cls.c_typedef or cls.name, "")
    class_doc = _clean_text(raw_class_doc) or f"A {cls.name} value."
    lines.append(_format_docstring(class_doc, 4))
    lines.append("\n")

    for fname, ftype, fdoc in fields:
        lines.append(f"    {fname}: {ftype}\n")
        if fdoc:
            lines.append(_format_docstring(fdoc, 4))
    if not fields:
        lines.append("    ...\n")

    lines.append("\n\n")


def _emit_class(
    lines: list[str],
    cls: ClassDef,
    docs: dict[str, str],
) -> None:
    """
    Emit a regular class stub for *cls*.

    Args:
        lines (list[str]): Output buffer to append to.
        cls (ClassDef): Class definition from stub_map.
        docs (dict[str, str]): Parsed C header docs.
    """

    lines.append(f"class {cls.name}:\n")

    # Class-level docstring.
    raw_class_doc: str = ""
    if cls.c_typedef:
        raw_class_doc = docs.get(cls.c_typedef, "")
    class_doc: str = _clean_text(raw_class_doc)
    if class_doc:
        lines.append(_format_docstring(class_doc, 4))
    lines.append("\n")

    # Context-manager methods first.
    if cls.context_manager:
        lines.append("    def __enter__(self) -> Self: ...\n")
        lines.append(
            "    def __exit__(self, *args: object) -> None: ...\n"
        )
        lines.append("\n")

    # Methods.
    for method in cls.methods:
        _emit_method(lines, method, docs)

    lines.append("\n")


def _emit_method(
    lines: list[str],
    method: MethodDef,
    docs: dict[str, str],
) -> None:
    """
    Emit a single method stub.

    Args:
        lines (list[str]): Output buffer to append to.
        method (MethodDef): Method definition from stub_map.
        docs (dict[str, str]): Parsed C header docs.
    """

    # Resolve docstring: manual_doc takes priority over C header.
    if method.manual_doc:
        doc_body: str = method.manual_doc
    elif method.c_func and method.c_func in docs:
        doc_body = adapt_docstring(docs[method.c_func], method)
    else:
        doc_body = ""

    # Decorator(s)
    if method.kind == "classmethod":
        lines.append("    @classmethod\n")
    elif method.kind == "property":
        lines.append("    @property\n")
    elif method.kind == "staticmethod":
        lines.append("    @staticmethod\n")

    # Signature
    if method.kind == "classmethod":
        first_arg = "cls"
    elif method.kind == "staticmethod":
        first_arg = ""
    else:
        first_arg = "self"

    if first_arg and method.params:
        params_str = f"{first_arg}, {method.params}"
    elif first_arg:
        params_str = first_arg
    else:
        params_str = method.params

    # Special dunder methods without explicit return annotation
    # (e.g. __iter__ already has a return type in the MethodDef)
    sig_line = (
        f"    def {method.name}({params_str}) -> {method.ret}:\n"
    )
    lines.append(sig_line)

    if doc_body:
        lines.append(_format_docstring(doc_body, 8))
        lines.append("        ...\n")
    else:
        lines.append("        ...\n")

    lines.append("\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """
    Parse arguments and generate all ``.pyi`` stub files.
    """

    parser = argparse.ArgumentParser(
        description="Generate bethkit .pyi stubs from bethkit.h."
    )
    parser.add_argument(
        "--header",
        type=Path,
        default=_DEFAULT_HEADER,
        help=(
            "Path to bethkit.h "
            f"(default: {_DEFAULT_HEADER})"
        ),
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=_DEFAULT_OUT,
        help=(
            "Output directory for .pyi files "
            f"(default: {_DEFAULT_OUT})"
        ),
    )
    args = parser.parse_args()

    header: Path = args.header.resolve()
    out_dir: Path = args.out_dir.resolve()

    if not header.exists():
        print(
            f"error: header not found: {header}",
            file=sys.stderr,
        )
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Parsing {header} …")
    docs: dict[str, str] = parse_header(header)
    print(f"  found {len(docs)} documented identifiers")

    print(f"Emitting stubs to {out_dir} …")
    for _mod_name, mod in MODULES.items():
        emit_module(mod, docs, out_dir)

    print("Done.")


if __name__ == "__main__":
    main()
