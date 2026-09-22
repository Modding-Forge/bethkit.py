"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base


class AmbientColor7037(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LGTM/1:Lighting/payload/0:Ambient Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="LGTM/1:Lighting/payload/0:Ambient Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="LGTM/1:Lighting/payload/0:Ambient Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="LGTM/1:Lighting/payload/0:Ambient Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="LGTM/1:Lighting/payload/0:Ambient Color/3:Unused",
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


class DirectionalColor7042(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LGTM/1:Lighting/payload/1:Directional Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="LGTM/1:Lighting/payload/1:Directional Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("LGTM/1:Lighting/payload/1:Directional Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("LGTM/1:Lighting/payload/1:Directional Color/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("LGTM/1:Lighting/payload/1:Directional Color/3:Unused"),
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


class FogColorNear7047(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LGTM/1:Lighting/payload/2:Fog Color Near"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="LGTM/1:Lighting/payload/2:Fog Color Near/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="LGTM/1:Lighting/payload/2:Fog Color Near/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="LGTM/1:Lighting/payload/2:Fog Color Near/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="LGTM/1:Lighting/payload/2:Fog Color Near/3:Unused",
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


class X7061(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/0:X+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/0:X+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/0:X+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/0:X+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
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


class X7066(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/1:X-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/1:X-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/1:X-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/1:X-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
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


class Y7071(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/2:Y+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/2:Y+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/2:Y+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/2:Y+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
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


class Y7076(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/3:Y-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/3:Y-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/3:Y-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/3:Y-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
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


class Z7081(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/4:Z+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/4:Z+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/4:Z+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/4:Z+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
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


class Z7086(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/5:Z-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/5:Z-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/5:Z-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
                "l/5:Z-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directiona"
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


class Directional7060(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/0:X+"
            ),
            kind="struct",
            name="X+",
        ),
        "x_7066": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/1:X-"
            ),
            kind="struct",
            name="X-",
        ),
        "y": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/2:Y+"
            ),
            kind="struct",
            name="Y+",
        ),
        "y_7076": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/3:Y-"
            ),
            kind="struct",
            name="Y-",
        ),
        "z": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/4:Z+"
            ),
            kind="struct",
            name="Z+",
        ),
        "z_7086": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional/5:Z-"
            ),
            kind="struct",
            name="Z-",
        ),
    }

    x: X7061
    """Value decoded from this schema node."""

    x_7066: X7066
    """Value decoded from this schema node."""

    y: Y7071
    """Value decoded from this schema node."""

    y_7076: Y7076
    """Value decoded from this schema node."""

    z: Z7081
    """Value decoded from this schema node."""

    z_7086: Z7086
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[X7061]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["x_7066"]) -> _base.FieldRef[X7066]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Y7071]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y_7076"]) -> _base.FieldRef[Y7076]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Z7081]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z_7086"]) -> _base.FieldRef[Z7086]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Specular7091(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/10:Ambient Colors/1:Specular"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("LGTM/1:Lighting/payload/10:Ambient Colors/1:Specular/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/1:Specular/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/1:Specular/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/1:Lighting/payload/10:Ambient Colors/1:Specular/3:Unused"
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


class AmbientColors7059(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LGTM/1:Lighting/payload/10:Ambient Colors"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=("LGTM/1:Lighting/payload/10:Ambient Colors/0:Directional"),
            kind="struct",
            name="Directional",
        ),
        "specular": _base.Binding(
            path=("LGTM/1:Lighting/payload/10:Ambient Colors/1:Specular"),
            kind="struct",
            name="Specular",
        ),
        "scale": _base.Binding(
            path="LGTM/1:Lighting/payload/10:Ambient Colors/2:Scale",
            kind="primitive",
            name="Scale",
        ),
    }

    directional: Directional7060
    """Value decoded from this schema node."""

    specular: Optional[Specular7091] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["directional"]
    ) -> _base.FieldRef[Directional7060]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular"]
    ) -> _base.FieldRef[Optional[Specular7091]]:
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


class FogColorFar7097(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LGTM/1:Lighting/payload/11:Fog Color Far"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="LGTM/1:Lighting/payload/11:Fog Color Far/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="LGTM/1:Lighting/payload/11:Fog Color Far/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="LGTM/1:Lighting/payload/11:Fog Color Far/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="LGTM/1:Lighting/payload/11:Fog Color Far/3:Unused",
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


class LightFadeDistances7103(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/1:Lighting/payload/13:Light Fade Distances"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "start": _base.Binding(
            path=("LGTM/1:Lighting/payload/13:Light Fade Distances/0:Start"),
            kind="primitive",
            name="Start",
        ),
        "end": _base.Binding(
            path=("LGTM/1:Lighting/payload/13:Light Fade Distances/1:End"),
            kind="primitive",
            name="End",
        ),
    }

    start: float
    """Value decoded from this schema node."""

    end: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["start"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["end"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure7036(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LGTM/1:Lighting/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ambient_color": _base.Binding(
            path="LGTM/1:Lighting/payload/0:Ambient Color",
            kind="struct",
            name="Ambient Color",
        ),
        "directional_color": _base.Binding(
            path="LGTM/1:Lighting/payload/1:Directional Color",
            kind="struct",
            name="Directional Color",
        ),
        "fog_color_near": _base.Binding(
            path="LGTM/1:Lighting/payload/2:Fog Color Near",
            kind="struct",
            name="Fog Color Near",
        ),
        "fog_near": _base.Binding(
            path="LGTM/1:Lighting/payload/3:Fog Near",
            kind="primitive",
            name="Fog Near",
        ),
        "fog_far": _base.Binding(
            path="LGTM/1:Lighting/payload/4:Fog Far",
            kind="primitive",
            name="Fog Far",
        ),
        "directional_rotation_xy": _base.Binding(
            path="LGTM/1:Lighting/payload/5:Directional Rotation XY",
            kind="primitive",
            name="Directional Rotation XY",
        ),
        "directional_rotation_z": _base.Binding(
            path="LGTM/1:Lighting/payload/6:Directional Rotation Z",
            kind="primitive",
            name="Directional Rotation Z",
        ),
        "directional_fade": _base.Binding(
            path="LGTM/1:Lighting/payload/7:Directional Fade",
            kind="primitive",
            name="Directional Fade",
        ),
        "fog_clip_dist": _base.Binding(
            path="LGTM/1:Lighting/payload/8:Fog Clip Dist",
            kind="primitive",
            name="Fog Clip Dist",
        ),
        "fog_power": _base.Binding(
            path="LGTM/1:Lighting/payload/9:Fog Power",
            kind="primitive",
            name="Fog Power",
        ),
        "ambient_colors": _base.Binding(
            path="LGTM/1:Lighting/payload/10:Ambient Colors",
            kind="optional_struct",
            name="Ambient Colors",
        ),
        "fog_color_far": _base.Binding(
            path="LGTM/1:Lighting/payload/11:Fog Color Far",
            kind="struct",
            name="Fog Color Far",
        ),
        "fog_max": _base.Binding(
            path="LGTM/1:Lighting/payload/12:Fog Max",
            kind="primitive",
            name="Fog Max",
        ),
        "light_fade_distances": _base.Binding(
            path="LGTM/1:Lighting/payload/13:Light Fade Distances",
            kind="struct",
            name="Light Fade Distances",
        ),
        "unknown": _base.Binding(
            path="LGTM/1:Lighting/payload/14:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    ambient_color: AmbientColor7037
    """Value decoded from this schema node."""

    directional_color: DirectionalColor7042
    """Value decoded from this schema node."""

    fog_color_near: FogColorNear7047
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

    fog_clip_dist: float
    """Value decoded from this schema node."""

    fog_power: float
    """Value decoded from this schema node."""

    ambient_colors: AmbientColors7059
    """Value decoded from this schema node."""

    fog_color_far: Optional[FogColorFar7097] = None
    """Value decoded from this schema node."""

    fog_max: Optional[float] = None
    """Value decoded from this schema node."""

    light_fade_distances: Optional[LightFadeDistances7103] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ambient_color"]
    ) -> _base.FieldRef[AmbientColor7037]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["directional_color"]
    ) -> _base.FieldRef[DirectionalColor7042]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_color_near"]
    ) -> _base.FieldRef[FogColorNear7047]:
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
    def field(self, name: Literal["fog_clip_dist"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fog_power"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ambient_colors"]
    ) -> _base.FieldRef[AmbientColors7059]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_color_far"]
    ) -> _base.FieldRef[Optional[FogColorFar7097]]:
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
        self, name: Literal["light_fade_distances"]
    ) -> _base.FieldRef[Optional[LightFadeDistances7103]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class X7110(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/0:Directional/0:X+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/0:X+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/0:X+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/0:X+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/0:X+/3:Unused"
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


class X7115(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/0:Directional/1:X-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/1:X-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/1:X-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/1:X-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/1:X-/3:Unused"
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


class Y7120(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/0:Directional/2:Y+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/2:Y+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/2:Y+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/2:Y+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/2:Y+/3:Unused"
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


class Y7125(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/0:Directional/3:Y-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/3:Y-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/3:Y-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/3:Y-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/3:Y-/3:Unused"
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


class Z7130(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/0:Directional/4:Z+"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/4:Z+/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/4:Z+/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/4:Z+/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/4:Z+/3:Unused"
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


class Z7135(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/0:Directional/5:Z-"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/5:Z-/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/5:Z-/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/5:Z-/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/5:Z-/3:Unused"
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


class Directional7109(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/0:Directional"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/0:X+"
            ),
            kind="struct",
            name="X+",
        ),
        "x_7115": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/1:X-"
            ),
            kind="struct",
            name="X-",
        ),
        "y": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/2:Y+"
            ),
            kind="struct",
            name="Y+",
        ),
        "y_7125": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/3:Y-"
            ),
            kind="struct",
            name="Y-",
        ),
        "z": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/4:Z+"
            ),
            kind="struct",
            name="Z+",
        ),
        "z_7135": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional/5:Z-"
            ),
            kind="struct",
            name="Z-",
        ),
    }

    x: X7110
    """Value decoded from this schema node."""

    x_7115: X7115
    """Value decoded from this schema node."""

    y: Y7120
    """Value decoded from this schema node."""

    y_7125: Y7125
    """Value decoded from this schema node."""

    z: Z7130
    """Value decoded from this schema node."""

    z_7135: Z7135
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[X7110]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["x_7115"]) -> _base.FieldRef[X7115]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Y7120]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y_7125"]) -> _base.FieldRef[Y7125]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Z7130]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z_7135"]) -> _base.FieldRef[Z7135]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Specular7140(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload/1:Specular"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/1:S"
                "pecular/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/1:S"
                "pecular/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/1:S"
                "pecular/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/1:S"
                "pecular/3:Unused"
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


class Structure7108(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LGTM/2:Directional Ambient Lighting Colors/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/0:D"
                "irectional"
            ),
            kind="struct",
            name="Directional",
        ),
        "specular": _base.Binding(
            path=(
                "LGTM/2:Directional Ambient Lighting Colors/payload/1:Specular"
            ),
            kind="struct",
            name="Specular",
        ),
        "scale": _base.Binding(
            path=("LGTM/2:Directional Ambient Lighting Colors/payload/2:Scale"),
            kind="primitive",
            name="Scale",
        ),
    }

    directional: Directional7109
    """Value decoded from this schema node."""

    specular: Optional[Specular7140] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["directional"]
    ) -> _base.FieldRef[Directional7109]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular"]
    ) -> _base.FieldRef[Optional[Specular7140]]:
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


class LightingTemplateRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LGTM"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LGTM"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LGTM/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "lighting": _base.Binding(
            path="LGTM/1:Lighting",
            kind="subrecord",
            name="Lighting",
        ),
        "directional_ambient_lighting_colors": _base.Binding(
            path="LGTM/2:Directional Ambient Lighting Colors",
            kind="subrecord",
            name="Directional Ambient Lighting Colors",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    lighting: Optional[Structure7036] = None
    """Value decoded from this schema node."""

    directional_ambient_lighting_colors: Optional[Structure7108] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lighting"]
    ) -> _base.FieldRef[Optional[Structure7036]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["directional_ambient_lighting_colors"]
    ) -> _base.FieldRef[Optional[Structure7108]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
