"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import os
from pathlib import Path

_METADATA_DIRECTORIES: frozenset[str] = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        ".pyright",
    }
)


def _is_virtual_environment(path: Path) -> bool:
    """Identifies a real environment by its configuration and runtime layout.

    Args:
        path: Directory considered for exclusion from maintained source files.

    Returns:
        Whether a configuration, interpreter, and site-packages tree coexist.
        A directory name or a configuration marker alone never exempts sources.
    """

    if not (path / "pyvenv.cfg").is_file():
        return False
    windows = (path / "Scripts" / "python.exe").is_file() and (
        path / "Lib" / "site-packages"
    ).is_dir()
    posix = (path / "bin" / "python").is_file() and any(
        candidate.is_dir()
        for candidate in (path / "lib").glob("python*/site-packages")
    )
    return windows or posix


def source_paths(root: Path) -> list[str]:
    """Lists unpacked source files without broad build-directory exemptions.

    Only VCS metadata, named tool caches, generated egg-info/PKG-INFO metadata,
    and verified Python environments are excluded. Maintained files under
    build, dist, target, or a directory merely named venv remain subject to the
    same checks as tracked Git sources. Symbolic links remain visible so the
    common reader can reject them without following their targets.

    Args:
        root: Unpacked source-distribution directory.

    Returns:
        Sorted source paths relative to the directory.

    Raises:
        OSError: A source directory cannot be inspected.
    """

    paths: list[str] = []
    for directory, directories, filenames in os.walk(
        root, onerror=_raise_walk_error, followlinks=False
    ):
        base = Path(directory)
        for name in directories.copy():
            path = base / name
            if path.is_symlink():
                paths.append(path.relative_to(root).as_posix())
                directories.remove(name)
            elif (
                name in _METADATA_DIRECTORIES
                or name.endswith(".egg-info")
                or _is_virtual_environment(path)
            ):
                directories.remove(name)
        for name in filenames:
            relative = (base / name).relative_to(root).as_posix()
            if relative != "PKG-INFO":
                paths.append(relative)
    return sorted(paths)


def _raise_walk_error(error: OSError) -> None:
    """Prevents inaccessible directories from silently escaping validation.

    Args:
        error: Filesystem failure reported by the recursive walker.

    Raises:
        OSError: Always re-raises the original directory access failure.
    """

    raise error
