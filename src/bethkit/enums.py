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


class FieldValueKind(IntEnum):
    """
    Discriminant tag for the ``BethkitFieldValue`` tagged union.

    Each variant corresponds to a concrete Python type returned by the
    schema decoding layer.
    """

    INT = 0
    """Signed or unsigned integer field, decoded as ``int``."""

    FLOAT = 1
    """Floating-point field, decoded as ``float``."""

    STR = 2
    """Zero-terminated string field, decoded as ``str``."""

    FORM_ID = 3
    """Raw 32-bit FormID, decoded as ``int``."""

    FORM_ID_TYPED = 4
    """FormID with type constraints, decoded as :class:`TypedFormId`."""

    BYTES = 5
    """Raw byte slice, decoded as ``bytes``."""

    ENUM = 6
    """Enumeration field, decoded as :class:`EnumVal`."""

    FLAGS = 7
    """Bit-flags field, decoded as :class:`FlagsVal`."""

    STRUCT = 8
    """Inline struct, decoded as ``list[NamedField]``."""

    ARRAY = 9
    """Repeated field, decoded as ``list[FieldValue]``."""

    MISSING = 10
    """Field absent or unknown; value is ``None``."""

    UINT = 11
    """Unsigned 64-bit integer field, decoded as ``int``."""
