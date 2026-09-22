"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from enum import IntEnum


class StringFileKind(IntEnum):
    """
    The three localisation string-file types used by Bethesda games.
    """

    STRINGS = 0
    """Plain null-terminated strings (.STRINGS)."""

    DL_STRINGS = 1
    """Length-prefixed strings (.DLSTRINGS)."""

    IL_STRINGS = 2
    """Length-prefixed localised strings (.ILSTRINGS)."""
