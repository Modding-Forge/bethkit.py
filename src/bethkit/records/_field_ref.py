"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Generic, TypeVar

from ._field_reference import FieldReference

_T = TypeVar("_T")


class FieldRef(FieldReference, Generic[_T], frozen=True):
    """An immutable value paired with its exact, typed editing position."""

    value: _T
    """Decoded snapshot value; modifying it never modifies a plugin."""
