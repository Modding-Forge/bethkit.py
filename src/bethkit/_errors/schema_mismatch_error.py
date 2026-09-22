"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_error import BethkitError


class SchemaMismatchError(BethkitError):
    """Generated record types do not match the exact loaded schema."""
