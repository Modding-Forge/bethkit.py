"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_error import BethkitError


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
        """Stores the copied native diagnostic without further FFI calls.

        Args:
            message (str): Error text returned by the native library.
        """

        super().__init__(message)
        self.message = message

    def __repr__(self) -> str:
        """Returns the exception type and native diagnostic for debugging.

        Returns:
            str: Developer-friendly representation including the message.
        """

        return f"BethkitNativeError({self.message!r})"
