"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import hashlib
import keyword
import re

HEADER: str = '''"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values

'''
NAMES: dict[str, str] = {
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
