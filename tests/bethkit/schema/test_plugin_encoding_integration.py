"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import (
    BethkitNativeError,
    Game,
    Plugin,
    SchemaPackage,
    SemanticContext,
)
from bethkit.strings import LocalizationEditor

from ..strings.test_localization_integration import _schema_path


def _plugin(text: bytes, count: int = 8) -> bytes:
    """Builds a class with one translatable string and a technical identifier.

    Args:
        text: Already encoded display-name bytes without a terminator.
        count: Number of class records in the fixture.

    Returns:
        A valid binary plugin with repeated representative text.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=count))
    )
    records = b"".join(
        build_record(
            b"CLAS",
            0x800 + index,
            0,
            build_subrecord(b"EDID", f"Class{index}".encode() + b"\0")
            + build_subrecord(b"FULL", text + b"\0"),
        )
        for index in range(count)
    )
    return header + build_grup(b"CLAS", 0, records)


@pytest.mark.integration
class TestPluginEncodingIntegration:
    """Exercises automatic decisions through the public read and write API."""

    def test_sampling_is_bounded(self) -> None:
        """Stops scanning at the native record and sample-byte limits."""

        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(
                _plugin(b"Short text", 600), Game.SKYRIM_SE
            ) as plugin,
            SemanticContext.for_plugin(package, plugin) as context,
        ):
            decision = context.encoding_decision
            assert decision is not None
            assert decision.scanned_records == 512
            assert decision.sample_strings == 512
            assert decision.sample_bytes <= 65536

    @pytest.mark.parametrize(
        ("codec", "text", "expected"),
        [
            ("utf-8", "Grüße aus der Taverne, öffne die Tür.", "utf8"),
            (
                "cp1252",
                "Grüße aus der Taverne, öffne die Tür.",
                "windows_1252",
            ),
            (
                "cp1251",
                "Найдите древний меч и вернитесь к хозяину таверны.",
                "windows-1251",
            ),
        ],
    )
    def test_detect_read_and_edit(
        self, tmp_path: Path, codec: str, text: str, expected: str
    ) -> None:
        """Detects one plugin codec and preserves it while editing.

        Args:
            tmp_path: Isolated output directory.
            codec: Known fixture encoding.
            text: Known source Unicode string.
            expected: Canonical native codec name.
        """

        # given
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(
                _plugin(text.encode(codec)), Game.SKYRIM_SE, name="test.esp"
            ) as plugin,
            SemanticContext.for_plugin(package, plugin) as context,
        ):
            decision = context.encoding_decision
            assert decision is not None
            assert decision.encoding == expected
            assert decision.source == "detector"
            assert decision.sample_strings == 8
            assert decision.sample_bytes == 8 * (len(text.encode(codec)) + 1)
            reference = next(plugin.iter_strings(context))
            assert reference.text == text

            # when
            replacement = f"{text} [edited]"
            with LocalizationEditor(plugin, context) as editor:
                editor.replace(reference, replacement)
                output = editor.save_bundle(tmp_path / "output", "test.esp")

            # then
            assert (
                replacement.encode(codec) + b"\0"
                in (output / "test.esp").read_bytes()
            )
            with Plugin.open(output / "test.esp", Game.SKYRIM_SE) as reloaded:
                with SemanticContext.for_plugin(package, reloaded) as reread:
                    assert (
                        next(reloaded.iter_strings(reread)).text == replacement
                    )

    def test_override_wins_and_bad_override_fails(self, tmp_path: Path) -> None:
        """Honors an override even when UTF-8 detection would disagree.

        Args:
            tmp_path: Isolated override-file directory.
        """

        # given
        path = tmp_path / "test.cpoverride"
        path.write_text("1252\n", encoding="utf-8")
        original = "Grüße aus der Taverne".encode()
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(_plugin(original), Game.SKYRIM_SE) as plugin,
        ):
            # when
            with SemanticContext.for_plugin(
                package, plugin, cpoverride=path
            ) as context:
                decision = context.encoding_decision
                assert decision is not None
                assert decision.source == "cpoverride"
                assert decision.sample_bytes == decision.scanned_records == 0
                assert next(
                    plugin.iter_strings(context)
                ).text == original.decode("cp1252")

            # then
            path.write_text("unknown", encoding="utf-8")
            with pytest.raises(BethkitNativeError):
                SemanticContext.for_plugin(package, plugin, cpoverride=path)
            with pytest.raises(BethkitNativeError):
                SemanticContext.for_plugin(
                    package, plugin, cpoverride=tmp_path / "missing.cpoverride"
                )

    def test_ascii_and_foreign_plugin(self) -> None:
        """Reports insufficient ASCII evidence and rejects another instance."""

        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(_plugin(b"Plain text"), Game.SKYRIM_SE) as plugin,
            Plugin.from_bytes(_plugin(b"Other text"), Game.SKYRIM_SE) as other,
            SemanticContext.for_plugin(package, plugin) as context,
        ):
            decision = context.encoding_decision
            assert decision is not None
            assert decision.source == "ascii"
            assert next(plugin.iter_strings(context)).text == "Plain text"
            with pytest.raises(ValueError, match="another plugin"):
                next(other.iter_strings(context))
