"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base


class Tint18338(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
        "Data/payload/0:Tint"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/0:Tint/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/0:Tint/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/0:Tint/2:Blue"
            ),
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


class Flags18347(enum.IntFlag):
    """Named values from the pinned schema."""

    ROTATES = 1
    SHRINKS_WHEN_OCCLUDED = 2


class Structure18337(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "tint": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/0:Tint"
            ),
            kind="struct",
            name="Tint",
        ),
        "width": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/1:Width"
            ),
            kind="primitive",
            name="Width",
        ),
        "height": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/2:Height"
            ),
            kind="primitive",
            name="Height",
        ),
        "position": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/3:Position"
            ),
            kind="primitive",
            name="Position",
        ),
        "angular_fade": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/4:Angular Fade"
            ),
            kind="primitive",
            name="Angular Fade",
        ),
        "opacity": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/5:Opacity"
            ),
            kind="primitive",
            name="Opacity",
        ),
        "flags": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare "
                "Data/payload/6:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
    }

    tint: Tint18338
    """Value decoded from this schema node."""

    width: float
    """Value decoded from this schema node."""

    height: float
    """Value decoded from this schema node."""

    position: float
    """Value decoded from this schema node."""

    angular_fade: float
    """Value decoded from this schema node."""

    opacity: float
    """Value decoded from this schema node."""

    flags: Flags18347
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["tint"]) -> _base.FieldRef[Tint18338]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["width"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["angular_fade"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["opacity"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags18347]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flare18331(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LENS/4:Lens Flare Sprites/repeat/0:Flare"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "lens_flare_sprite_id": _base.Binding(
            path=(
                "LENS/4:Lens Flare Sprites/repeat/0:Flare/0:Lens Flare "
                "Sprite ID"
            ),
            kind="subrecord",
            name="Lens Flare Sprite ID",
        ),
        "texture": _base.Binding(
            path=("LENS/4:Lens Flare Sprites/repeat/0:Flare/1:Texture"),
            kind="subrecord",
            name="Texture",
        ),
        "lens_flare_data": _base.Binding(
            path=("LENS/4:Lens Flare Sprites/repeat/0:Flare/2:Lens Flare Data"),
            kind="subrecord",
            name="Lens Flare Data",
        ),
    }

    lens_flare_sprite_id: Optional[str] = None
    """Value decoded from this schema node."""

    texture: Optional[str] = None
    """Value decoded from this schema node."""

    lens_flare_data: Optional[Structure18337] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["lens_flare_sprite_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["texture"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lens_flare_data"]
    ) -> _base.FieldRef[Optional[Structure18337]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LensFlareRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LENS"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LENS"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LENS/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "color_influence": _base.Binding(
            path="LENS/1:Color Influence",
            kind="subrecord",
            name="Color Influence",
        ),
        "fade_distance_radius_scale": _base.Binding(
            path="LENS/2:Fade Distance Radius Scale",
            kind="subrecord",
            name="Fade Distance Radius Scale",
        ),
        "count": _base.Binding(
            path="LENS/3:Count",
            kind="subrecord",
            name="Count",
        ),
        "lens_flare_sprites": _base.Binding(
            path="LENS/4:Lens Flare Sprites",
            kind="repeat",
            name="Lens Flare Sprites",
            repeated_path="LENS/4:Lens Flare Sprites/repeat/0:Flare",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    color_influence: Optional[float] = None
    """Value decoded from this schema node."""

    fade_distance_radius_scale: Optional[float] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    lens_flare_sprites: tuple[Flare18331, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color_influence"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fade_distance_radius_scale"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lens_flare_sprites"]
    ) -> _base.FieldRef[tuple[Flare18331, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
