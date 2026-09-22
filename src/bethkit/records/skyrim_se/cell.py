"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class IsInteriorCellHasWaterCanTravelFromHeC8471C652665(enum.IntFlag):
    """Named values from the pinned schema."""

    IS_INTERIOR_CELL = 1
    HAS_WATER = 2
    CAN_TRAVEL_FROM_HERE = 4
    NO_LOD_WATER = 8
    UNKNOWN_5 = 16
    PUBLIC_AREA = 32
    HAND_CHANGED = 64
    SHOW_SKY = 128
    USE_SKY_LIGHTING = 256


class LandFlags2670(enum.IntFlag):
    """Named values from the pinned schema."""

    HIDE_QUAD_1 = 1
    HIDE_QUAD_2 = 2
    HIDE_QUAD_3 = 4
    HIDE_QUAD_4 = 8


class Structure2667(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/3:Grid/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="CELL/3:Grid/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="CELL/3:Grid/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
        "land_flags": _base.Binding(
            path="CELL/3:Grid/payload/2:Land Flags",
            kind="primitive",
            name="Land Flags",
        ),
        "unused": _base.Binding(
            path="CELL/3:Grid/payload/3:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    x: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    y: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    land_flags: Optional[LandFlags2670] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["land_flags"]
    ) -> _base.FieldRef[Optional[LandFlags2670]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class AmbientColor2674(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/4:Lighting/payload/0:Ambient Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="CELL/4:Lighting/payload/0:Ambient Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="CELL/4:Lighting/payload/0:Ambient Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="CELL/4:Lighting/payload/0:Ambient Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="CELL/4:Lighting/payload/0:Ambient Color/3:Unused",
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class DirectionalColor2679(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/4:Lighting/payload/1:Directional Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="CELL/4:Lighting/payload/1:Directional Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("CELL/4:Lighting/payload/1:Directional Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("CELL/4:Lighting/payload/1:Directional Color/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("CELL/4:Lighting/payload/1:Directional Color/3:Unused"),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FogColorNear2684(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/4:Lighting/payload/2:Fog Color Near"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="CELL/4:Lighting/payload/2:Fog Color Near/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="CELL/4:Lighting/payload/2:Fog Color Near/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="CELL/4:Lighting/payload/2:Fog Color Near/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="CELL/4:Lighting/payload/2:Fog Color Near/3:Unused",
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class X2698(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/0:X+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/0:X+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/0:X+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/0:X+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/0:X+/3:Unused"
            ),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class X2703(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/1:X-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/1:X-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/1:X-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/1:X-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/1:X-/3:Unused"
            ),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Y2708(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/2:Y+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/2:Y+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/2:Y+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/2:Y+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/2:Y+/3:Unused"
            ),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Y2713(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/3:Y-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/3:Y-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/3:Y-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/3:Y-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/3:Y-/3:Unused"
            ),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Z2718(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/4:Z+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/4:Z+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/4:Z+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/4:Z+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/4:Z+/3:Unused"
            ),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Z2723(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/5:Z-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/5:Z-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/5:Z-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/5:Z-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/5:Z-/3:Unused"
            ),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Directional2697(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/0:X+"
            ),
            kind="struct",
            name="X+",
        ),
        "x_2703": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/1:X-"
            ),
            kind="struct",
            name="X-",
        ),
        "y": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/2:Y+"
            ),
            kind="struct",
            name="Y+",
        ),
        "y_2713": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/3:Y-"
            ),
            kind="struct",
            name="Y-",
        ),
        "z": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/4:Z+"
            ),
            kind="struct",
            name="Z+",
        ),
        "z_2723": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/0:Directional/5:Z-"
            ),
            kind="struct",
            name="Z-",
        ),
    }

    x: X2698
    """Value decoded from this schema node."""

    x_2703: X2703
    """Value decoded from this schema node."""

    y: Y2708
    """Value decoded from this schema node."""

    y_2713: Y2713
    """Value decoded from this schema node."""

    z: Z2718
    """Value decoded from this schema node."""

    z_2723: Z2723
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[X2698]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["x_2703"]) -> _base.FieldRef[X2703]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Y2708]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y_2713"]) -> _base.FieldRef[Y2713]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Z2718]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z_2723"]) -> _base.FieldRef[Z2723]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Specular2728(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/4:Lighting/payload/10:Ambient Colors/1:Specular"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("CELL/4:Lighting/payload/10:Ambient Colors/1:Specular/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/1:Specular/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/1:Specular/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "CELL/4:Lighting/payload/10:Ambient Colors/1:Specular/3:Unused"
            ),
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class AmbientColors2696(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/4:Lighting/payload/10:Ambient Colors"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=("CELL/4:Lighting/payload/10:Ambient Colors/0:Directional"),
            kind="struct",
            name="Directional",
        ),
        "specular": _base.Binding(
            path=("CELL/4:Lighting/payload/10:Ambient Colors/1:Specular"),
            kind="struct",
            name="Specular",
        ),
        "scale": _base.Binding(
            path="CELL/4:Lighting/payload/10:Ambient Colors/2:Scale",
            kind="primitive",
            name="Scale",
        ),
    }

    directional: Directional2697
    """Value decoded from this schema node."""

    specular: Optional[Specular2728] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["directional"]
    ) -> _base.FieldRef[Directional2697]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular"]
    ) -> _base.FieldRef[Optional[Specular2728]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["scale"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FogColorFar2734(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/4:Lighting/payload/11:Fog Color Far"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="CELL/4:Lighting/payload/11:Fog Color Far/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="CELL/4:Lighting/payload/11:Fog Color Far/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="CELL/4:Lighting/payload/11:Fog Color Far/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="CELL/4:Lighting/payload/11:Fog Color Far/3:Unused",
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

    unused: bytes
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Inherits2742(enum.IntFlag):
    """Named values from the pinned schema."""

    AMBIENT_COLOR = 1
    DIRECTIONAL_COLOR = 2
    FOG_COLOR = 4
    FOG_NEAR = 8
    FOG_FAR = 16
    DIRECTIONAL_ROTATION = 32
    DIRECTIONAL_FADE = 64
    CLIP_DISTANCE = 128
    FOG_POWER = 256
    FOG_MAX = 512
    LIGHT_FADE_DISTANCES = 1024


class Structure2673(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/4:Lighting/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ambient_color": _base.Binding(
            path="CELL/4:Lighting/payload/0:Ambient Color",
            kind="struct",
            name="Ambient Color",
        ),
        "directional_color": _base.Binding(
            path="CELL/4:Lighting/payload/1:Directional Color",
            kind="struct",
            name="Directional Color",
        ),
        "fog_color_near": _base.Binding(
            path="CELL/4:Lighting/payload/2:Fog Color Near",
            kind="struct",
            name="Fog Color Near",
        ),
        "fog_near": _base.Binding(
            path="CELL/4:Lighting/payload/3:Fog Near",
            kind="primitive",
            name="Fog Near",
        ),
        "fog_far": _base.Binding(
            path="CELL/4:Lighting/payload/4:Fog Far",
            kind="primitive",
            name="Fog Far",
        ),
        "directional_rotation_xy": _base.Binding(
            path="CELL/4:Lighting/payload/5:Directional Rotation XY",
            kind="primitive",
            name="Directional Rotation XY",
        ),
        "directional_rotation_z": _base.Binding(
            path="CELL/4:Lighting/payload/6:Directional Rotation Z",
            kind="primitive",
            name="Directional Rotation Z",
        ),
        "directional_fade": _base.Binding(
            path="CELL/4:Lighting/payload/7:Directional Fade",
            kind="primitive",
            name="Directional Fade",
        ),
        "fog_clip_distance": _base.Binding(
            path="CELL/4:Lighting/payload/8:Fog Clip Distance",
            kind="primitive",
            name="Fog Clip Distance",
        ),
        "fog_power": _base.Binding(
            path="CELL/4:Lighting/payload/9:Fog Power",
            kind="primitive",
            name="Fog Power",
        ),
        "ambient_colors": _base.Binding(
            path="CELL/4:Lighting/payload/10:Ambient Colors",
            kind="optional_struct",
            name="Ambient Colors",
        ),
        "fog_color_far": _base.Binding(
            path="CELL/4:Lighting/payload/11:Fog Color Far",
            kind="struct",
            name="Fog Color Far",
        ),
        "fog_max": _base.Binding(
            path="CELL/4:Lighting/payload/12:Fog Max",
            kind="primitive",
            name="Fog Max",
        ),
        "light_fade_begin": _base.Binding(
            path="CELL/4:Lighting/payload/13:Light Fade Begin",
            kind="primitive",
            name="Light Fade Begin",
        ),
        "light_fade_end": _base.Binding(
            path="CELL/4:Lighting/payload/14:Light Fade End",
            kind="primitive",
            name="Light Fade End",
        ),
        "inherits": _base.Binding(
            path="CELL/4:Lighting/payload/15:Inherits",
            kind="primitive",
            name="Inherits",
        ),
    }

    ambient_color: AmbientColor2674
    """Value decoded from this schema node."""

    directional_color: DirectionalColor2679
    """Value decoded from this schema node."""

    fog_color_near: FogColorNear2684
    """Value decoded from this schema node."""

    fog_near: float
    """Value decoded from this schema node."""

    fog_far: float
    """Value decoded from this schema node."""

    directional_rotation_xy: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    directional_rotation_z: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    directional_fade: float
    """Value decoded from this schema node."""

    fog_clip_distance: float
    """Value decoded from this schema node."""

    fog_power: float
    """Value decoded from this schema node."""

    ambient_colors: AmbientColors2696
    """Value decoded from this schema node."""

    fog_color_far: Optional[FogColorFar2734] = None
    """Value decoded from this schema node."""

    fog_max: Optional[float] = None
    """Value decoded from this schema node."""

    light_fade_begin: Optional[float] = None
    """Value decoded from this schema node."""

    light_fade_end: Optional[float] = None
    """Value decoded from this schema node."""

    inherits: Optional[Inherits2742] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ambient_color"]
    ) -> _base.FieldRef[AmbientColor2674]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["directional_color"]
    ) -> _base.FieldRef[DirectionalColor2679]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_color_near"]
    ) -> _base.FieldRef[FogColorNear2684]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fog_near"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fog_far"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["directional_rotation_xy"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["directional_rotation_z"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["directional_fade"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_clip_distance"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fog_power"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ambient_colors"]
    ) -> _base.FieldRef[AmbientColors2696]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_color_far"]
    ) -> _base.FieldRef[Optional[FogColorFar2734]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_max"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["light_fade_begin"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["light_fade_end"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["inherits"]
    ) -> _base.FieldRef[Optional[Inherits2742]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure2746(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/6:Max Height Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "offset": _base.Binding(
            path="CELL/6:Max Height Data/payload/0:Offset",
            kind="primitive",
            name="Offset",
        ),
        "rows": _base.Binding(
            path="CELL/6:Max Height Data/payload/1:Rows",
            kind="array",
            name="Rows",
        ),
    }

    offset: float
    """Value decoded from this schema node."""

    rows: tuple[bytes, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["offset"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rows"]) -> _base.FieldRef[tuple[bytes, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class UnknownVelocity2770(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CELL/15:Water Currents/payload/element/0:Unknown Velocity"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "CELL/15:Water Currents/payload/element/0:Unknown Velocity/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "CELL/15:Water Currents/payload/element/0:Unknown Velocity/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "CELL/15:Water Currents/payload/element/0:Unknown Velocity/2:Z"
            ),
            kind="primitive",
            name="Z",
        ),
    }

    x: float
    """Value decoded from this schema node."""

    y: float
    """Value decoded from this schema node."""

    z: float
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
    def field(self, name: Literal["z"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class WaterVelocities2769(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/15:Water Currents/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown_velocity": _base.Binding(
            path=("CELL/15:Water Currents/payload/element/0:Unknown Velocity"),
            kind="struct",
            name="Unknown Velocity",
        ),
        "unknown": _base.Binding(
            path="CELL/15:Water Currents/payload/element/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    unknown_velocity: UnknownVelocity2770
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown_velocity"]
    ) -> _base.FieldRef[UnknownVelocity2770]:
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


class Ownership2777(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL/17:Ownership"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path="CELL/17:Ownership/0:Owner",
            kind="subrecord",
            name="Owner",
        ),
        "faction_rank": _base.Binding(
            path="CELL/17:Ownership/1:Faction rank",
            kind="subrecord",
            name="Faction rank",
        ),
    }

    owner: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    faction_rank: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["owner"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["faction_rank"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ]
        ]
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


class CellRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CELL"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "CELL"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="CELL/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="CELL/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "flags": _base.Binding(
            path="CELL/2:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "grid": _base.Binding(
            path="CELL/3:Grid",
            kind="subrecord",
            name="Grid",
        ),
        "lighting": _base.Binding(
            path="CELL/4:Lighting",
            kind="subrecord",
            name="Lighting",
        ),
        "occlusion_data": _base.Binding(
            path="CELL/5:Occlusion Data",
            kind="subrecord",
            name="Occlusion Data",
        ),
        "max_height_data": _base.Binding(
            path="CELL/6:Max Height Data",
            kind="subrecord",
            name="Max Height Data",
        ),
        "lighting_template": _base.Binding(
            path="CELL/7:Lighting Template",
            kind="subrecord",
            name="Lighting Template",
        ),
        "unknown": _base.Binding(
            path="CELL/8:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "water_height": _base.Binding(
            path="CELL/9:Water Height",
            kind="subrecord",
            name="Water Height",
        ),
        "water_noise_texture": _base.Binding(
            path="CELL/10:Water Noise Texture",
            kind="subrecord",
            name="Water Noise Texture",
        ),
        "regions": _base.Binding(
            path="CELL/11:Regions",
            kind="subrecord",
            name="Regions",
        ),
        "location": _base.Binding(
            path="CELL/12:Location",
            kind="subrecord",
            name="Location",
        ),
        "water_current_count": _base.Binding(
            path="CELL/13:Water Current Count",
            kind="subrecord",
            name="Water Current Count",
        ),
        "water_current_count_old": _base.Binding(
            path="CELL/14:Water Current Count (Old)",
            kind="subrecord",
            name="Water Current Count (Old)",
        ),
        "water_currents": _base.Binding(
            path="CELL/15:Water Currents",
            kind="subrecord",
            name="Water Currents",
        ),
        "water": _base.Binding(
            path="CELL/16:Water",
            kind="subrecord",
            name="Water",
        ),
        "ownership": _base.Binding(
            path="CELL/17:Ownership",
            kind="sequence",
            name="Ownership",
        ),
        "lock_list": _base.Binding(
            path="CELL/18:Lock List",
            kind="subrecord",
            name="Lock List",
        ),
        "water_environment_map": _base.Binding(
            path="CELL/19:Water Environment Map",
            kind="subrecord",
            name="Water Environment Map",
        ),
        "sky_weather_from_region": _base.Binding(
            path="CELL/20:Sky/Weather from Region",
            kind="subrecord",
            name="Sky/Weather from Region",
        ),
        "acoustic_space": _base.Binding(
            path="CELL/21:Acoustic Space",
            kind="subrecord",
            name="Acoustic Space",
        ),
        "encounter_zone": _base.Binding(
            path="CELL/22:Encounter Zone",
            kind="subrecord",
            name="Encounter Zone",
        ),
        "music_type": _base.Binding(
            path="CELL/23:Music Type",
            kind="subrecord",
            name="Music Type",
        ),
        "image_space": _base.Binding(
            path="CELL/24:Image Space",
            kind="subrecord",
            name="Image Space",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    flags: Optional[IsInteriorCellHasWaterCanTravelFromHeC8471C652665] = None
    """Value decoded from this schema node."""

    grid: Optional[Structure2667] = None
    """Value decoded from this schema node."""

    lighting: Optional[Structure2673] = None
    """Value decoded from this schema node."""

    occlusion_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    max_height_data: Optional[Structure2746] = None
    """Value decoded from this schema node."""

    lighting_template: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    water_height: Optional[float] = None
    """Value decoded from this schema node."""

    water_noise_texture: Optional[str] = None
    """Value decoded from this schema node."""

    regions: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    location: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    water_current_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    water_current_count_old: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    water_currents: Optional[tuple[WaterVelocities2769, ...]] = None
    """Value decoded from this schema node."""

    water: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ownership: Optional[Ownership2777] = None
    """Value decoded from this schema node."""

    lock_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    water_environment_map: Optional[str] = None
    """Value decoded from this schema node."""

    sky_weather_from_region: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    acoustic_space: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    encounter_zone: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    music_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    image_space: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["name"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[IsInteriorCellHasWaterCanTravelFromHeC8471C652665]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid"]
    ) -> _base.FieldRef[Optional[Structure2667]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lighting"]
    ) -> _base.FieldRef[Optional[Structure2673]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["occlusion_data"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["max_height_data"]
    ) -> _base.FieldRef[Optional[Structure2746]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lighting_template"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_height"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_noise_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["regions"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_count_old"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_currents"]
    ) -> _base.FieldRef[Optional[tuple[WaterVelocities2769, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ownership"]
    ) -> _base.FieldRef[Optional[Ownership2777]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lock_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_environment_map"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sky_weather_from_region"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["acoustic_space"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["encounter_zone"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["music_type"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["image_space"]
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
