"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes


def declare(lib: ctypes.CDLL) -> None:
    """Declares optional cursor APIs while retaining older-library fallback.

    Args:
        lib: Loaded native library receiving exact ownership declarations.
    """

    names = (
        "bethkit_string_cursor_new",
        "bethkit_string_cursor_next_json",
        "bethkit_string_cursor_free",
    )
    if hasattr(lib, "bethkit_semantic_context_new_for_plugin_preserving_text"):
        function = lib.bethkit_semantic_context_new_for_plugin_preserving_text
        function.restype = ctypes.c_void_p
        function.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p]
    if hasattr(lib, "bethkit_semantic_context_new_for_plugin_mixed"):
        lib.bethkit_semantic_context_new_for_plugin_mixed.restype = (
            ctypes.c_void_p
        )
        lib.bethkit_semantic_context_new_for_plugin_mixed.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_char_p,
        ]
    if not all(hasattr(lib, name) for name in names):
        return
    lib.bethkit_string_cursor_new.restype = ctypes.c_void_p
    lib.bethkit_string_cursor_new.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_bool,
    ]
    lib.bethkit_string_cursor_next_json.restype = ctypes.c_void_p
    lib.bethkit_string_cursor_next_json.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
    ]
    lib.bethkit_string_cursor_free.restype = None
    lib.bethkit_string_cursor_free.argtypes = [ctypes.c_void_p]
    if hasattr(lib, "bethkit_string_cursor_new_preserving_nontext"):
        lib.bethkit_string_cursor_new_preserving_nontext.restype = (
            ctypes.c_void_p
        )
        lib.bethkit_string_cursor_new_preserving_nontext.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
        ]
