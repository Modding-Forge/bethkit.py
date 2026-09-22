"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure9078(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "COLL/3:Debug Color/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="COLL/3:Debug Color/payload/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="COLL/3:Debug Color/payload/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="COLL/3:Debug Color/payload/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="COLL/3:Debug Color/payload/3:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    red: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    green: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    blue: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["red"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["green"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["blue"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class TriggerVolumeSensorNavmeshObstacle9084(enum.IntFlag):
    """Named values from the pinned schema."""

    TRIGGER_VOLUME = 1
    SENSOR = 2
    NAVMESH_OBSTACLE = 4


class CollisionLayerRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "COLL"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "COLL"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="COLL/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "description": _base.Binding(
            path="COLL/1:Description",
            kind="subrecord",
            name="Description",
        ),
        "index": _base.Binding(
            path="COLL/2:Index",
            kind="subrecord",
            name="Index",
        ),
        "debug_color": _base.Binding(
            path="COLL/3:Debug Color",
            kind="subrecord",
            name="Debug Color",
        ),
        "flags": _base.Binding(
            path="COLL/4:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "name": _base.Binding(
            path="COLL/5:Name",
            kind="subrecord",
            name="Name",
        ),
        "interactables_count": _base.Binding(
            path="COLL/6:Interactables Count",
            kind="subrecord",
            name="Interactables Count",
        ),
        "collides_with": _base.Binding(
            path="COLL/7:Collides With",
            kind="subrecord",
            name="Collides With",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    debug_color: Optional[Structure9078] = None
    """Value decoded from this schema node."""

    flags: Optional[TriggerVolumeSensorNavmeshObstacle9084] = None
    """Value decoded from this schema node."""

    name: Optional[str] = None
    """Value decoded from this schema node."""

    interactables_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    collides_with: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["debug_color"]
    ) -> _base.FieldRef[Optional[Structure9078]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[TriggerVolumeSensorNavmeshObstacle9084]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["name"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["interactables_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["collides_with"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
