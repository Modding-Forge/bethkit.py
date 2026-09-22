"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class Value4170(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FLOAT = 102
    LONG = 108
    SHORT = 115


class GlobalValueRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "GLOB"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "GLOB"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="GLOB/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "type": _base.Binding(
            path="GLOB/1:Type",
            kind="subrecord",
            name="Type",
        ),
        "value": _base.Binding(
            path="GLOB/2:Value",
            kind="subrecord",
            name="Value",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    type: Optional[Value4170] = None
    """Value decoded from this schema node."""

    value: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["type"]
    ) -> _base.FieldRef[Optional[Value4170]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
