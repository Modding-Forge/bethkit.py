"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel


class TypedFormId(BaseModel, frozen=True):
    """A FormID and the record signatures it may reference."""

    raw: int
    """File-local unsigned record identifier."""
    allowed_sigs: tuple[bytes, ...]
    """Schema-declared target record signatures."""
