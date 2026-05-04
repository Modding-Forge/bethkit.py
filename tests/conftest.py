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

import io
import json
import struct
import sys
import urllib.request
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING, Any, Optional
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

_GITHUB_API = (
    "https://api.github.com/repos/Modding-Forge/bethkit/releases/latest"
)
_GITHUB_HEADERS: dict[str, str] = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "bethkit.py/tests",
    "X-GitHub-Api-Version": "2022-11-28",
}


def _native_lib_name() -> str:
    """
    Return the platform-specific name of the bethkit native library.

    Returns:
        str: Library file name for the current OS.
    """

    if sys.platform == "win32":
        return "bethkit_ffi.dll"
    if sys.platform == "darwin":
        return "libbethkit_ffi.dylib"
    return "libbethkit_ffi.so"


def _zip_asset_name() -> str:
    """
    Return the platform-specific ZIP asset name used in GitHub releases.

    Returns:
        str: ZIP asset name for the current OS.
    """

    if sys.platform == "win32":
        return "windows-x64"
    if sys.platform == "darwin":
        return "macos-x64"
    return "linux-x64"


def _try_download_native_lib() -> None:
    """
    Attempt to download the bethkit native library from the latest GitHub
    release ZIP and extract it next to the package so ``_ffi.load_lib()``
    finds it.

    The ZIP is expected to have a flat layout with the library at its root
    (e.g. ``bethkit_ffi.dll`` directly, not inside subdirectories).

    Silently does nothing on any network or API error.
    """

    lib_name = _native_lib_name()
    dest: Path = Path(__file__).parent.parent / "src" / "bethkit" / lib_name

    if dest.exists():
        return

    try:
        req = urllib.request.Request(_GITHUB_API, headers=_GITHUB_HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            release: Any = json.loads(resp.read())
    except Exception:
        return

    platform_suffix = _zip_asset_name()
    download_url: Optional[str] = None
    assets: list[dict[str, Any]] = release.get("assets") or []
    for asset in assets:
        name = asset.get("name", "")
        if isinstance(name, str) and name.endswith(f"-{platform_suffix}.zip"):
            url = asset.get("browser_download_url")
            if isinstance(url, str):
                download_url = url
            break

    if not download_url:
        return

    try:
        with urllib.request.urlopen(download_url, timeout=60) as resp:
            zip_data = resp.read()
    except Exception:
        return

    try:
        with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
            if lib_name in zf.namelist():
                dest.write_bytes(zf.read(lib_name))
    except Exception:
        pass


def pytest_configure(config: pytest.Config) -> None:
    """
    Download the platform-specific bethkit native library before test
    collection when it is not already present.
    """

    _try_download_native_lib()


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """
    Automatically skip tests marked ``integration`` when the native library
    is unavailable.
    """

    try:
        from bethkit._ffi import load_lib

        load_lib()
        _lib_available = True
    except Exception:
        _lib_available = False

    if _lib_available:
        return

    skip_marker = pytest.mark.skip(
        reason="bethkit_ffi native library not available"
    )
    for item in items:
        if item.get_closest_marker("integration"):
            item.add_marker(skip_marker)


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
