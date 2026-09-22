"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Any

from .enum_val import EnumVal
from .flags_val import FlagsVal
from .typed_form_id import TypedFormId

FieldValue = (
    int
    | float
    | str
    | bytes
    | TypedFormId
    | EnumVal
    | FlagsVal
    | list[Any]
    | None
)
"""Legacy decoded values; nested lists remain mutable for compatibility."""
