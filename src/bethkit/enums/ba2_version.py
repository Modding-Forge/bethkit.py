"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from enum import IntEnum


class Ba2Version(IntEnum):
    """
    BA2 (Bethesda Archive 2) format version selector.
    """

    V1 = 0
    """Fallout 4 original BA2 version."""

    V7 = 1
    """Fallout 4 Next-Gen patch BA2 version 7."""

    V8 = 2
    """Fallout 4 Next-Gen patch BA2 version 8."""
