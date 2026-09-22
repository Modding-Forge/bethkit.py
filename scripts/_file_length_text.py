"""
Copyright (c) Modding Forge
"""

# Distinguishes encoded text from binaries without bypassing source checks.

from __future__ import annotations

import pathlib
from typing import Optional

_TEXT_SUFFIXES: frozenset[str] = frozenset(
    {
        ".py",
        ".pyi",
        ".pyw",
        ".json",
        ".jsonl",
        ".toml",
        ".md",
        ".txt",
        ".yml",
        ".yaml",
        ".sh",
        ".bash",
        ".ps1",
        ".ini",
        ".cfg",
        ".conf",
        ".bat",
        ".cmd",
        ".rst",
        ".adoc",
        ".xml",
        ".svg",
        ".html",
        ".css",
        ".js",
        ".ts",
        ".tsx",
        ".jsx",
        ".rs",
        ".c",
        ".h",
        ".cpp",
        ".hpp",
        ".sql",
        ".csv",
        ".tsv",
    }
)
_TEXT_NAMES: frozenset[str] = frozenset(
    {
        "license",
        "manifest.in",
        ".gitignore",
        ".gitattributes",
        "pre-commit",
        "pre-push",
        "dockerfile",
        "makefile",
    }
)
_BOM_ENCODINGS: tuple[tuple[bytes, str], ...] = (
    (b"\xff\xfe\x00\x00", "utf-32"),
    (b"\x00\x00\xfe\xff", "utf-32"),
    (b"\xff\xfe", "utf-16"),
    (b"\xfe\xff", "utf-16"),
    (b"\xef\xbb\xbf", "utf-8-sig"),
)


def count_text_lines(path: str, data: bytes) -> Optional[int]:
    """Counts physical text lines without treating encoded source as binary.

    UTF-16 and UTF-32 require a byte-order mark. Other NUL-free text, including
    legacy single-byte encodings, uses its physical CR/LF byte boundaries.
    File extensions never exempt text. Unknown formats need actual NUL or
    non-whitespace ASCII control bytes to be classified as opaque binary data.

    Args:
        path: Source path used for classification and error diagnostics.
        data: Exact bytes from the selected snapshot.

    Returns:
        The physical line count, or None for an opaque binary artifact.

    Raises:
        ValueError: BOM-marked text is malformed or known source contains NUL.
    """

    source = pathlib.PurePosixPath(path)
    suffix = source.suffix.lower()
    for marker, encoding in _BOM_ENCODINGS:
        if data.startswith(marker):
            try:
                data = data.decode(encoding).encode("utf-8")
            except UnicodeError as exc:
                raise ValueError(f"Invalid {encoding} text: {path}") from exc
            break
    known_source = (
        suffix in _TEXT_SUFFIXES or source.name.lower() in _TEXT_NAMES
    )
    if b"\0" in data:
        if known_source:
            raise ValueError(
                f"NUL-containing source text is not allowed: {path}"
            )
        return None
    if not known_source and any(
        byte < 32 and byte not in (9, 10, 12, 13) for byte in data
    ):
        return None
    return len(data.splitlines())
