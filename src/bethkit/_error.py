"""
Copyright (c) Modding Forge
"""
from __future__ import annotations


class BethkitError(Exception):
    """
    Base exception for all bethkit errors.

    All exceptions raised by bethkit.py are subclasses of this class,
    so callers can catch everything with a single ``except BethkitError``.
    """


class BethkitLibraryNotFoundError(BethkitError):
    """
    Raised when the native bethkit shared library cannot be loaded.

    Check that ``bethkit_ffi.dll`` / ``libbethkit_ffi.so`` /
    ``libbethkit_ffi.dylib`` is placed next to the package directory or
    that the ``BETHKIT_LIB`` environment variable points to the file.
    """


class BethkitNativeError(BethkitError):
    """
    Raised when a native FFI call returns an error code.

    The error message is the text returned by ``bethkit_last_error()``
    immediately after the failing call, copied before any subsequent
    FFI call can overwrite the thread-local error buffer.

    Attributes:
        message (str): Human-readable error text from the native library.
    """

    message: str
    """Human-readable error text from the native library."""

    def __init__(self, message: str) -> None:
        """
        Args:
            message (str): Error text returned by the native library.
        """

        super().__init__(message)
        self.message = message

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation including the message.
        """

        return f"BethkitNativeError({self.message!r})"


class BethkitClosedError(BethkitError):
    """
    Raised when a method is called on an already-closed native handle.

    Once :meth:`close` has been called (or the context manager has
    exited), the wrapper object is invalid and must not be used.
    """


class BethkitOwnershipError(BethkitError):
    """
    Raised when ownership of a handle is transferred more than once.

    After a handle has been moved into a container (e.g.
    :meth:`~bethkit.PluginCache.add`), the original wrapper is consumed
    and must not be used again.
    """


class BethkitNotFoundError(BethkitNativeError):
    """
    Raised by ``*_required`` convenience methods when a lookup fails.

    Normal lookup methods return ``None`` on not-found; this exception
    is raised only by the strict ``*_required`` variants that must
    succeed or fail loudly.
    """
