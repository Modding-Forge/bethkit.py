"""
Copyright (c) Modding Forge
"""

# Typed scalar values shared by generated game models.

from __future__ import annotations

import enum
from typing import Annotated, Optional, TypeAlias

import pydantic

UInt32: TypeAlias = Annotated[
    int, pydantic.Field(strict=True, ge=0, le=0xFFFFFFFF)
]


class FormId(pydantic.BaseModel, frozen=True):
    """An unresolved, file-local FormID and its permitted target signatures."""

    raw: UInt32
    """Raw file-local identifier; zero is a null reference."""

    allowed_signatures: tuple[str, ...] = ()
    """Schema-declared target record signatures, empty when unrestricted."""


class OpenIntEnum(enum.IntEnum):
    """A named integer enumeration that preserves unknown on-disk values."""

    @classmethod
    def _missing_(cls, value: object) -> Optional[OpenIntEnum]:
        """Preserves numeric values not present in this schema revision.

        Args:
            value: Raw integer encountered in a plugin.

        Returns:
            An unnamed member, or None for a non-integer input.
        """

        if not isinstance(value, int) or isinstance(value, bool):
            return None
        member = int.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member
