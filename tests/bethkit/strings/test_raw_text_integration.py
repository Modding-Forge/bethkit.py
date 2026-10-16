"""
Copyright (c) Modding Forge
"""

from pathlib import Path

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import (
    Game,
    Plugin,
    PluginPatcher,
    SchemaPackage,
    SemanticContext,
    UnsupportedEditError,
)
from bethkit.strings import LocalizationEditor, StringReference

from .test_localization_integration import _schema_path


def source_bytes(body: bytes) -> bytes:
    """Build a source with valid text and one suspect description.

    Args:
        body: Exact original DNAM text body.

    Returns:
        Source bytes with an ordinary FULL and byte-preserved DNAM.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
    )
    effect = build_record(
        b"MGEF",
        0x800,
        0,
        build_subrecord(b"FULL", b"Safe name\0")
        + build_subrecord(b"DNAM", body + b"\0"),
    )
    return header + build_grup(b"MGEF", 0, effect)


@pytest.mark.integration
class TestRawTextPreservation:
    """Warn without inventing text, mutating bytes or permitting blind edits."""

    def test_raw_warning_roundtrip_and_unrelated_edit(
        self, tmp_path: Path
    ) -> None:
        """Retains damaged bytes through JSON and actual bundle writing.

        Args:
            tmp_path: Isolated output folder, never a real mod location.
        """

        # given
        body = b"\xec\xb2\xb4\xeb\xa0\xa5\xea\xb3? <mag>"
        original = source_bytes(body)
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(original, Game.SKYRIM_SE) as plugin,
            SemanticContext.for_plugin(
                package, plugin, preserve_undecodable=True
            ) as context,
        ):
            values = list(plugin.iter_strings(context))
            raw = next(value for value in values if value.raw_bytes is not None)
            assert raw.text is None
            assert raw.encoding is None
            assert raw.decoding_warning
            assert raw.raw_bytes == body
            assert (
                StringReference.model_validate_json(
                    raw.model_dump_json()
                ).raw_bytes
                == body
            )
            assert (
                StringReference.model_validate(raw.model_dump()).raw_bytes
                == body
            )
            with PluginPatcher(plugin) as patcher:
                assert patcher.write_to_bytes() == original

            # when
            with LocalizationEditor(plugin, context) as editor:
                with pytest.raises(UnsupportedEditError, match="codec"):
                    editor.replace(raw, "Must not overwrite bytes")
                safe = next(
                    value for value in values if value.text == "Safe name"
                )
                editor.replace(safe, "Changed name")
                editor.save_bundle(tmp_path / "bundle", "test.esp")

            # then
            with Plugin.open(
                tmp_path / "bundle/test.esp", Game.SKYRIM_SE
            ) as result:
                record = result.find_record(0x800)
                assert record is not None
                assert record.subrecord_at(1).raw_bytes == body + b"\0"
                assert record.subrecord_at(0).raw_bytes == b"Changed name\0"

    def test_authoritative_override_wins(self, tmp_path: Path) -> None:
        """Uses the selected codec rather than diagnosing a different guess.

        Args:
            tmp_path: Isolated override file folder.
        """

        override = tmp_path / "test.cpoverride"
        override.write_text("1252", encoding="utf-8")
        body = b"\xec\xb2\xb4\xeb\xa0\xa5\xea\xb3?"
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(source_bytes(body), Game.SKYRIM_SE) as plugin,
            SemanticContext.for_plugin(
                package,
                plugin,
                cpoverride=override,
                preserve_undecodable=True,
            ) as context,
        ):
            values = list(plugin.iter_strings(context))
            assert all(value.raw_bytes is None for value in values)
            assert values[1].text == body.decode("cp1252")
            assert context.encoding_decision is not None
            assert context.encoding_decision.source == "cpoverride"

    def test_explicit_field_selection_resolves_raw_text(self) -> None:
        """An explicit field codec permits a deliberate edit."""

        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(
                source_bytes(b"Uncertain\x81"), Game.SKYRIM_SE
            ) as plugin,
            SemanticContext.for_plugin(
                package, plugin, preserve_undecodable=True
            ) as context,
            LocalizationEditor(plugin, context) as editor,
        ):
            raw = list(plugin.iter_strings(context))[1]
            assert raw.raw_bytes is not None
            selected = editor.select_inline_encoding(raw, "cp1252")
            assert selected.raw_bytes is None
            assert selected.text == "Uncertain\x81"
            editor.replace(selected, "Deliberate replacement")

    def test_invalid_explicit_utf8_is_preserved(self, tmp_path: Path) -> None:
        """An authoritative codec failure produces raw text without guessing.

        Args:
            tmp_path: Isolated override file folder.
        """

        override = tmp_path / "test.cpoverride"
        override.write_text("utf8", encoding="utf-8")
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(
                source_bytes(b"Broken\xff"), Game.SKYRIM_SE
            ) as plugin,
            SemanticContext.for_plugin(
                package,
                plugin,
                cpoverride=override,
                preserve_undecodable=True,
            ) as context,
        ):
            raw = list(plugin.iter_strings(context))[1]
            assert raw.raw_bytes == b"Broken\xff"
            assert raw.text is None
            assert raw.best_effort_encoding == "UTF-8"
            assert raw.best_effort_text == "Broken\\xff"
