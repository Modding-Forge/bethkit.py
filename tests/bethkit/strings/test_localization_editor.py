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

from bethkit import Plugin, StringFileKind, _error
from bethkit.schema import RecordEditor, SemanticContext
from bethkit.strings import (
    LocalizationEditor,
    LocalizationSet,
    references,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


from ._fixtures import snapshot as _snapshot


class TestLocalizationEditor:
    """Verifies isolated edits, rollback, and consistent publication."""

    def test_cleanup_failure_does_not_skip_other_owned_handles(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Attempts every cleanup without retrying a failed destructor."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = True
        context = mocker.create_autospec(SemanticContext, instance=True)
        tables = mocker.create_autospec(LocalizationSet, instance=True)
        working = mocker.create_autospec(LocalizationSet, instance=True)
        tables.clone.return_value = working
        working.close.side_effect = RuntimeError("cleanup failure")
        native_patcher = mocker.MagicMock()
        mocker.patch(
            "bethkit.strings.editor.patcher.PluginPatcher",
            return_value=native_patcher,
        )
        with Plugin._from_native(0x100) as plugin:
            editor = LocalizationEditor(plugin, context, tables)

            # when / then
            with pytest.raises(RuntimeError, match="cleanup failure"):
                editor.close()
            editor.close()

        working.close.assert_called_once()
        native_patcher.close.assert_called_once()
        tables.close.assert_not_called()

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
        with Plugin._from_native(0x100) as plugin:
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
        with Plugin._from_native(0x100) as plugin:
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
        with (
            Plugin._from_native(0x100) as source,
            Plugin._from_native(0x500) as other,
        ):
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
        with Plugin._from_native(0x100) as plugin:
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
        with Plugin._from_native(0x100) as plugin:
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
        with Plugin._from_native(0x100) as plugin:
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
