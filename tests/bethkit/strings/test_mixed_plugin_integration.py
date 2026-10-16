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


def mixed_effect(description: bytes) -> bytes:
    """Builds one effect with UTF-8 name and independently encoded description.

    Args:
        description: Already encoded description without its terminator.

    Returns:
        Minimal plugin containing both inline strings in the same record.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
    )
    effect = build_record(
        b"MGEF",
        0x800,
        0,
        build_subrecord(b"FULL", "Grüße".encode() + b"\0")
        + build_subrecord(b"DNAM", description + b"\0"),
    )
    return header + build_grup(b"MGEF", 0, effect)


@pytest.mark.integration
class TestNativeMixedPlugin:
    """Keeps independently encoded siblings and explicit override precedence."""

    def test_repeated_buttons_keep_distinct_codecs(
        self, tmp_path: Path
    ) -> None:
        """Edits a UTF-8 button without re-encoding its repeated legacy sibling.

        Args:
            tmp_path: Isolated output bundle directory.
        """

        header = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
        )
        message = build_record(
            b"MESG",
            0x800,
            0,
            build_subrecord(b"FULL", b"Menu\0")
            + build_subrecord(b"DNAM", b"\x01\0\0\0")
            + build_subrecord(b"ITXT", "Öffnen".encode() + b"\0")
            + build_subrecord(b"ITXT", b"Schlie\xdfen\0"),
        )
        original = header + build_grup(b"MESG", 0, message)
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(original, Game.SKYRIM_SE) as plugin,
            SemanticContext.for_plugin(package, plugin, mixed=True) as context,
        ):
            values = list(plugin.iter_strings(context))
            assert [v.text for v in values] == ["Menu", "Öffnen", "Schließen"]
            assert (
                values[1].identity.repeat_scopes
                != values[2].identity.repeat_scopes
            )
            with LocalizationEditor(plugin, context) as editor:
                editor.replace(values[1], "Öffnen geändert")
                output = editor.save_bundle(tmp_path / "output", "buttons.esp")
            written = (output / "buttons.esp").read_bytes()
            assert b"Schlie\xdfen\0" in written
            assert "Öffnen geändert".encode() + b"\0" in written

    @pytest.mark.parametrize(
        ("codec", "description"),
        [
            ("cp1252", "Öffne die Tür und grüße den Händler."),
            (
                "cp1251",
                "Найдите древний меч и вернитесь к хозяину таверны. " * 20,
            ),
        ],
    )
    def test_edit_preserves_sibling_bytes(
        self, tmp_path: Path, codec: str, description: str
    ) -> None:
        """Preserves the unedited sibling and retains the edited field codec.

        Args:
            tmp_path: Isolated output directory.
            codec: Known legacy codec in this fixture.
            description: Known source Unicode text.
        """

        encoded = description.encode(codec)
        original = mixed_effect(encoded)
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(original, Game.SKYRIM_SE) as plugin,
            SemanticContext.for_plugin(package, plugin, mixed=True) as context,
        ):
            values = list(plugin.iter_strings(context))
            assert [value.text for value in values] == ["Grüße", description]
            assert values[0].encoding == "utf8"
            replacement = description + " [edited]"
            with LocalizationEditor(plugin, context) as editor:
                editor.replace(values[1], replacement)
                output = editor.save_bundle(tmp_path / "output", "mixed.esp")
            written = (output / "mixed.esp").read_bytes()
            assert "Grüße".encode() + b"\0" in written
            assert replacement.encode(codec) + b"\0" in written
            with (
                Plugin.open(output / "mixed.esp", Game.SKYRIM_SE) as reloaded,
                SemanticContext.for_plugin(
                    package, reloaded, mixed=True
                ) as reread,
            ):
                assert [v.text for v in reloaded.iter_strings(reread)] == [
                    "Grüße",
                    replacement,
                ]

    def test_override_disables_heuristic(self, tmp_path: Path) -> None:
        """Never overrides the user's explicit codepage with UTF-8 preference.

        Args:
            tmp_path: Isolated override directory.
        """

        override = tmp_path / "mixed.cpoverride"
        override.write_text("1252", encoding="utf-8")
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(
                mixed_effect(b"T\xfcr"), Game.SKYRIM_SE
            ) as plugin,
            SemanticContext.for_plugin(
                package, plugin, cpoverride=override, mixed=True
            ) as context,
        ):
            decision = context.encoding_decision
            assert decision is not None
            assert decision.source == "cpoverride"
            values = list(plugin.iter_strings(context))
            assert values[0].text == "Grüße".encode().decode("cp1252")
            assert values[1].text == "Tür"
