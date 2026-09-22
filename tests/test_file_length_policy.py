"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts import check_file_lengths
from tests import file_length_support as support


def _generated_source(root: Path, count: int) -> None:
    """Creates a marked generated source with an exact physical line count.

    Args:
        root: Fixture root containing the generated module.
        count: Positive number of lines including the marker.

    Raises:
        OSError: The temporary generated source cannot be written.
    """

    path = support.write_lines(root, support.GENERATED_PATH, 0)
    path.write_bytes(
        support.GENERATED_MARKER.encode("utf-8")
        + b"\n"
        + b"fixture\n" * (count - 1)
    )


class TestFileLengthExceptions:
    """Requires explicit, bounded, justified generated-source exceptions."""

    def test_exact_exception_is_bounded(self, tmp_path: Path) -> None:
        """Allows the documented bound but rejects even one extra line.

        Args:
            tmp_path: Isolated generated-source fixture.
        """

        # given
        support.write_policy(
            tmp_path,
            exceptions={
                support.GENERATED_PATH: {
                    "max_lines": 450,
                    "reason": "Generated schema uses one record per module.",
                }
            },
        )
        _generated_source(tmp_path, 450)

        # when
        within_bound = check_file_lengths.check_file_lengths(tmp_path)
        _generated_source(tmp_path, 451)
        above_bound = check_file_lengths.check_file_lengths(tmp_path)

        # then
        assert within_bound == []
        assert any(support.GENERATED_PATH in error for error in above_bound)

    @pytest.mark.parametrize(
        "path",
        [
            "src/bethkit/records/skyrim_se/*.py",
            "src/bethkit/records/skyrim_se/../fixture.py",
            "/src/bethkit/records/skyrim_se/fixture.py",
            "src/bethkit/records/skyrim_se/fi?xture.py",
            "./src/bethkit/records/skyrim_se/fixture.py",
            "C:/src/bethkit/records/skyrim_se/fixture.py",
        ],
    )
    def test_non_exact_paths_are_rejected(
        self, tmp_path: Path, path: str
    ) -> None:
        """Rejects globs and noncanonical paths rather than widening policy.

        Args:
            tmp_path: Isolated generated-source fixture.
            path: Invalid policy key that must not become an exemption.
        """

        _generated_source(tmp_path, 420)
        support.write_policy(
            tmp_path,
            exceptions={
                path: {"max_lines": 450, "reason": "Generated schema."}
            },
        )
        assert check_file_lengths.check_file_lengths(tmp_path)

    @pytest.mark.parametrize(
        "exception",
        [
            {"max_lines": 450, "reason": ""},
            {"max_lines": 450, "reason": "   "},
            {"max_lines": 400, "reason": "Generated schema."},
            {"max_lines": True, "reason": "Generated schema."},
            {"max_lines": 450},
        ],
    )
    def test_invalid_exception_is_rejected(
        self, tmp_path: Path, exception: dict[str, object]
    ) -> None:
        """Requires a real reason and a numeric bound above the ordinary cap.

        Args:
            tmp_path: Isolated generated-source fixture.
            exception: Invalid exception definition.
        """

        _generated_source(tmp_path, 420)
        support.write_policy(
            tmp_path, exceptions={support.GENERATED_PATH: exception}
        )
        assert check_file_lengths.check_file_lengths(tmp_path)

    @pytest.mark.parametrize("lines", [0, 399])
    def test_stale_exception_is_rejected(
        self, tmp_path: Path, lines: int
    ) -> None:
        """Rejects exceptions for missing files and files below the normal cap.

        Args:
            tmp_path: Isolated policy fixture.
            lines: Generated source length, or zero to omit the file.
        """

        if lines:
            _generated_source(tmp_path, lines)
        support.write_policy(
            tmp_path,
            exceptions={
                support.GENERATED_PATH: {
                    "max_lines": 450,
                    "reason": "Generated schema.",
                }
            },
        )
        assert check_file_lengths.check_file_lengths(tmp_path)

    def test_handwritten_file_cannot_claim_exception(
        self, tmp_path: Path
    ) -> None:
        """Rejects ordinary code even when an exact larger limit is supplied.

        Args:
            tmp_path: Isolated hand-written-source fixture.
        """

        support.write_lines(tmp_path, "src/package.py", 420)
        support.write_policy(
            tmp_path,
            exceptions={
                "src/package.py": {"max_lines": 450, "reason": "Convenience."}
            },
        )
        assert check_file_lengths.check_file_lengths(tmp_path)

    def test_staged_policy_cannot_be_relaxed_by_worktree(
        self, tmp_path: Path
    ) -> None:
        """Uses the staged policy together with the staged source files.

        Args:
            tmp_path: Isolated repository with an unstaged policy relaxation.
        """

        # given
        support.create_repository(tmp_path)
        _generated_source(tmp_path, 420)
        support.run_git(tmp_path, "add", support.GENERATED_PATH)
        support.write_policy(
            tmp_path,
            exceptions={
                support.GENERATED_PATH: {
                    "max_lines": 450,
                    "reason": "Generated schema.",
                }
            },
        )

        # when
        staged = check_file_lengths.check_file_lengths(tmp_path, staged=True)
        working = check_file_lengths.check_file_lengths(tmp_path)

        # then
        assert any(support.GENERATED_PATH in error for error in staged)
        assert working == []

    def test_revision_uses_its_own_policy(self, tmp_path: Path) -> None:
        """Does not apply an uncommitted exception to committed source files.

        Args:
            tmp_path: Repository containing an oversized committed module.
        """

        # given
        support.create_repository(tmp_path)
        _generated_source(tmp_path, 420)
        support.run_git(tmp_path, "add", support.GENERATED_PATH)
        support.run_git(tmp_path, "commit", "--quiet", "-m", "test: generated")
        support.write_policy(
            tmp_path,
            exceptions={
                support.GENERATED_PATH: {
                    "max_lines": 450,
                    "reason": "Generated schema.",
                }
            },
        )

        # when
        errors = check_file_lengths.check_file_lengths(
            tmp_path, revision="HEAD"
        )

        # then
        assert any(support.GENERATED_PATH in error for error in errors)
        assert check_file_lengths.check_file_lengths(tmp_path) == []

    def test_generated_directory_requires_a_marker(
        self, tmp_path: Path
    ) -> None:
        """Does not exempt unmarked code solely because of its directory.

        Args:
            tmp_path: Unmarked source pretending to be generated.
        """

        support.write_lines(tmp_path, support.GENERATED_PATH, 420)
        support.write_policy(
            tmp_path,
            exceptions={
                support.GENERATED_PATH: {
                    "max_lines": 450,
                    "reason": "Generated schema.",
                }
            },
        )
        assert check_file_lengths.check_file_lengths(tmp_path)

    @pytest.mark.parametrize(
        "content",
        [
            "not-json",
            '{"format_version":1,"max_lines":400,"max_lines":500,'
            '"exceptions":{}}',
            '{"format_version":1,"max_lines":400,"exceptions":{},'
            '"exceptions":{}}',
            '{"format_version":1,"max_lines":500,"exceptions":{}}',
        ],
        ids=["invalid-json", "duplicate-limit", "duplicate-map", "raised-cap"],
    )
    def test_invalid_policy_fails_closed(
        self, tmp_path: Path, content: str
    ) -> None:
        """Rejects ambiguous or weakened policy instead of choosing a value.

        Args:
            tmp_path: Isolated policy fixture.
            content: Invalid or ambiguous policy bytes represented as text.
        """

        (tmp_path / support.POLICY_NAME).write_text(content, encoding="utf-8")
        assert check_file_lengths.check_file_lengths(tmp_path)


class TestPhysicalLineCounts:
    """Counts physical lines independent of platform or Unicode separators."""

    @pytest.mark.parametrize(
        ("content", "expected_violation"),
        [
            (b"", False),
            (b"line\n" * 400, False),
            (b"line\n" * 399 + b"last", False),
            (b"line\r\n" * 400, False),
            (b"line\n" * 400 + b"last", True),
            (b"line\r\n" * 401, True),
            (b"line\r" * 401, True),
            (("cafe\u0301\u2028inside\n" * 400).encode("utf-8"), False),
            (("caf\u00e9\n" * 401).encode("utf-8"), True),
            (("caf\u00e9\n" * 401).encode("latin-1"), True),
            (b"\0binary\n" * 401, False),
        ],
        ids=[
            "empty",
            "lf-exact-bound",
            "no-final-newline-exact-bound",
            "crlf-exact-bound",
            "no-final-newline-over-bound",
            "crlf-over-bound",
            "cr-over-bound",
            "unicode-separator-is-not-physical-newline",
            "utf8-over-bound",
            "latin1-over-bound",
            "nul-binary-is-excluded",
        ],
    )
    def test_text_boundaries(
        self, tmp_path: Path, content: bytes, expected_violation: bool
    ) -> None:
        """Checks line boundaries without counting Unicode as extra newlines.

        Args:
            tmp_path: Isolated plain-source fixture.
            content: Exact file bytes, including any final newline.
            expected_violation: Whether the 400-line maximum is exceeded.
        """

        support.write_policy(tmp_path)
        filename = "fixture.bin" if b"\0" in content else "fixture.txt"
        (tmp_path / filename).write_bytes(content)
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert bool(errors) is expected_violation
        if expected_violation:
            assert any(filename in error for error in errors)
