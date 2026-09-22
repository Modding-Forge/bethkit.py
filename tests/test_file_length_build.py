"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import TYPE_CHECKING, Any
from unittest.mock import MagicMock

import pytest

from scripts import hatch_build

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestFileLengthBuildGate:
    """Ensures no build target skips or weakens the source policy."""

    @pytest.mark.parametrize(
        ("target", "version"),
        [("wheel", "standard"), ("wheel", "editable"), ("sdist", "standard")],
    )
    def test_violation_blocks_every_build_variant(
        self,
        target: str,
        version: str,
        tmp_path: Path,
        mocker: MockerFixture,
    ) -> None:
        """Rejects invalid source before native loading or packaging."""

        # given
        gate = mocker.patch.object(
            hatch_build,
            "_validate_file_lengths",
            side_effect=RuntimeError("source exceeds 400 lines"),
        )
        native = mocker.patch.object(hatch_build, "_validate_library")
        hook = hatch_build.CustomBuildHook(
            str(tmp_path), {}, MagicMock(), MagicMock(), str(tmp_path), target
        )
        build_data: dict[str, Any] = {}

        # when
        with pytest.raises(RuntimeError, match="exceeds 400"):
            hook.initialize(version, build_data)

        # then
        gate.assert_called_once_with(tmp_path)
        native.assert_not_called()
        assert build_data == {}

    def test_source_distribution_keeps_checker_and_policy(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Includes the policy tooling so extracted source builds stay gated."""

        # given
        gate = mocker.patch.object(hatch_build, "_validate_file_lengths")
        scratch = tmp_path / "scripts" / "ignored_work_notes.py"
        scratch.parent.mkdir()
        scratch.write_text("# Work notes\n" * 401, encoding="utf-8")
        (tmp_path / ".gitignore").write_text(
            "scripts/ignored_work_notes.py\n", encoding="utf-8"
        )
        hook = hatch_build.CustomBuildHook(
            str(tmp_path), {}, MagicMock(), MagicMock(), str(tmp_path), "sdist"
        )
        build_data: dict[str, Any] = {}

        # when
        hook.initialize("standard", build_data)

        # then
        gate.assert_called_once_with(tmp_path)
        expected = (
            "scripts/hatch_build.py",
            "scripts/check_file_lengths.py",
            "scripts/_file_length_text.py",
            "scripts/_file_length_archive.py",
            "file-length-policy.json",
        )
        assert build_data["force_include"] == {
            str(tmp_path / relative): relative for relative in expected
        }
        assert str(scratch) not in build_data["force_include"]

    def test_missing_checker_fails_closed(self, tmp_path: Path) -> None:
        """Cannot build source distributions that omit the policy checker."""

        with pytest.raises(RuntimeError, match="checker is missing"):
            hatch_build._validate_file_lengths(tmp_path)

    def test_checker_failure_is_reported(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Propagates the checker diagnostic instead of allowing the build."""

        # given
        checker = tmp_path / "scripts" / "check_file_lengths.py"
        checker.parent.mkdir()
        checker.touch()
        process = mocker.patch.object(
            hatch_build.subprocess,
            "run",
            return_value=subprocess.CompletedProcess(
                [], 1, stdout="module.py: 401 lines > 400", stderr=""
            ),
        )

        # when
        with pytest.raises(RuntimeError, match="module.py: 401 lines"):
            hatch_build._validate_file_lengths(tmp_path)

        # then
        process.assert_called_once()

    def test_checker_launch_failure_blocks_build(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Reports process-launch failure without suppressing enforcement."""

        # given
        checker = tmp_path / "scripts" / "check_file_lengths.py"
        checker.parent.mkdir()
        checker.touch()
        mocker.patch.object(
            hatch_build.subprocess, "run", side_effect=OSError("unavailable")
        )

        # when
        with pytest.raises(RuntimeError, match="Cannot execute"):
            hatch_build._validate_file_lengths(tmp_path)
