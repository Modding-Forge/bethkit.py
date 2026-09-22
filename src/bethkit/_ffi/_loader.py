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
from typing import Optional

from . import (
    _declare_archive,
    _declare_core,
    _declare_load_order,
    _declare_plugin,
    _declare_schema,
    _declare_strings,
)

_lib: Optional[ctypes.CDLL] = None
_lib_lock: threading.Lock = threading.Lock()


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
            be found or loaded, or lacks the required ABI and symbols.
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
            try:
                loaded.bethkit_abi_version.restype = ctypes.c_uint32
                loaded.bethkit_abi_version.argtypes = []
                abi_version = int(loaded.bethkit_abi_version())
            except AttributeError as exc:
                raise BethkitLibraryNotFoundError(
                    f"Native library '{path}' predates ABI 2. "
                    "Replace the bundled library or set BETHKIT_LIB."
                ) from exc
            if abi_version != 2:
                raise BethkitLibraryNotFoundError(
                    f"bethkit native ABI {abi_version} is incompatible; "
                    "ABI 2 is required."
                )
            try:
                _declare(loaded)
            except AttributeError as exc:
                raise BethkitLibraryNotFoundError(
                    f"Native library '{path}' lacks a required API: {exc}. "
                    "Use the native revision pinned by this Python package."
                ) from exc
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

    msg: Optional[bytes] = lib.bethkit_last_error()
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

    Raises:
        UnicodeDecodeError: The buffer is not UTF-8; it is still freed.
    """

    try:
        return ctypes.string_at(ptr).decode("utf-8")
    finally:
        free_fn(ptr)


def enc(s: Path) -> bytes:
    """
    Encode a filesystem path for a NUL-terminated native argument.

    Args:
        s (Path): Filesystem path to encode.

    Returns:
        bytes: UTF-8 encoded path bytes.

    Raises:
        ValueError: The path contains a NUL character.
        UnicodeEncodeError: The path contains an unpaired surrogate.
    """

    return senc(str(s))


def senc(s: str) -> bytes:
    """
    Encode a plain string to a NUL-compatible UTF-8 bytes object.

    Args:
        s (str): String to encode.

    Returns:
        bytes: UTF-8 encoded bytes.

    Raises:
        ValueError: The string contains a NUL character.
        UnicodeEncodeError: The string contains an unpaired surrogate.
    """

    if "\x00" in s:
        raise ValueError("Native strings cannot contain NUL characters.")
    return s.encode("utf-8")


def _declare(lib: ctypes.CDLL) -> None:
    """Declares every required ABI symbol before publishing the singleton.

    Args:
        lib: Loaded native library using the required ABI version.

    Raises:
        AttributeError: If any required ABI symbol is unavailable.
    """

    _declare_core.declare(lib)
    _declare_plugin.declare(lib)
    _declare_archive.declare(lib)
    _declare_strings.declare(lib)
    _declare_schema.declare(lib)
    _declare_load_order.declare(lib)
