"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class EnumVal(BaseModel, frozen=True):
    """A decoded enumeration value."""

    value: int
    """Encoded enumeration value, including unknown values."""
    name: Optional[str]
    """Declared value label, when known."""
