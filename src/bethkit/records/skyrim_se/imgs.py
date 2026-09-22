"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

from .. import _base, _values

_VARIANT_5256: _base.Variant = _base.Variant(
    path="IMGS/1:ENAM/payload/variants/0:Unknown"
)


class Unknown5257(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMGS/1:ENAM/payload/variants/1:unknown"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "eye_adapt_speed": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/0:Eye Adapt Speed"),
            kind="primitive",
            name="Eye Adapt Speed",
        ),
        "bloom_blur_radius": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/1:Bloom Blur Radius"),
            kind="primitive",
            name="Bloom Blur Radius",
        ),
        "bloom_threshold": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/2:Bloom Threshold"),
            kind="primitive",
            name="Bloom Threshold",
        ),
        "bloom_scale": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/3:Bloom Scale"),
            kind="primitive",
            name="Bloom Scale",
        ),
        "receive_bloom_threshold": _base.Binding(
            path=(
                "IMGS/1:ENAM/payload/variants/1:unknown/4:Receive Bloom"
                " Threshold"
            ),
            kind="primitive",
            name="Receive Bloom Threshold",
        ),
        "sunlight_scale": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/5:Sunlight Scale"),
            kind="primitive",
            name="Sunlight Scale",
        ),
        "sky_scale": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/6:Sky Scale"),
            kind="primitive",
            name="Sky Scale",
        ),
        "saturation": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/7:Saturation"),
            kind="primitive",
            name="Saturation",
        ),
        "brightness": _base.Binding(
            path=("IMGS/1:ENAM/payload/variants/1:unknown/8:Brightness"),
            kind="primitive",
            name="Brightness",
        ),
        "contrast": _base.Binding(
            path="IMGS/1:ENAM/payload/variants/1:unknown/9:Contrast",
            kind="primitive",
            name="Contrast",
        ),
        "unknown": _base.Binding(
            path="IMGS/1:ENAM/payload/variants/1:unknown/10:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    eye_adapt_speed: float
    """Value decoded from this schema node."""

    bloom_blur_radius: float
    """Value decoded from this schema node."""

    bloom_threshold: float
    """Value decoded from this schema node."""

    bloom_scale: float
    """Value decoded from this schema node."""

    receive_bloom_threshold: float
    """Value decoded from this schema node."""

    sunlight_scale: float
    """Value decoded from this schema node."""

    sky_scale: float
    """Value decoded from this schema node."""

    saturation: float
    """Value decoded from this schema node."""

    brightness: float
    """Value decoded from this schema node."""

    contrast: float
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["eye_adapt_speed"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_blur_radius"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bloom_threshold"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bloom_scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["receive_bloom_threshold"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunlight_scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sky_scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["saturation"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["brightness"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["contrast"]) -> _base.FieldRef[float]:
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


_VARIANT_5257: _base.Variant = _base.Variant(
    path="IMGS/1:ENAM/payload/variants/1:unknown"
)


class Structure5270(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMGS/2:HDR/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "eye_adapt_speed": _base.Binding(
            path="IMGS/2:HDR/payload/0:Eye Adapt Speed",
            kind="primitive",
            name="Eye Adapt Speed",
        ),
        "bloom_blur_radius": _base.Binding(
            path="IMGS/2:HDR/payload/1:Bloom Blur Radius",
            kind="primitive",
            name="Bloom Blur Radius",
        ),
        "bloom_threshold": _base.Binding(
            path="IMGS/2:HDR/payload/2:Bloom Threshold",
            kind="primitive",
            name="Bloom Threshold",
        ),
        "bloom_scale": _base.Binding(
            path="IMGS/2:HDR/payload/3:Bloom Scale",
            kind="primitive",
            name="Bloom Scale",
        ),
        "receive_bloom_threshold": _base.Binding(
            path="IMGS/2:HDR/payload/4:Receive Bloom Threshold",
            kind="primitive",
            name="Receive Bloom Threshold",
        ),
        "white": _base.Binding(
            path="IMGS/2:HDR/payload/5:White",
            kind="primitive",
            name="White",
        ),
        "sunlight_scale": _base.Binding(
            path="IMGS/2:HDR/payload/6:Sunlight Scale",
            kind="primitive",
            name="Sunlight Scale",
        ),
        "sky_scale": _base.Binding(
            path="IMGS/2:HDR/payload/7:Sky Scale",
            kind="primitive",
            name="Sky Scale",
        ),
        "eye_adapt_strength": _base.Binding(
            path="IMGS/2:HDR/payload/8:Eye Adapt Strength",
            kind="primitive",
            name="Eye Adapt Strength",
        ),
    }

    eye_adapt_speed: float
    """Value decoded from this schema node."""

    bloom_blur_radius: float
    """Value decoded from this schema node."""

    bloom_threshold: float
    """Value decoded from this schema node."""

    bloom_scale: float
    """Value decoded from this schema node."""

    receive_bloom_threshold: float
    """Value decoded from this schema node."""

    white: float
    """Value decoded from this schema node."""

    sunlight_scale: float
    """Value decoded from this schema node."""

    sky_scale: float
    """Value decoded from this schema node."""

    eye_adapt_strength: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["eye_adapt_speed"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_blur_radius"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bloom_threshold"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bloom_scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["receive_bloom_threshold"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["white"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sunlight_scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sky_scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eye_adapt_strength"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure5281(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMGS/3:Cinematic/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "saturation": _base.Binding(
            path="IMGS/3:Cinematic/payload/0:Saturation",
            kind="primitive",
            name="Saturation",
        ),
        "brightness": _base.Binding(
            path="IMGS/3:Cinematic/payload/1:Brightness",
            kind="primitive",
            name="Brightness",
        ),
        "contrast": _base.Binding(
            path="IMGS/3:Cinematic/payload/2:Contrast",
            kind="primitive",
            name="Contrast",
        ),
    }

    saturation: float
    """Value decoded from this schema node."""

    brightness: float
    """Value decoded from this schema node."""

    contrast: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["saturation"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["brightness"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["contrast"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Color5288(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMGS/4:Tint/payload/1:Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="IMGS/4:Tint/payload/1:Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="IMGS/4:Tint/payload/1:Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="IMGS/4:Tint/payload/1:Color/2:Blue",
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


class Structure5286(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMGS/4:Tint/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "amount": _base.Binding(
            path="IMGS/4:Tint/payload/0:Amount",
            kind="primitive",
            name="Amount",
        ),
        "color": _base.Binding(
            path="IMGS/4:Tint/payload/1:Color",
            kind="struct",
            name="Color",
        ),
    }

    amount: float
    """Value decoded from this schema node."""

    color: Color5288
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["amount"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["color"]) -> _base.FieldRef[Color5288]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class SkyBlurRadius5298(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    RADIUS_0 = 16384
    NO_SKY_RADIUS_0 = 16576
    RADIUS_1 = 16672
    NO_SKY_RADIUS_1 = 16736
    RADIUS_2 = 16784
    NO_SKY_RADIUS_2 = 16816
    RADIUS_3 = 16848
    NO_SKY_RADIUS_3 = 16880
    RADIUS_4 = 16904
    NO_SKY_RADIUS_4 = 16920
    RADIUS_5 = 16936
    NO_SKY_RADIUS_5 = 16952
    RADIUS_6 = 16968
    NO_SKY_RADIUS_6 = 16984
    RADIUS_7 = 17000
    NO_SKY_RADIUS_7 = 17016


class Structure5293(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMGS/5:Depth of Field/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "strength": _base.Binding(
            path="IMGS/5:Depth of Field/payload/0:Strength",
            kind="primitive",
            name="Strength",
        ),
        "distance": _base.Binding(
            path="IMGS/5:Depth of Field/payload/1:Distance",
            kind="primitive",
            name="Distance",
        ),
        "range": _base.Binding(
            path="IMGS/5:Depth of Field/payload/2:Range",
            kind="primitive",
            name="Range",
        ),
        "unknown": _base.Binding(
            path="IMGS/5:Depth of Field/payload/3:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "sky_blur_radius": _base.Binding(
            path="IMGS/5:Depth of Field/payload/4:Sky / Blur Radius",
            kind="primitive",
            name="Sky / Blur Radius",
        ),
    }

    strength: float
    """Value decoded from this schema node."""

    distance: float
    """Value decoded from this schema node."""

    range: float
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    sky_blur_radius: Optional[SkyBlurRadius5298] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["strength"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["distance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["range"]) -> _base.FieldRef[float]:
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
        self, name: Literal["sky_blur_radius"]
    ) -> _base.FieldRef[Optional[SkyBlurRadius5298]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ImageSpaceRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMGS"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "IMGS"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="IMGS/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "enam": _base.Binding(
            path="IMGS/1:ENAM",
            kind="subrecord",
            name="ENAM",
        ),
        "hdr": _base.Binding(
            path="IMGS/2:HDR",
            kind="subrecord",
            name="HDR",
        ),
        "cinematic": _base.Binding(
            path="IMGS/3:Cinematic",
            kind="subrecord",
            name="Cinematic",
        ),
        "tint": _base.Binding(
            path="IMGS/4:Tint",
            kind="subrecord",
            name="Tint",
        ),
        "depth_of_field": _base.Binding(
            path="IMGS/5:Depth of Field",
            kind="subrecord",
            name="Depth of Field",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    enam: Optional[
        Annotated[bytes, _VARIANT_5256] | Annotated[Unknown5257, _VARIANT_5257]
    ] = None
    """Value decoded from this schema node."""

    hdr: Optional[Structure5270] = None
    """Value decoded from this schema node."""

    cinematic: Optional[Structure5281] = None
    """Value decoded from this schema node."""

    tint: Optional[Structure5286] = None
    """Value decoded from this schema node."""

    depth_of_field: Optional[Structure5293] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enam"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[bytes, _VARIANT_5256]
            | Annotated[Unknown5257, _VARIANT_5257]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hdr"]
    ) -> _base.FieldRef[Optional[Structure5270]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cinematic"]
    ) -> _base.FieldRef[Optional[Structure5281]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tint"]
    ) -> _base.FieldRef[Optional[Structure5286]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["depth_of_field"]
    ) -> _base.FieldRef[Optional[Structure5293]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
