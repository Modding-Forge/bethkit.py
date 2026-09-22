"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes


def declare(lib: ctypes.CDLL) -> None:
    """Declares the archive ABI functions.

    Args:
        lib: Native library receiving exact argument and result types.

    Raises:
        AttributeError: If a required ABI symbol is unavailable.
    """

    lib.bethkit_archive_extract_status.restype = ctypes.c_int32
    lib.bethkit_archive_extract_status.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.POINTER(ctypes.c_size_t),
    ]
    lib.bethkit_archive_open.restype = ctypes.c_void_p
    lib.bethkit_archive_open.argtypes = [ctypes.c_char_p]

    lib.bethkit_archive_free.restype = None
    lib.bethkit_archive_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_archive_format_name.restype = ctypes.c_char_p
    lib.bethkit_archive_format_name.argtypes = [ctypes.c_void_p]

    lib.bethkit_archive_file_count.restype = ctypes.c_size_t
    lib.bethkit_archive_file_count.argtypes = [ctypes.c_void_p]

    lib.bethkit_archive_entry_get.restype = ctypes.c_void_p
    lib.bethkit_archive_entry_get.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

    lib.bethkit_archive_entry_path.restype = ctypes.c_void_p
    lib.bethkit_archive_entry_path.argtypes = [ctypes.c_void_p]

    lib.bethkit_archive_entry_path_free.restype = None
    lib.bethkit_archive_entry_path_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_archive_entry_uncompressed_size.restype = ctypes.c_uint32
    lib.bethkit_archive_entry_uncompressed_size.argtypes = [ctypes.c_void_p]

    lib.bethkit_archive_extract.restype = ctypes.POINTER(ctypes.c_uint8)
    lib.bethkit_archive_extract.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.POINTER(ctypes.c_size_t),
    ]

    lib.bethkit_archive_extract_to_file.restype = ctypes.c_int32
    lib.bethkit_archive_extract_to_file.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_bsa_writer_new.restype = ctypes.c_void_p
    lib.bethkit_bsa_writer_new.argtypes = [ctypes.c_int32]

    lib.bethkit_bsa_writer_free.restype = None
    lib.bethkit_bsa_writer_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_bsa_writer_set_compress.restype = ctypes.c_int32
    lib.bethkit_bsa_writer_set_compress.argtypes = [
        ctypes.c_void_p,
        ctypes.c_bool,
    ]

    lib.bethkit_bsa_writer_set_embed_names.restype = ctypes.c_int32
    lib.bethkit_bsa_writer_set_embed_names.argtypes = [
        ctypes.c_void_p,
        ctypes.c_bool,
    ]

    lib.bethkit_bsa_writer_add.restype = ctypes.c_int32
    lib.bethkit_bsa_writer_add.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]

    lib.bethkit_bsa_writer_write_to.restype = ctypes.c_int32
    lib.bethkit_bsa_writer_write_to.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_ba2_gnrl_writer_new.restype = ctypes.c_void_p
    lib.bethkit_ba2_gnrl_writer_new.argtypes = [ctypes.c_int32]

    lib.bethkit_ba2_gnrl_writer_free.restype = None
    lib.bethkit_ba2_gnrl_writer_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_ba2_gnrl_writer_add.restype = ctypes.c_int32
    lib.bethkit_ba2_gnrl_writer_add.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]

    lib.bethkit_ba2_gnrl_writer_write_to.restype = ctypes.c_int32
    lib.bethkit_ba2_gnrl_writer_write_to.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_ba2_dx10_writer_new.restype = ctypes.c_void_p
    lib.bethkit_ba2_dx10_writer_new.argtypes = [ctypes.c_int32]

    lib.bethkit_ba2_dx10_writer_free.restype = None
    lib.bethkit_ba2_dx10_writer_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_ba2_dx10_writer_add.restype = ctypes.c_int32
    lib.bethkit_ba2_dx10_writer_add.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]

    lib.bethkit_ba2_dx10_writer_write_to.restype = ctypes.c_int32
    lib.bethkit_ba2_dx10_writer_write_to.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]
