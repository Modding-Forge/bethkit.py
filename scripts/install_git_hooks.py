"""
Copyright (c) Modding Forge
"""

# Installs opt-in repository hooks without replacing a user's hook manager.

from __future__ import annotations

import stat
import subprocess
import sys
from pathlib import Path


def git_config(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    """Runs Git configuration or repository discovery for hook installation.

    Args:
        root: Repository directory containing this script.
        arguments: Git command and arguments.

    Returns:
        Captured Git output and status.

    Raises:
        OSError: Git cannot be executed.
    """

    return subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", *arguments],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )


def install(root: Path, interpreter: Path) -> None:
    """Enables project hooks only when no existing hook setup would be replaced.

    Args:
        root: Absolute repository directory.
        interpreter: Python 3.10 or newer executable used by both hooks.

    Raises:
        RuntimeError: Git fails or a different hook installation already exists.
        OSError: Hook permissions cannot be adjusted.
    """

    hooks = root / ".githooks"
    configured = git_config(root, "config", "--get", "core.hooksPath")
    if configured.returncode not in (0, 1):
        raise RuntimeError(configured.stderr.strip())
    current = configured.stdout.strip()
    if current:
        current_path = Path(current).expanduser()
        if not current_path.is_absolute():
            current_path = root / current_path
        if current_path.resolve() != hooks.resolve():
            raise RuntimeError(
                f"Existing core.hooksPath is {current!r}; configure chaining "
                "with that hook manager instead of replacing it."
            )
    else:
        result = git_config(root, "rev-parse", "--git-path", "hooks")
        if result.returncode:
            raise RuntimeError(result.stderr.strip())
        default_hooks = Path(result.stdout.strip())
        if not default_hooks.is_absolute():
            default_hooks = root / default_hooks
        active = (
            [
                path.name
                for path in default_hooks.iterdir()
                if path.is_file() and not path.name.endswith(".sample")
            ]
            if default_hooks.is_dir()
            else []
        )
        if active:
            raise RuntimeError(
                f"Existing Git hooks found: {', '.join(sorted(active))}. "
                "Integrate them explicitly before installing project hooks."
            )
    for name in ("pre-commit", "pre-push"):
        path = hooks / name
        path.chmod(
            path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
        )
    for key, value in (
        ("bethkit.policyPython", interpreter.resolve().as_posix()),
        ("core.hooksPath", ".githooks"),
    ):
        result = git_config(root, "config", "--local", key, value)
        if result.returncode:
            raise RuntimeError(result.stderr.strip())


def main() -> int:
    """Installs hooks with this interpreter without modifying the Git index.

    Returns:
        Zero after installation, otherwise one.
    """

    # This standalone installer may run before package dependency validation.
    if sys.version_info < (3, 10):  # noqa: UP036
        print("Repository hooks require Python 3.10 or newer.", file=sys.stderr)
        return 1
    root = Path(__file__).resolve().parents[1]
    try:
        install(root, Path(sys.executable))
    except (OSError, RuntimeError) as error:
        print(f"Git hook installation refused: {error}", file=sys.stderr)
        return 1
    print("Installed staged-commit and outgoing-push file-length checks.")
    print(f"Hook interpreter: {Path(sys.executable).resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
