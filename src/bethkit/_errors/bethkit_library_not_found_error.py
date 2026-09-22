"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_error import BethkitError


class BethkitLibraryNotFoundError(BethkitError):
    """
    Raised when the native bethkit shared library cannot be loaded.

    Check that ``bethkit_ffi.dll`` / ``libbethkit_ffi.so`` /
    ``libbethkit_ffi.dylib`` is placed next to the package directory or
    that the ``BETHKIT_LIB`` environment variable points to the file.
    """
