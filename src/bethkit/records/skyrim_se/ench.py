"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure3521(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ENCH/1:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="ENCH/1:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="ENCH/1:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="ENCH/1:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="ENCH/1:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="ENCH/1:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="ENCH/1:Object Bounds/payload/5:Z2",
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


class Flags3533(enum.IntFlag):
    """Named values from the pinned schema."""

    NO_AUTO_CALC = 1
    VALUE = 2
    EXTEND_DURATION_ON_RECAST = 4


class CastType3534(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


class TargetType3536(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


class EnchantType3537(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ENCHANTMENT = 6
    STAFF_ENCHANTMENT = 12


class Structure3531(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ENCH/3:Effect Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "enchantment_cost": _base.Binding(
            path="ENCH/3:Effect Data/payload/0:Enchantment Cost",
            kind="primitive",
            name="Enchantment Cost",
        ),
        "flags": _base.Binding(
            path="ENCH/3:Effect Data/payload/1:Flags",
            kind="primitive",
            name="Flags",
        ),
        "cast_type": _base.Binding(
            path="ENCH/3:Effect Data/payload/2:Cast Type",
            kind="primitive",
            name="Cast Type",
        ),
        "enchantment_amount": _base.Binding(
            path="ENCH/3:Effect Data/payload/3:Enchantment Amount",
            kind="primitive",
            name="Enchantment Amount",
        ),
        "target_type": _base.Binding(
            path="ENCH/3:Effect Data/payload/4:Target Type",
            kind="primitive",
            name="Target Type",
        ),
        "enchant_type": _base.Binding(
            path="ENCH/3:Effect Data/payload/5:Enchant Type",
            kind="primitive",
            name="Enchant Type",
        ),
        "charge_time": _base.Binding(
            path="ENCH/3:Effect Data/payload/6:Charge Time",
            kind="primitive",
            name="Charge Time",
        ),
        "base_enchantment": _base.Binding(
            path="ENCH/3:Effect Data/payload/7:Base Enchantment",
            kind="primitive",
            name="Base Enchantment",
        ),
        "worn_restrictions": _base.Binding(
            path="ENCH/3:Effect Data/payload/8:Worn Restrictions",
            kind="primitive",
            name="Worn Restrictions",
        ),
    }

    enchantment_cost: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    flags: Flags3533
    """Value decoded from this schema node."""

    cast_type: CastType3534
    """Value decoded from this schema node."""

    enchantment_amount: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    target_type: TargetType3536
    """Value decoded from this schema node."""

    enchant_type: EnchantType3537
    """Value decoded from this schema node."""

    charge_time: float
    """Value decoded from this schema node."""

    base_enchantment: _values.FormId
    """Value decoded from this schema node."""

    worn_restrictions: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["enchantment_cost"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags3533]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["cast_type"]) -> _base.FieldRef[CastType3534]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enchantment_amount"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_type"]
    ) -> _base.FieldRef[TargetType3536]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enchant_type"]
    ) -> _base.FieldRef[EnchantType3537]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["charge_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_enchantment"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["worn_restrictions"]
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


class Structure3546(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ENCH/4:Effects/repeat/0:Effect/1:EFIT/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "magnitude": _base.Binding(
            path=("ENCH/4:Effects/repeat/0:Effect/1:EFIT/payload/0:Magnitude"),
            kind="primitive",
            name="Magnitude",
        ),
        "area": _base.Binding(
            path=("ENCH/4:Effects/repeat/0:Effect/1:EFIT/payload/1:Area"),
            kind="primitive",
            name="Area",
        ),
        "duration": _base.Binding(
            path=("ENCH/4:Effects/repeat/0:Effect/1:EFIT/payload/2:Duration"),
            kind="primitive",
            name="Duration",
        ),
    }

    magnitude: float
    """Value decoded from this schema node."""

    area: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    duration: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["magnitude"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["area"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["duration"]
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


_VARIANT_3557: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/2:Comparison Value/variants/0:"
        "Comparison Value - Float"
    )
)


_VARIANT_3558: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/2:Comparison Value/variants/1:"
        "Comparison Value - Global"
    )
)


_VARIANT_3562: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/0:Unkn"
        "own"
    )
)


_VARIANT_3563: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/1:None"
    )
)


_VARIANT_3564: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/2:Inte"
        "ger"
    )
)


_VARIANT_3565: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/3:Floa"
        "t"
    )
)


_VARIANT_3566: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/4:Vari"
        "able Name"
    )
)


class Sex3567(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_3567: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/5:Sex"
    )
)


class ActorValue3568(_values.OpenIntEnum):
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


_VARIANT_3568: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/6:Acto"
        "r Value"
    )
)


class CrimeType3569(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_3569: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/7:Crim"
        "e Type"
    )
)


class Axis3570(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_3570: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/8:Axis"
    )
)


_VARIANT_3571: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/9:Ques"
        "t Stage (unused)"
    )
)


class MiscStat3572(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ARMOR_MADE = 37001190
    STORES_INVESTED_IN = 97801986
    QUESTS_COMPLETED = 226200342
    FAVORITE_WEAPON = 387732369
    POISONS_MIXED = 398870120
    EASTMARCH_BOUNTY = 439874358
    WEAPONS_IMPROVED = 490448964
    BRIBES = 494469227
    NECKS_BITTEN = 583191504
    CRITICAL_STRIKES = 584432184
    WEAPONS_MADE = 636611109
    DAYS_AS_A_VAMPIRE = 735757167
    WORDS_OF_POWER_UNLOCKED = 745422784
    BRAWLS_WON = 830376780
    LARGEST_BOUNTY = 891348752
    DAEDRIC_QUESTS_COMPLETED = 894973771
    BUNNIES_SLAUGHTERED = 906157711
    ARMOR_IMPROVED = 913147087
    DAWNGUARD_QUESTS_COMPLETED = 933717029
    WEREWOLF_TRANSFORMATIONS = 950197606
    DAYS_PASSED = 1013082768
    THE_PALE_BOUNTY = 1042709879
    CREATURES_KILLED = 1085349630
    UNDEAD_KILLED = 1104460815
    FAVORITE_SPELL = 1105033126
    POTIONS_MIXED = 1109974661
    WHITERUN_BOUNTY = 1110571599
    DRAGON_SOULS_COLLECTED = 1188494268
    PERSUASIONS = 1202160743
    INGREDIENTS_EATEN = 1203019797
    TRAINING_SESSIONS = 1277502353
    FINES_PAID = 1325669026
    THE_RIFT_BOUNTY = 1352810345
    TIMES_SHOUTED = 1353365043
    HJAALMARCH_BOUNTY = 1366050925
    FAVORITE_SHOUT = 1368112206
    HOUSES_OWNED = 1383987287
    THE_DARK_BROTHERHOOD_QUESTS_COMPLETED = 1387948235
    CHESTS_LOOTED = 1406790069
    NUM_VAMPIRE_PERKS = 1456274516
    AUTOMATIONS_KILLED = 1470102133
    GOLD_FOUND = 1472236023
    LOCKS_PICKED = 1479134254
    FALKREATH_BOUNTY = 1522772205
    SPELLS_LEARNED = 1590206234
    WEAPONS_DISARMED = 1638253993
    THIEVES_GUILD_QUESTS_COMPLETED = 1655892317
    JAIL_ESCAPES = 1713849931
    COLLEGE_OF_WINTERHOLD_QUESTS_COMPLETED = 1724695818
    CIVIL_WAR_QUESTS_COMPLETED = 1748769152
    THE_REACH_BOUNTY = 1773437303
    DAYS_AS_A_WEREWOLF = 1852327312
    MAULS = 1904714248
    SHOUTS_MASTERED = 1931170611
    NUM_WEREWOLF_PERKS = 1990305216
    TRESPASSES = 2062195755
    INTIMIDATIONS = 2100189120
    POISONS_USED = 2106535590
    MAIN_QUESTS_COMPLETED = 2124573741
    ITEMS_STOLEN = 2196869314
    DISEASES_CONTRACTED = 2237050248
    FAVORITE_SCHOOL = 2276536012
    MAGIC_ITEMS_MADE = 2282264953
    LOCATIONS_DISCOVERED = 2317680098
    ASSAULTS = 2384517065
    WINGS_PLUCKED = 2455132007
    FOOD_EATEN = 2467410475
    TIMES_JAILED = 2488068755
    WORDS_OF_POWER_LEARNED = 2493491132
    POTIONS_USED = 2519854097
    MISC_OBJECTIVES_COMPLETED = 2565756380
    TOTAL_LIFETIME_BOUNTY = 2579203800
    TRIBAL_ORCS_BOUNTY = 2792761076
    SOUL_GEMS_USED = 2806824579
    DAEDRA_KILLED = 2838534159
    DUNGEONS_CLEARED = 2856601237
    SKILL_BOOKS_READ = 2900652247
    HORSES_OWNED = 2963399470
    SIDE_QUESTS_COMPLETED = 2980988818
    STANDING_STONES_FOUND = 2991694662
    SNEAK_ATTACKS = 3042364498
    DAYS_JAILED = 3069253851
    BACKSTABS = 3115648805
    SHOUTS_LEARNED = 3141089694
    NIRNROOTS_FOUND = 3203124359
    ITEMS_PICKPOCKETED = 3256287925
    SOULS_TRAPPED = 3268010547
    WINTERHOLD_BOUNTY = 3355201933
    HOURS_WAITING = 3402820769
    BOOKS_READ = 3434697422
    INGREDIENTS_HARVESTED = 3464766294
    THE_COMPANIONS_QUESTS_COMPLETED = 3506335793
    HAAFINGAR_BOUNTY = 3524188751
    MURDERS = 3548145929
    QUESTLINES_COMPLETED = 3731649534
    HORSES_STOLEN = 3954062824
    BARTERS = 3983150834
    PEOPLE_KILLED = 4062871859
    POCKETS_PICKED = 4072325684
    SKILL_INCREASES = 4080087246
    VAMPIRISM_CURES = 4086456481
    SHOUTS_UNLOCKED = 4179744954
    HOURS_SLEPT = 4194451480
    MOST_GOLD_CARRIED = 4194706187
    ANIMALS_KILLED = 4242362385


_VARIANT_3572: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/10:Mis"
        "c Stat"
    )
)


class Alignment3573(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_3573: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/11:Ali"
        "gnment"
    )
)


_VARIANT_3574: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/12:Equ"
        "ip Type"
    )
)


class FormType3575(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ACTIVATOR = 0
    ARMOR = 1
    BOOK = 2
    CONTAINER = 3
    DOOR = 4
    INGREDIENT = 5
    LIGHT = 6
    MISC_ITEM = 7
    STATIC = 8
    GRASS = 9
    TREE = 10
    WEAPON = 12
    ACTOR = 13
    LEVELED_CHARACTER = 14
    SPELL = 15
    ENCHANTMENT = 16
    POTION = 17
    LEVELED_ITEM = 18
    KEY = 19
    AMMO = 20
    FLORA = 21
    FURNITURE = 22
    SOUND_MARKER = 23
    LAND_TEXTURE = 24
    COMBAT_STYLE = 25
    LOAD_SCREEN = 26
    LEVELED_SPELL = 27
    ANIM_OBJECT = 28
    WATER_TYPE = 29
    IDLE_MARKER = 30
    EFFECT_SHADER = 31
    PROJECTILE = 32
    TALKING_ACTIVATOR = 33
    EXPLOSION = 34
    TEXTURE_SET = 35
    DEBRIS = 36
    MENU_ICON = 37
    FORM_LIST = 38
    PERK = 39
    BODY_PART_DATA = 40
    ADD_ON_NODE = 41
    MOVABLE_STATIC = 42
    CAMERA_SHOT = 43
    IMPACT_DATA = 44
    IMPACT_DATA_SET = 45
    QUEST = 46
    PACKAGE = 47
    VOICE_TYPE = 48
    CLASS = 49
    RACE = 50
    EYES = 51
    HEAD_PART = 52
    FACTION = 53
    NOTE = 54
    WEATHER = 55
    CLIMATE = 56
    ARMOR_ADDON = 57
    GLOBAL = 58
    IMAGESPACE = 59
    IMAGESPACE_MODIFIER = 60
    ENCOUNTER_ZONE = 61
    MESSAGE = 62
    CONSTRUCTIBLE_OBJECT = 63
    ACOUSTIC_SPACE = 64
    RAGDOLL = 65
    SCRIPT = 66
    MAGIC_EFFECT = 67
    MUSIC_TYPE = 68
    STATIC_COLLECTION = 69
    KEYWORD = 70
    LOCATION = 71
    LOCATION_REF_TYPE = 72
    FOOTSTEP = 73
    FOOTSTEP_SET = 74
    MATERIAL_TYPE = 75
    ACTOR_ACTION = 76
    MUSIC_TRACK = 77
    WORD_OF_POWER = 78
    SHOUT = 79
    RELATIONSHIP = 80
    EQUIP_SLOT = 81
    ASSOCIATION_TYPE = 82
    OUTFIT = 83
    ART_OBJECT = 84
    MATERIAL_OBJECT = 85
    LIGHTING_TEMPLATE = 87
    SHADER_PARTICLE_GEOMETRY = 88
    VISUAL_EFFECT = 89
    APPARATUS = 90
    MOVEMENT_TYPE = 91
    HAZARD = 92
    SM_EVENT_NODE = 93
    SOUND_DESCRIPTOR = 94
    DUAL_CAST_DATA = 95
    SOUND_CATEGORY = 96
    SOUL_GEM = 97
    SOUND_OUTPUT_MODEL = 98
    COLLISION_LAYER = 99
    SCROLL = 100
    COLOR_FORM = 101
    REVERB_PARAMETERS = 102


_VARIANT_3575: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/13:For"
        "m Type"
    )
)


class CriticalStage3576(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_3576: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/14:Cri"
        "tical Stage"
    )
)


_VARIANT_3577: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/15:Obj"
        "ect Reference"
    )
)


_VARIANT_3578: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/16:Inv"
        "entory Object"
    )
)


_VARIANT_3579: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/17:Act"
        "or"
    )
)


_VARIANT_3580: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/18:Voi"
        "ce Type"
    )
)


_VARIANT_3581: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/19:Idl"
        "e"
    )
)


_VARIANT_3582: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/20:For"
        "m List"
    )
)


_VARIANT_3583: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/21:Que"
        "st"
    )
)


_VARIANT_3584: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/22:Fac"
        "tion"
    )
)


_VARIANT_3585: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/23:Cel"
        "l"
    )
)


_VARIANT_3586: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/24:Cla"
        "ss"
    )
)


_VARIANT_3587: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/25:Rac"
        "e"
    )
)


_VARIANT_3588: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/26:Act"
        "or Base"
    )
)


_VARIANT_3589: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/27:Glo"
        "bal"
    )
)


_VARIANT_3590: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/28:Wea"
        "ther"
    )
)


_VARIANT_3591: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/29:Pac"
        "kage"
    )
)


_VARIANT_3592: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/30:Enc"
        "ounter Zone"
    )
)


_VARIANT_3593: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/31:Per"
        "k"
    )
)


_VARIANT_3594: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/32:Own"
        "er"
    )
)


_VARIANT_3595: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/33:Fur"
        "niture"
    )
)


_VARIANT_3596: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/34:Eff"
        "ect Item"
    )
)


_VARIANT_3597: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/35:Bas"
        "e Effect"
    )
)


_VARIANT_3598: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/36:Wor"
        "ldspace"
    )
)


class VatsValueFunction3599(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    WEAPON_IS = 0
    WEAPON_IN_LIST = 1
    TARGET_IS = 2
    TARGET_IN_LIST = 3
    TARGET_DISTANCE = 4
    TARGET_PART = 5
    VATS_ACTION = 6
    IS_SUCCESS = 7
    IS_CRITICAL = 8
    CRITICAL_EFFECT_IS = 9
    CRITICAL_EFFECT_IN_LIST = 10
    IS_FATAL = 11
    EXPLODE_PART = 12
    DISMEMBER_PART = 13
    CRIPPLE_PART = 14
    WEAPON_TYPE_IS = 15
    IS_STRANGER = 16
    IS_PARALYZING_PALM = 17
    PROJECTILE_TYPE_IS = 18
    DELIVERY_TYPE_IS = 19
    CASTING_TYPE_IS = 20


_VARIANT_3599: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/37:VAT"
        "S Value Function"
    )
)


_VARIANT_3600: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/38:VAT"
        "S Value Param (INVALID)"
    )
)


_VARIANT_3601: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/39:Ref"
        "erenceable Object"
    )
)


_VARIANT_3602: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/40:Reg"
        "ion"
    )
)


_VARIANT_3603: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/41:Key"
        "word"
    )
)


class PlayerAction3604(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_3604: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/42:Pla"
        "yer Action"
    )
)


class CastingType3605(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_3605: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/43:Cas"
        "ting Type"
    )
)


_VARIANT_3606: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/44:Sho"
        "ut"
    )
)


_VARIANT_3607: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/45:Loc"
        "ation"
    )
)


_VARIANT_3608: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/46:Loc"
        "ation Ref Type"
    )
)


_VARIANT_3609: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/47:Ali"
        "as"
    )
)


_VARIANT_3610: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/48:Pac"
        "kdata ID"
    )
)


_VARIANT_3611: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/49:Ass"
        "ociation Type"
    )
)


class FurnitureAnim3612(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_3612: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/50:Fur"
        "niture Anim"
    )
)


class FurnitureEntry3613(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_3613: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/51:Fur"
        "niture Entry"
    )
)


_VARIANT_3614: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/52:Sce"
        "ne"
    )
)


class WardState3615(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_3615: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/53:War"
        "d State"
    )
)


_VARIANT_3616: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/54:Eve"
        "nt"
    )
)


_VARIANT_3617: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/55:Eve"
        "nt Data"
    )
)


_VARIANT_3618: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/56:Kno"
        "wable"
    )
)


_VARIANT_3619: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/5:Parameter #1/variants/57:Fac"
        "tion"
    )
)


_VARIANT_3621: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/0:Unkn"
        "own"
    )
)


_VARIANT_3622: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/1:None"
    )
)


_VARIANT_3623: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/2:Inte"
        "ger"
    )
)


_VARIANT_3624: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/3:Floa"
        "t"
    )
)


_VARIANT_3625: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/4:Vari"
        "able Name"
    )
)


class Sex3626(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_3626: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/5:Sex"
    )
)


class ActorValue3627(_values.OpenIntEnum):
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


_VARIANT_3627: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/6:Acto"
        "r Value"
    )
)


class CrimeType3628(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_3628: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/7:Crim"
        "e Type"
    )
)


class Axis3629(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_3629: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/8:Axis"
    )
)


_VARIANT_3630: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/9:Ques"
        "t Stage"
    )
)


class MiscStat3631(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ARMOR_MADE = 37001190
    STORES_INVESTED_IN = 97801986
    QUESTS_COMPLETED = 226200342
    FAVORITE_WEAPON = 387732369
    POISONS_MIXED = 398870120
    EASTMARCH_BOUNTY = 439874358
    WEAPONS_IMPROVED = 490448964
    BRIBES = 494469227
    NECKS_BITTEN = 583191504
    CRITICAL_STRIKES = 584432184
    WEAPONS_MADE = 636611109
    DAYS_AS_A_VAMPIRE = 735757167
    WORDS_OF_POWER_UNLOCKED = 745422784
    BRAWLS_WON = 830376780
    LARGEST_BOUNTY = 891348752
    DAEDRIC_QUESTS_COMPLETED = 894973771
    BUNNIES_SLAUGHTERED = 906157711
    ARMOR_IMPROVED = 913147087
    DAWNGUARD_QUESTS_COMPLETED = 933717029
    WEREWOLF_TRANSFORMATIONS = 950197606
    DAYS_PASSED = 1013082768
    THE_PALE_BOUNTY = 1042709879
    CREATURES_KILLED = 1085349630
    UNDEAD_KILLED = 1104460815
    FAVORITE_SPELL = 1105033126
    POTIONS_MIXED = 1109974661
    WHITERUN_BOUNTY = 1110571599
    DRAGON_SOULS_COLLECTED = 1188494268
    PERSUASIONS = 1202160743
    INGREDIENTS_EATEN = 1203019797
    TRAINING_SESSIONS = 1277502353
    FINES_PAID = 1325669026
    THE_RIFT_BOUNTY = 1352810345
    TIMES_SHOUTED = 1353365043
    HJAALMARCH_BOUNTY = 1366050925
    FAVORITE_SHOUT = 1368112206
    HOUSES_OWNED = 1383987287
    THE_DARK_BROTHERHOOD_QUESTS_COMPLETED = 1387948235
    CHESTS_LOOTED = 1406790069
    NUM_VAMPIRE_PERKS = 1456274516
    AUTOMATIONS_KILLED = 1470102133
    GOLD_FOUND = 1472236023
    LOCKS_PICKED = 1479134254
    FALKREATH_BOUNTY = 1522772205
    SPELLS_LEARNED = 1590206234
    WEAPONS_DISARMED = 1638253993
    THIEVES_GUILD_QUESTS_COMPLETED = 1655892317
    JAIL_ESCAPES = 1713849931
    COLLEGE_OF_WINTERHOLD_QUESTS_COMPLETED = 1724695818
    CIVIL_WAR_QUESTS_COMPLETED = 1748769152
    THE_REACH_BOUNTY = 1773437303
    DAYS_AS_A_WEREWOLF = 1852327312
    MAULS = 1904714248
    SHOUTS_MASTERED = 1931170611
    NUM_WEREWOLF_PERKS = 1990305216
    TRESPASSES = 2062195755
    INTIMIDATIONS = 2100189120
    POISONS_USED = 2106535590
    MAIN_QUESTS_COMPLETED = 2124573741
    ITEMS_STOLEN = 2196869314
    DISEASES_CONTRACTED = 2237050248
    FAVORITE_SCHOOL = 2276536012
    MAGIC_ITEMS_MADE = 2282264953
    LOCATIONS_DISCOVERED = 2317680098
    ASSAULTS = 2384517065
    WINGS_PLUCKED = 2455132007
    FOOD_EATEN = 2467410475
    TIMES_JAILED = 2488068755
    WORDS_OF_POWER_LEARNED = 2493491132
    POTIONS_USED = 2519854097
    MISC_OBJECTIVES_COMPLETED = 2565756380
    TOTAL_LIFETIME_BOUNTY = 2579203800
    TRIBAL_ORCS_BOUNTY = 2792761076
    SOUL_GEMS_USED = 2806824579
    DAEDRA_KILLED = 2838534159
    DUNGEONS_CLEARED = 2856601237
    SKILL_BOOKS_READ = 2900652247
    HORSES_OWNED = 2963399470
    SIDE_QUESTS_COMPLETED = 2980988818
    STANDING_STONES_FOUND = 2991694662
    SNEAK_ATTACKS = 3042364498
    DAYS_JAILED = 3069253851
    BACKSTABS = 3115648805
    SHOUTS_LEARNED = 3141089694
    NIRNROOTS_FOUND = 3203124359
    ITEMS_PICKPOCKETED = 3256287925
    SOULS_TRAPPED = 3268010547
    WINTERHOLD_BOUNTY = 3355201933
    HOURS_WAITING = 3402820769
    BOOKS_READ = 3434697422
    INGREDIENTS_HARVESTED = 3464766294
    THE_COMPANIONS_QUESTS_COMPLETED = 3506335793
    HAAFINGAR_BOUNTY = 3524188751
    MURDERS = 3548145929
    QUESTLINES_COMPLETED = 3731649534
    HORSES_STOLEN = 3954062824
    BARTERS = 3983150834
    PEOPLE_KILLED = 4062871859
    POCKETS_PICKED = 4072325684
    SKILL_INCREASES = 4080087246
    VAMPIRISM_CURES = 4086456481
    SHOUTS_UNLOCKED = 4179744954
    HOURS_SLEPT = 4194451480
    MOST_GOLD_CARRIED = 4194706187
    ANIMALS_KILLED = 4242362385


_VARIANT_3631: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/10:Mis"
        "c Stat"
    )
)


class Alignment3632(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_3632: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/11:Ali"
        "gnment"
    )
)


_VARIANT_3633: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/12:Equ"
        "ip Type"
    )
)


class FormType3634(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ACTIVATOR = 0
    ARMOR = 1
    BOOK = 2
    CONTAINER = 3
    DOOR = 4
    INGREDIENT = 5
    LIGHT = 6
    MISC_ITEM = 7
    STATIC = 8
    GRASS = 9
    TREE = 10
    WEAPON = 12
    ACTOR = 13
    LEVELED_CHARACTER = 14
    SPELL = 15
    ENCHANTMENT = 16
    POTION = 17
    LEVELED_ITEM = 18
    KEY = 19
    AMMO = 20
    FLORA = 21
    FURNITURE = 22
    SOUND_MARKER = 23
    LAND_TEXTURE = 24
    COMBAT_STYLE = 25
    LOAD_SCREEN = 26
    LEVELED_SPELL = 27
    ANIM_OBJECT = 28
    WATER_TYPE = 29
    IDLE_MARKER = 30
    EFFECT_SHADER = 31
    PROJECTILE = 32
    TALKING_ACTIVATOR = 33
    EXPLOSION = 34
    TEXTURE_SET = 35
    DEBRIS = 36
    MENU_ICON = 37
    FORM_LIST = 38
    PERK = 39
    BODY_PART_DATA = 40
    ADD_ON_NODE = 41
    MOVABLE_STATIC = 42
    CAMERA_SHOT = 43
    IMPACT_DATA = 44
    IMPACT_DATA_SET = 45
    QUEST = 46
    PACKAGE = 47
    VOICE_TYPE = 48
    CLASS = 49
    RACE = 50
    EYES = 51
    HEAD_PART = 52
    FACTION = 53
    NOTE = 54
    WEATHER = 55
    CLIMATE = 56
    ARMOR_ADDON = 57
    GLOBAL = 58
    IMAGESPACE = 59
    IMAGESPACE_MODIFIER = 60
    ENCOUNTER_ZONE = 61
    MESSAGE = 62
    CONSTRUCTIBLE_OBJECT = 63
    ACOUSTIC_SPACE = 64
    RAGDOLL = 65
    SCRIPT = 66
    MAGIC_EFFECT = 67
    MUSIC_TYPE = 68
    STATIC_COLLECTION = 69
    KEYWORD = 70
    LOCATION = 71
    LOCATION_REF_TYPE = 72
    FOOTSTEP = 73
    FOOTSTEP_SET = 74
    MATERIAL_TYPE = 75
    ACTOR_ACTION = 76
    MUSIC_TRACK = 77
    WORD_OF_POWER = 78
    SHOUT = 79
    RELATIONSHIP = 80
    EQUIP_SLOT = 81
    ASSOCIATION_TYPE = 82
    OUTFIT = 83
    ART_OBJECT = 84
    MATERIAL_OBJECT = 85
    LIGHTING_TEMPLATE = 87
    SHADER_PARTICLE_GEOMETRY = 88
    VISUAL_EFFECT = 89
    APPARATUS = 90
    MOVEMENT_TYPE = 91
    HAZARD = 92
    SM_EVENT_NODE = 93
    SOUND_DESCRIPTOR = 94
    DUAL_CAST_DATA = 95
    SOUND_CATEGORY = 96
    SOUL_GEM = 97
    SOUND_OUTPUT_MODEL = 98
    COLLISION_LAYER = 99
    SCROLL = 100
    COLOR_FORM = 101
    REVERB_PARAMETERS = 102


_VARIANT_3634: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/13:For"
        "m Type"
    )
)


class CriticalStage3635(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_3635: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/14:Cri"
        "tical Stage"
    )
)


_VARIANT_3636: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/15:Obj"
        "ect Reference"
    )
)


_VARIANT_3637: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/16:Inv"
        "entory Object"
    )
)


_VARIANT_3638: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/17:Act"
        "or"
    )
)


_VARIANT_3639: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/18:Voi"
        "ce Type"
    )
)


_VARIANT_3640: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/19:Idl"
        "e"
    )
)


_VARIANT_3641: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/20:For"
        "m List"
    )
)


_VARIANT_3642: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/21:Que"
        "st"
    )
)


_VARIANT_3643: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/22:Fac"
        "tion"
    )
)


_VARIANT_3644: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/23:Cel"
        "l"
    )
)


_VARIANT_3645: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/24:Cla"
        "ss"
    )
)


_VARIANT_3646: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/25:Rac"
        "e"
    )
)


_VARIANT_3647: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/26:Act"
        "or Base"
    )
)


_VARIANT_3648: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/27:Glo"
        "bal"
    )
)


_VARIANT_3649: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/28:Wea"
        "ther"
    )
)


_VARIANT_3650: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/29:Pac"
        "kage"
    )
)


_VARIANT_3651: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/30:Enc"
        "ounter Zone"
    )
)


_VARIANT_3652: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/31:Per"
        "k"
    )
)


_VARIANT_3653: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/32:Own"
        "er"
    )
)


_VARIANT_3654: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/33:Fur"
        "niture"
    )
)


_VARIANT_3655: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/34:Eff"
        "ect Item"
    )
)


_VARIANT_3656: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/35:Bas"
        "e Effect"
    )
)


_VARIANT_3657: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/36:Wor"
        "ldspace"
    )
)


class VatsValueFunction3658(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    WEAPON_IS = 0
    WEAPON_IN_LIST = 1
    TARGET_IS = 2
    TARGET_IN_LIST = 3
    TARGET_DISTANCE = 4
    TARGET_PART = 5
    VATS_ACTION = 6
    IS_SUCCESS = 7
    IS_CRITICAL = 8
    CRITICAL_EFFECT_IS = 9
    CRITICAL_EFFECT_IN_LIST = 10
    IS_FATAL = 11
    EXPLODE_PART = 12
    DISMEMBER_PART = 13
    CRIPPLE_PART = 14
    WEAPON_TYPE_IS = 15
    IS_STRANGER = 16
    IS_PARALYZING_PALM = 17
    PROJECTILE_TYPE_IS = 18
    DELIVERY_TYPE_IS = 19
    CASTING_TYPE_IS = 20


_VARIANT_3658: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/37:VAT"
        "S Value Function"
    )
)


_VARIANT_3660: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/0:Weapon"
    )
)


_VARIANT_3661: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/1:Weapon List"
    )
)


_VARIANT_3662: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/2:Target"
    )
)


_VARIANT_3663: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/3:Target List"
    )
)


_VARIANT_3664: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/4:Unknown"
    )
)


class TargetPart3665(_values.OpenIntEnum):
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


_VARIANT_3665: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/5:Target Part"
    )
)


class VatsAction3666(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    UNARMED_ATTACK = 0
    ONE_HAND_MELEE_ATTACK = 1
    TWO_HAND_MELEE_ATTACK = 2
    MAGIC_ATTACK = 3
    RANGED_ATTACK = 4
    RELOAD = 5
    CROUCH = 6
    STAND = 7
    SWITCH_WEAPON = 8
    TOGGLE_WEAPON_DRAWN = 9
    HEAL = 10
    PLAYER_DEATH = 11


_VARIANT_3666: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/6:VATS Action"
    )
)


_VARIANT_3667: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/7:Unknown"
    )
)


_VARIANT_3668: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/8:Unknown"
    )
)


_VARIANT_3669: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/9:Critical Effect"
    )
)


_VARIANT_3670: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/10:Critical Effect List"
    )
)


_VARIANT_3671: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/11:Unknown"
    )
)


_VARIANT_3672: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/12:Unknown"
    )
)


_VARIANT_3673: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/13:Unknown"
    )
)


_VARIANT_3674: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/14:Unknown"
    )
)


class WeaponType3675(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    HAND_TO_HAND_MELEE = 0
    ONE_HAND_SWORD = 1
    ONE_HAND_DAGGER = 2
    ONE_HAND_AXE = 3
    ONE_HAND_MACE = 4
    TWO_HAND_SWORD = 5
    TWO_HAND_AXE = 6
    BOW = 7
    STAFF = 8
    CROSSBOW = 9


_VARIANT_3675: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_3676: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/16:Unknown"
    )
)


_VARIANT_3677: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/17:Unknown"
    )
)


class ProjectileType3678(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_3678: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/18:Projectile Type"
    )
)


class DeliveryType3679(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_3679: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/19:Delivery Type"
    )
)


class CastingType3680(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_3680: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param/variants/20:Casting Type"
    )
)


_VARIANT_3659: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/38:VAT"
        "S Value Param"
    )
)


_VARIANT_3681: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/39:Ref"
        "erenceable Object"
    )
)


_VARIANT_3682: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/40:Reg"
        "ion"
    )
)


_VARIANT_3683: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/41:Key"
        "word"
    )
)


class PlayerAction3684(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_3684: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/42:Pla"
        "yer Action"
    )
)


class CastingType3685(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_3685: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/43:Cas"
        "ting Type"
    )
)


_VARIANT_3686: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/44:Sho"
        "ut"
    )
)


_VARIANT_3687: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/45:Loc"
        "ation"
    )
)


_VARIANT_3688: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/46:Loc"
        "ation Ref Type"
    )
)


_VARIANT_3689: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/47:Ali"
        "as"
    )
)


_VARIANT_3690: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/48:Pac"
        "kdata ID"
    )
)


_VARIANT_3691: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/49:Ass"
        "ociation Type"
    )
)


class FurnitureAnim3692(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_3692: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/50:Fur"
        "niture Anim"
    )
)


class FurnitureEntry3693(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_3693: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/51:Fur"
        "niture Entry"
    )
)


_VARIANT_3694: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/52:Sce"
        "ne"
    )
)


class WardState3695(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_3695: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/53:War"
        "d State"
    )
)


_VARIANT_3696: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/54:Eve"
        "nt"
    )
)


_VARIANT_3697: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/55:Eve"
        "nt Data"
    )
)


_VARIANT_3698: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/56:Kno"
        "wable"
    )
)


_VARIANT_3699: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/6:Parameter #2/variants/57:Fac"
        "tion"
    )
)


class RunOn3700(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_3702: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/8:Reference/variants/0:Unused"
    )
)


_VARIANT_3703: _base.Variant = _base.Variant(
    path=(
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload/8:Reference/variants/1:Referen"
        "ce"
    )
)


class Structure3553(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
        "ondition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_3560": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA/payload/9:Parameter #3"
            ),
            kind="primitive",
            name="Parameter #3",
        ),
    }

    type: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    comparison_value: (
        Annotated[float, _VARIANT_3557]
        | Annotated[_values.FormId, _VARIANT_3558]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_3560: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_3562]
        | Annotated[bytes, _VARIANT_3563]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3564,
        ]
        | Annotated[float, _VARIANT_3565]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3566,
        ]
        | Annotated[Sex3567, _VARIANT_3567]
        | Annotated[ActorValue3568, _VARIANT_3568]
        | Annotated[CrimeType3569, _VARIANT_3569]
        | Annotated[Axis3570, _VARIANT_3570]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3571,
        ]
        | Annotated[MiscStat3572, _VARIANT_3572]
        | Annotated[Alignment3573, _VARIANT_3573]
        | Annotated[_values.FormId, _VARIANT_3574]
        | Annotated[FormType3575, _VARIANT_3575]
        | Annotated[CriticalStage3576, _VARIANT_3576]
        | Annotated[_values.FormId, _VARIANT_3577]
        | Annotated[_values.FormId, _VARIANT_3578]
        | Annotated[_values.FormId, _VARIANT_3579]
        | Annotated[_values.FormId, _VARIANT_3580]
        | Annotated[_values.FormId, _VARIANT_3581]
        | Annotated[_values.FormId, _VARIANT_3582]
        | Annotated[_values.FormId, _VARIANT_3583]
        | Annotated[_values.FormId, _VARIANT_3584]
        | Annotated[_values.FormId, _VARIANT_3585]
        | Annotated[_values.FormId, _VARIANT_3586]
        | Annotated[_values.FormId, _VARIANT_3587]
        | Annotated[_values.FormId, _VARIANT_3588]
        | Annotated[_values.FormId, _VARIANT_3589]
        | Annotated[_values.FormId, _VARIANT_3590]
        | Annotated[_values.FormId, _VARIANT_3591]
        | Annotated[_values.FormId, _VARIANT_3592]
        | Annotated[_values.FormId, _VARIANT_3593]
        | Annotated[_values.FormId, _VARIANT_3594]
        | Annotated[_values.FormId, _VARIANT_3595]
        | Annotated[_values.FormId, _VARIANT_3596]
        | Annotated[_values.FormId, _VARIANT_3597]
        | Annotated[_values.FormId, _VARIANT_3598]
        | Annotated[VatsValueFunction3599, _VARIANT_3599]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3600,
        ]
        | Annotated[_values.FormId, _VARIANT_3601]
        | Annotated[_values.FormId, _VARIANT_3602]
        | Annotated[_values.FormId, _VARIANT_3603]
        | Annotated[PlayerAction3604, _VARIANT_3604]
        | Annotated[CastingType3605, _VARIANT_3605]
        | Annotated[_values.FormId, _VARIANT_3606]
        | Annotated[_values.FormId, _VARIANT_3607]
        | Annotated[_values.FormId, _VARIANT_3608]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3609,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3610,
        ]
        | Annotated[_values.FormId, _VARIANT_3611]
        | Annotated[FurnitureAnim3612, _VARIANT_3612]
        | Annotated[FurnitureEntry3613, _VARIANT_3613]
        | Annotated[_values.FormId, _VARIANT_3614]
        | Annotated[WardState3615, _VARIANT_3615]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3616,
        ]
        | Annotated[_values.FormId, _VARIANT_3617]
        | Annotated[_values.FormId, _VARIANT_3618]
        | Annotated[_values.FormId, _VARIANT_3619]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_3621]
        | Annotated[bytes, _VARIANT_3622]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3623,
        ]
        | Annotated[float, _VARIANT_3624]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3625,
        ]
        | Annotated[Sex3626, _VARIANT_3626]
        | Annotated[ActorValue3627, _VARIANT_3627]
        | Annotated[CrimeType3628, _VARIANT_3628]
        | Annotated[Axis3629, _VARIANT_3629]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3630,
        ]
        | Annotated[MiscStat3631, _VARIANT_3631]
        | Annotated[Alignment3632, _VARIANT_3632]
        | Annotated[_values.FormId, _VARIANT_3633]
        | Annotated[FormType3634, _VARIANT_3634]
        | Annotated[CriticalStage3635, _VARIANT_3635]
        | Annotated[_values.FormId, _VARIANT_3636]
        | Annotated[_values.FormId, _VARIANT_3637]
        | Annotated[_values.FormId, _VARIANT_3638]
        | Annotated[_values.FormId, _VARIANT_3639]
        | Annotated[_values.FormId, _VARIANT_3640]
        | Annotated[_values.FormId, _VARIANT_3641]
        | Annotated[_values.FormId, _VARIANT_3642]
        | Annotated[_values.FormId, _VARIANT_3643]
        | Annotated[_values.FormId, _VARIANT_3644]
        | Annotated[_values.FormId, _VARIANT_3645]
        | Annotated[_values.FormId, _VARIANT_3646]
        | Annotated[_values.FormId, _VARIANT_3647]
        | Annotated[_values.FormId, _VARIANT_3648]
        | Annotated[_values.FormId, _VARIANT_3649]
        | Annotated[_values.FormId, _VARIANT_3650]
        | Annotated[_values.FormId, _VARIANT_3651]
        | Annotated[_values.FormId, _VARIANT_3652]
        | Annotated[_values.FormId, _VARIANT_3653]
        | Annotated[_values.FormId, _VARIANT_3654]
        | Annotated[_values.FormId, _VARIANT_3655]
        | Annotated[_values.FormId, _VARIANT_3656]
        | Annotated[_values.FormId, _VARIANT_3657]
        | Annotated[VatsValueFunction3658, _VARIANT_3658]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_3660]
            | Annotated[_values.FormId, _VARIANT_3661]
            | Annotated[_values.FormId, _VARIANT_3662]
            | Annotated[_values.FormId, _VARIANT_3663]
            | Annotated[bytes, _VARIANT_3664]
            | Annotated[TargetPart3665, _VARIANT_3665]
            | Annotated[VatsAction3666, _VARIANT_3666]
            | Annotated[bytes, _VARIANT_3667]
            | Annotated[bytes, _VARIANT_3668]
            | Annotated[_values.FormId, _VARIANT_3669]
            | Annotated[_values.FormId, _VARIANT_3670]
            | Annotated[bytes, _VARIANT_3671]
            | Annotated[bytes, _VARIANT_3672]
            | Annotated[bytes, _VARIANT_3673]
            | Annotated[bytes, _VARIANT_3674]
            | Annotated[WeaponType3675, _VARIANT_3675]
            | Annotated[bytes, _VARIANT_3676]
            | Annotated[bytes, _VARIANT_3677]
            | Annotated[ProjectileType3678, _VARIANT_3678]
            | Annotated[DeliveryType3679, _VARIANT_3679]
            | Annotated[CastingType3680, _VARIANT_3680],
            _VARIANT_3659,
        ]
        | Annotated[_values.FormId, _VARIANT_3681]
        | Annotated[_values.FormId, _VARIANT_3682]
        | Annotated[_values.FormId, _VARIANT_3683]
        | Annotated[PlayerAction3684, _VARIANT_3684]
        | Annotated[CastingType3685, _VARIANT_3685]
        | Annotated[_values.FormId, _VARIANT_3686]
        | Annotated[_values.FormId, _VARIANT_3687]
        | Annotated[_values.FormId, _VARIANT_3688]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3689,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3690,
        ]
        | Annotated[_values.FormId, _VARIANT_3691]
        | Annotated[FurnitureAnim3692, _VARIANT_3692]
        | Annotated[FurnitureEntry3693, _VARIANT_3693]
        | Annotated[_values.FormId, _VARIANT_3694]
        | Annotated[WardState3695, _VARIANT_3695]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3696,
        ]
        | Annotated[_values.FormId, _VARIANT_3697]
        | Annotated[_values.FormId, _VARIANT_3698]
        | Annotated[_values.FormId, _VARIANT_3699]
    )
    """Value decoded from this schema node."""

    run_on: RunOn3700
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3702,
        ]
        | Annotated[_values.FormId, _VARIANT_3703]
    )
    """Value decoded from this schema node."""

    parameter_3: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["type"]
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
    def field(
        self, name: Literal["comparison_value"]
    ) -> _base.FieldRef[
        Annotated[float, _VARIANT_3557]
        | Annotated[_values.FormId, _VARIANT_3558]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["function"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_3560"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_3562]
        | Annotated[bytes, _VARIANT_3563]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3564,
        ]
        | Annotated[float, _VARIANT_3565]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3566,
        ]
        | Annotated[Sex3567, _VARIANT_3567]
        | Annotated[ActorValue3568, _VARIANT_3568]
        | Annotated[CrimeType3569, _VARIANT_3569]
        | Annotated[Axis3570, _VARIANT_3570]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3571,
        ]
        | Annotated[MiscStat3572, _VARIANT_3572]
        | Annotated[Alignment3573, _VARIANT_3573]
        | Annotated[_values.FormId, _VARIANT_3574]
        | Annotated[FormType3575, _VARIANT_3575]
        | Annotated[CriticalStage3576, _VARIANT_3576]
        | Annotated[_values.FormId, _VARIANT_3577]
        | Annotated[_values.FormId, _VARIANT_3578]
        | Annotated[_values.FormId, _VARIANT_3579]
        | Annotated[_values.FormId, _VARIANT_3580]
        | Annotated[_values.FormId, _VARIANT_3581]
        | Annotated[_values.FormId, _VARIANT_3582]
        | Annotated[_values.FormId, _VARIANT_3583]
        | Annotated[_values.FormId, _VARIANT_3584]
        | Annotated[_values.FormId, _VARIANT_3585]
        | Annotated[_values.FormId, _VARIANT_3586]
        | Annotated[_values.FormId, _VARIANT_3587]
        | Annotated[_values.FormId, _VARIANT_3588]
        | Annotated[_values.FormId, _VARIANT_3589]
        | Annotated[_values.FormId, _VARIANT_3590]
        | Annotated[_values.FormId, _VARIANT_3591]
        | Annotated[_values.FormId, _VARIANT_3592]
        | Annotated[_values.FormId, _VARIANT_3593]
        | Annotated[_values.FormId, _VARIANT_3594]
        | Annotated[_values.FormId, _VARIANT_3595]
        | Annotated[_values.FormId, _VARIANT_3596]
        | Annotated[_values.FormId, _VARIANT_3597]
        | Annotated[_values.FormId, _VARIANT_3598]
        | Annotated[VatsValueFunction3599, _VARIANT_3599]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3600,
        ]
        | Annotated[_values.FormId, _VARIANT_3601]
        | Annotated[_values.FormId, _VARIANT_3602]
        | Annotated[_values.FormId, _VARIANT_3603]
        | Annotated[PlayerAction3604, _VARIANT_3604]
        | Annotated[CastingType3605, _VARIANT_3605]
        | Annotated[_values.FormId, _VARIANT_3606]
        | Annotated[_values.FormId, _VARIANT_3607]
        | Annotated[_values.FormId, _VARIANT_3608]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3609,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3610,
        ]
        | Annotated[_values.FormId, _VARIANT_3611]
        | Annotated[FurnitureAnim3612, _VARIANT_3612]
        | Annotated[FurnitureEntry3613, _VARIANT_3613]
        | Annotated[_values.FormId, _VARIANT_3614]
        | Annotated[WardState3615, _VARIANT_3615]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3616,
        ]
        | Annotated[_values.FormId, _VARIANT_3617]
        | Annotated[_values.FormId, _VARIANT_3618]
        | Annotated[_values.FormId, _VARIANT_3619]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_3621]
        | Annotated[bytes, _VARIANT_3622]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3623,
        ]
        | Annotated[float, _VARIANT_3624]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3625,
        ]
        | Annotated[Sex3626, _VARIANT_3626]
        | Annotated[ActorValue3627, _VARIANT_3627]
        | Annotated[CrimeType3628, _VARIANT_3628]
        | Annotated[Axis3629, _VARIANT_3629]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3630,
        ]
        | Annotated[MiscStat3631, _VARIANT_3631]
        | Annotated[Alignment3632, _VARIANT_3632]
        | Annotated[_values.FormId, _VARIANT_3633]
        | Annotated[FormType3634, _VARIANT_3634]
        | Annotated[CriticalStage3635, _VARIANT_3635]
        | Annotated[_values.FormId, _VARIANT_3636]
        | Annotated[_values.FormId, _VARIANT_3637]
        | Annotated[_values.FormId, _VARIANT_3638]
        | Annotated[_values.FormId, _VARIANT_3639]
        | Annotated[_values.FormId, _VARIANT_3640]
        | Annotated[_values.FormId, _VARIANT_3641]
        | Annotated[_values.FormId, _VARIANT_3642]
        | Annotated[_values.FormId, _VARIANT_3643]
        | Annotated[_values.FormId, _VARIANT_3644]
        | Annotated[_values.FormId, _VARIANT_3645]
        | Annotated[_values.FormId, _VARIANT_3646]
        | Annotated[_values.FormId, _VARIANT_3647]
        | Annotated[_values.FormId, _VARIANT_3648]
        | Annotated[_values.FormId, _VARIANT_3649]
        | Annotated[_values.FormId, _VARIANT_3650]
        | Annotated[_values.FormId, _VARIANT_3651]
        | Annotated[_values.FormId, _VARIANT_3652]
        | Annotated[_values.FormId, _VARIANT_3653]
        | Annotated[_values.FormId, _VARIANT_3654]
        | Annotated[_values.FormId, _VARIANT_3655]
        | Annotated[_values.FormId, _VARIANT_3656]
        | Annotated[_values.FormId, _VARIANT_3657]
        | Annotated[VatsValueFunction3658, _VARIANT_3658]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_3660]
            | Annotated[_values.FormId, _VARIANT_3661]
            | Annotated[_values.FormId, _VARIANT_3662]
            | Annotated[_values.FormId, _VARIANT_3663]
            | Annotated[bytes, _VARIANT_3664]
            | Annotated[TargetPart3665, _VARIANT_3665]
            | Annotated[VatsAction3666, _VARIANT_3666]
            | Annotated[bytes, _VARIANT_3667]
            | Annotated[bytes, _VARIANT_3668]
            | Annotated[_values.FormId, _VARIANT_3669]
            | Annotated[_values.FormId, _VARIANT_3670]
            | Annotated[bytes, _VARIANT_3671]
            | Annotated[bytes, _VARIANT_3672]
            | Annotated[bytes, _VARIANT_3673]
            | Annotated[bytes, _VARIANT_3674]
            | Annotated[WeaponType3675, _VARIANT_3675]
            | Annotated[bytes, _VARIANT_3676]
            | Annotated[bytes, _VARIANT_3677]
            | Annotated[ProjectileType3678, _VARIANT_3678]
            | Annotated[DeliveryType3679, _VARIANT_3679]
            | Annotated[CastingType3680, _VARIANT_3680],
            _VARIANT_3659,
        ]
        | Annotated[_values.FormId, _VARIANT_3681]
        | Annotated[_values.FormId, _VARIANT_3682]
        | Annotated[_values.FormId, _VARIANT_3683]
        | Annotated[PlayerAction3684, _VARIANT_3684]
        | Annotated[CastingType3685, _VARIANT_3685]
        | Annotated[_values.FormId, _VARIANT_3686]
        | Annotated[_values.FormId, _VARIANT_3687]
        | Annotated[_values.FormId, _VARIANT_3688]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3689,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3690,
        ]
        | Annotated[_values.FormId, _VARIANT_3691]
        | Annotated[FurnitureAnim3692, _VARIANT_3692]
        | Annotated[FurnitureEntry3693, _VARIANT_3693]
        | Annotated[_values.FormId, _VARIANT_3694]
        | Annotated[WardState3695, _VARIANT_3695]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3696,
        ]
        | Annotated[_values.FormId, _VARIANT_3697]
        | Annotated[_values.FormId, _VARIANT_3698]
        | Annotated[_values.FormId, _VARIANT_3699]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn3700]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3702,
        ]
        | Annotated[_values.FormId, _VARIANT_3703]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_3"]
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


class Condition3551(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:C"
                "ondition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure3553] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure3553]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
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


class Effect3542(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ENCH/4:Effects/repeat/0:Effect"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "base_effect": _base.Binding(
            path="ENCH/4:Effects/repeat/0:Effect/0:Base Effect",
            kind="subrecord",
            name="Base Effect",
        ),
        "efit": _base.Binding(
            path="ENCH/4:Effects/repeat/0:Effect/1:EFIT",
            kind="subrecord",
            name="EFIT",
        ),
        "conditions": _base.Binding(
            path="ENCH/4:Effects/repeat/0:Effect/2:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "ENCH/4:Effects/repeat/0:Effect/2:Conditions/repeat/0:Condition"
            ),
            child_kind="sequence",
        ),
    }

    base_effect: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    efit: Optional[Structure3546] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition3551, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["base_effect"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["efit"]
    ) -> _base.FieldRef[Optional[Structure3546]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition3551, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ObjectEffectRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ENCH"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "ENCH"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="ENCH/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "object_bounds": _base.Binding(
            path="ENCH/1:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "name": _base.Binding(
            path="ENCH/2:Name",
            kind="subrecord",
            name="Name",
        ),
        "effect_data": _base.Binding(
            path="ENCH/3:Effect Data",
            kind="subrecord",
            name="Effect Data",
        ),
        "effects": _base.Binding(
            path="ENCH/4:Effects",
            kind="repeat",
            name="Effects",
            repeated_path="ENCH/4:Effects/repeat/0:Effect",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure3521] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    effect_data: Optional[Structure3531] = None
    """Value decoded from this schema node."""

    effects: tuple[Effect3542, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure3521]]:
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
        self, name: Literal["effect_data"]
    ) -> _base.FieldRef[Optional[Structure3531]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effects"]
    ) -> _base.FieldRef[tuple[Effect3542, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
