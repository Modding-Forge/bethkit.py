"""
Copyright (c) Modding Forge
"""

from __future__ import annotations


class BethkitError(Exception):
    """
    Base exception for Bethkit-specific errors.

    Bethkit-specific exceptions derive from this class. Invalid Python inputs,
    text decoding, filesystem operations, and model validation can also raise
    their documented standard-library or Pydantic exceptions.
    """
