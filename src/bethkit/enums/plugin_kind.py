"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from enum import IntEnum


class PluginKind(IntEnum):
    """
    Plugin type as declared in the file header.
    """

    FULL = 0
    """Standard full plugin (ESP/ESM with a complete load-order slot)."""

    LIGHT = 1
    """Light plugin (ESL) with a 12-bit FormID range."""

    OVERLAY = 2
    """Overlay plugin (ESM override) introduced in Starfield."""
