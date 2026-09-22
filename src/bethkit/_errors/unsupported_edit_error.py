"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_error import BethkitError


class UnsupportedEditError(BethkitError):
    """An edit cannot be performed without losing structural information."""
