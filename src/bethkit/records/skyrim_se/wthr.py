"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class CloudSpeed17634(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/38:Cloud Speed"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "y_speed": _base.Binding(
            path="WTHR/38:Cloud Speed/0:Y Speed",
            kind="subrecord",
            name="Y Speed",
        ),
        "x_speed": _base.Binding(
            path="WTHR/38:Cloud Speed/1:X Speed",
            kind="subrecord",
            name="X Speed",
        ),
    }

    y_speed: Optional[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    ] = None
    """Value decoded from this schema node."""

    x_speed: Optional[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["y_speed"]
    ) -> _base.FieldRef[
        Optional[
            tuple[
                Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...
            ]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["x_speed"]
    ) -> _base.FieldRef[
        Optional[
            tuple[
                Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...
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


class Sunrise17644(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/39:Cloud Colors/payload/element/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/0:Sunrise/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/0:Sunrise/3:Unused"),
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


class Day17649(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/39:Cloud Colors/payload/element/1:Day"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="WTHR/39:Cloud Colors/payload/element/1:Day/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="WTHR/39:Cloud Colors/payload/element/1:Day/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/1:Day/3:Unused"),
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


class Sunset17654(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/39:Cloud Colors/payload/element/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/2:Sunset/3:Unused"),
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


class Night17659(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/39:Cloud Colors/payload/element/3:Night"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/39:Cloud Colors/payload/element/3:Night/3:Unused"),
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


class Layer17643(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/39:Cloud Colors/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path="WTHR/39:Cloud Colors/payload/element/0:Sunrise",
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/39:Cloud Colors/payload/element/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/39:Cloud Colors/payload/element/2:Sunset",
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/39:Cloud Colors/payload/element/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17644
    """Value decoded from this schema node."""

    day: Day17649
    """Value decoded from this schema node."""

    sunset: Sunset17654
    """Value decoded from this schema node."""

    night: Night17659
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17644]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17649]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17654]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17659]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Layer17666(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/40:Cloud Alphas/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path="WTHR/40:Cloud Alphas/payload/element/0:Sunrise",
            kind="primitive",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/40:Cloud Alphas/payload/element/1:Day",
            kind="primitive",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/40:Cloud Alphas/payload/element/2:Sunset",
            kind="primitive",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/40:Cloud Alphas/payload/element/3:Night",
            kind="primitive",
            name="Night",
        ),
    }

    sunrise: float
    """Value decoded from this schema node."""

    day: float
    """Value decoded from this schema node."""

    sunset: float
    """Value decoded from this schema node."""

    night: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17674(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/0:Sky-Upper/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/0:Sky-Upper/0:Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/0:Sky-Upper/0:Sunrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/0:Sky-Upper/0:Sunrise/3:Unused"
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


class Day17679(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/0:Sky-Upper/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/1:Day/3:Unused"),
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


class Sunset17684(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/0:Sky-Upper/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/0:Sky-Upper/2:Sunset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/0:Sky-Upper/2:Sunset/3:Unused"
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


class Night17689(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/0:Sky-Upper/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/0:Sky-Upper/3:Night/3:Unused"
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


class SkyUpper17673(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/0:Sky-Upper"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/0:Sky-Upper/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/0:Sky-Upper/3:Night"),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17674
    """Value decoded from this schema node."""

    day: Day17679
    """Value decoded from this schema node."""

    sunset: Sunset17684
    """Value decoded from this schema node."""

    night: Night17689
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17674]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17679]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17684]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17689]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17695(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/1:Fog Near/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/1:Fog Near/0:Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/1:Fog Near/0:Sunrise/3:Unused"
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


class Day17700(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/1:Fog Near/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/1:Day/3:Unused"),
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


class Sunset17705(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/1:Fog Near/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/1:Fog Near/2:Sunset/3:Unused"
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


class Night17710(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/1:Fog Near/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/3:Night/3:Unused"),
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


class FogNear17694(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/1:Fog Near"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/1:Fog Near/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/1:Fog Near/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/1:Fog Near/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17695
    """Value decoded from this schema node."""

    day: Day17700
    """Value decoded from this schema node."""

    sunset: Sunset17705
    """Value decoded from this schema node."""

    night: Night17710
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17695]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17700]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17705]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17710]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17716(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/2:Unknown/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/0:Sunrise/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/2:Unknown/0:Sunrise/3:Unused"
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


class Day17721(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/2:Unknown/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/1:Day/3:Unused"),
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


class Sunset17726(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/2:Unknown/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/2:Sunset/3:Unused"),
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


class Night17731(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/2:Unknown/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/3:Night/3:Unused"),
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


class Unknown17715(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/2:Unknown"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/2:Unknown/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/2:Unknown/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/41:Weather Colors/payload/2:Unknown/2:Sunset",
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/2:Unknown/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17716
    """Value decoded from this schema node."""

    day: Day17721
    """Value decoded from this schema node."""

    sunset: Sunset17726
    """Value decoded from this schema node."""

    night: Night17731
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17716]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17721]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17726]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17731]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17737(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/3:Ambient/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/0:Sunrise/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/3:Ambient/0:Sunrise/3:Unused"
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


class Day17742(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/3:Ambient/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/1:Day/3:Unused"),
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


class Sunset17747(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/3:Ambient/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/2:Sunset/3:Unused"),
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


class Night17752(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/3:Ambient/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/3:Night/3:Unused"),
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


class Ambient17736(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/3:Ambient"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/3:Ambient/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/3:Ambient/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/41:Weather Colors/payload/3:Ambient/2:Sunset",
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/3:Ambient/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17737
    """Value decoded from this schema node."""

    day: Day17742
    """Value decoded from this schema node."""

    sunset: Sunset17747
    """Value decoded from this schema node."""

    night: Night17752
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17737]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17742]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17747]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17752]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17758(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/4:Sunlight/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/4:Sunlight/0:Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/4:Sunlight/0:Sunrise/3:Unused"
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


class Day17763(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/4:Sunlight/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/1:Day/3:Unused"),
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


class Sunset17768(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/4:Sunlight/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/4:Sunlight/2:Sunset/3:Unused"
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


class Night17773(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/4:Sunlight/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/3:Night/3:Unused"),
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


class Sunlight17757(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/4:Sunlight"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/4:Sunlight/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/4:Sunlight/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/4:Sunlight/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17758
    """Value decoded from this schema node."""

    day: Day17763
    """Value decoded from this schema node."""

    sunset: Sunset17768
    """Value decoded from this schema node."""

    night: Night17773
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17758]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17763]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17768]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17773]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17779(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/5:Sun/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/0:Sunrise/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/0:Sunrise/3:Unused"),
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


class Day17784(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/5:Sun/1:Day"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="WTHR/41:Weather Colors/payload/5:Sun/1:Day/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="WTHR/41:Weather Colors/payload/5:Sun/1:Day/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/1:Day/3:Unused"),
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


class Sunset17789(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/5:Sun/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/2:Sunset/3:Unused"),
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


class Night17794(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/5:Sun/3:Night"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/5:Sun/3:Night/3:Unused"),
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


class Sun17778(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/5:Sun"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path="WTHR/41:Weather Colors/payload/5:Sun/0:Sunrise",
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/5:Sun/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/41:Weather Colors/payload/5:Sun/2:Sunset",
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/5:Sun/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17779
    """Value decoded from this schema node."""

    day: Day17784
    """Value decoded from this schema node."""

    sunset: Sunset17789
    """Value decoded from this schema node."""

    night: Night17794
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17779]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17784]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17789]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17794]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17800(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/6:Stars/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/0:Sunrise/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/0:Sunrise/3:Unused"),
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


class Day17805(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/6:Stars/1:Day"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/1:Day/3:Unused"),
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


class Sunset17810(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/6:Stars/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/2:Sunset/3:Unused"),
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


class Night17815(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/6:Stars/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/6:Stars/3:Night/3:Unused"),
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


class Stars17799(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/6:Stars"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path="WTHR/41:Weather Colors/payload/6:Stars/0:Sunrise",
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/6:Stars/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/41:Weather Colors/payload/6:Stars/2:Sunset",
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/6:Stars/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17800
    """Value decoded from this schema node."""

    day: Day17805
    """Value decoded from this schema node."""

    sunset: Sunset17810
    """Value decoded from this schema node."""

    night: Night17815
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17800]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17805]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17810]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17815]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17821(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/7:Sky-Lower/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/7:Sky-Lower/0:Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/7:Sky-Lower/0:Sunrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/7:Sky-Lower/0:Sunrise/3:Unused"
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


class Day17826(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/7:Sky-Lower/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/1:Day/3:Unused"),
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


class Sunset17831(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/7:Sky-Lower/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/7:Sky-Lower/2:Sunset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/7:Sky-Lower/2:Sunset/3:Unused"
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


class Night17836(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/7:Sky-Lower/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/7:Sky-Lower/3:Night/3:Unused"
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


class SkyLower17820(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/7:Sky-Lower"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/7:Sky-Lower/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/7:Sky-Lower/3:Night"),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17821
    """Value decoded from this schema node."""

    day: Day17826
    """Value decoded from this schema node."""

    sunset: Sunset17831
    """Value decoded from this schema node."""

    night: Night17836
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17821]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17826]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17831]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17836]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17842(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/8:Horizon/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/0:Sunrise/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/8:Horizon/0:Sunrise/3:Unused"
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


class Day17847(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/8:Horizon/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/1:Day/3:Unused"),
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


class Sunset17852(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/8:Horizon/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/2:Sunset/3:Unused"),
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


class Night17857(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/8:Horizon/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/3:Night/3:Unused"),
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


class Horizon17841(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/8:Horizon"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/8:Horizon/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/8:Horizon/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/41:Weather Colors/payload/8:Horizon/2:Sunset",
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/8:Horizon/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17842
    """Value decoded from this schema node."""

    day: Day17847
    """Value decoded from this schema node."""

    sunset: Sunset17852
    """Value decoded from this schema node."""

    night: Night17857
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17842]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17847]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17852]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17857]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17863(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/9:Effect Lighting/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/0:Sun"
                "rise/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/0:Sun"
                "rise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/0:Sun"
                "rise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/0:Sun"
                "rise/3:Unused"
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


class Day17868(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/9:Effect Lighting/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/1:Day/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/1:Day/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/1:Day/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/1:Day"
                "/3:Unused"
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


class Sunset17873(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/9:Effect Lighting/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/2:Sun"
                "set/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/2:Sun"
                "set/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/2:Sun"
                "set/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/2:Sun"
                "set/3:Unused"
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


class Night17878(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/9:Effect Lighting/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/3:Night/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/3:Nig"
                "ht/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/3:Nig"
                "ht/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/9:Effect Lighting/3:Nig"
                "ht/3:Unused"
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


class EffectLighting17862(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/9:Effect Lighting"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/9:Effect Lighting/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/9:Effect Lighting/1:Day"),
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/9:Effect Lighting/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/9:Effect Lighting/3:Night"),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17863
    """Value decoded from this schema node."""

    day: Day17868
    """Value decoded from this schema node."""

    sunset: Sunset17873
    """Value decoded from this schema node."""

    night: Night17878
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17863]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17868]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17873]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17878]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17884(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/0:"
                "Sunrise/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/0:"
                "Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/0:"
                "Sunrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/0:"
                "Sunrise/3:Unused"
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


class Day17889(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/1:"
                "Day/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/1:"
                "Day/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/1:"
                "Day/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/1:"
                "Day/3:Unused"
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


class Sunset17894(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/2:"
                "Sunset/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/2:"
                "Sunset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/2:"
                "Sunset/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/2:"
                "Sunset/3:Unused"
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


class Night17899(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/3:"
                "Night/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/3:"
                "Night/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/3:"
                "Night/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/3:"
                "Night/3:Unused"
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


class CloudLodDiffuse17883(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/0:Sunrise"
            ),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/1:Day"),
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/2:Sunset"
            ),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse/3:Night"
            ),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17884
    """Value decoded from this schema node."""

    day: Day17889
    """Value decoded from this schema node."""

    sunset: Sunset17894
    """Value decoded from this schema node."""

    night: Night17899
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17884]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17889]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17894]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17899]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17905(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/0:"
                "Sunrise/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/0:"
                "Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/0:"
                "Sunrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/0:"
                "Sunrise/3:Unused"
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


class Day17910(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/1:"
                "Day/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/1:"
                "Day/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/1:"
                "Day/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/1:"
                "Day/3:Unused"
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


class Sunset17915(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/2:"
                "Sunset/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/2:"
                "Sunset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/2:"
                "Sunset/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/2:"
                "Sunset/3:Unused"
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


class Night17920(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/3:"
                "Night/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/3:"
                "Night/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/3:"
                "Night/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/3:"
                "Night/3:Unused"
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


class CloudLodAmbient17904(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/0:Sunrise"
            ),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/1:Day"),
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/2:Sunset"
            ),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient/3:Night"
            ),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17905
    """Value decoded from this schema node."""

    day: Day17910
    """Value decoded from this schema node."""

    sunset: Sunset17915
    """Value decoded from this schema node."""

    night: Night17920
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17905]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17910]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17915]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17920]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17926(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/12:Fog Far/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/0:Sunrise/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/12:Fog Far/0:Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/0:Sunrise/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/12:Fog Far/0:Sunrise/3:Unused"
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


class Day17931(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/12:Fog Far/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/1:Day/3:Unused"),
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


class Sunset17936(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/12:Fog Far/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/2:Sunset/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/2:Sunset/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/12:Fog Far/2:Sunset/3:Unused"
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


class Night17941(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/12:Fog Far/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/3:Night/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/3:Night/3:Unused"),
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


class FogFar17925(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/12:Fog Far"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/12:Fog Far/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/12:Fog Far/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/41:Weather Colors/payload/12:Fog Far/3:Night",
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17926
    """Value decoded from this schema node."""

    day: Day17931
    """Value decoded from this schema node."""

    sunset: Sunset17936
    """Value decoded from this schema node."""

    night: Night17941
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17926]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17931]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17936]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17941]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17947(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/13:Sky Statics/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/0:Sunrise/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/0:Sunris"
                "e/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/0:Sunrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/0:Sunris"
                "e/3:Unused"
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


class Day17952(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/13:Sky Statics/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/13:Sky Statics/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/1:Day/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/13:Sky Statics/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/1:Day/3:Unused"
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


class Sunset17957(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/13:Sky Statics/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/2:Sunset/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/2:Sunset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/2:Sunset/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/2:Sunset"
                "/3:Unused"
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


class Night17962(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/13:Sky Statics/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/3:Night/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/3:Night/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/3:Night/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/13:Sky Statics/3:Night/3:Unused"
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


class SkyStatics17946(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/13:Sky Statics"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/13:Sky Statics/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/13:Sky Statics/1:Day"),
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/13:Sky Statics/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/13:Sky Statics/3:Night"),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17947
    """Value decoded from this schema node."""

    day: Day17952
    """Value decoded from this schema node."""

    sunset: Sunset17957
    """Value decoded from this schema node."""

    night: Night17962
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17947]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17952]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17957]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17962]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17968(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/14:Water Multiplier/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/0:S"
                "unrise/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/0:S"
                "unrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/0:S"
                "unrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/0:S"
                "unrise/3:Unused"
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


class Day17973(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/14:Water Multiplier/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/1:Day/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/1:D"
                "ay/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/1:D"
                "ay/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/1:D"
                "ay/3:Unused"
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


class Sunset17978(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/14:Water Multiplier/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/2:S"
                "unset/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/2:S"
                "unset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/2:S"
                "unset/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/2:S"
                "unset/3:Unused"
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


class Night17983(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/14:Water Multiplier/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/3:N"
                "ight/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/3:N"
                "ight/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/3:N"
                "ight/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/3:N"
                "ight/3:Unused"
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


class WaterMultiplier17967(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/14:Water Multiplier"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/0:Sunrise"
            ),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/14:Water Multiplier/1:Day"),
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/14:Water Multiplier/2:Sunset"
            ),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/14:Water Multiplier/3:Night"),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17968
    """Value decoded from this schema node."""

    day: Day17973
    """Value decoded from this schema node."""

    sunset: Sunset17978
    """Value decoded from this schema node."""

    night: Night17983
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17968]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17973]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17978]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night17983]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise17989(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/15:Sun Glare/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/0:Sunrise/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/0:Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/0:Sunrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/0:Sunrise/3:Unused"
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


class Day17994(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/15:Sun Glare/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/1:Day/3:Unused"),
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


class Sunset17999(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/15:Sun Glare/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/2:Sunset/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/2:Sunset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/2:Sunset/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/2:Sunset/3:Unused"
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


class Night18004(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/15:Sun Glare/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/3:Night/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/3:Night/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/15:Sun Glare/3:Night/3:Unused"
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


class SunGlare17988(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/15:Sun Glare"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/41:Weather Colors/payload/15:Sun Glare/1:Day",
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/15:Sun Glare/3:Night"),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise17989
    """Value decoded from this schema node."""

    day: Day17994
    """Value decoded from this schema node."""

    sunset: Sunset17999
    """Value decoded from this schema node."""

    night: Night18004
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise17989]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day17994]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset17999]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night18004]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sunrise18010(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/16:Moon Glare/0:Sunrise"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/0:Sunrise/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/0:Sunrise/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/0:Sunrise/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/0:Sunrise"
                "/3:Unused"
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


class Day18015(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/16:Moon Glare/1:Day"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/1:Day/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/1:Day/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/1:Day/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/1:Day/3:Unused"
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


class Sunset18020(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/16:Moon Glare/2:Sunset"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/2:Sunset/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/2:Sunset/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/2:Sunset/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/2:Sunset/3:Unused"
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


class Night18025(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/41:Weather Colors/payload/16:Moon Glare/3:Night"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/3:Night/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/3:Night/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/3:Night/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/41:Weather Colors/payload/16:Moon Glare/3:Night/3:Unused"
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


class MoonGlare18009(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload/16:Moon Glare"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/0:Sunrise"),
            kind="struct",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/1:Day"),
            kind="struct",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/2:Sunset"),
            kind="struct",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/16:Moon Glare/3:Night"),
            kind="struct",
            name="Night",
        ),
    }

    sunrise: Sunrise18010
    """Value decoded from this schema node."""

    day: Day18015
    """Value decoded from this schema node."""

    sunset: Sunset18020
    """Value decoded from this schema node."""

    night: Night18025
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[Sunrise18010]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[Day18015]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[Sunset18020]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[Night18025]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17672(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/41:Weather Colors/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sky_upper": _base.Binding(
            path="WTHR/41:Weather Colors/payload/0:Sky-Upper",
            kind="struct",
            name="Sky-Upper",
        ),
        "fog_near": _base.Binding(
            path="WTHR/41:Weather Colors/payload/1:Fog Near",
            kind="struct",
            name="Fog Near",
        ),
        "unknown": _base.Binding(
            path="WTHR/41:Weather Colors/payload/2:Unknown",
            kind="struct",
            name="Unknown",
        ),
        "ambient": _base.Binding(
            path="WTHR/41:Weather Colors/payload/3:Ambient",
            kind="struct",
            name="Ambient",
        ),
        "sunlight": _base.Binding(
            path="WTHR/41:Weather Colors/payload/4:Sunlight",
            kind="struct",
            name="Sunlight",
        ),
        "sun": _base.Binding(
            path="WTHR/41:Weather Colors/payload/5:Sun",
            kind="struct",
            name="Sun",
        ),
        "stars": _base.Binding(
            path="WTHR/41:Weather Colors/payload/6:Stars",
            kind="struct",
            name="Stars",
        ),
        "sky_lower": _base.Binding(
            path="WTHR/41:Weather Colors/payload/7:Sky-Lower",
            kind="struct",
            name="Sky-Lower",
        ),
        "horizon": _base.Binding(
            path="WTHR/41:Weather Colors/payload/8:Horizon",
            kind="struct",
            name="Horizon",
        ),
        "effect_lighting": _base.Binding(
            path="WTHR/41:Weather Colors/payload/9:Effect Lighting",
            kind="struct",
            name="Effect Lighting",
        ),
        "cloud_lod_diffuse": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/10:Cloud LOD Diffuse"),
            kind="struct",
            name="Cloud LOD Diffuse",
        ),
        "cloud_lod_ambient": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/11:Cloud LOD Ambient"),
            kind="struct",
            name="Cloud LOD Ambient",
        ),
        "fog_far": _base.Binding(
            path="WTHR/41:Weather Colors/payload/12:Fog Far",
            kind="struct",
            name="Fog Far",
        ),
        "sky_statics": _base.Binding(
            path="WTHR/41:Weather Colors/payload/13:Sky Statics",
            kind="struct",
            name="Sky Statics",
        ),
        "water_multiplier": _base.Binding(
            path=("WTHR/41:Weather Colors/payload/14:Water Multiplier"),
            kind="struct",
            name="Water Multiplier",
        ),
        "sun_glare": _base.Binding(
            path="WTHR/41:Weather Colors/payload/15:Sun Glare",
            kind="struct",
            name="Sun Glare",
        ),
        "moon_glare": _base.Binding(
            path="WTHR/41:Weather Colors/payload/16:Moon Glare",
            kind="struct",
            name="Moon Glare",
        ),
    }

    sky_upper: SkyUpper17673
    """Value decoded from this schema node."""

    fog_near: FogNear17694
    """Value decoded from this schema node."""

    unknown: Unknown17715
    """Value decoded from this schema node."""

    ambient: Ambient17736
    """Value decoded from this schema node."""

    sunlight: Sunlight17757
    """Value decoded from this schema node."""

    sun: Sun17778
    """Value decoded from this schema node."""

    stars: Stars17799
    """Value decoded from this schema node."""

    sky_lower: SkyLower17820
    """Value decoded from this schema node."""

    horizon: Horizon17841
    """Value decoded from this schema node."""

    effect_lighting: EffectLighting17862
    """Value decoded from this schema node."""

    cloud_lod_diffuse: CloudLodDiffuse17883
    """Value decoded from this schema node."""

    cloud_lod_ambient: CloudLodAmbient17904
    """Value decoded from this schema node."""

    fog_far: FogFar17925
    """Value decoded from this schema node."""

    sky_statics: Optional[SkyStatics17946] = None
    """Value decoded from this schema node."""

    water_multiplier: Optional[WaterMultiplier17967] = None
    """Value decoded from this schema node."""

    sun_glare: Optional[SunGlare17988] = None
    """Value decoded from this schema node."""

    moon_glare: Optional[MoonGlare18009] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["sky_upper"]
    ) -> _base.FieldRef[SkyUpper17673]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fog_near"]) -> _base.FieldRef[FogNear17694]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[Unknown17715]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ambient"]) -> _base.FieldRef[Ambient17736]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunlight"]) -> _base.FieldRef[Sunlight17757]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sun"]) -> _base.FieldRef[Sun17778]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["stars"]) -> _base.FieldRef[Stars17799]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sky_lower"]
    ) -> _base.FieldRef[SkyLower17820]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["horizon"]) -> _base.FieldRef[Horizon17841]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effect_lighting"]
    ) -> _base.FieldRef[EffectLighting17862]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_lod_diffuse"]
    ) -> _base.FieldRef[CloudLodDiffuse17883]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_lod_ambient"]
    ) -> _base.FieldRef[CloudLodAmbient17904]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fog_far"]) -> _base.FieldRef[FogFar17925]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sky_statics"]
    ) -> _base.FieldRef[Optional[SkyStatics17946]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_multiplier"]
    ) -> _base.FieldRef[Optional[WaterMultiplier17967]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sun_glare"]
    ) -> _base.FieldRef[Optional[SunGlare17988]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["moon_glare"]
    ) -> _base.FieldRef[Optional[MoonGlare18009]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure18031(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/42:Fog Distance/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "day_near": _base.Binding(
            path="WTHR/42:Fog Distance/payload/0:Day - Near",
            kind="primitive",
            name="Day - Near",
        ),
        "day_far": _base.Binding(
            path="WTHR/42:Fog Distance/payload/1:Day - Far",
            kind="primitive",
            name="Day - Far",
        ),
        "night_near": _base.Binding(
            path="WTHR/42:Fog Distance/payload/2:Night - Near",
            kind="primitive",
            name="Night - Near",
        ),
        "night_far": _base.Binding(
            path="WTHR/42:Fog Distance/payload/3:Night - Far",
            kind="primitive",
            name="Night - Far",
        ),
        "day_power": _base.Binding(
            path="WTHR/42:Fog Distance/payload/4:Day - Power",
            kind="primitive",
            name="Day - Power",
        ),
        "night_power": _base.Binding(
            path="WTHR/42:Fog Distance/payload/5:Night - Power",
            kind="primitive",
            name="Night - Power",
        ),
        "day_max": _base.Binding(
            path="WTHR/42:Fog Distance/payload/6:Day - Max",
            kind="primitive",
            name="Day - Max",
        ),
        "night_max": _base.Binding(
            path="WTHR/42:Fog Distance/payload/7:Night - Max",
            kind="primitive",
            name="Night - Max",
        ),
    }

    day_near: float
    """Value decoded from this schema node."""

    day_far: float
    """Value decoded from this schema node."""

    night_near: float
    """Value decoded from this schema node."""

    night_far: float
    """Value decoded from this schema node."""

    day_power: float
    """Value decoded from this schema node."""

    night_power: float
    """Value decoded from this schema node."""

    day_max: float
    """Value decoded from this schema node."""

    night_max: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["day_near"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day_far"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night_near"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night_far"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day_power"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night_power"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day_max"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night_max"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags18052(enum.IntFlag):
    """Named values from the pinned schema."""

    WEATHER_PLEASANT = 1
    WEATHER_CLOUDY = 2
    WEATHER_RAINY = 4
    WEATHER_SNOW = 8
    SKY_STATICS_ALWAYS_VISIBLE = 16
    SKY_STATICS_FOLLOWS_SUN_POSITION = 32


class LightningColor18053(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/43:Data/payload/11:Lightning Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="WTHR/43:Data/payload/11:Lightning Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="WTHR/43:Data/payload/11:Lightning Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="WTHR/43:Data/payload/11:Lightning Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
    }

    red: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    green: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    blue: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
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
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure18041(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/43:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "wind_speed": _base.Binding(
            path="WTHR/43:Data/payload/0:Wind Speed",
            kind="primitive",
            name="Wind Speed",
        ),
        "unknown": _base.Binding(
            path="WTHR/43:Data/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "trans_delta": _base.Binding(
            path="WTHR/43:Data/payload/2:Trans Delta",
            kind="primitive",
            name="Trans Delta",
        ),
        "sun_glare": _base.Binding(
            path="WTHR/43:Data/payload/3:Sun Glare",
            kind="primitive",
            name="Sun Glare",
        ),
        "sun_damage": _base.Binding(
            path="WTHR/43:Data/payload/4:Sun Damage",
            kind="primitive",
            name="Sun Damage",
        ),
        "precipitation_begin_fade_in": _base.Binding(
            path=("WTHR/43:Data/payload/5:Precipitation - Begin Fade In"),
            kind="primitive",
            name="Precipitation - Begin Fade In",
        ),
        "precipitation_end_fade_out": _base.Binding(
            path=("WTHR/43:Data/payload/6:Precipitation - End Fade Out"),
            kind="primitive",
            name="Precipitation - End Fade Out",
        ),
        "thunder_lightning_begin_fade_in": _base.Binding(
            path=("WTHR/43:Data/payload/7:Thunder/Lightning - Begin Fade In"),
            kind="primitive",
            name="Thunder/Lightning - Begin Fade In",
        ),
        "thunder_lightning_end_fade_out": _base.Binding(
            path=("WTHR/43:Data/payload/8:Thunder/Lightning - End Fade Out"),
            kind="primitive",
            name="Thunder/Lightning - End Fade Out",
        ),
        "thunder_lightning_frequency": _base.Binding(
            path=("WTHR/43:Data/payload/9:Thunder/Lightning - Frequency"),
            kind="primitive",
            name="Thunder/Lightning - Frequency",
        ),
        "flags": _base.Binding(
            path="WTHR/43:Data/payload/10:Flags",
            kind="primitive",
            name="Flags",
        ),
        "lightning_color": _base.Binding(
            path="WTHR/43:Data/payload/11:Lightning Color",
            kind="struct",
            name="Lightning Color",
        ),
        "visual_effect_begin": _base.Binding(
            path="WTHR/43:Data/payload/12:Visual Effect - Begin",
            kind="primitive",
            name="Visual Effect - Begin",
        ),
        "visual_effect_end": _base.Binding(
            path="WTHR/43:Data/payload/13:Visual Effect - End",
            kind="primitive",
            name="Visual Effect - End",
        ),
        "wind_direction": _base.Binding(
            path="WTHR/43:Data/payload/14:Wind Direction",
            kind="primitive",
            name="Wind Direction",
        ),
        "wind_direction_range": _base.Binding(
            path="WTHR/43:Data/payload/15:Wind Direction Range",
            kind="primitive",
            name="Wind Direction Range",
        ),
    }

    wind_speed: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    trans_delta: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    sun_glare: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    sun_damage: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    precipitation_begin_fade_in: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    precipitation_end_fade_out: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    thunder_lightning_begin_fade_in: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    thunder_lightning_end_fade_out: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    thunder_lightning_frequency: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    flags: Flags18052
    """Value decoded from this schema node."""

    lightning_color: LightningColor18053
    """Value decoded from this schema node."""

    visual_effect_begin: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    visual_effect_end: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    wind_direction: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    wind_direction_range: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["wind_speed"]
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
    def field(
        self, name: Literal["trans_delta"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sun_glare"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sun_damage"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["precipitation_begin_fade_in"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["precipitation_end_fade_out"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["thunder_lightning_begin_fade_in"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["thunder_lightning_end_fade_out"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["thunder_lightning_frequency"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags18052]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lightning_color"]
    ) -> _base.FieldRef[LightningColor18053]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["visual_effect_begin"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["visual_effect_end"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["wind_direction"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["wind_direction_range"]
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


class Value012345678910111213141518182105118062(enum.IntFlag):
    """Named values from the pinned schema."""

    VALUE_0 = 1
    VALUE_1 = 2
    VALUE_2 = 4
    VALUE_3 = 8
    VALUE_4 = 16
    VALUE_5 = 32
    VALUE_6 = 64
    VALUE_7 = 128
    VALUE_8 = 256
    VALUE_9 = 512
    VALUE_10 = 1024
    VALUE_11 = 2048
    VALUE_12 = 4096
    VALUE_13 = 8192
    VALUE_14 = 16384
    VALUE_15 = 32768
    VALUE_16 = 65536
    VALUE_17 = 131072
    VALUE_18 = 262144
    VALUE_19 = 524288
    VALUE_20 = 1048576
    VALUE_21 = 2097152
    VALUE_22 = 4194304
    VALUE_23 = 8388608
    VALUE_24 = 16777216
    VALUE_25 = 33554432
    VALUE_26 = 67108864
    VALUE_27 = 134217728
    VALUE_28 = 268435456
    VALUE_29 = 536870912
    VALUE_30 = 1073741824
    VALUE_31 = 2147483648


class Type18067(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    DEFAULT = 0
    PRECIPITATION = 1
    WIND = 2
    THUNDER = 3


class Structure18065(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/45:Sounds/repeat/0:Sound/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sound": _base.Binding(
            path="WTHR/45:Sounds/repeat/0:Sound/payload/0:Sound",
            kind="primitive",
            name="Sound",
        ),
        "type": _base.Binding(
            path="WTHR/45:Sounds/repeat/0:Sound/payload/1:Type",
            kind="primitive",
            name="Type",
        ),
    }

    sound: _values.FormId
    """Value decoded from this schema node."""

    type: Type18067
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sound"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type18067]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure18072(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/47:Image Spaces/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path="WTHR/47:Image Spaces/payload/0:Sunrise",
            kind="primitive",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/47:Image Spaces/payload/1:Day",
            kind="primitive",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/47:Image Spaces/payload/2:Sunset",
            kind="primitive",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/47:Image Spaces/payload/3:Night",
            kind="primitive",
            name="Night",
        ),
    }

    sunrise: _values.FormId
    """Value decoded from this schema node."""

    day: _values.FormId
    """Value decoded from this schema node."""

    sunset: _values.FormId
    """Value decoded from this schema node."""

    night: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure18078(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/48:Volumetric Lighting/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path="WTHR/48:Volumetric Lighting/payload/0:Sunrise",
            kind="primitive",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/48:Volumetric Lighting/payload/1:Day",
            kind="primitive",
            name="Day",
        ),
        "sunset": _base.Binding(
            path="WTHR/48:Volumetric Lighting/payload/2:Sunset",
            kind="primitive",
            name="Sunset",
        ),
        "night": _base.Binding(
            path="WTHR/48:Volumetric Lighting/payload/3:Night",
            kind="primitive",
            name="Night",
        ),
    }

    sunrise: _values.FormId
    """Value decoded from this schema node."""

    day: _values.FormId
    """Value decoded from this schema node."""

    sunset: _values.FormId
    """Value decoded from this schema node."""

    night: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["sunrise"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["day"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunset"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["night"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class X18087(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/0:Directional/0:X+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/0:X+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/0:X+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/0:X+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/0:X+/3:Unused"
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


class X18092(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/0:Directional/1:X-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/1:X-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/1:X-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/1:X-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/1:X-/3:Unused"
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


class Y18097(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/0:Directional/2:Y+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/2:Y+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/2:Y+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/2:Y+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/2:Y+/3:Unused"
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


class Y18102(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/0:Directional/3:Y-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/3:Y-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/3:Y-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/3:Y-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/3:Y-/3:Unused"
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


class Z18107(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/0:Directional/4:Z+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/4:Z+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/4:Z+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/4:Z+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/4:Z+/3:Unused"
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


class Z18112(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/0:Directional/5:Z-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/5:Z-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/5:Z-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/5:Z-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/5:Z-/3:Unused"
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


class Directional18086(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/0:Directional"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/0:X+"
            ),
            kind="struct",
            name="X+",
        ),
        "x_18092": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/1:X-"
            ),
            kind="struct",
            name="X-",
        ),
        "y": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/2:Y+"
            ),
            kind="struct",
            name="Y+",
        ),
        "y_18102": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/3:Y-"
            ),
            kind="struct",
            name="Y-",
        ),
        "z": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/4:Z+"
            ),
            kind="struct",
            name="Z+",
        ),
        "z_18112": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional/5:Z-"
            ),
            kind="struct",
            name="Z-",
        ),
    }

    x: X18087
    """Value decoded from this schema node."""

    x_18092: X18092
    """Value decoded from this schema node."""

    y: Y18097
    """Value decoded from this schema node."""

    y_18102: Y18102
    """Value decoded from this schema node."""

    z: Z18107
    """Value decoded from this schema node."""

    z_18112: Z18112
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[X18087]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["x_18092"]) -> _base.FieldRef[X18092]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Y18097]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y_18102"]) -> _base.FieldRef[Y18102]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Z18107]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z_18112"]) -> _base.FieldRef[Z18112]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Specular18117(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
        "payload/1:Specular"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/1:Specular/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/1:Specular/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/1:Specular/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/1:Specular/3:Unused"
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


class Structure18085(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/0:Directional"
            ),
            kind="struct",
            name="Directional",
        ),
        "specular": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/1:Specular"
            ),
            kind="struct",
            name="Specular",
        ),
        "scale": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/0:Sunrise/"
                "payload/2:Scale"
            ),
            kind="primitive",
            name="Scale",
        ),
    }

    directional: Directional18086
    """Value decoded from this schema node."""

    specular: Optional[Specular18117] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["directional"]
    ) -> _base.FieldRef[Directional18086]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular"]
    ) -> _base.FieldRef[Optional[Specular18117]]:
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


class X18126(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
        "oad/0:Directional/0:X+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/0:X+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/0:X+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/0:X+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/0:X+/3:Unused"
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


class X18131(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
        "oad/0:Directional/1:X-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/1:X-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/1:X-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/1:X-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/1:X-/3:Unused"
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


class Y18136(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
        "oad/0:Directional/2:Y+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/2:Y+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/2:Y+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/2:Y+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/2:Y+/3:Unused"
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


class Y18141(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
        "oad/0:Directional/3:Y-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/3:Y-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/3:Y-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/3:Y-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/3:Y-/3:Unused"
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


class Z18146(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
        "oad/0:Directional/4:Z+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/4:Z+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/4:Z+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/4:Z+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/4:Z+/3:Unused"
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


class Z18151(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
        "oad/0:Directional/5:Z-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/5:Z-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/5:Z-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/5:Z-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/5:Z-/3:Unused"
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


class Directional18125(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
        "oad/0:Directional"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/0:X+"
            ),
            kind="struct",
            name="X+",
        ),
        "x_18131": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/1:X-"
            ),
            kind="struct",
            name="X-",
        ),
        "y": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/2:Y+"
            ),
            kind="struct",
            name="Y+",
        ),
        "y_18141": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/3:Y-"
            ),
            kind="struct",
            name="Y-",
        ),
        "z": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/4:Z+"
            ),
            kind="struct",
            name="Z+",
        ),
        "z_18151": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional/5:Z-"
            ),
            kind="struct",
            name="Z-",
        ),
    }

    x: X18126
    """Value decoded from this schema node."""

    x_18131: X18131
    """Value decoded from this schema node."""

    y: Y18136
    """Value decoded from this schema node."""

    y_18141: Y18141
    """Value decoded from this schema node."""

    z: Z18146
    """Value decoded from this schema node."""

    z_18151: Z18151
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[X18126]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["x_18131"]) -> _base.FieldRef[X18131]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Y18136]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y_18141"]) -> _base.FieldRef[Y18141]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Z18146]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z_18151"]) -> _base.FieldRef[Z18151]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Specular18156(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payload/1:Specular"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/1:Specular/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/1:Specular/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/1:Specular/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/1:Specular/3:Unused"
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


class Structure18124(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/1:Day/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/0:Directional"
            ),
            kind="struct",
            name="Directional",
        ),
        "specular": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/1:Specular"
            ),
            kind="struct",
            name="Specular",
        ),
        "scale": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/1:Day/payl"
                "oad/2:Scale"
            ),
            kind="primitive",
            name="Scale",
        ),
    }

    directional: Directional18125
    """Value decoded from this schema node."""

    specular: Optional[Specular18156] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["directional"]
    ) -> _base.FieldRef[Directional18125]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular"]
    ) -> _base.FieldRef[Optional[Specular18156]]:
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


class X18165(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/0:Directional/0:X+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/0:X+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/0:X+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/0:X+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/0:X+/3:Unused"
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


class X18170(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/0:Directional/1:X-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/1:X-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/1:X-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/1:X-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/1:X-/3:Unused"
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


class Y18175(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/0:Directional/2:Y+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/2:Y+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/2:Y+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/2:Y+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/2:Y+/3:Unused"
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


class Y18180(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/0:Directional/3:Y-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/3:Y-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/3:Y-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/3:Y-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/3:Y-/3:Unused"
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


class Z18185(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/0:Directional/4:Z+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/4:Z+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/4:Z+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/4:Z+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/4:Z+/3:Unused"
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


class Z18190(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/0:Directional/5:Z-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/5:Z-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/5:Z-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/5:Z-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/5:Z-/3:Unused"
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


class Directional18164(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/0:Directional"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/0:X+"
            ),
            kind="struct",
            name="X+",
        ),
        "x_18170": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/1:X-"
            ),
            kind="struct",
            name="X-",
        ),
        "y": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/2:Y+"
            ),
            kind="struct",
            name="Y+",
        ),
        "y_18180": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/3:Y-"
            ),
            kind="struct",
            name="Y-",
        ),
        "z": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/4:Z+"
            ),
            kind="struct",
            name="Z+",
        ),
        "z_18190": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional/5:Z-"
            ),
            kind="struct",
            name="Z-",
        ),
    }

    x: X18165
    """Value decoded from this schema node."""

    x_18170: X18170
    """Value decoded from this schema node."""

    y: Y18175
    """Value decoded from this schema node."""

    y_18180: Y18180
    """Value decoded from this schema node."""

    z: Z18185
    """Value decoded from this schema node."""

    z_18190: Z18190
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[X18165]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["x_18170"]) -> _base.FieldRef[X18170]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Y18175]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y_18180"]) -> _base.FieldRef[Y18180]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Z18185]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z_18190"]) -> _base.FieldRef[Z18190]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Specular18195(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
        "ayload/1:Specular"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/1:Specular/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/1:Specular/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/1:Specular/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/1:Specular/3:Unused"
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


class Structure18163(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/0:Directional"
            ),
            kind="struct",
            name="Directional",
        ),
        "specular": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/1:Specular"
            ),
            kind="struct",
            name="Specular",
        ),
        "scale": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/2:Sunset/p"
                "ayload/2:Scale"
            ),
            kind="primitive",
            name="Scale",
        ),
    }

    directional: Directional18164
    """Value decoded from this schema node."""

    specular: Optional[Specular18195] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["directional"]
    ) -> _base.FieldRef[Directional18164]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular"]
    ) -> _base.FieldRef[Optional[Specular18195]]:
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


class X18204(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
        "yload/0:Directional/0:X+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/0:X+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/0:X+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/0:X+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/0:X+/3:Unused"
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


class X18209(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
        "yload/0:Directional/1:X-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/1:X-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/1:X-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/1:X-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/1:X-/3:Unused"
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


class Y18214(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
        "yload/0:Directional/2:Y+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/2:Y+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/2:Y+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/2:Y+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/2:Y+/3:Unused"
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


class Y18219(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
        "yload/0:Directional/3:Y-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/3:Y-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/3:Y-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/3:Y-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/3:Y-/3:Unused"
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


class Z18224(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
        "yload/0:Directional/4:Z+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/4:Z+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/4:Z+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/4:Z+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/4:Z+/3:Unused"
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


class Z18229(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
        "yload/0:Directional/5:Z-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/5:Z-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/5:Z-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/5:Z-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/5:Z-/3:Unused"
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


class Directional18203(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
        "yload/0:Directional"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/0:X+"
            ),
            kind="struct",
            name="X+",
        ),
        "x_18209": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/1:X-"
            ),
            kind="struct",
            name="X-",
        ),
        "y": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/2:Y+"
            ),
            kind="struct",
            name="Y+",
        ),
        "y_18219": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/3:Y-"
            ),
            kind="struct",
            name="Y-",
        ),
        "z": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/4:Z+"
            ),
            kind="struct",
            name="Z+",
        ),
        "z_18229": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional/5:Z-"
            ),
            kind="struct",
            name="Z-",
        ),
    }

    x: X18204
    """Value decoded from this schema node."""

    x_18209: X18209
    """Value decoded from this schema node."""

    y: Y18214
    """Value decoded from this schema node."""

    y_18219: Y18219
    """Value decoded from this schema node."""

    z: Z18224
    """Value decoded from this schema node."""

    z_18229: Z18229
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[X18204]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["x_18209"]) -> _base.FieldRef[X18209]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Y18214]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y_18219"]) -> _base.FieldRef[Y18219]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Z18224]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z_18229"]) -> _base.FieldRef[Z18229]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Specular18234(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/payload/1:Specular"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/1:Specular/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/1:Specular/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/1:Specular/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/1:Specular/3:Unused"
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


class Structure18202(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/49:Directional Ambient Lighting Colors/3:Night/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/0:Directional"
            ),
            kind="struct",
            name="Directional",
        ),
        "specular": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/1:Specular"
            ),
            kind="struct",
            name="Specular",
        ),
        "scale": _base.Binding(
            path=(
                "WTHR/49:Directional Ambient Lighting Colors/3:Night/pa"
                "yload/2:Scale"
            ),
            kind="primitive",
            name="Scale",
        ),
    }

    directional: Directional18203
    """Value decoded from this schema node."""

    specular: Optional[Specular18234] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["directional"]
    ) -> _base.FieldRef[Directional18203]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular"]
    ) -> _base.FieldRef[Optional[Specular18234]]:
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


class DirectionalAmbientLightingColors18083(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/49:Directional Ambient Lighting Colors"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sunrise": _base.Binding(
            path=("WTHR/49:Directional Ambient Lighting Colors/0:Sunrise"),
            kind="subrecord",
            name="Sunrise",
        ),
        "day": _base.Binding(
            path="WTHR/49:Directional Ambient Lighting Colors/1:Day",
            kind="subrecord",
            name="Day",
        ),
        "sunset": _base.Binding(
            path=("WTHR/49:Directional Ambient Lighting Colors/2:Sunset"),
            kind="subrecord",
            name="Sunset",
        ),
        "night": _base.Binding(
            path=("WTHR/49:Directional Ambient Lighting Colors/3:Night"),
            kind="subrecord",
            name="Night",
        ),
    }

    sunrise: Optional[Structure18085] = None
    """Value decoded from this schema node."""

    day: Optional[Structure18124] = None
    """Value decoded from this schema node."""

    sunset: Optional[Structure18163] = None
    """Value decoded from this schema node."""

    night: Optional[Structure18202] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["sunrise"]
    ) -> _base.FieldRef[Optional[Structure18085]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["day"]
    ) -> _base.FieldRef[Optional[Structure18124]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sunset"]
    ) -> _base.FieldRef[Optional[Structure18163]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["night"]
    ) -> _base.FieldRef[Optional[Structure18202]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure18250(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18252": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18253": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18254": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_18252: bytes
    """Value decoded from this schema node."""

    unused_18253: bytes
    """Value decoded from this schema node."""

    unused_18254: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18252"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18253"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18254"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_18250: _base.Variant = _base.Variant(
    path=(
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/0:Structure"
    )
)


class Structure18255(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_18258": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18259": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_18258: bytes
    """Value decoded from this schema node."""

    unused_18259: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["error"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18258"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18259"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_18255: _base.Variant = _base.Variant(
    path=(
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/1:Structure"
    )
)


class Texture18263(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/2:Structure/1:Textures/element/2:Folder Hash"
            ),
            kind="primitive",
            name="Folder Hash",
        ),
    }

    file_hash: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    extension: str
    """Value decoded from this schema node."""

    folder_hash: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["extension"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["folder_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class Structure18260(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_18267": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18268": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture18263, ...]
    """Value decoded from this schema node."""

    unused_18267: bytes
    """Value decoded from this schema node."""

    unused_18268: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture18263, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18267"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18268"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_18260: _base.Variant = _base.Variant(
    path=(
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/2:Structure"
    )
)


class Texture18273(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/1:Textures/element/2:Folder Hash"
            ),
            kind="primitive",
            name="Folder Hash",
        ),
    }

    file_hash: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    extension: str
    """Value decoded from this schema node."""

    folder_hash: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["extension"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["folder_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class Material18280(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/3:Materials/element/2:Folder Hash"
            ),
            kind="primitive",
            name="Folder Hash",
        ),
    }

    file_hash: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    extension: str
    """Value decoded from this schema node."""

    folder_hash: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["extension"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["folder_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class Structure18269(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
                "iants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture18273, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material18280, ...]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["headers"]
    ) -> _base.FieldRef[
        tuple[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            ...,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture18273, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addons"]
    ) -> _base.FieldRef[
        tuple[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            ...,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["materials"]
    ) -> _base.FieldRef[tuple[Material18280, ...]]:
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


_VARIANT_18269: _base.Variant = _base.Variant(
    path=(
        "WTHR/52:Aurora/0:Model/1:Model Information/payload/var"
        "iants/3:Structure"
    )
)


class AlternateTexture18287(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WTHR/52:Aurora/0:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/2:Alternate Textures/payload/el"
                "ement/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/2:Alternate Textures/payload/el"
                "ement/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "WTHR/52:Aurora/0:Model/2:Alternate Textures/payload/el"
                "ement/2:3D Index"
            ),
            kind="primitive",
            name="3D Index",
        ),
    }

    value_3_d_name: str
    """Value decoded from this schema node."""

    new_texture: _values.FormId
    """Value decoded from this schema node."""

    value_3_d_index: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["value_3_d_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["new_texture"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value_3_d_index"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
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


class Model18245(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/52:Aurora/0:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="WTHR/52:Aurora/0:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="WTHR/52:Aurora/0:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="WTHR/52:Aurora/0:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure18250, _VARIANT_18250]
        | Annotated[Structure18255, _VARIANT_18255]
        | Annotated[Structure18260, _VARIANT_18260]
        | Annotated[Structure18269, _VARIANT_18269]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture18287, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["model_file_name_value"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_information_value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure18250, _VARIANT_18250]
            | Annotated[Structure18255, _VARIANT_18255]
            | Annotated[Structure18260, _VARIANT_18260]
            | Annotated[Structure18269, _VARIANT_18269]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture18287, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Aurora18244(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR/52:Aurora"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model": _base.Binding(
            path="WTHR/52:Aurora/0:Model",
            kind="unordered",
            name="Model",
        ),
    }

    model: Optional[Model18245] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model18245]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class WeatherRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WTHR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "WTHR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="WTHR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "cloud_texture_layer_0": _base.Binding(
            path="WTHR/1:Cloud Texture Layer #0",
            kind="subrecord",
            name="Cloud Texture Layer #0",
        ),
        "cloud_texture_layer_1": _base.Binding(
            path="WTHR/2:Cloud Texture Layer #1",
            kind="subrecord",
            name="Cloud Texture Layer #1",
        ),
        "cloud_texture_layer_2": _base.Binding(
            path="WTHR/3:Cloud Texture Layer #2",
            kind="subrecord",
            name="Cloud Texture Layer #2",
        ),
        "cloud_texture_layer_3": _base.Binding(
            path="WTHR/4:Cloud Texture Layer #3",
            kind="subrecord",
            name="Cloud Texture Layer #3",
        ),
        "cloud_texture_layer_4": _base.Binding(
            path="WTHR/5:Cloud Texture Layer #4",
            kind="subrecord",
            name="Cloud Texture Layer #4",
        ),
        "cloud_texture_layer_5": _base.Binding(
            path="WTHR/6:Cloud Texture Layer #5",
            kind="subrecord",
            name="Cloud Texture Layer #5",
        ),
        "cloud_texture_layer_6": _base.Binding(
            path="WTHR/7:Cloud Texture Layer #6",
            kind="subrecord",
            name="Cloud Texture Layer #6",
        ),
        "cloud_texture_layer_7": _base.Binding(
            path="WTHR/8:Cloud Texture Layer #7",
            kind="subrecord",
            name="Cloud Texture Layer #7",
        ),
        "cloud_texture_layer_8": _base.Binding(
            path="WTHR/9:Cloud Texture Layer #8",
            kind="subrecord",
            name="Cloud Texture Layer #8",
        ),
        "cloud_texture_layer_9": _base.Binding(
            path="WTHR/10:Cloud Texture Layer #9",
            kind="subrecord",
            name="Cloud Texture Layer #9",
        ),
        "cloud_texture_layer_10": _base.Binding(
            path="WTHR/11:Cloud Texture Layer #10",
            kind="subrecord",
            name="Cloud Texture Layer #10",
        ),
        "cloud_texture_layer_11": _base.Binding(
            path="WTHR/12:Cloud Texture Layer #11",
            kind="subrecord",
            name="Cloud Texture Layer #11",
        ),
        "cloud_texture_layer_12": _base.Binding(
            path="WTHR/13:Cloud Texture Layer #12",
            kind="subrecord",
            name="Cloud Texture Layer #12",
        ),
        "cloud_texture_layer_13": _base.Binding(
            path="WTHR/14:Cloud Texture Layer #13",
            kind="subrecord",
            name="Cloud Texture Layer #13",
        ),
        "cloud_texture_layer_14": _base.Binding(
            path="WTHR/15:Cloud Texture Layer #14",
            kind="subrecord",
            name="Cloud Texture Layer #14",
        ),
        "cloud_texture_layer_15": _base.Binding(
            path="WTHR/16:Cloud Texture Layer #15",
            kind="subrecord",
            name="Cloud Texture Layer #15",
        ),
        "cloud_texture_layer_16": _base.Binding(
            path="WTHR/17:Cloud Texture Layer #16",
            kind="subrecord",
            name="Cloud Texture Layer #16",
        ),
        "cloud_texture_layer_17": _base.Binding(
            path="WTHR/18:Cloud Texture Layer #17",
            kind="subrecord",
            name="Cloud Texture Layer #17",
        ),
        "cloud_texture_layer_18": _base.Binding(
            path="WTHR/19:Cloud Texture Layer #18",
            kind="subrecord",
            name="Cloud Texture Layer #18",
        ),
        "cloud_texture_layer_19": _base.Binding(
            path="WTHR/20:Cloud Texture Layer #19",
            kind="subrecord",
            name="Cloud Texture Layer #19",
        ),
        "cloud_texture_layer_20": _base.Binding(
            path="WTHR/21:Cloud Texture Layer #20",
            kind="subrecord",
            name="Cloud Texture Layer #20",
        ),
        "cloud_texture_layer_21": _base.Binding(
            path="WTHR/22:Cloud Texture Layer #21",
            kind="subrecord",
            name="Cloud Texture Layer #21",
        ),
        "cloud_texture_layer_22": _base.Binding(
            path="WTHR/23:Cloud Texture Layer #22",
            kind="subrecord",
            name="Cloud Texture Layer #22",
        ),
        "cloud_texture_layer_23": _base.Binding(
            path="WTHR/24:Cloud Texture Layer #23",
            kind="subrecord",
            name="Cloud Texture Layer #23",
        ),
        "cloud_texture_layer_24": _base.Binding(
            path="WTHR/25:Cloud Texture Layer #24",
            kind="subrecord",
            name="Cloud Texture Layer #24",
        ),
        "cloud_texture_layer_25": _base.Binding(
            path="WTHR/26:Cloud Texture Layer #25",
            kind="subrecord",
            name="Cloud Texture Layer #25",
        ),
        "cloud_texture_layer_26": _base.Binding(
            path="WTHR/27:Cloud Texture Layer #26",
            kind="subrecord",
            name="Cloud Texture Layer #26",
        ),
        "cloud_texture_layer_27": _base.Binding(
            path="WTHR/28:Cloud Texture Layer #27",
            kind="subrecord",
            name="Cloud Texture Layer #27",
        ),
        "cloud_texture_layer_28": _base.Binding(
            path="WTHR/29:Cloud Texture Layer #28",
            kind="subrecord",
            name="Cloud Texture Layer #28",
        ),
        "unused": _base.Binding(
            path="WTHR/30:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_17620": _base.Binding(
            path="WTHR/31:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_17622": _base.Binding(
            path="WTHR/32:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_17624": _base.Binding(
            path="WTHR/33:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unknown": _base.Binding(
            path="WTHR/34:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "precipitation_type": _base.Binding(
            path="WTHR/35:Precipitation Type",
            kind="subrecord",
            name="Precipitation Type",
        ),
        "visual_effect": _base.Binding(
            path="WTHR/36:Visual Effect",
            kind="subrecord",
            name="Visual Effect",
        ),
        "unused_17632": _base.Binding(
            path="WTHR/37:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "cloud_speed": _base.Binding(
            path="WTHR/38:Cloud Speed",
            kind="sequence",
            name="Cloud Speed",
        ),
        "cloud_colors": _base.Binding(
            path="WTHR/39:Cloud Colors",
            kind="subrecord",
            name="Cloud Colors",
        ),
        "cloud_alphas": _base.Binding(
            path="WTHR/40:Cloud Alphas",
            kind="subrecord",
            name="Cloud Alphas",
        ),
        "weather_colors": _base.Binding(
            path="WTHR/41:Weather Colors",
            kind="subrecord",
            name="Weather Colors",
        ),
        "fog_distance": _base.Binding(
            path="WTHR/42:Fog Distance",
            kind="subrecord",
            name="Fog Distance",
        ),
        "data": _base.Binding(
            path="WTHR/43:Data",
            kind="subrecord",
            name="Data",
        ),
        "disabled_cloud_layers": _base.Binding(
            path="WTHR/44:Disabled Cloud Layers",
            kind="subrecord",
            name="Disabled Cloud Layers",
        ),
        "sounds": _base.Binding(
            path="WTHR/45:Sounds",
            kind="repeat",
            name="Sounds",
            repeated_path="WTHR/45:Sounds/repeat/0:Sound",
            child_kind="subrecord",
        ),
        "sky_statics": _base.Binding(
            path="WTHR/46:Sky Statics",
            kind="repeat",
            name="Sky Statics",
            repeated_path="WTHR/46:Sky Statics/repeat/0:Static",
            child_kind="subrecord",
        ),
        "image_spaces": _base.Binding(
            path="WTHR/47:Image Spaces",
            kind="subrecord",
            name="Image Spaces",
        ),
        "volumetric_lighting": _base.Binding(
            path="WTHR/48:Volumetric Lighting",
            kind="subrecord",
            name="Volumetric Lighting",
        ),
        "directional_ambient_lighting_colors": _base.Binding(
            path="WTHR/49:Directional Ambient Lighting Colors",
            kind="sequence",
            name="Directional Ambient Lighting Colors",
        ),
        "unused_18240": _base.Binding(
            path="WTHR/50:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_18242": _base.Binding(
            path="WTHR/51:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "aurora": _base.Binding(
            path="WTHR/52:Aurora",
            kind="sequence",
            name="Aurora",
        ),
        "sun_glare_lens_flare": _base.Binding(
            path="WTHR/53:Sun Glare Lens Flare",
            kind="subrecord",
            name="Sun Glare Lens Flare",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_0: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_1: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_2: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_3: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_4: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_5: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_6: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_7: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_8: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_9: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_10: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_11: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_12: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_13: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_14: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_15: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_16: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_17: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_18: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_19: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_20: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_21: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_22: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_23: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_24: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_25: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_26: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_27: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_texture_layer_28: Optional[str] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_17620: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_17622: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_17624: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    precipitation_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    visual_effect: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused_17632: Optional[bytes] = None
    """Value decoded from this schema node."""

    cloud_speed: Optional[CloudSpeed17634] = None
    """Value decoded from this schema node."""

    cloud_colors: Optional[tuple[Layer17643, ...]] = None
    """Value decoded from this schema node."""

    cloud_alphas: Optional[tuple[Layer17666, ...]] = None
    """Value decoded from this schema node."""

    weather_colors: Optional[Structure17672] = None
    """Value decoded from this schema node."""

    fog_distance: Optional[Structure18031] = None
    """Value decoded from this schema node."""

    data: Optional[Structure18041] = None
    """Value decoded from this schema node."""

    disabled_cloud_layers: Optional[
        Value012345678910111213141518182105118062
    ] = None
    """Value decoded from this schema node."""

    sounds: tuple[Structure18065, ...] = ()
    """Value decoded from this schema node."""

    sky_statics: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    image_spaces: Optional[Structure18072] = None
    """Value decoded from this schema node."""

    volumetric_lighting: Optional[Structure18078] = None
    """Value decoded from this schema node."""

    directional_ambient_lighting_colors: Optional[
        DirectionalAmbientLightingColors18083
    ] = None
    """Value decoded from this schema node."""

    unused_18240: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_18242: Optional[bytes] = None
    """Value decoded from this schema node."""

    aurora: Optional[Aurora18244] = None
    """Value decoded from this schema node."""

    sun_glare_lens_flare: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_0"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_1"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_2"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_3"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_4"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_5"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_6"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_7"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_8"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_9"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_10"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_11"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_12"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_13"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_14"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_15"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_16"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_17"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_18"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_19"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_20"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_21"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_22"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_23"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_24"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_25"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_26"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_27"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_texture_layer_28"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_17620"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_17622"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_17624"]
    ) -> _base.FieldRef[Optional[bytes]]:
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
        self, name: Literal["precipitation_type"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["visual_effect"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_17632"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_speed"]
    ) -> _base.FieldRef[Optional[CloudSpeed17634]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_colors"]
    ) -> _base.FieldRef[Optional[tuple[Layer17643, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_alphas"]
    ) -> _base.FieldRef[Optional[tuple[Layer17666, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["weather_colors"]
    ) -> _base.FieldRef[Optional[Structure17672]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_distance"]
    ) -> _base.FieldRef[Optional[Structure18031]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure18041]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["disabled_cloud_layers"]
    ) -> _base.FieldRef[Optional[Value012345678910111213141518182105118062]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sounds"]
    ) -> _base.FieldRef[tuple[Structure18065, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sky_statics"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["image_spaces"]
    ) -> _base.FieldRef[Optional[Structure18072]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["volumetric_lighting"]
    ) -> _base.FieldRef[Optional[Structure18078]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["directional_ambient_lighting_colors"]
    ) -> _base.FieldRef[Optional[DirectionalAmbientLightingColors18083]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_18240"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_18242"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["aurora"]
    ) -> _base.FieldRef[Optional[Aurora18244]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sun_glare_lens_flare"]
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
