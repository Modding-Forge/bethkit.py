"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import hashlib
import os
import re
import tempfile
from collections.abc import Mapping
from pathlib import Path
from typing import Literal, Optional

import pydantic

from ..enums import StringFileKind

EXTENSIONS: dict[StringFileKind, str] = {
    StringFileKind.STRINGS: "STRINGS",
    StringFileKind.DL_STRINGS: "DLSTRINGS",
    StringFileKind.IL_STRINGS: "ILSTRINGS",
}


class _BundleFile(pydantic.BaseModel, frozen=True):
    """Checksum of one complete output artifact."""

    path: str
    """Bundle-relative file path."""
    size: int
    """Encoded byte length."""
    sha256: str
    """Checksum of the exact saved bytes."""


class _BundleManifest(pydantic.BaseModel, frozen=True):
    """Description of a jointly published plugin and its string tables."""

    format_version: Literal[1]
    """Version of this bundle manifest."""
    plugin: str
    """Plugin filename inside the bundle."""
    language: str
    """Language used for the external string filenames."""
    schema_payload_sha256: Optional[str]
    """Schema identity when at least one record was edited."""
    files: tuple[_BundleFile, ...]
    """Encoded output files and their integrity hashes."""


def validate_filename(name: str, language: str) -> None:
    """Rejects output names that could escape or confuse the bundle layout.

    Args:
        name: Destination plugin basename.
        language: String table language component.

    Raises:
        ValueError: Either component is not a safe filename component.
    """

    if (
        not name
        or any(character in '<>:"/\\|?*\0' for character in name)
        or name != name.strip()
        or name.endswith(".")
        or Path(name).suffix.lower() not in {".esp", ".esm", ".esl"}
    ):
        raise ValueError(
            "plugin_name must be a plain ESP, ESM, or ESL filename."
        )
    if re.fullmatch(r"[A-Za-z0-9_-]+", language) is None:
        raise ValueError("language must contain letters, digits, '_' or '-'.")


def publish(
    destination: Path,
    plugin_name: str,
    language: str,
    plugin_bytes: bytes,
    table_bytes: Mapping[StringFileKind, bytes],
    schema_hash: Optional[str],
    *,
    exist_ok: bool = False,
) -> Path:
    """Stages serialized outputs before publishing a directory or merging files.

    Args:
        destination: Absolute output directory with an existing parent.
        plugin_name: Validated plain plugin filename.
        language: Validated Bethesda string-table filename suffix.
        plugin_bytes: Complete encoded plugin.
        table_bytes: Complete encoded tables indexed by format.
        schema_hash: Schema identity used by the editor, if any record changed.
        exist_ok: Merge staged files into an existing ordinary directory.

    Returns:
        The published directory path.

    Raises:
        FileExistsError: The destination exists and exist_ok is False.
        OSError: Staging, writing, or publication failed.
    """

    if destination.exists() and not exist_ok:
        raise FileExistsError(destination)
    payloads = {plugin_name: plugin_bytes}
    stem = Path(plugin_name).stem
    for kind, data in table_bytes.items():
        payloads[f"Strings/{stem}_{language}.{EXTENSIONS[kind]}"] = data
    manifest = _BundleManifest(
        format_version=1,
        plugin=plugin_name,
        language=language,
        schema_payload_sha256=schema_hash,
        files=tuple(
            _BundleFile(
                path=name,
                size=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
            )
            for name, data in sorted(payloads.items())
        ),
    )
    payloads["manifest.json"] = manifest.model_dump_json(
        indent=4, by_alias=True, exclude_defaults=True
    ).encode("utf-8")
    with tempfile.TemporaryDirectory(
        prefix=f".{destination.name}-", dir=destination.parent
    ) as temporary:
        staging = Path(temporary)
        for name, data in payloads.items():
            file_path = staging / name
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with file_path.open("xb") as output:
                output.write(data)
                output.flush()
                os.fsync(output.fileno())
        if destination.exists() or destination.is_symlink():
            if not exist_ok:
                raise FileExistsError(destination)
            _merge(staging, destination, payloads)
        else:
            staging.rename(destination)
    return destination


def _merge(
    staging: Path, destination: Path, payloads: Mapping[str, bytes]
) -> None:
    """Publishes staged files without deleting unrelated directory contents.

    Args:
        staging: Directory containing every fully written output file.
        destination: Existing output directory, never a symbolic link.
        payloads: Validated bundle-relative output names.

    Raises:
        OSError: A path is unsafe or a file replacement fails. Earlier file
            replacements may remain; this is not a multi-file transaction.
    """

    if destination.is_symlink() or not destination.is_dir():
        raise NotADirectoryError(destination)
    for name in payloads:
        target = destination / name
        if target.parent != destination:
            if target.parent.is_symlink() or (
                target.parent.exists() and not target.parent.is_dir()
            ):
                raise NotADirectoryError(target.parent)
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise FileExistsError(target)
    for name in payloads:
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        os.replace(staging / name, target)
