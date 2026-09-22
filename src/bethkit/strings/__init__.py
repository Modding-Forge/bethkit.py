"""
Copyright (c) Modding Forge
"""

# Strings subpackage — reading and writing Bethesda localisation string tables.

from __future__ import annotations

from ..strings.editor import LocalizationEditor
from ..strings.references import (
    StringIdentity,
    StringReference,
    iter_strings,
)
from ..strings.strings import LocalizationSet, StringTable

__all__ = [
    "LocalizationSet",
    "LocalizationEditor",
    "StringIdentity",
    "StringReference",
    "StringTable",
    "iter_strings",
]
