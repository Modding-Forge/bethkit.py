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
from .string_scan_diagnostic import StringScanDiagnostic

__all__ = [
    "LocalizationSet",
    "LocalizationEditor",
    "StringIdentity",
    "StringReference",
    "StringScanDiagnostic",
    "StringTable",
    "iter_strings",
]
