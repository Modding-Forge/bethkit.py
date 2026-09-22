"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_error import BethkitError


class BethkitOwnershipError(BethkitError):
    """
    Raised when ownership of a handle is transferred more than once.

    After a handle has been moved into a container (e.g.
    :meth:`~bethkit.PluginCache.add`), the original wrapper is consumed
    and must not be used again.
    """
