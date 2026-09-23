"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import struct
from pathlib import Path

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord
from record_native_support import record as fixture_record

from bethkit import Game, Plugin, Record, SemanticContext
from bethkit.plugin import PluginPatcher
from bethkit.records.skyrim_se import MagicEffectRecord
from bethkit.strings import LocalizationEditor

_NAME_PATH: str = "MGEF/2:Name"
_ASSOC_PATH: str = "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item"
_ORIGINAL_NAME: str = "Original effect"
_REPLACEMENT_NAME: str = "A longer replacement effect name"
_UNKNOWN: bytes = b"opaque magic-effect extension"
_ARCHETYPES: tuple[tuple[int, int], ...] = (
    (0, 0),
    (12, 1),
    (17, 2),
    (18, 3),
    (25, 4),
    (34, 8),
    (35, 5),
    (36, 6),
    (39, 7),
    (40, 4),
    (46, 6),
)


def _magic_effect_data(archetype: int) -> bytes:
    """Builds DATA with distinct selector and taper positions, without ESCE.

    Args:
        archetype: Magic-effect archetype at the Skyrim SE DATA offset.

    Returns:
        Complete 152-byte DATA with zero associated item and counter count.
    """

    data = bytearray(152)
    struct.pack_into("<f", data, 56, 0.0)
    struct.pack_into("<I", data, 64, archetype)
    return bytes(data)


def _source_bytes(archetype: int) -> bytes:
    """Builds a synthetic plugin with header metadata and an opaque field.

    Args:
        archetype: Magic-effect archetype used by the associated-item union.

    Returns:
        Plugin bytes whose FULL is the only field intended to change.
    """

    header = build_record(
        b"TES4",
        0,
        0,
        build_subrecord(
            b"HEDR", build_hedr(num_records=2, next_object_id=0x801)
        )
        + build_subrecord(b"CNAM", b"Synthetic fixture author\0")
        + build_subrecord(b"ZZZ1", b"opaque header extension"),
    )
    payload = (
        build_subrecord(b"EDID", b"UnionRegressionEffect\0")
        + build_subrecord(b"FULL", _ORIGINAL_NAME.encode("ascii") + b"\0")
        + build_subrecord(b"DATA", _magic_effect_data(archetype))
        + build_subrecord(b"ZZZZ", _UNKNOWN)
    )
    return header + build_grup(
        b"MGEF", 0, build_record(b"MGEF", 0x800, 0, payload)
    )


def _assert_union(
    record: Record,
    context: SemanticContext,
    archetype: int,
    variant: int,
    name: str,
) -> MagicEffectRecord:
    """Checks both the typed view and the decoder's exact selected variant.

    Args:
        record: Borrowed magic-effect record in an open fixture plugin.
        context: Runtime using the pinned Skyrim SE schema.
        archetype: Expected DATA archetype, not the unrelated taper value.
        variant: Expected associated-item alternative selected by archetype.
        name: Expected inline FULL text.

    Returns:
        Immutable typed record for further public-editor calls.
    """

    snapshot = context.snapshot(record)
    model = MagicEffectRecord.from_snapshot(snapshot)
    assert model.name == name
    assert model.magic_effect_data is not None
    data = model.magic_effect_data.data
    assert data is not None
    assert data.archtype == archetype
    assert data.counter_effect_count == 0
    assert data.assoc_item.raw == 0
    assert record.find_subrecord(b"ESCE") is None
    packed = next(field for field in snapshot.fields if field.name == "Data")
    assert packed.value.kind == "struct"
    associated = next(
        field for field in packed.value.fields if field.path == _ASSOC_PATH
    )
    variant_name = "Unused" if variant == 0 else "Assoc. Item"
    assert associated.effective_path == (
        f"{_ASSOC_PATH}/variants/{variant}:{variant_name}"
    )
    return model


def _assert_round_trip(
    source: bytes,
    patched: bytes,
    context: SemanticContext,
    archetype: int,
    variant: int,
) -> None:
    """Checks the edited name and exact preservation of unrelated bytes.

    Args:
        source: Original plugin with TES4 metadata and an opaque MGEF field.
        patched: Serialized result from a public patching workflow.
        context: Runtime used to decode the reopened plugin.
        archetype: Expected unchanged magic-effect archetype.
        variant: Expected unchanged associated-item union alternative.
    """

    header_end = 24 + struct.unpack_from("<I", source, 4)[0]
    assert patched[:header_end] == source[:header_end]
    with Plugin.from_bytes(patched, Game.SKYRIM_SE) as reopened:
        record = fixture_record(reopened, 0x800)
        _assert_union(record, context, archetype, variant, _REPLACEMENT_NAME)
        data = record.find_subrecord(b"DATA")
        assert data is not None
        assert data.raw_bytes == _magic_effect_data(archetype)
        unknown = record.find_subrecord(b"ZZZZ")
        assert unknown is not None
        assert unknown.raw_bytes == _UNKNOWN


@pytest.mark.integration
@pytest.mark.parametrize(("archetype", "variant"), _ARCHETYPES)
class TestNativeMagicEffectEdits:
    """Exercises FULL edits across every associated-item selector branch."""

    def test_decode_and_validation_accept_original_record(
        self,
        native_schema_context: SemanticContext,
        archetype: int,
        variant: int,
    ) -> None:
        """Distinguishes valid input from the editor's union-context failure.

        Args:
            native_schema_context: Runtime using the pinned schema.
            archetype: Numeric archetype stored in DATA at offset 64.
            variant: Expected union alternative for that archetype.
        """

        # given
        source = _source_bytes(archetype)
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = fixture_record(plugin, 0x800)
            # when
            strict = native_schema_context.validate(record)
            compatible = native_schema_context.validate(
                record, xedit_compatible=True
            )
            # then
            assert not strict.has_errors
            assert not compatible.has_errors
            _assert_union(
                record,
                native_schema_context,
                archetype,
                variant,
                _ORIGINAL_NAME,
            )

    def test_legacy_full_edit_survives_patcher(
        self,
        native_schema_context: SemanticContext,
        archetype: int,
        variant: int,
    ) -> None:
        """Updates a legacy path without reinterpreting unrelated DATA unions.

        Args:
            native_schema_context: Runtime using the pinned schema.
            archetype: Numeric archetype stored in DATA at offset 64.
            variant: Expected union alternative for that archetype.
        """

        # given
        source = _source_bytes(archetype)
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = fixture_record(plugin, 0x800)
            with (
                native_schema_context.edit(record) as editor,
                PluginPatcher(plugin) as patcher,
            ):
                # when
                editor.set(_NAME_PATH, _REPLACEMENT_NAME)
                with editor.finish() as replacement:
                    patcher.replace_record(0x800, replacement)
                patched = patcher.write_to_bytes()
        # then
        _assert_round_trip(
            source, patched, native_schema_context, archetype, variant
        )

    def test_typed_full_edit_survives_patcher(
        self,
        native_schema_context: SemanticContext,
        archetype: int,
        variant: int,
    ) -> None:
        """Updates an exact typed name reference and preserves source metadata.

        Args:
            native_schema_context: Runtime using the pinned schema.
            archetype: Numeric archetype stored in DATA at offset 64.
            variant: Expected union alternative for that archetype.
        """

        # given
        source = _source_bytes(archetype)
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            record = fixture_record(plugin, 0x800)
            model = MagicEffectRecord.from_record(record, native_schema_context)
            with (
                native_schema_context.edit(record) as editor,
                PluginPatcher(plugin) as patcher,
            ):
                # when
                editor.set(model.field("name"), _REPLACEMENT_NAME)
                with editor.finish() as replacement:
                    patcher.replace_record(0x800, replacement)
                patched = patcher.write_to_bytes()
        # then
        _assert_round_trip(
            source, patched, native_schema_context, archetype, variant
        )

    def test_localization_editor_full_edit_survives_bundle(
        self,
        native_schema_context: SemanticContext,
        tmp_path: Path,
        archetype: int,
        variant: int,
    ) -> None:
        """Replaces one StringReference and reloads the resulting plugin bundle.

        Args:
            native_schema_context: Runtime using the pinned schema.
            tmp_path: Isolated output location without installed game files.
            archetype: Numeric archetype stored in DATA at offset 64.
            variant: Expected union alternative for that archetype.
        """

        # given
        source = _source_bytes(archetype)
        with Plugin.from_bytes(source, Game.SKYRIM_SE) as plugin:
            reference = next(
                item
                for item in plugin.iter_strings(native_schema_context)
                if item.address.form_id == 0x800
                and item.address.subrecord_path == _NAME_PATH
            )
            assert reference.text == _ORIGINAL_NAME
            with LocalizationEditor(plugin, native_schema_context) as editor:
                # when
                editor.replace(reference, _REPLACEMENT_NAME)
                bundle = editor.save_bundle(tmp_path / "bundle", "effect.esp")
        # then
        _assert_round_trip(
            source,
            (bundle / "effect.esp").read_bytes(),
            native_schema_context,
            archetype,
            variant,
        )
