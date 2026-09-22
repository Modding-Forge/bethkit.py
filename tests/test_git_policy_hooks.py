"""
Copyright (c) Modding Forge
"""

# Uses isolated repositories to exercise staged and outgoing-commit guards.

from __future__ import annotations

import io
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from scripts import git_policy_hooks, install_git_hooks

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def _git(root: Path, *arguments: str) -> str:
    """Runs Git only inside a temporary test repository.

    Args:
        root: Isolated repository created by pytest.
        arguments: Command and arguments for Git.

    Returns:
        Stripped command output.

    Raises:
        subprocess.CalledProcessError: Test repository setup fails.
    """

    return subprocess.run(
        [
            "git",
            "-c",
            f"safe.directory={root.as_posix()}",
            "-c",
            "user.name=Policy Test",
            "-c",
            "user.email=policy@example.invalid",
            *arguments,
        ],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


@pytest.fixture
def repository(tmp_path: Path) -> Path:
    """Creates an isolated Git repository without touching the project index.

    Args:
        tmp_path: Temporary directory managed by pytest.

    Returns:
        Initialized repository with a configured origin name.
    """

    root = tmp_path / "work"
    remote = tmp_path / "remote.git"
    root.mkdir()
    remote.mkdir()
    _git(remote, "init", "--bare")
    _git(root, "init", "--initial-branch=master")
    _git(root, "remote", "add", "origin", remote.as_posix())
    return root


def _commit(root: Path, text: str) -> str:
    """Creates one content snapshot in an isolated test repository.

    Args:
        root: Temporary repository.
        text: Sample file content for this commit.

    Returns:
        Created commit hash.
    """

    (root / "sample.py").write_text(text, encoding="utf-8")
    _git(root, "add", "sample.py")
    _git(root, "commit", "-m", "test: record policy snapshot")
    return _git(root, "rev-parse", "HEAD")


class TestOutgoingSnapshots:
    """Ensures a short current file cannot hide an oversized outgoing commit."""

    def test_includes_intermediate_commits(self, repository: Path) -> None:
        """Includes intermediate violations even when the final file is short.

        Args:
            repository: Isolated Git repository.
        """

        # given
        previous = _commit(repository, "initial\n")
        oversized = _commit(repository, "line\n" * 401)
        tip = _commit(repository, "short again\n")
        update = f"refs/heads/master {tip} refs/heads/master {previous}\n"
        # when
        revisions = git_policy_hooks.outgoing_revisions(
            repository, "origin", update
        )
        # then
        assert revisions == (oversized, tip)

    def test_checks_tag_tip_already_present_on_remote(
        self, repository: Path
    ) -> None:
        """Checks a tag even when its commit is already on the remote.

        Args:
            repository: Isolated Git repository.
        """

        # given
        tip = _commit(repository, "sample\n")
        _git(repository, "push", "origin", "HEAD:refs/heads/master")
        _git(repository, "tag", "-a", "v1.0.0", "-m", "Test release")
        tag = _git(repository, "rev-parse", "refs/tags/v1.0.0")
        update = f"refs/tags/v1.0.0 {tag} refs/tags/v1.0.0 {'0' * 40}\n"
        # when
        revisions = git_policy_hooks.outgoing_revisions(
            repository, "origin", update
        )
        # then
        assert revisions == (tip,)

    def test_skips_deletions(self, repository: Path) -> None:
        """Does not demand a content snapshot for a deleted destination ref.

        Args:
            repository: Isolated Git repository.
        """

        update = f"(delete) {'0' * 40} refs/heads/old {'1' * 40}\n"
        assert (
            git_policy_hooks.outgoing_revisions(repository, "origin", update)
            == ()
        )

    def test_missing_remote_history_fails_closed(
        self, repository: Path
    ) -> None:
        """Requires fetching absent remote history instead of guessing a range.

        Args:
            repository: Isolated Git repository.
        """

        tip = _commit(repository, "sample\n")
        update = f"refs/heads/master {tip} refs/heads/master {'1' * 40}\n"
        with pytest.raises(subprocess.CalledProcessError):
            git_policy_hooks.outgoing_revisions(repository, "origin", update)


class TestHookInvocation:
    """Binds the commit guard to the staged snapshot."""

    def test_commit_selects_staged_snapshot(
        self, mocker: MockerFixture
    ) -> None:
        """Forwards the explicit staged selector to the shared checker.

        Args:
            mocker: Restored command-line and checker patches.
        """

        # given
        mocker.patch.object(sys, "argv", ["git_policy_hooks.py", "pre-commit"])
        check = mocker.patch.object(
            git_policy_hooks, "check_snapshot", return_value=True
        )
        # when
        result = git_policy_hooks.main()
        # then
        assert result == 0
        check.assert_called_once_with(
            Path(git_policy_hooks.__file__).resolve().parents[1], "--staged"
        )

    def test_push_stops_at_failing_intermediate_snapshot(
        self, mocker: MockerFixture
    ) -> None:
        """Rejects an intermediate failure even when the tip is compliant.

        Args:
            mocker: Restored input and checker patches.
        """

        # given
        mocker.patch.object(
            sys, "argv", ["git_policy_hooks.py", "pre-push", "origin", "url"]
        )
        mocker.patch.object(sys, "stdin", io.StringIO("ref update\n"))
        outgoing = mocker.patch.object(
            git_policy_hooks, "outgoing_revisions", return_value=("bad", "tip")
        )
        check = mocker.patch.object(
            git_policy_hooks, "check_snapshot", return_value=False
        )
        # when
        result = git_policy_hooks.main()
        # then
        root = Path(git_policy_hooks.__file__).resolve().parents[1]
        assert result == 1
        outgoing.assert_called_once_with(root, "url", "ref update\n")
        check.assert_called_once_with(root, "--revision", "bad")


class TestHookInstallation:
    """Protects existing hook managers and records the selected interpreter."""

    def test_refuses_existing_hook_manager(self, repository: Path) -> None:
        """Never silently replaces a custom hooks path.

        Args:
            repository: Isolated Git repository.
        """

        _git(repository, "config", "core.hooksPath", "custom-hooks")
        with pytest.raises(RuntimeError, match="Existing core.hooksPath"):
            install_git_hooks.install(repository, Path(sys.executable))
        assert _git(repository, "config", "core.hooksPath") == "custom-hooks"

    def test_refuses_active_default_hooks(self, repository: Path) -> None:
        """Leaves existing unmanaged hooks active instead of shadowing them.

        Args:
            repository: Isolated Git repository.
        """

        hook = repository / ".git" / "hooks" / "pre-commit"
        hook.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        with pytest.raises(RuntimeError, match="Existing Git hooks found"):
            install_git_hooks.install(repository, Path(sys.executable))
        assert hook.read_text(encoding="utf-8") == "#!/bin/sh\nexit 0\n"

    def test_installs_idempotently_with_exact_interpreter(
        self, repository: Path
    ) -> None:
        """Permits repeated installation without changing the index.

        Args:
            repository: Isolated Git repository.
        """

        # given
        hooks = repository / ".githooks"
        hooks.mkdir()
        for name in ("pre-commit", "pre-push"):
            (hooks / name).write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        interpreter = Path(sys.executable)
        # when
        install_git_hooks.install(repository, interpreter)
        install_git_hooks.install(repository, interpreter)
        # then
        assert _git(repository, "config", "core.hooksPath") == ".githooks"
        assert _git(repository, "config", "bethkit.policyPython") == (
            interpreter.resolve().as_posix()
        )
        assert not _git(repository, "diff", "--cached", "--name-only")
