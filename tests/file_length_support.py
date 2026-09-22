"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Optional

POLICY_NAME: str = "file-length-policy.json"
GENERATED_PATH: str = "src/bethkit/records/skyrim_se/fixture.py"
GENERATED_MARKER: str = (
    "# Generated from the pinned xEdit/Bethkit schema. Do not edit."
)


def run_git(root: Path, *arguments: str) -> str:
    """Runs Git against an isolated fixture without user hooks or signing.

    Args:
        root: Repository used by this test only.
        *arguments: Git arguments without shell interpolation.

    Returns:
        Captured standard output after successful execution.

    Raises:
        subprocess.CalledProcessError: The fixture command fails.
    """

    result = subprocess.run(
        [
            "git",
            "-c",
            f"safe.directory={root.as_posix()}",
            "-c",
            f"core.hooksPath={(root / '.git' / 'no-hooks').as_posix()}",
            "-c",
            "user.name=Bethkit Test",
            "-c",
            "user.email=test@example.invalid",
            "-c",
            "commit.gpgsign=false",
            "-c",
            "core.autocrlf=false",
            "-c",
            "core.safecrlf=false",
            *arguments,
        ],
        cwd=root,
        capture_output=True,
        check=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout


def write_policy(
    root: Path,
    *,
    exceptions: Optional[dict[str, dict[str, object]]] = None,
) -> Path:
    """Writes the minimal explicit policy for a fixture.

    Args:
        root: Existing repository or extracted-source directory.
        exceptions: Exact generated-file exceptions, if any.

    Returns:
        The written policy path.

    Raises:
        OSError: The temporary fixture cannot be written.
    """

    path = root / POLICY_NAME
    policy: dict[str, object] = {
        "format_version": 1,
        "max_lines": 400,
        "exceptions": exceptions or {},
    }
    path.write_text(json.dumps(policy, indent=4), encoding="utf-8")
    return path


def create_repository(root: Path) -> None:
    """Creates an isolated Git repository with one committed valid policy.

    Args:
        root: Existing empty temporary directory.

    Raises:
        subprocess.CalledProcessError: Git initialization or commit fails.
        OSError: The temporary policy cannot be written.
    """

    run_git(root, "init", "--quiet")
    write_policy(root)
    run_git(root, "add", POLICY_NAME)
    run_git(root, "commit", "--quiet", "-m", "test: add file length policy")


def write_lines(root: Path, relative: str, count: int) -> Path:
    """Creates an exact number of newline-terminated fixture lines.

    Args:
        root: Repository or archive root containing the file.
        relative: Forward-slash-separated relative filename.
        count: Nonnegative number of physical lines.

    Returns:
        The written file path.

    Raises:
        OSError: The temporary directory or file cannot be created.
    """

    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"fixture\n" * count)
    return path
