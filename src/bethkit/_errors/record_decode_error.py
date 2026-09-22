"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .bethkit_error import BethkitError


class RecordDecodeError(BethkitError):
    """A semantic snapshot cannot be represented by its generated model."""
