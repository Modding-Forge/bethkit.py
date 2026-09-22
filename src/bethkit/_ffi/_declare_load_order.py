"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes

from ._types import BethkitGlobalFormId


def declare(lib: ctypes.CDLL) -> None:
    """Declares the load order ABI functions.

    Args:
        lib: Native library receiving exact argument and result types.

    Raises:
        AttributeError: If a required ABI symbol is unavailable.
    """

    lib.bethkit_load_order_resolve_with_plugin.restype = ctypes.c_int32
    lib.bethkit_load_order_resolve_with_plugin.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.c_char_p,
        ctypes.c_void_p,
        ctypes.POINTER(BethkitGlobalFormId),
    ]
    lib.bethkit_load_order_new.restype = ctypes.c_void_p
    lib.bethkit_load_order_new.argtypes = []

    lib.bethkit_load_order_free.restype = None
    lib.bethkit_load_order_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_load_order_push.restype = ctypes.c_int32
    lib.bethkit_load_order_push.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_int32,
    ]

    lib.bethkit_load_order_len.restype = ctypes.c_size_t
    lib.bethkit_load_order_len.argtypes = [ctypes.c_void_p]

    lib.bethkit_load_order_resolve.restype = ctypes.c_int32
    lib.bethkit_load_order_resolve.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.c_char_p,
        ctypes.POINTER(BethkitGlobalFormId),
    ]
