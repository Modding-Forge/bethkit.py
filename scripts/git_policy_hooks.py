"""
Copyright (c) Modding Forge
"""

# Checks the actual Git snapshots being committed or sent to a remote.

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional


def git_output(root: Path, *arguments: str) -> str:
    """Runs a read-only Git query in the selected repository.

    Args:
        root: Absolute repository directory.
        arguments: Git command and arguments.

    Returns:
        Stripped command output.

    Raises:
        subprocess.CalledProcessError: Git cannot resolve the requested state.
        subprocess.TimeoutExpired: Git did not finish within thirty seconds.
    """

    return subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", *arguments],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    ).stdout.strip()


def _advertised_commits(root: Path, remote: str) -> tuple[str, ...]:
    """Resolves freshly advertised remote history without trusting cached refs.

    Args:
        root: Local repository containing the fetched remote commit objects.
        remote: Exact destination name or URL, never printed in diagnostics.

    Returns:
        Unique locally available commit tips advertised by remote heads/tags.

    Raises:
        ValueError: Advertisement fails, is malformed, or needs fetched objects.
    """

    try:
        advertisement = git_output(
            root, "ls-remote", "--heads", "--tags", "--", remote
        )
    except (OSError, subprocess.SubprocessError):
        # Git command/error text can contain credentials from destination URLs.
        raise ValueError(
            "Cannot read remote refs; verify access and retry."
        ) from None
    refs: dict[str, str] = {}
    for line in advertisement.splitlines():
        parts = line.split()
        if (
            len(parts) != 2
            or re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", parts[0]) is None
            or not parts[1].startswith(("refs/heads/", "refs/tags/"))
            or parts[1] in refs
        ):
            raise ValueError(
                "The remote advertised malformed or duplicate refs."
            )
        refs[parts[1]] = parts[0]
    commits: dict[str, None] = {}
    for name, oid in refs.items():
        if name.endswith("^{}"):
            continue
        peeled = refs.get(f"{name}^{{}}", oid)
        try:
            kind = git_output(root, "cat-file", "-t", peeled)
        except (OSError, subprocess.SubprocessError):
            raise ValueError(
                "Remote history is unavailable locally; fetch heads and tags "
                "from the push destination before retrying."
            ) from None
        if kind == "commit":
            commits[peeled] = None
        elif name.startswith("refs/heads/") or kind == "tag":
            raise ValueError(
                "Remote refs could not be peeled to known objects."
            )
        # Tags may name blobs/trees; they contain no commit history to exclude.
    return tuple(commits)


def outgoing_revisions(
    root: Path, remote: str, updates: str
) -> tuple[str, ...]:
    """Finds outgoing commits and destination tips from Git history.

    Args:
        root: Absolute repository directory.
        remote: Destination name or URL supplied by Git's pre-push hook.
        updates: Git's four-column ref updates received on standard input.

    Returns:
        Unique commit hashes in deterministic checking order.

    Raises:
        ValueError: Ref updates or remote history cannot be safely inspected.
        subprocess.CalledProcessError: A required commit is unavailable locally.
        subprocess.TimeoutExpired: A Git query exceeded thirty seconds.
    """

    revisions: dict[str, None] = {}
    advertised: Optional[tuple[str, ...]] = None
    for update in updates.splitlines():
        columns = update.split()
        if len(columns) != 4:
            raise ValueError(
                "Expected four fields in each pre-push ref update."
            )
        _, local_oid, _, remote_oid = columns
        if set(local_oid) == {"0"}:
            continue
        tip = git_output(
            root,
            "rev-parse",
            "--verify",
            "--end-of-options",
            f"{local_oid}^{{commit}}",
        )
        arguments = ["rev-list", "--reverse", tip]
        if set(remote_oid) != {"0"}:
            previous = git_output(
                root,
                "rev-parse",
                "--verify",
                "--end-of-options",
                f"{remote_oid}^{{commit}}",
            )
            arguments.append(f"^{previous}")
        else:
            if advertised is None:
                advertised = _advertised_commits(root, remote)
            arguments.extend(f"^{commit}" for commit in advertised)
        for revision in git_output(root, *arguments).splitlines():
            revisions[revision] = None
        revisions[tip] = None
    return tuple(revisions)


def check_snapshot(root: Path, *arguments: str) -> bool:
    """Invokes the shared policy checker against one exact Git snapshot.

    Args:
        root: Absolute repository directory.
        arguments: Snapshot selector accepted by the policy checker.

    Returns:
        Whether the snapshot satisfies the checked-in policy.
    """

    result = subprocess.run(
        [
            sys.executable,
            str(root / "scripts" / "check_file_lengths.py"),
            "--root",
            str(root),
            *arguments,
        ],
        cwd=root,
        check=False,
    )
    return result.returncode == 0


def main() -> int:
    """Runs the selected hook and reports unavailable snapshots as failures.

    Returns:
        Zero for an accepted operation, otherwise one.
    """

    parser = argparse.ArgumentParser(
        description="Enforce repository file lengths."
    )
    parser.add_argument("hook", choices=("pre-commit", "pre-push"))
    parser.add_argument("remote", nargs="?", default="")
    parser.add_argument("remote_url", nargs="?", default="")
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        if arguments.hook == "pre-commit":
            return 0 if check_snapshot(root, "--staged") else 1
        destination = arguments.remote_url or arguments.remote
        revisions = outgoing_revisions(root, destination, sys.stdin.read())
        for revision in revisions:
            print(f"Checking outgoing commit {revision}.", flush=True)
            if not check_snapshot(root, "--revision", revision):
                return 1
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"Cannot verify Git file-length policy: {error}", file=sys.stderr)
        print("Fetch missing remote history before retrying.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
