"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import (
    Game,
    Plugin,
    RecordDecodeError,
    SchemaPackage,
    SemanticContext,
)
from bethkit.strings import StringReference, _batch, references

from .test_localization_integration import _schema_path


def corpus(count: int, *, malformed: bool = False) -> bytes:
    """Builds many classes with an optional invalid UTF-8 final name.

    Args:
        count: Number of source-order class records.
        malformed: Whether the final name must fail strict UTF-8 decoding.

    Returns:
        A plugin with a deliberate batch-boundary crossing.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=count))
    )
    records = b"".join(
        build_record(
            b"CLAS",
            0x800 + index,
            0,
            build_subrecord(
                b"FULL",
                b"bad\xfc\0"
                if malformed and index == count - 1
                else f"Class {index}".encode() + b"\0",
            ),
        )
        for index in range(count)
    )
    return header + build_grup(b"CLAS", 0, records)


@pytest.mark.integration
class TestNativeStringBatch:
    """Compares exact results and error prefixes with the snapshot oracle."""

    def test_nontext_failure_keeps_the_exact_string_prefix(self) -> None:
        """Avoids unused hashes without skipping nontext decoding or errors."""

        # given
        header = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=4))
        )
        first = build_record(
            b"CLAS", 0x800, 0, build_subrecord(b"FULL", b"First\0")
        )
        valid = build_record(
            b"GLOB", 0x801, 0, build_subrecord(b"FLTV", b"\0" * 4)
        )
        broken = build_record(
            b"GLOB", 0x802, 0, build_subrecord(b"FLTV", b"\0")
        )
        last = build_record(
            b"CLAS", 0x803, 0, build_subrecord(b"FULL", b"After\0")
        )
        source = (
            header
            + build_grup(b"CLAS", 0, first)
            + build_grup(b"GLOB", 0, valid + broken)
            + build_grup(b"CLAS", 0, last)
        )
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin,
            SemanticContext(package) as context,
        ):
            # when
            values: list[StringReference] = []
            with pytest.raises(RecordDecodeError):
                values.extend(plugin.iter_strings(context))

            # then
            assert [value.text for value in values] == ["First"]
            assert [
                value.text
                for value in plugin.iter_strings(
                    context, validate_nontext=False
                )
            ] == ["First", "After"]

    def test_nontext_skipping_requires_explicit_opt_in(self) -> None:
        """Skips nontext validation only when extraction-only is requested."""

        header = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
        )
        broken = build_record(
            b"GLOB", 0x800, 0, build_subrecord(b"FLTV", b"\0")
        )
        source = header + build_grup(b"GLOB", 0, broken)
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin,
            SemanticContext(package) as context,
        ):
            with pytest.raises(RecordDecodeError):
                list(plugin.iter_strings(context))
            assert (
                list(plugin.iter_strings(context, validate_nontext=False)) == []
            )

    def test_nested_groups_keep_source_order(self) -> None:
        """Walks nested and subsequent root groups without losing siblings."""

        header = build_record(
            b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=3))
        )
        first = build_record(
            b"CLAS", 0x800, 0, build_subrecord(b"FULL", b"First\0")
        )
        second = build_record(
            b"CLAS", 0x801, 0, build_subrecord(b"FULL", b"Second\0")
        )
        third = build_record(
            b"CLAS", 0x802, 0, build_subrecord(b"FULL", b"Third\0")
        )
        source = (
            header
            + build_grup(b"CLAS", 0, build_grup(b"CLAS", 1, first) + second)
            + build_grup(b"CLAS", 0, third)
        )
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin,
            SemanticContext.for_plugin(package, plugin) as context,
        ):
            assert [v.text for v in plugin.iter_strings(context)] == [
                "First",
                "Second",
                "Third",
            ]

    def test_matches_record_snapshots(self) -> None:
        """Retains every address, codec, identity and string across batches."""

        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(corpus(600), Game.SKYRIM_SE) as plugin,
            SemanticContext.for_plugin(package, plugin) as context,
        ):
            assert _batch.available()
            expected: list[StringReference] = []
            for record in references._iter_records(plugin):
                expected.extend(
                    references._from_snapshot(
                        context.strings_snapshot(record), plugin, None
                    )
                )
            actual = list(plugin.iter_strings(context))
            assert len(actual) == 600
            assert [v.model_dump() for v in actual] == [
                v.model_dump() for v in expected
            ]

    def test_valid_prefix_before_error(self) -> None:
        """Reports malformed records after yielding every preceding string."""

        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(
                corpus(250, malformed=True), Game.SKYRIM_SE
            ) as plugin,
            SemanticContext(package, inline_encoding="utf-8") as context,
        ):
            values: list[StringReference] = []
            with pytest.raises(RecordDecodeError, match="utf-8"):
                values.extend(plugin.iter_strings(context))
            assert len(values) == 249
            assert values[-1].text == "Class 248"

    def test_source_files_are_unchanged(self, tmp_path: Path) -> None:
        """Never writes to the source while walking its strings.

        Args:
            tmp_path: Isolated source directory.
        """

        path = tmp_path / "source.esp"
        original = corpus(4)
        path.write_bytes(original)
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.open(path, Game.SKYRIM_SE) as plugin,
            SemanticContext.for_plugin(package, plugin) as context,
        ):
            assert len(list(plugin.iter_strings(context))) == 4
        assert path.read_bytes() == original
