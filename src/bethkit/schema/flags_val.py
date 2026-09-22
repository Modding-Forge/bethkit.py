"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel


class FlagsVal(BaseModel, frozen=True):
    """A decoded bit-flags value."""

    raw_value: int
    """Complete encoded bitmask, including unknown bits."""
    active_names: tuple[str, ...]
    """Labels of active schema-declared flag bits."""
