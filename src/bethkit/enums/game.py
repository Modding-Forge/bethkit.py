"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from enum import IntEnum


class Game(IntEnum):
    """
    Supported Bethesda game titles.

    These values are passed to the native library to select the correct
    plugin and archive format for a given game.
    """

    SKYRIM_LE = 0
    """The Elder Scrolls V: Skyrim Legendary Edition."""

    SKYRIM_SE = 1
    """Skyrim Special Edition (64-bit, AE/SE)."""

    SKYRIM_VR = 2
    """The Elder Scrolls V: Skyrim VR."""

    FALLOUT3 = 3
    """Fallout 3."""

    FALLOUT_NV = 4
    """Fallout: New Vegas."""

    FALLOUT4 = 5
    """Fallout 4."""

    FALLOUT4_VR = 6
    """Fallout 4 VR."""

    FALLOUT76 = 7
    """Fallout 76."""

    OBLIVION = 8
    """The Elder Scrolls IV: Oblivion."""

    MORROWIND = 9
    """The Elder Scrolls III: Morrowind."""

    STARFIELD = 10
    """Starfield."""

    SKYRIM = SKYRIM_LE
    """Deprecated compatibility alias for Skyrim Legendary Edition."""
