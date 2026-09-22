"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class CausesDamageUnknown1Unknown2EnableFlowBb6343B116988(enum.IntFlag):
    """Named values from the pinned schema."""

    CAUSES_DAMAGE = 1
    UNKNOWN_1 = 2
    UNKNOWN_2 = 4
    ENABLE_FLOWMAP = 8
    BLEND_NORMALS = 16
    UNKNOWN_5 = 32
    UNKNOWN_6 = 64
    UNKNOWN_7 = 128


class ShallowColor17013(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WATR/11:Visual Data/payload/10:Shallow Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WATR/11:Visual Data/payload/10:Shallow Color/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WATR/11:Visual Data/payload/10:Shallow Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WATR/11:Visual Data/payload/10:Shallow Color/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WATR/11:Visual Data/payload/10:Shallow Color/3:Unused"),
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


class DeepColor17018(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WATR/11:Visual Data/payload/11:Deep Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="WATR/11:Visual Data/payload/11:Deep Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="WATR/11:Visual Data/payload/11:Deep Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="WATR/11:Visual Data/payload/11:Deep Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WATR/11:Visual Data/payload/11:Deep Color/3:Unused"),
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


class ReflectionColor17023(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WATR/11:Visual Data/payload/12:Reflection Color"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=("WATR/11:Visual Data/payload/12:Reflection Color/0:Red"),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=("WATR/11:Visual Data/payload/12:Reflection Color/1:Green"),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=("WATR/11:Visual Data/payload/12:Reflection Color/2:Blue"),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=("WATR/11:Visual Data/payload/12:Reflection Color/3:Unused"),
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


class Structure17002(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WATR/11:Visual Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="WATR/11:Visual Data/payload/0:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17004": _base.Binding(
            path="WATR/11:Visual Data/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17005": _base.Binding(
            path="WATR/11:Visual Data/payload/2:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17006": _base.Binding(
            path="WATR/11:Visual Data/payload/3:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "specular_properties_sun_specular_power": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/4:Specular Properties - Su"
                "n Specular Power"
            ),
            kind="primitive",
            name="Specular Properties - Sun Specular Power",
        ),
        "water_properties_reflectivity_amount": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/5:Water Properties - Refle"
                "ctivity Amount"
            ),
            kind="primitive",
            name="Water Properties - Reflectivity Amount",
        ),
        "water_properties_fresnel_amount": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/6:Water Properties - Fresn"
                "el Amount"
            ),
            kind="primitive",
            name="Water Properties - Fresnel Amount",
        ),
        "unknown_17010": _base.Binding(
            path="WATR/11:Visual Data/payload/7:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "fog_properties_above_water_fog_distance_near_plane": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/8:Fog Properties - Above W"
                "ater - Fog Distance - Near Plane"
            ),
            kind="primitive",
            name=("Fog Properties - Above Water - Fog Distance - Near Plane"),
        ),
        "fog_properties_above_water_fog_distance_far_plane": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/9:Fog Properties - Above W"
                "ater - Fog Distance - Far Plane"
            ),
            kind="primitive",
            name=("Fog Properties - Above Water - Fog Distance - Far Plane"),
        ),
        "shallow_color": _base.Binding(
            path="WATR/11:Visual Data/payload/10:Shallow Color",
            kind="struct",
            name="Shallow Color",
        ),
        "deep_color": _base.Binding(
            path="WATR/11:Visual Data/payload/11:Deep Color",
            kind="struct",
            name="Deep Color",
        ),
        "reflection_color": _base.Binding(
            path="WATR/11:Visual Data/payload/12:Reflection Color",
            kind="struct",
            name="Reflection Color",
        ),
        "unknown_17028": _base.Binding(
            path="WATR/11:Visual Data/payload/13:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17029": _base.Binding(
            path="WATR/11:Visual Data/payload/14:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17030": _base.Binding(
            path="WATR/11:Visual Data/payload/15:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17031": _base.Binding(
            path="WATR/11:Visual Data/payload/16:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17032": _base.Binding(
            path="WATR/11:Visual Data/payload/17:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "displacement_simulator_starting_size": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/18:Displacement Simulator "
                "- Starting Size"
            ),
            kind="primitive",
            name="Displacement Simulator - Starting Size",
        ),
        "displacement_simulator_force": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/19:Displacement Simulator - Force"
            ),
            kind="primitive",
            name="Displacement Simulator - Force",
        ),
        "displacement_simulator_velocity": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/20:Displacement Simulator "
                "- Velocity"
            ),
            kind="primitive",
            name="Displacement Simulator - Velocity",
        ),
        "displacement_simulator_falloff": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/21:Displacement Simulator "
                "- Falloff"
            ),
            kind="primitive",
            name="Displacement Simulator - Falloff",
        ),
        "displacement_simulator_dampner": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/22:Displacement Simulator "
                "- Dampner"
            ),
            kind="primitive",
            name="Displacement Simulator - Dampner",
        ),
        "unknown_17038": _base.Binding(
            path="WATR/11:Visual Data/payload/23:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "noise_properties_noise_falloff": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/24:Noise Properties - Nois"
                "e Falloff"
            ),
            kind="primitive",
            name="Noise Properties - Noise Falloff",
        ),
        "noise_properties_layer_one_wind_direction": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/25:Noise Properties - Laye"
                "r One - Wind Direction"
            ),
            kind="primitive",
            name="Noise Properties - Layer One - Wind Direction",
        ),
        "noise_properties_layer_two_wind_direction": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/26:Noise Properties - Laye"
                "r Two - Wind Direction"
            ),
            kind="primitive",
            name="Noise Properties - Layer Two - Wind Direction",
        ),
        "noise_properties_layer_three_wind_direction": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/27:Noise Properties - Laye"
                "r Three - Wind Direction"
            ),
            kind="primitive",
            name="Noise Properties - Layer Three - Wind Direction",
        ),
        "noise_properties_layer_one_wind_speed": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/28:Noise Properties - Laye"
                "r One - Wind Speed"
            ),
            kind="primitive",
            name="Noise Properties - Layer One - Wind Speed",
        ),
        "noise_properties_layer_two_wind_speed": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/29:Noise Properties - Laye"
                "r Two - Wind Speed"
            ),
            kind="primitive",
            name="Noise Properties - Layer Two - Wind Speed",
        ),
        "noise_properties_layer_three_wind_speed": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/30:Noise Properties - Laye"
                "r Three - Wind Speed"
            ),
            kind="primitive",
            name="Noise Properties - Layer Three - Wind Speed",
        ),
        "unknown_17046": _base.Binding(
            path="WATR/11:Visual Data/payload/31:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_17047": _base.Binding(
            path="WATR/11:Visual Data/payload/32:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "fog_properties_above_water_fog_amount": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/33:Fog Properties - Above "
                "Water - Fog Amount"
            ),
            kind="primitive",
            name="Fog Properties - Above Water - Fog Amount",
        ),
        "unknown_17049": _base.Binding(
            path="WATR/11:Visual Data/payload/34:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "fog_properties_under_water_fog_amount": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/35:Fog Properties - Under "
                "Water - Fog Amount"
            ),
            kind="primitive",
            name="Fog Properties - Under Water - Fog Amount",
        ),
        "fog_properties_under_water_fog_distance_near_plane": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/36:Fog Properties - Under "
                "Water - Fog Distance - Near Plane"
            ),
            kind="primitive",
            name=("Fog Properties - Under Water - Fog Distance - Near Plane"),
        ),
        "fog_properties_under_water_fog_distance_far_plane": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/37:Fog Properties - Under "
                "Water - Fog Distance - Far Plane"
            ),
            kind="primitive",
            name=("Fog Properties - Under Water - Fog Distance - Far Plane"),
        ),
        "water_properties_refraction_magnitude": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/38:Water Properties - Refr"
                "action Magnitude"
            ),
            kind="primitive",
            name="Water Properties - Refraction Magnitude",
        ),
        "specular_properties_specular_power": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/39:Specular Properties - S"
                "pecular Power"
            ),
            kind="primitive",
            name="Specular Properties - Specular Power",
        ),
        "unknown_17055": _base.Binding(
            path="WATR/11:Visual Data/payload/40:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "specular_properties_specular_radius": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/41:Specular Properties - S"
                "pecular Radius"
            ),
            kind="primitive",
            name="Specular Properties - Specular Radius",
        ),
        "specular_properties_specular_brightness": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/42:Specular Properties - S"
                "pecular Brightness"
            ),
            kind="primitive",
            name="Specular Properties - Specular Brightness",
        ),
        "noise_properties_layer_one_uv_scale": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/43:Noise Properties - Laye"
                "r One - UV Scale"
            ),
            kind="primitive",
            name="Noise Properties - Layer One - UV Scale",
        ),
        "noise_properties_layer_two_uv_scale": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/44:Noise Properties - Laye"
                "r Two - UV Scale"
            ),
            kind="primitive",
            name="Noise Properties - Layer Two - UV Scale",
        ),
        "noise_properties_layer_three_uv_scale": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/45:Noise Properties - Laye"
                "r Three - UV Scale"
            ),
            kind="primitive",
            name="Noise Properties - Layer Three - UV Scale",
        ),
        "noise_properties_layer_one_amplitude_scale": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/46:Noise Properties - Laye"
                "r One - Amplitude Scale"
            ),
            kind="primitive",
            name="Noise Properties - Layer One - Amplitude Scale",
        ),
        "noise_properties_layer_two_amplitude_scale": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/47:Noise Properties - Laye"
                "r Two - Amplitude Scale"
            ),
            kind="primitive",
            name="Noise Properties - Layer Two - Amplitude Scale",
        ),
        "noise_properties_layer_three_amplitude_scale": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/48:Noise Properties - Laye"
                "r Three - Amplitude Scale"
            ),
            kind="primitive",
            name="Noise Properties - Layer Three - Amplitude Scale",
        ),
        "water_properties_reflection_magnitude": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/49:Water Properties - Refl"
                "ection Magnitude"
            ),
            kind="primitive",
            name="Water Properties - Reflection Magnitude",
        ),
        "specular_properties_sun_sparkle_magnitude": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/50:Specular Properties - S"
                "un Sparkle Magnitude"
            ),
            kind="primitive",
            name="Specular Properties - Sun Sparkle Magnitude",
        ),
        "specular_properties_sun_specular_magnitude": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/51:Specular Properties - S"
                "un Specular Magnitude"
            ),
            kind="primitive",
            name="Specular Properties - Sun Specular Magnitude",
        ),
        "depth_properties_reflections": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/52:Depth Properties - Reflections"
            ),
            kind="primitive",
            name="Depth Properties - Reflections",
        ),
        "depth_properties_refraction": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/53:Depth Properties - Refraction"
            ),
            kind="primitive",
            name="Depth Properties - Refraction",
        ),
        "depth_properties_normals": _base.Binding(
            path=("WATR/11:Visual Data/payload/54:Depth Properties - Normals"),
            kind="primitive",
            name="Depth Properties - Normals",
        ),
        "depth_properties_specular_lighting": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/55:Depth Properties - Spec"
                "ular Lighting"
            ),
            kind="primitive",
            name="Depth Properties - Specular Lighting",
        ),
        "specular_properties_sun_sparkle_power": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/56:Specular Properties - S"
                "un Sparkle Power"
            ),
            kind="primitive",
            name="Specular Properties - Sun Sparkle Power",
        ),
        "noise_properties_flowmap_scale": _base.Binding(
            path=(
                "WATR/11:Visual Data/payload/57:Noise Properties - Flow"
                "map Scale"
            ),
            kind="primitive",
            name="Noise Properties - Flowmap Scale",
        ),
    }

    unknown: float
    """Value decoded from this schema node."""

    unknown_17004: float
    """Value decoded from this schema node."""

    unknown_17005: float
    """Value decoded from this schema node."""

    unknown_17006: float
    """Value decoded from this schema node."""

    specular_properties_sun_specular_power: float
    """Value decoded from this schema node."""

    water_properties_reflectivity_amount: float
    """Value decoded from this schema node."""

    water_properties_fresnel_amount: float
    """Value decoded from this schema node."""

    unknown_17010: bytes
    """Value decoded from this schema node."""

    fog_properties_above_water_fog_distance_near_plane: float
    """Value decoded from this schema node."""

    fog_properties_above_water_fog_distance_far_plane: float
    """Value decoded from this schema node."""

    shallow_color: ShallowColor17013
    """Value decoded from this schema node."""

    deep_color: DeepColor17018
    """Value decoded from this schema node."""

    reflection_color: ReflectionColor17023
    """Value decoded from this schema node."""

    unknown_17028: bytes
    """Value decoded from this schema node."""

    unknown_17029: float
    """Value decoded from this schema node."""

    unknown_17030: float
    """Value decoded from this schema node."""

    unknown_17031: float
    """Value decoded from this schema node."""

    unknown_17032: float
    """Value decoded from this schema node."""

    displacement_simulator_starting_size: float
    """Value decoded from this schema node."""

    displacement_simulator_force: float
    """Value decoded from this schema node."""

    displacement_simulator_velocity: float
    """Value decoded from this schema node."""

    displacement_simulator_falloff: float
    """Value decoded from this schema node."""

    displacement_simulator_dampner: float
    """Value decoded from this schema node."""

    unknown_17038: float
    """Value decoded from this schema node."""

    noise_properties_noise_falloff: float
    """Value decoded from this schema node."""

    noise_properties_layer_one_wind_direction: float
    """Value decoded from this schema node."""

    noise_properties_layer_two_wind_direction: float
    """Value decoded from this schema node."""

    noise_properties_layer_three_wind_direction: float
    """Value decoded from this schema node."""

    noise_properties_layer_one_wind_speed: float
    """Value decoded from this schema node."""

    noise_properties_layer_two_wind_speed: float
    """Value decoded from this schema node."""

    noise_properties_layer_three_wind_speed: float
    """Value decoded from this schema node."""

    unknown_17046: float
    """Value decoded from this schema node."""

    unknown_17047: float
    """Value decoded from this schema node."""

    fog_properties_above_water_fog_amount: float
    """Value decoded from this schema node."""

    unknown_17049: float
    """Value decoded from this schema node."""

    fog_properties_under_water_fog_amount: float
    """Value decoded from this schema node."""

    fog_properties_under_water_fog_distance_near_plane: float
    """Value decoded from this schema node."""

    fog_properties_under_water_fog_distance_far_plane: float
    """Value decoded from this schema node."""

    water_properties_refraction_magnitude: float
    """Value decoded from this schema node."""

    specular_properties_specular_power: float
    """Value decoded from this schema node."""

    unknown_17055: float
    """Value decoded from this schema node."""

    specular_properties_specular_radius: float
    """Value decoded from this schema node."""

    specular_properties_specular_brightness: float
    """Value decoded from this schema node."""

    noise_properties_layer_one_uv_scale: float
    """Value decoded from this schema node."""

    noise_properties_layer_two_uv_scale: float
    """Value decoded from this schema node."""

    noise_properties_layer_three_uv_scale: float
    """Value decoded from this schema node."""

    noise_properties_layer_one_amplitude_scale: float
    """Value decoded from this schema node."""

    noise_properties_layer_two_amplitude_scale: float
    """Value decoded from this schema node."""

    noise_properties_layer_three_amplitude_scale: float
    """Value decoded from this schema node."""

    water_properties_reflection_magnitude: float
    """Value decoded from this schema node."""

    specular_properties_sun_sparkle_magnitude: float
    """Value decoded from this schema node."""

    specular_properties_sun_specular_magnitude: float
    """Value decoded from this schema node."""

    depth_properties_reflections: float
    """Value decoded from this schema node."""

    depth_properties_refraction: float
    """Value decoded from this schema node."""

    depth_properties_normals: float
    """Value decoded from this schema node."""

    depth_properties_specular_lighting: float
    """Value decoded from this schema node."""

    specular_properties_sun_sparkle_power: float
    """Value decoded from this schema node."""

    noise_properties_flowmap_scale: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17004"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17005"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17006"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular_properties_sun_specular_power"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_properties_reflectivity_amount"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_properties_fresnel_amount"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17010"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self,
        name: Literal["fog_properties_above_water_fog_distance_near_plane"],
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_properties_above_water_fog_distance_far_plane"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["shallow_color"]
    ) -> _base.FieldRef[ShallowColor17013]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["deep_color"]
    ) -> _base.FieldRef[DeepColor17018]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reflection_color"]
    ) -> _base.FieldRef[ReflectionColor17023]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17028"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17029"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17030"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17031"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17032"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["displacement_simulator_starting_size"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["displacement_simulator_force"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["displacement_simulator_velocity"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["displacement_simulator_falloff"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["displacement_simulator_dampner"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17038"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_noise_falloff"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_one_wind_direction"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_two_wind_direction"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_three_wind_direction"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_one_wind_speed"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_two_wind_speed"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_three_wind_speed"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17046"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17047"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_properties_above_water_fog_amount"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17049"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_properties_under_water_fog_amount"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self,
        name: Literal["fog_properties_under_water_fog_distance_near_plane"],
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fog_properties_under_water_fog_distance_far_plane"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_properties_refraction_magnitude"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular_properties_specular_power"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17055"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular_properties_specular_radius"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular_properties_specular_brightness"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_one_uv_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_two_uv_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_three_uv_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_one_amplitude_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_two_amplitude_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_layer_three_amplitude_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_properties_reflection_magnitude"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular_properties_sun_sparkle_magnitude"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular_properties_sun_specular_magnitude"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["depth_properties_reflections"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["depth_properties_refraction"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["depth_properties_normals"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["depth_properties_specular_lighting"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["specular_properties_sun_sparkle_power"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_properties_flowmap_scale"]
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


class Structure17076(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WATR/13:Linear Velocity/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WATR/13:Linear Velocity/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WATR/13:Linear Velocity/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="WATR/13:Linear Velocity/payload/2:Z",
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


class Structure17081(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WATR/14:Angular Velocity/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WATR/14:Angular Velocity/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WATR/14:Angular Velocity/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="WATR/14:Angular Velocity/payload/2:Z",
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


class WaterRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WATR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "WATR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="WATR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="WATR/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "unused": _base.Binding(
            path="WATR/2:Unused",
            kind="repeat",
            name="Unused",
            repeated_path="WATR/2:Unused/repeat/0:Noise Map",
            child_kind="subrecord",
        ),
        "opacity": _base.Binding(
            path="WATR/3:Opacity",
            kind="subrecord",
            name="Opacity",
        ),
        "flags": _base.Binding(
            path="WATR/4:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "unused_16989": _base.Binding(
            path="WATR/5:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "material": _base.Binding(
            path="WATR/6:Material",
            kind="subrecord",
            name="Material",
        ),
        "open_sound": _base.Binding(
            path="WATR/7:Open Sound",
            kind="subrecord",
            name="Open Sound",
        ),
        "spell": _base.Binding(
            path="WATR/8:Spell",
            kind="subrecord",
            name="Spell",
        ),
        "image_space": _base.Binding(
            path="WATR/9:Image Space",
            kind="subrecord",
            name="Image Space",
        ),
        "unused_16999": _base.Binding(
            path="WATR/10:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "visual_data": _base.Binding(
            path="WATR/11:Visual Data",
            kind="subrecord",
            name="Visual Data",
        ),
        "unused_17073": _base.Binding(
            path="WATR/12:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "linear_velocity": _base.Binding(
            path="WATR/13:Linear Velocity",
            kind="subrecord",
            name="Linear Velocity",
        ),
        "angular_velocity": _base.Binding(
            path="WATR/14:Angular Velocity",
            kind="subrecord",
            name="Angular Velocity",
        ),
        "noise_layer_one_noise_texture": _base.Binding(
            path="WATR/15:Noise Layer One - Noise Texture",
            kind="subrecord",
            name="Noise Layer One - Noise Texture",
        ),
        "noise_layer_two_noise_texture": _base.Binding(
            path="WATR/16:Noise Layer Two - Noise Texture",
            kind="subrecord",
            name="Noise Layer Two - Noise Texture",
        ),
        "noise_layer_three_noise_texture": _base.Binding(
            path="WATR/17:Noise Layer Three - Noise Texture",
            kind="subrecord",
            name="Noise Layer Three - Noise Texture",
        ),
        "flow_normals_noise_texture": _base.Binding(
            path="WATR/18:Flow Normals - Noise Texture",
            kind="subrecord",
            name="Flow Normals - Noise Texture",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    unused: tuple[str, ...] = ()
    """Value decoded from this schema node."""

    opacity: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ] = None
    """Value decoded from this schema node."""

    flags: Optional[CausesDamageUnknown1Unknown2EnableFlowBb6343B116988] = None
    """Value decoded from this schema node."""

    unused_16989: Optional[bytes] = None
    """Value decoded from this schema node."""

    material: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    open_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    spell: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    image_space: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused_16999: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    visual_data: Optional[Structure17002] = None
    """Value decoded from this schema node."""

    unused_17073: Optional[bytes] = None
    """Value decoded from this schema node."""

    linear_velocity: Optional[Structure17076] = None
    """Value decoded from this schema node."""

    angular_velocity: Optional[Structure17081] = None
    """Value decoded from this schema node."""

    noise_layer_one_noise_texture: Optional[str] = None
    """Value decoded from this schema node."""

    noise_layer_two_noise_texture: Optional[str] = None
    """Value decoded from this schema node."""

    noise_layer_three_noise_texture: Optional[str] = None
    """Value decoded from this schema node."""

    flow_normals_noise_texture: Optional[str] = None
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
    def field(self, name: Literal["unused"]) -> _base.FieldRef[tuple[str, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["opacity"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[CausesDamageUnknown1Unknown2EnableFlowBb6343B116988]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_16989"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["material"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["open_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["spell"]
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
    def field(
        self, name: Literal["unused_16999"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["visual_data"]
    ) -> _base.FieldRef[Optional[Structure17002]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_17073"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["linear_velocity"]
    ) -> _base.FieldRef[Optional[Structure17076]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["angular_velocity"]
    ) -> _base.FieldRef[Optional[Structure17081]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_layer_one_noise_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_layer_two_noise_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["noise_layer_three_noise_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flow_normals_noise_texture"]
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
