"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from ..load_order import GlobalFormId
from .record import Record


class CacheHit(BaseModel, frozen=True):
    """Result of a successful :meth:`PluginCache.find_by_editor_id` lookup."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    record: Record
    """The matched record (borrowed, valid while the cache is open)."""

    global_form_id: GlobalFormId
    """The resolved global FormID of the matched record."""
