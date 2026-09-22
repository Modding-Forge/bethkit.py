"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from bethkit.records import _wire


def snapshot(*, localized: bool = False) -> _wire.RecordSnapshot:
    """Builds two same-text fields in different native grammar repetitions.

    Args:
        localized: Whether both fields share the same external string ID.

    Returns:
        A typed native-boundary snapshot with unambiguous field positions.
    """

    fields: list[_wire.WireField] = []
    for index in range(2):
        address = _wire.FieldAddress(
            schema_payload_sha256="schema",
            structure_hash="structure",
            record_signature=(81, 85, 83, 84),
            form_id=0x800,
            subrecord_index=index,
            subrecord_path="QUST/Stages/Stage/Entries/Entry/Log Entry",
            repeat_scopes=(
                _wire.RepeatScope(path="QUST/Stages/Stage", occurrence=index),
                _wire.RepeatScope(
                    path="QUST/Stages/Stage/Entries/Entry", occurrence=0
                ),
            ),
        )
        value = _wire.WireScalar(
            kind="uint" if localized else "string",
            address=address,
            value=17 if localized else "Same text",
            translatable=True,
            string_table="dl_strings" if localized else None,
        )
        fields.append(
            _wire.WireField(
                name="Log Entry",
                node_id=10,
                path=address.subrecord_path,
                span=_wire.ByteSpan(start=0, end=4),
                origin="schema",
                address=address,
                value=value,
            )
        )
    return _wire.RecordSnapshot(
        format_version=1,
        schema_payload_sha256="schema",
        structure_hash="structure",
        record_signature="QUST",
        form_id=0x800,
        fields=tuple(fields),
    )
