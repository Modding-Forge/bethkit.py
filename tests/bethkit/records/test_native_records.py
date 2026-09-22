"""
Copyright (c) Modding Forge

Native integration coverage for generated Skyrim SE records and lossless edits.
"""

from __future__ import annotations

import os
import struct
import zlib
from collections.abc import Iterator
from pathlib import Path

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import (
    Game,
    Plugin,
    Record,
    SchemaPackage,
    SemanticContext,
    UnsupportedEditError,
)
from bethkit.plugin import PluginPatcher
from bethkit.records import FormId
from bethkit.records.skyrim_se import InfoRecord, PerkRecord, QuestRecord
from bethkit.records.skyrim_se.acti import ActivatorRecord, Type176
from bethkit.records.skyrim_se.info import Sex9485
from bethkit.records.skyrim_se.perk import QuestStage5919


def _quest_payload() -> bytes:
    """Builds two stages, each with two independently grouped journal entries.

    Returns:
        Encoded subrecords using the pinned Skyrim SE layout.
    """

    parts = [build_subrecord(b"EDID", b"IntegrationQuest\0")]
    for stage in (10, 20):
        parts.append(build_subrecord(b"INDX", struct.pack("<HBB", stage, 0, 0)))
        for entry in (1, 2):
            parts.append(build_subrecord(b"QSDT", b"\0"))
            text = f"Stage {stage} entry {entry}".encode() + b"\0"
            parts.append(build_subrecord(b"CNAM", text))
    parts.append(build_subrecord(b"ZZZZ", b"opaque quest extension"))
    return b"".join(parts)


def _info_payload() -> bytes:
    """Builds two dialogue responses with distinct text and response numbers.

    Returns:
        Encoded INFO subrecords including their packed response structures.
    """

    parts: list[bytes] = []
    for index in (1, 2):
        data = struct.pack("<III B3x IB3x", 0, 25, 0, index, 0, 0)
        parts.append(build_subrecord(b"TRDT", data))
        parts.append(build_subrecord(b"NAM1", f"Response {index}\0".encode()))
        parts.append(build_subrecord(b"NAM2", f"Notes {index}\0".encode()))
    return b"".join(parts)


def _perk_payload() -> bytes:
    """Builds a quest-stage effect and an ability effect in separate groups.

    Returns:
        Encoded PERK subrecords exercising struct and scalar union alternatives.
    """

    return b"".join(
        (
            build_subrecord(b"EDID", b"IntegrationPerk\0"),
            build_subrecord(b"PRKE", bytes((0, 1, 2))),
            build_subrecord(b"DATA", struct.pack("<IB3x", 0x800, 10)),
            build_subrecord(b"PRKF", b""),
            build_subrecord(b"PRKE", bytes((1, 2, 3))),
            build_subrecord(b"DATA", struct.pack("<I", 0x901)),
            build_subrecord(b"PRKF", b""),
        )
    )


def _source_bytes() -> bytes:
    """Builds a small plugin without requiring copyrighted game data.

    Returns:
        Complete plugin with grouped and untouched compressed records.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=4))
    )
    groups = [
        build_grup(signature, 0, build_record(signature, form_id, 0, payload))
        for signature, form_id, payload in (
            (b"QUST", 0x800, _quest_payload()),
            (b"INFO", 0x801, _info_payload()),
            (b"PERK", 0x802, _perk_payload()),
        )
    ]
    untouched = build_subrecord(b"EDID", b"KeepCompressedBytes\0")
    compressed = struct.pack("<I", len(untouched)) + zlib.compress(
        untouched, level=1
    )
    groups.append(
        build_grup(
            b"MISC", 0, build_record(b"MISC", 0x900, 0x40000, compressed)
        )
    )
    return header + b"".join(groups)


def _record(plugin: Plugin, form_id: int) -> Record:
    """Finds a fixture record and reports a missing fixture as an assertion.

    Args:
        plugin: Open fixture plugin.
        form_id: Expected file-local record identity.

    Returns:
        Borrowed record owned by the supplied plugin.
    """

    record = plugin.find_record(form_id)
    assert record is not None
    return record


def _single_record_source(signature: bytes, payload: bytes) -> bytes:
    """Builds one synthetic record inside a complete Skyrim SE plugin.

    Args:
        signature: Four-byte record signature.
        payload: Concatenated encoded subrecords.

    Returns:
        Complete plugin containing FormID 0x800.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
    )
    return header + build_grup(
        signature, 0, build_record(signature, 0x800, 0, payload)
    )


def _vmad_text(value: str) -> bytes:
    """Encodes a synthetic VMAD length-prefixed string.

    Args:
        value: ASCII fixture text without a trailing terminator.

    Returns:
        Unsigned 16-bit byte length followed by the text bytes.
    """

    encoded = value.encode("ascii")
    return struct.pack("<H", len(encoded)) + encoded


def _vmad_array_payload() -> bytes:
    """Builds string and signed-integer array properties in one VMAD script.

    Returns:
        Version 5 VMAD using object format 2 and two edited properties.
    """

    strings = (
        _vmad_text("Texts")
        + bytes((12, 1))
        + struct.pack("<I", 2)
        + _vmad_text("hello")
        + _vmad_text("world")
    )
    integers = (
        _vmad_text("Numbers") + bytes((13, 1)) + struct.pack("<Iii", 2, -7, 42)
    )
    return (
        struct.pack("<HHH", 5, 2, 1)
        + _vmad_text("IntegrationScript")
        + struct.pack("<BH", 0, 2)
        + strings
        + integers
    )


@pytest.fixture(scope="module")
def native_schema_context() -> Iterator[SemanticContext]:
    """Loads the pinned Skyrim SE schema only for native integration tests.

    Yields:
        Live runtime using the configured or locally built schema.
    """

    configured = os.environ.get("BETHKIT_SCHEMA")
    path = (
        Path(configured)
        if configured
        else Path(__file__).resolve().parents[4]
        / "bethkit"
        / "target"
        / "release-schemas"
        / "skyrim_se.bkschema"
    )
    if not path.is_file():
        if configured:
            pytest.fail(f"BETHKIT_SCHEMA does not name a schema file: {path}")
        pytest.skip(
            "Set BETHKIT_SCHEMA to the pinned Skyrim SE schema package."
        )
    with (
        SchemaPackage.open(path) as package,
        SemanticContext(package) as context,
    ):
        yield context


@pytest.mark.integration
class TestNativeGeneratedRecords:
    """Exercises generated models against real grammar and editing code."""

    def test_vmad_string_and_int_arrays_use_native_union_selection(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Materializes two different array types inside the same script.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        payload = (
            build_subrecord(b"EDID", b"ArrayActivator\0")
            + build_subrecord(b"VMAD", _vmad_array_payload())
            + build_subrecord(b"OBND", bytes(12))
        )
        source = _single_record_source(b"ACTI", payload)
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            # when
            result = ActivatorRecord.from_record(
                _record(plugin, 0x800), native_schema_context
            )

        # then
        assert result.virtual_machine_adapter is not None
        properties = result.virtual_machine_adapter.scripts[0].properties
        assert len(properties) == 2
        assert properties[0].type is Type176.ARRAY_OF_STRING
        assert properties[0].value == ("hello", "world")
        assert properties[1].type is Type176.ARRAY_OF_INT32
        assert properties[1].value == (-7, 42)

    def test_condition_parameter_uses_native_sex_enum_selection(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Keeps the GetIsSex parameter as the generated Sex enum.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        condition = struct.pack("<B3xfH2xIIIII", 0, 1.0, 70, 1, 0, 0, 0, 0)
        source = _single_record_source(
            b"INFO", build_subrecord(b"CTDA", condition)
        )
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            # when
            result = InfoRecord.from_record(
                _record(plugin, 0x800), native_schema_context
            )

        # then
        assert len(result.conditions) == 1
        decoded = result.conditions[0].ctda
        assert decoded is not None
        assert decoded.parameter_1 is Sex9485.FEMALE

    def test_insert_missing_name_survives_patcher_and_reload(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Adds a missing FULL field without losing opaque neighboring bytes.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        source = _single_record_source(
            b"ACTI",
            build_subrecord(b"EDID", b"NamelessActivator\0")
            + build_subrecord(b"OBND", bytes(12))
            + build_subrecord(b"ZZZZ", b"opaque extension"),
        )
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = _record(plugin, 0x800)
            assert record.find_subrecord(b"FULL") is None
            with (
                native_schema_context.edit(record) as editor,
                PluginPatcher(plugin) as patcher,
            ):
                # when
                editor.insert("ACTI/3:Name", "Inserted display name")
                with editor.finish() as replacement:
                    patcher.replace_record(0x800, replacement)
                patched = patcher.write_to_bytes()

        # then
        with Plugin.from_bytes(patched, Game.SKYRIM_SE) as reopened:
            record = _record(reopened, 0x800)
            result = ActivatorRecord.from_record(record, native_schema_context)
            assert result.name == "Inserted display name"
            unknown = record.find_subrecord(b"ZZZZ")
            assert unknown is not None
            assert unknown.raw_bytes == b"opaque extension"

    def test_quest_nested_scopes_survive_source_close(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Keeps independent stage entries in an owned snapshot.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        with Plugin.from_bytes(_source_bytes(), Game.SKYRIM_SE) as plugin:
            # when
            quest = QuestRecord.from_record(
                _record(plugin, 0x800), native_schema_context
            )

        # then
        assert len(quest.stages) == 2
        assert [len(stage.log_entries) for stage in quest.stages] == [2, 2]
        assert [
            entry.log_entry
            for stage in quest.stages
            for entry in stage.log_entries
        ] == [
            "Stage 10 entry 1",
            "Stage 10 entry 2",
            "Stage 20 entry 1",
            "Stage 20 entry 2",
        ]
        first = quest.stages[0].log_entries[0].field("log_entry").address
        second = quest.stages[1].log_entries[0].field("log_entry").address
        assert first is not None and second is not None
        assert [scope.occurrence for scope in first.repeat_scopes] == [0, 0]
        assert [scope.occurrence for scope in second.repeat_scopes] == [1, 0]

    def test_quest_targeted_edit_preserves_untouched_bytes(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Edits exact nested entries and preserves unrelated record bytes.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        source = _source_bytes()
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = _record(plugin, 0x800)
            quest = QuestRecord.from_record(record, native_schema_context)
            with (
                native_schema_context.edit(record) as editor,
                PluginPatcher(plugin) as patcher,
            ):
                # when
                editor.set(
                    quest.stages[1].log_entries[1].field("log_entry"),
                    "Longer text",
                )
                editor.set(
                    quest.stages[0].log_entries[0].field("log_entry"),
                    "First changed",
                )
                with editor.finish() as replacement:
                    patcher.replace_record(0x800, replacement)
                patched = patcher.write_to_bytes()

        # then
        assert (
            source[source.index(b"INFO") :] == patched[patched.index(b"INFO") :]
        )
        with Plugin.from_bytes(patched, Game.SKYRIM_SE) as reopened:
            record = _record(reopened, 0x800)
            updated = QuestRecord.from_record(record, native_schema_context)
            assert [
                entry.log_entry
                for stage in updated.stages
                for entry in stage.log_entries
            ] == [
                "First changed",
                "Stage 10 entry 2",
                "Stage 20 entry 1",
                "Longer text",
            ]
            unknown = record.find_subrecord(b"ZZZZ")
            assert unknown is not None
            assert unknown.raw_bytes == b"opaque quest extension"

    def test_info_response_groups_and_packed_edit(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Targets the second response and its packed response-number member.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        with Plugin.from_bytes(_source_bytes(), Game.SKYRIM_SE) as plugin:
            record = _record(plugin, 0x801)
            info = InfoRecord.from_record(record, native_schema_context)
            assert len(info.responses) == 2
            second = info.responses[1]
            assert second.response_data is not None
            with native_schema_context.edit(record) as editor:
                # when
                editor.set(
                    second.field("response_text"), "A longer second response"
                )
                editor.set(second.response_data.field("response_number"), 7)
                updated = InfoRecord.from_snapshot(editor.snapshot())

        # then
        assert updated.responses[0].response_text == "Response 1"
        assert updated.responses[1].response_text == "A longer second response"
        assert updated.responses[0].response_data is not None
        assert updated.responses[1].response_data is not None
        assert updated.responses[0].response_data.response_number == 1
        assert updated.responses[1].response_data.response_number == 7
        assert updated.responses[1].script_notes == "Notes 2"

    def test_perk_effect_union_selection_and_nested_edit(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Keeps a struct effect distinct from its scalar FormID sibling.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        with Plugin.from_bytes(_source_bytes(), Game.SKYRIM_SE) as plugin:
            record = _record(plugin, 0x802)
            perk = PerkRecord.from_record(record, native_schema_context)
            assert len(perk.effects) == 2
            quest_effect = perk.effects[0].effect_data
            ability_effect = perk.effects[1].effect_data
            assert isinstance(quest_effect, QuestStage5919)
            assert isinstance(ability_effect, FormId)
            assert ability_effect.raw == 0x901
            with (
                native_schema_context.edit(record) as editor,
                PluginPatcher(plugin) as patcher,
            ):
                # when
                editor.set(quest_effect.field("quest_stage"), 20)
                editor.set(
                    perk.effects[1].field("effect_data"), FormId(raw=0x902)
                )
                with editor.finish() as replacement:
                    patcher.replace_record(0x802, replacement)
                patched = patcher.write_to_bytes()

        # then
        with Plugin.from_bytes(patched, Game.SKYRIM_SE) as reopened:
            updated = PerkRecord.from_record(
                _record(reopened, 0x802), native_schema_context
            )
        changed = updated.effects[0].effect_data
        changed_ability = updated.effects[1].effect_data
        assert isinstance(changed, QuestStage5919)
        assert isinstance(changed_ability, FormId)
        assert changed.quest_stage == 20
        assert changed.quest.raw == 0x800
        assert changed_ability.raw == 0x902

    def test_structural_removal_rejects_stale_field_references(
        self, native_schema_context: SemanticContext
    ) -> None:
        """Rejects original addresses after changing the record topology.

        Args:
            native_schema_context: Runtime using the pinned schema.
        """

        # given
        with Plugin.from_bytes(_source_bytes(), Game.SKYRIM_SE) as plugin:
            record = _record(plugin, 0x800)
            quest = QuestRecord.from_record(record, native_schema_context)
            old = quest.stages[1].log_entries[1].field("log_entry")
            with native_schema_context.edit(record) as editor:
                # when
                editor.remove(quest.stages[0].log_entries[0].field("log_entry"))
                # then
                with pytest.raises(UnsupportedEditError):
                    editor.set(old, "Must not be written")
                fresh = QuestRecord.from_snapshot(editor.snapshot())
                editor.set(
                    fresh.stages[1].log_entries[1].field("log_entry"),
                    "Fresh edit",
                )
                updated = QuestRecord.from_snapshot(editor.snapshot())
                assert (
                    updated.stages[1].log_entries[1].log_entry == "Fresh edit"
                )

    def test_noop_patcher_preserves_complete_plugin(self) -> None:
        """Retains every original byte when nothing is edited."""

        # given
        source = _source_bytes()
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            patcher = PluginPatcher(plugin)
        with patcher:
            # when
            patched = patcher.write_to_bytes()
        # then
        assert patched == source
