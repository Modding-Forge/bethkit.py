"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from test_git_policy_hooks import _commit, _git
from test_git_policy_hooks import repository as repository

from scripts import git_policy_hooks

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestAdvertisedHistory:
    """Uses actual remote refs instead of stale local tracking information."""

    @pytest.mark.parametrize("kind", ["heads", "tags"])
    def test_stale_tracking_tip_cannot_hide_oversized_intermediate(
        self, repository: Path, kind: str
    ) -> None:
        """Checks new history while excluding only the real advertised base.

        Args:
            repository: Isolated working repository and local bare origin.
            kind: New branch or tag update being pushed.
        """

        # given
        historical = _commit(repository, "pre-policy history\n" * 500)
        _git(repository, "push", "origin", "HEAD:refs/heads/master")
        oversized = _commit(repository, "oversized\n" * 401)
        tip = _commit(repository, "compliant again\n")
        _git(repository, "update-ref", "refs/remotes/origin/deleted", tip)
        if kind == "tags":
            _git(repository, "tag", "-a", "candidate", "-m", "Candidate")
            local_oid = _git(repository, "rev-parse", "refs/tags/candidate")
        else:
            local_oid = tip
        ref = f"refs/{kind}/candidate"
        update = f"{ref} {local_oid} {ref} {'0' * 40}\n"

        # when
        revisions = git_policy_hooks.outgoing_revisions(
            repository, "origin", update
        )

        # then
        assert revisions == (oversized, tip)
        assert historical not in revisions

    def test_peeled_tag_excludes_existing_history_without_local_tag_object(
        self, repository: Path, mocker: MockerFixture
    ) -> None:
        """Verifies advertised peeled commits, not absent annotated-tag objects.

        Args:
            repository: Isolated repository with the advertised commit object.
            mocker: Fixture replacing only the remote advertisement.
        """

        # given
        existing = _commit(repository, "old oversized content\n" * 500)
        tip = _commit(repository, "new compliant content\n")
        original_query = git_policy_hooks.git_output

        def advertise(root: Path, *arguments: str) -> str:
            """Provides a missing tag object with an available peeled commit.

            Args:
                root: Isolated repository receiving the query.
                *arguments: Read-only Git command and its arguments.

            Returns:
                Synthetic advertisement or actual local Git query output.
            """

            if arguments[0] == "ls-remote":
                return (
                    f"{'1' * 40}\trefs/tags/old\n{existing}\trefs/tags/old^{{}}"
                )
            return original_query(root, *arguments)

        mocker.patch.object(
            git_policy_hooks, "git_output", side_effect=advertise
        )
        update = f"refs/heads/new {tip} refs/heads/new {'0' * 40}\n"

        # when / then
        assert git_policy_hooks.outgoing_revisions(
            repository, "origin", update
        ) == (tip,)

    def test_unfetched_advertised_commit_fails_with_fetch_hint(
        self, repository: Path
    ) -> None:
        """Requires actual remote objects instead of trusting cached old refs.

        Args:
            repository: Local repository lacking the publisher's new commit.
        """

        # given
        tip = _commit(repository, "local content\n")
        publisher = repository.parent / "publisher"
        publisher.mkdir()
        _git(publisher, "init", "--initial-branch=master")
        _commit(publisher, "remote-only content\n")
        remote = _git(repository, "remote", "get-url", "origin")
        _git(publisher, "push", remote, "HEAD:refs/heads/master")
        _git(repository, "update-ref", "refs/remotes/origin/master", tip)
        update = f"refs/heads/new {tip} refs/heads/new {'0' * 40}\n"

        # when / then
        with pytest.raises(ValueError, match="fetch heads and tags"):
            git_policy_hooks.outgoing_revisions(repository, "origin", update)

    def test_remote_failure_does_not_reveal_url_credentials(
        self, repository: Path, mocker: MockerFixture
    ) -> None:
        """Suppresses command and stderr details containing remote secrets.

        Args:
            repository: Local repository with a new candidate branch.
            mocker: Fixture injecting the credential-bearing transport failure.
        """

        # given
        tip = _commit(repository, "local content\n")
        secret_url = "https://user:secret@example.invalid/repo"
        original_query = git_policy_hooks.git_output

        def reject_remote(root: Path, *arguments: str) -> str:
            """Fails remote transport without starting any network operation.

            Args:
                root: Isolated repository receiving the query.
                *arguments: Read-only Git command and its arguments.

            Returns:
                Actual local Git query output.

            Raises:
                subprocess.CalledProcessError: A remote command was requested.
            """

            if arguments[0] == "ls-remote":
                raise subprocess.CalledProcessError(1, ["git", secret_url])
            return original_query(root, *arguments)

        mocker.patch.object(
            git_policy_hooks, "git_output", side_effect=reject_remote
        )
        update = f"refs/heads/new {tip} refs/heads/new {'0' * 40}\n"

        # when / then
        with pytest.raises(
            ValueError, match="Cannot read remote refs"
        ) as error:
            git_policy_hooks.outgoing_revisions(repository, secret_url, update)
        assert "secret" not in str(error.value)
