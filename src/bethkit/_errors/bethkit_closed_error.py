"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_error import BethkitError


class BethkitClosedError(BethkitError):
    """
    Raised when a method is called on an already-closed native handle.

    Once :meth:`close` has been called (or the context manager has
    exited), the wrapper object is invalid and must not be used.
    """
