"""
Copyright (c) Modding Forge

Static contracts for generated field references and immutable record views.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Optional

import pydantic


class _Position(pydantic.BaseModel, frozen=True):
    """Source position of an independent typing probe."""

    line: int
    """Zero-based source line."""


class _Range(pydantic.BaseModel, frozen=True):
    """Source range selected by a type-checking diagnostic."""

    start: _Position
    """Start position of the invalid operation."""


class _Diagnostic(pydantic.BaseModel, frozen=True):
    """Relevant diagnostic fields from Pyright's machine-readable output."""

    severity: str
    """Diagnostic severity reported by the type checker."""
    message: str
    """Description of the violated type contract."""
    range: _Range
    """Source position used to require rejection of every invalid operation."""
    rule: Optional[str] = None
    """Specific type-checking rule, when provided."""


class _Result(pydantic.BaseModel, frozen=True):
    """Validated diagnostic collection returned by one static check."""

    diagnostics: tuple[_Diagnostic, ...] = pydantic.Field(
        alias="generalDiagnostics"
    )
    """Diagnostics produced for the isolated source snippet."""


def _check_source(tmp_path: Path, source: str) -> tuple[_Diagnostic, ...]:
    """Runs strict Pyright against a standalone consumer of the public API.

    Args:
        tmp_path: Isolated temporary directory owned by pytest.
        source: Complete Python source containing one or more typing probes.

    Returns:
        Validated diagnostics without loading the native library.
    """

    path = tmp_path / "typing_probe.py"
    path.write_text(source, encoding="utf-8")
    project = Path(__file__).resolve().parents[3]
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pyright",
            "--outputjson",
            "--pythonpath",
            sys.executable,
            "--project",
            str(project),
            str(path),
        ],
        cwd=project,
        check=False,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode in (0, 1), result.stderr
    return _Result.model_validate_json(result.stdout).diagnostics


class TestGeneratedStaticTyping:
    """Protects editor value inference and frozen generated model contracts."""

    def test_accepts_exact_field_types(self, tmp_path: Path) -> None:
        """Accepts valid field replacements and retains the concrete value type.

        Args:
            tmp_path: Isolated source-snippet directory.
        """

        # given
        source = '''"""Valid typed public API usage."""
from typing import Optional
from bethkit import RecordEditor
from bethkit.records import FieldRef
from bethkit.records.skyrim_se import QuestRecord

def accepted(editor: RecordEditor, quest: QuestRecord) -> None:
    """Uses generated and explicitly annotated typed references."""
    reference: FieldRef[Optional[str]] = quest.field("editor_id")
    value: Optional[str] = reference.value
    editor.set(reference, value)
    editor.set(reference, "A new editor ID")
    editor.set(reference, None)
    editor.set(quest.field("editor_id"), "Another editor ID")
'''
        # when
        diagnostics = _check_source(tmp_path, source)
        # then
        assert not diagnostics, diagnostics

    def test_rejects_wrong_values_and_immutable_assignments(
        self, tmp_path: Path
    ) -> None:
        """Rejects integer text edits and writes to frozen views and references.

        Args:
            tmp_path: Isolated source-snippet directory.
        """

        # given
        source = '''"""Invalid calls rejected by public annotations."""
from typing import Optional
from bethkit import RecordEditor
from bethkit.records import FieldRef
from bethkit.records.skyrim_se import QuestRecord

def rejected(
    editor: RecordEditor, quest: QuestRecord, reference: FieldRef[Optional[str]]
) -> None:
    """Exercises independent consumer mistakes without suppressions."""
    editor.set(quest.field("editor_id"), 123)
    editor.set(reference, 123)
    quest.editor_id = "Mutated"
    reference.value = "Mutated"
    reference.address = None
'''
        # when
        diagnostics = _check_source(tmp_path, source)
        # then
        errors = tuple(item for item in diagnostics if item.severity == "error")
        assert {item.range.start.line for item in errors} == {
            10,
            11,
            12,
            13,
            14,
        }, diagnostics
        assert all(
            item.rule
            in {
                "reportCallIssue",
                "reportArgumentType",
                "reportAttributeAccessIssue",
            }
            for item in errors
        ), errors
        assert sum("read-only" in item.message for item in errors) == 3
