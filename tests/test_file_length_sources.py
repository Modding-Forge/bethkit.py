"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import venv
from pathlib import Path

import pytest

from scripts import check_file_lengths
from tests import file_length_support as support


class TestFileLengthSnapshots:
    """Checks the exact Git snapshot rather than unrelated on-disk content."""

    def test_staged_check_does_not_read_worktree(self, tmp_path: Path) -> None:
        """Checks staged bytes even when the working copy is longer.

        Args:
            tmp_path: Isolated temporary repository root.
        """

        # given
        support.create_repository(tmp_path)
        support.write_lines(tmp_path, "module.py", 400)
        support.run_git(tmp_path, "add", "module.py")
        support.write_lines(tmp_path, "module.py", 401)

        # when
        staged = check_file_lengths.check_file_lengths(tmp_path, staged=True)
        working = check_file_lengths.check_file_lengths(tmp_path)

        # then
        assert staged == []
        assert any("module.py" in error for error in working)

    def test_short_worktree_cannot_hide_staged_violation(
        self, tmp_path: Path
    ) -> None:
        """Rejects oversized index content despite an unstaged local fix.

        Args:
            tmp_path: Isolated temporary repository root.
        """

        # given
        support.create_repository(tmp_path)
        support.write_lines(tmp_path, "module.py", 401)
        support.run_git(tmp_path, "add", "module.py")
        support.write_lines(tmp_path, "module.py", 1)

        # when
        errors = check_file_lengths.check_file_lengths(tmp_path, staged=True)

        # then
        assert any("module.py" in error for error in errors)
        assert check_file_lengths.check_file_lengths(tmp_path) == []

    def test_revision_uses_committed_bytes(self, tmp_path: Path) -> None:
        """Keeps revision validation independent of index and worktree fixes.

        Args:
            tmp_path: Isolated temporary repository root.
        """

        # given
        support.create_repository(tmp_path)
        initial = support.run_git(tmp_path, "rev-parse", "HEAD").strip()
        support.write_lines(tmp_path, "module.py", 401)
        support.run_git(tmp_path, "add", "module.py")
        support.run_git(tmp_path, "commit", "--quiet", "-m", "test: oversized")
        support.write_lines(tmp_path, "module.py", 1)
        support.run_git(tmp_path, "add", "module.py")

        # when
        errors = check_file_lengths.check_file_lengths(
            tmp_path, revision="HEAD"
        )

        # then
        assert any("module.py" in error for error in errors)
        assert (
            check_file_lengths.check_file_lengths(tmp_path, revision=initial)
            == []
        )

    def test_untracked_files_are_checked(self, tmp_path: Path) -> None:
        """Includes new source files before they have been staged.

        Args:
            tmp_path: Isolated temporary repository root.
        """

        support.create_repository(tmp_path)
        support.write_lines(tmp_path, "new module.py", 401)
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert any("new module.py" in error for error in errors)

    def test_ignored_files_are_not_worktree_sources(
        self, tmp_path: Path
    ) -> None:
        """Excludes existing ignored artifacts but still checks tracked files.

        Args:
            tmp_path: Isolated temporary repository root.
        """

        # given
        support.create_repository(tmp_path)
        (tmp_path / ".gitignore").write_text("artifacts/\n", encoding="utf-8")
        support.write_lines(tmp_path, "artifacts/local.log", 900)

        # when
        before_tracking = check_file_lengths.check_file_lengths(tmp_path)
        support.run_git(tmp_path, "add", "--force", "artifacts/local.log")
        after_tracking = check_file_lengths.check_file_lengths(tmp_path)

        # then
        assert before_tracking == []
        assert any("artifacts/local.log" in error for error in after_tracking)

    def test_unknown_revision_fails_closed(self, tmp_path: Path) -> None:
        """Reports missing Git objects instead of silently checking HEAD.

        Args:
            tmp_path: Isolated temporary repository root.
        """

        support.create_repository(tmp_path)
        assert check_file_lengths.check_file_lengths(
            tmp_path, revision="refs/heads/nonexistent-fixture"
        )

    @pytest.mark.parametrize("mode", ["staged", "revision"])
    def test_git_symlink_modes_fail(self, tmp_path: Path, mode: str) -> None:
        """Rejects link modes even on systems that check out links as files.

        Args:
            tmp_path: Isolated repository without real operating-system links.
            mode: Index or committed-tree snapshot to inspect.
        """

        # given
        support.create_repository(tmp_path)
        target = support.write_lines(tmp_path, "link-target.txt", 1)
        blob = support.run_git(
            tmp_path, "hash-object", "-w", str(target)
        ).strip()
        support.run_git(
            tmp_path,
            "update-index",
            "--add",
            "--cacheinfo",
            f"120000,{blob},linked.py",
        )
        if mode == "revision":
            support.run_git(
                tmp_path, "commit", "--quiet", "-m", "test: record link mode"
            )

        # when
        errors = check_file_lengths.check_file_lengths(
            tmp_path,
            staged=mode == "staged",
            revision="HEAD" if mode == "revision" else None,
        )

        # then
        assert any(
            "Symbolic source" in error and "linked.py" in error
            for error in errors
        )


class TestFileLengthSourceArchives:
    """Applies the same source limit without requiring Git metadata."""

    def test_archive_sources_are_checked(self, tmp_path: Path) -> None:
        """Finds deeply nested sources in an extracted source archive.

        Args:
            tmp_path: Extracted-source fixture with no Git directory.
        """

        support.write_policy(tmp_path)
        support.write_lines(tmp_path, "src/package/deep/module.py", 401)
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert any("src/package/deep/module.py" in error for error in errors)

    @pytest.mark.parametrize("directory", [".pytest_cache", "__pycache__"])
    def test_archive_metadata_is_not_checked(
        self, tmp_path: Path, directory: str
    ) -> None:
        """Does not classify known environment metadata as archive sources.

        Args:
            tmp_path: Extracted-source fixture with no Git repository.
            directory: Non-source metadata directory to ignore.
        """

        support.write_policy(tmp_path)
        support.write_lines(tmp_path, f"{directory}/artifact.txt", 401)
        assert check_file_lengths.check_file_lengths(tmp_path) == []

    @pytest.mark.parametrize(
        "directory", ["build", "dist", "target", "venv", ".venv"]
    )
    def test_output_directory_names_do_not_exempt_sources(
        self, tmp_path: Path, directory: str
    ) -> None:
        """Checks maintained sources wherever an archive actually contains them.

        Args:
            tmp_path: Unpacked source archive without Git metadata.
            directory: Conventional artifact name that must not exempt sources.
        """

        support.write_policy(tmp_path)
        name = f"{directory}/maintained.py"
        support.write_lines(tmp_path, name, 401)
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert any(name in error for error in errors)

    def test_marker_alone_cannot_exempt_sources(self, tmp_path: Path) -> None:
        """Does not treat an arbitrary pyvenv.cfg marker as an environment.

        Args:
            tmp_path: Unpacked source archive with an ambiguous marker.
        """

        support.write_policy(tmp_path)
        name = "build/maintained.py"
        support.write_lines(tmp_path, name, 401)
        (tmp_path / "build" / "pyvenv.cfg").write_text(
            "home = fixture\n", encoding="utf-8"
        )
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert any(name in error for error in errors)

    def test_real_editable_environment_is_not_source(
        self, tmp_path: Path
    ) -> None:
        """Recognizes an actual development environment by its installed layout.

        Args:
            tmp_path: Source archive with a real isolated Python environment.
        """

        support.write_policy(tmp_path)
        environment = tmp_path / "development-environment"
        venv.EnvBuilder(with_pip=False).create(environment)
        support.write_lines(environment, "installed-dependency.py", 401)
        assert check_file_lengths.check_file_lengths(tmp_path) == []

    @pytest.mark.parametrize("mode", ["staged", "revision"])
    def test_git_modes_reject_plain_archives(
        self, tmp_path: Path, mode: str
    ) -> None:
        """Never substitutes archive scanning for an unavailable Git snapshot.

        Args:
            tmp_path: Source archive without Git metadata.
            mode: Requested Git-only check mode.
        """

        support.write_policy(tmp_path)
        errors = check_file_lengths.check_file_lengths(
            tmp_path,
            staged=mode == "staged",
            revision="HEAD" if mode == "revision" else None,
        )
        assert errors

    def test_broken_git_metadata_fails_closed(self, tmp_path: Path) -> None:
        """Does not hide inaccessible repository metadata via archive mode.

        Args:
            tmp_path: Fixture containing an invalid Git metadata directory.
        """

        support.write_policy(tmp_path)
        (tmp_path / ".git").mkdir()
        assert check_file_lengths.check_file_lengths(tmp_path)
