"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.compare_string_benchmarks import compare


class TestStringBenchmarkComparison:
    """Rejects misleading speedups when content, addresses or errors differ."""

    @pytest.mark.parametrize(
        "changed", ["references_sha256", "sha256", "failure", "path"]
    )
    def test_changed_contract_fails(self, tmp_path: Path, changed: str) -> None:
        """Requires source and observed behavior equivalence before timing.

        Args:
            tmp_path: Isolated report directory.
            changed: Contract field deliberately changed by the candidate.
        """

        row: dict[str, object] = {
            "path": "test.esp",
            "size": 20,
            "sha256": "source",
            "count": 1,
            "references_sha256": "references",
            "decision": {},
            "failure": None,
            "open_seconds": 1,
            "detect_seconds": 1,
            "enumerate_seconds": 10,
        }
        before = tmp_path / "before.jsonl"
        after = tmp_path / "after.jsonl"
        before.write_text(json.dumps(row), encoding="utf-8")
        row[changed] = "changed"
        after.write_text(json.dumps(row), encoding="utf-8")
        with pytest.raises(ValueError, match="mismatch"):
            compare(before, after)

    def test_partial_corpus_fails(self, tmp_path: Path) -> None:
        """Rejects incomplete runs rather than reporting apparent speedups.

        Args:
            tmp_path: Isolated report directory.
        """

        before = tmp_path / "before.jsonl"
        after = tmp_path / "after.jsonl"
        before.write_text("", encoding="utf-8")
        after.write_text("", encoding="utf-8")
        with pytest.raises(ValueError, match="nonempty corpus"):
            compare(before, after)
