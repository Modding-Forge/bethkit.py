"""
Copyright (c) Modding Forge

Shared pytest fixtures and binary builder helpers for bethkit.py tests.

Binary layout (SSE / Skyrim Special Edition plugin format):
  Record  = sig(4) + data_size(4) + flags(4) + form_id(4)
              + version_control(4) + form_version(2) + unknown(2) + data
  SubRec  = sig(4) + size(2) + data
  GRUP    = "GRUP"(4) + total_size(4) + label(4) + group_type(4)
              + version_control(4) + unknown(4) + children
  HEDR    = f32(version) + u32(num_records) + u32(next_object_id)  [12 B]
"""
from __future__ import annotations

import struct
from typing import TYPE_CHECKING, Optional
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def build_hedr(
    version: float = 1.7,
    num_records: int = 0,
    next_object_id: int = 0x800,
) -> bytes:
    """
    Build a 12-byte HEDR payload.

    Args:
        version (float): Plugin version float stored in the HEDR sub-record.
        num_records (int): Number of records declared in the header.
        next_object_id (int): Next object ID counter.

    Returns:
        bytes: 12-byte little-endian payload.
    """

    return struct.pack("<fII", version, num_records, next_object_id)


def build_subrecord(sig: bytes, data: bytes) -> bytes:
    """
    Build a sub-record: ``sig(4) + size(2) + data``.

    Args:
        sig (bytes): Four-byte signature.
        data (bytes): Sub-record payload.

    Returns:
        bytes: Encoded sub-record.
    """

    return sig + struct.pack("<H", len(data)) + data


def build_record(
    sig: bytes,
    form_id: int,
    flags: int,
    data: bytes,
    form_version: int = 44,
) -> bytes:
    """
    Build a 24-byte record header followed by *data*.

    Args:
        sig (bytes): Four-byte record type signature.
        form_id (int): Raw 32-bit FormID.
        flags (int): Record header flags bitmask.
        data (bytes): Record body payload.
        form_version (int): Form version number. Defaults to ``44`` (SSE).

    Returns:
        bytes: Complete encoded record.
    """

    header = (
        sig
        + struct.pack("<I", len(data))
        + struct.pack("<I", flags)
        + struct.pack("<I", form_id)
        + struct.pack("<I", 0)
        + struct.pack("<H", form_version)
        + struct.pack("<H", 0)
    )
    return header + data


def build_grup(
    label: bytes,
    group_type: int,
    children: bytes,
) -> bytes:
    """
    Build a GRUP block: 24-byte header + *children*.

    Args:
        label (bytes): Four-byte group label (e.g. ``b"NPC_"``).
        group_type (int): Numeric group type code (``0`` = top-level).
        children (bytes): Serialised child records or groups.

    Returns:
        bytes: Complete GRUP block.
    """

    total: int = 24 + len(children)
    label_int: int = int.from_bytes(label, "little")
    header = (
        b"GRUP"
        + struct.pack("<I", total)
        + struct.pack("<I", label_int)
        + struct.pack("<I", group_type)
        + struct.pack("<I", 0)
        + struct.pack("<I", 0)
    )
    return header + children


def build_minimal_plugin(
    hedr_version: float = 1.7,
    masters: Optional[list[str]] = None,
) -> bytes:
    """
    Build minimal valid SSE plugin bytes with one NPC_ group.

    The plugin contains:
    - A ``TES4`` header record with a HEDR sub-record (and optional MAST).
    - One top-level NPC_ group containing one NPC_ record with an EDID.

    Args:
        hedr_version (float): HEDR version float. Defaults to ``1.7``.
        masters (list[str] | None): Optional list of master names to embed
            as MAST sub-records in the TES4 header.

    Returns:
        bytes: Minimal valid plugin byte string.
    """

    hedr_data = build_hedr(hedr_version, 1, 0x800)
    tes4_body = build_subrecord(b"HEDR", hedr_data)

    for master_name in masters or []:
        tes4_body += build_subrecord(
            b"MAST", master_name.encode("utf-8") + b"\x00"
        )
        tes4_body += build_subrecord(b"DATA", struct.pack("<Q", 0))

    tes4_rec = build_record(b"TES4", 0, 0, tes4_body)

    edid_sr = build_subrecord(b"EDID", b"TestNPC\x00")
    npc_rec = build_record(b"NPC_", 0x000D62, 0, edid_sr)
    npc_grup = build_grup(b"NPC_", 0, npc_rec)

    return tes4_rec + npc_grup


@pytest.fixture()
def mock_lib(mocker: MockerFixture) -> MagicMock:
    """
    Fixture that patches ``bethkit._ffi.load_lib`` with a ``MagicMock``.

    Returns a configured :class:`~unittest.mock.MagicMock` that can be
    used to set expected return values for individual FFI functions.

    Returns:
        MagicMock: The mock native library handle.
    """

    lib = MagicMock()
    mocker.patch("bethkit._ffi.load_lib", return_value=lib)
    return lib
