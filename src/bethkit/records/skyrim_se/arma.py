"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class FirstPersonFlags1348(enum.IntFlag):
    """Named values from the pinned schema."""

    VALUE_30_HEAD = 1
    VALUE_31_HAIR = 2
    VALUE_32_BODY = 4
    VALUE_33_HANDS = 8
    VALUE_34_FOREARMS = 16
    VALUE_35_AMULET = 32
    VALUE_36_RING = 64
    VALUE_37_FEET = 128
    VALUE_38_CALVES = 256
    VALUE_39_SHIELD = 512
    VALUE_40_TAIL = 1024
    VALUE_41_LONG_HAIR = 2048
    VALUE_42_CIRCLET = 4096
    VALUE_43_EARS = 8192
    VALUE_44_UNNAMED = 16384
    VALUE_45_UNNAMED = 32768
    VALUE_46_UNNAMED = 65536
    VALUE_47_UNNAMED = 131072
    VALUE_48_UNNAMED = 262144
    VALUE_49_UNNAMED = 524288
    VALUE_50_DECAPITATE_HEAD = 1048576
    VALUE_51_DECAPITATE = 2097152
    VALUE_52_UNNAMED = 4194304
    VALUE_53_UNNAMED = 8388608
    VALUE_54_UNNAMED = 16777216
    VALUE_55_UNNAMED = 33554432
    VALUE_56_UNNAMED = 67108864
    VALUE_57_UNNAMED = 134217728
    VALUE_58_UNNAMED = 268435456
    VALUE_59_UNNAMED = 536870912
    VALUE_60_UNNAMED = 1073741824
    VALUE_61_FX01 = 2147483648


class ArmorType1351(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LIGHT_ARMOR = 0
    HEAVY_ARMOR = 1
    CLOTHING = 2


class Structure1347(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/1:Biped Body Template/0:Biped Body Template/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "first_person_flags": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/0:Biped Body Template/paylo"
                "ad/0:First Person Flags"
            ),
            kind="primitive",
            name="First Person Flags",
        ),
        "general_flags": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/0:Biped Body Template/paylo"
                "ad/1:General Flags"
            ),
            kind="custom",
            name="General Flags",
        ),
        "unused": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/0:Biped Body Template/paylo"
                "ad/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "armor_type": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/0:Biped Body Template/paylo"
                "ad/3:Armor Type"
            ),
            kind="primitive",
            name="Armor Type",
        ),
    }

    first_person_flags: FirstPersonFlags1348
    """Value decoded from this schema node."""

    general_flags: Literal[0]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    armor_type: ArmorType1351
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["first_person_flags"]
    ) -> _base.FieldRef[FirstPersonFlags1348]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["general_flags"]
    ) -> _base.FieldRef[Literal[0]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["armor_type"]
    ) -> _base.FieldRef[ArmorType1351]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1346: _base.Variant = _base.Variant(
    path="ARMA/1:Biped Body Template/0:Biped Body Template"
)


class FirstPersonFlags1354(enum.IntFlag):
    """Named values from the pinned schema."""

    VALUE_30_HEAD = 1
    VALUE_31_HAIR = 2
    VALUE_32_BODY = 4
    VALUE_33_HANDS = 8
    VALUE_34_FOREARMS = 16
    VALUE_35_AMULET = 32
    VALUE_36_RING = 64
    VALUE_37_FEET = 128
    VALUE_38_CALVES = 256
    VALUE_39_SHIELD = 512
    VALUE_40_TAIL = 1024
    VALUE_41_LONG_HAIR = 2048
    VALUE_42_CIRCLET = 4096
    VALUE_43_EARS = 8192
    VALUE_44_UNNAMED = 16384
    VALUE_45_UNNAMED = 32768
    VALUE_46_UNNAMED = 65536
    VALUE_47_UNNAMED = 131072
    VALUE_48_UNNAMED = 262144
    VALUE_49_UNNAMED = 524288
    VALUE_50_DECAPITATE_HEAD = 1048576
    VALUE_51_DECAPITATE = 2097152
    VALUE_52_UNNAMED = 4194304
    VALUE_53_UNNAMED = 8388608
    VALUE_54_UNNAMED = 16777216
    VALUE_55_UNNAMED = 33554432
    VALUE_56_UNNAMED = 67108864
    VALUE_57_UNNAMED = 134217728
    VALUE_58_UNNAMED = 268435456
    VALUE_59_UNNAMED = 536870912
    VALUE_60_UNNAMED = 1073741824
    VALUE_61_FX01 = 2147483648


class GeneralFlags1355(enum.IntFlag):
    """Named values from the pinned schema."""

    ARMA_MODULATES_VOICE = 1
    UNKNOWN_2 = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    ARMO_NON_PLAYABLE = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    UNKNOWN_8 = 128


class ArmorType1357(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LIGHT_ARMOR = 0
    HEAVY_ARMOR = 1
    CLOTHING = 2


class Structure1353(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/1:Biped Body Template/1:Body Template/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "first_person_flags": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/1:Body Template/payload/0:F"
                "irst Person Flags"
            ),
            kind="primitive",
            name="First Person Flags",
        ),
        "general_flags": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/1:Body Template/payload/1:G"
                "eneral Flags"
            ),
            kind="primitive",
            name="General Flags",
        ),
        "unused": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/1:Body Template/payload/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "armor_type": _base.Binding(
            path=(
                "ARMA/1:Biped Body Template/1:Body Template/payload/3:A"
                "rmor Type"
            ),
            kind="primitive",
            name="Armor Type",
        ),
    }

    first_person_flags: FirstPersonFlags1354
    """Value decoded from this schema node."""

    general_flags: GeneralFlags1355
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    armor_type: Optional[ArmorType1357] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["first_person_flags"]
    ) -> _base.FieldRef[FirstPersonFlags1354]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["general_flags"]
    ) -> _base.FieldRef[GeneralFlags1355]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["armor_type"]
    ) -> _base.FieldRef[Optional[ArmorType1357]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1352: _base.Variant = _base.Variant(
    path="ARMA/1:Biped Body Template/1:Body Template"
)


class WeightSliderMale1364(enum.IntFlag):
    """Named values from the pinned schema."""

    UNKNOWN_0 = 1
    ENABLED = 2


class WeightSliderFemale1365(enum.IntFlag):
    """Named values from the pinned schema."""

    UNKNOWN_0 = 1
    ENABLED = 2


class Structure1361(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ARMA/3:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "male_priority": _base.Binding(
            path="ARMA/3:Data/payload/0:Male Priority",
            kind="primitive",
            name="Male Priority",
        ),
        "female_priority": _base.Binding(
            path="ARMA/3:Data/payload/1:Female Priority",
            kind="primitive",
            name="Female Priority",
        ),
        "weight_slider_male": _base.Binding(
            path="ARMA/3:Data/payload/2:Weight slider - Male",
            kind="primitive",
            name="Weight slider - Male",
        ),
        "weight_slider_female": _base.Binding(
            path="ARMA/3:Data/payload/3:Weight slider - Female",
            kind="primitive",
            name="Weight slider - Female",
        ),
        "unknown": _base.Binding(
            path="ARMA/3:Data/payload/4:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "detection_sound_value": _base.Binding(
            path="ARMA/3:Data/payload/5:Detection Sound Value",
            kind="primitive",
            name="Detection Sound Value",
        ),
        "unknown_1368": _base.Binding(
            path="ARMA/3:Data/payload/6:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "weapon_adjust": _base.Binding(
            path="ARMA/3:Data/payload/7:Weapon Adjust",
            kind="primitive",
            name="Weapon Adjust",
        ),
    }

    male_priority: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    female_priority: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    weight_slider_male: WeightSliderMale1364
    """Value decoded from this schema node."""

    weight_slider_female: WeightSliderFemale1365
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    detection_sound_value: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    unknown_1368: bytes
    """Value decoded from this schema node."""

    weapon_adjust: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["male_priority"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_priority"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["weight_slider_male"]
    ) -> _base.FieldRef[WeightSliderMale1364]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["weight_slider_female"]
    ) -> _base.FieldRef[WeightSliderFemale1365]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["detection_sound_value"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_1368"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["weapon_adjust"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure1375(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1377": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1378": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1379": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_1377: bytes
    """Value decoded from this schema node."""

    unused_1378: bytes
    """Value decoded from this schema node."""

    unused_1379: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1377"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1378"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1379"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1375: _base.Variant = _base.Variant(
    path=(
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/0:Structure"
    )
)


class Structure1380(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_1383": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1384": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_1383: bytes
    """Value decoded from this schema node."""

    unused_1384: bytes
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
    def field(self, name: Literal["unused_1383"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1384"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1380: _base.Variant = _base.Variant(
    path=(
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/1:Structure"
    )
)


class Texture1388(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/2:Structure/1:Textures/element/2:Folder Hash"
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


class Structure1385(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_1392": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1393": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture1388, ...]
    """Value decoded from this schema node."""

    unused_1392: bytes
    """Value decoded from this schema node."""

    unused_1393: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture1388, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1392"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1393"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1385: _base.Variant = _base.Variant(
    path=(
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/2:Structure"
    )
)


class Texture1398(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/1:Textures/element/2:Folder Hash"
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


class Material1405(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/3:Materials/element/2:Folder Hash"
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


class Structure1394(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/1:Model Information/payload/va"
                "riants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture1398, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material1405, ...]
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
    ) -> _base.FieldRef[tuple[Texture1398, ...]]:
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
    ) -> _base.FieldRef[tuple[Material1405, ...]]:
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


_VARIANT_1394: _base.Variant = _base.Variant(
    path=(
        "ARMA/4:Male Biped Model/1:Model Information/payload/va"
        "riants/3:Structure"
    )
)


class AlternateTexture1412(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/4:Male Biped Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/2:Alternate Textures/payload/e"
                "lement/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/2:Alternate Textures/payload/e"
                "lement/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "ARMA/4:Male Biped Model/2:Alternate Textures/payload/e"
                "lement/2:3D Index"
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


class MaleBipedModel1370(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ARMA/4:Male Biped Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="ARMA/4:Male Biped Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="ARMA/4:Male Biped Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="ARMA/4:Male Biped Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure1375, _VARIANT_1375]
        | Annotated[Structure1380, _VARIANT_1380]
        | Annotated[Structure1385, _VARIANT_1385]
        | Annotated[Structure1394, _VARIANT_1394]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture1412, ...]] = None
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
            Annotated[Structure1375, _VARIANT_1375]
            | Annotated[Structure1380, _VARIANT_1380]
            | Annotated[Structure1385, _VARIANT_1385]
            | Annotated[Structure1394, _VARIANT_1394]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture1412, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure1421(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1423": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1424": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1425": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_1423: bytes
    """Value decoded from this schema node."""

    unused_1424: bytes
    """Value decoded from this schema node."""

    unused_1425: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1423"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1424"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1425"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1421: _base.Variant = _base.Variant(
    path=(
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/0:Structure"
    )
)


class Structure1426(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_1429": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1430": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_1429: bytes
    """Value decoded from this schema node."""

    unused_1430: bytes
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
    def field(self, name: Literal["unused_1429"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1430"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1426: _base.Variant = _base.Variant(
    path=(
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/1:Structure"
    )
)


class Texture1434(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/2:Structure/1:Textures/element/2:Folder Hash"
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


class Structure1431(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_1438": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1439": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture1434, ...]
    """Value decoded from this schema node."""

    unused_1438: bytes
    """Value decoded from this schema node."""

    unused_1439: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture1434, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1438"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1439"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1431: _base.Variant = _base.Variant(
    path=(
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/2:Structure"
    )
)


class Texture1444(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/1:Textures/element/2:Folder Hash"
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


class Material1451(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/3:Materials/element/2:Folder Hash"
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


class Structure1440(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/1:Model Information/payload/"
                "variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture1444, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material1451, ...]
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
    ) -> _base.FieldRef[tuple[Texture1444, ...]]:
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
    ) -> _base.FieldRef[tuple[Material1451, ...]]:
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


_VARIANT_1440: _base.Variant = _base.Variant(
    path=(
        "ARMA/5:Female Biped Model/1:Model Information/payload/"
        "variants/3:Structure"
    )
)


class AlternateTexture1458(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/5:Female Biped Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/2:Alternate Textures/payload"
                "/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/2:Alternate Textures/payload"
                "/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "ARMA/5:Female Biped Model/2:Alternate Textures/payload"
                "/element/2:3D Index"
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


class FemaleBipedModel1416(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ARMA/5:Female Biped Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="ARMA/5:Female Biped Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="ARMA/5:Female Biped Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="ARMA/5:Female Biped Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure1421, _VARIANT_1421]
        | Annotated[Structure1426, _VARIANT_1426]
        | Annotated[Structure1431, _VARIANT_1431]
        | Annotated[Structure1440, _VARIANT_1440]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture1458, ...]] = None
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
            Annotated[Structure1421, _VARIANT_1421]
            | Annotated[Structure1426, _VARIANT_1426]
            | Annotated[Structure1431, _VARIANT_1431]
            | Annotated[Structure1440, _VARIANT_1440]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture1458, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure1467(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1469": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1470": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1471": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_1469: bytes
    """Value decoded from this schema node."""

    unused_1470: bytes
    """Value decoded from this schema node."""

    unused_1471: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1469"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1470"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1471"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1467: _base.Variant = _base.Variant(
    path=(
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/0:Structure"
    )
)


class Structure1472(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_1475": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1476": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
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

    unused_1475: bytes
    """Value decoded from this schema node."""

    unused_1476: bytes
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
    def field(self, name: Literal["unused_1475"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1476"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1472: _base.Variant = _base.Variant(
    path=(
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/1:Structure"
    )
)


class Texture1480(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
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


class Structure1477(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_1484": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1485": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture1480, ...]
    """Value decoded from this schema node."""

    unused_1484: bytes
    """Value decoded from this schema node."""

    unused_1485: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture1480, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1484"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1485"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1477: _base.Variant = _base.Variant(
    path=(
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/2:Structure"
    )
)


class Texture1490(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
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


class Material1497(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
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


class Structure1486(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
                "iants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/1:Model Information/payload/var"
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

    textures: tuple[Texture1490, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material1497, ...]
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
    ) -> _base.FieldRef[tuple[Texture1490, ...]]:
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
    ) -> _base.FieldRef[tuple[Material1497, ...]]:
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


_VARIANT_1486: _base.Variant = _base.Variant(
    path=(
        "ARMA/6:Male 1st Person/1:Model Information/payload/var"
        "iants/3:Structure"
    )
)


class AlternateTexture1504(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/6:Male 1st Person/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/2:Alternate Textures/payload/el"
                "ement/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/2:Alternate Textures/payload/el"
                "ement/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "ARMA/6:Male 1st Person/2:Alternate Textures/payload/el"
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


class Male1StPerson1462(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ARMA/6:Male 1st Person"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="ARMA/6:Male 1st Person/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="ARMA/6:Male 1st Person/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="ARMA/6:Male 1st Person/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure1467, _VARIANT_1467]
        | Annotated[Structure1472, _VARIANT_1472]
        | Annotated[Structure1477, _VARIANT_1477]
        | Annotated[Structure1486, _VARIANT_1486]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture1504, ...]] = None
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
            Annotated[Structure1467, _VARIANT_1467]
            | Annotated[Structure1472, _VARIANT_1472]
            | Annotated[Structure1477, _VARIANT_1477]
            | Annotated[Structure1486, _VARIANT_1486]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture1504, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure1513(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1515": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1516": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1517": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_1515: bytes
    """Value decoded from this schema node."""

    unused_1516: bytes
    """Value decoded from this schema node."""

    unused_1517: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1515"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1516"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1517"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1513: _base.Variant = _base.Variant(
    path=(
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/0:Structure"
    )
)


class Structure1518(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_1521": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1522": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_1521: bytes
    """Value decoded from this schema node."""

    unused_1522: bytes
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
    def field(self, name: Literal["unused_1521"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1522"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1518: _base.Variant = _base.Variant(
    path=(
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/1:Structure"
    )
)


class Texture1526(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/2:Structure/1:Textures/element/2:Folder Hash"
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


class Structure1523(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_1530": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_1531": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture1526, ...]
    """Value decoded from this schema node."""

    unused_1530: bytes
    """Value decoded from this schema node."""

    unused_1531: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture1526, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1530"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_1531"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_1523: _base.Variant = _base.Variant(
    path=(
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/2:Structure"
    )
)


class Texture1536(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/1:Textures/element/2:Folder Hash"
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


class Material1543(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/3:Materials/element/2:Folder Hash"
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


class Structure1532(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/1:Model Information/payload/v"
                "ariants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture1536, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material1543, ...]
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
    ) -> _base.FieldRef[tuple[Texture1536, ...]]:
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
    ) -> _base.FieldRef[tuple[Material1543, ...]]:
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


_VARIANT_1532: _base.Variant = _base.Variant(
    path=(
        "ARMA/7:Female 1st Person/1:Model Information/payload/v"
        "ariants/3:Structure"
    )
)


class AlternateTexture1550(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ARMA/7:Female 1st Person/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/2:Alternate Textures/payload/"
                "element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/2:Alternate Textures/payload/"
                "element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "ARMA/7:Female 1st Person/2:Alternate Textures/payload/"
                "element/2:3D Index"
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


class Female1StPerson1508(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ARMA/7:Female 1st Person"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="ARMA/7:Female 1st Person/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="ARMA/7:Female 1st Person/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="ARMA/7:Female 1st Person/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure1513, _VARIANT_1513]
        | Annotated[Structure1518, _VARIANT_1518]
        | Annotated[Structure1523, _VARIANT_1523]
        | Annotated[Structure1532, _VARIANT_1532]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture1550, ...]] = None
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
            Annotated[Structure1513, _VARIANT_1513]
            | Annotated[Structure1518, _VARIANT_1518]
            | Annotated[Structure1523, _VARIANT_1523]
            | Annotated[Structure1532, _VARIANT_1532]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture1550, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ArmorAddonRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ARMA"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "ARMA"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="ARMA/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "biped_body_template": _base.Binding(
            path="ARMA/1:Biped Body Template",
            kind="choice",
            name="Biped Body Template",
        ),
        "race": _base.Binding(
            path="ARMA/2:Race",
            kind="subrecord",
            name="Race",
        ),
        "data": _base.Binding(
            path="ARMA/3:Data",
            kind="subrecord",
            name="Data",
        ),
        "male_biped_model": _base.Binding(
            path="ARMA/4:Male Biped Model",
            kind="sequence",
            name="Male Biped Model",
        ),
        "female_biped_model": _base.Binding(
            path="ARMA/5:Female Biped Model",
            kind="sequence",
            name="Female Biped Model",
        ),
        "male_1st_person": _base.Binding(
            path="ARMA/6:Male 1st Person",
            kind="sequence",
            name="Male 1st Person",
        ),
        "female_1st_person": _base.Binding(
            path="ARMA/7:Female 1st Person",
            kind="sequence",
            name="Female 1st Person",
        ),
        "male_skin_texture": _base.Binding(
            path="ARMA/8:Male Skin Texture",
            kind="subrecord",
            name="Male Skin Texture",
        ),
        "female_skin_texture": _base.Binding(
            path="ARMA/9:Female Skin texture",
            kind="subrecord",
            name="Female Skin texture",
        ),
        "male_skin_texture_swap_list": _base.Binding(
            path="ARMA/10:Male Skin Texture Swap List",
            kind="subrecord",
            name="Male Skin Texture Swap List",
        ),
        "female_skin_texture_swap_list": _base.Binding(
            path="ARMA/11:Female Skin Texture Swap List",
            kind="subrecord",
            name="Female Skin Texture Swap List",
        ),
        "additional_races": _base.Binding(
            path="ARMA/12:Additional Races",
            kind="repeat",
            name="Additional Races",
            repeated_path="ARMA/12:Additional Races/repeat/0:Race",
            child_kind="subrecord",
        ),
        "footstep_sound": _base.Binding(
            path="ARMA/13:Footstep Sound",
            kind="subrecord",
            name="Footstep Sound",
        ),
        "art_object": _base.Binding(
            path="ARMA/14:Art Object",
            kind="subrecord",
            name="Art Object",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    biped_body_template: Optional[
        Annotated[Structure1347, _VARIANT_1346]
        | Annotated[Structure1353, _VARIANT_1352]
    ] = None
    """Value decoded from this schema node."""

    race: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    data: Optional[Structure1361] = None
    """Value decoded from this schema node."""

    male_biped_model: Optional[MaleBipedModel1370] = None
    """Value decoded from this schema node."""

    female_biped_model: Optional[FemaleBipedModel1416] = None
    """Value decoded from this schema node."""

    male_1st_person: Optional[Male1StPerson1462] = None
    """Value decoded from this schema node."""

    female_1st_person: Optional[Female1StPerson1508] = None
    """Value decoded from this schema node."""

    male_skin_texture: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    female_skin_texture: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    male_skin_texture_swap_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    female_skin_texture_swap_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    additional_races: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    footstep_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    art_object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["biped_body_template"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure1347, _VARIANT_1346]
            | Annotated[Structure1353, _VARIANT_1352]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["race"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure1361]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_biped_model"]
    ) -> _base.FieldRef[Optional[MaleBipedModel1370]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_biped_model"]
    ) -> _base.FieldRef[Optional[FemaleBipedModel1416]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_1st_person"]
    ) -> _base.FieldRef[Optional[Male1StPerson1462]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_1st_person"]
    ) -> _base.FieldRef[Optional[Female1StPerson1508]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_skin_texture"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_skin_texture"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_skin_texture_swap_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_skin_texture_swap_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["additional_races"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["footstep_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["art_object"]
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
