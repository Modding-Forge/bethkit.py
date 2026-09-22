"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class Conflict(BaseModel, frozen=True):
    """Immutable semantic conflict result."""

    object_id: int
    """Resolved identity shared by the compared records."""
    signature: bytes
    """Four-byte record type."""
    plugins: tuple[str, ...]
    """Participating source plugins in load order."""
    winner: str
    """Plugin supplying the winning override."""
    classification: Literal["identical", "override", "conflict"]
    """Semantic relationship between the compared records."""
    paths: tuple[str, ...]
    """Schema paths involved in this result."""
