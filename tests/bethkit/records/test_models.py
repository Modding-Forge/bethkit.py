"""
Copyright (c) Modding Forge

Unit tests for immutable generated views without loading a native library.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import cast

import pydantic
import pytest

from bethkit._error import RecordDecodeError, SchemaMismatchError
from bethkit.records import _base, _wire
from bethkit.records.skyrim_se import QuestRecord

_STAGE: str = "QUST/10:Stages/repeat/0:Stage"
_ENTRY: str = _STAGE + "/1:Log Entries/repeat/0:Log Entry"
_TEXT: str = _ENTRY + "/2:Log Entry"


def _text(stage: int, entry: int, index: int, text: str) -> _wire.WireField:
    """Builds an addressed native text leaf with nested repeat scopes."""

    address = _wire.FieldAddress(
        schema_payload_sha256=QuestRecord.schema_sha256,
        structure_hash="structure",
        record_signature=(81, 85, 83, 84),
        form_id=0x800,
        subrecord_index=index,
        subrecord_path=_TEXT,
        repeat_scopes=(
            _wire.RepeatScope(path=_STAGE, occurrence=stage),
            _wire.RepeatScope(path=_ENTRY, occurrence=entry),
        ),
    )
    return _wire.WireField(
        name="Log Entry",
        node_id=1,
        path=_TEXT,
        span=_wire.ByteSpan(start=0, end=len(text) + 1),
        origin="schema",
        address=address,
        value=_wire.WireScalar(kind="string", address=address, value=text),
    )


def _snapshot(*fields: _wire.WireField) -> _wire.RecordSnapshot:
    """Builds a schema-pinned in-memory record snapshot."""

    return _wire.RecordSnapshot(
        format_version=1,
        schema_payload_sha256=QuestRecord.schema_sha256,
        structure_hash="structure",
        record_signature="QUST",
        form_id=0x800,
        fields=fields,
    )


class TestGeneratedModels:
    """Checks hierarchy, immutability, schema identity, and lazy loading."""

    def test_partial_snapshot_cannot_become_a_complete_model(self) -> None:
        """A strings-only projection never silently supplies default fields."""

        snapshot = _snapshot().model_copy(update={"projection": "strings"})
        with pytest.raises(RecordDecodeError, match="full record snapshot"):
            QuestRecord.from_snapshot(snapshot)

    def test_native_scope_resets_entries_per_stage(self) -> None:
        """An Entry occurrence of zero in stage two is not stage one's entry."""

        # given
        snapshot = _snapshot(
            _text(0, 0, 0, "First"),
            _text(0, 1, 1, "Second"),
            _text(1, 0, 2, "Third"),
        )

        # when
        quest = QuestRecord.from_snapshot(snapshot)

        # then
        assert len(quest.stages) == 2
        assert tuple(e.log_entry for e in quest.stages[0].log_entries) == (
            "First",
            "Second",
        )
        target = quest.stages[1].log_entries[0]
        assert target.log_entry == "Third"
        reference = target.field("log_entry")
        assert reference.value == "Third"
        assert reference.address is not None
        assert reference.address.subrecord_index == 2
        assert _base.encode_replacement(reference, "Replacement") == {
            "kind": "string",
            "value": "Replacement",
        }

    def test_every_nested_view_is_frozen(self) -> None:
        """Neither root nor nested fields allow accidental in-place edits."""

        quest = QuestRecord.from_snapshot(_snapshot(_text(0, 0, 0, "Original")))
        with pytest.raises(pydantic.ValidationError):
            setattr(quest, "editor_id", "Changed")
        with pytest.raises(pydantic.ValidationError):
            setattr(quest.stages[0].log_entries[0], "log_entry", "Changed")

    def test_mismatched_schema_fails_before_materialization(self) -> None:
        """Generated classes never silently decode another schema revision."""

        snapshot = _snapshot().model_copy(
            update={"schema_payload_sha256": "other"}
        )
        with pytest.raises(SchemaMismatchError, match="schemas? differ"):
            QuestRecord.from_snapshot(snapshot)

    def test_wrong_signature_is_rejected(self) -> None:
        """Record types are not interchangeable when their fields overlap."""

        snapshot = _snapshot().model_copy(update={"record_signature": "INFO"})
        with pytest.raises(SchemaMismatchError, match="Expected QUST"):
            QuestRecord.from_snapshot(snapshot)

    def test_bad_native_value_raises_domain_error(self) -> None:
        """An incompatible native payload does not leak an opaque FFI error."""

        leaf = _text(0, 0, 0, "Text")
        bad_value = leaf.value.model_copy(
            update={"kind": "bytes", "value": (255,)}
        )
        snapshot = _snapshot(leaf.model_copy(update={"value": bad_value}))
        with pytest.raises(RecordDecodeError):
            QuestRecord.from_snapshot(snapshot)

    def test_generated_field_rejects_wrong_replacement_type(self) -> None:
        """Runtime validation also protects callers that evade static typing."""

        quest = QuestRecord.from_snapshot(_snapshot(_text(0, 0, 0, "Text")))
        reference = cast(_base.FieldRef[object], quest.field("editor_id"))
        with pytest.raises(pydantic.ValidationError):
            pydantic.TypeAdapter[object](reference._annotation).validate_python(
                42
            )

    def test_game_package_loads_only_requested_record_module(self) -> None:
        """Importing the library or one game does not construct every model."""

        script = (
            "import sys; import bethkit.records.skyrim_se as game; "
            "assert 'bethkit.records.skyrim_se.qust' not in sys.modules; "
            "game.QuestRecord; "
            "assert 'bethkit.records.skyrim_se.qust' in sys.modules; "
            "assert 'bethkit.records.skyrim_se.info' not in sys.modules"
        )
        subprocess.run(
            [sys.executable, "-c", script],
            check=True,
            env={
                **os.environ,
                "PYTHONPATH": str(Path(__file__).resolve().parents[3] / "src"),
            },
        )
