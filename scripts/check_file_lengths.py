"""
Copyright (c) Modding Forge
"""

# Checks Git snapshots and unpacked source distributions without dependencies.

from __future__ import annotations

import argparse
import json
import subprocess
from collections.abc import Callable
from pathlib import Path, PurePosixPath
from typing import Optional, cast

if __package__:
    from . import _file_length_archive, _file_length_text
else:
    import _file_length_archive
    import _file_length_text

POLICY_FILENAME: str = "file-length-policy.json"
_GENERATED_PARENT: PurePosixPath = PurePosixPath(
    "src/bethkit/records/skyrim_se"
)


def _git(root: Path, *arguments: str) -> bytes:
    """Runs one bounded, read-only Git command in the project.

    Args:
        root: Project directory.
        arguments: Individual Git command arguments.

    Returns:
        Raw command output, preserving arbitrary file contents.

    Raises:
        OSError: Git could not be started.
        ValueError: Git rejected the snapshot or exceeded its time limit.
    """

    try:
        result = subprocess.run(
            [
                "git",
                "-c",
                f"safe.directory={root.as_posix()}",
                "-C",
                str(root),
                *arguments,
            ],
            capture_output=True,
            check=False,
            timeout=30,
        )
    except subprocess.TimeoutExpired as exc:
        raise ValueError("Git snapshot inspection timed out.") from exc
    if result.returncode:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(f"Git snapshot inspection failed: {message}")
    return result.stdout


def _snapshot(
    root: Path, staged: bool, revision: Optional[str]
) -> tuple[list[str], Callable[[str], bytes]]:
    """Selects file paths and a reader from exactly one source snapshot.

    Args:
        root: Project directory.
        staged: Whether to inspect the staged Git index.
        revision: Optional commit or tree to inspect instead.

    Returns:
        Relative paths and a reader using the same snapshot for every file.

    Raises:
        OSError: A selected file cannot be read.
        ValueError: The selected snapshot is unavailable or contradictory.
    """

    if staged and revision is not None:
        raise ValueError("Choose either staged files or a revision.")
    try:
        top = _git(root, "rev-parse", "--show-toplevel").decode().strip()
        repository = Path(top).resolve() == root
    except (OSError, ValueError):
        if (root / ".git").exists() or staged or revision is not None:
            raise ValueError("The selected Git snapshot is unavailable.")
        repository = False
    if not repository and (staged or revision is not None):
        raise ValueError("The project root is not the selected Git repository.")
    tree: Optional[str] = None
    if revision is not None:
        tree = (
            _git(
                root,
                "rev-parse",
                "--verify",
                "--end-of-options",
                f"{revision}^{{tree}}",
            )
            .decode()
            .strip()
        )
        output = _git(root, "ls-tree", "-r", "-z", tree)
    elif staged:
        output = _git(root, "ls-files", "--stage", "-z")
    elif repository:
        output = _git(
            root, "ls-files", "--cached", "--others", "--exclude-standard", "-z"
        )
    else:
        output = b""
    if repository:
        entries = [entry for entry in output.split(b"\0") if entry]
        if staged or tree is not None:
            for index, entry in enumerate(entries):
                metadata, filename = entry.split(b"\t", 1)
                if metadata.split()[0] == b"120000":
                    raise ValueError(
                        "Symbolic source files are unsupported: "
                        + filename.decode("utf-8")
                    )
                entries[index] = filename
        paths = sorted({entry.decode("utf-8") for entry in entries})
        if not staged and tree is None:
            paths = [
                name
                for name in paths
                if (root / name).exists() or (root / name).is_symlink()
            ]
    else:
        paths = _file_length_archive.source_paths(root)

    def read(path: str) -> bytes:
        """Reads one file from the selected snapshot without following links.

        Args:
            path: Exact source path relative to the project.

        Returns:
            The selected file contents.

        Raises:
            OSError: The working source file cannot be read.
            ValueError: Git cannot read the file or it is a symbolic link.
        """

        if staged:
            return _git(root, "show", f":{path}")
        if tree is not None:
            return _git(root, "show", f"{tree}:{path}")
        source = root / path
        if source.is_symlink():
            raise ValueError(f"Symbolic source files are unsupported: {path}")
        return source.read_bytes()

    return paths, read


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """Rejects repeated JSON keys instead of silently replacing policy values.

    Args:
        pairs: Ordered JSON object entries supplied by the decoder.

    Returns:
        The object with each key represented exactly once.

    Raises:
        ValueError: A key occurs more than once in the same object.
    """

    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate policy key: {key}")
        result[key] = value
    return result


def _policy(data: bytes) -> tuple[int, dict[str, tuple[int, str]]]:
    """Validates the policy and its exact, individually justified exceptions.

    Args:
        data: Policy bytes from the same snapshot as the checked files.

    Returns:
        Default line limit and path-specific limits with their explanations.

    Raises:
        ValueError: Policy JSON or any exception is malformed.
    """

    policy: object = json.loads(data, object_pairs_hook=_unique_object)
    if not isinstance(policy, dict):
        raise ValueError("Policy must be a JSON object.")
    settings = cast(dict[str, object], policy)
    if set(settings) != {"format_version", "max_lines", "exceptions"}:
        raise ValueError("Policy must declare version, max_lines, exceptions.")
    if (
        type(settings["format_version"]) is not int
        or settings["format_version"] != 1
    ):
        raise ValueError("Unsupported policy format_version.")
    limit = settings["max_lines"]
    if type(limit) is not int or not 1 <= limit <= 400:
        raise ValueError("Policy max_lines must be an integer from 1 to 400.")
    raw_exceptions = settings["exceptions"]
    if not isinstance(raw_exceptions, dict):
        raise ValueError("Policy exceptions must be an exact-path object.")
    exceptions: dict[str, tuple[int, str]] = {}
    for path, entry in cast(dict[str, object], raw_exceptions).items():
        relative = PurePosixPath(path)
        if (
            not path
            or relative.is_absolute()
            or ".." in relative.parts
            or any(char in path for char in "*?[]\\:")
            or relative.as_posix() != path
        ):
            raise ValueError(
                f"Exception must use a canonical exact path: {path}"
            )
        if relative.parent != _GENERATED_PARENT or relative.suffix != ".py":
            raise ValueError(
                f"Only generated record files may be excepted: {path}"
            )
        if not isinstance(entry, dict):
            raise ValueError(f"Exception needs a limit and reason: {path}")
        options = cast(dict[str, object], entry)
        if set(options) != {"max_lines", "reason"}:
            raise ValueError(f"Exception needs max_lines and reason: {path}")
        maximum = options["max_lines"]
        reason = options["reason"]
        if type(maximum) is not int or maximum <= limit:
            raise ValueError(
                f"Exception needs a larger finite line limit: {path}"
            )
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"Exception needs a nonempty reason: {path}")
        exceptions[path] = (maximum, reason)
    return limit, exceptions


def check_file_lengths(
    root: Path, *, staged: bool = False, revision: Optional[str] = None
) -> list[str]:
    """Checks source files against the selected snapshot's explicit policy.

    Git working trees include tracked and nonignored new files. Source archives
    exclude only VCS, cache and build metadata. Encoded text is counted while
    opaque binary files are skipped; malformed known source fails closed.

    Args:
        root: Project root containing file-length-policy.json.
        staged: Whether to inspect staged contents instead of working files.
        revision: Optional Git commit or tree whose files should be inspected.

    Returns:
        Deterministic diagnostics; an empty list indicates success. Invalid or
        missing policies, unavailable files, and unused exceptions fail closed.
    """

    try:
        paths, read = _snapshot(root.resolve(), staged, revision)
        if POLICY_FILENAME not in paths:
            return [f"Missing policy in selected snapshot: {POLICY_FILENAME}"]
        limit, exceptions = _policy(read(POLICY_FILENAME))
        problems: list[str] = []
        for path in sorted(set(exceptions) - set(paths)):
            problems.append(f"Exception references a missing file: {path}")
        for path in paths:
            data = read(path)
            exception = exceptions.get(path)
            lines = _file_length_text.count_text_lines(path, data)
            if lines is None:
                if exception is not None:
                    problems.append(f"Unused exception for binary file: {path}")
                continue
            maximum = limit
            if exception is not None:
                maximum = exception[0]
                header = data.splitlines()[:12]
                generated = any(
                    line.startswith(b"# ") and b"generated" in line.lower()
                    for line in header
                )
                if not generated:
                    problems.append(
                        f"Exception lacks a generated marker: {path}"
                    )
                if lines <= limit:
                    problems.append(
                        f"Unused exception below {limit} lines: {path}"
                    )
            if lines > maximum:
                problems.append(
                    f"{path}: {lines} lines exceeds limit {maximum}."
                )
        return problems
    except (OSError, ValueError) as exc:
        return [f"File-length check failed: {exc}"]


def main() -> int:
    """Runs the shared gate for local hooks, builds, and continuous integration.

    Returns:
        Zero for a compliant snapshot, otherwise one.
    """

    parser = argparse.ArgumentParser(
        description="Enforce source-file line limits."
    )
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--staged", action="store_true")
    selection.add_argument("--revision", "--git-ref", dest="revision")
    arguments = parser.parse_args()
    problems = check_file_lengths(
        arguments.root, staged=arguments.staged, revision=arguments.revision
    )
    for problem in problems:
        print(problem)
    if problems:
        print(
            "Split oversized files; generated exceptions need policy entries."
        )
    else:
        print("File-length policy passed.")
    return int(bool(problems))


if __name__ == "__main__":
    raise SystemExit(main())
