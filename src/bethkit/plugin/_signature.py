"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes


def signature_buffer(sig: bytes | str) -> ctypes.Array[ctypes.c_uint8]:
    """Convert a 4-byte signature to a ctypes ``c_uint8`` array.

    Args:
        sig (bytes | str): Four-byte ASCII signature.

    Returns:
        ctypes.Array: A ``c_uint8[4]`` array containing the signature.

    Raises:
        ValueError: If *sig* is not exactly 4 bytes.
    """

    if isinstance(sig, str):
        sig = sig.encode("ascii")
    if len(sig) != 4:
        raise ValueError("signature must be exactly 4 bytes")
    return (ctypes.c_uint8 * 4)(*sig)
