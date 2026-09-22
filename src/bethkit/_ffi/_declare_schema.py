"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes

from ._types import BethkitFieldMetadata, BethkitFieldValue, BethkitNamedField


def declare(lib: ctypes.CDLL) -> None:
    """Declares the schema ABI functions.

    Args:
        lib: Native library receiving exact argument and result types.

    Raises:
        AttributeError: If a required ABI symbol is unavailable.
    """

    lib.bethkit_schema_package_manifest_json.restype = ctypes.c_void_p
    lib.bethkit_schema_package_manifest_json.argtypes = [ctypes.c_void_p]
    lib.bethkit_schema_package_graph_json.restype = ctypes.c_void_p
    lib.bethkit_schema_package_graph_json.argtypes = [ctypes.c_void_p]

    lib.bethkit_semantic_validate_json.restype = ctypes.c_void_p
    lib.bethkit_semantic_validate_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_bool,
        ctypes.c_uint32,
    ]

    lib.bethkit_record_view_field_metadata.restype = ctypes.c_int32
    lib.bethkit_record_view_field_metadata.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
        ctypes.POINTER(BethkitFieldMetadata),
    ]
    lib.bethkit_field_entries_metadata.restype = ctypes.c_int32
    lib.bethkit_field_entries_metadata.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
        ctypes.POINTER(BethkitFieldMetadata),
    ]

    lib.bethkit_schema_catalog_embedded.restype = ctypes.c_void_p
    lib.bethkit_schema_catalog_embedded.argtypes = []

    lib.bethkit_schema_catalog_open.restype = ctypes.c_void_p
    lib.bethkit_schema_catalog_open.argtypes = [ctypes.c_char_p]

    lib.bethkit_schema_catalog_free.restype = None
    lib.bethkit_schema_catalog_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_schema_catalog_package.restype = ctypes.c_void_p
    lib.bethkit_schema_catalog_package.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int32,
    ]

    lib.bethkit_schema_package_open.restype = ctypes.c_void_p
    lib.bethkit_schema_package_open.argtypes = [ctypes.c_char_p]

    lib.bethkit_schema_package_free.restype = None
    lib.bethkit_schema_package_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_semantic_context_new.restype = ctypes.c_void_p
    lib.bethkit_semantic_context_new.argtypes = [ctypes.c_void_p]

    lib.bethkit_semantic_context_free.restype = None
    lib.bethkit_semantic_context_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_editor_new.restype = ctypes.c_void_p
    lib.bethkit_record_editor_new.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_bool,
    ]

    lib.bethkit_record_editor_free.restype = None
    lib.bethkit_record_editor_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_editor_set_i64.restype = ctypes.c_int32
    lib.bethkit_record_editor_set_i64.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_size_t,
        ctypes.c_int64,
    ]

    lib.bethkit_record_editor_set_u64.restype = ctypes.c_int32
    lib.bethkit_record_editor_set_u64.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_size_t,
        ctypes.c_uint64,
    ]

    lib.bethkit_record_editor_set_f64.restype = ctypes.c_int32
    lib.bethkit_record_editor_set_f64.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_size_t,
        ctypes.c_double,
    ]

    lib.bethkit_record_editor_set_form_id.restype = ctypes.c_int32
    lib.bethkit_record_editor_set_form_id.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_size_t,
        ctypes.c_uint32,
    ]

    lib.bethkit_record_editor_set_string.restype = ctypes.c_int32
    lib.bethkit_record_editor_set_string.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_size_t,
        ctypes.c_char_p,
    ]

    lib.bethkit_record_editor_set_bytes.restype = ctypes.c_int32
    lib.bethkit_record_editor_set_bytes.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_size_t,
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_size_t,
    ]

    lib.bethkit_record_editor_remove.restype = ctypes.c_int32
    lib.bethkit_record_editor_remove.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_size_t,
    ]

    lib.bethkit_record_editor_finish.restype = ctypes.c_void_p
    lib.bethkit_record_editor_finish.argtypes = [ctypes.c_void_p]

    lib.bethkit_semantic_snapshot_json.restype = ctypes.c_void_p
    lib.bethkit_semantic_snapshot_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_bool,
    ]

    lib.bethkit_semantic_strings_snapshot_json.restype = ctypes.c_void_p
    lib.bethkit_semantic_strings_snapshot_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_bool,
    ]

    lib.bethkit_record_editor_snapshot_json.restype = ctypes.c_void_p
    lib.bethkit_record_editor_snapshot_json.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_editor_strings_snapshot_json.restype = ctypes.c_void_p
    lib.bethkit_record_editor_strings_snapshot_json.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_editor_insert_json.restype = ctypes.c_int32
    lib.bethkit_record_editor_insert_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_record_editor_set_at_json.restype = ctypes.c_int32
    lib.bethkit_record_editor_set_at_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_record_editor_insert_at_json.restype = ctypes.c_int32
    lib.bethkit_record_editor_insert_at_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_record_editor_remove_at_json.restype = ctypes.c_int32
    lib.bethkit_record_editor_remove_at_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
    ]

    lib.bethkit_record_view_new.restype = ctypes.c_void_p
    lib.bethkit_record_view_new.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_bool,
    ]

    lib.bethkit_record_view_free.restype = None
    lib.bethkit_record_view_free.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_view_field_count.restype = ctypes.c_size_t
    lib.bethkit_record_view_field_count.argtypes = [ctypes.c_void_p]

    lib.bethkit_record_view_field_get.restype = ctypes.POINTER(
        BethkitNamedField
    )
    lib.bethkit_record_view_field_get.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
    ]

    lib.bethkit_field_entries_len.restype = ctypes.c_size_t
    lib.bethkit_field_entries_len.argtypes = [ctypes.c_void_p]

    lib.bethkit_field_entries_get.restype = ctypes.POINTER(BethkitNamedField)
    lib.bethkit_field_entries_get.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

    lib.bethkit_field_entries_free.restype = None
    lib.bethkit_field_entries_free.argtypes = [ctypes.c_void_p]
    # NOTE: bethkit_field_entries_free is never called directly from Python.
    # NOTE: bethkit_record_view_free transitively frees the entries buffer.
    # NOTE: Declared here to keep the 1:1 FFI mapping intact.

    lib.bethkit_field_values_len.restype = ctypes.c_size_t
    lib.bethkit_field_values_len.argtypes = [ctypes.c_void_p]

    lib.bethkit_field_values_get.restype = ctypes.POINTER(BethkitFieldValue)
    lib.bethkit_field_values_get.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

    lib.bethkit_field_values_free.restype = None
    lib.bethkit_field_values_free.argtypes = [ctypes.c_void_p]
    # NOTE: bethkit_field_values_free is never called directly from Python.
    # NOTE: The values buffer is freed transitively by bethkit_record_view_free.
    # NOTE: Declared here to keep the 1:1 FFI mapping intact.
