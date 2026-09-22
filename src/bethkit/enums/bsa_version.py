"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from enum import IntEnum


class BsaVersion(IntEnum):
    """
    BSA (Bethesda Softworks Archive) format version selector.
    """

    TES3 = 0
    """Morrowind BSA format."""

    TES4 = 1
    """Oblivion BSA format."""

    FO3 = 2
    """Fallout 3 / New Vegas BSA format."""

    SSE = 3
    """Skyrim Special Edition BSA format."""
