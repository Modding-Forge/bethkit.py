"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
import os
import sys
import threading
from collections.abc import Callable
from pathlib import Path

from ._types import (
    BethkitFieldValue,
    BethkitGlobalFormId,
    BethkitNamedField,
    BethkitSlice,
)

_lib: ctypes.CDLL | None = None
_lib_lock: threading.Lock = threading.Lock()

_c = ctypes.c_char_p
_vp = ctypes.c_void_p
_sz = ctypes.c_size_t
_i32 = ctypes.c_int32
_u8 = ctypes.c_uint8
_u16 = ctypes.c_uint16
_u32 = ctypes.c_uint32
_u64 = ctypes.c_uint64
_i64 = ctypes.c_int64
_f32 = ctypes.c_float
_bl = ctypes.c_bool


def _find_library() -> Path:
    """
    Locate the bethkit shared library.

    Checks the ``BETHKIT_LIB`` environment variable first, then looks
    next to the package directory, then falls back to a bare name for
    the OS loader.

    Returns:
        Path: Resolved path to the library file.
    """

    env = os.environ.get("BETHKIT_LIB")
    if env:
        return Path(env)

    if sys.platform == "win32":
        candidates = ["bethkit_ffi.dll"]
    elif sys.platform == "darwin":
        candidates = ["libbethkit_ffi.dylib"]
    else:
        candidates = ["libbethkit_ffi.so"]

    pkg_dir = Path(__file__).parent
    for name in candidates:
        for search_dir in (pkg_dir, pkg_dir.parent):
            path = search_dir / name
            if path.exists():
                return path

    return Path(candidates[0])


def load_lib() -> ctypes.CDLL:
    """
    Load the bethkit shared library (thread-safe singleton).

    Returns the already-loaded library on subsequent calls.

    Returns:
        ctypes.CDLL: The loaded native library handle.

    Raises:
        BethkitLibraryNotFoundError: If the shared library file cannot
            be found or loaded.
    """

    global _lib
    if _lib is not None:
        return _lib
    with _lib_lock:
        if _lib is None:
            from .._error import BethkitLibraryNotFoundError

            path = _find_library()
            try:
                if sys.platform == "win32" and path.is_absolute():
                    with os.add_dll_directory(str(path.parent)):
                        loaded = ctypes.CDLL(str(path))
                else:
                    loaded = ctypes.CDLL(str(path))
            except OSError as exc:
                raise BethkitLibraryNotFoundError(
                    f"Cannot load bethkit native library '{path}': {exc}. "
                    "Place bethkit_ffi.dll / libbethkit_ffi.so / "
                    "libbethkit_ffi.dylib next to the package or set the "
                    "BETHKIT_LIB environment variable."
                ) from exc
            _declare(loaded)
            _lib = loaded
    return _lib


def last_error(lib: ctypes.CDLL) -> str:
    """
    Return the last error message for the current thread.

    Must be called immediately after a failing FFI call because the
    thread-local error buffer is overwritten by the next FFI call.

    Args:
        lib (ctypes.CDLL): Loaded bethkit native library handle.

    Returns:
        str: The error text, or ``"unknown error"`` if none is set.
    """

    msg: bytes | None = lib.bethkit_last_error()
    if msg:
        return msg.decode("utf-8")
    return "unknown error"


def raise_last_error(lib: ctypes.CDLL) -> None:
    """
    Raise :class:`~bethkit.BethkitNativeError` with the last FFI error.

    Args:
        lib (ctypes.CDLL): Loaded bethkit native library handle.

    Raises:
        BethkitNativeError: Always raised with the current thread-local
            error text.
    """

    from .._error import BethkitNativeError

    raise BethkitNativeError(last_error(lib))


def copy_and_free_str(
    ptr: int,
    free_fn: Callable[[int], None],
    lib: ctypes.CDLL,
) -> str:
    """
    Copy the UTF-8 string at *ptr* into Python and free the native buffer.

    This is the correct pattern for owned ``char*`` values returned by
    the native library: copy first, then free, never hold the raw pointer.

    Args:
        ptr (int): Non-null ``c_void_p`` value pointing to the string.
        free_fn (Callable[[int], None]): The matching ``*_free`` function
            to call after copying.
        lib (ctypes.CDLL): Loaded native library (unused here but kept
            for uniform call-site signature).

    Returns:
        str: The decoded UTF-8 string.
    """

    try:
        return ctypes.string_at(ptr).decode("utf-8")
    finally:
        free_fn(ptr)


def enc(s: Path) -> bytes:
    """
    Encode a filesystem path to a NUL-compatible UTF-8 bytes object.

    Args:
        s (Path): Filesystem path to encode.

    Returns:
        bytes: UTF-8 encoded path bytes.
    """

    return str(s).encode("utf-8")


def senc(s: str) -> bytes:
    """
    Encode a plain string to a NUL-compatible UTF-8 bytes object.

    Args:
        s (str): String to encode.

    Returns:
        bytes: UTF-8 encoded bytes.
    """

    return s.encode("utf-8")


def _declare(lib: ctypes.CDLL) -> None:
    """
    Declare argtypes and restype for every exported bethkit function.

    Args:
        lib (ctypes.CDLL): The freshly loaded native library handle.
    """

    lib.bethkit_last_error.restype = _c
    lib.bethkit_last_error.argtypes = []

    lib.bethkit_bytes_free.restype = None
    lib.bethkit_bytes_free.argtypes = [ctypes.POINTER(_u8), _sz]

    lib.bethkit_plugin_open.restype = _vp
    lib.bethkit_plugin_open.argtypes = [_c, _i32]

    lib.bethkit_plugin_open_from_bytes.restype = _vp
    lib.bethkit_plugin_open_from_bytes.argtypes = [
        ctypes.POINTER(_u8), _sz, _i32
    ]

    lib.bethkit_plugin_free.restype = None
    lib.bethkit_plugin_free.argtypes = [_vp]

    lib.bethkit_plugin_kind.restype = _i32
    lib.bethkit_plugin_kind.argtypes = [_vp]

    lib.bethkit_plugin_is_localized.restype = _bl
    lib.bethkit_plugin_is_localized.argtypes = [_vp]

    lib.bethkit_plugin_master_count.restype = _sz
    lib.bethkit_plugin_master_count.argtypes = [_vp]

    lib.bethkit_plugin_master_get.restype = _c
    lib.bethkit_plugin_master_get.argtypes = [_vp, _sz]

    lib.bethkit_plugin_description.restype = _c
    lib.bethkit_plugin_description.argtypes = [_vp]

    lib.bethkit_plugin_group_count.restype = _sz
    lib.bethkit_plugin_group_count.argtypes = [_vp]

    lib.bethkit_plugin_group_get.restype = _vp
    lib.bethkit_plugin_group_get.argtypes = [_vp, _sz]

    lib.bethkit_plugin_find_record.restype = _vp
    lib.bethkit_plugin_find_record.argtypes = [_vp, _u32]

    lib.bethkit_record_signature.restype = _i32
    lib.bethkit_record_signature.argtypes = [_vp, ctypes.POINTER(_u8)]

    lib.bethkit_record_form_id.restype = _u32
    lib.bethkit_record_form_id.argtypes = [_vp]

    lib.bethkit_record_flags.restype = _u32
    lib.bethkit_record_flags.argtypes = [_vp]

    lib.bethkit_record_form_version.restype = _u16
    lib.bethkit_record_form_version.argtypes = [_vp]

    lib.bethkit_record_editor_id.restype = _vp
    lib.bethkit_record_editor_id.argtypes = [_vp]

    lib.bethkit_record_editor_id_free.restype = None
    lib.bethkit_record_editor_id_free.argtypes = [_vp]

    lib.bethkit_record_subrecord_count.restype = _i64
    lib.bethkit_record_subrecord_count.argtypes = [_vp]

    lib.bethkit_record_subrecord_get.restype = _vp
    lib.bethkit_record_subrecord_get.argtypes = [_vp, _sz]

    lib.bethkit_record_subrecord_find.restype = _vp
    lib.bethkit_record_subrecord_find.argtypes = [_vp, ctypes.POINTER(_u8)]

    lib.bethkit_subrecord_signature.restype = _i32
    lib.bethkit_subrecord_signature.argtypes = [_vp, ctypes.POINTER(_u8)]

    lib.bethkit_subrecord_bytes.restype = BethkitSlice
    lib.bethkit_subrecord_bytes.argtypes = [_vp]

    lib.bethkit_subrecord_as_u8.restype = _i32
    lib.bethkit_subrecord_as_u8.argtypes = [_vp, ctypes.POINTER(_u8)]

    lib.bethkit_subrecord_as_u16.restype = _i32
    lib.bethkit_subrecord_as_u16.argtypes = [_vp, ctypes.POINTER(_u16)]

    lib.bethkit_subrecord_as_u32.restype = _i32
    lib.bethkit_subrecord_as_u32.argtypes = [_vp, ctypes.POINTER(_u32)]

    lib.bethkit_subrecord_as_f32.restype = _i32
    lib.bethkit_subrecord_as_f32.argtypes = [_vp, ctypes.POINTER(_f32)]

    lib.bethkit_subrecord_as_zstring.restype = _vp
    lib.bethkit_subrecord_as_zstring.argtypes = [_vp]

    lib.bethkit_zstring_free.restype = None
    lib.bethkit_zstring_free.argtypes = [_vp]

    lib.bethkit_group_type.restype = _i32
    lib.bethkit_group_type.argtypes = [_vp]

    lib.bethkit_group_child_count.restype = _sz
    lib.bethkit_group_child_count.argtypes = [_vp]

    lib.bethkit_group_child_is_record.restype = _bl
    lib.bethkit_group_child_is_record.argtypes = [_vp, _sz]

    lib.bethkit_group_child_as_record.restype = _vp
    lib.bethkit_group_child_as_record.argtypes = [_vp, _sz]

    lib.bethkit_group_child_as_group.restype = _vp
    lib.bethkit_group_child_as_group.argtypes = [_vp, _sz]

    lib.bethkit_archive_open.restype = _vp
    lib.bethkit_archive_open.argtypes = [_c]

    lib.bethkit_archive_free.restype = None
    lib.bethkit_archive_free.argtypes = [_vp]

    lib.bethkit_archive_format_name.restype = _c
    lib.bethkit_archive_format_name.argtypes = [_vp]

    lib.bethkit_archive_file_count.restype = _sz
    lib.bethkit_archive_file_count.argtypes = [_vp]

    lib.bethkit_archive_entry_get.restype = _vp
    lib.bethkit_archive_entry_get.argtypes = [_vp, _sz]

    lib.bethkit_archive_entry_path.restype = _vp
    lib.bethkit_archive_entry_path.argtypes = [_vp]

    lib.bethkit_archive_entry_path_free.restype = None
    lib.bethkit_archive_entry_path_free.argtypes = [_vp]

    lib.bethkit_archive_entry_uncompressed_size.restype = _u32
    lib.bethkit_archive_entry_uncompressed_size.argtypes = [_vp]

    lib.bethkit_archive_extract.restype = ctypes.POINTER(_u8)
    lib.bethkit_archive_extract.argtypes = [_vp, _c, ctypes.POINTER(_sz)]

    lib.bethkit_archive_extract_to_file.restype = _i32
    lib.bethkit_archive_extract_to_file.argtypes = [_vp, _c, _c]

    lib.bethkit_bsa_writer_new.restype = _vp
    lib.bethkit_bsa_writer_new.argtypes = [_i32]

    lib.bethkit_bsa_writer_free.restype = None
    lib.bethkit_bsa_writer_free.argtypes = [_vp]

    lib.bethkit_bsa_writer_set_compress.restype = _i32
    lib.bethkit_bsa_writer_set_compress.argtypes = [_vp, _bl]

    lib.bethkit_bsa_writer_set_embed_names.restype = _i32
    lib.bethkit_bsa_writer_set_embed_names.argtypes = [_vp, _bl]

    lib.bethkit_bsa_writer_add.restype = _i32
    lib.bethkit_bsa_writer_add.argtypes = [
        _vp, _c, ctypes.POINTER(_u8), _sz
    ]

    lib.bethkit_bsa_writer_write_to.restype = _i32
    lib.bethkit_bsa_writer_write_to.argtypes = [_vp, _c]

    lib.bethkit_ba2_gnrl_writer_new.restype = _vp
    lib.bethkit_ba2_gnrl_writer_new.argtypes = [_i32]

    lib.bethkit_ba2_gnrl_writer_free.restype = None
    lib.bethkit_ba2_gnrl_writer_free.argtypes = [_vp]

    lib.bethkit_ba2_gnrl_writer_add.restype = _i32
    lib.bethkit_ba2_gnrl_writer_add.argtypes = [
        _vp, _c, ctypes.POINTER(_u8), _sz
    ]

    lib.bethkit_ba2_gnrl_writer_write_to.restype = _i32
    lib.bethkit_ba2_gnrl_writer_write_to.argtypes = [_vp, _c]

    lib.bethkit_ba2_dx10_writer_new.restype = _vp
    lib.bethkit_ba2_dx10_writer_new.argtypes = [_i32]

    lib.bethkit_ba2_dx10_writer_free.restype = None
    lib.bethkit_ba2_dx10_writer_free.argtypes = [_vp]

    lib.bethkit_ba2_dx10_writer_add.restype = _i32
    lib.bethkit_ba2_dx10_writer_add.argtypes = [
        _vp, _c, ctypes.POINTER(_u8), _sz
    ]

    lib.bethkit_ba2_dx10_writer_write_to.restype = _i32
    lib.bethkit_ba2_dx10_writer_write_to.argtypes = [_vp, _c]

    lib.bethkit_load_order_new.restype = _vp
    lib.bethkit_load_order_new.argtypes = []

    lib.bethkit_load_order_free.restype = None
    lib.bethkit_load_order_free.argtypes = [_vp]

    lib.bethkit_load_order_push.restype = _i32
    lib.bethkit_load_order_push.argtypes = [_vp, _c, _i32]

    lib.bethkit_load_order_len.restype = _sz
    lib.bethkit_load_order_len.argtypes = [_vp]

    lib.bethkit_load_order_resolve.restype = _i32
    lib.bethkit_load_order_resolve.argtypes = [
        _vp, _u32, _c, ctypes.POINTER(BethkitGlobalFormId)
    ]

    lib.bethkit_plugin_cache_new.restype = _vp
    lib.bethkit_plugin_cache_new.argtypes = []

    lib.bethkit_plugin_cache_free.restype = None
    lib.bethkit_plugin_cache_free.argtypes = [_vp]

    lib.bethkit_plugin_cache_add.restype = _i32
    lib.bethkit_plugin_cache_add.argtypes = [_vp, _c, _vp]

    lib.bethkit_plugin_cache_len.restype = _sz
    lib.bethkit_plugin_cache_len.argtypes = [_vp]

    lib.bethkit_plugin_cache_record_count.restype = _sz
    lib.bethkit_plugin_cache_record_count.argtypes = [_vp]

    lib.bethkit_plugin_cache_resolve.restype = _vp
    lib.bethkit_plugin_cache_resolve.argtypes = [_vp, _c, _u32]

    lib.bethkit_plugin_cache_find_by_editor_id.restype = _vp
    lib.bethkit_plugin_cache_find_by_editor_id.argtypes = [
        _vp, _c, ctypes.POINTER(BethkitGlobalFormId)
    ]

    lib.bethkit_string_table_new.restype = _vp
    lib.bethkit_string_table_new.argtypes = [_i32]

    lib.bethkit_string_table_open.restype = _vp
    lib.bethkit_string_table_open.argtypes = [_c]

    lib.bethkit_string_table_free.restype = None
    lib.bethkit_string_table_free.argtypes = [_vp]

    lib.bethkit_string_table_kind.restype = _i32
    lib.bethkit_string_table_kind.argtypes = [_vp]

    lib.bethkit_string_table_len.restype = _sz
    lib.bethkit_string_table_len.argtypes = [_vp]

    lib.bethkit_string_table_get.restype = ctypes.POINTER(_u8)
    lib.bethkit_string_table_get.argtypes = [_vp, _u32, ctypes.POINTER(_sz)]

    lib.bethkit_string_table_insert.restype = _i32
    lib.bethkit_string_table_insert.argtypes = [
        _vp, _u32, ctypes.POINTER(_u8), _sz
    ]

    lib.bethkit_string_table_insert_new.restype = _i32
    lib.bethkit_string_table_insert_new.argtypes = [
        _vp, ctypes.POINTER(_u8), _sz, ctypes.POINTER(_u32)
    ]

    lib.bethkit_string_table_remove.restype = _bl
    lib.bethkit_string_table_remove.argtypes = [_vp, _u32]

    lib.bethkit_string_table_write_to_file.restype = _i32
    lib.bethkit_string_table_write_to_file.argtypes = [_vp, _c]

    lib.bethkit_localization_set_new.restype = _vp
    lib.bethkit_localization_set_new.argtypes = []

    lib.bethkit_localization_set_open.restype = _vp
    lib.bethkit_localization_set_open.argtypes = [_c, _c]

    lib.bethkit_localization_set_free.restype = None
    lib.bethkit_localization_set_free.argtypes = [_vp]

    lib.bethkit_localization_set_get.restype = ctypes.POINTER(_u8)
    lib.bethkit_localization_set_get.argtypes = [
        _vp, _i32, _u32, ctypes.POINTER(_sz)
    ]

    lib.bethkit_localization_set_set.restype = _i32
    lib.bethkit_localization_set_set.argtypes = [
        _vp, _i32, _u32, ctypes.POINTER(_u8), _sz
    ]

    lib.bethkit_localization_set_write.restype = _i32
    lib.bethkit_localization_set_write.argtypes = [_vp, _c, _c]

    lib.bethkit_schema_registry_sse.restype = _vp
    lib.bethkit_schema_registry_sse.argtypes = []

    lib.bethkit_schema_registry_has.restype = _bl
    lib.bethkit_schema_registry_has.argtypes = [_vp, ctypes.POINTER(_u8)]

    lib.bethkit_record_view_new.restype = _vp
    lib.bethkit_record_view_new.argtypes = [_vp, ctypes.POINTER(_u8), _bl]

    lib.bethkit_record_view_free.restype = None
    lib.bethkit_record_view_free.argtypes = [_vp]

    lib.bethkit_record_view_field_count.restype = _sz
    lib.bethkit_record_view_field_count.argtypes = [_vp]

    lib.bethkit_record_view_field_get.restype = ctypes.POINTER(BethkitNamedField)
    lib.bethkit_record_view_field_get.argtypes = [_vp, _sz]

    lib.bethkit_field_entries_len.restype = _sz
    lib.bethkit_field_entries_len.argtypes = [_vp]

    lib.bethkit_field_entries_get.restype = ctypes.POINTER(BethkitNamedField)
    lib.bethkit_field_entries_get.argtypes = [_vp, _sz]

    lib.bethkit_field_entries_free.restype = None
    lib.bethkit_field_entries_free.argtypes = [_vp]

    lib.bethkit_field_values_len.restype = _sz
    lib.bethkit_field_values_len.argtypes = [_vp]

    lib.bethkit_field_values_get.restype = ctypes.POINTER(BethkitFieldValue)
    lib.bethkit_field_values_get.argtypes = [_vp, _sz]

    lib.bethkit_field_values_free.restype = None
    lib.bethkit_field_values_free.argtypes = [_vp]

    lib.bethkit_plugin_writer_new.restype = _vp
    lib.bethkit_plugin_writer_new.argtypes = [_i32, _f32]

    lib.bethkit_plugin_writer_free.restype = None
    lib.bethkit_plugin_writer_free.argtypes = [_vp]

    lib.bethkit_plugin_writer_add_group.restype = _i32
    lib.bethkit_plugin_writer_add_group.argtypes = [_vp, _vp]

    lib.bethkit_plugin_writer_write_to_file.restype = _i32
    lib.bethkit_plugin_writer_write_to_file.argtypes = [_vp, _c]

    lib.bethkit_plugin_writer_write_to_bytes.restype = ctypes.POINTER(_u8)
    lib.bethkit_plugin_writer_write_to_bytes.argtypes = [
        _vp, ctypes.POINTER(_sz)
    ]

    lib.bethkit_writable_group_new.restype = _vp
    lib.bethkit_writable_group_new.argtypes = [ctypes.POINTER(_u8), _i32]

    lib.bethkit_writable_group_free.restype = None
    lib.bethkit_writable_group_free.argtypes = [_vp]

    lib.bethkit_writable_group_add_record.restype = _i32
    lib.bethkit_writable_group_add_record.argtypes = [_vp, _vp]

    lib.bethkit_writable_group_add_group.restype = _i32
    lib.bethkit_writable_group_add_group.argtypes = [_vp, _vp]

    lib.bethkit_writable_record_new.restype = _vp
    lib.bethkit_writable_record_new.argtypes = [
        ctypes.POINTER(_u8), _u32, _u32, _u16
    ]

    lib.bethkit_writable_record_free.restype = None
    lib.bethkit_writable_record_free.argtypes = [_vp]

    lib.bethkit_writable_record_add_subrecord.restype = _i32
    lib.bethkit_writable_record_add_subrecord.argtypes = [
        _vp, ctypes.POINTER(_u8), ctypes.POINTER(_u8), _sz
    ]

