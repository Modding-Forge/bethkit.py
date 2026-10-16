"""
Copyright (c) Modding Forge
"""

import pytest
from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import (
    Game,
    Plugin,
    RecordDecodeError,
    SchemaPackage,
    SemanticContext,
)
from bethkit.strings import references

from .test_localization_integration import _schema_path


def source(payload: bytes) -> bytes:
    """Build an isolated reference whose record type supports strings.

    Args:
        payload: Exact subrecords of the reference.

    Returns:
        A synthetic SSE plugin, unrelated to any installed mod.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
    )
    return header + build_grup(
        b"REFR", 0, build_record(b"REFR", 0x800, 0, payload)
    )


@pytest.mark.integration
class TestEmptyStringProjection:
    """Keep full decoding when only the string projection is provably empty."""

    @pytest.mark.parametrize("length", [0, 1, 3, 23, 25])
    @pytest.mark.parametrize("validate_nontext", [False, True])
    def test_text_capable_record_errors_remain_strict(
        self, length: int, validate_nontext: bool
    ) -> None:
        """Never turn a missing string tag into opaque error recovery.

        Args:
            length: Invalid position/rotation payload length.
            validate_nontext: Explicit record-type skipping policy.
        """

        # given
        data = source(build_subrecord(b"DATA", bytes(length)))
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(data, Game.SKYRIM_SE) as plugin,
            SemanticContext(package) as context,
        ):
            record = plugin.find_record(0x800)
            assert record is not None
            with pytest.raises(RecordDecodeError) as ordinary:
                context.strings_snapshot(record)

            # when
            with pytest.raises(RecordDecodeError) as optimized:
                list(
                    plugin.iter_strings(
                        context,
                        validate_nontext=validate_nontext,
                        preserve_opaque_nontext=validate_nontext,
                    )
                )

            # then
            assert str(optimized.value) == str(ordinary.value)

    @pytest.mark.parametrize("include_text", [False, True])
    def test_present_strings_keep_exact_snapshot_addresses(
        self, include_text: bool
    ) -> None:
        """Compare both empty and text-bearing records with the snapshot oracle.

        Args:
            include_text: Whether the concrete record contains its name tag.
        """

        # given
        payload = build_subrecord(b"DATA", bytes(24))
        if include_text:
            payload = build_subrecord(b"FULL", b"Reference name\0") + payload
        with (
            SchemaPackage.open(_schema_path()) as package,
            Plugin.from_bytes(source(payload), Game.SKYRIM_SE) as plugin,
            SemanticContext(package) as context,
        ):
            record = plugin.find_record(0x800)
            assert record is not None
            snapshot = context.strings_snapshot(record)
            expected = list(references._from_snapshot(snapshot, plugin, None))

            # when
            actual = list(plugin.iter_strings(context))

            # then
            assert len(actual) == int(include_text)
            assert [value.model_dump() for value in actual] == [
                value.model_dump() for value in expected
            ]
