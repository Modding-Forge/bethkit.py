"""
Copyright (c) Modding Forge
"""

# Checks positional text editing and coordinated output publication.

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import Game, Plugin, StringFileKind, _error
from bethkit.records import _wire
from bethkit.schema import RecordEditor, SemanticContext
from bethkit.strings import (
    LocalizationEditor,
    LocalizationSet,
    references,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def _snapshot(*, localized: bool = False) -> _wire.RecordSnapshot:
    """Builds two same-text fields in different native grammar repetitions.

    Args:
        localized: Whether both fields share the same external string ID.

    Returns:
        A typed native-boundary snapshot with unambiguous field positions.
    """

    fields: list[_wire.WireField] = []
    for index in range(2):
        address = _wire.FieldAddress(
            schema_payload_sha256="schema",
            structure_hash="structure",
            record_signature=(81, 85, 83, 84),
            form_id=0x800,
            subrecord_index=index,
            subrecord_path="QUST/Stages/Stage/Entries/Entry/Log Entry",
            repeat_scopes=(
                _wire.RepeatScope(path="QUST/Stages/Stage", occurrence=index),
                _wire.RepeatScope(
                    path="QUST/Stages/Stage/Entries/Entry", occurrence=0
                ),
            ),
        )
        value = _wire.WireScalar(
            kind="uint" if localized else "string",
            address=address,
            value=17 if localized else "Same text",
            translatable=True,
            string_table="dl_strings" if localized else None,
        )
        fields.append(
            _wire.WireField(
                name="Log Entry",
                node_id=10,
                path=address.subrecord_path,
                span=_wire.ByteSpan(start=0, end=4),
                origin="schema",
                address=address,
                value=value,
            )
        )
    return _wire.RecordSnapshot(
        format_version=1,
        schema_payload_sha256="schema",
        structure_hash="structure",
        record_signature="QUST",
        form_id=0x800,
        fields=tuple(fields),
    )


class TestStringReferences:
    """Covers identity, schema annotations, and lazy text enumeration."""

    def test_equal_text_has_different_position_identity(
        self, mock_lib: MagicMock
    ) -> None:
        """Does not identify repeated quest strings by their text content."""

        # given
        with Plugin(0x100) as plugin:
            # when
            result = list(references._from_snapshot(_snapshot(), plugin, None))

        # then
        assert result[0].text == result[1].text
        assert result[0].identity != result[1].identity
        assert result[0].address.repeat_scopes[0].occurrence == 0
        assert result[1].address.repeat_scopes[0].occurrence == 1

    def test_identity_survives_text_change_and_reload(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps filename plus structural position stable across instances."""

        # given
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0x100
        original = _snapshot()
        first = original.fields[0]
        changed = original.model_copy(
            update={
                "fields": (
                    first.model_copy(
                        update={
                            "value": first.value.model_copy(
                                update={"value": "A longer changed text"}
                            )
                        }
                    ),
                )
            }
        )
        with Plugin.from_bytes(b"", Game.SKYRIM_SE, name="quest.esp") as source:
            before = next(references._from_snapshot(original, source, None))
        with Plugin.from_bytes(b"", Game.SKYRIM_SE, name="quest.esp") as reload:
            # when
            after = next(references._from_snapshot(changed, reload, None))

        # then
        assert before.identity == after.identity
        assert before.text != after.text
        assert before._source_token != after._source_token

    def test_external_reference_without_tables_is_unresolved(
        self, mock_lib: MagicMock
    ) -> None:
        """Retains identity and storage metadata without inventing text."""

        # given
        with Plugin(0x100) as plugin:
            # when
            result = next(
                references._from_snapshot(
                    _snapshot(localized=True), plugin, None
                )
            )

        # then
        assert result.text is None
        assert result.storage == "external"
        assert result.string_id == 17
        assert result.table_kind == StringFileKind.DL_STRINGS

    def test_supplied_tables_must_resolve_referenced_ids(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Raises on incomplete tables instead of silently dropping strings."""

        # given
        tables = mocker.create_autospec(LocalizationSet, instance=True)
        tables.get_str.return_value = None
        with Plugin(0x100) as plugin:
            # when / then
            with pytest.raises(_error.StringTableError, match="absent"):
                list(
                    references._from_snapshot(
                        _snapshot(localized=True), plugin, tables
                    )
                )

    def test_plugin_iteration_is_lazy_and_filters_nontranslatable(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Builds no semantic snapshots until strings are requested."""

        # given
        snapshot = _snapshot()
        field = snapshot.fields[1]
        snapshot = snapshot.model_copy(
            update={
                "fields": (
                    snapshot.fields[0],
                    field.model_copy(
                        update={
                            "value": field.value.model_copy(
                                update={"translatable": False}
                            )
                        }
                    ),
                )
            }
        )
        context = mocker.create_autospec(SemanticContext, instance=True)
        context.strings_snapshot.return_value = snapshot
        mock_lib.bethkit_plugin_is_localized.return_value = False
        mock_lib.bethkit_plugin_group_count.return_value = 1
        mock_lib.bethkit_plugin_group_get.return_value = 0x200
        mock_lib.bethkit_group_child_count.return_value = 1
        mock_lib.bethkit_group_child_is_record.return_value = True
        mock_lib.bethkit_group_child_as_record.return_value = 0x300
        with Plugin(0x100) as plugin:
            iterator = plugin.iter_strings(context)
            context.strings_snapshot.assert_not_called()

            # when
            result = list(iterator)

        # then
        assert len(result) == 1
        context.strings_snapshot.assert_called_once()


class TestLocalizationEditor:
    """Verifies isolated edits, rollback, and consistent publication."""

    def test_external_edit_allocates_copy_on_write_id(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Never overwrites the shared ID referenced by another field."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = True
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        mock_lib.bethkit_plugin_find_record.return_value = 0x300
        context = mocker.create_autospec(SemanticContext, instance=True)
        native_editor = mocker.create_autospec(RecordEditor, instance=True)
        native_editor.strings_snapshot.return_value = _snapshot(localized=True)
        context.edit.return_value = native_editor
        tables = mocker.create_autospec(LocalizationSet, instance=True)
        working = mocker.create_autospec(LocalizationSet, instance=True)
        tables.clone.return_value = working
        working.get_str.return_value = "Same text"
        working.insert_new.return_value = 41
        with Plugin(0x100) as plugin:
            source_refs = list(
                references._from_snapshot(
                    _snapshot(localized=True), plugin, None
                )
            )
            with LocalizationEditor(plugin, context, tables) as editor:
                # when
                editor.replace(source_refs[0], "Changed text")

        # then
        working.insert_new.assert_called_once_with(
            StringFileKind.DL_STRINGS, b"Changed text"
        )
        working.set.assert_not_called()
        tables.set.assert_not_called()
        native_editor._set_json.assert_called_once_with(
            source_refs[0].address, {"kind": "uint", "value": 41}
        )
        tables.close.assert_not_called()
        working.close.assert_called_once()

    def test_failed_semantic_edit_rolls_back_new_id(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Removes only the newly allocated ID after a rejected record edit."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = True
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        mock_lib.bethkit_plugin_find_record.return_value = 0x300
        context = mocker.create_autospec(SemanticContext, instance=True)
        native_editor = mocker.create_autospec(RecordEditor, instance=True)
        native_editor.strings_snapshot.return_value = _snapshot(localized=True)
        native_editor._set_json.side_effect = _error.UnsupportedEditError("bad")
        context.edit.return_value = native_editor
        tables = mocker.create_autospec(LocalizationSet, instance=True)
        working = mocker.create_autospec(LocalizationSet, instance=True)
        tables.clone.return_value = working
        working.get_str.return_value = "Same text"
        working.insert_new.return_value = 41
        with Plugin(0x100) as plugin:
            reference = next(
                references._from_snapshot(
                    _snapshot(localized=True), plugin, None
                )
            )
            with LocalizationEditor(plugin, context, tables) as editor:
                # when / then
                with pytest.raises(_error.UnsupportedEditError, match="bad"):
                    editor.replace(reference, "Rejected text")
        working.remove.assert_called_once_with(StringFileKind.DL_STRINGS, 41)

    def test_foreign_reference_rejected_before_record_lookup(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Rejects another plugin even when record IDs and positions match."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = False
        mock_lib.bethkit_plugin_patcher_new.return_value = 0x200
        context = mocker.create_autospec(SemanticContext, instance=True)
        with Plugin(0x100) as source, Plugin(0x500) as other:
            foreign = next(references._from_snapshot(_snapshot(), other, None))
            with LocalizationEditor(source, context) as editor:
                # when / then
                with pytest.raises(_error.StringTableError, match="different"):
                    editor.replace(foreign, "Rejected text")
        mock_lib.bethkit_plugin_find_record.assert_not_called()
        context.edit.assert_not_called()

    def test_save_bundle_stages_all_outputs_and_preserves_existing_target(
        self,
        mock_lib: MagicMock,
        mocker: MockerFixture,
        tmp_path: Path,
    ) -> None:
        """Publishes all outputs together without replacing existing targets."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = True
        native_patcher = mocker.MagicMock()
        native_patcher.write_to_bytes.return_value = b"plugin"
        mocker.patch(
            "bethkit.strings.editor.patcher.PluginPatcher",
            return_value=native_patcher,
        )
        context = mocker.create_autospec(SemanticContext, instance=True)
        tables = mocker.create_autospec(LocalizationSet, instance=True)
        working = mocker.create_autospec(LocalizationSet, instance=True)
        tables.clone.return_value = working
        working.table_to_bytes.return_value = b"table"
        destination = tmp_path / "bundle"
        with Plugin(0x100) as plugin:
            with LocalizationEditor(plugin, context, tables) as editor:
                # when
                result = editor.save_bundle(destination, "test.esp")

                # then
                assert result == destination
                assert (destination / "test.esp").read_bytes() == b"plugin"
                manifest = json.loads(
                    (destination / "manifest.json").read_text("utf-8")
                )
                assert len(manifest["files"]) == 4
                assert (
                    destination / "Strings" / "test_english.DLSTRINGS"
                ).read_bytes() == b"table"
                with pytest.raises(FileExistsError):
                    editor.save_bundle(destination, "test.esp")
        native_patcher.write_to_bytes.assert_called_once()

    def test_failed_publish_can_retry_without_rewriting_records(
        self,
        mock_lib: MagicMock,
        mocker: MockerFixture,
        tmp_path: Path,
    ) -> None:
        """Leaves no partial output directory after a staging failure."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = False
        native_patcher = mocker.MagicMock()
        native_patcher.write_to_bytes.return_value = b"plugin"
        mocker.patch(
            "bethkit.strings.editor.patcher.PluginPatcher",
            return_value=native_patcher,
        )
        context = mocker.create_autospec(SemanticContext, instance=True)
        failed_rename = mocker.patch.object(
            Path, "rename", side_effect=OSError("simulated publication error")
        )
        destination = tmp_path / "bundle"
        with Plugin(0x100) as plugin:
            with LocalizationEditor(plugin, context) as editor:
                # when
                with pytest.raises(OSError, match="simulated"):
                    editor.save_bundle(destination, "test.esp")
                assert not destination.exists()
                assert list(tmp_path.iterdir()) == []
                mocker.stop(failed_rename)
                editor.save_bundle(destination, "test.esp")

        # then
        assert (destination / "test.esp").read_bytes() == b"plugin"
        native_patcher.write_to_bytes.assert_called_once()

    def test_no_op_text_does_not_rewrite_a_record(
        self,
        mock_lib: MagicMock,
        mocker: MockerFixture,
        tmp_path: Path,
    ) -> None:
        """Preserves original bytes when replacement text is identical."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = False
        mock_lib.bethkit_plugin_find_record.return_value = 0x300
        native_patcher = mocker.MagicMock()
        native_patcher.write_to_bytes.return_value = b"plugin"
        mocker.patch(
            "bethkit.strings.editor.patcher.PluginPatcher",
            return_value=native_patcher,
        )
        context = mocker.create_autospec(SemanticContext, instance=True)
        native_editor = mocker.create_autospec(RecordEditor, instance=True)
        native_editor.strings_snapshot.return_value = _snapshot()
        context.edit.return_value = native_editor
        with Plugin(0x100) as plugin:
            reference = next(
                references._from_snapshot(_snapshot(), plugin, None)
            )
            with LocalizationEditor(plugin, context) as editor:
                # when
                editor.replace(reference, "Same text")
                editor.save_bundle(tmp_path / "bundle", "test.esp")

        # then
        native_editor._set_json.assert_not_called()
        native_editor.finish.assert_not_called()
        native_patcher.replace_record.assert_not_called()
