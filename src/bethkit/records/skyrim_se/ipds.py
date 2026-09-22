"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class Structure6705(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IPDS/1:Data/repeat/0:PNAM/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "material": _base.Binding(
            path="IPDS/1:Data/repeat/0:PNAM/payload/0:Material",
            kind="primitive",
            name="Material",
        ),
        "impact": _base.Binding(
            path="IPDS/1:Data/repeat/0:PNAM/payload/1:Impact",
            kind="primitive",
            name="Impact",
        ),
    }

    material: _values.FormId
    """Value decoded from this schema node."""

    impact: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["material"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["impact"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ImpactDataSetRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IPDS"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "IPDS"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="IPDS/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "data": _base.Binding(
            path="IPDS/1:Data",
            kind="repeat",
            name="Data",
            repeated_path="IPDS/1:Data/repeat/0:PNAM",
            child_kind="subrecord",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    data: tuple[Structure6705, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[tuple[Structure6705, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
