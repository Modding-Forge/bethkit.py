"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import ClassVar

import pydantic

from ._binding import Binding
from ._field_reference import FieldReference


class StructModel(pydantic.BaseModel, frozen=True):
    """Base of generated, immutable payload and grammar models."""

    model_config = pydantic.ConfigDict(
        extra="forbid", protected_namespaces=("model_validate", "model_dump")
    )
    _schema_path: ClassVar[str] = ""
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, Binding]] = {}
    _references: dict[str, FieldReference] = pydantic.PrivateAttr(
        default_factory=dict
    )

    def field(self, name: str) -> FieldReference:
        """Returns an addressed field from a native snapshot.

        Args:
            name: Python attribute name from this generated model.

        Returns:
            The field reference; generated overloads retain its concrete type.

        Raises:
            KeyError: The name is unknown or the model was constructed manually.
        """

        return self._references[name]
