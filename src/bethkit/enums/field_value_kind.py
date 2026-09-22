"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from enum import IntEnum


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
