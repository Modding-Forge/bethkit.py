"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from bethkit import Game, Plugin, SchemaPackage, SemanticContext
from bethkit.strings import LocalizationEditor, StringReference

from .test_localization_integration import _schema_path


@pytest.mark.integration
class TestUssepMixedLive:
    """Checks real overrides without embedding third-party assets."""

    def test_info_and_quest_inline_edits_round_trip(
        self, tmp_path: Path
    ) -> None:
        """Edits UTF-8 INFO and QUST fields in a copied USSEP plugin.

        Args:
            tmp_path: Isolated output directory for the patched plugin.
        """

        configured = os.environ.get("BETHKIT_USSEP_ESP")
        if configured is None:
            pytest.skip("Set BETHKIT_USSEP_ESP for the live corpus test.")
        source = Path(configured)
        if not source.is_file():
            pytest.fail(f"BETHKIT_USSEP_ESP is not a file: {source}")

        # given
        with (
            SchemaPackage.open(_schema_path()) as package,
            SemanticContext(package, inline_decoding="prefer_utf8") as context,
            Plugin.open(source, Game.SKYRIM_SE) as plugin,
        ):
            selected: dict[tuple[int, ...], StringReference] = {}
            signatures = {tuple(b"INFO"), tuple(b"QUST")}
            for reference in plugin.iter_strings(context):
                signature = reference.identity.record_signature
                if (
                    signature in signatures
                    and reference.encoding_source == "heuristic"
                    and reference.text
                ):
                    selected.setdefault(signature, reference)
                if len(selected) == len(signatures):
                    break
            assert set(selected) == signatures

            # when
            with LocalizationEditor(plugin, context) as editor:
                replacements: dict[tuple[int, ...], str] = {}
                for signature, reference in selected.items():
                    replacement = f"{reference.text} [Bethkit test]"
                    editor.replace(reference, replacement)
                    replacements[signature] = replacement
                output = editor.save_bundle(tmp_path / "edited", source.name)

            # then
            identities = {item.identity for item in selected.values()}
            with Plugin.open(output / source.name, Game.SKYRIM_SE) as reloaded:
                found = {
                    reference.identity.record_signature: reference.text
                    for reference in reloaded.iter_strings(context)
                    if reference.identity in identities
                }
                assert found == replacements
