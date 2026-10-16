"""
Copyright (c) Modding Forge
"""

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import (
    Game,
    Plugin,
    PluginPatcher,
    RecordDecodeError,
    SchemaPackage,
    SemanticContext,
    WritableRecord,
)
from bethkit.strings import StringScanDiagnostic

from .test_localization_integration import _schema_path


@pytest.mark.integration
class TestOpaquePreservation:
    """Retains opaque bytes without weakening text validation."""

    def test_source_bytes_survive_extraction_and_unrelated_edit(self) -> None:
        """Retains compressed corrupt NAVM and extended SPGD bytes exactly."""

        # given
        header = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=3))
        )
        text = build_grup(
            b"CLAS",
            0,
            build_record(
                b"CLAS", 0x800, 0, build_subrecord(b"FULL", b"Before\0")
            ),
        )
        opaque = build_grup(
            b"NAVM",
            0,
            build_record(
                b"NAVM",
                0x801,
                0x40000,
                bytes.fromhex("0c000000789c63606060a898c30c2419180108230119"),
            ),
        ) + build_grup(
            b"SPGD",
            0,
            build_record(
                b"SPGD", 0x802, 0, build_subrecord(b"DATA", bytes(range(96)))
            ),
        )
        source = header + text + opaque
        diagnostics: list[StringScanDiagnostic] = []
        with (
            SchemaPackage.open(_schema_path()) as package,
            SemanticContext(package) as context,
            Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin,
        ):
            with pytest.raises(RecordDecodeError):
                list(plugin.iter_strings(context))

            # when
            values = list(
                plugin.iter_strings(
                    context,
                    preserve_opaque_nontext=True,
                    on_diagnostic=diagnostics.append,
                )
            )
            with PluginPatcher(plugin) as patcher:
                assert patcher.write_to_bytes() == source
                with WritableRecord.new("CLAS", form_id=0x800) as changed:
                    changed.add_subrecord("FULL", b"After\0")
                    patcher.replace_record(0x800, changed)
                    output = patcher.write_to_bytes()

            # then
            assert [value.text for value in values] == ["Before"]
            assert [item.record_signature for item in diagnostics] == [
                "NAVM",
                "SPGD",
            ]
            assert [item.form_id for item in diagnostics] == [0x801, 0x802]
            assert all(item.message for item in diagnostics)
            assert output.endswith(opaque)
            assert b"After\0" in output

    def test_text_failure_is_never_retained_as_success(self) -> None:
        """A malformed text-bearing record still aborts opaque-enabled scans."""

        source = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
        ) + build_grup(
            b"CLAS",
            0,
            build_record(b"CLAS", 0x800, 0, build_subrecord(b"DATA", b"\0")),
        )
        with (
            SchemaPackage.open(_schema_path()) as package,
            SemanticContext(package) as context,
            Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin,
        ):
            with pytest.raises(RecordDecodeError):
                list(plugin.iter_strings(context, preserve_opaque_nontext=True))

    def test_preservation_cannot_be_combined_with_skipping(self) -> None:
        """Every retained opaque diagnostic must follow an attempted decode."""

        source = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=0))
        )
        with (
            SchemaPackage.open(_schema_path()) as package,
            SemanticContext(package) as context,
            Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin,
        ):
            with pytest.raises(ValueError, match="full validation"):
                list(
                    plugin.iter_strings(
                        context,
                        validate_nontext=False,
                        preserve_opaque_nontext=True,
                    )
                )
