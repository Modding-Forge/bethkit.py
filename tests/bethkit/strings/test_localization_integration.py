"""
Copyright (c) Modding Forge
"""

# Native end-to-end text editing with the pinned Skyrim SE schema.

from __future__ import annotations

import os
import struct
from collections.abc import Iterator
from pathlib import Path

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import (
    BethkitNativeError,
    Game,
    Plugin,
    SchemaPackage,
    SemanticContext,
    StringFileKind,
)
from bethkit.strings import LocalizationEditor, LocalizationSet, StringTable


@pytest.fixture(scope="module")
def native_context() -> Iterator[SemanticContext]:
    """Loads an explicit schema or the sibling workspace's pinned test schema.

    Yields:
        A real native semantic context for this test module.

    Raises:
        AssertionError: Native integration was requested without its schema.
    """

    default = (
        Path(__file__).resolve().parents[4]
        / "bethkit"
        / "target"
        / "release-schemas"
        / "skyrim_se.bkschema"
    )
    path = Path(os.environ.get("BETHKIT_SCHEMA", str(default)))
    assert path.is_file(), "Set BETHKIT_SCHEMA to the tested Skyrim SE schema."
    with SchemaPackage.open(path) as package:
        with SemanticContext(package) as context:
            yield context


def _plugin_bytes(*, localized: bool) -> bytes:
    """Builds two simple activators whose display names initially match.

    Args:
        localized: Whether both names reference the same external string ID.

    Returns:
        A synthetic Skyrim SE plugin with two independently editable names.
    """

    header = build_record(
        b"TES4",
        0,
        0x80 if localized else 0,
        build_subrecord(b"HEDR", build_hedr(num_records=2)),
    )
    payload = struct.pack("<I", 17) if localized else b"Same text\0"
    records = b"".join(
        build_record(
            b"ACTI",
            0x800 + index,
            0,
            build_subrecord(b"EDID", f"Activator{index}\0".encode("ascii"))
            + build_subrecord(b"OBND", bytes(12))
            + build_subrecord(b"FULL", payload),
        )
        for index in range(2)
    )
    return header + build_grup(b"ACTI", 0, records)


@pytest.mark.integration
class TestNativeLocalization:
    """Exercises the compiled schema, editor, patcher, and string writers."""

    def test_partial_language_pack_uses_strings_subdirectory(
        self, tmp_path: Path
    ) -> None:
        """Opens a partial language pack and leaves absent formats empty."""

        # given
        directory = tmp_path / "Strings"
        directory.mkdir()
        with StringTable.new(StringFileKind.STRINGS) as table:
            table.insert(17, b"Partial pack")
            table.write_to_file(directory / "test_english.STRINGS")

        # when / then
        with LocalizationSet.open(tmp_path / "test.esp", "english") as tables:
            assert tables.get_str(StringFileKind.STRINGS, 17) == "Partial pack"
            assert tables.get(StringFileKind.DL_STRINGS, 17) is None
            assert tables.get(StringFileKind.IL_STRINGS, 17) is None

    def test_existing_malformed_table_is_not_treated_as_missing(
        self, tmp_path: Path
    ) -> None:
        """Distinguishes an absent language file from corrupt existing data."""

        # given
        directory = tmp_path / "Strings"
        directory.mkdir()
        (directory / "test_english.STRINGS").write_bytes(b"invalid")

        # when / then
        with pytest.raises(BethkitNativeError):
            LocalizationSet.open(tmp_path / "test.esp", "english")

    def test_write_creates_all_three_strings_files(
        self, tmp_path: Path
    ) -> None:
        """Writes the documented layout, including initially empty tables."""

        # given
        with LocalizationSet.new() as tables:
            tables.set(StringFileKind.STRINGS, 17, b"Written pack")

            # when
            tables.write(tmp_path / "test.esp", "english")

        # then
        expected = {"STRINGS", "DLSTRINGS", "ILSTRINGS"}
        assert {
            path.suffix[1:] for path in (tmp_path / "Strings").iterdir()
        } == expected
        with LocalizationSet.open(tmp_path / "test.esp", "english") as tables:
            assert tables.get_str(StringFileKind.STRINGS, 17) == "Written pack"

    def test_inline_text_edit_keeps_identity_across_length_changes(
        self, native_context: SemanticContext, tmp_path: Path
    ) -> None:
        """Edits long text twice and keeps independent positional identities."""

        # given
        original = _plugin_bytes(localized=False)
        with Plugin.from_bytes(
            original, Game.SKYRIM_SE, name="test.esp"
        ) as plugin:
            before = list(plugin.iter_strings(native_context))
            assert len(before) == 2
            with LocalizationEditor(plugin, native_context) as editor:
                # when
                editor.replace(before[0], "A much longer display name")
                after_first = list(editor.iter_strings())
                editor.replace(before[0], "Short")
                editor.replace(before[1], "Second display name")
                output = editor.save_bundle(tmp_path / "inline", "test.esp")

            # then
            assert (
                list(plugin.iter_strings(native_context))[0].text == "Same text"
            )
            assert after_first[0].identity == before[0].identity
            assert after_first[0].address == before[0].address
        with Plugin.open(output / "test.esp", Game.SKYRIM_SE) as reloaded:
            result = list(reloaded.iter_strings(native_context))
            assert [reference.text for reference in result] == [
                "Short",
                "Second display name",
            ]
            assert result[0].identity == before[0].identity

    def test_shared_external_id_is_copied_and_saved_with_plugin(
        self, native_context: SemanticContext, tmp_path: Path
    ) -> None:
        """Changes one shared-ID user and preserves the original tables."""

        # given
        original = _plugin_bytes(localized=True)
        with LocalizationSet.new() as tables:
            tables.set(StringFileKind.STRINGS, 17, b"Same text")
            with Plugin.from_bytes(
                original, Game.SKYRIM_SE, name="test.esp"
            ) as plugin:
                before = list(plugin.iter_strings(native_context, tables))
                assert len(before) == 2
                assert before[0].string_id == before[1].string_id == 17
                with LocalizationEditor(
                    plugin, native_context, tables
                ) as editor:
                    # when
                    editor.replace(before[0], "Changed external name")
                    current = list(editor.iter_strings())
                    output = editor.save_bundle(
                        tmp_path / "external", "test.esp"
                    )

                # then
                assert current[0].string_id != 17
                assert current[1].string_id == 17
                assert current[0].identity == before[0].identity
                assert tables.get_str(StringFileKind.STRINGS, 17) == "Same text"
                assert before[0].string_id == 17
            with Plugin.open(output / "test.esp", Game.SKYRIM_SE) as reloaded:
                with LocalizationSet.open(
                    output / "test.esp", "english"
                ) as saved:
                    result = list(reloaded.iter_strings(native_context, saved))
                    assert [reference.text for reference in result] == [
                        "Changed external name",
                        "Same text",
                    ]
                    assert result[0].identity == before[0].identity

    @pytest.mark.parametrize("kind", list(StringFileKind))
    def test_table_clone_insert_remove_and_bytes(
        self, kind: StringFileKind, tmp_path: Path
    ) -> None:
        """Round-trips every external table format through checked APIs."""

        # given
        extensions = {
            StringFileKind.STRINGS: "STRINGS",
            StringFileKind.DL_STRINGS: "DLSTRINGS",
            StringFileKind.IL_STRINGS: "ILSTRINGS",
        }
        with LocalizationSet.new() as original:
            original.set(kind, 17, b"Original")
            with original.clone() as working:
                # when
                assigned = working.insert_new(kind, b"New text")
                assert assigned != 17
                assert not working.remove(kind, 999)
                assert working.remove(kind, 17)
                encoded = working.table_to_bytes(kind)

            # then
            assert original.get_str(kind, 17) == "Original"
        path = tmp_path / f"test_english.{extensions[kind]}"
        path.write_bytes(encoded)
        with StringTable.open(path) as table:
            assert table.get_str(17) is None
            assert table.get_str(assigned) == "New text"
