"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_native_error import BethkitNativeError


class BethkitNotFoundError(BethkitNativeError):
    """Raised by ``*_required`` convenience methods when a lookup fails.

    Normal lookup methods return ``None`` on not-found; this exception
    is raised only by the strict ``*_required`` variants that must
    succeed or fail loudly.
    """
