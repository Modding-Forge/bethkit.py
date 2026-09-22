"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base


class Structure4213(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TXST/1:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="TXST/1:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="TXST/1:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="TXST/1:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="TXST/1:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="TXST/1:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="TXST/1:Object Bounds/payload/5:Z2",
            kind="primitive",
            name="Z2",
        ),
    }

    x1: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y1: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    z1: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    x2: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y2: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    z2: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x1"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y1"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z1"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["x2"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y2"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z2"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class TexturesRgbA4220(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TXST/2:Textures (RGB/A)"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "diffuse": _base.Binding(
            path="TXST/2:Textures (RGB/A)/0:Diffuse",
            kind="subrecord",
            name="Diffuse",
        ),
        "normal_gloss": _base.Binding(
            path="TXST/2:Textures (RGB/A)/1:Normal/Gloss",
            kind="subrecord",
            name="Normal/Gloss",
        ),
        "environment_mask_subsurface_tint": _base.Binding(
            path=("TXST/2:Textures (RGB/A)/2:Environment Mask/Subsurface Tint"),
            kind="subrecord",
            name="Environment Mask/Subsurface Tint",
        ),
        "glow_detail_map": _base.Binding(
            path="TXST/2:Textures (RGB/A)/3:Glow/Detail Map",
            kind="subrecord",
            name="Glow/Detail Map",
        ),
        "height": _base.Binding(
            path="TXST/2:Textures (RGB/A)/4:Height",
            kind="subrecord",
            name="Height",
        ),
        "environment": _base.Binding(
            path="TXST/2:Textures (RGB/A)/5:Environment",
            kind="subrecord",
            name="Environment",
        ),
        "multilayer": _base.Binding(
            path="TXST/2:Textures (RGB/A)/6:Multilayer",
            kind="subrecord",
            name="Multilayer",
        ),
        "backlight_mask_specular": _base.Binding(
            path="TXST/2:Textures (RGB/A)/7:Backlight Mask/Specular",
            kind="subrecord",
            name="Backlight Mask/Specular",
        ),
    }

    diffuse: Optional[str] = None
    """Value decoded from this schema node."""

    normal_gloss: Optional[str] = None
    """Value decoded from this schema node."""

    environment_mask_subsurface_tint: Optional[str] = None
    """Value decoded from this schema node."""

    glow_detail_map: Optional[str] = None
    """Value decoded from this schema node."""

    height: Optional[str] = None
    """Value decoded from this schema node."""

    environment: Optional[str] = None
    """Value decoded from this schema node."""

    multilayer: Optional[str] = None
    """Value decoded from this schema node."""

    backlight_mask_specular: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["diffuse"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["normal_gloss"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["environment_mask_subsurface_tint"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["glow_detail_map"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["height"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["environment"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["multilayer"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["backlight_mask_specular"]
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


class Parallax4245(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TXST/3:Decal Data/payload/6:Parallax"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "scale": _base.Binding(
            path="TXST/3:Decal Data/payload/6:Parallax/0:Scale",
            kind="primitive",
            name="Scale",
        ),
        "passes": _base.Binding(
            path="TXST/3:Decal Data/payload/6:Parallax/1:Passes",
            kind="primitive",
            name="Passes",
        ),
    }

    scale: float
    """Value decoded from this schema node."""

    passes: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["passes"]
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


class Flags4248(enum.IntFlag):
    """Named values from the pinned schema."""

    PARALLAX = 1
    ALPHA_BLENDING = 2
    ALPHA_TESTING = 4
    NO_SUBTEXTURES = 8


class Color4250(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TXST/3:Decal Data/payload/9:Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="TXST/3:Decal Data/payload/9:Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="TXST/3:Decal Data/payload/9:Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="TXST/3:Decal Data/payload/9:Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="TXST/3:Decal Data/payload/9:Color/3:Unused",
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


class Structure4238(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TXST/3:Decal Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "min_width": _base.Binding(
            path="TXST/3:Decal Data/payload/0:Min Width",
            kind="primitive",
            name="Min Width",
        ),
        "max_width": _base.Binding(
            path="TXST/3:Decal Data/payload/1:Max Width",
            kind="primitive",
            name="Max Width",
        ),
        "min_height": _base.Binding(
            path="TXST/3:Decal Data/payload/2:Min Height",
            kind="primitive",
            name="Min Height",
        ),
        "max_height": _base.Binding(
            path="TXST/3:Decal Data/payload/3:Max Height",
            kind="primitive",
            name="Max Height",
        ),
        "depth": _base.Binding(
            path="TXST/3:Decal Data/payload/4:Depth",
            kind="primitive",
            name="Depth",
        ),
        "shininess": _base.Binding(
            path="TXST/3:Decal Data/payload/5:Shininess",
            kind="primitive",
            name="Shininess",
        ),
        "parallax": _base.Binding(
            path="TXST/3:Decal Data/payload/6:Parallax",
            kind="struct",
            name="Parallax",
        ),
        "flags": _base.Binding(
            path="TXST/3:Decal Data/payload/7:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unknown": _base.Binding(
            path="TXST/3:Decal Data/payload/8:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "color": _base.Binding(
            path="TXST/3:Decal Data/payload/9:Color",
            kind="struct",
            name="Color",
        ),
    }

    min_width: float
    """Value decoded from this schema node."""

    max_width: float
    """Value decoded from this schema node."""

    min_height: float
    """Value decoded from this schema node."""

    max_height: float
    """Value decoded from this schema node."""

    depth: float
    """Value decoded from this schema node."""

    shininess: float
    """Value decoded from this schema node."""

    parallax: Parallax4245
    """Value decoded from this schema node."""

    flags: Flags4248
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    color: Color4250
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["min_width"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_width"]) -> _base.FieldRef[float]:
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
    def field(self, name: Literal["depth"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["shininess"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["parallax"]) -> _base.FieldRef[Parallax4245]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags4248]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["color"]) -> _base.FieldRef[Color4250]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class NoSpecularMapFacegenTexturesHasModelSpB49A22134256(enum.IntFlag):
    """Named values from the pinned schema."""

    NO_SPECULAR_MAP = 1
    FACEGEN_TEXTURES = 2
    HAS_MODEL_SPACE_NORMAL_MAP = 4


class TextureSetRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TXST"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "TXST"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="TXST/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "object_bounds": _base.Binding(
            path="TXST/1:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "textures_rgb_a": _base.Binding(
            path="TXST/2:Textures (RGB/A)",
            kind="sequence",
            name="Textures (RGB/A)",
        ),
        "decal_data": _base.Binding(
            path="TXST/3:Decal Data",
            kind="subrecord",
            name="Decal Data",
        ),
        "flags": _base.Binding(
            path="TXST/4:Flags",
            kind="subrecord",
            name="Flags",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure4213] = None
    """Value decoded from this schema node."""

    textures_rgb_a: Optional[TexturesRgbA4220] = None
    """Value decoded from this schema node."""

    decal_data: Optional[Structure4238] = None
    """Value decoded from this schema node."""

    flags: Optional[NoSpecularMapFacegenTexturesHasModelSpB49A22134256] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[Structure4213]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures_rgb_a"]
    ) -> _base.FieldRef[Optional[TexturesRgbA4220]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["decal_data"]
    ) -> _base.FieldRef[Optional[Structure4238]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[NoSpecularMapFacegenTexturesHasModelSpB49A22134256]
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
