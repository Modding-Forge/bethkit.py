"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Animatable5304(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Hdr5306(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/1:Data Count/payload/2:HDR"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "eye_adapt_speed_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/0:Eye Adapt Speed Mult"),
            kind="primitive",
            name="Eye Adapt Speed Mult",
        ),
        "eye_adapt_speed_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/1:Eye Adapt Speed Add"),
            kind="primitive",
            name="Eye Adapt Speed Add",
        ),
        "bloom_blur_radius_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/2:Bloom Blur Radius Mult"),
            kind="primitive",
            name="Bloom Blur Radius Mult",
        ),
        "bloom_blur_radius_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/3:Bloom Blur Radius Add"),
            kind="primitive",
            name="Bloom Blur Radius Add",
        ),
        "bloom_threshold_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/4:Bloom Threshold Mult"),
            kind="primitive",
            name="Bloom Threshold Mult",
        ),
        "bloom_threshold_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/5:Bloom Threshold Add"),
            kind="primitive",
            name="Bloom Threshold Add",
        ),
        "bloom_scale_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/6:Bloom Scale Mult"),
            kind="primitive",
            name="Bloom Scale Mult",
        ),
        "bloom_scale_add": _base.Binding(
            path="IMAD/1:Data Count/payload/2:HDR/7:Bloom Scale Add",
            kind="primitive",
            name="Bloom Scale Add",
        ),
        "target_lum_min_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/8:Target Lum Min Mult"),
            kind="primitive",
            name="Target Lum Min Mult",
        ),
        "target_lum_min_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/9:Target Lum Min Add"),
            kind="primitive",
            name="Target Lum Min Add",
        ),
        "target_lum_max_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/10:Target Lum Max Mult"),
            kind="primitive",
            name="Target Lum Max Mult",
        ),
        "target_lum_max_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/11:Target Lum Max Add"),
            kind="primitive",
            name="Target Lum Max Add",
        ),
        "sunlight_scale_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/12:Sunlight Scale Mult"),
            kind="primitive",
            name="Sunlight Scale Mult",
        ),
        "sunlight_scale_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/2:HDR/13:Sunlight Scale Add"),
            kind="primitive",
            name="Sunlight Scale Add",
        ),
        "sky_scale_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/2:HDR/14:Sky Scale Mult",
            kind="primitive",
            name="Sky Scale Mult",
        ),
        "sky_scale_add": _base.Binding(
            path="IMAD/1:Data Count/payload/2:HDR/15:Sky Scale Add",
            kind="primitive",
            name="Sky Scale Add",
        ),
    }

    eye_adapt_speed_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    eye_adapt_speed_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    bloom_blur_radius_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    bloom_blur_radius_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    bloom_threshold_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    bloom_threshold_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    bloom_scale_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    bloom_scale_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    target_lum_min_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    target_lum_min_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    target_lum_max_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    target_lum_max_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    sunlight_scale_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    sunlight_scale_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    sky_scale_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    sky_scale_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["eye_adapt_speed_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eye_adapt_speed_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_blur_radius_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_blur_radius_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_threshold_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_threshold_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_scale_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_scale_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_lum_min_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_lum_min_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_lum_max_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_lum_max_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sunlight_scale_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sunlight_scale_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sky_scale_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sky_scale_add"]
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


class Cinematic5341(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/1:Data Count/payload/21:Cinematic"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "saturation_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/21:Cinematic/0:Saturation Mult"),
            kind="primitive",
            name="Saturation Mult",
        ),
        "saturation_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/21:Cinematic/1:Saturation Add"),
            kind="primitive",
            name="Saturation Add",
        ),
        "brightness_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/21:Cinematic/2:Brightness Mult"),
            kind="primitive",
            name="Brightness Mult",
        ),
        "brightness_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/21:Cinematic/3:Brightness Add"),
            kind="primitive",
            name="Brightness Add",
        ),
        "contrast_mult": _base.Binding(
            path=("IMAD/1:Data Count/payload/21:Cinematic/4:Contrast Mult"),
            kind="primitive",
            name="Contrast Mult",
        ),
        "contrast_add": _base.Binding(
            path=("IMAD/1:Data Count/payload/21:Cinematic/5:Contrast Add"),
            kind="primitive",
            name="Contrast Add",
        ),
    }

    saturation_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    saturation_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    brightness_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    brightness_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    contrast_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    contrast_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["saturation_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["saturation_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["brightness_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["brightness_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["contrast_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["contrast_add"]
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


class RadialBlurFlags5356(enum.IntFlag):
    """Named values from the pinned schema."""

    USE_TARGET = 1


class DoFUseTarget5362(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class DoFFlags5363(enum.IntFlag):
    """Named values from the pinned schema."""

    MODE_FRONT = 1
    MODE_BACK = 2
    NO_SKY = 4
    BLUR_RADIUS_BIT_2 = 8
    BLUR_RADIUS_BIT_1 = 16
    BLUR_RADIUS_BIT_0 = 32


class Structure5303(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/1:Data Count/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "animatable": _base.Binding(
            path="IMAD/1:Data Count/payload/0:Animatable",
            kind="primitive",
            name="Animatable",
        ),
        "duration": _base.Binding(
            path="IMAD/1:Data Count/payload/1:Duration",
            kind="primitive",
            name="Duration",
        ),
        "hdr": _base.Binding(
            path="IMAD/1:Data Count/payload/2:HDR",
            kind="struct",
            name="HDR",
        ),
        "unknown08_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/3:Unknown08 Mult",
            kind="primitive",
            name="Unknown08 Mult",
        ),
        "unknown48_add": _base.Binding(
            path="IMAD/1:Data Count/payload/4:Unknown48 Add",
            kind="primitive",
            name="Unknown48 Add",
        ),
        "unknown09_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/5:Unknown09 Mult",
            kind="primitive",
            name="Unknown09 Mult",
        ),
        "unknown49_add": _base.Binding(
            path="IMAD/1:Data Count/payload/6:Unknown49 Add",
            kind="primitive",
            name="Unknown49 Add",
        ),
        "unknown0_a_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/7:Unknown0A Mult",
            kind="primitive",
            name="Unknown0A Mult",
        ),
        "unknown4_a_add": _base.Binding(
            path="IMAD/1:Data Count/payload/8:Unknown4A Add",
            kind="primitive",
            name="Unknown4A Add",
        ),
        "unknown0_b_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/9:Unknown0B Mult",
            kind="primitive",
            name="Unknown0B Mult",
        ),
        "unknown4_b_add": _base.Binding(
            path="IMAD/1:Data Count/payload/10:Unknown4B Add",
            kind="primitive",
            name="Unknown4B Add",
        ),
        "unknown0_c_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/11:Unknown0C Mult",
            kind="primitive",
            name="Unknown0C Mult",
        ),
        "unknown4_c_add": _base.Binding(
            path="IMAD/1:Data Count/payload/12:Unknown4C Add",
            kind="primitive",
            name="Unknown4C Add",
        ),
        "unknown0_d_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/13:Unknown0D Mult",
            kind="primitive",
            name="Unknown0D Mult",
        ),
        "unknown4_d_add": _base.Binding(
            path="IMAD/1:Data Count/payload/14:Unknown4D Add",
            kind="primitive",
            name="Unknown4D Add",
        ),
        "unknown0_e_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/15:Unknown0E Mult",
            kind="primitive",
            name="Unknown0E Mult",
        ),
        "unknown4_e_add": _base.Binding(
            path="IMAD/1:Data Count/payload/16:Unknown4E Add",
            kind="primitive",
            name="Unknown4E Add",
        ),
        "unknown0_f_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/17:Unknown0F Mult",
            kind="primitive",
            name="Unknown0F Mult",
        ),
        "unknown4_f_add": _base.Binding(
            path="IMAD/1:Data Count/payload/18:Unknown4F Add",
            kind="primitive",
            name="Unknown4F Add",
        ),
        "unknown10_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/19:Unknown10 Mult",
            kind="primitive",
            name="Unknown10 Mult",
        ),
        "unknown50_add": _base.Binding(
            path="IMAD/1:Data Count/payload/20:Unknown50 Add",
            kind="primitive",
            name="Unknown50 Add",
        ),
        "cinematic": _base.Binding(
            path="IMAD/1:Data Count/payload/21:Cinematic",
            kind="struct",
            name="Cinematic",
        ),
        "unknown14_mult": _base.Binding(
            path="IMAD/1:Data Count/payload/22:Unknown14 Mult",
            kind="primitive",
            name="Unknown14 Mult",
        ),
        "unknown54_add": _base.Binding(
            path="IMAD/1:Data Count/payload/23:Unknown54 Add",
            kind="primitive",
            name="Unknown54 Add",
        ),
        "tint_color": _base.Binding(
            path="IMAD/1:Data Count/payload/24:Tint Color",
            kind="primitive",
            name="Tint Color",
        ),
        "blur_radius": _base.Binding(
            path="IMAD/1:Data Count/payload/25:Blur Radius",
            kind="primitive",
            name="Blur Radius",
        ),
        "double_vision_strength": _base.Binding(
            path=("IMAD/1:Data Count/payload/26:Double Vision Strength"),
            kind="primitive",
            name="Double Vision Strength",
        ),
        "radial_blur_strength": _base.Binding(
            path="IMAD/1:Data Count/payload/27:Radial Blur Strength",
            kind="primitive",
            name="Radial Blur Strength",
        ),
        "radial_blur_ramp_up": _base.Binding(
            path="IMAD/1:Data Count/payload/28:Radial Blur Ramp Up",
            kind="primitive",
            name="Radial Blur Ramp Up",
        ),
        "radial_blur_start": _base.Binding(
            path="IMAD/1:Data Count/payload/29:Radial Blur Start",
            kind="primitive",
            name="Radial Blur Start",
        ),
        "radial_blur_flags": _base.Binding(
            path="IMAD/1:Data Count/payload/30:Radial Blur Flags",
            kind="primitive",
            name="Radial Blur Flags",
        ),
        "radial_blur_center_x": _base.Binding(
            path="IMAD/1:Data Count/payload/31:Radial Blur Center X",
            kind="primitive",
            name="Radial Blur Center X",
        ),
        "radial_blur_center_y": _base.Binding(
            path="IMAD/1:Data Count/payload/32:Radial Blur Center Y",
            kind="primitive",
            name="Radial Blur Center Y",
        ),
        "do_f_strength": _base.Binding(
            path="IMAD/1:Data Count/payload/33:DoF Strength",
            kind="primitive",
            name="DoF Strength",
        ),
        "do_f_distance": _base.Binding(
            path="IMAD/1:Data Count/payload/34:DoF Distance",
            kind="primitive",
            name="DoF Distance",
        ),
        "do_f_range": _base.Binding(
            path="IMAD/1:Data Count/payload/35:DoF Range",
            kind="primitive",
            name="DoF Range",
        ),
        "do_f_use_target": _base.Binding(
            path="IMAD/1:Data Count/payload/36:DoF Use Target",
            kind="primitive",
            name="DoF Use Target",
        ),
        "do_f_flags": _base.Binding(
            path="IMAD/1:Data Count/payload/37:DoF Flags",
            kind="primitive",
            name="DoF Flags",
        ),
        "unused": _base.Binding(
            path="IMAD/1:Data Count/payload/38:Unused",
            kind="primitive",
            name="Unused",
        ),
        "radial_blur_ramp_down": _base.Binding(
            path=("IMAD/1:Data Count/payload/39:Radial Blur Ramp Down"),
            kind="primitive",
            name="Radial Blur Ramp Down",
        ),
        "radial_blur_down_start": _base.Binding(
            path=("IMAD/1:Data Count/payload/40:Radial Blur Down Start"),
            kind="primitive",
            name="Radial Blur Down Start",
        ),
        "fade_color": _base.Binding(
            path="IMAD/1:Data Count/payload/41:Fade Color",
            kind="primitive",
            name="Fade Color",
        ),
        "motion_blur_strength": _base.Binding(
            path="IMAD/1:Data Count/payload/42:Motion Blur Strength",
            kind="primitive",
            name="Motion Blur Strength",
        ),
    }

    animatable: Animatable5304
    """Value decoded from this schema node."""

    duration: float
    """Value decoded from this schema node."""

    hdr: Hdr5306
    """Value decoded from this schema node."""

    unknown08_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown48_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown09_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown49_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown0_a_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown4_a_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown0_b_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown4_b_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown0_c_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown4_c_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown0_d_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown4_d_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown0_e_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown4_e_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown0_f_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown4_f_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown10_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown50_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    cinematic: Cinematic5341
    """Value decoded from this schema node."""

    unknown14_mult: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unknown54_add: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    tint_color: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    blur_radius: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    double_vision_strength: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    radial_blur_strength: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    radial_blur_ramp_up: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    radial_blur_start: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    radial_blur_flags: RadialBlurFlags5356
    """Value decoded from this schema node."""

    radial_blur_center_x: float
    """Value decoded from this schema node."""

    radial_blur_center_y: float
    """Value decoded from this schema node."""

    do_f_strength: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    do_f_distance: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    do_f_range: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    do_f_use_target: DoFUseTarget5362
    """Value decoded from this schema node."""

    do_f_flags: DoFFlags5363
    """Value decoded from this schema node."""

    unused: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    radial_blur_ramp_down: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    radial_blur_down_start: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    fade_color: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    motion_blur_strength: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["animatable"]
    ) -> _base.FieldRef[Animatable5304]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["duration"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["hdr"]) -> _base.FieldRef[Hdr5306]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown08_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown48_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown09_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown49_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown0_a_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown4_a_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown0_b_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown4_b_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown0_c_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown4_c_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown0_d_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown4_d_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown0_e_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown4_e_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown0_f_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown4_f_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown10_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown50_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cinematic"]
    ) -> _base.FieldRef[Cinematic5341]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown14_mult"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown54_add"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tint_color"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["blur_radius"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["double_vision_strength"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_strength"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_ramp_up"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_start"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_flags"]
    ) -> _base.FieldRef[RadialBlurFlags5356]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_center_x"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_center_y"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["do_f_strength"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["do_f_distance"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["do_f_range"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["do_f_use_target"]
    ) -> _base.FieldRef[DoFUseTarget5362]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["do_f_flags"]
    ) -> _base.FieldRef[DoFFlags5363]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_ramp_down"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur_down_start"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fade_color"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["motion_blur_strength"]
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


class Data5371(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/2:Blur Radius/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/2:Blur Radius/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/2:Blur Radius/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5376(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/3:Double Vision Strength/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/3:Double Vision Strength/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/3:Double Vision Strength/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Value5383(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/4:Tint Color/payload/element/1:Value"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="IMAD/4:Tint Color/payload/element/1:Value/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="IMAD/4:Tint Color/payload/element/1:Value/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="IMAD/4:Tint Color/payload/element/1:Value/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "alpha": _base.Binding(
            path="IMAD/4:Tint Color/payload/element/1:Value/3:Alpha",
            kind="primitive",
            name="Alpha",
        ),
    }

    red: float
    """Value decoded from this schema node."""

    green: float
    """Value decoded from this schema node."""

    blue: float
    """Value decoded from this schema node."""

    alpha: float
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
    def field(self, name: Literal["alpha"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5381(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/4:Tint Color/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/4:Tint Color/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/4:Tint Color/payload/element/1:Value",
            kind="struct",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: Value5383
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[Value5383]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Value5392(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/5:Fade Color/payload/element/1:Value"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="IMAD/5:Fade Color/payload/element/1:Value/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="IMAD/5:Fade Color/payload/element/1:Value/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="IMAD/5:Fade Color/payload/element/1:Value/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "alpha": _base.Binding(
            path="IMAD/5:Fade Color/payload/element/1:Value/3:Alpha",
            kind="primitive",
            name="Alpha",
        ),
    }

    red: float
    """Value decoded from this schema node."""

    green: float
    """Value decoded from this schema node."""

    blue: float
    """Value decoded from this schema node."""

    alpha: float
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
    def field(self, name: Literal["alpha"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5390(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/5:Fade Color/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/5:Fade Color/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/5:Fade Color/payload/element/1:Value",
            kind="struct",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: Value5392
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[Value5392]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5400(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/6:Radial Blur/0:Strength/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/6:Radial Blur/0:Strength/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/6:Radial Blur/0:Strength/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5405(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/6:Radial Blur/1:Ramp Up/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/6:Radial Blur/1:Ramp Up/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/6:Radial Blur/1:Ramp Up/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5410(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/6:Radial Blur/2:Start/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/6:Radial Blur/2:Start/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/6:Radial Blur/2:Start/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5415(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/6:Radial Blur/3:Ramp Down/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/6:Radial Blur/3:Ramp Down/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/6:Radial Blur/3:Ramp Down/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5420(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/6:Radial Blur/4:Down Start/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/6:Radial Blur/4:Down Start/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/6:Radial Blur/4:Down Start/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class RadialBlur5397(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/6:Radial Blur"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "strength": _base.Binding(
            path="IMAD/6:Radial Blur/0:Strength",
            kind="subrecord",
            name="Strength",
        ),
        "ramp_up": _base.Binding(
            path="IMAD/6:Radial Blur/1:Ramp Up",
            kind="subrecord",
            name="Ramp Up",
        ),
        "start": _base.Binding(
            path="IMAD/6:Radial Blur/2:Start",
            kind="subrecord",
            name="Start",
        ),
        "ramp_down": _base.Binding(
            path="IMAD/6:Radial Blur/3:Ramp Down",
            kind="subrecord",
            name="Ramp Down",
        ),
        "down_start": _base.Binding(
            path="IMAD/6:Radial Blur/4:Down Start",
            kind="subrecord",
            name="Down Start",
        ),
    }

    strength: Optional[tuple[Data5400, ...]] = None
    """Value decoded from this schema node."""

    ramp_up: Optional[tuple[Data5405, ...]] = None
    """Value decoded from this schema node."""

    start: Optional[tuple[Data5410, ...]] = None
    """Value decoded from this schema node."""

    ramp_down: Optional[tuple[Data5415, ...]] = None
    """Value decoded from this schema node."""

    down_start: Optional[tuple[Data5420, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["strength"]
    ) -> _base.FieldRef[Optional[tuple[Data5400, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ramp_up"]
    ) -> _base.FieldRef[Optional[tuple[Data5405, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["start"]
    ) -> _base.FieldRef[Optional[tuple[Data5410, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ramp_down"]
    ) -> _base.FieldRef[Optional[tuple[Data5415, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["down_start"]
    ) -> _base.FieldRef[Optional[tuple[Data5420, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5426(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/7:Depht of Field/0:Strength/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/7:Depht of Field/0:Strength/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/7:Depht of Field/0:Strength/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5431(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/7:Depht of Field/1:Distance/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/7:Depht of Field/1:Distance/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/7:Depht of Field/1:Distance/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5436(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/7:Depht of Field/2:Range/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/7:Depht of Field/2:Range/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/7:Depht of Field/2:Range/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class DephtOfField5423(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/7:Depht of Field"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "strength": _base.Binding(
            path="IMAD/7:Depht of Field/0:Strength",
            kind="subrecord",
            name="Strength",
        ),
        "distance": _base.Binding(
            path="IMAD/7:Depht of Field/1:Distance",
            kind="subrecord",
            name="Distance",
        ),
        "range": _base.Binding(
            path="IMAD/7:Depht of Field/2:Range",
            kind="subrecord",
            name="Range",
        ),
    }

    strength: Optional[tuple[Data5426, ...]] = None
    """Value decoded from this schema node."""

    distance: Optional[tuple[Data5431, ...]] = None
    """Value decoded from this schema node."""

    range: Optional[tuple[Data5436, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["strength"]
    ) -> _base.FieldRef[Optional[tuple[Data5426, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["distance"]
    ) -> _base.FieldRef[Optional[tuple[Data5431, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["range"]
    ) -> _base.FieldRef[Optional[tuple[Data5436, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5441(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/8:Motion Blur Strength/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/8:Motion Blur Strength/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/8:Motion Blur Strength/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5448(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/0:Eye Adapt Speed/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/0:Eye Adapt Speed/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/9:HDR/0:Eye Adapt Speed/0:Mult/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5453(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/0:Eye Adapt Speed/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/0:Eye Adapt Speed/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/0:Eye Adapt Speed/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class EyeAdaptSpeed5445(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/0:Eye Adapt Speed"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/0:Eye Adapt Speed/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/0:Eye Adapt Speed/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5448, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5453, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5448, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5453, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5459(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/1:Bloom Blur Radius/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=(
                "IMAD/9:HDR/1:Bloom Blur Radius/0:Mult/payload/element/0:Time"
            ),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/9:HDR/1:Bloom Blur Radius/0:Mult/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5464(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/1:Bloom Blur Radius/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=(
                "IMAD/9:HDR/1:Bloom Blur Radius/1:Add/payload/element/0:Time"
            ),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/9:HDR/1:Bloom Blur Radius/1:Add/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BloomBlurRadius5456(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/1:Bloom Blur Radius"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/1:Bloom Blur Radius/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/1:Bloom Blur Radius/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5459, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5464, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5459, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5464, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5470(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/2:Bloom Threshold/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/2:Bloom Threshold/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/9:HDR/2:Bloom Threshold/0:Mult/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5475(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/2:Bloom Threshold/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/2:Bloom Threshold/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/2:Bloom Threshold/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BloomThreshold5467(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/2:Bloom Threshold"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/2:Bloom Threshold/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/2:Bloom Threshold/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5470, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5475, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5470, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5475, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5481(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/3:Bloom Scale/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/3:Bloom Scale/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/3:Bloom Scale/0:Mult/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5486(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/3:Bloom Scale/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/3:Bloom Scale/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/3:Bloom Scale/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BloomScale5478(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/3:Bloom Scale"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/3:Bloom Scale/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/3:Bloom Scale/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5481, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5486, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5481, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5486, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5492(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/4:Target Lum Min/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/4:Target Lum Min/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/4:Target Lum Min/0:Mult/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5497(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/4:Target Lum Min/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/4:Target Lum Min/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/4:Target Lum Min/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class TargetLumMin5489(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/4:Target Lum Min"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/4:Target Lum Min/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/4:Target Lum Min/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5492, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5497, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5492, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5497, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5503(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/5:Target Lum Max/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/5:Target Lum Max/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/5:Target Lum Max/0:Mult/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5508(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/5:Target Lum Max/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/5:Target Lum Max/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/5:Target Lum Max/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class TargetLumMax5500(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/5:Target Lum Max"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/5:Target Lum Max/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/5:Target Lum Max/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5503, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5508, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5503, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5508, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5514(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/6:Sunlight Scale/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/6:Sunlight Scale/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/6:Sunlight Scale/0:Mult/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5519(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/6:Sunlight Scale/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/6:Sunlight Scale/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/6:Sunlight Scale/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class SunlightScale5511(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/6:Sunlight Scale"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/6:Sunlight Scale/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/6:Sunlight Scale/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5514, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5519, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5514, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5519, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5525(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/9:HDR/7:Sky Scale/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/7:Sky Scale/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/7:Sky Scale/0:Mult/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5530(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/7:Sky Scale/1:Add/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/9:HDR/7:Sky Scale/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/9:HDR/7:Sky Scale/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class SkyScale5522(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR/7:Sky Scale"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/9:HDR/7:Sky Scale/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/9:HDR/7:Sky Scale/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5525, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5530, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5525, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5530, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Hdr5444(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/9:HDR"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "eye_adapt_speed": _base.Binding(
            path="IMAD/9:HDR/0:Eye Adapt Speed",
            kind="sequence",
            name="Eye Adapt Speed",
        ),
        "bloom_blur_radius": _base.Binding(
            path="IMAD/9:HDR/1:Bloom Blur Radius",
            kind="sequence",
            name="Bloom Blur Radius",
        ),
        "bloom_threshold": _base.Binding(
            path="IMAD/9:HDR/2:Bloom Threshold",
            kind="sequence",
            name="Bloom Threshold",
        ),
        "bloom_scale": _base.Binding(
            path="IMAD/9:HDR/3:Bloom Scale",
            kind="sequence",
            name="Bloom Scale",
        ),
        "target_lum_min": _base.Binding(
            path="IMAD/9:HDR/4:Target Lum Min",
            kind="sequence",
            name="Target Lum Min",
        ),
        "target_lum_max": _base.Binding(
            path="IMAD/9:HDR/5:Target Lum Max",
            kind="sequence",
            name="Target Lum Max",
        ),
        "sunlight_scale": _base.Binding(
            path="IMAD/9:HDR/6:Sunlight Scale",
            kind="sequence",
            name="Sunlight Scale",
        ),
        "sky_scale": _base.Binding(
            path="IMAD/9:HDR/7:Sky Scale",
            kind="sequence",
            name="Sky Scale",
        ),
    }

    eye_adapt_speed: Optional[EyeAdaptSpeed5445] = None
    """Value decoded from this schema node."""

    bloom_blur_radius: Optional[BloomBlurRadius5456] = None
    """Value decoded from this schema node."""

    bloom_threshold: Optional[BloomThreshold5467] = None
    """Value decoded from this schema node."""

    bloom_scale: Optional[BloomScale5478] = None
    """Value decoded from this schema node."""

    target_lum_min: Optional[TargetLumMin5489] = None
    """Value decoded from this schema node."""

    target_lum_max: Optional[TargetLumMax5500] = None
    """Value decoded from this schema node."""

    sunlight_scale: Optional[SunlightScale5511] = None
    """Value decoded from this schema node."""

    sky_scale: Optional[SkyScale5522] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["eye_adapt_speed"]
    ) -> _base.FieldRef[Optional[EyeAdaptSpeed5445]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_blur_radius"]
    ) -> _base.FieldRef[Optional[BloomBlurRadius5456]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_threshold"]
    ) -> _base.FieldRef[Optional[BloomThreshold5467]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bloom_scale"]
    ) -> _base.FieldRef[Optional[BloomScale5478]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_lum_min"]
    ) -> _base.FieldRef[Optional[TargetLumMin5489]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_lum_max"]
    ) -> _base.FieldRef[Optional[TargetLumMax5500]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sunlight_scale"]
    ) -> _base.FieldRef[Optional[SunlightScale5511]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sky_scale"]
    ) -> _base.FieldRef[Optional[SkyScale5522]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5535(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/10:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/10:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/10:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5540(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/11:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/11:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/11:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5545(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/12:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/12:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/12:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5550(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/13:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/13:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/13:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5555(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/14:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/14:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/14:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5560(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/15:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/15:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/15:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5565(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/16:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/16:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/16:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5570(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/17:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/17:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/17:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5575(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/18:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/18:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/18:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5580(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/19:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/19:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/19:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5585(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/20:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/20:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/20:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5590(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/21:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/21:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/21:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5595(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/22:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/22:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/22:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5600(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/23:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/23:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/23:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5605(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/24:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/24:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/24:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5610(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/25:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/25:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/25:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5615(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/26:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/26:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/26:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5620(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/27:Unused/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="IMAD/27:Unused/payload/element/0:Time",
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path="IMAD/27:Unused/payload/element/1:Value",
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5627(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/0:Saturation/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=(
                "IMAD/28:Cinematic/0:Saturation/0:Mult/payload/element/0:Time"
            ),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/28:Cinematic/0:Saturation/0:Mult/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5632(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/0:Saturation/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=(
                "IMAD/28:Cinematic/0:Saturation/1:Add/payload/element/0:Time"
            ),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/28:Cinematic/0:Saturation/1:Add/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Saturation5624(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/28:Cinematic/0:Saturation"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/28:Cinematic/0:Saturation/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/28:Cinematic/0:Saturation/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5627, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5632, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5627, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5632, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5638(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/1:Brightness/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=(
                "IMAD/28:Cinematic/1:Brightness/0:Mult/payload/element/0:Time"
            ),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/28:Cinematic/1:Brightness/0:Mult/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5643(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/1:Brightness/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=(
                "IMAD/28:Cinematic/1:Brightness/1:Add/payload/element/0:Time"
            ),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/28:Cinematic/1:Brightness/1:Add/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Brightness5635(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/28:Cinematic/1:Brightness"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/28:Cinematic/1:Brightness/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/28:Cinematic/1:Brightness/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5638, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5643, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5638, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5643, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5649(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/2:Contrast/0:Mult/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/28:Cinematic/2:Contrast/0:Mult/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/28:Cinematic/2:Contrast/0:Mult/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5654(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/2:Contrast/1:Add/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/28:Cinematic/2:Contrast/1:Add/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=("IMAD/28:Cinematic/2:Contrast/1:Add/payload/element/1:Value"),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Contrast5646(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/28:Cinematic/2:Contrast"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mult": _base.Binding(
            path="IMAD/28:Cinematic/2:Contrast/0:Mult",
            kind="subrecord",
            name="Mult",
        ),
        "add": _base.Binding(
            path="IMAD/28:Cinematic/2:Contrast/1:Add",
            kind="subrecord",
            name="Add",
        ),
    }

    mult: Optional[tuple[Data5649, ...]] = None
    """Value decoded from this schema node."""

    add: Optional[tuple[Data5654, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["mult"]
    ) -> _base.FieldRef[Optional[tuple[Data5649, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["add"]
    ) -> _base.FieldRef[Optional[tuple[Data5654, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5660(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/3:Unused/0:Unused/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/28:Cinematic/3:Unused/0:Unused/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/28:Cinematic/3:Unused/0:Unused/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Data5665(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "IMAD/28:Cinematic/3:Unused/1:Unused/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path=("IMAD/28:Cinematic/3:Unused/1:Unused/payload/element/0:Time"),
            kind="primitive",
            name="Time",
        ),
        "value": _base.Binding(
            path=(
                "IMAD/28:Cinematic/3:Unused/1:Unused/payload/element/1:Value"
            ),
            kind="primitive",
            name="Value",
        ),
    }

    time: float
    """Value decoded from this schema node."""

    value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Unused5657(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/28:Cinematic/3:Unused"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path="IMAD/28:Cinematic/3:Unused/0:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5663": _base.Binding(
            path="IMAD/28:Cinematic/3:Unused/1:Unused",
            kind="subrecord",
            name="Unused",
        ),
    }

    unused: Optional[tuple[Data5660, ...]] = None
    """Value decoded from this schema node."""

    unused_5663: Optional[tuple[Data5665, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[Optional[tuple[Data5660, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5663"]
    ) -> _base.FieldRef[Optional[tuple[Data5665, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Cinematic5623(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD/28:Cinematic"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "saturation": _base.Binding(
            path="IMAD/28:Cinematic/0:Saturation",
            kind="sequence",
            name="Saturation",
        ),
        "brightness": _base.Binding(
            path="IMAD/28:Cinematic/1:Brightness",
            kind="sequence",
            name="Brightness",
        ),
        "contrast": _base.Binding(
            path="IMAD/28:Cinematic/2:Contrast",
            kind="sequence",
            name="Contrast",
        ),
        "unused": _base.Binding(
            path="IMAD/28:Cinematic/3:Unused",
            kind="sequence",
            name="Unused",
        ),
    }

    saturation: Optional[Saturation5624] = None
    """Value decoded from this schema node."""

    brightness: Optional[Brightness5635] = None
    """Value decoded from this schema node."""

    contrast: Optional[Contrast5646] = None
    """Value decoded from this schema node."""

    unused: Optional[Unused5657] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["saturation"]
    ) -> _base.FieldRef[Optional[Saturation5624]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["brightness"]
    ) -> _base.FieldRef[Optional[Brightness5635]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["contrast"]
    ) -> _base.FieldRef[Optional[Contrast5646]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[Optional[Unused5657]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ImageSpaceAdapterRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "IMAD"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "IMAD"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="IMAD/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "data_count": _base.Binding(
            path="IMAD/1:Data Count",
            kind="subrecord",
            name="Data Count",
        ),
        "blur_radius": _base.Binding(
            path="IMAD/2:Blur Radius",
            kind="subrecord",
            name="Blur Radius",
        ),
        "double_vision_strength": _base.Binding(
            path="IMAD/3:Double Vision Strength",
            kind="subrecord",
            name="Double Vision Strength",
        ),
        "tint_color": _base.Binding(
            path="IMAD/4:Tint Color",
            kind="subrecord",
            name="Tint Color",
        ),
        "fade_color": _base.Binding(
            path="IMAD/5:Fade Color",
            kind="subrecord",
            name="Fade Color",
        ),
        "radial_blur": _base.Binding(
            path="IMAD/6:Radial Blur",
            kind="sequence",
            name="Radial Blur",
        ),
        "depht_of_field": _base.Binding(
            path="IMAD/7:Depht of Field",
            kind="sequence",
            name="Depht of Field",
        ),
        "motion_blur_strength": _base.Binding(
            path="IMAD/8:Motion Blur Strength",
            kind="subrecord",
            name="Motion Blur Strength",
        ),
        "hdr": _base.Binding(
            path="IMAD/9:HDR",
            kind="sequence",
            name="HDR",
        ),
        "unused": _base.Binding(
            path="IMAD/10:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5538": _base.Binding(
            path="IMAD/11:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5543": _base.Binding(
            path="IMAD/12:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5548": _base.Binding(
            path="IMAD/13:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5553": _base.Binding(
            path="IMAD/14:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5558": _base.Binding(
            path="IMAD/15:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5563": _base.Binding(
            path="IMAD/16:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5568": _base.Binding(
            path="IMAD/17:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5573": _base.Binding(
            path="IMAD/18:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5578": _base.Binding(
            path="IMAD/19:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5583": _base.Binding(
            path="IMAD/20:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5588": _base.Binding(
            path="IMAD/21:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5593": _base.Binding(
            path="IMAD/22:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5598": _base.Binding(
            path="IMAD/23:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5603": _base.Binding(
            path="IMAD/24:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5608": _base.Binding(
            path="IMAD/25:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5613": _base.Binding(
            path="IMAD/26:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_5618": _base.Binding(
            path="IMAD/27:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "cinematic": _base.Binding(
            path="IMAD/28:Cinematic",
            kind="sequence",
            name="Cinematic",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    data_count: Optional[Structure5303] = None
    """Value decoded from this schema node."""

    blur_radius: Optional[tuple[Data5371, ...]] = None
    """Value decoded from this schema node."""

    double_vision_strength: Optional[tuple[Data5376, ...]] = None
    """Value decoded from this schema node."""

    tint_color: Optional[tuple[Data5381, ...]] = None
    """Value decoded from this schema node."""

    fade_color: Optional[tuple[Data5390, ...]] = None
    """Value decoded from this schema node."""

    radial_blur: Optional[RadialBlur5397] = None
    """Value decoded from this schema node."""

    depht_of_field: Optional[DephtOfField5423] = None
    """Value decoded from this schema node."""

    motion_blur_strength: Optional[tuple[Data5441, ...]] = None
    """Value decoded from this schema node."""

    hdr: Optional[Hdr5444] = None
    """Value decoded from this schema node."""

    unused: Optional[tuple[Data5535, ...]] = None
    """Value decoded from this schema node."""

    unused_5538: Optional[tuple[Data5540, ...]] = None
    """Value decoded from this schema node."""

    unused_5543: Optional[tuple[Data5545, ...]] = None
    """Value decoded from this schema node."""

    unused_5548: Optional[tuple[Data5550, ...]] = None
    """Value decoded from this schema node."""

    unused_5553: Optional[tuple[Data5555, ...]] = None
    """Value decoded from this schema node."""

    unused_5558: Optional[tuple[Data5560, ...]] = None
    """Value decoded from this schema node."""

    unused_5563: Optional[tuple[Data5565, ...]] = None
    """Value decoded from this schema node."""

    unused_5568: Optional[tuple[Data5570, ...]] = None
    """Value decoded from this schema node."""

    unused_5573: Optional[tuple[Data5575, ...]] = None
    """Value decoded from this schema node."""

    unused_5578: Optional[tuple[Data5580, ...]] = None
    """Value decoded from this schema node."""

    unused_5583: Optional[tuple[Data5585, ...]] = None
    """Value decoded from this schema node."""

    unused_5588: Optional[tuple[Data5590, ...]] = None
    """Value decoded from this schema node."""

    unused_5593: Optional[tuple[Data5595, ...]] = None
    """Value decoded from this schema node."""

    unused_5598: Optional[tuple[Data5600, ...]] = None
    """Value decoded from this schema node."""

    unused_5603: Optional[tuple[Data5605, ...]] = None
    """Value decoded from this schema node."""

    unused_5608: Optional[tuple[Data5610, ...]] = None
    """Value decoded from this schema node."""

    unused_5613: Optional[tuple[Data5615, ...]] = None
    """Value decoded from this schema node."""

    unused_5618: Optional[tuple[Data5620, ...]] = None
    """Value decoded from this schema node."""

    cinematic: Optional[Cinematic5623] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data_count"]
    ) -> _base.FieldRef[Optional[Structure5303]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["blur_radius"]
    ) -> _base.FieldRef[Optional[tuple[Data5371, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["double_vision_strength"]
    ) -> _base.FieldRef[Optional[tuple[Data5376, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tint_color"]
    ) -> _base.FieldRef[Optional[tuple[Data5381, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fade_color"]
    ) -> _base.FieldRef[Optional[tuple[Data5390, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radial_blur"]
    ) -> _base.FieldRef[Optional[RadialBlur5397]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["depht_of_field"]
    ) -> _base.FieldRef[Optional[DephtOfField5423]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["motion_blur_strength"]
    ) -> _base.FieldRef[Optional[tuple[Data5441, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["hdr"]) -> _base.FieldRef[Optional[Hdr5444]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[Optional[tuple[Data5535, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5538"]
    ) -> _base.FieldRef[Optional[tuple[Data5540, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5543"]
    ) -> _base.FieldRef[Optional[tuple[Data5545, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5548"]
    ) -> _base.FieldRef[Optional[tuple[Data5550, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5553"]
    ) -> _base.FieldRef[Optional[tuple[Data5555, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5558"]
    ) -> _base.FieldRef[Optional[tuple[Data5560, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5563"]
    ) -> _base.FieldRef[Optional[tuple[Data5565, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5568"]
    ) -> _base.FieldRef[Optional[tuple[Data5570, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5573"]
    ) -> _base.FieldRef[Optional[tuple[Data5575, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5578"]
    ) -> _base.FieldRef[Optional[tuple[Data5580, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5583"]
    ) -> _base.FieldRef[Optional[tuple[Data5585, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5588"]
    ) -> _base.FieldRef[Optional[tuple[Data5590, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5593"]
    ) -> _base.FieldRef[Optional[tuple[Data5595, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5598"]
    ) -> _base.FieldRef[Optional[tuple[Data5600, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5603"]
    ) -> _base.FieldRef[Optional[tuple[Data5605, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5608"]
    ) -> _base.FieldRef[Optional[tuple[Data5610, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5613"]
    ) -> _base.FieldRef[Optional[tuple[Data5615, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_5618"]
    ) -> _base.FieldRef[Optional[tuple[Data5620, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cinematic"]
    ) -> _base.FieldRef[Optional[Cinematic5623]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
