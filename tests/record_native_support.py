"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import struct
import zlib

from conftest import build_grup, build_hedr, build_record, build_subrecord

from bethkit import Plugin, Record


def _quest_payload() -> bytes:
    """Builds two stages, each with two independently grouped journal entries.

    Returns:
        Encoded subrecords using the pinned Skyrim SE layout.
    """

    parts = [build_subrecord(b"EDID", b"IntegrationQuest\0")]
    for stage in (10, 20):
        parts.append(build_subrecord(b"INDX", struct.pack("<HBB", stage, 0, 0)))
        for entry in (1, 2):
            parts.append(build_subrecord(b"QSDT", b"\0"))
            text = f"Stage {stage} entry {entry}".encode() + b"\0"
            parts.append(build_subrecord(b"CNAM", text))
    parts.append(build_subrecord(b"ZZZZ", b"opaque quest extension"))
    return b"".join(parts)


def _info_payload() -> bytes:
    """Builds two dialogue responses with distinct text and response numbers.

    Returns:
        Encoded INFO subrecords including their packed response structures.
    """

    parts: list[bytes] = []
    for index in (1, 2):
        data = struct.pack("<III B3x IB3x", 0, 25, 0, index, 0, 0)
        parts.append(build_subrecord(b"TRDT", data))
        parts.append(build_subrecord(b"NAM1", f"Response {index}\0".encode()))
        parts.append(build_subrecord(b"NAM2", f"Notes {index}\0".encode()))
    return b"".join(parts)


def _perk_payload() -> bytes:
    """Builds a quest-stage effect and an ability effect in separate groups.

    Returns:
        Encoded PERK subrecords exercising struct and scalar union alternatives.
    """

    return b"".join(
        (
            build_subrecord(b"EDID", b"IntegrationPerk\0"),
            build_subrecord(b"PRKE", bytes((0, 1, 2))),
            build_subrecord(b"DATA", struct.pack("<IB3x", 0x800, 10)),
            build_subrecord(b"PRKF", b""),
            build_subrecord(b"PRKE", bytes((1, 2, 3))),
            build_subrecord(b"DATA", struct.pack("<I", 0x901)),
            build_subrecord(b"PRKF", b""),
        )
    )


def source_bytes() -> bytes:
    """Builds a small plugin without requiring copyrighted game data.

    Returns:
        Complete plugin with grouped and untouched compressed records.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=4))
    )
    groups = [
        build_grup(signature, 0, build_record(signature, form_id, 0, payload))
        for signature, form_id, payload in (
            (b"QUST", 0x800, _quest_payload()),
            (b"INFO", 0x801, _info_payload()),
            (b"PERK", 0x802, _perk_payload()),
        )
    ]
    untouched = build_subrecord(b"EDID", b"KeepCompressedBytes\0")
    compressed = struct.pack("<I", len(untouched)) + zlib.compress(
        untouched, level=1
    )
    groups.append(
        build_grup(
            b"MISC", 0, build_record(b"MISC", 0x900, 0x40000, compressed)
        )
    )
    return header + b"".join(groups)


def record(plugin: Plugin, form_id: int) -> Record:
    """Finds a fixture record and reports a missing fixture as an assertion.

    Args:
        plugin: Open fixture plugin.
        form_id: Expected file-local record identity.

    Returns:
        Borrowed record owned by the supplied plugin.
    """

    record = plugin.find_record(form_id)
    assert record is not None
    return record


def single_record_source(signature: bytes, payload: bytes) -> bytes:
    """Builds one synthetic record inside a complete Skyrim SE plugin.

    Args:
        signature: Four-byte record signature.
        payload: Concatenated encoded subrecords.

    Returns:
        Complete plugin containing FormID 0x800.
    """

    header = build_record(
        b"TES4", 0, 0, build_subrecord(b"HEDR", build_hedr(num_records=1))
    )
    return header + build_grup(
        signature, 0, build_record(signature, 0x800, 0, payload)
    )


def _vmad_text(value: str) -> bytes:
    """Encodes a synthetic VMAD length-prefixed string.

    Args:
        value: ASCII fixture text without a trailing terminator.

    Returns:
        Unsigned 16-bit byte length followed by the text bytes.
    """

    encoded = value.encode("ascii")
    return struct.pack("<H", len(encoded)) + encoded


def vmad_array_payload() -> bytes:
    """Builds string and signed-integer array properties in one VMAD script.

    Returns:
        Version 5 VMAD using object format 2 and two edited properties.
    """

    strings = (
        _vmad_text("Texts")
        + bytes((12, 1))
        + struct.pack("<I", 2)
        + _vmad_text("hello")
        + _vmad_text("world")
    )
    integers = (
        _vmad_text("Numbers") + bytes((13, 1)) + struct.pack("<Iii", 2, -7, 42)
    )
    return (
        struct.pack("<HHH", 5, 2, 1)
        + _vmad_text("IntegrationScript")
        + struct.pack("<BH", 0, 2)
        + strings
        + integers
    )
