"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import Game, Plugin, SchemaPackage, SemanticContext
from bethkit.strings import LocalizationEditor

from .test_localization_integration import _schema_path


@pytest.mark.integration
class TestInlineEncodingIntegration:
    """Covers ambiguous bytes and field-scoped codec selection."""

    def test_ambiguous_inline_bytes_accept_explicit_field_codec(
        self, tmp_path: Path
    ) -> None:
        """Uses a field-specific codec when legacy bytes also form UTF-8.

        Args:
            tmp_path: Isolated destination for the edited plugin.
        """

        # given
        header = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
        )
        record = build_record(
            b"CLAS",
            0x800,
            0,
            build_subrecord(b"EDID", b"AmbiguousClass\0")
            + build_subrecord(b"FULL", b"\xc3\xa4\0"),
        )
        original = header + build_grup(b"CLAS", 0, record)
        with (
            SchemaPackage.open(_schema_path()) as package,
            SemanticContext(package, inline_decoding="prefer_utf8") as context,
            Plugin.from_bytes(
                original, Game.SKYRIM_SE, name="ambiguous.esp"
            ) as plugin,
        ):
            reference = next(plugin.iter_strings(context))
            assert reference.text == "ä"
            assert reference.encoding_source == "heuristic"

            # when
            with LocalizationEditor(plugin, context) as editor:
                corrected = editor.select_inline_encoding(reference, "cp1252")
                assert corrected.text == "Ã¤"
                assert corrected.encoding_source == "forced"
                editor.replace(corrected, "Änderung")
                assert next(editor.iter_strings()).text == "Änderung"
                output = editor.save_bundle(
                    tmp_path / "ambiguous", "ambiguous.esp"
                )

            # then
            content = (output / "ambiguous.esp").read_bytes()
            assert b"\xc4nderung\0" in content
            with Plugin.open(
                output / "ambiguous.esp", Game.SKYRIM_SE
            ) as reloaded:
                assert next(reloaded.iter_strings(context)).text == "Änderung"
