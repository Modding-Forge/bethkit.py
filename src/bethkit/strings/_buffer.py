"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes


def from_bytes(data: bytes) -> ctypes.Array[ctypes.c_uint8]:
    """
    Wraps *data* in a ctypes ``c_uint8`` array for FFI calls.

    Args:
        data (bytes): Byte sequence to wrap.

    Returns:
        ctypes.Array: A ``c_uint8`` array backed by a copy of *data*.
    """

    return (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
