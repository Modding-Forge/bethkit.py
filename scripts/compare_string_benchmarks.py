"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Optional

import pydantic


class BenchmarkResult(pydantic.BaseModel, frozen=True):
    """Validated per-plugin result, including partial results before errors."""

    path: str
    """Exact input path, also preserving corpus order."""
    size: int
    """Input file size in bytes."""
    sha256: str
    """Fingerprint of the complete unchanged source plugin."""
    count: int
    """Number of references emitted before EOF or a reported error."""
    references_sha256: str
    """Ordered fingerprint of references, addresses and codec metadata."""
    decision: dict[str, str | int]
    """Retained detector evidence and selected plugin codec."""
    failure: Optional[str]
    """Exact exception text, never discarded from equivalence checks."""
    open_seconds: float
    """Time to open the plugin."""
    detect_seconds: float
    """Time to create its plugin-specific context."""
    enumerate_seconds: float
    """Time to enumerate and fingerprint strings, including owner cleanup."""


def compare(before: Path, after: Path) -> dict[str, int | float]:
    """Rejects changed results before reporting observed throughput.

    Args:
        before: Complete baseline JSON-lines report.
        after: Report for the same ordered real-file corpus.

    Returns:
        Aggregate counts, durations and observed enumeration speedup.

    Raises:
        OSError: A report cannot be read.
        pydantic.ValidationError: A report row is invalid.
        ValueError: Corpora, text, addresses, decisions or errors differ.
    """

    baseline = [
        BenchmarkResult.model_validate_json(line)
        for line in before.read_text(encoding="utf-8").splitlines()
    ]
    candidate = [
        BenchmarkResult.model_validate_json(line)
        for line in after.read_text(encoding="utf-8").splitlines()
    ]
    if not baseline or len(baseline) != len(candidate):
        raise ValueError("Reports must contain the same nonempty corpus")
    timing = {"open_seconds", "detect_seconds", "enumerate_seconds"}
    for old, new in zip(baseline, candidate):
        if old.model_dump(exclude=timing) != new.model_dump(exclude=timing):
            raise ValueError(
                f"Reference, input, decision or error mismatch: {old.path}"
            )
    old_seconds = sum(row.enumerate_seconds for row in baseline)
    new_seconds = sum(row.enumerate_seconds for row in candidate)
    return {
        "plugins": len(baseline),
        "references": sum(row.count for row in baseline),
        "failures_preserved": sum(row.failure is not None for row in baseline),
        "baseline_detection_seconds": sum(
            row.detect_seconds for row in baseline
        ),
        "candidate_detection_seconds": sum(
            row.detect_seconds for row in candidate
        ),
        "baseline_enumeration_seconds": old_seconds,
        "candidate_enumeration_seconds": new_seconds,
        "enumeration_speedup": old_seconds / new_seconds if new_seconds else 0,
    }


def main() -> None:
    """Compares complete reports and fails before printing misleading speedups.

    Raises:
        OSError: An input report is inaccessible.
        ValueError: The reports are not equivalent.
    """

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    arguments = parser.parse_args()
    print(json.dumps(compare(arguments.before, arguments.after), indent=2))


if __name__ == "__main__":
    main()
