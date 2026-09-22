"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel


class DecoderRequirement(BaseModel, frozen=True):
    """One custom decoder required by a schema package."""

    id: str
    """Stable decoder identifier."""

    minimum_version: int
    """Minimum compatible decoder implementation version."""
