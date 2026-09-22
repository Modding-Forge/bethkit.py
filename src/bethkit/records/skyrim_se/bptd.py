"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure6125(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6127": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6128": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6129": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_6127: bytes
    """Value decoded from this schema node."""

    unused_6128: bytes
    """Value decoded from this schema node."""

    unused_6129: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6127"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6128"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6129"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6125: _base.Variant = _base.Variant(
    path=("BPTD/1:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure6130(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_6133": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6134": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_6133: bytes
    """Value decoded from this schema node."""

    unused_6134: bytes
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
    def field(self, name: Literal["unused_6133"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6134"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6130: _base.Variant = _base.Variant(
    path=("BPTD/1:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture6138(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/2:Folder Hash"
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


class Structure6135(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_6142": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6143": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture6138, ...]
    """Value decoded from this schema node."""

    unused_6142: bytes
    """Value decoded from this schema node."""

    unused_6143: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture6138, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6142"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6143"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6135: _base.Variant = _base.Variant(
    path=("BPTD/1:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture6148(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/2:Folder Hash"
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


class Material6155(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/2:Folder Hash"
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


class Structure6144(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "BPTD/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture6148, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material6155, ...]
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
    ) -> _base.FieldRef[tuple[Texture6148, ...]]:
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
    ) -> _base.FieldRef[tuple[Material6155, ...]]:
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


_VARIANT_6144: _base.Variant = _base.Variant(
    path=("BPTD/1:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture6162(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/1:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "BPTD/1:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "BPTD/1:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "BPTD/1:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model6120(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "BPTD/1:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="BPTD/1:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="BPTD/1:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="BPTD/1:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure6125, _VARIANT_6125]
        | Annotated[Structure6130, _VARIANT_6130]
        | Annotated[Structure6135, _VARIANT_6135]
        | Annotated[Structure6144, _VARIANT_6144]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture6162, ...]] = None
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
            Annotated[Structure6125, _VARIANT_6125]
            | Annotated[Structure6130, _VARIANT_6130]
            | Annotated[Structure6135, _VARIANT_6135]
            | Annotated[Structure6144, _VARIANT_6144]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture6162, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags6181(enum.IntFlag):
    """Named values from the pinned schema."""

    SEVERABLE = 1
    IK_DATA = 2
    IK_DATA_BIPED_DATA = 4
    EXPLODABLE = 8
    IK_DATA_IS_HEAD = 16
    IK_DATA_HEADTRACKING = 32
    TO_HIT_CHANCE_ABSOLUTE = 64


class PartType6182(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TORSO = 0
    HEAD = 1
    EYE = 2
    LOOK_AT = 3
    FLY_GRAB = 4
    SADDLE = 5


class ActorValue6184(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    AGGRESSION = 0
    CONFIDENCE = 1
    ENERGY = 2
    MORALITY = 3
    MOOD = 4
    ASSISTANCE = 5
    ONE_HANDED = 6
    TWO_HANDED = 7
    ARCHERY = 8
    BLOCK = 9
    SMITHING = 10
    HEAVY_ARMOR = 11
    LIGHT_ARMOR = 12
    PICKPOCKET = 13
    LOCKPICKING = 14
    SNEAK = 15
    ALCHEMY = 16
    SPEECH = 17
    ALTERATION = 18
    CONJURATION = 19
    DESTRUCTION = 20
    ILLUSION = 21
    RESTORATION = 22
    ENCHANTING = 23
    HEALTH = 24
    MAGICKA = 25
    STAMINA = 26
    HEAL_RATE = 27
    MAGICKA_RATE = 28
    STAMINA_RATE = 29
    SPEED_MULT = 30
    INVENTORY_WEIGHT = 31
    CARRY_WEIGHT = 32
    CRITICAL_CHANCE = 33
    MELEE_DAMAGE = 34
    UNARMED_DAMAGE = 35
    MASS = 36
    VOICE_POINTS = 37
    VOICE_RATE = 38
    DAMAGE_RESIST = 39
    POISON_RESIST = 40
    RESIST_FIRE = 41
    RESIST_SHOCK = 42
    RESIST_FROST = 43
    RESIST_MAGIC = 44
    RESIST_DISEASE = 45
    UNKNOWN_46 = 46
    UNKNOWN_47 = 47
    UNKNOWN_48 = 48
    UNKNOWN_49 = 49
    UNKNOWN_50 = 50
    UNKNOWN_51 = 51
    UNKNOWN_52 = 52
    PARALYSIS = 53
    INVISIBILITY = 54
    NIGHT_EYE = 55
    DETECT_LIFE_RANGE = 56
    WATER_BREATHING = 57
    WATER_WALKING = 58
    UNKNOWN_59 = 59
    FAME = 60
    INFAMY = 61
    JUMPING_BONUS = 62
    WARD_POWER = 63
    RIGHT_ITEM_CHARGE = 64
    ARMOR_PERKS = 65
    SHIELD_PERKS = 66
    WARD_DEFLECTION = 67
    VARIABLE01 = 68
    VARIABLE02 = 69
    VARIABLE03 = 70
    VARIABLE04 = 71
    VARIABLE05 = 72
    VARIABLE06 = 73
    VARIABLE07 = 74
    VARIABLE08 = 75
    VARIABLE09 = 76
    VARIABLE10 = 77
    BOW_SPEED_BONUS = 78
    FAVOR_ACTIVE = 79
    FAVORS_PER_DAY = 80
    FAVORS_PER_DAY_TIMER = 81
    LEFT_ITEM_CHARGE = 82
    ABSORB_CHANCE = 83
    BLINDNESS = 84
    WEAPON_SPEED_MULT = 85
    SHOUT_RECOVERY_MULT = 86
    BOW_STAGGER_BONUS = 87
    TELEKINESIS = 88
    FAVOR_POINTS_BONUS = 89
    LAST_BRIBED_INTIMIDATED = 90
    LAST_FLATTERED = 91
    MOVEMENT_NOISE_MULT = 92
    BYPASS_VENDOR_STOLEN_CHECK = 93
    BYPASS_VENDOR_KEYWORD_CHECK = 94
    WAITING_FOR_PLAYER = 95
    ONE_HANDED_MODIFIER = 96
    TWO_HANDED_MODIFIER = 97
    MARKSMAN_MODIFIER = 98
    BLOCK_MODIFIER = 99
    SMITHING_MODIFIER = 100
    HEAVY_ARMOR_MODIFIER = 101
    LIGHT_ARMOR_MODIFIER = 102
    PICKPOCKET_MODIFIER = 103
    LOCKPICKING_MODIFIER = 104
    SNEAKING_MODIFIER = 105
    ALCHEMY_MODIFIER = 106
    SPEECHCRAFT_MODIFIER = 107
    ALTERATION_MODIFIER = 108
    CONJURATION_MODIFIER = 109
    DESTRUCTION_MODIFIER = 110
    ILLUSION_MODIFIER = 111
    RESTORATION_MODIFIER = 112
    ENCHANTING_MODIFIER = 113
    ONE_HANDED_SKILL_ADVANCE = 114
    TWO_HANDED_SKILL_ADVANCE = 115
    MARKSMAN_SKILL_ADVANCE = 116
    BLOCK_SKILL_ADVANCE = 117
    SMITHING_SKILL_ADVANCE = 118
    HEAVY_ARMOR_SKILL_ADVANCE = 119
    LIGHT_ARMOR_SKILL_ADVANCE = 120
    PICKPOCKET_SKILL_ADVANCE = 121
    LOCKPICKING_SKILL_ADVANCE = 122
    SNEAKING_SKILL_ADVANCE = 123
    ALCHEMY_SKILL_ADVANCE = 124
    SPEECHCRAFT_SKILL_ADVANCE = 125
    ALTERATION_SKILL_ADVANCE = 126
    CONJURATION_SKILL_ADVANCE = 127
    DESTRUCTION_SKILL_ADVANCE = 128
    ILLUSION_SKILL_ADVANCE = 129
    RESTORATION_SKILL_ADVANCE = 130
    ENCHANTING_SKILL_ADVANCE = 131
    LEFT_WEAPON_SPEED_MULTIPLY = 132
    DRAGON_SOULS = 133
    COMBAT_HEALTH_REGEN_MULTIPLY = 134
    ONE_HANDED_POWER_MODIFIER = 135
    TWO_HANDED_POWER_MODIFIER = 136
    MARKSMAN_POWER_MODIFIER = 137
    BLOCK_POWER_MODIFIER = 138
    SMITHING_POWER_MODIFIER = 139
    HEAVY_ARMOR_POWER_MODIFIER = 140
    LIGHT_ARMOR_POWER_MODIFIER = 141
    PICKPOCKET_POWER_MODIFIER = 142
    LOCKPICKING_POWER_MODIFIER = 143
    SNEAKING_POWER_MODIFIER = 144
    ALCHEMY_POWER_MODIFIER = 145
    SPEECHCRAFT_POWER_MODIFIER = 146
    ALTERATION_POWER_MODIFIER = 147
    CONJURATION_POWER_MODIFIER = 148
    DESTRUCTION_POWER_MODIFIER = 149
    ILLUSION_POWER_MODIFIER = 150
    RESTORATION_POWER_MODIFIER = 151
    ENCHANTING_POWER_MODIFIER = 152
    DRAGON_REND = 153
    ATTACK_DAMAGE_MULT = 154
    HEAL_RATE_MULT = 155
    MAGICKA_RATE_MULT = 156
    STAMINA_RATE_MULT = 157
    WEREWOLF_PERKS = 158
    VAMPIRE_PERKS = 159
    GRAB_ACTOR_OFFSET = 160
    GRABBED = 161
    UNKNOWN_162 = 162
    REFLECT_DAMAGE = 163


class Position6197(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
        ":Gore Effects Positioning/0:Position"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/0:Position/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/0:Position/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/0:Position/2:Z"
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


class Rotation6201(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
        ":Gore Effects Positioning/1:Rotation"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/1:Rotation/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/1:Rotation/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/1:Rotation/2:Z"
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


class GoreEffectsPositioning6196(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
        ":Gore Effects Positioning"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "position": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/0:Position"
            ),
            kind="struct",
            name="Position",
        ),
        "rotation": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning/1:Rotation"
            ),
            kind="struct",
            name="Rotation",
        ),
    }

    position: Position6197
    """Value decoded from this schema node."""

    rotation: Rotation6201
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position6197]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotation"]) -> _base.FieldRef[Rotation6201]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure6179(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "damage_mult": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/0:"
                "Damage Mult"
            ),
            kind="primitive",
            name="Damage Mult",
        ),
        "flags": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "part_type": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/2:"
                "Part Type"
            ),
            kind="primitive",
            name="Part Type",
        ),
        "health_percent": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/3:"
                "Health Percent"
            ),
            kind="primitive",
            name="Health Percent",
        ),
        "actor_value": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/4:"
                "Actor Value"
            ),
            kind="primitive",
            name="Actor Value",
        ),
        "to_hit_chance": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/5:"
                "To Hit Chance"
            ),
            kind="primitive",
            name="To Hit Chance",
        ),
        "explodable_explosion_chance": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/6:"
                "Explodable - Explosion Chance %"
            ),
            kind="primitive",
            name="Explodable - Explosion Chance %",
        ),
        "explodable_debris_count": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/7:"
                "Explodable - Debris Count"
            ),
            kind="primitive",
            name="Explodable - Debris Count",
        ),
        "explodable_debris": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/8:"
                "Explodable - Debris"
            ),
            kind="primitive",
            name="Explodable - Debris",
        ),
        "explodable_explosion": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/9:"
                "Explodable - Explosion"
            ),
            kind="primitive",
            name="Explodable - Explosion",
        ),
        "tracking_max_angle": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/10"
                ":Tracking Max Angle"
            ),
            kind="primitive",
            name="Tracking Max Angle",
        ),
        "explodable_debris_scale": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/11"
                ":Explodable - Debris Scale"
            ),
            kind="primitive",
            name="Explodable - Debris Scale",
        ),
        "severable_debris_count": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/12"
                ":Severable - Debris Count"
            ),
            kind="primitive",
            name="Severable - Debris Count",
        ),
        "severable_debris": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/13"
                ":Severable - Debris"
            ),
            kind="primitive",
            name="Severable - Debris",
        ),
        "severable_explosion": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/14"
                ":Severable - Explosion"
            ),
            kind="primitive",
            name="Severable - Explosion",
        ),
        "severable_debris_scale": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/15"
                ":Severable - Debris Scale"
            ),
            kind="primitive",
            name="Severable - Debris Scale",
        ),
        "gore_effects_positioning": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/16"
                ":Gore Effects Positioning"
            ),
            kind="struct",
            name="Gore Effects Positioning",
        ),
        "severable_impact_data_set": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/17"
                ":Severable - Impact DataSet"
            ),
            kind="primitive",
            name="Severable - Impact DataSet",
        ),
        "explodable_impact_data_set": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/18"
                ":Explodable - Impact DataSet"
            ),
            kind="primitive",
            name="Explodable - Impact DataSet",
        ),
        "severable_decal_count": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/19"
                ":Severable - Decal Count"
            ),
            kind="primitive",
            name="Severable - Decal Count",
        ),
        "explodable_decal_count": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/20"
                ":Explodable - Decal Count"
            ),
            kind="primitive",
            name="Explodable - Decal Count",
        ),
        "unknown": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/21:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "limb_replacement_scale": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/5:BPND/payload/22"
                ":Limb Replacement Scale"
            ),
            kind="primitive",
            name="Limb Replacement Scale",
        ),
    }

    damage_mult: float
    """Value decoded from this schema node."""

    flags: Flags6181
    """Value decoded from this schema node."""

    part_type: PartType6182
    """Value decoded from this schema node."""

    health_percent: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    actor_value: ActorValue6184
    """Value decoded from this schema node."""

    to_hit_chance: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    explodable_explosion_chance: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    explodable_debris_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=65535)
    ]
    """Value decoded from this schema node."""

    explodable_debris: _values.FormId
    """Value decoded from this schema node."""

    explodable_explosion: _values.FormId
    """Value decoded from this schema node."""

    tracking_max_angle: float
    """Value decoded from this schema node."""

    explodable_debris_scale: float
    """Value decoded from this schema node."""

    severable_debris_count: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    severable_debris: _values.FormId
    """Value decoded from this schema node."""

    severable_explosion: _values.FormId
    """Value decoded from this schema node."""

    severable_debris_scale: float
    """Value decoded from this schema node."""

    gore_effects_positioning: GoreEffectsPositioning6196
    """Value decoded from this schema node."""

    severable_impact_data_set: _values.FormId
    """Value decoded from this schema node."""

    explodable_impact_data_set: _values.FormId
    """Value decoded from this schema node."""

    severable_decal_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    explodable_decal_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    limb_replacement_scale: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["damage_mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags6181]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["part_type"]) -> _base.FieldRef[PartType6182]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["health_percent"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actor_value"]
    ) -> _base.FieldRef[ActorValue6184]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["to_hit_chance"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explodable_explosion_chance"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explodable_debris_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explodable_debris"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explodable_explosion"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tracking_max_angle"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explodable_debris_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["severable_debris_count"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["severable_debris"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["severable_explosion"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["severable_debris_scale"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["gore_effects_positioning"]
    ) -> _base.FieldRef[GoreEffectsPositioning6196]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["severable_impact_data_set"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explodable_impact_data_set"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["severable_decal_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explodable_decal_count"]
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
        self, name: Literal["limb_replacement_scale"]
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


class Structure6217(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6219": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6220": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6221": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_6219: bytes
    """Value decoded from this schema node."""

    unused_6220: bytes
    """Value decoded from this schema node."""

    unused_6221: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6219"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6220"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6221"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6217: _base.Variant = _base.Variant(
    path=(
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/0:Structure"
    )
)


class Structure6222(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_6225": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6226": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_6225: bytes
    """Value decoded from this schema node."""

    unused_6226: bytes
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
    def field(self, name: Literal["unused_6225"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6226"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6222: _base.Variant = _base.Variant(
    path=(
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/1:Structure"
    )
)


class Texture6230(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/2:Structure/1:Textures/element/0:F"
                "ile Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/2:Structure/1:Textures/element/1:E"
                "xtension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/2:Structure/1:Textures/element/2:F"
                "older Hash"
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


class Structure6227(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_6234": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6235": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture6230, ...]
    """Value decoded from this schema node."""

    unused_6234: bytes
    """Value decoded from this schema node."""

    unused_6235: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture6230, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6234"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6235"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6227: _base.Variant = _base.Variant(
    path=(
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/2:Structure"
    )
)


class Texture6240(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/1:Textures/element/0:F"
                "ile Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/1:Textures/element/1:E"
                "xtension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/1:Textures/element/2:F"
                "older Hash"
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


class Material6247(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/3:Materials/element/0:"
                "File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/3:Materials/element/1:"
                "Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/3:Materials/element/2:"
                "Folder Hash"
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


class Structure6236(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
                "on/payload/variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture6240, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material6247, ...]
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
    ) -> _base.FieldRef[tuple[Texture6240, ...]]:
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
    ) -> _base.FieldRef[tuple[Material6247, ...]]:
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


_VARIANT_6236: _base.Variant = _base.Variant(
    path=(
        "BPTD/2:Body Parts/repeat/0:Body Part/8:Model Informati"
        "on/payload/variants/3:Structure"
    )
)


class BodyPart6167(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "BPTD/2:Body Parts/repeat/0:Body Part"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "part_name": _base.Binding(
            path="BPTD/2:Body Parts/repeat/0:Body Part/0:Part Name",
            kind="subrecord",
            name="Part Name",
        ),
        "pose_matching": _base.Binding(
            path=("BPTD/2:Body Parts/repeat/0:Body Part/1:Pose Matching"),
            kind="subrecord",
            name="Pose Matching",
        ),
        "part_node": _base.Binding(
            path="BPTD/2:Body Parts/repeat/0:Body Part/2:Part Node",
            kind="subrecord",
            name="Part Node",
        ),
        "vats_target": _base.Binding(
            path=("BPTD/2:Body Parts/repeat/0:Body Part/3:VATS Target"),
            kind="subrecord",
            name="VATS Target",
        ),
        "ik_data_start_node": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/4:IK Data - Start Node"
            ),
            kind="subrecord",
            name="IK Data - Start Node",
        ),
        "bpnd": _base.Binding(
            path="BPTD/2:Body Parts/repeat/0:Body Part/5:BPND",
            kind="subrecord",
            name="BPND",
        ),
        "limb_replacement_model": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/6:Limb Replacement Model"
            ),
            kind="subrecord",
            name="Limb Replacement Model",
        ),
        "gore_effects_target_bone": _base.Binding(
            path=(
                "BPTD/2:Body Parts/repeat/0:Body Part/7:Gore Effects - "
                "Target Bone"
            ),
            kind="subrecord",
            name="Gore Effects - Target Bone",
        ),
        "model_information_value": _base.Binding(
            path=("BPTD/2:Body Parts/repeat/0:Body Part/8:Model Information"),
            kind="subrecord",
            name="Model Information",
        ),
    }

    part_name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    pose_matching: Optional[str] = None
    """Value decoded from this schema node."""

    part_node: Optional[str] = None
    """Value decoded from this schema node."""

    vats_target: Optional[str] = None
    """Value decoded from this schema node."""

    ik_data_start_node: Optional[str] = None
    """Value decoded from this schema node."""

    bpnd: Optional[Structure6179] = None
    """Value decoded from this schema node."""

    limb_replacement_model: Optional[str] = None
    """Value decoded from this schema node."""

    gore_effects_target_bone: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure6217, _VARIANT_6217]
        | Annotated[Structure6222, _VARIANT_6222]
        | Annotated[Structure6227, _VARIANT_6227]
        | Annotated[Structure6236, _VARIANT_6236]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["part_name"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["pose_matching"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["part_node"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vats_target"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ik_data_start_node"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bpnd"]
    ) -> _base.FieldRef[Optional[Structure6179]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["limb_replacement_model"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["gore_effects_target_bone"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_information_value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure6217, _VARIANT_6217]
            | Annotated[Structure6222, _VARIANT_6222]
            | Annotated[Structure6227, _VARIANT_6227]
            | Annotated[Structure6236, _VARIANT_6236]
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


class BodyPartDataRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "BPTD"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "BPTD"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="BPTD/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "model": _base.Binding(
            path="BPTD/1:Model",
            kind="unordered",
            name="Model",
        ),
        "body_parts": _base.Binding(
            path="BPTD/2:Body Parts",
            kind="repeat",
            name="Body Parts",
            repeated_path="BPTD/2:Body Parts/repeat/0:Body Part",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    model: Optional[Model6120] = None
    """Value decoded from this schema node."""

    body_parts: tuple[BodyPart6167, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model6120]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["body_parts"]
    ) -> _base.FieldRef[tuple[BodyPart6167, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
