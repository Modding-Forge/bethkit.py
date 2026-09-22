"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes


def declare(lib: ctypes.CDLL) -> None:
    """Declares the core ABI functions.

    Args:
        lib: Native library receiving exact argument and result types.

    Raises:
        AttributeError: If a required ABI symbol is unavailable.
    """

    lib.bethkit_last_error.restype = ctypes.c_char_p
    lib.bethkit_last_error.argtypes = []

    lib.bethkit_abi_version.restype = ctypes.c_uint32
    lib.bethkit_abi_version.argtypes = []

    lib.bethkit_string_free.restype = None
    lib.bethkit_string_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_bytes_free.restype = None
    lib.bethkit_bytes_free.argtypes = [
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]
