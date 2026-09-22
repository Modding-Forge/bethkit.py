"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class FootstepRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FSTP"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "FSTP"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="FSTP/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "impact_data_set": _base.Binding(
            path="FSTP/1:Impact Data Set",
            kind="subrecord",
            name="Impact Data Set",
        ),
        "tag": _base.Binding(
            path="FSTP/2:Tag",
            kind="subrecord",
            name="Tag",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    impact_data_set: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    tag: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["impact_data_set"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["tag"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
