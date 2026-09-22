"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel


class ReferenceEdge(BaseModel, frozen=True):
    """Immutable directed reference edge."""

    source_plugin: str
    """Plugin containing the reference."""
    source_object_id: int
    """Resolved identity of the referring record."""
    target_plugin: str
    """Plugin defining the reference target."""
    target_object_id: int
    """Resolved identity of the referenced record."""
    schema_path: str
    """Structural location of the reference."""
