"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import codecs
from typing import Optional


def resolve_encoding(language: str, encoding: Optional[str] = None) -> str:
    """Resolves an explicit codec or the Bethesda code page for a language.

    Args:
        language: Bethesda language suffix used in string-table filenames.
        encoding: Optional Python codec name overriding the language default.

    Returns:
        Canonical Python codec name.

    Raises:
        LookupError: The explicit codec name is not recognized.
    """

    if encoding is not None:
        return codecs.lookup(encoding).name

    language_key: str = language.casefold()
    return _LANGUAGE_CODE_PAGES.get(language_key, "cp1252")


def normalize_encoding(encoding: str) -> str:
    """Returns the canonical codec name after validating a user selection.

    Args:
        encoding: Python codec name.

    Returns:
        Canonical Python codec name.

    Raises:
        LookupError: The codec name is not recognized.
    """

    return codecs.lookup(encoding).name


_LANGUAGE_CODE_PAGES: dict[str, str] = {
    "russian": "cp1251",
    "polish": "cp1250",
    "czech": "cp1250",
    "hungarian": "cp1250",
    "japanese": "shift_jis",
    "chinese": "gbk",
    "traditionalchinese": "big5",
    "traditional_chinese": "big5",
}
