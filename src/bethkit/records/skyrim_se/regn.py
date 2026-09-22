"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure15934(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REGN/1:Map Color/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="REGN/1:Map Color/payload/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="REGN/1:Map Color/payload/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="REGN/1:Map Color/payload/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unknown": _base.Binding(
            path="REGN/1:Map Color/payload/3:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    red: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    green: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    blue: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unknown: bytes
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
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Point15947(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/3:Region Areas/repeat/0:Region Area/1:Region Poin"
        "t List Data/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "REGN/3:Region Areas/repeat/0:Region Area/1:Region Poin"
                "t List Data/payload/element/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "REGN/3:Region Areas/repeat/0:Region Area/1:Region Poin"
                "t List Data/payload/element/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
    }

    x: float
    """Value decoded from this schema node."""

    y: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class RegionArea15942(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REGN/3:Region Areas/repeat/0:Region Area"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "edge_fall_off": _base.Binding(
            path=("REGN/3:Region Areas/repeat/0:Region Area/0:Edge Fall-off"),
            kind="subrecord",
            name="Edge Fall-off",
        ),
        "region_point_list_data": _base.Binding(
            path=(
                "REGN/3:Region Areas/repeat/0:Region Area/1:Region Poin"
                "t List Data"
            ),
            kind="subrecord",
            name="Region Point List Data",
        ),
    }

    edge_fall_off: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    region_point_list_data: Optional[tuple[Point15947, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["edge_fall_off"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["region_point_list_data"]
    ) -> _base.FieldRef[Optional[tuple[Point15947, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type15954(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    UNKNOWN_0 = 0
    UNKNOWN_1 = 1
    OBJECTS = 2
    WEATHER = 3
    MAP = 4
    LAND = 5
    GRASS = 6
    SOUND = 7
    IMPOSTER = 8
    UNKNOWN_10 = 9
    UNKNOWN_11 = 10
    UNKNOWN_12 = 11
    UNKNOWN_13 = 12
    UNKNOWN_14 = 13
    UNKNOWN_15 = 14
    UNKNOWN_16 = 15


class Flags15955(enum.IntFlag):
    """Named values from the pinned schema."""

    OVERRIDE = 1


class Structure15953(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
        "0:Data Header/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "0:Data Header/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "0:Data Header/payload/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "priority": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "0:Data Header/payload/2:Priority"
            ),
            kind="primitive",
            name="Priority",
        ),
        "unknown": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "0:Data Header/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    type: Type15954
    """Value decoded from this schema node."""

    flags: Flags15955
    """Value decoded from this schema node."""

    priority: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type15954]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15955]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["priority"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Icon15958(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry/1:Icon"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "large_icon_file_name": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "1:Icon/0:Large Icon FileName"
            ),
            kind="subrecord",
            name="Large Icon FileName",
        ),
        "small_icon_file_name": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "1:Icon/1:Small Icon FileName"
            ),
            kind="subrecord",
            name="Small Icon FileName",
        ),
    }

    large_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    small_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["large_icon_file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["small_icon_file_name"]
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


class Flags15969(enum.IntFlag):
    """Named values from the pinned schema."""

    PLEASANT = 1
    CLOUDY = 2
    RAINY = 4
    SNOWY = 8


class Sound15967(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
        "3:Sounds/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sound": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "3:Sounds/payload/element/0:Sound"
            ),
            kind="primitive",
            name="Sound",
        ),
        "flags": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "3:Sounds/payload/element/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "chance": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "3:Sounds/payload/element/2:Chance"
            ),
            kind="primitive",
            name="Chance",
        ),
    }

    sound: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags15969
    """Value decoded from this schema node."""

    chance: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sound"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15969]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["chance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags15983(enum.IntFlag):
    """Named values from the pinned schema."""

    CONFORM_TO_SLOPE = 1
    PAINT_VERTICES = 2
    SIZE_VARIANCE = 4
    X = 8
    Y = 16
    Z = 32
    TREE = 64
    HUGE_ROCK = 128


class AngleVariance15991(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
        "5:Objects/payload/element/15:Angle Variance"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/15:Angle Variance/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/15:Angle Variance/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/15:Angle Variance/2:Z"
            ),
            kind="primitive",
            name="Z",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    z: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
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


class Object15975(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
        "5:Objects/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "object": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/0:Object"
            ),
            kind="primitive",
            name="Object",
        ),
        "parent_index": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/1:Parent Index"
            ),
            kind="primitive",
            name="Parent Index",
        ),
        "unknown": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "density": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/3:Density"
            ),
            kind="primitive",
            name="Density",
        ),
        "clustering": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/4:Clustering"
            ),
            kind="primitive",
            name="Clustering",
        ),
        "min_slope": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/5:Min Slope"
            ),
            kind="primitive",
            name="Min Slope",
        ),
        "max_slope": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/6:Max Slope"
            ),
            kind="primitive",
            name="Max Slope",
        ),
        "flags": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/7:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "radius_wrt_parent": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/8:Radius wrt Parent"
            ),
            kind="primitive",
            name="Radius wrt Parent",
        ),
        "radius": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/9:Radius"
            ),
            kind="primitive",
            name="Radius",
        ),
        "min_height": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/10:Min Height"
            ),
            kind="primitive",
            name="Min Height",
        ),
        "max_height": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/11:Max Height"
            ),
            kind="primitive",
            name="Max Height",
        ),
        "sink": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/12:Sink"
            ),
            kind="primitive",
            name="Sink",
        ),
        "sink_variance": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/13:Sink Variance"
            ),
            kind="primitive",
            name="Sink Variance",
        ),
        "size_variance": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/14:Size Variance"
            ),
            kind="primitive",
            name="Size Variance",
        ),
        "angle_variance": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/15:Angle Variance"
            ),
            kind="struct",
            name="Angle Variance",
        ),
        "unknown_15995": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/16:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15996": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects/payload/element/17:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    object: _values.FormId
    """Value decoded from this schema node."""

    parent_index: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    density: float
    """Value decoded from this schema node."""

    clustering: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    min_slope: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    max_slope: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    flags: Flags15983
    """Value decoded from this schema node."""

    radius_wrt_parent: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=65535)
    ]
    """Value decoded from this schema node."""

    radius: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    min_height: float
    """Value decoded from this schema node."""

    max_height: float
    """Value decoded from this schema node."""

    sink: float
    """Value decoded from this schema node."""

    sink_variance: float
    """Value decoded from this schema node."""

    size_variance: float
    """Value decoded from this schema node."""

    angle_variance: AngleVariance15991
    """Value decoded from this schema node."""

    unknown_15995: bytes
    """Value decoded from this schema node."""

    unknown_15996: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["object"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parent_index"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["density"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["clustering"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["min_slope"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["max_slope"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15983]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radius_wrt_parent"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radius"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["min_height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sink"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sink_variance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["size_variance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["angle_variance"]
    ) -> _base.FieldRef[AngleVariance15991]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15995"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15996"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Grass15999(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
        "6:Grasses/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "grass": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "6:Grasses/payload/element/0:Grass"
            ),
            kind="primitive",
            name="Grass",
        ),
        "unknown": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "6:Grasses/payload/element/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    grass: _values.FormId
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["grass"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class WeatherType16004(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
        "7:Weather Types/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "weather": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "7:Weather Types/payload/element/0:Weather"
            ),
            kind="primitive",
            name="Weather",
        ),
        "chance": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "7:Weather Types/payload/element/1:Chance"
            ),
            kind="primitive",
            name="Chance",
        ),
        "global_value": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "7:Weather Types/payload/element/2:Global"
            ),
            kind="primitive",
            name="Global",
        ),
    }

    weather: _values.FormId
    """Value decoded from this schema node."""

    chance: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    global_value: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["weather"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["chance"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["global_value"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class RegionDataEntry15951(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REGN/4:Region Data Entries/repeat/0:Region Data Entry"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "data_header": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "0:Data Header"
            ),
            kind="subrecord",
            name="Data Header",
        ),
        "icon": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/1:Icon"
            ),
            kind="unordered",
            name="Icon",
        ),
        "music": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/2:Music"
            ),
            kind="subrecord",
            name="Music",
        ),
        "sounds": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/3:Sounds"
            ),
            kind="subrecord",
            name="Sounds",
        ),
        "map_name": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "4:Map Name"
            ),
            kind="subrecord",
            name="Map Name",
        ),
        "objects": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "5:Objects"
            ),
            kind="subrecord",
            name="Objects",
        ),
        "grasses": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "6:Grasses"
            ),
            kind="subrecord",
            name="Grasses",
        ),
        "weather_types": _base.Binding(
            path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry/"
                "7:Weather Types"
            ),
            kind="subrecord",
            name="Weather Types",
        ),
    }

    data_header: Optional[Structure15953] = None
    """Value decoded from this schema node."""

    icon: Optional[Icon15958] = None
    """Value decoded from this schema node."""

    music: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sounds: Optional[tuple[Sound15967, ...]] = None
    """Value decoded from this schema node."""

    map_name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    objects: Optional[tuple[Object15975, ...]] = None
    """Value decoded from this schema node."""

    grasses: Optional[tuple[Grass15999, ...]] = None
    """Value decoded from this schema node."""

    weather_types: Optional[tuple[WeatherType16004, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["data_header"]
    ) -> _base.FieldRef[Optional[Structure15953]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["icon"]
    ) -> _base.FieldRef[Optional[Icon15958]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["music"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sounds"]
    ) -> _base.FieldRef[Optional[tuple[Sound15967, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["map_name"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["objects"]
    ) -> _base.FieldRef[Optional[tuple[Object15975, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grasses"]
    ) -> _base.FieldRef[Optional[tuple[Grass15999, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["weather_types"]
    ) -> _base.FieldRef[Optional[tuple[WeatherType16004, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class RegionRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REGN"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "REGN"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="REGN/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "map_color": _base.Binding(
            path="REGN/1:Map Color",
            kind="subrecord",
            name="Map Color",
        ),
        "worldspace": _base.Binding(
            path="REGN/2:Worldspace",
            kind="subrecord",
            name="Worldspace",
        ),
        "region_areas": _base.Binding(
            path="REGN/3:Region Areas",
            kind="repeat",
            name="Region Areas",
            repeated_path="REGN/3:Region Areas/repeat/0:Region Area",
            child_kind="sequence",
        ),
        "region_data_entries": _base.Binding(
            path="REGN/4:Region Data Entries",
            kind="repeat",
            name="Region Data Entries",
            repeated_path=(
                "REGN/4:Region Data Entries/repeat/0:Region Data Entry"
            ),
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    map_color: Optional[Structure15934] = None
    """Value decoded from this schema node."""

    worldspace: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    region_areas: tuple[RegionArea15942, ...] = ()
    """Value decoded from this schema node."""

    region_data_entries: tuple[RegionDataEntry15951, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["map_color"]
    ) -> _base.FieldRef[Optional[Structure15934]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["worldspace"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["region_areas"]
    ) -> _base.FieldRef[tuple[RegionArea15942, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["region_data_entries"]
    ) -> _base.FieldRef[tuple[RegionDataEntry15951, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
