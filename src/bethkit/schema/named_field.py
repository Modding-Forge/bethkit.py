"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from .field_value import FieldValue


class NamedField(BaseModel, frozen=True):
    """A field with frozen attributes and compatibility-preserving payloads.

    Nested list values remain mutable. Use generated record models when deep
    immutable typed values are needed instead of this legacy generic view.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    """Schema-provided field label."""
    value: FieldValue
    """Generic decoded scalar or nested payload."""
