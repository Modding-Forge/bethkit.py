"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class MembraneShaderSourceBlendMode3384(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ZERO = 1
    ONE = 2
    SOURCE_COLOR = 3
    SOURCE_INVERSE_COLOR = 4
    SOURCE_ALPHA = 5
    SOURCE_INVERTED_ALPHA = 6
    DEST_ALPHA = 7
    DEST_INVERTED_ALPHA = 8
    DEST_COLOR = 9
    DEST_INVERSE_COLOR = 10
    SOURCE_ALPHA_SAT = 11


class MembraneShaderBlendOperation3385(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ADD = 1
    SUBTRACT = 2
    REVERSE_SUBTRACT = 3
    MINIMUM = 4
    MAXIMUM = 5


class MembraneShaderZTestFunction3386(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EQUAL_TO = 3
    NORMAL = 4
    GREATER_THAN = 5
    GREATER_THAN_OR_EQUAL_TO = 7
    ALWAYS_SHOW = 8


class FillTextureEffectColorKey13387(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "EFSH/6:DATA/payload/4:Fill/Texture Effect - Color Key 1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/4:Fill/Texture Effect - Color Key 1/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/4:Fill/Texture Effect - Color Key "
                "1/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/4:Fill/Texture Effect - Color Key 1/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/4:Fill/Texture Effect - Color Key "
                "1/3:Unused"
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


class EdgeEffectColor3401(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EFSH/6:DATA/payload/14:Edge Effect - Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="EFSH/6:DATA/payload/14:Edge Effect - Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("EFSH/6:DATA/payload/14:Edge Effect - Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="EFSH/6:DATA/payload/14:Edge Effect - Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("EFSH/6:DATA/payload/14:Edge Effect - Color/3:Unused"),
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


class MembraneShaderDestBlendMode3414(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ZERO = 1
    ONE = 2
    SOURCE_COLOR = 3
    SOURCE_INVERSE_COLOR = 4
    SOURCE_ALPHA = 5
    SOURCE_INVERTED_ALPHA = 6
    DEST_ALPHA = 7
    DEST_INVERTED_ALPHA = 8
    DEST_COLOR = 9
    DEST_INVERSE_COLOR = 10
    SOURCE_ALPHA_SAT = 11


class ParticleShaderSourceBlendMode3415(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ZERO = 1
    ONE = 2
    SOURCE_COLOR = 3
    SOURCE_INVERSE_COLOR = 4
    SOURCE_ALPHA = 5
    SOURCE_INVERTED_ALPHA = 6
    DEST_ALPHA = 7
    DEST_INVERTED_ALPHA = 8
    DEST_COLOR = 9
    DEST_INVERSE_COLOR = 10
    SOURCE_ALPHA_SAT = 11


class ParticleShaderBlendOperation3416(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ADD = 1
    SUBTRACT = 2
    REVERSE_SUBTRACT = 3
    MINIMUM = 4
    MAXIMUM = 5


class ParticleShaderZTestFunction3417(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EQUAL_TO = 3
    NORMAL = 4
    GREATER_THAN = 5
    GREATER_THAN_OR_EQUAL_TO = 7
    ALWAYS_SHOW = 8


class ParticleShaderDestBlendMode3418(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ZERO = 1
    ONE = 2
    SOURCE_COLOR = 3
    SOURCE_INVERSE_COLOR = 4
    SOURCE_ALPHA = 5
    SOURCE_INVERTED_ALPHA = 6
    DEST_ALPHA = 7
    DEST_INVERTED_ALPHA = 8
    DEST_COLOR = 9
    DEST_INVERSE_COLOR = 10
    SOURCE_ALPHA_SAT = 11


class ColorKey1Color3438(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EFSH/6:DATA/payload/47:Color Key 1 - Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="EFSH/6:DATA/payload/47:Color Key 1 - Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("EFSH/6:DATA/payload/47:Color Key 1 - Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="EFSH/6:DATA/payload/47:Color Key 1 - Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("EFSH/6:DATA/payload/47:Color Key 1 - Color/3:Unused"),
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


class ColorKey2Color3443(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EFSH/6:DATA/payload/48:Color Key 2 - Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="EFSH/6:DATA/payload/48:Color Key 2 - Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("EFSH/6:DATA/payload/48:Color Key 2 - Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="EFSH/6:DATA/payload/48:Color Key 2 - Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("EFSH/6:DATA/payload/48:Color Key 2 - Color/3:Unused"),
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


class ColorKey3Color3448(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EFSH/6:DATA/payload/49:Color Key 3 - Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="EFSH/6:DATA/payload/49:Color Key 3 - Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("EFSH/6:DATA/payload/49:Color Key 3 - Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="EFSH/6:DATA/payload/49:Color Key 3 - Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("EFSH/6:DATA/payload/49:Color Key 3 - Color/3:Unused"),
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


class EdgeColor3470(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EFSH/6:DATA/payload/67:Edge Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="EFSH/6:DATA/payload/67:Edge Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="EFSH/6:DATA/payload/67:Edge Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="EFSH/6:DATA/payload/67:Edge Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="EFSH/6:DATA/payload/67:Edge Color/3:Unused",
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


class FillTextureEffectColorKey23485(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "EFSH/6:DATA/payload/78:Fill/Texture Effect - Color Key 2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/78:Fill/Texture Effect - Color Key 2/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/78:Fill/Texture Effect - Color Key"
                " 2/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/78:Fill/Texture Effect - Color Key"
                " 2/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/78:Fill/Texture Effect - Color Key"
                " 2/3:Unused"
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


class FillTextureEffectColorKey33490(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "EFSH/6:DATA/payload/79:Fill/Texture Effect - Color Key 3"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/79:Fill/Texture Effect - Color Key 3/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/79:Fill/Texture Effect - Color Key"
                " 3/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/79:Fill/Texture Effect - Color Key"
                " 3/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/79:Fill/Texture Effect - Color Key"
                " 3/3:Unused"
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


class FillTextureEffectColorKeyScaleTime3495(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key Scale/Time"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "color_key_1_scale": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key"
                " Scale/Time/0:Color Key 1 - Scale"
            ),
            kind="primitive",
            name="Color Key 1 - Scale",
        ),
        "color_key_2_scale": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key"
                " Scale/Time/1:Color Key 2 - Scale"
            ),
            kind="primitive",
            name="Color Key 2 - Scale",
        ),
        "color_key_3_scale": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key"
                " Scale/Time/2:Color Key 3 - Scale"
            ),
            kind="primitive",
            name="Color Key 3 - Scale",
        ),
        "color_key_1_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key"
                " Scale/Time/3:Color Key 1 - Time"
            ),
            kind="primitive",
            name="Color Key 1 - Time",
        ),
        "color_key_2_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key"
                " Scale/Time/4:Color Key 2 - Time"
            ),
            kind="primitive",
            name="Color Key 2 - Time",
        ),
        "color_key_3_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key"
                " Scale/Time/5:Color Key 3 - Time"
            ),
            kind="primitive",
            name="Color Key 3 - Time",
        ),
    }

    color_key_1_scale: float
    """Value decoded from this schema node."""

    color_key_2_scale: float
    """Value decoded from this schema node."""

    color_key_3_scale: float
    """Value decoded from this schema node."""

    color_key_1_time: float
    """Value decoded from this schema node."""

    color_key_2_time: float
    """Value decoded from this schema node."""

    color_key_3_time: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["color_key_1_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_2_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_3_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["color_key_1_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["color_key_2_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["color_key_3_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ParticleShaderAnimated3505(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "EFSH/6:DATA/payload/84:Particle Shader Animated"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "start_frame": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/84:Particle Shader Animated/0:Start Frame"
            ),
            kind="primitive",
            name="Start Frame",
        ),
        "start_frame_variation": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/84:Particle Shader Animated/1:Star"
                "t Frame Variation"
            ),
            kind="primitive",
            name="Start Frame Variation",
        ),
        "end_frame": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/84:Particle Shader Animated/2:End Frame"
            ),
            kind="primitive",
            name="End Frame",
        ),
        "loop_start_frame": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/84:Particle Shader Animated/3:Loop"
                " Start Frame"
            ),
            kind="primitive",
            name="Loop Start Frame",
        ),
        "loop_start_variation": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/84:Particle Shader Animated/4:Loop"
                " Start Variation"
            ),
            kind="primitive",
            name="Loop Start Variation",
        ),
        "frame_count": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/84:Particle Shader Animated/5:Frame Count"
            ),
            kind="primitive",
            name="Frame Count",
        ),
        "frame_count_variation": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/84:Particle Shader Animated/6:Fram"
                "e Count Variation"
            ),
            kind="primitive",
            name="Frame Count Variation",
        ),
    }

    start_frame: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    start_frame_variation: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    end_frame: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    loop_start_frame: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    loop_start_variation: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    frame_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    frame_count_variation: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["start_frame"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["start_frame_variation"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["end_frame"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["loop_start_frame"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["loop_start_variation"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["frame_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["frame_count_variation"]
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


class Flags3513(enum.IntFlag):
    """Named values from the pinned schema."""

    NO_MEMBRANE_SHADER = 1
    MEMBRANE_GRAYSCALE_COLOR = 2
    MEMBRANE_GRAYSCALE_ALPHA = 4
    NO_PARTICLE_SHADER = 8
    EDGE_EFFECT_INVERSE = 16
    AFFECT_SKIN_ONLY = 32
    IGNORE_ALPHA = 64
    PROJECT_UVS = 128
    IGNORE_BASE_GEOMETRY_ALPHA = 256
    LIGHTING = 512
    NO_WEAPONS = 1024
    UNKNOWN_11 = 2048
    UNKNOWN_12 = 4096
    UNKNOWN_13 = 8192
    UNKNOWN_14 = 16384
    PARTICLE_ANIMATED = 32768
    PARTICLE_GRAYSCALE_COLOR = 65536
    PARTICLE_GRAYSCALE_ALPHA = 131072
    UNKNOWN_18 = 262144
    UNKNOWN_19 = 524288
    UNKNOWN_20 = 1048576
    UNKNOWN_21 = 2097152
    UNKNOWN_22 = 4194304
    UNKNOWN_23 = 8388608
    USE_BLOOD_GEOMETRY = 16777216


class Structure3382(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EFSH/6:DATA/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="EFSH/6:DATA/payload/0:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "membrane_shader_source_blend_mode": _base.Binding(
            path=("EFSH/6:DATA/payload/1:Membrane Shader - Source Blend Mode"),
            kind="primitive",
            name="Membrane Shader - Source Blend Mode",
        ),
        "membrane_shader_blend_operation": _base.Binding(
            path=("EFSH/6:DATA/payload/2:Membrane Shader - Blend Operation"),
            kind="primitive",
            name="Membrane Shader - Blend Operation",
        ),
        "membrane_shader_z_test_function": _base.Binding(
            path=("EFSH/6:DATA/payload/3:Membrane Shader - Z Test Function"),
            kind="primitive",
            name="Membrane Shader - Z Test Function",
        ),
        "fill_texture_effect_color_key_1": _base.Binding(
            path=("EFSH/6:DATA/payload/4:Fill/Texture Effect - Color Key 1"),
            kind="struct",
            name="Fill/Texture Effect - Color Key 1",
        ),
        "fill_texture_effect_alpha_fade_in_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/5:Fill/Texture Effect - Alpha Fade In Time"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Alpha Fade In Time",
        ),
        "fill_texture_effect_full_alpha_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/6:Fill/Texture Effect - Full Alpha Time"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Full Alpha Time",
        ),
        "fill_texture_effect_alpha_fade_out_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/7:Fill/Texture Effect - Alpha Fade"
                " Out Time"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Alpha Fade Out Time",
        ),
        "fill_texture_effect_presistent_alpha_ratio": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/8:Fill/Texture Effect - Presistent"
                " Alpha Ratio"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Presistent Alpha Ratio",
        ),
        "fill_texture_effect_alpha_pulse_amplitude": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/9:Fill/Texture Effect - Alpha Puls"
                "e Amplitude"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Alpha Pulse Amplitude",
        ),
        "fill_texture_effect_alpha_pulse_frequency": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/10:Fill/Texture Effect - Alpha Pul"
                "se Frequency"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Alpha Pulse Frequency",
        ),
        "fill_texture_effect_texture_animation_speed_u": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/11:Fill/Texture Effect - Texture A"
                "nimation Speed (U)"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Texture Animation Speed (U)",
        ),
        "fill_texture_effect_texture_animation_speed_v": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/12:Fill/Texture Effect - Texture A"
                "nimation Speed (V)"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Texture Animation Speed (V)",
        ),
        "edge_effect_fall_off": _base.Binding(
            path="EFSH/6:DATA/payload/13:Edge Effect - Fall Off",
            kind="primitive",
            name="Edge Effect - Fall Off",
        ),
        "edge_effect_color": _base.Binding(
            path="EFSH/6:DATA/payload/14:Edge Effect - Color",
            kind="struct",
            name="Edge Effect - Color",
        ),
        "edge_effect_alpha_fade_in_time": _base.Binding(
            path=("EFSH/6:DATA/payload/15:Edge Effect - Alpha Fade In Time"),
            kind="primitive",
            name="Edge Effect - Alpha Fade In Time",
        ),
        "edge_effect_full_alpha_time": _base.Binding(
            path=("EFSH/6:DATA/payload/16:Edge Effect - Full Alpha Time"),
            kind="primitive",
            name="Edge Effect - Full Alpha Time",
        ),
        "edge_effect_alpha_fade_out_time": _base.Binding(
            path=("EFSH/6:DATA/payload/17:Edge Effect - Alpha Fade Out Time"),
            kind="primitive",
            name="Edge Effect - Alpha Fade Out Time",
        ),
        "edge_effect_persistent_alpha_ratio": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/18:Edge Effect - Persistent Alpha Ratio"
            ),
            kind="primitive",
            name="Edge Effect - Persistent Alpha Ratio",
        ),
        "edge_effect_alpha_pulse_amplitude": _base.Binding(
            path=("EFSH/6:DATA/payload/19:Edge Effect - Alpha Pulse Amplitude"),
            kind="primitive",
            name="Edge Effect - Alpha Pulse Amplitude",
        ),
        "edge_effect_alpha_pulse_frequency": _base.Binding(
            path=("EFSH/6:DATA/payload/20:Edge Effect - Alpha Pulse Frequency"),
            kind="primitive",
            name="Edge Effect - Alpha Pulse Frequency",
        ),
        "fill_texture_effect_full_alpha_ratio": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/21:Fill/Texture Effect - Full Alpha Ratio"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Full Alpha Ratio",
        ),
        "edge_effect_full_alpha_ratio": _base.Binding(
            path=("EFSH/6:DATA/payload/22:Edge Effect - Full Alpha Ratio"),
            kind="primitive",
            name="Edge Effect - Full Alpha Ratio",
        ),
        "membrane_shader_dest_blend_mode": _base.Binding(
            path=("EFSH/6:DATA/payload/23:Membrane Shader - Dest Blend Mode"),
            kind="primitive",
            name="Membrane Shader - Dest Blend Mode",
        ),
        "particle_shader_source_blend_mode": _base.Binding(
            path=("EFSH/6:DATA/payload/24:Particle Shader - Source Blend Mode"),
            kind="primitive",
            name="Particle Shader - Source Blend Mode",
        ),
        "particle_shader_blend_operation": _base.Binding(
            path=("EFSH/6:DATA/payload/25:Particle Shader - Blend Operation"),
            kind="primitive",
            name="Particle Shader - Blend Operation",
        ),
        "particle_shader_z_test_function": _base.Binding(
            path=("EFSH/6:DATA/payload/26:Particle Shader - Z Test Function"),
            kind="primitive",
            name="Particle Shader - Z Test Function",
        ),
        "particle_shader_dest_blend_mode": _base.Binding(
            path=("EFSH/6:DATA/payload/27:Particle Shader - Dest Blend Mode"),
            kind="primitive",
            name="Particle Shader - Dest Blend Mode",
        ),
        "particle_shader_particle_birth_ramp_up_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/28:Particle Shader - Particle Birt"
                "h Ramp Up Time"
            ),
            kind="primitive",
            name="Particle Shader - Particle Birth Ramp Up Time",
        ),
        "particle_shader_full_particle_birth_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/29:Particle Shader - Full Particle"
                " Birth Time"
            ),
            kind="primitive",
            name="Particle Shader - Full Particle Birth Time",
        ),
        "particle_shader_particle_birth_ramp_down_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/30:Particle Shader - Particle Birt"
                "h Ramp Down Time"
            ),
            kind="primitive",
            name="Particle Shader - Particle Birth Ramp Down Time",
        ),
        "particle_shader_full_particle_birth_ratio": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/31:Particle Shader - Full Particle"
                " Birth Ratio"
            ),
            kind="primitive",
            name="Particle Shader - Full Particle Birth Ratio",
        ),
        "particle_shader_persistant_particle_count": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/32:Particle Shader - Persistant Pa"
                "rticle Count"
            ),
            kind="primitive",
            name="Particle Shader - Persistant Particle Count",
        ),
        "particle_shader_particle_lifetime": _base.Binding(
            path=("EFSH/6:DATA/payload/33:Particle Shader - Particle Lifetime"),
            kind="primitive",
            name="Particle Shader - Particle Lifetime",
        ),
        "particle_shader_particle_lifetime_3425": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/34:Particle Shader - Particle Lifetime +/-"
            ),
            kind="primitive",
            name="Particle Shader - Particle Lifetime +/-",
        ),
        "particle_shader_initial_speed_along_normal": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/35:Particle Shader - Initial Speed"
                " Along Normal"
            ),
            kind="primitive",
            name="Particle Shader - Initial Speed Along Normal",
        ),
        "particle_shader_acceleration_along_normal": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/36:Particle Shader - Acceleration "
                "Along Normal"
            ),
            kind="primitive",
            name="Particle Shader - Acceleration Along Normal",
        ),
        "particle_shader_initial_velocity_1": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/37:Particle Shader - Initial Velocity #1"
            ),
            kind="primitive",
            name="Particle Shader - Initial Velocity #1",
        ),
        "particle_shader_initial_velocity_2": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/38:Particle Shader - Initial Velocity #2"
            ),
            kind="primitive",
            name="Particle Shader - Initial Velocity #2",
        ),
        "particle_shader_initial_velocity_3": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/39:Particle Shader - Initial Velocity #3"
            ),
            kind="primitive",
            name="Particle Shader - Initial Velocity #3",
        ),
        "particle_shader_acceleration_1": _base.Binding(
            path=("EFSH/6:DATA/payload/40:Particle Shader - Acceleration #1"),
            kind="primitive",
            name="Particle Shader - Acceleration #1",
        ),
        "particle_shader_acceleration_2": _base.Binding(
            path=("EFSH/6:DATA/payload/41:Particle Shader - Acceleration #2"),
            kind="primitive",
            name="Particle Shader - Acceleration #2",
        ),
        "particle_shader_acceleration_3": _base.Binding(
            path=("EFSH/6:DATA/payload/42:Particle Shader - Acceleration #3"),
            kind="primitive",
            name="Particle Shader - Acceleration #3",
        ),
        "particle_shader_scale_key_1": _base.Binding(
            path=("EFSH/6:DATA/payload/43:Particle Shader - Scale Key 1"),
            kind="primitive",
            name="Particle Shader - Scale Key 1",
        ),
        "particle_shader_scale_key_2": _base.Binding(
            path=("EFSH/6:DATA/payload/44:Particle Shader - Scale Key 2"),
            kind="primitive",
            name="Particle Shader - Scale Key 2",
        ),
        "particle_shader_scale_key_1_time": _base.Binding(
            path=("EFSH/6:DATA/payload/45:Particle Shader - Scale Key 1 Time"),
            kind="primitive",
            name="Particle Shader - Scale Key 1 Time",
        ),
        "particle_shader_scale_key_2_time": _base.Binding(
            path=("EFSH/6:DATA/payload/46:Particle Shader - Scale Key 2 Time"),
            kind="primitive",
            name="Particle Shader - Scale Key 2 Time",
        ),
        "color_key_1_color": _base.Binding(
            path="EFSH/6:DATA/payload/47:Color Key 1 - Color",
            kind="struct",
            name="Color Key 1 - Color",
        ),
        "color_key_2_color": _base.Binding(
            path="EFSH/6:DATA/payload/48:Color Key 2 - Color",
            kind="struct",
            name="Color Key 2 - Color",
        ),
        "color_key_3_color": _base.Binding(
            path="EFSH/6:DATA/payload/49:Color Key 3 - Color",
            kind="struct",
            name="Color Key 3 - Color",
        ),
        "color_key_1_color_alpha": _base.Binding(
            path="EFSH/6:DATA/payload/50:Color Key 1 - Color Alpha",
            kind="primitive",
            name="Color Key 1 - Color Alpha",
        ),
        "color_key_2_color_alpha": _base.Binding(
            path="EFSH/6:DATA/payload/51:Color Key 2 - Color Alpha",
            kind="primitive",
            name="Color Key 2 - Color Alpha",
        ),
        "color_key_3_color_alpha": _base.Binding(
            path="EFSH/6:DATA/payload/52:Color Key 3 - Color Alpha",
            kind="primitive",
            name="Color Key 3 - Color Alpha",
        ),
        "color_key_1_color_key_time": _base.Binding(
            path=("EFSH/6:DATA/payload/53:Color Key 1 - Color Key Time"),
            kind="primitive",
            name="Color Key 1 - Color Key Time",
        ),
        "color_key_2_color_key_time": _base.Binding(
            path=("EFSH/6:DATA/payload/54:Color Key 2 - Color Key Time"),
            kind="primitive",
            name="Color Key 2 - Color Key Time",
        ),
        "color_key_3_color_key_time": _base.Binding(
            path=("EFSH/6:DATA/payload/55:Color Key 3 - Color Key Time"),
            kind="primitive",
            name="Color Key 3 - Color Key Time",
        ),
        "particle_shader_initial_speed_along_normal_3459": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/56:Particle Shader - Initial Speed"
                " Along Normal +/-"
            ),
            kind="primitive",
            name="Particle Shader - Initial Speed Along Normal +/-",
        ),
        "particle_shader_initial_rotation_deg": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/57:Particle Shader - Initial Rotat"
                "ion (deg)"
            ),
            kind="primitive",
            name="Particle Shader - Initial Rotation (deg)",
        ),
        "particle_shader_initial_rotation_deg_3461": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/58:Particle Shader - Initial Rotat"
                "ion (deg) +/-"
            ),
            kind="primitive",
            name="Particle Shader - Initial Rotation (deg) +/-",
        ),
        "particle_shader_rotation_speed_deg_sec": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/59:Particle Shader - Rotation Spee"
                "d (deg/sec)"
            ),
            kind="primitive",
            name="Particle Shader - Rotation Speed (deg/sec)",
        ),
        "particle_shader_rotation_speed_deg_sec_3463": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/60:Particle Shader - Rotation Spee"
                "d (deg/sec) +/-"
            ),
            kind="primitive",
            name="Particle Shader - Rotation Speed (deg/sec) +/-",
        ),
        "addon_models": _base.Binding(
            path="EFSH/6:DATA/payload/61:Addon Models",
            kind="primitive",
            name="Addon Models",
        ),
        "holes_start_time": _base.Binding(
            path="EFSH/6:DATA/payload/62:Holes - Start Time",
            kind="primitive",
            name="Holes - Start Time",
        ),
        "holes_end_time": _base.Binding(
            path="EFSH/6:DATA/payload/63:Holes - End Time",
            kind="primitive",
            name="Holes - End Time",
        ),
        "holes_start_val": _base.Binding(
            path="EFSH/6:DATA/payload/64:Holes - Start Val",
            kind="primitive",
            name="Holes - Start Val",
        ),
        "holes_end_val": _base.Binding(
            path="EFSH/6:DATA/payload/65:Holes - End Val",
            kind="primitive",
            name="Holes - End Val",
        ),
        "edge_width_alpha_units": _base.Binding(
            path="EFSH/6:DATA/payload/66:Edge Width (alpha units)",
            kind="primitive",
            name="Edge Width (alpha units)",
        ),
        "edge_color": _base.Binding(
            path="EFSH/6:DATA/payload/67:Edge Color",
            kind="struct",
            name="Edge Color",
        ),
        "explosion_wind_speed": _base.Binding(
            path="EFSH/6:DATA/payload/68:Explosion Wind Speed",
            kind="primitive",
            name="Explosion Wind Speed",
        ),
        "texture_count_u": _base.Binding(
            path="EFSH/6:DATA/payload/69:Texture Count U",
            kind="primitive",
            name="Texture Count U",
        ),
        "texture_count_v": _base.Binding(
            path="EFSH/6:DATA/payload/70:Texture Count V",
            kind="primitive",
            name="Texture Count V",
        ),
        "addon_models_fade_in_time": _base.Binding(
            path=("EFSH/6:DATA/payload/71:Addon Models - Fade In Time"),
            kind="primitive",
            name="Addon Models - Fade In Time",
        ),
        "addon_models_fade_out_time": _base.Binding(
            path=("EFSH/6:DATA/payload/72:Addon Models - Fade Out Time"),
            kind="primitive",
            name="Addon Models - Fade Out Time",
        ),
        "addon_models_scale_start": _base.Binding(
            path="EFSH/6:DATA/payload/73:Addon Models - Scale Start",
            kind="primitive",
            name="Addon Models - Scale Start",
        ),
        "addon_models_scale_end": _base.Binding(
            path="EFSH/6:DATA/payload/74:Addon Models - Scale End",
            kind="primitive",
            name="Addon Models - Scale End",
        ),
        "addon_models_scale_in_time": _base.Binding(
            path=("EFSH/6:DATA/payload/75:Addon Models - Scale In Time"),
            kind="primitive",
            name="Addon Models - Scale In Time",
        ),
        "addon_models_scale_out_time": _base.Binding(
            path=("EFSH/6:DATA/payload/76:Addon Models - Scale Out Time"),
            kind="primitive",
            name="Addon Models - Scale Out Time",
        ),
        "ambient_sound": _base.Binding(
            path="EFSH/6:DATA/payload/77:Ambient Sound",
            kind="primitive",
            name="Ambient Sound",
        ),
        "fill_texture_effect_color_key_2": _base.Binding(
            path=("EFSH/6:DATA/payload/78:Fill/Texture Effect - Color Key 2"),
            kind="struct",
            name="Fill/Texture Effect - Color Key 2",
        ),
        "fill_texture_effect_color_key_3": _base.Binding(
            path=("EFSH/6:DATA/payload/79:Fill/Texture Effect - Color Key 3"),
            kind="struct",
            name="Fill/Texture Effect - Color Key 3",
        ),
        "fill_texture_effect_color_key_scale_time": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/80:Fill/Texture Effect - Color Key"
                " Scale/Time"
            ),
            kind="struct",
            name="Fill/Texture Effect - Color Key Scale/Time",
        ),
        "color_scale": _base.Binding(
            path="EFSH/6:DATA/payload/81:Color Scale",
            kind="primitive",
            name="Color Scale",
        ),
        "birth_position_offset": _base.Binding(
            path="EFSH/6:DATA/payload/82:Birth Position Offset",
            kind="primitive",
            name="Birth Position Offset",
        ),
        "birth_position_offset_range": _base.Binding(
            path=("EFSH/6:DATA/payload/83:Birth Position Offset Range +/-"),
            kind="primitive",
            name="Birth Position Offset Range +/-",
        ),
        "particle_shader_animated": _base.Binding(
            path="EFSH/6:DATA/payload/84:Particle Shader Animated",
            kind="struct",
            name="Particle Shader Animated",
        ),
        "flags": _base.Binding(
            path="EFSH/6:DATA/payload/85:Flags",
            kind="primitive",
            name="Flags",
        ),
        "fill_texture_effect_texture_scale_u": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/86:Fill/Texture Effect - Texture Scale (U)"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Texture Scale (U)",
        ),
        "fill_texture_effect_texture_scale_v": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/87:Fill/Texture Effect - Texture Scale (V)"
            ),
            kind="primitive",
            name="Fill/Texture Effect - Texture Scale (V)",
        ),
        "scene_graph_emit_depth_limit_unused": _base.Binding(
            path=(
                "EFSH/6:DATA/payload/88:Scene Graph Emit Depth Limit (unused)"
            ),
            kind="primitive",
            name="Scene Graph Emit Depth Limit (unused)",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    membrane_shader_source_blend_mode: Optional[
        MembraneShaderSourceBlendMode3384
    ] = None
    """Value decoded from this schema node."""

    membrane_shader_blend_operation: Optional[
        MembraneShaderBlendOperation3385
    ] = None
    """Value decoded from this schema node."""

    membrane_shader_z_test_function: Optional[
        MembraneShaderZTestFunction3386
    ] = None
    """Value decoded from this schema node."""

    fill_texture_effect_color_key_1: Optional[
        FillTextureEffectColorKey13387
    ] = None
    """Value decoded from this schema node."""

    fill_texture_effect_alpha_fade_in_time: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_full_alpha_time: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_alpha_fade_out_time: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_presistent_alpha_ratio: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_alpha_pulse_amplitude: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_alpha_pulse_frequency: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_texture_animation_speed_u: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_texture_animation_speed_v: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_fall_off: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_color: Optional[EdgeEffectColor3401] = None
    """Value decoded from this schema node."""

    edge_effect_alpha_fade_in_time: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_full_alpha_time: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_alpha_fade_out_time: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_persistent_alpha_ratio: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_alpha_pulse_amplitude: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_alpha_pulse_frequency: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_full_alpha_ratio: Optional[float] = None
    """Value decoded from this schema node."""

    edge_effect_full_alpha_ratio: Optional[float] = None
    """Value decoded from this schema node."""

    membrane_shader_dest_blend_mode: Optional[
        MembraneShaderDestBlendMode3414
    ] = None
    """Value decoded from this schema node."""

    particle_shader_source_blend_mode: Optional[
        ParticleShaderSourceBlendMode3415
    ] = None
    """Value decoded from this schema node."""

    particle_shader_blend_operation: Optional[
        ParticleShaderBlendOperation3416
    ] = None
    """Value decoded from this schema node."""

    particle_shader_z_test_function: Optional[
        ParticleShaderZTestFunction3417
    ] = None
    """Value decoded from this schema node."""

    particle_shader_dest_blend_mode: Optional[
        ParticleShaderDestBlendMode3418
    ] = None
    """Value decoded from this schema node."""

    particle_shader_particle_birth_ramp_up_time: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_full_particle_birth_time: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_particle_birth_ramp_down_time: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_full_particle_birth_ratio: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_persistant_particle_count: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_particle_lifetime: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_particle_lifetime_3425: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_initial_speed_along_normal: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_acceleration_along_normal: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_initial_velocity_1: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_initial_velocity_2: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_initial_velocity_3: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_acceleration_1: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_acceleration_2: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_acceleration_3: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_scale_key_1: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_scale_key_2: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_scale_key_1_time: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_scale_key_2_time: Optional[float] = None
    """Value decoded from this schema node."""

    color_key_1_color: Optional[ColorKey1Color3438] = None
    """Value decoded from this schema node."""

    color_key_2_color: Optional[ColorKey2Color3443] = None
    """Value decoded from this schema node."""

    color_key_3_color: Optional[ColorKey3Color3448] = None
    """Value decoded from this schema node."""

    color_key_1_color_alpha: Optional[float] = None
    """Value decoded from this schema node."""

    color_key_2_color_alpha: Optional[float] = None
    """Value decoded from this schema node."""

    color_key_3_color_alpha: Optional[float] = None
    """Value decoded from this schema node."""

    color_key_1_color_key_time: Optional[float] = None
    """Value decoded from this schema node."""

    color_key_2_color_key_time: Optional[float] = None
    """Value decoded from this schema node."""

    color_key_3_color_key_time: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_initial_speed_along_normal_3459: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_initial_rotation_deg: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_initial_rotation_deg_3461: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_rotation_speed_deg_sec: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_rotation_speed_deg_sec_3463: Optional[float] = None
    """Value decoded from this schema node."""

    addon_models: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    holes_start_time: Optional[float] = None
    """Value decoded from this schema node."""

    holes_end_time: Optional[float] = None
    """Value decoded from this schema node."""

    holes_start_val: Optional[float] = None
    """Value decoded from this schema node."""

    holes_end_val: Optional[float] = None
    """Value decoded from this schema node."""

    edge_width_alpha_units: Optional[float] = None
    """Value decoded from this schema node."""

    edge_color: Optional[EdgeColor3470] = None
    """Value decoded from this schema node."""

    explosion_wind_speed: Optional[float] = None
    """Value decoded from this schema node."""

    texture_count_u: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    texture_count_v: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    addon_models_fade_in_time: Optional[float] = None
    """Value decoded from this schema node."""

    addon_models_fade_out_time: Optional[float] = None
    """Value decoded from this schema node."""

    addon_models_scale_start: Optional[float] = None
    """Value decoded from this schema node."""

    addon_models_scale_end: Optional[float] = None
    """Value decoded from this schema node."""

    addon_models_scale_in_time: Optional[float] = None
    """Value decoded from this schema node."""

    addon_models_scale_out_time: Optional[float] = None
    """Value decoded from this schema node."""

    ambient_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    fill_texture_effect_color_key_2: Optional[
        FillTextureEffectColorKey23485
    ] = None
    """Value decoded from this schema node."""

    fill_texture_effect_color_key_3: Optional[
        FillTextureEffectColorKey33490
    ] = None
    """Value decoded from this schema node."""

    fill_texture_effect_color_key_scale_time: Optional[
        FillTextureEffectColorKeyScaleTime3495
    ] = None
    """Value decoded from this schema node."""

    color_scale: Optional[float] = None
    """Value decoded from this schema node."""

    birth_position_offset: Optional[float] = None
    """Value decoded from this schema node."""

    birth_position_offset_range: Optional[float] = None
    """Value decoded from this schema node."""

    particle_shader_animated: Optional[ParticleShaderAnimated3505] = None
    """Value decoded from this schema node."""

    flags: Optional[Flags3513] = None
    """Value decoded from this schema node."""

    fill_texture_effect_texture_scale_u: Optional[float] = None
    """Value decoded from this schema node."""

    fill_texture_effect_texture_scale_v: Optional[float] = None
    """Value decoded from this schema node."""

    scene_graph_emit_depth_limit_unused: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["membrane_shader_source_blend_mode"]
    ) -> _base.FieldRef[Optional[MembraneShaderSourceBlendMode3384]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["membrane_shader_blend_operation"]
    ) -> _base.FieldRef[Optional[MembraneShaderBlendOperation3385]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["membrane_shader_z_test_function"]
    ) -> _base.FieldRef[Optional[MembraneShaderZTestFunction3386]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_color_key_1"]
    ) -> _base.FieldRef[Optional[FillTextureEffectColorKey13387]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_alpha_fade_in_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_full_alpha_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_alpha_fade_out_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_presistent_alpha_ratio"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_alpha_pulse_amplitude"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_alpha_pulse_frequency"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_texture_animation_speed_u"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_texture_animation_speed_v"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_fall_off"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_color"]
    ) -> _base.FieldRef[Optional[EdgeEffectColor3401]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_alpha_fade_in_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_full_alpha_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_alpha_fade_out_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_persistent_alpha_ratio"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_alpha_pulse_amplitude"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_alpha_pulse_frequency"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_full_alpha_ratio"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_effect_full_alpha_ratio"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["membrane_shader_dest_blend_mode"]
    ) -> _base.FieldRef[Optional[MembraneShaderDestBlendMode3414]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_source_blend_mode"]
    ) -> _base.FieldRef[Optional[ParticleShaderSourceBlendMode3415]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_blend_operation"]
    ) -> _base.FieldRef[Optional[ParticleShaderBlendOperation3416]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_z_test_function"]
    ) -> _base.FieldRef[Optional[ParticleShaderZTestFunction3417]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_dest_blend_mode"]
    ) -> _base.FieldRef[Optional[ParticleShaderDestBlendMode3418]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_particle_birth_ramp_up_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_full_particle_birth_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_particle_birth_ramp_down_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_full_particle_birth_ratio"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_persistant_particle_count"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_particle_lifetime"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_particle_lifetime_3425"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_initial_speed_along_normal"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_acceleration_along_normal"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_initial_velocity_1"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_initial_velocity_2"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_initial_velocity_3"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_acceleration_1"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_acceleration_2"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_acceleration_3"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_scale_key_1"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_scale_key_2"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_scale_key_1_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_scale_key_2_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_1_color"]
    ) -> _base.FieldRef[Optional[ColorKey1Color3438]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_2_color"]
    ) -> _base.FieldRef[Optional[ColorKey2Color3443]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_3_color"]
    ) -> _base.FieldRef[Optional[ColorKey3Color3448]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_1_color_alpha"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_2_color_alpha"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_3_color_alpha"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_1_color_key_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_2_color_key_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_key_3_color_key_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_initial_speed_along_normal_3459"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_initial_rotation_deg"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_initial_rotation_deg_3461"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_rotation_speed_deg_sec"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_rotation_speed_deg_sec_3463"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addon_models"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["holes_start_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["holes_end_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["holes_start_val"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["holes_end_val"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_width_alpha_units"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_color"]
    ) -> _base.FieldRef[Optional[EdgeColor3470]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explosion_wind_speed"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["texture_count_u"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["texture_count_v"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addon_models_fade_in_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addon_models_fade_out_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addon_models_scale_start"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addon_models_scale_end"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addon_models_scale_in_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addon_models_scale_out_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ambient_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_color_key_2"]
    ) -> _base.FieldRef[Optional[FillTextureEffectColorKey23485]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_color_key_3"]
    ) -> _base.FieldRef[Optional[FillTextureEffectColorKey33490]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_color_key_scale_time"]
    ) -> _base.FieldRef[Optional[FillTextureEffectColorKeyScaleTime3495]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_scale"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["birth_position_offset"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["birth_position_offset_range"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_animated"]
    ) -> _base.FieldRef[Optional[ParticleShaderAnimated3505]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[Flags3513]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_texture_scale_u"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture_effect_texture_scale_v"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["scene_graph_emit_depth_limit_unused"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class EffectShaderRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EFSH"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "EFSH"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="EFSH/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "fill_texture": _base.Binding(
            path="EFSH/1:Fill Texture",
            kind="subrecord",
            name="Fill Texture",
        ),
        "particle_shader_texture": _base.Binding(
            path="EFSH/2:Particle Shader Texture",
            kind="subrecord",
            name="Particle Shader Texture",
        ),
        "holes_texture": _base.Binding(
            path="EFSH/3:Holes Texture",
            kind="subrecord",
            name="Holes Texture",
        ),
        "membrane_palette_texture": _base.Binding(
            path="EFSH/4:Membrane Palette Texture",
            kind="subrecord",
            name="Membrane Palette Texture",
        ),
        "particle_palette_texture": _base.Binding(
            path="EFSH/5:Particle Palette Texture",
            kind="subrecord",
            name="Particle Palette Texture",
        ),
        "data": _base.Binding(
            path="EFSH/6:DATA",
            kind="subrecord",
            name="DATA",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    fill_texture: Optional[str] = None
    """Value decoded from this schema node."""

    particle_shader_texture: Optional[str] = None
    """Value decoded from this schema node."""

    holes_texture: Optional[str] = None
    """Value decoded from this schema node."""

    membrane_palette_texture: Optional[str] = None
    """Value decoded from this schema node."""

    particle_palette_texture: Optional[str] = None
    """Value decoded from this schema node."""

    data: Optional[Structure3382] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fill_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_shader_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["holes_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["membrane_palette_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["particle_palette_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure3382]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
