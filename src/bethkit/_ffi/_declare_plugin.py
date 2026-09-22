"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes

from ._types import BethkitGlobalFormId, BethkitSlice


def declare(lib: ctypes.CDLL) -> None:
    """Declares the plugin ABI functions.

    Args:
        lib: Native library receiving exact argument and result types.

    Raises:
        AttributeError: If a required ABI symbol is unavailable.
    """

    lib.bethkit_record_editor_id_status.restype = ctypes.c_int32
    lib.bethkit_record_editor_id_status.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_void_p),
    ]

    lib.bethkit_plugin_patcher_new.restype = ctypes.c_void_p
    lib.bethkit_plugin_patcher_new.argtypes = [ctypes.c_void_p]
    lib.bethkit_plugin_patcher_free.restype = None
    lib.bethkit_plugin_patcher_free.argtypes = [ctypes.c_void_p]
    lib.bethkit_plugin_patcher_replace_record.restype = ctypes.c_int32
    lib.bethkit_plugin_patcher_replace_record.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.c_void_p,
    ]
    lib.bethkit_plugin_patcher_write_to_bytes.restype = ctypes.c_int32
    lib.bethkit_plugin_patcher_write_to_bytes.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)),
        ctypes.POINTER(ctypes.c_size_t),
    ]
    lib.bethkit_plugin_patcher_write_to_file.restype = ctypes.c_int32
    lib.bethkit_plugin_patcher_write_to_file.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_plugin_writer_add_master.restype = ctypes.c_int32
    lib.bethkit_plugin_writer_add_master.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]
    lib.bethkit_plugin_writer_set_description.restype = ctypes.c_int32
    lib.bethkit_plugin_writer_set_description.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]
    lib.bethkit_plugin_writer_set_localized.restype = ctypes.c_int32
    lib.bethkit_plugin_writer_set_localized.argtypes = [
        ctypes.c_void_p,
        ctypes.c_bool,
    ]

    lib.bethkit_plugin_open.restype = ctypes.c_void_p
    lib.bethkit_plugin_open.argtypes = [ctypes.c_char_p, ctypes.c_int32]

    lib.bethkit_plugin_open_from_bytes.restype = ctypes.c_void_p
    lib.bethkit_plugin_open_from_bytes.argtypes = [
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
        ctypes.c_int32,
    ]

    lib.bethkit_plugin_free.restype = None
    lib.bethkit_plugin_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_kind.restype = ctypes.c_int32
    lib.bethkit_plugin_kind.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_is_localized.restype = ctypes.c_bool
    lib.bethkit_plugin_is_localized.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_master_count.restype = ctypes.c_size_t
    lib.bethkit_plugin_master_count.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_master_get.restype = ctypes.c_char_p
    lib.bethkit_plugin_master_get.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

    lib.bethkit_plugin_description.restype = ctypes.c_char_p
    lib.bethkit_plugin_description.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_group_count.restype = ctypes.c_size_t
    lib.bethkit_plugin_group_count.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_group_get.restype = ctypes.c_void_p
    lib.bethkit_plugin_group_get.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

    lib.bethkit_plugin_find_record.restype = ctypes.c_void_p
    lib.bethkit_plugin_find_record.argtypes = [ctypes.c_void_p, ctypes.c_uint32]

    lib.bethkit_record_signature.restype = ctypes.c_int32
    lib.bethkit_record_signature.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint8),
    ]

    lib.bethkit_record_form_id.restype = ctypes.c_uint32
    lib.bethkit_record_form_id.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_flags.restype = ctypes.c_uint32
    lib.bethkit_record_flags.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_form_version.restype = ctypes.c_uint16
    lib.bethkit_record_form_version.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_editor_id.restype = ctypes.c_void_p
    lib.bethkit_record_editor_id.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_editor_id_free.restype = None
    lib.bethkit_record_editor_id_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_subrecord_count.restype = ctypes.c_int64
    lib.bethkit_record_subrecord_count.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_subrecord_get.restype = ctypes.c_void_p
    lib.bethkit_record_subrecord_get.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
    ]

    lib.bethkit_record_subrecord_find.restype = ctypes.c_void_p
    lib.bethkit_record_subrecord_find.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint8),
    ]

    lib.bethkit_subrecord_signature.restype = ctypes.c_int32
    lib.bethkit_subrecord_signature.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint8),
    ]

    lib.bethkit_subrecord_bytes.restype = BethkitSlice
    lib.bethkit_subrecord_bytes.argtypes = [ctypes.c_void_p]

    lib.bethkit_subrecord_as_u8.restype = ctypes.c_int32
    lib.bethkit_subrecord_as_u8.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint8),
    ]

    lib.bethkit_subrecord_as_u16.restype = ctypes.c_int32
    lib.bethkit_subrecord_as_u16.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint16),
    ]

    lib.bethkit_subrecord_as_u32.restype = ctypes.c_int32
    lib.bethkit_subrecord_as_u32.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint32),
    ]

    lib.bethkit_subrecord_as_f32.restype = ctypes.c_int32
    lib.bethkit_subrecord_as_f32.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_float),
    ]

    lib.bethkit_subrecord_as_zstring.restype = ctypes.c_void_p
    lib.bethkit_subrecord_as_zstring.argtypes = [ctypes.c_void_p]

    lib.bethkit_zstring_free.restype = None
    lib.bethkit_zstring_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_group_type.restype = ctypes.c_int32
    lib.bethkit_group_type.argtypes = [ctypes.c_void_p]

    lib.bethkit_group_child_count.restype = ctypes.c_size_t
    lib.bethkit_group_child_count.argtypes = [ctypes.c_void_p]

    lib.bethkit_group_child_is_record.restype = ctypes.c_bool
    lib.bethkit_group_child_is_record.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
    ]

    lib.bethkit_group_child_as_record.restype = ctypes.c_void_p
    lib.bethkit_group_child_as_record.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
    ]

    lib.bethkit_group_child_as_group.restype = ctypes.c_void_p
    lib.bethkit_group_child_as_group.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
    ]

    lib.bethkit_plugin_cache_new.restype = ctypes.c_void_p
    lib.bethkit_plugin_cache_new.argtypes = []

    lib.bethkit_plugin_cache_free.restype = None
    lib.bethkit_plugin_cache_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_cache_add.restype = ctypes.c_int32
    lib.bethkit_plugin_cache_add.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_void_p,
    ]

    lib.bethkit_plugin_cache_len.restype = ctypes.c_size_t
    lib.bethkit_plugin_cache_len.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_cache_record_count.restype = ctypes.c_size_t
    lib.bethkit_plugin_cache_record_count.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_cache_resolve.restype = ctypes.c_void_p
    lib.bethkit_plugin_cache_resolve.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_uint32,
    ]

    lib.bethkit_plugin_cache_find_by_editor_id.restype = ctypes.c_void_p
    lib.bethkit_plugin_cache_find_by_editor_id.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.POINTER(BethkitGlobalFormId),
    ]

    lib.bethkit_plugin_writer_new.restype = ctypes.c_void_p
    lib.bethkit_plugin_writer_new.argtypes = [ctypes.c_int32, ctypes.c_float]

    lib.bethkit_plugin_writer_free.restype = None
    lib.bethkit_plugin_writer_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_plugin_writer_add_group.restype = ctypes.c_int32
    lib.bethkit_plugin_writer_add_group.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
    ]

    lib.bethkit_plugin_writer_write_to_file.restype = ctypes.c_int32
    lib.bethkit_plugin_writer_write_to_file.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_plugin_writer_write_to_bytes.restype = ctypes.POINTER(
        ctypes.c_uint8
    )
    lib.bethkit_plugin_writer_write_to_bytes.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_size_t),
    ]

    lib.bethkit_writable_group_new.restype = ctypes.c_void_p
    lib.bethkit_writable_group_new.argtypes = [
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_int32,
    ]

    lib.bethkit_writable_group_free.restype = None
    lib.bethkit_writable_group_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_writable_group_add_record.restype = ctypes.c_int32
    lib.bethkit_writable_group_add_record.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
    ]

    lib.bethkit_writable_group_add_group.restype = ctypes.c_int32
    lib.bethkit_writable_group_add_group.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
    ]

    lib.bethkit_writable_record_new.restype = ctypes.c_void_p
    lib.bethkit_writable_record_new.argtypes = [
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.c_uint16,
    ]

    lib.bethkit_writable_record_free.restype = None
    lib.bethkit_writable_record_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_writable_record_add_subrecord.restype = ctypes.c_int32
    lib.bethkit_writable_record_add_subrecord.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]
