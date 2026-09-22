"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Type2902(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    RAIN = 0
    SNOW = 1


class Structure2892(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SPGD/1:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "gravity_velocity": _base.Binding(
            path="SPGD/1:Data/payload/0:Gravity Velocity",
            kind="primitive",
            name="Gravity Velocity",
        ),
        "rotation_velocity": _base.Binding(
            path="SPGD/1:Data/payload/1:Rotation Velocity",
            kind="primitive",
            name="Rotation Velocity",
        ),
        "particle_size_x": _base.Binding(
            path="SPGD/1:Data/payload/2:Particle Size X",
            kind="primitive",
            name="Particle Size X",
        ),
        "particle_size_y": _base.Binding(
            path="SPGD/1:Data/payload/3:Particle Size Y",
            kind="primitive",
            name="Particle Size Y",
        ),
        "center_offset_min": _base.Binding(
            path="SPGD/1:Data/payload/4:Center Offset Min",
            kind="primitive",
            name="Center Offset Min",
        ),
        "center_offset_max": _base.Binding(
            path="SPGD/1:Data/payload/5:Center Offset Max",
            kind="primitive",
            name="Center Offset Max",
        ),
        "initial_rotation_range": _base.Binding(
            path="SPGD/1:Data/payload/6:Initial Rotation Range",
            kind="primitive",
            name="Initial Rotation Range",
        ),
        "of_subtextures_x": _base.Binding(
            path="SPGD/1:Data/payload/7:# of Subtextures X",
            kind="primitive",
            name="# of Subtextures X",
        ),
        "of_subtextures_y": _base.Binding(
            path="SPGD/1:Data/payload/8:# of Subtextures Y",
            kind="primitive",
            name="# of Subtextures Y",
        ),
        "type": _base.Binding(
            path="SPGD/1:Data/payload/9:Type",
            kind="primitive",
            name="Type",
        ),
        "box_size": _base.Binding(
            path="SPGD/1:Data/payload/10:Box Size",
            kind="primitive",
            name="Box Size",
        ),
        "particle_density": _base.Binding(
            path="SPGD/1:Data/payload/11:Particle Density",
            kind="primitive",
            name="Particle Density",
        ),
    }

    gravity_velocity: float
    """Value decoded from this schema node."""

    rotation_velocity: float
    """Value decoded from this schema node."""

    particle_size_x: float
    """Value decoded from this schema node."""

    particle_size_y: float
    """Value decoded from this schema node."""

    center_offset_min: float
    """Value decoded from this schema node."""

    center_offset_max: float
    """Value decoded from this schema node."""

    initial_rotation_range: float
    """Value decoded from this schema node."""

    of_subtextures_x: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    of_subtextures_y: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    type: Type2902
    """Value decoded from this schema node."""

    box_size: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    particle_density: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["gravity_velocity"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotation_velocity"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["particle_size_x"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["particle_size_y"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["center_offset_min"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["center_offset_max"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["initial_rotation_range"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["of_subtextures_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["of_subtextures_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type2902]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["box_size"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_density"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ShaderParticleGeometryRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SPGD"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SPGD"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SPGD/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "data": _base.Binding(
            path="SPGD/1:Data",
            kind="subrecord",
            name="Data",
        ),
        "particle_texture": _base.Binding(
            path="SPGD/2:Particle Texture",
            kind="subrecord",
            name="Particle Texture",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    data: Optional[Structure2892] = None
    """Value decoded from this schema node."""

    particle_texture: Optional[str] = None
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
    ) -> _base.FieldRef[Optional[Structure2892]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
