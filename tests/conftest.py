"""
Copyright (c) Modding Forge
"""

# Test fixtures and binary builders.

from __future__ import annotations

import gc
import os
import struct
from collections.abc import Iterator
from typing import TYPE_CHECKING, Optional
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


@pytest.fixture(autouse=True)
def collect_mock_handles(mocker: MockerFixture) -> Iterator[None]:
    """Finalizes fake native handles while their library is still patched.

    Args:
        mocker: Active mock manager whose patches outlive this fixture.

    Yields:
        Control to the test before breaking mock-held reference cycles.
    """

    yield
    mocker.resetall(return_value=True, side_effect=True)
    gc.collect()


def pytest_addoption(parser: pytest.Parser) -> None:
    """Registers the mandatory native integration gate.

    Args:
        parser: Parser receiving the test-suite option.
    """

    parser.addoption(
        "--require-native",
        action="store_true",
        default=False,
        help="Fail when native integration cannot load the configured library.",
    )


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """Gates integration tests without accessing the network.

    Args:
        config: Active pytest configuration.
        items: Collected tests, including explicitly marked integration cases.

    Raises:
        pytest.UsageError: An explicitly configured native library cannot load.
    """

    integration = [
        item for item in items if item.get_closest_marker("integration")
    ]
    if not integration:
        return

    required = bool(config.getoption("--require-native"))
    configured = bool(os.environ.get("BETHKIT_LIB"))
    if not required and not configured:
        marker = pytest.mark.skip(
            reason="Set BETHKIT_LIB or --require-native for native integration."
        )
        for item in integration:
            item.add_marker(marker)
        return

    from bethkit import _error, _ffi

    try:
        _ffi.load_lib()
    except _error.BethkitLibraryNotFoundError as exc:
        raise pytest.UsageError(
            f"Configured native integration is unavailable: {exc}"
        ) from exc


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
