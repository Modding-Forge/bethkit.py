"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes


def declare(lib: ctypes.CDLL) -> None:
    """Declares the strings ABI functions.

    Args:
        lib: Native library receiving exact argument and result types.

    Raises:
        AttributeError: If a required ABI symbol is unavailable.
    """

    lib.bethkit_string_table_new.restype = ctypes.c_void_p
    lib.bethkit_string_table_new.argtypes = [ctypes.c_int32]

    lib.bethkit_string_table_open.restype = ctypes.c_void_p
    lib.bethkit_string_table_open.argtypes = [ctypes.c_char_p]

    lib.bethkit_string_table_free.restype = None
    lib.bethkit_string_table_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_string_table_kind.restype = ctypes.c_int32
    lib.bethkit_string_table_kind.argtypes = [ctypes.c_void_p]

    lib.bethkit_string_table_len.restype = ctypes.c_size_t
    lib.bethkit_string_table_len.argtypes = [ctypes.c_void_p]

    lib.bethkit_string_table_get.restype = ctypes.POINTER(ctypes.c_uint8)
    lib.bethkit_string_table_get.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_size_t),
    ]

    lib.bethkit_string_table_insert.restype = ctypes.c_int32
    lib.bethkit_string_table_insert.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]

    lib.bethkit_string_table_insert_new.restype = ctypes.c_int32
    lib.bethkit_string_table_insert_new.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
        ctypes.POINTER(ctypes.c_uint32),
    ]

    lib.bethkit_string_table_remove.restype = ctypes.c_bool
    lib.bethkit_string_table_remove.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
    ]

    lib.bethkit_string_table_write_to_file.restype = ctypes.c_int32
    lib.bethkit_string_table_write_to_file.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_localization_set_new.restype = ctypes.c_void_p
    lib.bethkit_localization_set_new.argtypes = []

    lib.bethkit_localization_set_clone.restype = ctypes.c_void_p
    lib.bethkit_localization_set_clone.argtypes = [ctypes.c_void_p]

    lib.bethkit_localization_set_insert_new.restype = ctypes.c_int32
    lib.bethkit_localization_set_insert_new.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int32,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
        ctypes.POINTER(ctypes.c_uint32),
    ]

    lib.bethkit_localization_set_remove.restype = ctypes.c_int32
    lib.bethkit_localization_set_remove.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int32,
        ctypes.c_uint32,
    ]

    lib.bethkit_localization_set_table_to_bytes.restype = ctypes.c_int32
    lib.bethkit_localization_set_table_to_bytes.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int32,
        ctypes.POINTER(ctypes.c_void_p),
        ctypes.POINTER(ctypes.c_size_t),
    ]

    lib.bethkit_localization_set_open.restype = ctypes.c_void_p
    lib.bethkit_localization_set_open.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_localization_set_free.restype = None
    lib.bethkit_localization_set_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_localization_set_get.restype = ctypes.POINTER(ctypes.c_uint8)
    lib.bethkit_localization_set_get.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int32,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_size_t),
    ]

    lib.bethkit_localization_set_set.restype = ctypes.c_int32
    lib.bethkit_localization_set_set.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int32,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]

    lib.bethkit_localization_set_write.restype = ctypes.c_int32
    lib.bethkit_localization_set_write.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]
