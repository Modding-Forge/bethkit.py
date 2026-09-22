"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Optional

import pydantic

from . import _wire


class FieldReference(pydantic.BaseModel, frozen=True):
    """Address-bearing base for dynamically selected fields."""

    address: Optional[_wire.FieldAddress] = None
    """Native edit address, absent for multi-subrecord grammar groups."""
    _wire_value: Optional[_wire.WireValue] = pydantic.PrivateAttr(default=None)
    _annotation: object = pydantic.PrivateAttr(default=object)
