"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import Plugin, SemanticContext, StringFileKind
from bethkit.strings import LocalizationEditor, _bundle

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestExistingBundle:
    """Checks opt-in bundle merging without removing unrelated files."""

    def test_editor_allows_existing_directory(
        self, mock_lib: MagicMock, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Forwards the opt-in flag and retains existing unrelated content."""

        # given
        mock_lib.bethkit_plugin_is_localized.return_value = False
        native_patcher = mocker.MagicMock()
        native_patcher.write_to_bytes.return_value = b"plugin"
        mocker.patch(
            "bethkit.strings.editor.patcher.PluginPatcher",
            return_value=native_patcher,
        )
        context = mocker.create_autospec(SemanticContext, instance=True)
        destination = tmp_path / "bundle"
        destination.mkdir()
        (destination / "other.esp").write_bytes(b"keep")
        (destination / "test.esp").write_bytes(b"old")

        # when
        with (
            Plugin._from_native(0x100) as plugin,
            LocalizationEditor(plugin, context) as editor,
        ):
            with pytest.raises(FileExistsError):
                editor.save_bundle(destination, "test.esp")
            result = editor.save_bundle(destination, "test.esp", exist_ok=True)

        # then
        assert result == destination
        assert (destination / "test.esp").read_bytes() == b"plugin"
        assert (destination / "other.esp").read_bytes() == b"keep"
        native_patcher.write_to_bytes.assert_called_once()

    def test_merge_replaces_only_generated_tables(self, tmp_path: Path) -> None:
        """Preserves other plugins, tables and folders in the destination."""

        # given
        destination = tmp_path / "bundle"
        tables = destination / "Strings"
        tables.mkdir(parents=True)
        (tables / "other_english.STRINGS").write_bytes(b"other")
        (tables / "test_english.STRINGS").write_bytes(b"old")

        # when
        _bundle.publish(
            destination,
            "test.esp",
            "english",
            b"plugin",
            {StringFileKind.STRINGS: b"new"},
            None,
            exist_ok=True,
        )

        # then
        assert (tables / "test_english.STRINGS").read_bytes() == b"new"
        assert (tables / "other_english.STRINGS").read_bytes() == b"other"
        manifest = json.loads((destination / "manifest.json").read_text())
        assert {file["path"] for file in manifest["files"]} == {
            "test.esp",
            "Strings/test_english.STRINGS",
        }

    @pytest.mark.parametrize("conflict", ["destination", "Strings", "test.esp"])
    def test_conflicts_leave_existing_outputs_unchanged(
        self, tmp_path: Path, conflict: str
    ) -> None:
        """Preflights file/directory conflicts before replacing any output."""

        # given
        destination = tmp_path / "bundle"
        if conflict == "destination":
            destination.write_bytes(b"keep")
        else:
            destination.mkdir()
            if conflict == "test.esp":
                (destination / conflict).mkdir()
            else:
                (destination / conflict).write_bytes(b"keep")
                (destination / "test.esp").write_bytes(b"old")

        # when / then
        with pytest.raises(OSError):
            _bundle.publish(
                destination,
                "test.esp",
                "english",
                b"plugin",
                {StringFileKind.STRINGS: b"table"},
                None,
                exist_ok=True,
            )
        if conflict == "destination":
            assert destination.read_bytes() == b"keep"
        elif conflict == "Strings":
            assert (destination / "test.esp").read_bytes() == b"old"
            assert (destination / "Strings").read_bytes() == b"keep"
        else:
            assert (destination / "test.esp").is_dir()
        assert not list(tmp_path.glob(".bundle-*"))

    def test_new_directory_still_supported(self, tmp_path: Path) -> None:
        """Publishes a new directory when no target exists."""

        destination = tmp_path / "bundle"
        assert (
            _bundle.publish(
                destination,
                "test.esp",
                "english",
                b"plugin",
                {},
                None,
                exist_ok=True,
            )
            == destination
        )
        assert (destination / "test.esp").read_bytes() == b"plugin"

    @pytest.mark.parametrize("linked", ["bundle", "Strings", "test.esp"])
    def test_linked_targets_are_rejected(
        self, tmp_path: Path, mocker: MockerFixture, linked: str
    ) -> None:
        """Rejects symlink paths, including dangling table-directory links."""

        destination = tmp_path / "bundle"
        destination.mkdir()
        unsafe = destination if linked == "bundle" else destination / linked
        original = Path.is_symlink

        def is_link(path: Path) -> bool:
            """Marks the chosen unsafe path as a symbolic link."""

            return path == unsafe or original(path)

        mocker.patch.object(
            Path,
            "is_symlink",
            autospec=True,
            side_effect=is_link,
        )
        with pytest.raises(OSError):
            _bundle.publish(
                destination,
                "test.esp",
                "english",
                b"plugin",
                {StringFileKind.STRINGS: b"table"},
                None,
                exist_ok=True,
            )
        assert list(destination.iterdir()) == []
