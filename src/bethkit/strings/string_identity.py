"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Optional

import pydantic

from ..records import _wire


class StringIdentity(pydantic.BaseModel, frozen=True):
    """Persistent string position independent of text, IDs, and edit guards.

    A filename is available for disk plugins and named in-memory plugins.
    Callers persisting references for multiple in-memory plugins must supply
    a unique filename to ``Plugin.from_bytes(name=...)``.
    """

    plugin_name: Optional[str]
    """Source filename, or None for an unnamed in-memory plugin."""
    record_signature: tuple[int, int, int, int]
    """Containing record signature."""
    form_id: int
    """File-local record identifier."""
    subrecord_index: int
    """Position of the containing subrecord."""
    subrecord_path: str
    """Matched subrecord schema path."""
    repeat_scopes: tuple[_wire.RepeatScope, ...]
    """Native grammar repetition occurrences."""
    value_steps: tuple[_wire.ValueStep, ...]
    """Exact nested payload position."""
