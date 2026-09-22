"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class Structure6603(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MATT/3:Havok Display Color/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="MATT/3:Havok Display Color/payload/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="MATT/3:Havok Display Color/payload/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="MATT/3:Havok Display Color/payload/2:Blue",
            kind="primitive",
            name="Blue",
        ),
    }

    red: float
    """Value decoded from this schema node."""

    green: float
    """Value decoded from this schema node."""

    blue: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["red"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["green"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["blue"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class StairMaterialArrowsStick6610(enum.IntFlag):
    """Named values from the pinned schema."""

    STAIR_MATERIAL = 1
    ARROWS_STICK = 2


class MaterialTypeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MATT"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "MATT"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="MATT/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "material_parent": _base.Binding(
            path="MATT/1:Material Parent",
            kind="subrecord",
            name="Material Parent",
        ),
        "material_name": _base.Binding(
            path="MATT/2:Material Name",
            kind="subrecord",
            name="Material Name",
        ),
        "havok_display_color": _base.Binding(
            path="MATT/3:Havok Display Color",
            kind="subrecord",
            name="Havok Display Color",
        ),
        "buoyancy": _base.Binding(
            path="MATT/4:Buoyancy",
            kind="subrecord",
            name="Buoyancy",
        ),
        "flags": _base.Binding(
            path="MATT/5:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "havok_impact_data_set": _base.Binding(
            path="MATT/6:Havok Impact Data Set",
            kind="subrecord",
            name="Havok Impact Data Set",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    material_parent: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    material_name: Optional[str] = None
    """Value decoded from this schema node."""

    havok_display_color: Optional[Structure6603] = None
    """Value decoded from this schema node."""

    buoyancy: Optional[float] = None
    """Value decoded from this schema node."""

    flags: Optional[StairMaterialArrowsStick6610] = None
    """Value decoded from this schema node."""

    havok_impact_data_set: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["material_parent"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["material_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["havok_display_color"]
    ) -> _base.FieldRef[Optional[Structure6603]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["buoyancy"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[StairMaterialArrowsStick6610]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["havok_impact_data_set"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
