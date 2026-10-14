"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes

from .. import _ffi
from ..enums import StringFileKind


def serialize_table(pointer: int, kind: StringFileKind) -> bytes:
    """Serializes one localization table and frees its native byte buffer.

    Args:
        pointer: Open native localization-set handle.
        kind: Table to serialize.

    Returns:
        Encoded Bethesda string-table bytes.

    Raises:
        BethkitNativeError: Serialization failed.
    """

    lib = _ffi.load_lib()
    result = ctypes.c_void_p()
    length = ctypes.c_size_t()
    if (
        lib.bethkit_localization_set_table_to_bytes(
            pointer, int(kind), ctypes.byref(result), ctypes.byref(length)
        )
        != 0
    ):
        _ffi.raise_last_error(lib)
    try:
        return bytes(ctypes.string_at(result, length.value))
    finally:
        lib.bethkit_bytes_free(
            ctypes.cast(result, ctypes.POINTER(ctypes.c_uint8)), length.value
        )
