"""
Copyright (c) Modding Forge
"""

from pathlib import Path

import pytest

from bethkit import Game, LocalizationEditor, Plugin, SemanticContext

from .test_localization_integration import _plugin_bytes


@pytest.mark.integration
class TestExistingBundleIntegration:
    """Checks native text serialization into a pre-existing output folder."""

    def test_existing_output_reloads_with_edited_text(
        self, native_schema_context: SemanticContext, tmp_path: Path
    ) -> None:
        """Retains unrelated files and decodes the replaced plugin correctly."""

        # given
        destination = tmp_path / "bundle"
        destination.mkdir()
        (destination / "unrelated.txt").write_text("keep", encoding="utf-8")
        (destination / "test.esp").write_bytes(b"old output")
        with (
            Plugin.from_bytes(
                _plugin_bytes(localized=False),
                Game.SKYRIM_SE,
                name="test.esp",
            ) as plugin,
            LocalizationEditor(plugin, native_schema_context) as editor,
        ):
            # when
            reference = next(plugin.iter_strings(native_schema_context))
            editor.replace(reference, "Updated name")
            editor.save_bundle(destination, "test.esp", exist_ok=True)

        # then
        with Plugin.open(destination / "test.esp", Game.SKYRIM_SE) as saved:
            assert (
                next(saved.iter_strings(native_schema_context)).text
                == "Updated name"
            )
        assert (destination / "unrelated.txt").read_text("utf-8") == "keep"
