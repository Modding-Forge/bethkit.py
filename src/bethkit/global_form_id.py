"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field


class GlobalFormId(BaseModel, frozen=True):
    """Globally unique plugin name and 24-bit object identifier."""

    plugin_name: str
    """Name of the owning plugin (e.g. ``"Skyrim.esm"``)."""

    object_id: Annotated[int, Field(strict=True, ge=0, le=0xFFFFFF)]
    """24-bit object identifier within *plugin_name*."""

    def __str__(self) -> str:
        """
        Returns a human-readable representation of this FormID.

        Returns:
            str: Human-readable ``"PluginName:0xOBJECTID"`` representation.
        """

        return f"{self.plugin_name}:0x{self.object_id:06X}"
