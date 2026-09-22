"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import enum
import math
from typing import Optional, TypeVar, cast

import pydantic

from .._error import UnsupportedEditError
from . import _values, _wire
from ._field_ref import FieldRef
from ._struct_model import StructModel

_T = TypeVar("_T")


def encode_replacement(
    reference: FieldRef[_T], value: _T
) -> dict[str, pydantic.JsonValue]:
    """Validates a replacement against its exact generated field type.

    Args:
        reference: Typed snapshot reference to an existing native field.
        value: Replacement value matching the generated field type.

    Returns:
        A tagged JSON value suitable for the authoritative native editor.

    Raises:
        UnsupportedEditError: This is a multi-subrecord grammar group.
        pydantic.ValidationError: The value violates the generated type.
    """

    if reference.address is None or reference._wire_value is None:
        raise UnsupportedEditError(
            "Edit individual fields within a grammar group."
        )
    checked = pydantic.TypeAdapter[object](
        reference._annotation
    ).validate_python(value)
    return _encode(checked, reference._wire_value)


def _encode(
    value: object,
    template: Optional[_wire.WireValue] = None,
) -> dict[str, pydantic.JsonValue]:
    """Converts validated values while retaining native signedness and paths."""

    if isinstance(value, StructModel):
        existing = (
            {field.path: field.value for field in template.fields}
            if isinstance(template, _wire.WireStruct)
            else {}
        )
        fields: list[pydantic.JsonValue] = []
        for name, binding in type(value)._bindings.items():
            member: object = getattr(value, name)
            fields.append(
                {
                    "name": binding.name,
                    "path": binding.path,
                    "value": _encode(member, existing.get(binding.path)),
                }
            )
        return {"kind": "struct", "fields": fields}
    if isinstance(value, tuple):
        items = cast(tuple[object, ...], value)
        templates = (
            template.items if isinstance(template, _wire.WireArray) else ()
        )
        return {
            "kind": "array",
            "items": [
                _encode(
                    item, templates[index] if index < len(templates) else None
                )
                for index, item in enumerate(items)
            ],
        }
    if isinstance(value, _values.FormId):
        return {"kind": "form_id", "value": value.raw}
    if isinstance(value, bytes):
        return {"kind": "bytes", "value": list(value)}
    if value is None:
        return {"kind": "absent", "value": None}
    if isinstance(value, bool):
        raise TypeError("Booleans are not native integer fields.")
    if isinstance(value, enum.IntFlag):
        return {"kind": "flags", "value": int(value)}
    if isinstance(value, enum.IntEnum):
        return {"kind": "enum", "value": int(value)}
    if isinstance(value, float) and not math.isfinite(value):
        special = (
            "NaN"
            if math.isnan(value)
            else "Infinity"
            if value > 0
            else "-Infinity"
        )
        return {"kind": "float", "value": special}
    if isinstance(value, (int, float, str)):
        kind = (
            template.kind
            if isinstance(template, _wire.WireScalar)
            else "string"
            if isinstance(value, str)
            else "float"
            if isinstance(value, float)
            else "int"
            if value < 0
            else "uint"
        )
        return {"kind": kind, "value": value}
    raise TypeError(
        f"Unsupported semantic replacement type: {type(value).__name__}"
    )
