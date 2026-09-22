"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class FirstPersonFlags14065(enum.IntFlag):
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


class ArmorType14068(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LIGHT_ARMOR = 0
    HEAVY_ARMOR = 1
    CLOTHING = 2


class Structure14064(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/6:Biped Body Template/0:Biped Body Template/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "first_person_flags": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/0:Biped Body Template/paylo"
                "ad/0:First Person Flags"
            ),
            kind="primitive",
            name="First Person Flags",
        ),
        "general_flags": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/0:Biped Body Template/paylo"
                "ad/1:General Flags"
            ),
            kind="custom",
            name="General Flags",
        ),
        "unused": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/0:Biped Body Template/paylo"
                "ad/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "armor_type": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/0:Biped Body Template/paylo"
                "ad/3:Armor Type"
            ),
            kind="primitive",
            name="Armor Type",
        ),
    }

    first_person_flags: FirstPersonFlags14065
    """Value decoded from this schema node."""

    general_flags: Literal[0]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    armor_type: ArmorType14068
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["first_person_flags"]
    ) -> _base.FieldRef[FirstPersonFlags14065]:
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
    ) -> _base.FieldRef[ArmorType14068]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14063: _base.Variant = _base.Variant(
    path="RACE/6:Biped Body Template/0:Biped Body Template"
)


class FirstPersonFlags14071(enum.IntFlag):
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


class GeneralFlags14072(enum.IntFlag):
    """Named values from the pinned schema."""

    ARMA_MODULATES_VOICE = 1
    UNKNOWN_2 = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    ARMO_NON_PLAYABLE = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    UNKNOWN_8 = 128


class ArmorType14074(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LIGHT_ARMOR = 0
    HEAVY_ARMOR = 1
    CLOTHING = 2


class Structure14070(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/6:Biped Body Template/1:Body Template/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "first_person_flags": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/1:Body Template/payload/0:F"
                "irst Person Flags"
            ),
            kind="primitive",
            name="First Person Flags",
        ),
        "general_flags": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/1:Body Template/payload/1:G"
                "eneral Flags"
            ),
            kind="primitive",
            name="General Flags",
        ),
        "unused": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/1:Body Template/payload/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "armor_type": _base.Binding(
            path=(
                "RACE/6:Biped Body Template/1:Body Template/payload/3:A"
                "rmor Type"
            ),
            kind="primitive",
            name="Armor Type",
        ),
    }

    first_person_flags: FirstPersonFlags14071
    """Value decoded from this schema node."""

    general_flags: GeneralFlags14072
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    armor_type: Optional[ArmorType14074] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["first_person_flags"]
    ) -> _base.FieldRef[FirstPersonFlags14071]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["general_flags"]
    ) -> _base.FieldRef[GeneralFlags14072]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["armor_type"]
    ) -> _base.FieldRef[Optional[ArmorType14074]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14069: _base.Variant = _base.Variant(
    path="RACE/6:Biped Body Template/1:Body Template"
)


class Skill14084(_values.OpenIntEnum):
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


class SkillBoost14083(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/9:DATA/payload/0:Skill Boosts/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "skill": _base.Binding(
            path=("RACE/9:DATA/payload/0:Skill Boosts/element/0:Skill"),
            kind="primitive",
            name="Skill",
        ),
        "boost": _base.Binding(
            path=("RACE/9:DATA/payload/0:Skill Boosts/element/1:Boost"),
            kind="primitive",
            name="Boost",
        ),
    }

    skill: Skill14084
    """Value decoded from this schema node."""

    boost: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["skill"]) -> _base.FieldRef[Skill14084]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["boost"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
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


class Flags14091(enum.IntFlag):
    """Named values from the pinned schema."""

    PLAYABLE = 1
    FACE_GEN_HEAD = 2
    CHILD = 4
    TILT_FRONT_BACK = 8
    TILT_LEFT_RIGHT = 16
    NO_SHADOW = 32
    SWIMS = 64
    FLIES = 128
    WALKS = 256
    IMMOBILE = 512
    NOT_PUSHABLE = 1024
    NO_COMBAT_IN_WATER = 2048
    NO_ROTATING_TO_HEAD_TRACK = 4096
    DON_T_SHOW_BLOOD_SPRAY = 8192
    DON_T_SHOW_BLOOD_DECAL = 16384
    USES_HEAD_TRACK_ANIMS = 32768
    SPELLS_ALIGN_W_MAGIC_NODE = 65536
    USE_WORLD_RAYCASTS_FOR_FOOT_IK = 131072
    ALLOW_RAGDOLL_COLLISION = 262144
    REGEN_HP_IN_COMBAT = 524288
    CAN_T_OPEN_DOORS = 1048576
    ALLOW_PC_DIALOGUE = 2097152
    NO_KNOCKDOWNS = 4194304
    ALLOW_PICKPOCKET = 8388608
    ALWAYS_USE_PROXY_CONTROLLER = 16777216
    DON_T_SHOW_WEAPON_BLOOD = 33554432
    OVERLAY_HEAD_PART_LIST = 67108864
    OVERRIDE_HEAD_PART_LIST = 134217728
    CAN_PICKUP_ITEMS = 268435456
    ALLOW_MULTIPLE_MEMBRANE_SHADERS = 536870912
    CAN_DUAL_WIELD = 1073741824
    AVOIDS_ROADS = 2147483648


class Size14099(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    EXTRA_LARGE = 3


class HeadBipedObject14100(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    VALUE_30_HEAD = 0
    VALUE_31_HAIR = 1
    VALUE_32_BODY = 2
    VALUE_33_HANDS = 3
    VALUE_34_FOREARMS = 4
    VALUE_35_AMULET = 5
    VALUE_36_RING = 6
    VALUE_37_FEET = 7
    VALUE_38_CALVES = 8
    VALUE_39_SHIELD = 9
    VALUE_40_TAIL = 10
    VALUE_41_LONG_HAIR = 11
    VALUE_42_CIRCLET = 12
    VALUE_43_EARS = 13
    VALUE_44_UNNAMED = 14
    VALUE_45_UNNAMED = 15
    VALUE_46_UNNAMED = 16
    VALUE_47_UNNAMED = 17
    VALUE_48_UNNAMED = 18
    VALUE_49_UNNAMED = 19
    VALUE_50_DECAPITATE_HEAD = 20
    VALUE_51_DECAPITATE = 21
    VALUE_52_UNNAMED = 22
    VALUE_53_UNNAMED = 23
    VALUE_54_UNNAMED = 24
    VALUE_55_UNNAMED = 25
    VALUE_56_UNNAMED = 26
    VALUE_57_UNNAMED = 27
    VALUE_58_UNNAMED = 28
    VALUE_59_UNNAMED = 29
    VALUE_60_UNNAMED = 30
    VALUE_61_FX01 = 31


class HairBipedObject14101(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    VALUE_30_HEAD = 0
    VALUE_31_HAIR = 1
    VALUE_32_BODY = 2
    VALUE_33_HANDS = 3
    VALUE_34_FOREARMS = 4
    VALUE_35_AMULET = 5
    VALUE_36_RING = 6
    VALUE_37_FEET = 7
    VALUE_38_CALVES = 8
    VALUE_39_SHIELD = 9
    VALUE_40_TAIL = 10
    VALUE_41_LONG_HAIR = 11
    VALUE_42_CIRCLET = 12
    VALUE_43_EARS = 13
    VALUE_44_UNNAMED = 14
    VALUE_45_UNNAMED = 15
    VALUE_46_UNNAMED = 16
    VALUE_47_UNNAMED = 17
    VALUE_48_UNNAMED = 18
    VALUE_49_UNNAMED = 19
    VALUE_50_DECAPITATE_HEAD = 20
    VALUE_51_DECAPITATE = 21
    VALUE_52_UNNAMED = 22
    VALUE_53_UNNAMED = 23
    VALUE_54_UNNAMED = 24
    VALUE_55_UNNAMED = 25
    VALUE_56_UNNAMED = 26
    VALUE_57_UNNAMED = 27
    VALUE_58_UNNAMED = 28
    VALUE_59_UNNAMED = 29
    VALUE_60_UNNAMED = 30
    VALUE_61_FX01 = 31


class ShieldBipedObject14103(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    VALUE_30_HEAD = 0
    VALUE_31_HAIR = 1
    VALUE_32_BODY = 2
    VALUE_33_HANDS = 3
    VALUE_34_FOREARMS = 4
    VALUE_35_AMULET = 5
    VALUE_36_RING = 6
    VALUE_37_FEET = 7
    VALUE_38_CALVES = 8
    VALUE_39_SHIELD = 9
    VALUE_40_TAIL = 10
    VALUE_41_LONG_HAIR = 11
    VALUE_42_CIRCLET = 12
    VALUE_43_EARS = 13
    VALUE_44_UNNAMED = 14
    VALUE_45_UNNAMED = 15
    VALUE_46_UNNAMED = 16
    VALUE_47_UNNAMED = 17
    VALUE_48_UNNAMED = 18
    VALUE_49_UNNAMED = 19
    VALUE_50_DECAPITATE_HEAD = 20
    VALUE_51_DECAPITATE = 21
    VALUE_52_UNNAMED = 22
    VALUE_53_UNNAMED = 23
    VALUE_54_UNNAMED = 24
    VALUE_55_UNNAMED = 25
    VALUE_56_UNNAMED = 26
    VALUE_57_UNNAMED = 27
    VALUE_58_UNNAMED = 28
    VALUE_59_UNNAMED = 29
    VALUE_60_UNNAMED = 30
    VALUE_61_FX01 = 31


class BodyBipedObject14109(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    VALUE_30_HEAD = 0
    VALUE_31_HAIR = 1
    VALUE_32_BODY = 2
    VALUE_33_HANDS = 3
    VALUE_34_FOREARMS = 4
    VALUE_35_AMULET = 5
    VALUE_36_RING = 6
    VALUE_37_FEET = 7
    VALUE_38_CALVES = 8
    VALUE_39_SHIELD = 9
    VALUE_40_TAIL = 10
    VALUE_41_LONG_HAIR = 11
    VALUE_42_CIRCLET = 12
    VALUE_43_EARS = 13
    VALUE_44_UNNAMED = 14
    VALUE_45_UNNAMED = 15
    VALUE_46_UNNAMED = 16
    VALUE_47_UNNAMED = 17
    VALUE_48_UNNAMED = 18
    VALUE_49_UNNAMED = 19
    VALUE_50_DECAPITATE_HEAD = 20
    VALUE_51_DECAPITATE = 21
    VALUE_52_UNNAMED = 22
    VALUE_53_UNNAMED = 23
    VALUE_54_UNNAMED = 24
    VALUE_55_UNNAMED = 25
    VALUE_56_UNNAMED = 26
    VALUE_57_UNNAMED = 27
    VALUE_58_UNNAMED = 28
    VALUE_59_UNNAMED = 29
    VALUE_60_UNNAMED = 30
    VALUE_61_FX01 = 31


class Flags214114(enum.IntFlag):
    """Named values from the pinned schema."""

    USE_ADVANCED_AVOIDANCE = 1
    NON_HOSTILE = 2
    UNKNOWN_2 = 4
    UNKNOWN_3 = 8
    ALLOW_MOUNTED_COMBAT = 16


class MountData14115(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/9:DATA/payload/30:Mount Data"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "mount_offset_x": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/0:Mount Offset X"),
            kind="primitive",
            name="Mount Offset X",
        ),
        "mount_offset_y": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/1:Mount Offset Y"),
            kind="primitive",
            name="Mount Offset Y",
        ),
        "mount_offset_z": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/2:Mount Offset Z"),
            kind="primitive",
            name="Mount Offset Z",
        ),
        "dismount_offset_x": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/3:Dismount Offset X"),
            kind="primitive",
            name="Dismount Offset X",
        ),
        "dismount_offset_y": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/4:Dismount Offset Y"),
            kind="primitive",
            name="Dismount Offset Y",
        ),
        "dismount_offset_z": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/5:Dismount Offset Z"),
            kind="primitive",
            name="Dismount Offset Z",
        ),
        "mount_camera_offset_x": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/6:Mount Camera Offset X"),
            kind="primitive",
            name="Mount Camera Offset X",
        ),
        "mount_camera_offset_y": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/7:Mount Camera Offset Y"),
            kind="primitive",
            name="Mount Camera Offset Y",
        ),
        "mount_camera_offset_z": _base.Binding(
            path=("RACE/9:DATA/payload/30:Mount Data/8:Mount Camera Offset Z"),
            kind="primitive",
            name="Mount Camera Offset Z",
        ),
    }

    mount_offset_x: float
    """Value decoded from this schema node."""

    mount_offset_y: float
    """Value decoded from this schema node."""

    mount_offset_z: float
    """Value decoded from this schema node."""

    dismount_offset_x: float
    """Value decoded from this schema node."""

    dismount_offset_y: float
    """Value decoded from this schema node."""

    dismount_offset_z: float
    """Value decoded from this schema node."""

    mount_camera_offset_x: float
    """Value decoded from this schema node."""

    mount_camera_offset_y: float
    """Value decoded from this schema node."""

    mount_camera_offset_z: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["mount_offset_x"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["mount_offset_y"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["mount_offset_z"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["dismount_offset_x"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["dismount_offset_y"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["dismount_offset_z"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["mount_camera_offset_x"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["mount_camera_offset_y"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["mount_camera_offset_z"]
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


class Structure14081(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/9:DATA/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "skill_boosts": _base.Binding(
            path="RACE/9:DATA/payload/0:Skill Boosts",
            kind="array",
            name="Skill Boosts",
        ),
        "unknown": _base.Binding(
            path="RACE/9:DATA/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "male_height": _base.Binding(
            path="RACE/9:DATA/payload/2:Male Height",
            kind="primitive",
            name="Male Height",
        ),
        "female_height": _base.Binding(
            path="RACE/9:DATA/payload/3:Female Height",
            kind="primitive",
            name="Female Height",
        ),
        "male_weight": _base.Binding(
            path="RACE/9:DATA/payload/4:Male Weight",
            kind="primitive",
            name="Male Weight",
        ),
        "female_weight": _base.Binding(
            path="RACE/9:DATA/payload/5:Female Weight",
            kind="primitive",
            name="Female Weight",
        ),
        "flags": _base.Binding(
            path="RACE/9:DATA/payload/6:Flags",
            kind="primitive",
            name="Flags",
        ),
        "starting_health": _base.Binding(
            path="RACE/9:DATA/payload/7:Starting Health",
            kind="primitive",
            name="Starting Health",
        ),
        "starting_magicka": _base.Binding(
            path="RACE/9:DATA/payload/8:Starting Magicka",
            kind="primitive",
            name="Starting Magicka",
        ),
        "starting_stamina": _base.Binding(
            path="RACE/9:DATA/payload/9:Starting Stamina",
            kind="primitive",
            name="Starting Stamina",
        ),
        "base_carry_weight": _base.Binding(
            path="RACE/9:DATA/payload/10:Base Carry Weight",
            kind="primitive",
            name="Base Carry Weight",
        ),
        "base_mass": _base.Binding(
            path="RACE/9:DATA/payload/11:Base Mass",
            kind="primitive",
            name="Base Mass",
        ),
        "acceleration_rate": _base.Binding(
            path="RACE/9:DATA/payload/12:Acceleration rate",
            kind="primitive",
            name="Acceleration rate",
        ),
        "deceleration_rate": _base.Binding(
            path="RACE/9:DATA/payload/13:Deceleration rate",
            kind="primitive",
            name="Deceleration rate",
        ),
        "size": _base.Binding(
            path="RACE/9:DATA/payload/14:Size",
            kind="primitive",
            name="Size",
        ),
        "head_biped_object": _base.Binding(
            path="RACE/9:DATA/payload/15:Head Biped Object",
            kind="primitive",
            name="Head Biped Object",
        ),
        "hair_biped_object": _base.Binding(
            path="RACE/9:DATA/payload/16:Hair Biped Object",
            kind="primitive",
            name="Hair Biped Object",
        ),
        "injured_health_pct": _base.Binding(
            path="RACE/9:DATA/payload/17:Injured Health Pct",
            kind="primitive",
            name="Injured Health Pct",
        ),
        "shield_biped_object": _base.Binding(
            path="RACE/9:DATA/payload/18:Shield Biped Object",
            kind="primitive",
            name="Shield Biped Object",
        ),
        "health_regen": _base.Binding(
            path="RACE/9:DATA/payload/19:Health Regen",
            kind="primitive",
            name="Health Regen",
        ),
        "magicka_regen": _base.Binding(
            path="RACE/9:DATA/payload/20:Magicka Regen",
            kind="primitive",
            name="Magicka Regen",
        ),
        "stamina_regen": _base.Binding(
            path="RACE/9:DATA/payload/21:Stamina Regen",
            kind="primitive",
            name="Stamina Regen",
        ),
        "unarmed_damage": _base.Binding(
            path="RACE/9:DATA/payload/22:Unarmed Damage",
            kind="primitive",
            name="Unarmed Damage",
        ),
        "unarmed_reach": _base.Binding(
            path="RACE/9:DATA/payload/23:Unarmed Reach",
            kind="primitive",
            name="Unarmed Reach",
        ),
        "body_biped_object": _base.Binding(
            path="RACE/9:DATA/payload/24:Body Biped Object",
            kind="primitive",
            name="Body Biped Object",
        ),
        "aim_angle_tolerance": _base.Binding(
            path="RACE/9:DATA/payload/25:Aim Angle Tolerance",
            kind="primitive",
            name="Aim Angle Tolerance",
        ),
        "flight_radius": _base.Binding(
            path="RACE/9:DATA/payload/26:Flight Radius",
            kind="primitive",
            name="Flight Radius",
        ),
        "angular_acceleration_rate": _base.Binding(
            path="RACE/9:DATA/payload/27:Angular Acceleration Rate",
            kind="primitive",
            name="Angular Acceleration Rate",
        ),
        "angular_tolerance": _base.Binding(
            path="RACE/9:DATA/payload/28:Angular Tolerance",
            kind="primitive",
            name="Angular Tolerance",
        ),
        "flags_2": _base.Binding(
            path="RACE/9:DATA/payload/29:Flags 2",
            kind="primitive",
            name="Flags 2",
        ),
        "mount_data": _base.Binding(
            path="RACE/9:DATA/payload/30:Mount Data",
            kind="struct",
            name="Mount Data",
        ),
    }

    skill_boosts: tuple[SkillBoost14083, ...]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    male_height: float
    """Value decoded from this schema node."""

    female_height: float
    """Value decoded from this schema node."""

    male_weight: float
    """Value decoded from this schema node."""

    female_weight: float
    """Value decoded from this schema node."""

    flags: Flags14091
    """Value decoded from this schema node."""

    starting_health: float
    """Value decoded from this schema node."""

    starting_magicka: float
    """Value decoded from this schema node."""

    starting_stamina: float
    """Value decoded from this schema node."""

    base_carry_weight: float
    """Value decoded from this schema node."""

    base_mass: float
    """Value decoded from this schema node."""

    acceleration_rate: float
    """Value decoded from this schema node."""

    deceleration_rate: float
    """Value decoded from this schema node."""

    size: Size14099
    """Value decoded from this schema node."""

    head_biped_object: HeadBipedObject14100
    """Value decoded from this schema node."""

    hair_biped_object: HairBipedObject14101
    """Value decoded from this schema node."""

    injured_health_pct: float
    """Value decoded from this schema node."""

    shield_biped_object: ShieldBipedObject14103
    """Value decoded from this schema node."""

    health_regen: float
    """Value decoded from this schema node."""

    magicka_regen: float
    """Value decoded from this schema node."""

    stamina_regen: float
    """Value decoded from this schema node."""

    unarmed_damage: float
    """Value decoded from this schema node."""

    unarmed_reach: float
    """Value decoded from this schema node."""

    body_biped_object: BodyBipedObject14109
    """Value decoded from this schema node."""

    aim_angle_tolerance: float
    """Value decoded from this schema node."""

    flight_radius: float
    """Value decoded from this schema node."""

    angular_acceleration_rate: float
    """Value decoded from this schema node."""

    angular_tolerance: float
    """Value decoded from this schema node."""

    flags_2: Optional[Flags214114] = None
    """Value decoded from this schema node."""

    mount_data: Optional[MountData14115] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["skill_boosts"]
    ) -> _base.FieldRef[tuple[SkillBoost14083, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["male_height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["female_height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["male_weight"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["female_weight"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags14091]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["starting_health"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["starting_magicka"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["starting_stamina"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_carry_weight"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["base_mass"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["acceleration_rate"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["deceleration_rate"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["size"]) -> _base.FieldRef[Size14099]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head_biped_object"]
    ) -> _base.FieldRef[HeadBipedObject14100]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hair_biped_object"]
    ) -> _base.FieldRef[HairBipedObject14101]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["injured_health_pct"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["shield_biped_object"]
    ) -> _base.FieldRef[ShieldBipedObject14103]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["health_regen"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["magicka_regen"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["stamina_regen"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unarmed_damage"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unarmed_reach"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["body_biped_object"]
    ) -> _base.FieldRef[BodyBipedObject14109]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["aim_angle_tolerance"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flight_radius"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["angular_acceleration_rate"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["angular_tolerance"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags_2"]
    ) -> _base.FieldRef[Optional[Flags214114]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["mount_data"]
    ) -> _base.FieldRef[Optional[MountData14115]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14131(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/12:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/0:Structure"
                "/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14133": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/0:Structure"
                "/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14134": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/0:Structure"
                "/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14135": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/0:Structure"
                "/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_14133: bytes
    """Value decoded from this schema node."""

    unused_14134: bytes
    """Value decoded from this schema node."""

    unused_14135: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14133"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14134"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14135"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14131: _base.Variant = _base.Variant(
    path=("RACE/12:Model Information/payload/variants/0:Structure")
)


class Structure14136(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/12:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/1:Structure"
                "/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_14139": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/1:Structure"
                "/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14140": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/1:Structure"
                "/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_14139: bytes
    """Value decoded from this schema node."""

    unused_14140: bytes
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
    def field(self, name: Literal["unused_14139"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14140"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14136: _base.Variant = _base.Variant(
    path=("RACE/12:Model Information/payload/variants/1:Structure")
)


class Texture14144(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/12:Model Information/payload/variants/2:Structure"
        "/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/2:Structure"
                "/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/2:Structure"
                "/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/2:Structure"
                "/1:Textures/element/2:Folder Hash"
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


class Structure14141(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/12:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/2:Structure"
                "/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/2:Structure"
                "/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_14148": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/2:Structure"
                "/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14149": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/2:Structure"
                "/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture14144, ...]
    """Value decoded from this schema node."""

    unused_14148: bytes
    """Value decoded from this schema node."""

    unused_14149: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture14144, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14148"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14149"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14141: _base.Variant = _base.Variant(
    path=("RACE/12:Model Information/payload/variants/2:Structure")
)


class Texture14154(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/12:Model Information/payload/variants/3:Structure"
        "/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/1:Textures/element/2:Folder Hash"
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


class Material14161(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/12:Model Information/payload/variants/3:Structure"
        "/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/3:Materials/element/2:Folder Hash"
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


class Structure14150(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/12:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/12:Model Information/payload/variants/3:Structure"
                "/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture14154, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material14161, ...]
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
    ) -> _base.FieldRef[tuple[Texture14154, ...]]:
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
    ) -> _base.FieldRef[tuple[Material14161, ...]]:
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


_VARIANT_14150: _base.Variant = _base.Variant(
    path=("RACE/12:Model Information/payload/variants/3:Structure")
)


class Structure14172(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/15:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/0:Structure"
                "/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14174": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/0:Structure"
                "/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14175": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/0:Structure"
                "/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14176": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/0:Structure"
                "/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_14174: bytes
    """Value decoded from this schema node."""

    unused_14175: bytes
    """Value decoded from this schema node."""

    unused_14176: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14174"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14175"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14176"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14172: _base.Variant = _base.Variant(
    path=("RACE/15:Model Information/payload/variants/0:Structure")
)


class Structure14177(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/15:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/1:Structure"
                "/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_14180": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/1:Structure"
                "/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14181": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/1:Structure"
                "/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_14180: bytes
    """Value decoded from this schema node."""

    unused_14181: bytes
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
    def field(self, name: Literal["unused_14180"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14181"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14177: _base.Variant = _base.Variant(
    path=("RACE/15:Model Information/payload/variants/1:Structure")
)


class Texture14185(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/15:Model Information/payload/variants/2:Structure"
        "/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/2:Structure"
                "/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/2:Structure"
                "/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/2:Structure"
                "/1:Textures/element/2:Folder Hash"
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


class Structure14182(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/15:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/2:Structure"
                "/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/2:Structure"
                "/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_14189": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/2:Structure"
                "/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14190": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/2:Structure"
                "/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture14185, ...]
    """Value decoded from this schema node."""

    unused_14189: bytes
    """Value decoded from this schema node."""

    unused_14190: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture14185, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14189"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14190"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14182: _base.Variant = _base.Variant(
    path=("RACE/15:Model Information/payload/variants/2:Structure")
)


class Texture14195(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/15:Model Information/payload/variants/3:Structure"
        "/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/1:Textures/element/2:Folder Hash"
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


class Material14202(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/15:Model Information/payload/variants/3:Structure"
        "/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/3:Materials/element/2:Folder Hash"
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


class Structure14191(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/15:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/15:Model Information/payload/variants/3:Structure"
                "/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture14195, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material14202, ...]
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
    ) -> _base.FieldRef[tuple[Texture14195, ...]]:
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
    ) -> _base.FieldRef[tuple[Material14202, ...]]:
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


_VARIANT_14191: _base.Variant = _base.Variant(
    path=("RACE/15:Model Information/payload/variants/3:Structure")
)


class AttackFlags14236(enum.IntFlag):
    """Named values from the pinned schema."""

    IGNORE_WEAPON = 1
    BASH_ATTACK = 2
    POWER_ATTACK = 4
    LEFT_ATTACK = 8
    ROTATING_ATTACK = 16
    UNKNOWN_5 = 32
    UNKNOWN_6 = 64
    UNKNOWN_7 = 128
    UNKNOWN_8 = 256
    UNKNOWN_9 = 512
    UNKNOWN_10 = 1024
    UNKNOWN_11 = 2048
    UNKNOWN_12 = 4096
    UNKNOWN_13 = 8192
    UNKNOWN_14 = 16384
    UNKNOWN_15 = 32768
    UNKNOWN_16 = 65536
    UNKNOWN_17 = 131072
    UNKNOWN_18 = 262144
    UNKNOWN_19 = 524288
    UNKNOWN_20 = 1048576
    UNKNOWN_21 = 2097152
    UNKNOWN_22 = 4194304
    UNKNOWN_23 = 8388608
    UNKNOWN_24 = 16777216
    UNKNOWN_25 = 33554432
    UNKNOWN_26 = 67108864
    UNKNOWN_27 = 134217728
    UNKNOWN_28 = 268435456
    UNKNOWN_29 = 536870912
    UNKNOWN_30 = 1073741824
    OVERRIDE_DATA = 2147483648


class Structure14232(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "damage_mult": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "0:Damage Mult"
            ),
            kind="primitive",
            name="Damage Mult",
        ),
        "attack_chance": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "1:Attack Chance"
            ),
            kind="primitive",
            name="Attack Chance",
        ),
        "attack_spell": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "2:Attack Spell"
            ),
            kind="primitive",
            name="Attack Spell",
        ),
        "attack_flags": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "3:Attack Flags"
            ),
            kind="primitive",
            name="Attack Flags",
        ),
        "attack_angle": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "4:Attack Angle"
            ),
            kind="primitive",
            name="Attack Angle",
        ),
        "strike_angle": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "5:Strike Angle"
            ),
            kind="primitive",
            name="Strike Angle",
        ),
        "stagger": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "6:Stagger"
            ),
            kind="primitive",
            name="Stagger",
        ),
        "attack_type": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "7:Attack Type"
            ),
            kind="primitive",
            name="Attack Type",
        ),
        "knockdown": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "8:Knockdown"
            ),
            kind="primitive",
            name="Knockdown",
        ),
        "recovery_time": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "9:Recovery Time"
            ),
            kind="primitive",
            name="Recovery Time",
        ),
        "stamina_mult": _base.Binding(
            path=(
                "RACE/25:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "10:Stamina Mult"
            ),
            kind="primitive",
            name="Stamina Mult",
        ),
    }

    damage_mult: float
    """Value decoded from this schema node."""

    attack_chance: float
    """Value decoded from this schema node."""

    attack_spell: _values.FormId
    """Value decoded from this schema node."""

    attack_flags: AttackFlags14236
    """Value decoded from this schema node."""

    attack_angle: float
    """Value decoded from this schema node."""

    strike_angle: float
    """Value decoded from this schema node."""

    stagger: float
    """Value decoded from this schema node."""

    attack_type: _values.FormId
    """Value decoded from this schema node."""

    knockdown: float
    """Value decoded from this schema node."""

    recovery_time: float
    """Value decoded from this schema node."""

    stamina_mult: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["damage_mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["attack_chance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_spell"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_flags"]
    ) -> _base.FieldRef[AttackFlags14236]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["attack_angle"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["strike_angle"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["stagger"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_type"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["knockdown"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["recovery_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["stamina_mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Attack14230(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/25:Attacks/repeat/0:Attack"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "attack_data": _base.Binding(
            path="RACE/25:Attacks/repeat/0:Attack/0:Attack Data",
            kind="subrecord",
            name="Attack Data",
        ),
        "attack_event": _base.Binding(
            path="RACE/25:Attacks/repeat/0:Attack/1:Attack Event",
            kind="subrecord",
            name="Attack Event",
        ),
    }

    attack_data: Optional[Structure14232] = None
    """Value decoded from this schema node."""

    attack_event: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["attack_data"]
    ) -> _base.FieldRef[Optional[Structure14232]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_event"]
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


class BodyTexture14255(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    BODY_TEXTURE = 0


class Structure14261(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/0:Stru"
        "cture"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/0:Stru"
                "cture/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14263": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/0:Stru"
                "cture/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14264": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/0:Stru"
                "cture/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14265": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/0:Stru"
                "cture/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_14263: bytes
    """Value decoded from this schema node."""

    unused_14264: bytes
    """Value decoded from this schema node."""

    unused_14265: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14263"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14264"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14265"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14261: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/0:Stru"
        "cture"
    )
)


class Structure14266(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/1:Stru"
        "cture"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/1:Stru"
                "cture/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/1:Stru"
                "cture/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_14269": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/1:Stru"
                "cture/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14270": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/1:Stru"
                "cture/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_14269: bytes
    """Value decoded from this schema node."""

    unused_14270: bytes
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
    def field(self, name: Literal["unused_14269"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14270"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14266: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/1:Stru"
        "cture"
    )
)


class Texture14274(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/2:Stru"
        "cture/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/2:Stru"
                "cture/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/2:Stru"
                "cture/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/2:Stru"
                "cture/1:Textures/element/2:Folder Hash"
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


class Structure14271(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/2:Stru"
        "cture"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/2:Stru"
                "cture/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/2:Stru"
                "cture/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_14278": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/2:Stru"
                "cture/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14279": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/2:Stru"
                "cture/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture14274, ...]
    """Value decoded from this schema node."""

    unused_14278: bytes
    """Value decoded from this schema node."""

    unused_14279: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture14274, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14278"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14279"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14271: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/2:Stru"
        "cture"
    )
)


class Texture14284(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/3:Stru"
        "cture/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/1:Textures/element/2:Folder Hash"
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


class Material14291(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/3:Stru"
        "cture/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/3:Materials/element/2:Folder Hash"
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


class Structure14280(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/3:Stru"
        "cture"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information/payload/variants/3:Stru"
                "cture/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture14284, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material14291, ...]
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
    ) -> _base.FieldRef[tuple[Texture14284, ...]]:
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
    ) -> _base.FieldRef[tuple[Material14291, ...]]:
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


_VARIANT_14280: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/1:Model Information/payload/variants/3:Stru"
        "cture"
    )
)


class AlternateTexture14298(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
        "rt/1:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/2:Alternate Textures/payload/element/0:3D N"
                "ame"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/2:Alternate Textures/payload/element/1:New "
                "Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/2:Alternate Textures/payload/element/2:3D I"
                "ndex"
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


class Model14256(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Part/1:Model"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/0:Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/1:Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model/2:Alternate Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure14261, _VARIANT_14261]
        | Annotated[Structure14266, _VARIANT_14266]
        | Annotated[Structure14271, _VARIANT_14271]
        | Annotated[Structure14280, _VARIANT_14280]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture14298, ...]] = None
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
            Annotated[Structure14261, _VARIANT_14261]
            | Annotated[Structure14266, _VARIANT_14266]
            | Annotated[Structure14271, _VARIANT_14271]
            | Annotated[Structure14280, _VARIANT_14280]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture14298, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Part14253(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Part"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "index": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/0:Index"
            ),
            kind="subrecord",
            name="Index",
        ),
        "model": _base.Binding(
            path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Pa"
                "rt/1:Model"
            ),
            kind="unordered",
            name="Model",
        ),
    }

    index: Optional[BodyTexture14255] = None
    """Value decoded from this schema node."""

    model: Optional[Model14256] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[Optional[BodyTexture14255]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model14256]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class MaleBodyData14249(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/26:Body Data/1:Male Body Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "male_data_marker": _base.Binding(
            path=("RACE/26:Body Data/1:Male Body Data/0:Male Data Marker"),
            kind="subrecord",
            name="Male Data Marker",
        ),
        "parts": _base.Binding(
            path="RACE/26:Body Data/1:Male Body Data/1:Parts",
            kind="repeat",
            name="Parts",
            repeated_path=(
                "RACE/26:Body Data/1:Male Body Data/1:Parts/repeat/0:Part"
            ),
            child_kind="sequence",
        ),
    }

    male_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    parts: tuple[Part14253, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["male_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parts"]
    ) -> _base.FieldRef[tuple[Part14253, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BodyTexture14308(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    BODY_TEXTURE = 0


class Structure14314(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/0:St"
        "ructure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14316": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14317": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14318": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_14316: bytes
    """Value decoded from this schema node."""

    unused_14317: bytes
    """Value decoded from this schema node."""

    unused_14318: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14316"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14317"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14318"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14314: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/0:St"
        "ructure"
    )
)


class Structure14319(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/1:St"
        "ructure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_14322": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14323": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/1:St"
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

    unused_14322: bytes
    """Value decoded from this schema node."""

    unused_14323: bytes
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
    def field(self, name: Literal["unused_14322"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14323"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14319: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/1:St"
        "ructure"
    )
)


class Texture14327(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/2:St"
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


class Structure14324(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/2:St"
        "ructure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_14331": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14332": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture14327, ...]
    """Value decoded from this schema node."""

    unused_14331: bytes
    """Value decoded from this schema node."""

    unused_14332: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture14327, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14331"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14332"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14324: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/2:St"
        "ructure"
    )
)


class Texture14337(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
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


class Material14344(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
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


class Structure14333(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/3:St"
        "ructure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information/payload/variants/3:St"
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

    textures: tuple[Texture14337, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material14344, ...]
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
    ) -> _base.FieldRef[tuple[Texture14337, ...]]:
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
    ) -> _base.FieldRef[tuple[Material14344, ...]]:
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


_VARIANT_14333: _base.Variant = _base.Variant(
    path=(
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/1:Model Information/payload/variants/3:St"
        "ructure"
    )
)


class AlternateTexture14351(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
        "Part/1:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/2:Alternate Textures/payload/element/0:3D"
                " Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/2:Alternate Textures/payload/element/2:3D"
                " Index"
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


class Model14309(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:Part/1:Model"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/0:Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/1:Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model/2:Alternate Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure14314, _VARIANT_14314]
        | Annotated[Structure14319, _VARIANT_14319]
        | Annotated[Structure14324, _VARIANT_14324]
        | Annotated[Structure14333, _VARIANT_14333]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture14351, ...]] = None
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
            Annotated[Structure14314, _VARIANT_14314]
            | Annotated[Structure14319, _VARIANT_14319]
            | Annotated[Structure14324, _VARIANT_14324]
            | Annotated[Structure14333, _VARIANT_14333]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture14351, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Part14306(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:Part"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "index": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/0:Index"
            ),
            kind="subrecord",
            name="Index",
        ),
        "model": _base.Binding(
            path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:"
                "Part/1:Model"
            ),
            kind="unordered",
            name="Model",
        ),
    }

    index: Optional[BodyTexture14308] = None
    """Value decoded from this schema node."""

    model: Optional[Model14309] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[Optional[BodyTexture14308]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model14309]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FemaleBodyData14302(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/26:Body Data/2:Female Body Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "female_data_marker": _base.Binding(
            path=("RACE/26:Body Data/2:Female Body Data/0:Female Data Marker"),
            kind="subrecord",
            name="Female Data Marker",
        ),
        "parts": _base.Binding(
            path="RACE/26:Body Data/2:Female Body Data/1:Parts",
            kind="repeat",
            name="Parts",
            repeated_path=(
                "RACE/26:Body Data/2:Female Body Data/1:Parts/repeat/0:Part"
            ),
            child_kind="sequence",
        ),
    }

    female_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    parts: tuple[Part14306, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["female_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parts"]
    ) -> _base.FieldRef[tuple[Part14306, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BodyData14246(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/26:Body Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "body_data_marker": _base.Binding(
            path="RACE/26:Body Data/0:Body Data Marker",
            kind="subrecord",
            name="Body Data Marker",
        ),
        "male_body_data": _base.Binding(
            path="RACE/26:Body Data/1:Male Body Data",
            kind="sequence",
            name="Male Body Data",
        ),
        "female_body_data": _base.Binding(
            path="RACE/26:Body Data/2:Female Body Data",
            kind="sequence",
            name="Female Body Data",
        ),
    }

    body_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    male_body_data: Optional[MaleBodyData14249] = None
    """Value decoded from this schema node."""

    female_body_data: Optional[FemaleBodyData14302] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["body_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_body_data"]
    ) -> _base.FieldRef[Optional[MaleBodyData14249]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_body_data"]
    ) -> _base.FieldRef[Optional[FemaleBodyData14302]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14375(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14377": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14378": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14379": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_14377: bytes
    """Value decoded from this schema node."""

    unused_14378: bytes
    """Value decoded from this schema node."""

    unused_14379: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14377"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14378"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14379"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14375: _base.Variant = _base.Variant(
    path=(
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/0:Structure"
    )
)


class Structure14380(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_14383": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14384": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_14383: bytes
    """Value decoded from this schema node."""

    unused_14384: bytes
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
    def field(self, name: Literal["unused_14383"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14384"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14380: _base.Variant = _base.Variant(
    path=(
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/1:Structure"
    )
)


class Texture14388(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/2:Structure/1:Textures/element/0:Fi"
                "le Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/2:Structure/1:Textures/element/1:Ex"
                "tension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/2:Structure/1:Textures/element/2:Fo"
                "lder Hash"
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


class Structure14385(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_14392": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14393": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture14388, ...]
    """Value decoded from this schema node."""

    unused_14392: bytes
    """Value decoded from this schema node."""

    unused_14393: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture14388, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14392"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14393"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14385: _base.Variant = _base.Variant(
    path=(
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/2:Structure"
    )
)


class Texture14398(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/1:Textures/element/0:Fi"
                "le Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/1:Textures/element/1:Ex"
                "tension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/1:Textures/element/2:Fo"
                "lder Hash"
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


class Material14405(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/3:Materials/element/0:F"
                "ile Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/3:Materials/element/1:E"
                "xtension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/3:Materials/element/2:F"
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


class Structure14394(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
                "n/payload/variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture14398, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material14405, ...]
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
    ) -> _base.FieldRef[tuple[Texture14398, ...]]:
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
    ) -> _base.FieldRef[tuple[Material14405, ...]]:
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


_VARIANT_14394: _base.Variant = _base.Variant(
    path=(
        "RACE/32:Male Behavior Graph/1:Model/1:Model Informatio"
        "n/payload/variants/3:Structure"
    )
)


class AlternateTexture14412(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/32:Male Behavior Graph/1:Model/2:Alternate Textur"
        "es/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/2:Alternate Textur"
                "es/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/2:Alternate Textur"
                "es/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "RACE/32:Male Behavior Graph/1:Model/2:Alternate Textur"
                "es/payload/element/2:3D Index"
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


class Model14370(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/32:Male Behavior Graph/1:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=("RACE/32:Male Behavior Graph/1:Model/0:Model FileName"),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=("RACE/32:Male Behavior Graph/1:Model/1:Model Information"),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=("RACE/32:Male Behavior Graph/1:Model/2:Alternate Textures"),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure14375, _VARIANT_14375]
        | Annotated[Structure14380, _VARIANT_14380]
        | Annotated[Structure14385, _VARIANT_14385]
        | Annotated[Structure14394, _VARIANT_14394]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture14412, ...]] = None
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
            Annotated[Structure14375, _VARIANT_14375]
            | Annotated[Structure14380, _VARIANT_14380]
            | Annotated[Structure14385, _VARIANT_14385]
            | Annotated[Structure14394, _VARIANT_14394]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture14412, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class MaleBehaviorGraph14367(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/32:Male Behavior Graph"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "male_data_marker": _base.Binding(
            path="RACE/32:Male Behavior Graph/0:Male Data Marker",
            kind="subrecord",
            name="Male Data Marker",
        ),
        "model": _base.Binding(
            path="RACE/32:Male Behavior Graph/1:Model",
            kind="unordered",
            name="Model",
        ),
    }

    male_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    model: Optional[Model14370] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["male_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model14370]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14424(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14426": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14427": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14428": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_14426: bytes
    """Value decoded from this schema node."""

    unused_14427: bytes
    """Value decoded from this schema node."""

    unused_14428: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14426"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14427"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14428"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14424: _base.Variant = _base.Variant(
    path=(
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/0:Structure"
    )
)


class Structure14429(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_14432": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14433": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_14432: bytes
    """Value decoded from this schema node."""

    unused_14433: bytes
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
    def field(self, name: Literal["unused_14432"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14433"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14429: _base.Variant = _base.Variant(
    path=(
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/1:Structure"
    )
)


class Texture14437(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/2:Structure/1:Textures/element/0:"
                "File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/2:Structure/1:Textures/element/1:"
                "Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/2:Structure/1:Textures/element/2:"
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


class Structure14434(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_14441": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_14442": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture14437, ...]
    """Value decoded from this schema node."""

    unused_14441: bytes
    """Value decoded from this schema node."""

    unused_14442: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture14437, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14441"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_14442"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_14434: _base.Variant = _base.Variant(
    path=(
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/2:Structure"
    )
)


class Texture14447(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/1:Textures/element/0:"
                "File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/1:Textures/element/1:"
                "Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/1:Textures/element/2:"
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


class Material14454(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/3:Materials/element/0"
                ":File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/3:Materials/element/1"
                ":Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/3:Materials/element/2"
                ":Folder Hash"
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


class Structure14443(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
                "ion/payload/variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture14447, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material14454, ...]
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
    ) -> _base.FieldRef[tuple[Texture14447, ...]]:
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
    ) -> _base.FieldRef[tuple[Material14454, ...]]:
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


_VARIANT_14443: _base.Variant = _base.Variant(
    path=(
        "RACE/33:Female Behavior Graph/1:Model/1:Model Informat"
        "ion/payload/variants/3:Structure"
    )
)


class AlternateTexture14461(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/33:Female Behavior Graph/1:Model/2:Alternate Text"
        "ures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/2:Alternate Text"
                "ures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/2:Alternate Text"
                "ures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "RACE/33:Female Behavior Graph/1:Model/2:Alternate Text"
                "ures/payload/element/2:3D Index"
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


class Model14419(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/33:Female Behavior Graph/1:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=("RACE/33:Female Behavior Graph/1:Model/0:Model FileName"),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=("RACE/33:Female Behavior Graph/1:Model/1:Model Information"),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=("RACE/33:Female Behavior Graph/1:Model/2:Alternate Textures"),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure14424, _VARIANT_14424]
        | Annotated[Structure14429, _VARIANT_14429]
        | Annotated[Structure14434, _VARIANT_14434]
        | Annotated[Structure14443, _VARIANT_14443]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture14461, ...]] = None
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
            Annotated[Structure14424, _VARIANT_14424]
            | Annotated[Structure14429, _VARIANT_14429]
            | Annotated[Structure14434, _VARIANT_14434]
            | Annotated[Structure14443, _VARIANT_14443]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture14461, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FemaleBehaviorGraph14416(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/33:Female Behavior Graph"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "female_data_marker": _base.Binding(
            path=("RACE/33:Female Behavior Graph/0:Female Data Marker"),
            kind="subrecord",
            name="Female Data Marker",
        ),
        "model": _base.Binding(
            path="RACE/33:Female Behavior Graph/1:Model",
            kind="unordered",
            name="Model",
        ),
    }

    female_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    model: Optional[Model14419] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["female_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model14419]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14483(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
        "ide Values/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "left_walk": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/0:Left - Walk"
            ),
            kind="primitive",
            name="Left - Walk",
        ),
        "left_run": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/1:Left - Run"
            ),
            kind="primitive",
            name="Left - Run",
        ),
        "right_walk": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/2:Right - Walk"
            ),
            kind="primitive",
            name="Right - Walk",
        ),
        "right_run": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/3:Right - Run"
            ),
            kind="primitive",
            name="Right - Run",
        ),
        "forward_walk": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/4:Forward - Walk"
            ),
            kind="primitive",
            name="Forward - Walk",
        ),
        "forward_run": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/5:Forward - Run"
            ),
            kind="primitive",
            name="Forward - Run",
        ),
        "back_walk": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/6:Back - Walk"
            ),
            kind="primitive",
            name="Back - Walk",
        ),
        "back_run": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/7:Back - Run"
            ),
            kind="primitive",
            name="Back - Run",
        ),
        "rotate_walk": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/8:Rotate - Walk"
            ),
            kind="primitive",
            name="Rotate - Walk",
        ),
        "rotate_walk_14493": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/9:Rotate - Walk"
            ),
            kind="primitive",
            name="Rotate - Walk",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values/payload/10:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    left_walk: float
    """Value decoded from this schema node."""

    left_run: float
    """Value decoded from this schema node."""

    right_walk: float
    """Value decoded from this schema node."""

    right_run: float
    """Value decoded from this schema node."""

    forward_walk: float
    """Value decoded from this schema node."""

    forward_run: float
    """Value decoded from this schema node."""

    back_walk: float
    """Value decoded from this schema node."""

    back_run: float
    """Value decoded from this schema node."""

    rotate_walk: float
    """Value decoded from this schema node."""

    rotate_walk_14493: float
    """Value decoded from this schema node."""

    unknown: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["left_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["left_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["right_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["right_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["forward_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["forward_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["back_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["back_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotate_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotate_walk_14493"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class MovementTypes14479(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/40:Movement Types/repeat/0:Movement Types"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "movement_type": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/0:Movement Type"
            ),
            kind="subrecord",
            name="Movement Type",
        ),
        "override_values": _base.Binding(
            path=(
                "RACE/40:Movement Types/repeat/0:Movement Types/1:Overr"
                "ide Values"
            ),
            kind="subrecord",
            name="Override Values",
        ),
    }

    movement_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    override_values: Optional[Structure14483] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["movement_type"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["override_values"]
    ) -> _base.FieldRef[Optional[Structure14483]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class HandToHandMeleeOneHandSwordOneHandDaAea5D13714496(enum.IntFlag):
    """Named values from the pinned schema."""

    HAND_TO_HAND_MELEE = 1
    ONE_HAND_SWORD = 2
    ONE_HAND_DAGGER = 4
    ONE_HAND_AXE = 8
    ONE_HAND_MACE = 16
    TWO_HAND_SWORD = 32
    TWO_HAND_AXE = 64
    BOW = 128
    STAFF = 256
    SPELL = 512
    SHIELD = 1024
    TORCH = 2048
    CROSSBOW = 4096


class Structure14508(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Iy14506(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/0:IY"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/0:IY/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14508] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14508]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14527(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ih14525(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/1:IH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/1:IH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14527] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14527]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14546(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Eh14544(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/2:EH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/2:EH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14546] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14546]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14565(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ey14563(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/3:EY"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/3:EY/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14565] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14565]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14584(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ae14582(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/4:AE"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/4:AE/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14584] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14584]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14603(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Aa14601(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/5:AA"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/5:AA/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14603] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14603]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14622(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Aw14620(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/6:AW"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/6:AW/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14622] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14622]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14641(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ay14639(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/7:AY"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/7:AY/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14641] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14641]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14660(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ah14658(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/8:AH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/8:AH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14660] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14660]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14679(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ao14677(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/9:AO"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/9:AO/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14679] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14679]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14698(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Oy14696(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/10:OY"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/10:OY/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14698] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14698]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14717(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ow14715(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/11:OW"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/11:OW/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14717] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14717]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14736(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Uh14734(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/12:UH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/12:UH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14736] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14736]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14755(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Uw14753(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/13:UW"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/13:UW/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14755] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14755]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14774(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Er14772(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/14:ER"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/14:ER/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14774] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14774]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14793(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ax14791(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/15:AX"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/15:AX/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14793] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14793]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14812(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class S14810(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/16:S"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/16:S/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14812] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14812]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14831(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sh14829(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/17:SH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/17:SH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14831] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14831]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14850(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Z14848(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/18:Z"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/18:Z/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14850] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14850]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14869(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Zh14867(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/19:ZH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/19:ZH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14869] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14869]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14888(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class F14886(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/20:F"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/20:F/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14888] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14888]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14907(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Th14905(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/21:TH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/21:TH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14907] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14907]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14926(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class V14924(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/22:V"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/22:V/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14926] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14926]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14945(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Dh14943(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/23:DH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/23:DH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14945] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14945]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14964(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class M14962(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/24:M"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/24:M/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14964] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14964]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure14983(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class N14981(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/25:N"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/25:N/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure14983] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure14983]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15002(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ng15000(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/26:NG"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/26:NG/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15002] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15002]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15021(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LValue15019(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/27:L"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/27:L/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15021] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15021]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15040(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class R15038(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/28:R"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/28:R/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15040] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15040]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15059(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class W15057(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/29:W"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/29:W/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15059] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15059]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15078(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Y15076(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/30:Y"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/30:Y/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15078] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15078]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15097(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Hh15095(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/31:HH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/31:HH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15097] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15097]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15116(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class B15114(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/32:B"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/32:B/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15116] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15116]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15135(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class D15133(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/33:D"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/33:D/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15135] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15135]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15154(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Jh15152(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/34:JH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/34:JH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15154] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15154]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15173(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class G15171(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/35:G"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/35:G/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15173] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15173]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15192(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class P15190(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/36:P"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/36:P/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15192] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15192]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15211(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class T15209(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/37:T"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/37:T/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15211] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15211]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15230(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight/p"
                "ayload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class K15228(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/38:K"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/38:K/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15230] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15230]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15249(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight/"
                "payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ch15247(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/39:CH"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/39:CH/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15249] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15249]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15268(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"
                "/payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Sil15266(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/40:SIL"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/40:SIL/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15268] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15268]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15287(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target We"
                "ight/payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Shotsil15285(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/41:SHOTSIL"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/41:SHOTSIL/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15287] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15287]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15306(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weight/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aah_lip_big_aah": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/0:Aah / LipBigAah"
            ),
            kind="primitive",
            name="Aah / LipBigAah",
        ),
        "big_aah_lip_dst": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/1:BigAah / LipDST"
            ),
            kind="primitive",
            name="BigAah / LipDST",
        ),
        "bmp_lip_eee": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/2:BMP / LipEee"
            ),
            kind="primitive",
            name="BMP / LipEee",
        ),
        "ch_jsh_lip_fv": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/3:ChJsh / LipFV"
            ),
            kind="primitive",
            name="ChJsh / LipFV",
        ),
        "dst_lip_k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/4:DST / LipK"
            ),
            kind="primitive",
            name="DST / LipK",
        ),
        "eee_lip_l": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/5:Eee / LipL"
            ),
            kind="primitive",
            name="Eee / LipL",
        ),
        "eh_lip_r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/6:Eh / LipR"
            ),
            kind="primitive",
            name="Eh / LipR",
        ),
        "fv_lip_th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/7:FV / LipTh"
            ),
            kind="primitive",
            name="FV / LipTh",
        ),
        "i": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/8:I"
            ),
            kind="primitive",
            name="I",
        ),
        "k": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/9:K"
            ),
            kind="primitive",
            name="K",
        ),
        "n": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/10:N"
            ),
            kind="primitive",
            name="N",
        ),
        "oh": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/11:Oh"
            ),
            kind="primitive",
            name="Oh",
        ),
        "ooh_q": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/12:OohQ"
            ),
            kind="primitive",
            name="OohQ",
        ),
        "r": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/13:R"
            ),
            kind="primitive",
            name="R",
        ),
        "th": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/14:TH"
            ),
            kind="primitive",
            name="TH",
        ),
        "w": _base.Binding(
            path=(
                "RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weigh"
                "t/payload/15:W"
            ),
            kind="primitive",
            name="W",
        ),
    }

    aah_lip_big_aah: float
    """Value decoded from this schema node."""

    big_aah_lip_dst: float
    """Value decoded from this schema node."""

    bmp_lip_eee: float
    """Value decoded from this schema node."""

    ch_jsh_lip_fv: float
    """Value decoded from this schema node."""

    dst_lip_k: float
    """Value decoded from this schema node."""

    eee_lip_l: float
    """Value decoded from this schema node."""

    eh_lip_r: float
    """Value decoded from this schema node."""

    fv_lip_th: float
    """Value decoded from this schema node."""

    i: Optional[float] = None
    """Value decoded from this schema node."""

    k: Optional[float] = None
    """Value decoded from this schema node."""

    n: Optional[float] = None
    """Value decoded from this schema node."""

    oh: Optional[float] = None
    """Value decoded from this schema node."""

    ooh_q: Optional[float] = None
    """Value decoded from this schema node."""

    r: Optional[float] = None
    """Value decoded from this schema node."""

    th: Optional[float] = None
    """Value decoded from this schema node."""

    w: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["aah_lip_big_aah"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["big_aah_lip_dst"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bmp_lip_eee"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch_jsh_lip_fv"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dst_lip_k"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eee_lip_l"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh_lip_r"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fv_lip_th"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["i"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oh"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ooh_q"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flap15304(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes/42:FLAP"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phoneme_target_weight": _base.Binding(
            path=("RACE/45:FaceFX Phonemes/42:FLAP/0:Phoneme Target Weight"),
            kind="subrecord",
            name="Phoneme Target Weight",
        ),
    }

    phoneme_target_weight: Optional[Structure15306] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phoneme_target_weight"]
    ) -> _base.FieldRef[Optional[Structure15306]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FaceFxPhonemes14505(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/45:FaceFX Phonemes"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "iy": _base.Binding(
            path="RACE/45:FaceFX Phonemes/0:IY",
            kind="sequence",
            name="IY",
        ),
        "ih": _base.Binding(
            path="RACE/45:FaceFX Phonemes/1:IH",
            kind="sequence",
            name="IH",
        ),
        "eh": _base.Binding(
            path="RACE/45:FaceFX Phonemes/2:EH",
            kind="sequence",
            name="EH",
        ),
        "ey": _base.Binding(
            path="RACE/45:FaceFX Phonemes/3:EY",
            kind="sequence",
            name="EY",
        ),
        "ae": _base.Binding(
            path="RACE/45:FaceFX Phonemes/4:AE",
            kind="sequence",
            name="AE",
        ),
        "aa": _base.Binding(
            path="RACE/45:FaceFX Phonemes/5:AA",
            kind="sequence",
            name="AA",
        ),
        "aw": _base.Binding(
            path="RACE/45:FaceFX Phonemes/6:AW",
            kind="sequence",
            name="AW",
        ),
        "ay": _base.Binding(
            path="RACE/45:FaceFX Phonemes/7:AY",
            kind="sequence",
            name="AY",
        ),
        "ah": _base.Binding(
            path="RACE/45:FaceFX Phonemes/8:AH",
            kind="sequence",
            name="AH",
        ),
        "ao": _base.Binding(
            path="RACE/45:FaceFX Phonemes/9:AO",
            kind="sequence",
            name="AO",
        ),
        "oy": _base.Binding(
            path="RACE/45:FaceFX Phonemes/10:OY",
            kind="sequence",
            name="OY",
        ),
        "ow": _base.Binding(
            path="RACE/45:FaceFX Phonemes/11:OW",
            kind="sequence",
            name="OW",
        ),
        "uh": _base.Binding(
            path="RACE/45:FaceFX Phonemes/12:UH",
            kind="sequence",
            name="UH",
        ),
        "uw": _base.Binding(
            path="RACE/45:FaceFX Phonemes/13:UW",
            kind="sequence",
            name="UW",
        ),
        "er": _base.Binding(
            path="RACE/45:FaceFX Phonemes/14:ER",
            kind="sequence",
            name="ER",
        ),
        "ax": _base.Binding(
            path="RACE/45:FaceFX Phonemes/15:AX",
            kind="sequence",
            name="AX",
        ),
        "s": _base.Binding(
            path="RACE/45:FaceFX Phonemes/16:S",
            kind="sequence",
            name="S",
        ),
        "sh": _base.Binding(
            path="RACE/45:FaceFX Phonemes/17:SH",
            kind="sequence",
            name="SH",
        ),
        "z": _base.Binding(
            path="RACE/45:FaceFX Phonemes/18:Z",
            kind="sequence",
            name="Z",
        ),
        "zh": _base.Binding(
            path="RACE/45:FaceFX Phonemes/19:ZH",
            kind="sequence",
            name="ZH",
        ),
        "f": _base.Binding(
            path="RACE/45:FaceFX Phonemes/20:F",
            kind="sequence",
            name="F",
        ),
        "th": _base.Binding(
            path="RACE/45:FaceFX Phonemes/21:TH",
            kind="sequence",
            name="TH",
        ),
        "v": _base.Binding(
            path="RACE/45:FaceFX Phonemes/22:V",
            kind="sequence",
            name="V",
        ),
        "dh": _base.Binding(
            path="RACE/45:FaceFX Phonemes/23:DH",
            kind="sequence",
            name="DH",
        ),
        "m": _base.Binding(
            path="RACE/45:FaceFX Phonemes/24:M",
            kind="sequence",
            name="M",
        ),
        "n": _base.Binding(
            path="RACE/45:FaceFX Phonemes/25:N",
            kind="sequence",
            name="N",
        ),
        "ng": _base.Binding(
            path="RACE/45:FaceFX Phonemes/26:NG",
            kind="sequence",
            name="NG",
        ),
        "l_value": _base.Binding(
            path="RACE/45:FaceFX Phonemes/27:L",
            kind="sequence",
            name="L",
        ),
        "r": _base.Binding(
            path="RACE/45:FaceFX Phonemes/28:R",
            kind="sequence",
            name="R",
        ),
        "w": _base.Binding(
            path="RACE/45:FaceFX Phonemes/29:W",
            kind="sequence",
            name="W",
        ),
        "y": _base.Binding(
            path="RACE/45:FaceFX Phonemes/30:Y",
            kind="sequence",
            name="Y",
        ),
        "hh": _base.Binding(
            path="RACE/45:FaceFX Phonemes/31:HH",
            kind="sequence",
            name="HH",
        ),
        "b": _base.Binding(
            path="RACE/45:FaceFX Phonemes/32:B",
            kind="sequence",
            name="B",
        ),
        "d": _base.Binding(
            path="RACE/45:FaceFX Phonemes/33:D",
            kind="sequence",
            name="D",
        ),
        "jh": _base.Binding(
            path="RACE/45:FaceFX Phonemes/34:JH",
            kind="sequence",
            name="JH",
        ),
        "g": _base.Binding(
            path="RACE/45:FaceFX Phonemes/35:G",
            kind="sequence",
            name="G",
        ),
        "p": _base.Binding(
            path="RACE/45:FaceFX Phonemes/36:P",
            kind="sequence",
            name="P",
        ),
        "t": _base.Binding(
            path="RACE/45:FaceFX Phonemes/37:T",
            kind="sequence",
            name="T",
        ),
        "k": _base.Binding(
            path="RACE/45:FaceFX Phonemes/38:K",
            kind="sequence",
            name="K",
        ),
        "ch": _base.Binding(
            path="RACE/45:FaceFX Phonemes/39:CH",
            kind="sequence",
            name="CH",
        ),
        "sil": _base.Binding(
            path="RACE/45:FaceFX Phonemes/40:SIL",
            kind="sequence",
            name="SIL",
        ),
        "shotsil": _base.Binding(
            path="RACE/45:FaceFX Phonemes/41:SHOTSIL",
            kind="sequence",
            name="SHOTSIL",
        ),
        "flap": _base.Binding(
            path="RACE/45:FaceFX Phonemes/42:FLAP",
            kind="sequence",
            name="FLAP",
        ),
    }

    iy: Optional[Iy14506] = None
    """Value decoded from this schema node."""

    ih: Optional[Ih14525] = None
    """Value decoded from this schema node."""

    eh: Optional[Eh14544] = None
    """Value decoded from this schema node."""

    ey: Optional[Ey14563] = None
    """Value decoded from this schema node."""

    ae: Optional[Ae14582] = None
    """Value decoded from this schema node."""

    aa: Optional[Aa14601] = None
    """Value decoded from this schema node."""

    aw: Optional[Aw14620] = None
    """Value decoded from this schema node."""

    ay: Optional[Ay14639] = None
    """Value decoded from this schema node."""

    ah: Optional[Ah14658] = None
    """Value decoded from this schema node."""

    ao: Optional[Ao14677] = None
    """Value decoded from this schema node."""

    oy: Optional[Oy14696] = None
    """Value decoded from this schema node."""

    ow: Optional[Ow14715] = None
    """Value decoded from this schema node."""

    uh: Optional[Uh14734] = None
    """Value decoded from this schema node."""

    uw: Optional[Uw14753] = None
    """Value decoded from this schema node."""

    er: Optional[Er14772] = None
    """Value decoded from this schema node."""

    ax: Optional[Ax14791] = None
    """Value decoded from this schema node."""

    s: Optional[S14810] = None
    """Value decoded from this schema node."""

    sh: Optional[Sh14829] = None
    """Value decoded from this schema node."""

    z: Optional[Z14848] = None
    """Value decoded from this schema node."""

    zh: Optional[Zh14867] = None
    """Value decoded from this schema node."""

    f: Optional[F14886] = None
    """Value decoded from this schema node."""

    th: Optional[Th14905] = None
    """Value decoded from this schema node."""

    v: Optional[V14924] = None
    """Value decoded from this schema node."""

    dh: Optional[Dh14943] = None
    """Value decoded from this schema node."""

    m: Optional[M14962] = None
    """Value decoded from this schema node."""

    n: Optional[N14981] = None
    """Value decoded from this schema node."""

    ng: Optional[Ng15000] = None
    """Value decoded from this schema node."""

    l_value: Optional[LValue15019] = None
    """Value decoded from this schema node."""

    r: Optional[R15038] = None
    """Value decoded from this schema node."""

    w: Optional[W15057] = None
    """Value decoded from this schema node."""

    y: Optional[Y15076] = None
    """Value decoded from this schema node."""

    hh: Optional[Hh15095] = None
    """Value decoded from this schema node."""

    b: Optional[B15114] = None
    """Value decoded from this schema node."""

    d: Optional[D15133] = None
    """Value decoded from this schema node."""

    jh: Optional[Jh15152] = None
    """Value decoded from this schema node."""

    g: Optional[G15171] = None
    """Value decoded from this schema node."""

    p: Optional[P15190] = None
    """Value decoded from this schema node."""

    t: Optional[T15209] = None
    """Value decoded from this schema node."""

    k: Optional[K15228] = None
    """Value decoded from this schema node."""

    ch: Optional[Ch15247] = None
    """Value decoded from this schema node."""

    sil: Optional[Sil15266] = None
    """Value decoded from this schema node."""

    shotsil: Optional[Shotsil15285] = None
    """Value decoded from this schema node."""

    flap: Optional[Flap15304] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["iy"]) -> _base.FieldRef[Optional[Iy14506]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ih"]) -> _base.FieldRef[Optional[Ih14525]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eh"]) -> _base.FieldRef[Optional[Eh14544]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ey"]) -> _base.FieldRef[Optional[Ey14563]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ae"]) -> _base.FieldRef[Optional[Ae14582]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["aa"]) -> _base.FieldRef[Optional[Aa14601]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["aw"]) -> _base.FieldRef[Optional[Aw14620]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ay"]) -> _base.FieldRef[Optional[Ay14639]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ah"]) -> _base.FieldRef[Optional[Ah14658]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ao"]) -> _base.FieldRef[Optional[Ao14677]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["oy"]) -> _base.FieldRef[Optional[Oy14696]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ow"]) -> _base.FieldRef[Optional[Ow14715]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["uh"]) -> _base.FieldRef[Optional[Uh14734]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["uw"]) -> _base.FieldRef[Optional[Uw14753]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["er"]) -> _base.FieldRef[Optional[Er14772]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ax"]) -> _base.FieldRef[Optional[Ax14791]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["s"]) -> _base.FieldRef[Optional[S14810]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sh"]) -> _base.FieldRef[Optional[Sh14829]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["z"]) -> _base.FieldRef[Optional[Z14848]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["zh"]) -> _base.FieldRef[Optional[Zh14867]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["f"]) -> _base.FieldRef[Optional[F14886]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["th"]) -> _base.FieldRef[Optional[Th14905]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["v"]) -> _base.FieldRef[Optional[V14924]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dh"]) -> _base.FieldRef[Optional[Dh14943]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["m"]) -> _base.FieldRef[Optional[M14962]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["n"]) -> _base.FieldRef[Optional[N14981]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ng"]) -> _base.FieldRef[Optional[Ng15000]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["l_value"]
    ) -> _base.FieldRef[Optional[LValue15019]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["r"]) -> _base.FieldRef[Optional[R15038]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["w"]) -> _base.FieldRef[Optional[W15057]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[Optional[Y15076]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["hh"]) -> _base.FieldRef[Optional[Hh15095]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["b"]) -> _base.FieldRef[Optional[B15114]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["d"]) -> _base.FieldRef[Optional[D15133]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["jh"]) -> _base.FieldRef[Optional[Jh15152]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["g"]) -> _base.FieldRef[Optional[G15171]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["p"]) -> _base.FieldRef[Optional[P15190]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["t"]) -> _base.FieldRef[Optional[T15209]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["k"]) -> _base.FieldRef[Optional[K15228]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ch"]) -> _base.FieldRef[Optional[Ch15247]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sil"]) -> _base.FieldRef[Optional[Sil15266]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["shotsil"]
    ) -> _base.FieldRef[Optional[Shotsil15285]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flap"]
    ) -> _base.FieldRef[Optional[Flap15304]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class HeadPart15342(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/1:Head Parts/repeat/0:Head Part"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "head_part_number": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/1:Head Parts/repeat"
                "/0:Head Part/0:Head Part Number"
            ),
            kind="subrecord",
            name="Head Part Number",
        ),
        "head": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/1:Head Parts/repeat"
                "/0:Head Part/1:Head"
            ),
            kind="subrecord",
            name="Head",
        ),
    }

    head_part_number: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    head: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["head_part_number"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head"]
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


class NoseMorphFlags15352(enum.IntFlag):
    """Named values from the pinned schema."""

    NOSE_TYPE0 = 1
    NOSE_TYPE1 = 2
    NOSE_TYPE2 = 4
    NOSE_TYPE3 = 8
    NOSE_TYPE4 = 16
    NOSE_TYPE5 = 32
    NOSE_TYPE6 = 64
    NOSE_TYPE7 = 128
    NOSE_TYPE8 = 256
    NOSE_TYPE9 = 512
    NOSE_TYPE10 = 1024
    NOSE_TYPE11 = 2048
    NOSE_TYPE12 = 4096
    NOSE_TYPE13 = 8192
    NOSE_TYPE14 = 16384
    NOSE_TYPE15 = 32768
    NOSE_TYPE16 = 65536
    NOSE_TYPE17 = 131072
    NOSE_TYPE18 = 262144
    NOSE_TYPE19 = 524288
    NOSE_TYPE20 = 1048576
    NOSE_TYPE21 = 2097152
    NOSE_TYPE22 = 4194304
    NOSE_TYPE23 = 8388608
    NOSE_TYPE24 = 16777216
    NOSE_TYPE25 = 33554432
    NOSE_TYPE26 = 67108864
    NOSE_TYPE27 = 134217728
    NOSE_TYPE28 = 268435456
    NOSE_TYPE29 = 536870912
    NOSE_TYPE30 = 1073741824
    NOSE_TYPE31 = 2147483648


class Structure15351(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
        "1:Nose Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "nose_morph_flags": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/0:Nose Morph Flags"
            ),
            kind="primitive",
            name="Nose Morph Flags",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15354": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15355": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15356": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15357": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15358": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15359": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    nose_morph_flags: NoseMorphFlags15352
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15354: bytes
    """Value decoded from this schema node."""

    unknown_15355: bytes
    """Value decoded from this schema node."""

    unknown_15356: bytes
    """Value decoded from this schema node."""

    unknown_15357: bytes
    """Value decoded from this schema node."""

    unknown_15358: bytes
    """Value decoded from this schema node."""

    unknown_15359: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["nose_morph_flags"]
    ) -> _base.FieldRef[NoseMorphFlags15352]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15354"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15355"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15356"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15357"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15358"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15359"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BrowMorphFlags15364(enum.IntFlag):
    """Named values from the pinned schema."""

    BROW_TYPE0 = 1
    BROW_TYPE1 = 2
    BROW_TYPE2 = 4
    BROW_TYPE3 = 8
    BROW_TYPE4 = 16
    BROW_TYPE5 = 32
    BROW_TYPE6 = 64
    BROW_TYPE7 = 128
    BROW_TYPE8 = 256
    BROW_TYPE9 = 512
    BROW_TYPE10 = 1024
    BROW_TYPE11 = 2048
    BROW_TYPE12 = 4096
    BROW_TYPE13 = 8192
    BROW_TYPE14 = 16384
    BROW_TYPE15 = 32768
    BROW_TYPE16 = 65536
    BROW_TYPE17 = 131072
    BROW_TYPE18 = 262144
    BROW_TYPE19 = 524288
    BROW_TYPE20 = 1048576


class Structure15363(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
        "3:Brow Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "brow_morph_flags": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/0:Brow Morph Flags"
            ),
            kind="primitive",
            name="Brow Morph Flags",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15366": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15367": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15368": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15369": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15370": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15371": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    brow_morph_flags: BrowMorphFlags15364
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15366: bytes
    """Value decoded from this schema node."""

    unknown_15367: bytes
    """Value decoded from this schema node."""

    unknown_15368: bytes
    """Value decoded from this schema node."""

    unknown_15369: bytes
    """Value decoded from this schema node."""

    unknown_15370: bytes
    """Value decoded from this schema node."""

    unknown_15371: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["brow_morph_flags"]
    ) -> _base.FieldRef[BrowMorphFlags15364]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15366"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15367"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15368"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15369"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15370"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15371"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class EyeMorphFlags115376(enum.IntFlag):
    """Named values from the pinned schema."""

    EYES_TYPE0 = 1
    EYES_TYPE1 = 2
    EYES_TYPE2 = 4
    EYES_TYPE3 = 8
    EYES_TYPE4 = 16
    EYES_TYPE5 = 32
    EYES_TYPE6 = 64
    EYES_TYPE7 = 128
    EYES_TYPE8 = 256
    EYES_TYPE9 = 512
    EYES_TYPE10 = 1024
    EYES_TYPE11 = 2048
    EYES_TYPE12 = 4096
    EYES_TYPE13 = 8192
    EYES_TYPE14 = 16384
    EYES_TYPE15 = 32768
    EYES_TYPE16 = 65536
    EYES_TYPE17 = 131072
    EYES_TYPE18 = 262144
    EYES_TYPE19 = 524288
    EYES_TYPE20 = 1048576
    EYES_TYPE21 = 2097152
    EYES_TYPE22 = 4194304
    EYES_TYPE23 = 8388608
    EYES_TYPE24 = 16777216
    EYES_TYPE25 = 33554432
    EYES_TYPE26 = 67108864
    EYES_TYPE27 = 134217728
    EYES_TYPE28 = 268435456
    EYES_TYPE29 = 536870912
    EYES_TYPE30 = 1073741824
    EYES_TYPE31 = 2147483648


class EyeMorphFlags215377(enum.IntFlag):
    """Named values from the pinned schema."""

    EYES_TYPE32 = 1
    EYES_TYPE33 = 2
    EYES_TYPE34 = 4
    EYES_TYPE35 = 8
    EYES_TYPE36 = 16
    EYES_TYPE37 = 32
    EYES_TYPE38 = 64


class Structure15375(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
        "5:Eye Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "eye_morph_flags_1": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/0:Eye Morph Flags 1"
            ),
            kind="primitive",
            name="Eye Morph Flags 1",
        ),
        "eye_morph_flags_2": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/1:Eye Morph Flags 2"
            ),
            kind="primitive",
            name="Eye Morph Flags 2",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15379": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15380": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15381": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15382": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15383": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15384": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants/payload/8:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    eye_morph_flags_1: EyeMorphFlags115376
    """Value decoded from this schema node."""

    eye_morph_flags_2: EyeMorphFlags215377
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15379: bytes
    """Value decoded from this schema node."""

    unknown_15380: bytes
    """Value decoded from this schema node."""

    unknown_15381: bytes
    """Value decoded from this schema node."""

    unknown_15382: bytes
    """Value decoded from this schema node."""

    unknown_15383: bytes
    """Value decoded from this schema node."""

    unknown_15384: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["eye_morph_flags_1"]
    ) -> _base.FieldRef[EyeMorphFlags115376]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eye_morph_flags_2"]
    ) -> _base.FieldRef[EyeMorphFlags215377]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15379"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15380"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15381"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15382"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15383"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15384"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LipMorphFlags15389(enum.IntFlag):
    """Named values from the pinned schema."""

    LIP_TYPE0 = 1
    LIP_TYPE1 = 2
    LIP_TYPE2 = 4
    LIP_TYPE3 = 8
    LIP_TYPE4 = 16
    LIP_TYPE5 = 32
    LIP_TYPE6 = 64
    LIP_TYPE7 = 128
    LIP_TYPE8 = 256
    LIP_TYPE9 = 512
    LIP_TYPE10 = 1024
    LIP_TYPE11 = 2048
    LIP_TYPE12 = 4096
    LIP_TYPE13 = 8192
    LIP_TYPE14 = 16384
    LIP_TYPE15 = 32768
    LIP_TYPE16 = 65536
    LIP_TYPE17 = 131072
    LIP_TYPE18 = 262144
    LIP_TYPE19 = 524288
    LIP_TYPE20 = 1048576
    LIP_TYPE21 = 2097152
    LIP_TYPE22 = 4194304
    LIP_TYPE23 = 8388608
    LIP_TYPE24 = 16777216
    LIP_TYPE25 = 33554432
    LIP_TYPE26 = 67108864
    LIP_TYPE27 = 134217728
    LIP_TYPE28 = 268435456
    LIP_TYPE29 = 536870912
    LIP_TYPE30 = 1073741824
    LIP_TYPE31 = 2147483648


class Structure15388(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
        "7:Lip Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "lip_morph_flags": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/0:Lip Morph Flags"
            ),
            kind="primitive",
            name="Lip Morph Flags",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15391": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15392": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15393": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15394": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15395": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15396": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    lip_morph_flags: LipMorphFlags15389
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15391: bytes
    """Value decoded from this schema node."""

    unknown_15392: bytes
    """Value decoded from this schema node."""

    unknown_15393: bytes
    """Value decoded from this schema node."""

    unknown_15394: bytes
    """Value decoded from this schema node."""

    unknown_15395: bytes
    """Value decoded from this schema node."""

    unknown_15396: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["lip_morph_flags"]
    ) -> _base.FieldRef[LipMorphFlags15389]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15391"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15392"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15393"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15394"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15395"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15396"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class AvailableMorphs15347(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/2:Available Morphs"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "0:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "nose_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "1:Nose Variants"
            ),
            kind="subrecord",
            name="Nose Variants",
        ),
        "unknown_15360": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "2:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "brow_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "3:Brow Variants"
            ),
            kind="subrecord",
            name="Brow Variants",
        ),
        "unknown_15372": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "4:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "eye_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "5:Eye Variants"
            ),
            kind="subrecord",
            name="Eye Variants",
        ),
        "unknown_15385": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "6:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "lip_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/2:Available Morphs/"
                "7:Lip Variants"
            ),
            kind="subrecord",
            name="Lip Variants",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    nose_variants: Optional[Structure15351] = None
    """Value decoded from this schema node."""

    unknown_15360: Optional[bytes] = None
    """Value decoded from this schema node."""

    brow_variants: Optional[Structure15363] = None
    """Value decoded from this schema node."""

    unknown_15372: Optional[bytes] = None
    """Value decoded from this schema node."""

    eye_variants: Optional[Structure15375] = None
    """Value decoded from this schema node."""

    unknown_15385: Optional[bytes] = None
    """Value decoded from this schema node."""

    lip_variants: Optional[Structure15388] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["nose_variants"]
    ) -> _base.FieldRef[Optional[Structure15351]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_15360"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["brow_variants"]
    ) -> _base.FieldRef[Optional[Structure15363]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_15372"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eye_variants"]
    ) -> _base.FieldRef[Optional[Structure15375]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_15385"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lip_variants"]
    ) -> _base.FieldRef[Optional[Structure15388]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class NoneLipColorCheekColorEyelinerEyeSocke744D4Ec615417(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    LIP_COLOR = 1
    CHEEK_COLOR = 2
    EYELINER = 3
    EYE_SOCKET_UPPER = 4
    EYE_SOCKET_LOWER = 5
    SKIN_TONE = 6
    PAINT = 7
    LAUGH_LINES = 8
    CHEEK_COLOR_LOWER = 9
    NOSE = 10
    CHIN = 11
    NECK = 12
    FOREHEAD = 13
    DIRT = 14
    UNKNOWN_16 = 15


class Texture15411(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
        "/0:Tint Assets/0:Tint Layer/repeat/0:Texture"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "index": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/0:Tint Layer/repeat/0:Texture/0:Index"
            ),
            kind="subrecord",
            name="Index",
        ),
        "file_name": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/0:Tint Layer/repeat/0:Texture/1:File Na"
                "me"
            ),
            kind="subrecord",
            name="File Name",
        ),
        "mask_type": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/0:Tint Layer/repeat/0:Texture/2:Mask Ty"
                "pe"
            ),
            kind="subrecord",
            name="Mask Type",
        ),
        "preset_default": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/0:Tint Layer/repeat/0:Texture/3:Preset "
                "Default"
            ),
            kind="subrecord",
            name="Preset Default",
        ),
    }

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    file_name: Optional[str] = None
    """Value decoded from this schema node."""

    mask_type: Optional[NoneLipColorCheekColorEyelinerEyeSocke744D4Ec615417] = (
        None
    )
    """Value decoded from this schema node."""

    preset_default: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["mask_type"]
    ) -> _base.FieldRef[
        Optional[NoneLipColorCheekColorEyelinerEyeSocke744D4Ec615417]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["preset_default"]
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


class Preset15421(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
        "/0:Tint Assets/1:Presets/repeat/0:Preset"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "color": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/1:Presets/repeat/0:Preset/0:Color"
            ),
            kind="subrecord",
            name="Color",
        ),
        "default_value": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/1:Presets/repeat/0:Preset/1:Default Val"
                "ue"
            ),
            kind="subrecord",
            name="Default Value",
        ),
        "index": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/1:Presets/repeat/0:Preset/2:Index"
            ),
            kind="subrecord",
            name="Index",
        ),
    }

    color: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    default_value: Optional[float] = None
    """Value decoded from this schema node."""

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["color"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_value"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
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


class TintAssets15409(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat/0:Tint Assets"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "tint_layer": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/0:Tint Layer"
            ),
            kind="repeat",
            name="Tint Layer",
            repeated_path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/0:Tint Layer/repeat/0:Texture"
            ),
            child_kind="sequence",
        ),
        "presets": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/1:Presets"
            ),
            kind="repeat",
            name="Presets",
            repeated_path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets/1:Presets/repeat/0:Preset"
            ),
            child_kind="sequence",
        ),
    }

    tint_layer: tuple[Texture15411, ...] = ()
    """Value decoded from this schema node."""

    presets: tuple[Preset15421, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["tint_layer"]
    ) -> _base.FieldRef[tuple[Texture15411, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["presets"]
    ) -> _base.FieldRef[tuple[Preset15421, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15433(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15435": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15436": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15437": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_15435: bytes
    """Value decoded from this schema node."""

    unused_15436: bytes
    """Value decoded from this schema node."""

    unused_15437: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15435"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15436"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15437"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_15433: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/0:Structure"
    )
)


class Structure15438(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_15441": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15442": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_15441: bytes
    """Value decoded from this schema node."""

    unused_15442: bytes
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
    def field(self, name: Literal["unused_15441"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15442"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_15438: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/1:Structure"
    )
)


class Texture15446(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/2:Structure/1:Textures/eleme"
        "nt"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/2:Structure/1:Textures/eleme"
                "nt/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/2:Structure/1:Textures/eleme"
                "nt/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/2:Structure/1:Textures/eleme"
                "nt/2:Folder Hash"
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


class Structure15443(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_15450": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15451": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture15446, ...]
    """Value decoded from this schema node."""

    unused_15450: bytes
    """Value decoded from this schema node."""

    unused_15451: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture15446, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15450"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15451"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_15443: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/2:Structure"
    )
)


class Texture15456(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/3:Structure/1:Textures/eleme"
        "nt"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/1:Textures/eleme"
                "nt/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/1:Textures/eleme"
                "nt/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/1:Textures/eleme"
                "nt/2:Folder Hash"
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


class Material15463(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/3:Structure/3:Materials/elem"
        "ent"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/3:Materials/elem"
                "ent/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/3:Materials/elem"
                "ent/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/3:Materials/elem"
                "ent/2:Folder Hash"
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


class Structure15452(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
                "ormation/payload/variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture15456, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material15463, ...]
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
    ) -> _base.FieldRef[tuple[Texture15456, ...]]:
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
    ) -> _base.FieldRef[tuple[Material15463, ...]]:
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


_VARIANT_15452: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Inf"
        "ormation/payload/variants/3:Structure"
    )
)


class AlternateTexture15470(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/1:Male Head Data/8:Model/2:Alternate"
        " Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/2:Alternate"
                " Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/2:Alternate"
                " Textures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/2:Alternate"
                " Textures/payload/element/2:3D Index"
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


class Model15428(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/52:Head Data/1:Male Head Data/8:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/0:Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/1:Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/8:Model/2:Alternate"
                " Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure15433, _VARIANT_15433]
        | Annotated[Structure15438, _VARIANT_15438]
        | Annotated[Structure15443, _VARIANT_15443]
        | Annotated[Structure15452, _VARIANT_15452]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture15470, ...]] = None
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
            Annotated[Structure15433, _VARIANT_15433]
            | Annotated[Structure15438, _VARIANT_15438]
            | Annotated[Structure15443, _VARIANT_15443]
            | Annotated[Structure15452, _VARIANT_15452]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture15470, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class MaleHeadData15338(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/52:Head Data/1:Male Head Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "male_data_marker": _base.Binding(
            path=("RACE/52:Head Data/1:Male Head Data/0:Male Data Marker"),
            kind="subrecord",
            name="Male Data Marker",
        ),
        "head_parts": _base.Binding(
            path="RACE/52:Head Data/1:Male Head Data/1:Head Parts",
            kind="repeat",
            name="Head Parts",
            repeated_path=(
                "RACE/52:Head Data/1:Male Head Data/1:Head Parts/repeat"
                "/0:Head Part"
            ),
            child_kind="sequence",
        ),
        "available_morphs": _base.Binding(
            path=("RACE/52:Head Data/1:Male Head Data/2:Available Morphs"),
            kind="sequence",
            name="Available Morphs",
        ),
        "race_presets_male": _base.Binding(
            path=("RACE/52:Head Data/1:Male Head Data/3:Race Presets Male"),
            kind="repeat",
            name="Race Presets Male",
            repeated_path=(
                "RACE/52:Head Data/1:Male Head Data/3:Race Presets Male"
                "/repeat/0:Preset NPC"
            ),
            child_kind="subrecord",
        ),
        "available_hair_colors_male": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/4:Available Hair Co"
                "lors Male"
            ),
            kind="repeat",
            name="Available Hair Colors Male",
            repeated_path=(
                "RACE/52:Head Data/1:Male Head Data/4:Available Hair Co"
                "lors Male/repeat/0:Hair Color"
            ),
            child_kind="subrecord",
        ),
        "face_details_texture_set_list_male": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/5:Face Details Text"
                "ure Set List Male"
            ),
            kind="repeat",
            name="Face Details Texture Set List Male",
            repeated_path=(
                "RACE/52:Head Data/1:Male Head Data/5:Face Details Text"
                "ure Set List Male/repeat/0:Texture Set"
            ),
            child_kind="subrecord",
        ),
        "default_face_texture_male": _base.Binding(
            path=(
                "RACE/52:Head Data/1:Male Head Data/6:Default Face Texture Male"
            ),
            kind="subrecord",
            name="Default Face Texture Male",
        ),
        "tint_masks": _base.Binding(
            path="RACE/52:Head Data/1:Male Head Data/7:Tint Masks",
            kind="repeat",
            name="Tint Masks",
            repeated_path=(
                "RACE/52:Head Data/1:Male Head Data/7:Tint Masks/repeat"
                "/0:Tint Assets"
            ),
            child_kind="sequence",
        ),
        "model": _base.Binding(
            path="RACE/52:Head Data/1:Male Head Data/8:Model",
            kind="unordered",
            name="Model",
        ),
    }

    male_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    head_parts: tuple[HeadPart15342, ...] = ()
    """Value decoded from this schema node."""

    available_morphs: Optional[AvailableMorphs15347] = None
    """Value decoded from this schema node."""

    race_presets_male: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    available_hair_colors_male: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    face_details_texture_set_list_male: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    default_face_texture_male: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    tint_masks: tuple[TintAssets15409, ...] = ()
    """Value decoded from this schema node."""

    model: Optional[Model15428] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["male_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head_parts"]
    ) -> _base.FieldRef[tuple[HeadPart15342, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["available_morphs"]
    ) -> _base.FieldRef[Optional[AvailableMorphs15347]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["race_presets_male"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["available_hair_colors_male"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["face_details_texture_set_list_male"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_face_texture_male"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tint_masks"]
    ) -> _base.FieldRef[tuple[TintAssets15409, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model15428]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class HeadPart15480(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/2:Head Parts/repeat/0:Head Part"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "head_part_number": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/2:Head Parts/repe"
                "at/0:Head Part/0:Head Part Number"
            ),
            kind="subrecord",
            name="Head Part Number",
        ),
        "head": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/2:Head Parts/repe"
                "at/0:Head Part/1:Head"
            ),
            kind="subrecord",
            name="Head",
        ),
    }

    head_part_number: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    head: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["head_part_number"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head"]
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


class NoseMorphFlags15490(enum.IntFlag):
    """Named values from the pinned schema."""

    NOSE_TYPE0 = 1
    NOSE_TYPE1 = 2
    NOSE_TYPE2 = 4
    NOSE_TYPE3 = 8
    NOSE_TYPE4 = 16
    NOSE_TYPE5 = 32
    NOSE_TYPE6 = 64
    NOSE_TYPE7 = 128
    NOSE_TYPE8 = 256
    NOSE_TYPE9 = 512
    NOSE_TYPE10 = 1024
    NOSE_TYPE11 = 2048
    NOSE_TYPE12 = 4096
    NOSE_TYPE13 = 8192
    NOSE_TYPE14 = 16384
    NOSE_TYPE15 = 32768
    NOSE_TYPE16 = 65536
    NOSE_TYPE17 = 131072
    NOSE_TYPE18 = 262144
    NOSE_TYPE19 = 524288
    NOSE_TYPE20 = 1048576
    NOSE_TYPE21 = 2097152
    NOSE_TYPE22 = 4194304
    NOSE_TYPE23 = 8388608
    NOSE_TYPE24 = 16777216
    NOSE_TYPE25 = 33554432
    NOSE_TYPE26 = 67108864
    NOSE_TYPE27 = 134217728
    NOSE_TYPE28 = 268435456
    NOSE_TYPE29 = 536870912
    NOSE_TYPE30 = 1073741824
    NOSE_TYPE31 = 2147483648


class Structure15489(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
        "s/1:Nose Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "nose_morph_flags": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/0:Nose Morph Flags"
            ),
            kind="primitive",
            name="Nose Morph Flags",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15492": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15493": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15494": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15495": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15496": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15497": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    nose_morph_flags: NoseMorphFlags15490
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15492: bytes
    """Value decoded from this schema node."""

    unknown_15493: bytes
    """Value decoded from this schema node."""

    unknown_15494: bytes
    """Value decoded from this schema node."""

    unknown_15495: bytes
    """Value decoded from this schema node."""

    unknown_15496: bytes
    """Value decoded from this schema node."""

    unknown_15497: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["nose_morph_flags"]
    ) -> _base.FieldRef[NoseMorphFlags15490]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15492"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15493"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15494"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15495"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15496"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15497"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BrowMorphFlags15502(enum.IntFlag):
    """Named values from the pinned schema."""

    BROW_TYPE0 = 1
    BROW_TYPE1 = 2
    BROW_TYPE2 = 4
    BROW_TYPE3 = 8
    BROW_TYPE4 = 16
    BROW_TYPE5 = 32
    BROW_TYPE6 = 64
    BROW_TYPE7 = 128
    BROW_TYPE8 = 256
    BROW_TYPE9 = 512
    BROW_TYPE10 = 1024
    BROW_TYPE11 = 2048
    BROW_TYPE12 = 4096
    BROW_TYPE13 = 8192
    BROW_TYPE14 = 16384
    BROW_TYPE15 = 32768
    BROW_TYPE16 = 65536
    BROW_TYPE17 = 131072
    BROW_TYPE18 = 262144
    BROW_TYPE19 = 524288
    BROW_TYPE20 = 1048576


class Structure15501(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
        "s/3:Brow Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "brow_morph_flags": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/0:Brow Morph Flags"
            ),
            kind="primitive",
            name="Brow Morph Flags",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15504": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15505": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15506": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15507": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15508": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15509": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    brow_morph_flags: BrowMorphFlags15502
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15504: bytes
    """Value decoded from this schema node."""

    unknown_15505: bytes
    """Value decoded from this schema node."""

    unknown_15506: bytes
    """Value decoded from this schema node."""

    unknown_15507: bytes
    """Value decoded from this schema node."""

    unknown_15508: bytes
    """Value decoded from this schema node."""

    unknown_15509: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["brow_morph_flags"]
    ) -> _base.FieldRef[BrowMorphFlags15502]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15504"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15505"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15506"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15507"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15508"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15509"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class EyeMorphFlags115514(enum.IntFlag):
    """Named values from the pinned schema."""

    EYES_TYPE0 = 1
    EYES_TYPE1 = 2
    EYES_TYPE2 = 4
    EYES_TYPE3 = 8
    EYES_TYPE4 = 16
    EYES_TYPE5 = 32
    EYES_TYPE6 = 64
    EYES_TYPE7 = 128
    EYES_TYPE8 = 256
    EYES_TYPE9 = 512
    EYES_TYPE10 = 1024
    EYES_TYPE11 = 2048
    EYES_TYPE12 = 4096
    EYES_TYPE13 = 8192
    EYES_TYPE14 = 16384
    EYES_TYPE15 = 32768
    EYES_TYPE16 = 65536
    EYES_TYPE17 = 131072
    EYES_TYPE18 = 262144
    EYES_TYPE19 = 524288
    EYES_TYPE20 = 1048576
    EYES_TYPE21 = 2097152
    EYES_TYPE22 = 4194304
    EYES_TYPE23 = 8388608
    EYES_TYPE24 = 16777216
    EYES_TYPE25 = 33554432
    EYES_TYPE26 = 67108864
    EYES_TYPE27 = 134217728
    EYES_TYPE28 = 268435456
    EYES_TYPE29 = 536870912
    EYES_TYPE30 = 1073741824
    EYES_TYPE31 = 2147483648


class EyeMorphFlags215515(enum.IntFlag):
    """Named values from the pinned schema."""

    EYES_TYPE32 = 1
    EYES_TYPE33 = 2
    EYES_TYPE34 = 4
    EYES_TYPE35 = 8
    EYES_TYPE36 = 16
    EYES_TYPE37 = 32
    EYES_TYPE38 = 64


class Structure15513(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
        "s/5:Eye Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "eye_morph_flags_1": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/0:Eye Morph Flags 1"
            ),
            kind="primitive",
            name="Eye Morph Flags 1",
        ),
        "eye_morph_flags_2": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/1:Eye Morph Flags 2"
            ),
            kind="primitive",
            name="Eye Morph Flags 2",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15517": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15518": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15519": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15520": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15521": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15522": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants/payload/8:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    eye_morph_flags_1: EyeMorphFlags115514
    """Value decoded from this schema node."""

    eye_morph_flags_2: EyeMorphFlags215515
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15517: bytes
    """Value decoded from this schema node."""

    unknown_15518: bytes
    """Value decoded from this schema node."""

    unknown_15519: bytes
    """Value decoded from this schema node."""

    unknown_15520: bytes
    """Value decoded from this schema node."""

    unknown_15521: bytes
    """Value decoded from this schema node."""

    unknown_15522: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["eye_morph_flags_1"]
    ) -> _base.FieldRef[EyeMorphFlags115514]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eye_morph_flags_2"]
    ) -> _base.FieldRef[EyeMorphFlags215515]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15517"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15518"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15519"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15520"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15521"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15522"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LipMorphFlags15527(enum.IntFlag):
    """Named values from the pinned schema."""

    LIP_TYPE0 = 1
    LIP_TYPE1 = 2
    LIP_TYPE2 = 4
    LIP_TYPE3 = 8
    LIP_TYPE4 = 16
    LIP_TYPE5 = 32
    LIP_TYPE6 = 64
    LIP_TYPE7 = 128
    LIP_TYPE8 = 256
    LIP_TYPE9 = 512
    LIP_TYPE10 = 1024
    LIP_TYPE11 = 2048
    LIP_TYPE12 = 4096
    LIP_TYPE13 = 8192
    LIP_TYPE14 = 16384
    LIP_TYPE15 = 32768
    LIP_TYPE16 = 65536
    LIP_TYPE17 = 131072
    LIP_TYPE18 = 262144
    LIP_TYPE19 = 524288
    LIP_TYPE20 = 1048576
    LIP_TYPE21 = 2097152
    LIP_TYPE22 = 4194304
    LIP_TYPE23 = 8388608
    LIP_TYPE24 = 16777216
    LIP_TYPE25 = 33554432
    LIP_TYPE26 = 67108864
    LIP_TYPE27 = 134217728
    LIP_TYPE28 = 268435456
    LIP_TYPE29 = 536870912
    LIP_TYPE30 = 1073741824
    LIP_TYPE31 = 2147483648


class Structure15526(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
        "s/7:Lip Variants/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "lip_morph_flags": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/0:Lip Morph Flags"
            ),
            kind="primitive",
            name="Lip Morph Flags",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15529": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15530": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15531": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15532": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15533": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/6:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_15534": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants/payload/7:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    lip_morph_flags: LipMorphFlags15527
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    unknown_15529: bytes
    """Value decoded from this schema node."""

    unknown_15530: bytes
    """Value decoded from this schema node."""

    unknown_15531: bytes
    """Value decoded from this schema node."""

    unknown_15532: bytes
    """Value decoded from this schema node."""

    unknown_15533: bytes
    """Value decoded from this schema node."""

    unknown_15534: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["lip_morph_flags"]
    ) -> _base.FieldRef[LipMorphFlags15527]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15529"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15530"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15531"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15532"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15533"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15534"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class AvailableMorphs15485(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/3:Available Morphs"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/0:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "nose_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/1:Nose Variants"
            ),
            kind="subrecord",
            name="Nose Variants",
        ),
        "unknown_15498": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/2:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "brow_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/3:Brow Variants"
            ),
            kind="subrecord",
            name="Brow Variants",
        ),
        "unknown_15510": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/4:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "eye_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/5:Eye Variants"
            ),
            kind="subrecord",
            name="Eye Variants",
        ),
        "unknown_15523": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/6:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "lip_variants": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/3:Available Morph"
                "s/7:Lip Variants"
            ),
            kind="subrecord",
            name="Lip Variants",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    nose_variants: Optional[Structure15489] = None
    """Value decoded from this schema node."""

    unknown_15498: Optional[bytes] = None
    """Value decoded from this schema node."""

    brow_variants: Optional[Structure15501] = None
    """Value decoded from this schema node."""

    unknown_15510: Optional[bytes] = None
    """Value decoded from this schema node."""

    eye_variants: Optional[Structure15513] = None
    """Value decoded from this schema node."""

    unknown_15523: Optional[bytes] = None
    """Value decoded from this schema node."""

    lip_variants: Optional[Structure15526] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["nose_variants"]
    ) -> _base.FieldRef[Optional[Structure15489]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_15498"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["brow_variants"]
    ) -> _base.FieldRef[Optional[Structure15501]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_15510"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eye_variants"]
    ) -> _base.FieldRef[Optional[Structure15513]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_15523"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lip_variants"]
    ) -> _base.FieldRef[Optional[Structure15526]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class NoneLipColorCheekColorEyelinerEyeSocke744D4Ec615555(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    LIP_COLOR = 1
    CHEEK_COLOR = 2
    EYELINER = 3
    EYE_SOCKET_UPPER = 4
    EYE_SOCKET_LOWER = 5
    SKIN_TONE = 6
    PAINT = 7
    LAUGH_LINES = 8
    CHEEK_COLOR_LOWER = 9
    NOSE = 10
    CHIN = 11
    NECK = 12
    FOREHEAD = 13
    DIRT = 14
    UNKNOWN_16 = 15


class Texture15549(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
        "at/0:Tint Assets/0:Tint Layer/repeat/0:Texture"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "index": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/0:Tint Layer/repeat/0:Texture/0:Index"
            ),
            kind="subrecord",
            name="Index",
        ),
        "file_name": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/0:Tint Layer/repeat/0:Texture/1:File "
                "Name"
            ),
            kind="subrecord",
            name="File Name",
        ),
        "mask_type": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/0:Tint Layer/repeat/0:Texture/2:Mask "
                "Type"
            ),
            kind="subrecord",
            name="Mask Type",
        ),
        "preset_default": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/0:Tint Layer/repeat/0:Texture/3:Prese"
                "t Default"
            ),
            kind="subrecord",
            name="Preset Default",
        ),
    }

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    file_name: Optional[str] = None
    """Value decoded from this schema node."""

    mask_type: Optional[NoneLipColorCheekColorEyelinerEyeSocke744D4Ec615555] = (
        None
    )
    """Value decoded from this schema node."""

    preset_default: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["mask_type"]
    ) -> _base.FieldRef[
        Optional[NoneLipColorCheekColorEyelinerEyeSocke744D4Ec615555]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["preset_default"]
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


class Preset15559(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
        "at/0:Tint Assets/1:Presets/repeat/0:Preset"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "color": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/1:Presets/repeat/0:Preset/0:Color"
            ),
            kind="subrecord",
            name="Color",
        ),
        "default_value": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/1:Presets/repeat/0:Preset/1:Default V"
                "alue"
            ),
            kind="subrecord",
            name="Default Value",
        ),
        "index": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/1:Presets/repeat/0:Preset/2:Index"
            ),
            kind="subrecord",
            name="Index",
        ),
    }

    color: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    default_value: Optional[float] = None
    """Value decoded from this schema node."""

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["color"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_value"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
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


class TintAssets15547(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repeat/0:Tint Assets"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "tint_layer": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/0:Tint Layer"
            ),
            kind="repeat",
            name="Tint Layer",
            repeated_path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/0:Tint Layer/repeat/0:Texture"
            ),
            child_kind="sequence",
        ),
        "presets": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/1:Presets"
            ),
            kind="repeat",
            name="Presets",
            repeated_path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets/1:Presets/repeat/0:Preset"
            ),
            child_kind="sequence",
        ),
    }

    tint_layer: tuple[Texture15549, ...] = ()
    """Value decoded from this schema node."""

    presets: tuple[Preset15559, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["tint_layer"]
    ) -> _base.FieldRef[tuple[Texture15549, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["presets"]
    ) -> _base.FieldRef[tuple[Preset15559, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15571(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15573": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15574": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15575": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_15573: bytes
    """Value decoded from this schema node."""

    unused_15574: bytes
    """Value decoded from this schema node."""

    unused_15575: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15573"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15574"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15575"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_15571: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/0:Structure"
    )
)


class Structure15576(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_15579": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15580": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_15579: bytes
    """Value decoded from this schema node."""

    unused_15580: bytes
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
    def field(self, name: Literal["unused_15579"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15580"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_15576: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/1:Structure"
    )
)


class Texture15584(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/2:Structure/1:Textures/ele"
        "ment"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/2:Structure/1:Textures/ele"
                "ment/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/2:Structure/1:Textures/ele"
                "ment/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/2:Structure/1:Textures/ele"
                "ment/2:Folder Hash"
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


class Structure15581(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_15588": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_15589": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture15584, ...]
    """Value decoded from this schema node."""

    unused_15588: bytes
    """Value decoded from this schema node."""

    unused_15589: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture15584, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15588"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_15589"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_15581: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/2:Structure"
    )
)


class Texture15594(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/3:Structure/1:Textures/ele"
        "ment"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/1:Textures/ele"
                "ment/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/1:Textures/ele"
                "ment/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/1:Textures/ele"
                "ment/2:Folder Hash"
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


class Material15601(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/3:Structure/3:Materials/el"
        "ement"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/3:Materials/el"
                "ement/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/3:Materials/el"
                "ement/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/3:Materials/el"
                "ement/2:Folder Hash"
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


class Structure15590(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation/payload/variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture15594, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material15601, ...]
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
    ) -> _base.FieldRef[tuple[Texture15594, ...]]:
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
    ) -> _base.FieldRef[tuple[Material15601, ...]]:
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


_VARIANT_15590: _base.Variant = _base.Variant(
    path=(
        "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
        "nformation/payload/variants/3:Structure"
    )
)


class AlternateTexture15608(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "RACE/52:Head Data/2:Female Head Data/9:Model/2:Alterna"
        "te Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/2:Alterna"
                "te Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/2:Alterna"
                "te Textures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/2:Alterna"
                "te Textures/payload/element/2:3D Index"
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


class Model15566(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/52:Head Data/2:Female Head Data/9:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/0:Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/1:Model I"
                "nformation"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/9:Model/2:Alterna"
                "te Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure15571, _VARIANT_15571]
        | Annotated[Structure15576, _VARIANT_15576]
        | Annotated[Structure15581, _VARIANT_15581]
        | Annotated[Structure15590, _VARIANT_15590]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture15608, ...]] = None
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
            Annotated[Structure15571, _VARIANT_15571]
            | Annotated[Structure15576, _VARIANT_15576]
            | Annotated[Structure15581, _VARIANT_15581]
            | Annotated[Structure15590, _VARIANT_15590]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture15608, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FemaleHeadData15474(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/52:Head Data/2:Female Head Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "head_data_marker": _base.Binding(
            path=("RACE/52:Head Data/2:Female Head Data/0:Head Data Marker"),
            kind="subrecord",
            name="Head Data Marker",
        ),
        "female_data_marker": _base.Binding(
            path=("RACE/52:Head Data/2:Female Head Data/1:Female Data Marker"),
            kind="subrecord",
            name="Female Data Marker",
        ),
        "head_parts": _base.Binding(
            path="RACE/52:Head Data/2:Female Head Data/2:Head Parts",
            kind="repeat",
            name="Head Parts",
            repeated_path=(
                "RACE/52:Head Data/2:Female Head Data/2:Head Parts/repe"
                "at/0:Head Part"
            ),
            child_kind="sequence",
        ),
        "available_morphs": _base.Binding(
            path=("RACE/52:Head Data/2:Female Head Data/3:Available Morphs"),
            kind="sequence",
            name="Available Morphs",
        ),
        "race_presets_female": _base.Binding(
            path=("RACE/52:Head Data/2:Female Head Data/4:Race Presets Female"),
            kind="repeat",
            name="Race Presets Female",
            repeated_path=(
                "RACE/52:Head Data/2:Female Head Data/4:Race Presets Fe"
                "male/repeat/0:Preset NPC"
            ),
            child_kind="subrecord",
        ),
        "available_hair_colors_female": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/5:Available Hair "
                "Colors Female"
            ),
            kind="repeat",
            name="Available Hair Colors Female",
            repeated_path=(
                "RACE/52:Head Data/2:Female Head Data/5:Available Hair "
                "Colors Female/repeat/0:Hair Color"
            ),
            child_kind="subrecord",
        ),
        "face_details_texture_set_list_female": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/6:Face Details Te"
                "xture Set List Female"
            ),
            kind="repeat",
            name="Face Details Texture Set List Female",
            repeated_path=(
                "RACE/52:Head Data/2:Female Head Data/6:Face Details Te"
                "xture Set List Female/repeat/0:Texture Set"
            ),
            child_kind="subrecord",
        ),
        "default_face_texture_female": _base.Binding(
            path=(
                "RACE/52:Head Data/2:Female Head Data/7:Default Face Te"
                "xture Female"
            ),
            kind="subrecord",
            name="Default Face Texture Female",
        ),
        "tint_masks": _base.Binding(
            path="RACE/52:Head Data/2:Female Head Data/8:Tint Masks",
            kind="repeat",
            name="Tint Masks",
            repeated_path=(
                "RACE/52:Head Data/2:Female Head Data/8:Tint Masks/repe"
                "at/0:Tint Assets"
            ),
            child_kind="sequence",
        ),
        "model": _base.Binding(
            path="RACE/52:Head Data/2:Female Head Data/9:Model",
            kind="unordered",
            name="Model",
        ),
    }

    head_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    female_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    head_parts: tuple[HeadPart15480, ...] = ()
    """Value decoded from this schema node."""

    available_morphs: Optional[AvailableMorphs15485] = None
    """Value decoded from this schema node."""

    race_presets_female: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    available_hair_colors_female: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    face_details_texture_set_list_female: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    default_face_texture_female: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    tint_masks: tuple[TintAssets15547, ...] = ()
    """Value decoded from this schema node."""

    model: Optional[Model15566] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["head_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head_parts"]
    ) -> _base.FieldRef[tuple[HeadPart15480, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["available_morphs"]
    ) -> _base.FieldRef[Optional[AvailableMorphs15485]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["race_presets_female"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["available_hair_colors_female"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["face_details_texture_set_list_female"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_face_texture_female"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tint_masks"]
    ) -> _base.FieldRef[tuple[TintAssets15547, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model15566]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class HeadData15335(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE/52:Head Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "head_data_marker": _base.Binding(
            path="RACE/52:Head Data/0:Head Data Marker",
            kind="subrecord",
            name="Head Data Marker",
        ),
        "male_head_data": _base.Binding(
            path="RACE/52:Head Data/1:Male Head Data",
            kind="sequence",
            name="Male Head Data",
        ),
        "female_head_data": _base.Binding(
            path="RACE/52:Head Data/2:Female Head Data",
            kind="sequence",
            name="Female Head Data",
        ),
    }

    head_data_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    male_head_data: Optional[MaleHeadData15338] = None
    """Value decoded from this schema node."""

    female_head_data: Optional[FemaleHeadData15474] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["head_data_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_head_data"]
    ) -> _base.FieldRef[Optional[MaleHeadData15338]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_head_data"]
    ) -> _base.FieldRef[Optional[FemaleHeadData15474]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class RaceRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RACE"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "RACE"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="RACE/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="RACE/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "description": _base.Binding(
            path="RACE/2:Description",
            kind="subrecord",
            name="Description",
        ),
        "count": _base.Binding(
            path="RACE/3:Count",
            kind="subrecord",
            name="Count",
        ),
        "actor_effects": _base.Binding(
            path="RACE/4:Actor Effects",
            kind="repeat",
            name="Actor Effects",
            repeated_path="RACE/4:Actor Effects/repeat/0:Actor Effect",
            child_kind="subrecord",
        ),
        "skin": _base.Binding(
            path="RACE/5:Skin",
            kind="subrecord",
            name="Skin",
        ),
        "biped_body_template": _base.Binding(
            path="RACE/6:Biped Body Template",
            kind="choice",
            name="Biped Body Template",
        ),
        "keyword_count": _base.Binding(
            path="RACE/7:Keyword Count",
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path="RACE/8:Keywords",
            kind="subrecord",
            name="Keywords",
        ),
        "data": _base.Binding(
            path="RACE/9:DATA",
            kind="subrecord",
            name="DATA",
        ),
        "male_marker": _base.Binding(
            path="RACE/10:Male Marker",
            kind="subrecord",
            name="Male Marker",
        ),
        "male_skeletal_model": _base.Binding(
            path="RACE/11:Male Skeletal Model",
            kind="subrecord",
            name="Male Skeletal Model",
        ),
        "model_information_value": _base.Binding(
            path="RACE/12:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "female_marker": _base.Binding(
            path="RACE/13:Female Marker",
            kind="subrecord",
            name="Female Marker",
        ),
        "female_skeletal_model": _base.Binding(
            path="RACE/14:Female Skeletal Model",
            kind="subrecord",
            name="Female Skeletal Model",
        ),
        "model_information_value_14170": _base.Binding(
            path="RACE/15:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "marker_nam2_1": _base.Binding(
            path="RACE/16:Marker NAM2 #1",
            kind="subrecord",
            name="Marker NAM2 #1",
        ),
        "movement_type_names": _base.Binding(
            path="RACE/17:Movement Type Names",
            kind="repeat",
            name="Movement Type Names",
            repeated_path="RACE/17:Movement Type Names/repeat/0:Name",
            child_kind="subrecord",
        ),
        "voices": _base.Binding(
            path="RACE/18:Voices",
            kind="subrecord",
            name="Voices",
        ),
        "decapitate_armors": _base.Binding(
            path="RACE/19:Decapitate Armors",
            kind="subrecord",
            name="Decapitate Armors",
        ),
        "default_hair_colors": _base.Binding(
            path="RACE/20:Default Hair Colors",
            kind="subrecord",
            name="Default Hair Colors",
        ),
        "total_number_of_tints_in_list": _base.Binding(
            path="RACE/21:Total Number of Tints in List",
            kind="subrecord",
            name="Total Number of Tints in List",
        ),
        "face_gen_main_clamp": _base.Binding(
            path="RACE/22:FaceGen - Main clamp",
            kind="subrecord",
            name="FaceGen - Main clamp",
        ),
        "face_gen_face_clamp": _base.Binding(
            path="RACE/23:FaceGen - Face clamp",
            kind="subrecord",
            name="FaceGen - Face clamp",
        ),
        "attack_race": _base.Binding(
            path="RACE/24:Attack Race",
            kind="subrecord",
            name="Attack Race",
        ),
        "attacks": _base.Binding(
            path="RACE/25:Attacks",
            kind="repeat",
            name="Attacks",
            repeated_path="RACE/25:Attacks/repeat/0:Attack",
            child_kind="sequence",
        ),
        "body_data": _base.Binding(
            path="RACE/26:Body Data",
            kind="sequence",
            name="Body Data",
        ),
        "hairs": _base.Binding(
            path="RACE/27:Hairs",
            kind="subrecord",
            name="Hairs",
        ),
        "eyes": _base.Binding(
            path="RACE/28:Eyes",
            kind="subrecord",
            name="Eyes",
        ),
        "body_part_data": _base.Binding(
            path="RACE/29:Body Part Data",
            kind="subrecord",
            name="Body Part Data",
        ),
        "marker_nam2_2": _base.Binding(
            path="RACE/30:Marker NAM2 #2",
            kind="subrecord",
            name="Marker NAM2 #2",
        ),
        "marker_nam3_3": _base.Binding(
            path="RACE/31:Marker NAM3 #3",
            kind="subrecord",
            name="Marker NAM3 #3",
        ),
        "male_behavior_graph": _base.Binding(
            path="RACE/32:Male Behavior Graph",
            kind="sequence",
            name="Male Behavior Graph",
        ),
        "female_behavior_graph": _base.Binding(
            path="RACE/33:Female Behavior Graph",
            kind="sequence",
            name="Female Behavior Graph",
        ),
        "material_type": _base.Binding(
            path="RACE/34:Material Type",
            kind="subrecord",
            name="Material Type",
        ),
        "impact_data_set": _base.Binding(
            path="RACE/35:Impact Data Set",
            kind="subrecord",
            name="Impact Data Set",
        ),
        "decapitation_fx": _base.Binding(
            path="RACE/36:Decapitation FX",
            kind="subrecord",
            name="Decapitation FX",
        ),
        "open_loot_sound": _base.Binding(
            path="RACE/37:Open Loot Sound",
            kind="subrecord",
            name="Open Loot Sound",
        ),
        "close_loot_sound": _base.Binding(
            path="RACE/38:Close Loot Sound",
            kind="subrecord",
            name="Close Loot Sound",
        ),
        "biped_object_names": _base.Binding(
            path="RACE/39:Biped Object Names",
            kind="repeat",
            name="Biped Object Names",
            repeated_path="RACE/39:Biped Object Names/repeat/0:Name",
            child_kind="subrecord",
        ),
        "movement_types": _base.Binding(
            path="RACE/40:Movement Types",
            kind="repeat",
            name="Movement Types",
            repeated_path="RACE/40:Movement Types/repeat/0:Movement Types",
            child_kind="sequence",
        ),
        "equipment_flags": _base.Binding(
            path="RACE/41:Equipment Flags",
            kind="subrecord",
            name="Equipment Flags",
        ),
        "equip_slots": _base.Binding(
            path="RACE/42:Equip Slots",
            kind="repeat",
            name="Equip Slots",
            repeated_path="RACE/42:Equip Slots/repeat/0:Equip Slot",
            child_kind="subrecord",
        ),
        "unarmed_equip_slot": _base.Binding(
            path="RACE/43:Unarmed Equip Slot",
            kind="subrecord",
            name="Unarmed Equip Slot",
        ),
        "phoneme_target_names": _base.Binding(
            path="RACE/44:Phoneme Target Names",
            kind="repeat",
            name="Phoneme Target Names",
            repeated_path="RACE/44:Phoneme Target Names/repeat/0:Name",
            child_kind="subrecord",
        ),
        "face_fx_phonemes": _base.Binding(
            path="RACE/45:FaceFX Phonemes",
            kind="sequence",
            name="FaceFX Phonemes",
        ),
        "base_movement_default_walk": _base.Binding(
            path="RACE/46:Base Movement Default - Walk",
            kind="subrecord",
            name="Base Movement Default - Walk",
        ),
        "base_movement_default_run": _base.Binding(
            path="RACE/47:Base Movement Default - Run",
            kind="subrecord",
            name="Base Movement Default - Run",
        ),
        "base_movement_default_swim": _base.Binding(
            path="RACE/48:Base Movement Default - Swim",
            kind="subrecord",
            name="Base Movement Default - Swim",
        ),
        "base_movement_default_fly": _base.Binding(
            path="RACE/49:Base Movement Default - Fly",
            kind="subrecord",
            name="Base Movement Default - Fly",
        ),
        "base_movement_default_sneak": _base.Binding(
            path="RACE/50:Base Movement Default - Sneak",
            kind="subrecord",
            name="Base Movement Default - Sneak",
        ),
        "base_movement_default_sprint": _base.Binding(
            path="RACE/51:Base Movement Default - Sprint",
            kind="subrecord",
            name="Base Movement Default - Sprint",
        ),
        "head_data": _base.Binding(
            path="RACE/52:Head Data",
            kind="sequence",
            name="Head Data",
        ),
        "morph_race": _base.Binding(
            path="RACE/53:Morph race",
            kind="subrecord",
            name="Morph race",
        ),
        "armor_race": _base.Binding(
            path="RACE/54:Armor race",
            kind="subrecord",
            name="Armor race",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    actor_effects: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    skin: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    biped_body_template: Optional[
        Annotated[Structure14064, _VARIANT_14063]
        | Annotated[Structure14070, _VARIANT_14069]
    ] = None
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    data: Optional[Structure14081] = None
    """Value decoded from this schema node."""

    male_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    male_skeletal_model: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure14131, _VARIANT_14131]
        | Annotated[Structure14136, _VARIANT_14136]
        | Annotated[Structure14141, _VARIANT_14141]
        | Annotated[Structure14150, _VARIANT_14150]
    ] = None
    """Value decoded from this schema node."""

    female_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    female_skeletal_model: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value_14170: Optional[
        Annotated[Structure14172, _VARIANT_14172]
        | Annotated[Structure14177, _VARIANT_14177]
        | Annotated[Structure14182, _VARIANT_14182]
        | Annotated[Structure14191, _VARIANT_14191]
    ] = None
    """Value decoded from this schema node."""

    marker_nam2_1: Optional[bytes] = None
    """Value decoded from this schema node."""

    movement_type_names: tuple[str, ...] = ()
    """Value decoded from this schema node."""

    voices: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    decapitate_armors: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    default_hair_colors: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    total_number_of_tints_in_list: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    face_gen_main_clamp: Optional[float] = None
    """Value decoded from this schema node."""

    face_gen_face_clamp: Optional[float] = None
    """Value decoded from this schema node."""

    attack_race: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    attacks: tuple[Attack14230, ...] = ()
    """Value decoded from this schema node."""

    body_data: Optional[BodyData14246] = None
    """Value decoded from this schema node."""

    hairs: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    eyes: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    body_part_data: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    marker_nam2_2: Optional[bytes] = None
    """Value decoded from this schema node."""

    marker_nam3_3: Optional[bytes] = None
    """Value decoded from this schema node."""

    male_behavior_graph: Optional[MaleBehaviorGraph14367] = None
    """Value decoded from this schema node."""

    female_behavior_graph: Optional[FemaleBehaviorGraph14416] = None
    """Value decoded from this schema node."""

    material_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    impact_data_set: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    decapitation_fx: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    open_loot_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    close_loot_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    biped_object_names: tuple[str, ...] = ()
    """Value decoded from this schema node."""

    movement_types: tuple[MovementTypes14479, ...] = ()
    """Value decoded from this schema node."""

    equipment_flags: Optional[
        HandToHandMeleeOneHandSwordOneHandDaAea5D13714496
    ] = None
    """Value decoded from this schema node."""

    equip_slots: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    unarmed_equip_slot: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    phoneme_target_names: tuple[str, ...] = ()
    """Value decoded from this schema node."""

    face_fx_phonemes: Optional[FaceFxPhonemes14505] = None
    """Value decoded from this schema node."""

    base_movement_default_walk: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    base_movement_default_run: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    base_movement_default_swim: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    base_movement_default_fly: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    base_movement_default_sneak: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    base_movement_default_sprint: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    head_data: Optional[HeadData15335] = None
    """Value decoded from this schema node."""

    morph_race: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    armor_race: Optional[_values.FormId] = None
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
    def field(
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
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
        self, name: Literal["actor_effects"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skin"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["biped_body_template"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure14064, _VARIANT_14063]
            | Annotated[Structure14070, _VARIANT_14069]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["keyword_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["keywords"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure14081]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_skeletal_model"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_information_value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure14131, _VARIANT_14131]
            | Annotated[Structure14136, _VARIANT_14136]
            | Annotated[Structure14141, _VARIANT_14141]
            | Annotated[Structure14150, _VARIANT_14150]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_skeletal_model"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_information_value_14170"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure14172, _VARIANT_14172]
            | Annotated[Structure14177, _VARIANT_14177]
            | Annotated[Structure14182, _VARIANT_14182]
            | Annotated[Structure14191, _VARIANT_14191]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["marker_nam2_1"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["movement_type_names"]
    ) -> _base.FieldRef[tuple[str, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["voices"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["decapitate_armors"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_hair_colors"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["total_number_of_tints_in_list"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["face_gen_main_clamp"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["face_gen_face_clamp"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_race"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attacks"]
    ) -> _base.FieldRef[tuple[Attack14230, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["body_data"]
    ) -> _base.FieldRef[Optional[BodyData14246]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hairs"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eyes"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["body_part_data"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["marker_nam2_2"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["marker_nam3_3"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_behavior_graph"]
    ) -> _base.FieldRef[Optional[MaleBehaviorGraph14367]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_behavior_graph"]
    ) -> _base.FieldRef[Optional[FemaleBehaviorGraph14416]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["material_type"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["impact_data_set"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["decapitation_fx"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["open_loot_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["close_loot_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["biped_object_names"]
    ) -> _base.FieldRef[tuple[str, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["movement_types"]
    ) -> _base.FieldRef[tuple[MovementTypes14479, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_flags"]
    ) -> _base.FieldRef[
        Optional[HandToHandMeleeOneHandSwordOneHandDaAea5D13714496]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equip_slots"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unarmed_equip_slot"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["phoneme_target_names"]
    ) -> _base.FieldRef[tuple[str, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["face_fx_phonemes"]
    ) -> _base.FieldRef[Optional[FaceFxPhonemes14505]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_movement_default_walk"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_movement_default_run"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_movement_default_swim"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_movement_default_fly"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_movement_default_sneak"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_movement_default_sprint"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head_data"]
    ) -> _base.FieldRef[Optional[HeadData15335]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["morph_race"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["armor_race"]
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
