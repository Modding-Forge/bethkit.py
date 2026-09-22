"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel


class HandlerRequirement(BaseModel, frozen=True):
    """One semantic callback handler required by a schema package."""

    id: str
    """Stable semantic handler identifier."""

    minimum_version: int
    """Minimum compatible handler implementation version."""
