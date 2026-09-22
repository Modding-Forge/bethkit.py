"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure11470(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "COBJ/2:Items/repeat/0:Item/0:Item/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path="COBJ/2:Items/repeat/0:Item/0:Item/payload/0:Item",
            kind="primitive",
            name="Item",
        ),
        "count": _base.Binding(
            path="COBJ/2:Items/repeat/0:Item/0:Item/payload/1:Count",
            kind="primitive",
            name="Count",
        ),
    }

    item: _values.FormId
    """Value decoded from this schema node."""

    count: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["item"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
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


_VARIANT_11477: _base.Variant = _base.Variant(
    path=(
        "COBJ/2:Items/repeat/0:Item/1:Extra Data/payload/1:Glob"
        "al Variable / Required Rank/variants/0:Unused"
    )
)


_VARIANT_11478: _base.Variant = _base.Variant(
    path=(
        "COBJ/2:Items/repeat/0:Item/1:Extra Data/payload/1:Glob"
        "al Variable / Required Rank/variants/1:Global Variable"
    )
)


_VARIANT_11479: _base.Variant = _base.Variant(
    path=(
        "COBJ/2:Items/repeat/0:Item/1:Extra Data/payload/1:Glob"
        "al Variable / Required Rank/variants/2:Required Rank"
    )
)


class Structure11474(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "COBJ/2:Items/repeat/0:Item/1:Extra Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path=("COBJ/2:Items/repeat/0:Item/1:Extra Data/payload/0:Owner"),
            kind="primitive",
            name="Owner",
        ),
        "global_variable_required_rank": _base.Binding(
            path=(
                "COBJ/2:Items/repeat/0:Item/1:Extra Data/payload/1:Glob"
                "al Variable / Required Rank"
            ),
            kind="union",
            name="Global Variable / Required Rank",
        ),
        "item_condition": _base.Binding(
            path=(
                "COBJ/2:Items/repeat/0:Item/1:Extra Data/payload/2:Item"
                " Condition"
            ),
            kind="primitive",
            name="Item Condition",
        ),
    }

    owner: _values.FormId
    """Value decoded from this schema node."""

    global_variable_required_rank: (
        Annotated[bytes, _VARIANT_11477]
        | Annotated[_values.FormId, _VARIANT_11478]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11479,
        ]
    )
    """Value decoded from this schema node."""

    item_condition: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["owner"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["global_variable_required_rank"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_11477]
        | Annotated[_values.FormId, _VARIANT_11478]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11479,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["item_condition"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Item11468(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "COBJ/2:Items/repeat/0:Item"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path="COBJ/2:Items/repeat/0:Item/0:Item",
            kind="subrecord",
            name="Item",
        ),
        "extra_data": _base.Binding(
            path="COBJ/2:Items/repeat/0:Item/1:Extra Data",
            kind="subrecord",
            name="Extra Data",
        ),
    }

    item: Optional[Structure11470] = None
    """Value decoded from this schema node."""

    extra_data: Optional[Structure11474] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["item"]
    ) -> _base.FieldRef[Optional[Structure11470]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["extra_data"]
    ) -> _base.FieldRef[Optional[Structure11474]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_11488: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_11489: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_11493: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_11494: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/1:None"
    )
)


_VARIANT_11495: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/2:Integer"
    )
)


_VARIANT_11496: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/3:Float"
    )
)


_VARIANT_11497: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/4:Variable Name"
    )
)


class Sex11498(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_11498: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/5:Sex"
    )
)


class ActorValue11499(_values.OpenIntEnum):
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


_VARIANT_11499: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType11500(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_11500: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/7:Crime Type"
    )
)


class Axis11501(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_11501: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/8:Axis"
    )
)


_VARIANT_11502: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat11503(_values.OpenIntEnum):
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


_VARIANT_11503: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment11504(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_11504: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_11505: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/12:Equip Type"
    )
)


class FormType11506(_values.OpenIntEnum):
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


_VARIANT_11506: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage11507(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_11507: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_11508: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_11509: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_11510: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/17:Actor"
    )
)


_VARIANT_11511: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_11512: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/19:Idle"
    )
)


_VARIANT_11513: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/20:Form List"
    )
)


_VARIANT_11514: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/21:Quest"
    )
)


_VARIANT_11515: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/22:Faction"
    )
)


_VARIANT_11516: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/23:Cell"
    )
)


_VARIANT_11517: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/24:Class"
    )
)


_VARIANT_11518: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/25:Race"
    )
)


_VARIANT_11519: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_11520: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/27:Global"
    )
)


_VARIANT_11521: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/28:Weather"
    )
)


_VARIANT_11522: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/29:Package"
    )
)


_VARIANT_11523: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_11524: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/31:Perk"
    )
)


_VARIANT_11525: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/32:Owner"
    )
)


_VARIANT_11526: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_11527: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_11528: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_11529: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction11530(_values.OpenIntEnum):
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


_VARIANT_11530: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_11531: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_11532: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_11533: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/40:Region"
    )
)


_VARIANT_11534: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction11535(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_11535: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/42:Player Action"
    )
)


class CastingType11536(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_11536: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_11537: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/44:Shout"
    )
)


_VARIANT_11538: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/45:Location"
    )
)


_VARIANT_11539: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_11540: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/47:Alias"
    )
)


_VARIANT_11541: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_11542: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim11543(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_11543: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry11544(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_11544: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_11545: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/52:Scene"
    )
)


class WardState11546(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_11546: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_11547: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/54:Event"
    )
)


_VARIANT_11548: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_11549: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_11550: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/57:Faction"
    )
)


_VARIANT_11552: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_11553: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/1:None"
    )
)


_VARIANT_11554: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/2:Integer"
    )
)


_VARIANT_11555: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/3:Float"
    )
)


_VARIANT_11556: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/4:Variable Name"
    )
)


class Sex11557(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_11557: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/5:Sex"
    )
)


class ActorValue11558(_values.OpenIntEnum):
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


_VARIANT_11558: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType11559(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_11559: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/7:Crime Type"
    )
)


class Axis11560(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_11560: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/8:Axis"
    )
)


_VARIANT_11561: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat11562(_values.OpenIntEnum):
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


_VARIANT_11562: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment11563(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_11563: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_11564: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/12:Equip Type"
    )
)


class FormType11565(_values.OpenIntEnum):
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


_VARIANT_11565: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage11566(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_11566: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_11567: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_11568: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_11569: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/17:Actor"
    )
)


_VARIANT_11570: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_11571: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/19:Idle"
    )
)


_VARIANT_11572: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/20:Form List"
    )
)


_VARIANT_11573: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/21:Quest"
    )
)


_VARIANT_11574: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/22:Faction"
    )
)


_VARIANT_11575: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/23:Cell"
    )
)


_VARIANT_11576: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/24:Class"
    )
)


_VARIANT_11577: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/25:Race"
    )
)


_VARIANT_11578: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_11579: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/27:Global"
    )
)


_VARIANT_11580: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/28:Weather"
    )
)


_VARIANT_11581: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/29:Package"
    )
)


_VARIANT_11582: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_11583: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/31:Perk"
    )
)


_VARIANT_11584: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/32:Owner"
    )
)


_VARIANT_11585: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_11586: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_11587: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_11588: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction11589(_values.OpenIntEnum):
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


_VARIANT_11589: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_11591: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/0:W"
        "eapon"
    )
)


_VARIANT_11592: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/1:W"
        "eapon List"
    )
)


_VARIANT_11593: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/2:T"
        "arget"
    )
)


_VARIANT_11594: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/3:T"
        "arget List"
    )
)


_VARIANT_11595: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/4:U"
        "nknown"
    )
)


class TargetPart11596(_values.OpenIntEnum):
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


_VARIANT_11596: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/5:T"
        "arget Part"
    )
)


class VatsAction11597(_values.OpenIntEnum):
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


_VARIANT_11597: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/6:V"
        "ATS Action"
    )
)


_VARIANT_11598: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/7:U"
        "nknown"
    )
)


_VARIANT_11599: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/8:U"
        "nknown"
    )
)


_VARIANT_11600: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/9:C"
        "ritical Effect"
    )
)


_VARIANT_11601: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/10:"
        "Critical Effect List"
    )
)


_VARIANT_11602: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/11:"
        "Unknown"
    )
)


_VARIANT_11603: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/12:"
        "Unknown"
    )
)


_VARIANT_11604: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/13:"
        "Unknown"
    )
)


_VARIANT_11605: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/14:"
        "Unknown"
    )
)


class WeaponType11606(_values.OpenIntEnum):
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


_VARIANT_11606: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/15:"
        "Weapon Type"
    )
)


_VARIANT_11607: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/16:"
        "Unknown"
    )
)


_VARIANT_11608: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/17:"
        "Unknown"
    )
)


class ProjectileType11609(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_11609: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/18:"
        "Projectile Type"
    )
)


class DeliveryType11610(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_11610: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/19:"
        "Delivery Type"
    )
)


class CastingType11611(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_11611: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/20:"
        "Casting Type"
    )
)


_VARIANT_11590: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_11612: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_11613: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/40:Region"
    )
)


_VARIANT_11614: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction11615(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_11615: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/42:Player Action"
    )
)


class CastingType11616(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_11616: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_11617: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/44:Shout"
    )
)


_VARIANT_11618: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/45:Location"
    )
)


_VARIANT_11619: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_11620: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/47:Alias"
    )
)


_VARIANT_11621: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_11622: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim11623(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_11623: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry11624(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_11624: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_11625: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/52:Scene"
    )
)


class WardState11626(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_11626: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_11627: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/54:Event"
    )
)


_VARIANT_11628: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_11629: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_11630: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/57:Faction"
    )
)


class RunOn11631(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_11633: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/0:Unused"
    )
)


_VARIANT_11634: _base.Variant = _base.Variant(
    path=(
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/1:Reference"
    )
)


class Structure11484(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
                "Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_11491": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
                "Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
                "Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
                "Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "COBJ/3:Conditions/repeat/0:Condition/0:CTDA/payload/9:"
                "Parameter #3"
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
        Annotated[float, _VARIANT_11488]
        | Annotated[_values.FormId, _VARIANT_11489]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_11491: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_11493]
        | Annotated[bytes, _VARIANT_11494]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11495,
        ]
        | Annotated[float, _VARIANT_11496]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11497,
        ]
        | Annotated[Sex11498, _VARIANT_11498]
        | Annotated[ActorValue11499, _VARIANT_11499]
        | Annotated[CrimeType11500, _VARIANT_11500]
        | Annotated[Axis11501, _VARIANT_11501]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11502,
        ]
        | Annotated[MiscStat11503, _VARIANT_11503]
        | Annotated[Alignment11504, _VARIANT_11504]
        | Annotated[_values.FormId, _VARIANT_11505]
        | Annotated[FormType11506, _VARIANT_11506]
        | Annotated[CriticalStage11507, _VARIANT_11507]
        | Annotated[_values.FormId, _VARIANT_11508]
        | Annotated[_values.FormId, _VARIANT_11509]
        | Annotated[_values.FormId, _VARIANT_11510]
        | Annotated[_values.FormId, _VARIANT_11511]
        | Annotated[_values.FormId, _VARIANT_11512]
        | Annotated[_values.FormId, _VARIANT_11513]
        | Annotated[_values.FormId, _VARIANT_11514]
        | Annotated[_values.FormId, _VARIANT_11515]
        | Annotated[_values.FormId, _VARIANT_11516]
        | Annotated[_values.FormId, _VARIANT_11517]
        | Annotated[_values.FormId, _VARIANT_11518]
        | Annotated[_values.FormId, _VARIANT_11519]
        | Annotated[_values.FormId, _VARIANT_11520]
        | Annotated[_values.FormId, _VARIANT_11521]
        | Annotated[_values.FormId, _VARIANT_11522]
        | Annotated[_values.FormId, _VARIANT_11523]
        | Annotated[_values.FormId, _VARIANT_11524]
        | Annotated[_values.FormId, _VARIANT_11525]
        | Annotated[_values.FormId, _VARIANT_11526]
        | Annotated[_values.FormId, _VARIANT_11527]
        | Annotated[_values.FormId, _VARIANT_11528]
        | Annotated[_values.FormId, _VARIANT_11529]
        | Annotated[VatsValueFunction11530, _VARIANT_11530]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11531,
        ]
        | Annotated[_values.FormId, _VARIANT_11532]
        | Annotated[_values.FormId, _VARIANT_11533]
        | Annotated[_values.FormId, _VARIANT_11534]
        | Annotated[PlayerAction11535, _VARIANT_11535]
        | Annotated[CastingType11536, _VARIANT_11536]
        | Annotated[_values.FormId, _VARIANT_11537]
        | Annotated[_values.FormId, _VARIANT_11538]
        | Annotated[_values.FormId, _VARIANT_11539]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11540,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11541,
        ]
        | Annotated[_values.FormId, _VARIANT_11542]
        | Annotated[FurnitureAnim11543, _VARIANT_11543]
        | Annotated[FurnitureEntry11544, _VARIANT_11544]
        | Annotated[_values.FormId, _VARIANT_11545]
        | Annotated[WardState11546, _VARIANT_11546]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11547,
        ]
        | Annotated[_values.FormId, _VARIANT_11548]
        | Annotated[_values.FormId, _VARIANT_11549]
        | Annotated[_values.FormId, _VARIANT_11550]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_11552]
        | Annotated[bytes, _VARIANT_11553]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11554,
        ]
        | Annotated[float, _VARIANT_11555]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11556,
        ]
        | Annotated[Sex11557, _VARIANT_11557]
        | Annotated[ActorValue11558, _VARIANT_11558]
        | Annotated[CrimeType11559, _VARIANT_11559]
        | Annotated[Axis11560, _VARIANT_11560]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11561,
        ]
        | Annotated[MiscStat11562, _VARIANT_11562]
        | Annotated[Alignment11563, _VARIANT_11563]
        | Annotated[_values.FormId, _VARIANT_11564]
        | Annotated[FormType11565, _VARIANT_11565]
        | Annotated[CriticalStage11566, _VARIANT_11566]
        | Annotated[_values.FormId, _VARIANT_11567]
        | Annotated[_values.FormId, _VARIANT_11568]
        | Annotated[_values.FormId, _VARIANT_11569]
        | Annotated[_values.FormId, _VARIANT_11570]
        | Annotated[_values.FormId, _VARIANT_11571]
        | Annotated[_values.FormId, _VARIANT_11572]
        | Annotated[_values.FormId, _VARIANT_11573]
        | Annotated[_values.FormId, _VARIANT_11574]
        | Annotated[_values.FormId, _VARIANT_11575]
        | Annotated[_values.FormId, _VARIANT_11576]
        | Annotated[_values.FormId, _VARIANT_11577]
        | Annotated[_values.FormId, _VARIANT_11578]
        | Annotated[_values.FormId, _VARIANT_11579]
        | Annotated[_values.FormId, _VARIANT_11580]
        | Annotated[_values.FormId, _VARIANT_11581]
        | Annotated[_values.FormId, _VARIANT_11582]
        | Annotated[_values.FormId, _VARIANT_11583]
        | Annotated[_values.FormId, _VARIANT_11584]
        | Annotated[_values.FormId, _VARIANT_11585]
        | Annotated[_values.FormId, _VARIANT_11586]
        | Annotated[_values.FormId, _VARIANT_11587]
        | Annotated[_values.FormId, _VARIANT_11588]
        | Annotated[VatsValueFunction11589, _VARIANT_11589]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_11591]
            | Annotated[_values.FormId, _VARIANT_11592]
            | Annotated[_values.FormId, _VARIANT_11593]
            | Annotated[_values.FormId, _VARIANT_11594]
            | Annotated[bytes, _VARIANT_11595]
            | Annotated[TargetPart11596, _VARIANT_11596]
            | Annotated[VatsAction11597, _VARIANT_11597]
            | Annotated[bytes, _VARIANT_11598]
            | Annotated[bytes, _VARIANT_11599]
            | Annotated[_values.FormId, _VARIANT_11600]
            | Annotated[_values.FormId, _VARIANT_11601]
            | Annotated[bytes, _VARIANT_11602]
            | Annotated[bytes, _VARIANT_11603]
            | Annotated[bytes, _VARIANT_11604]
            | Annotated[bytes, _VARIANT_11605]
            | Annotated[WeaponType11606, _VARIANT_11606]
            | Annotated[bytes, _VARIANT_11607]
            | Annotated[bytes, _VARIANT_11608]
            | Annotated[ProjectileType11609, _VARIANT_11609]
            | Annotated[DeliveryType11610, _VARIANT_11610]
            | Annotated[CastingType11611, _VARIANT_11611],
            _VARIANT_11590,
        ]
        | Annotated[_values.FormId, _VARIANT_11612]
        | Annotated[_values.FormId, _VARIANT_11613]
        | Annotated[_values.FormId, _VARIANT_11614]
        | Annotated[PlayerAction11615, _VARIANT_11615]
        | Annotated[CastingType11616, _VARIANT_11616]
        | Annotated[_values.FormId, _VARIANT_11617]
        | Annotated[_values.FormId, _VARIANT_11618]
        | Annotated[_values.FormId, _VARIANT_11619]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11620,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11621,
        ]
        | Annotated[_values.FormId, _VARIANT_11622]
        | Annotated[FurnitureAnim11623, _VARIANT_11623]
        | Annotated[FurnitureEntry11624, _VARIANT_11624]
        | Annotated[_values.FormId, _VARIANT_11625]
        | Annotated[WardState11626, _VARIANT_11626]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11627,
        ]
        | Annotated[_values.FormId, _VARIANT_11628]
        | Annotated[_values.FormId, _VARIANT_11629]
        | Annotated[_values.FormId, _VARIANT_11630]
    )
    """Value decoded from this schema node."""

    run_on: RunOn11631
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11633,
        ]
        | Annotated[_values.FormId, _VARIANT_11634]
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
        Annotated[float, _VARIANT_11488]
        | Annotated[_values.FormId, _VARIANT_11489]
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
    def field(self, name: Literal["unused_11491"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_11493]
        | Annotated[bytes, _VARIANT_11494]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11495,
        ]
        | Annotated[float, _VARIANT_11496]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11497,
        ]
        | Annotated[Sex11498, _VARIANT_11498]
        | Annotated[ActorValue11499, _VARIANT_11499]
        | Annotated[CrimeType11500, _VARIANT_11500]
        | Annotated[Axis11501, _VARIANT_11501]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11502,
        ]
        | Annotated[MiscStat11503, _VARIANT_11503]
        | Annotated[Alignment11504, _VARIANT_11504]
        | Annotated[_values.FormId, _VARIANT_11505]
        | Annotated[FormType11506, _VARIANT_11506]
        | Annotated[CriticalStage11507, _VARIANT_11507]
        | Annotated[_values.FormId, _VARIANT_11508]
        | Annotated[_values.FormId, _VARIANT_11509]
        | Annotated[_values.FormId, _VARIANT_11510]
        | Annotated[_values.FormId, _VARIANT_11511]
        | Annotated[_values.FormId, _VARIANT_11512]
        | Annotated[_values.FormId, _VARIANT_11513]
        | Annotated[_values.FormId, _VARIANT_11514]
        | Annotated[_values.FormId, _VARIANT_11515]
        | Annotated[_values.FormId, _VARIANT_11516]
        | Annotated[_values.FormId, _VARIANT_11517]
        | Annotated[_values.FormId, _VARIANT_11518]
        | Annotated[_values.FormId, _VARIANT_11519]
        | Annotated[_values.FormId, _VARIANT_11520]
        | Annotated[_values.FormId, _VARIANT_11521]
        | Annotated[_values.FormId, _VARIANT_11522]
        | Annotated[_values.FormId, _VARIANT_11523]
        | Annotated[_values.FormId, _VARIANT_11524]
        | Annotated[_values.FormId, _VARIANT_11525]
        | Annotated[_values.FormId, _VARIANT_11526]
        | Annotated[_values.FormId, _VARIANT_11527]
        | Annotated[_values.FormId, _VARIANT_11528]
        | Annotated[_values.FormId, _VARIANT_11529]
        | Annotated[VatsValueFunction11530, _VARIANT_11530]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11531,
        ]
        | Annotated[_values.FormId, _VARIANT_11532]
        | Annotated[_values.FormId, _VARIANT_11533]
        | Annotated[_values.FormId, _VARIANT_11534]
        | Annotated[PlayerAction11535, _VARIANT_11535]
        | Annotated[CastingType11536, _VARIANT_11536]
        | Annotated[_values.FormId, _VARIANT_11537]
        | Annotated[_values.FormId, _VARIANT_11538]
        | Annotated[_values.FormId, _VARIANT_11539]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11540,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11541,
        ]
        | Annotated[_values.FormId, _VARIANT_11542]
        | Annotated[FurnitureAnim11543, _VARIANT_11543]
        | Annotated[FurnitureEntry11544, _VARIANT_11544]
        | Annotated[_values.FormId, _VARIANT_11545]
        | Annotated[WardState11546, _VARIANT_11546]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11547,
        ]
        | Annotated[_values.FormId, _VARIANT_11548]
        | Annotated[_values.FormId, _VARIANT_11549]
        | Annotated[_values.FormId, _VARIANT_11550]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_11552]
        | Annotated[bytes, _VARIANT_11553]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11554,
        ]
        | Annotated[float, _VARIANT_11555]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11556,
        ]
        | Annotated[Sex11557, _VARIANT_11557]
        | Annotated[ActorValue11558, _VARIANT_11558]
        | Annotated[CrimeType11559, _VARIANT_11559]
        | Annotated[Axis11560, _VARIANT_11560]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11561,
        ]
        | Annotated[MiscStat11562, _VARIANT_11562]
        | Annotated[Alignment11563, _VARIANT_11563]
        | Annotated[_values.FormId, _VARIANT_11564]
        | Annotated[FormType11565, _VARIANT_11565]
        | Annotated[CriticalStage11566, _VARIANT_11566]
        | Annotated[_values.FormId, _VARIANT_11567]
        | Annotated[_values.FormId, _VARIANT_11568]
        | Annotated[_values.FormId, _VARIANT_11569]
        | Annotated[_values.FormId, _VARIANT_11570]
        | Annotated[_values.FormId, _VARIANT_11571]
        | Annotated[_values.FormId, _VARIANT_11572]
        | Annotated[_values.FormId, _VARIANT_11573]
        | Annotated[_values.FormId, _VARIANT_11574]
        | Annotated[_values.FormId, _VARIANT_11575]
        | Annotated[_values.FormId, _VARIANT_11576]
        | Annotated[_values.FormId, _VARIANT_11577]
        | Annotated[_values.FormId, _VARIANT_11578]
        | Annotated[_values.FormId, _VARIANT_11579]
        | Annotated[_values.FormId, _VARIANT_11580]
        | Annotated[_values.FormId, _VARIANT_11581]
        | Annotated[_values.FormId, _VARIANT_11582]
        | Annotated[_values.FormId, _VARIANT_11583]
        | Annotated[_values.FormId, _VARIANT_11584]
        | Annotated[_values.FormId, _VARIANT_11585]
        | Annotated[_values.FormId, _VARIANT_11586]
        | Annotated[_values.FormId, _VARIANT_11587]
        | Annotated[_values.FormId, _VARIANT_11588]
        | Annotated[VatsValueFunction11589, _VARIANT_11589]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_11591]
            | Annotated[_values.FormId, _VARIANT_11592]
            | Annotated[_values.FormId, _VARIANT_11593]
            | Annotated[_values.FormId, _VARIANT_11594]
            | Annotated[bytes, _VARIANT_11595]
            | Annotated[TargetPart11596, _VARIANT_11596]
            | Annotated[VatsAction11597, _VARIANT_11597]
            | Annotated[bytes, _VARIANT_11598]
            | Annotated[bytes, _VARIANT_11599]
            | Annotated[_values.FormId, _VARIANT_11600]
            | Annotated[_values.FormId, _VARIANT_11601]
            | Annotated[bytes, _VARIANT_11602]
            | Annotated[bytes, _VARIANT_11603]
            | Annotated[bytes, _VARIANT_11604]
            | Annotated[bytes, _VARIANT_11605]
            | Annotated[WeaponType11606, _VARIANT_11606]
            | Annotated[bytes, _VARIANT_11607]
            | Annotated[bytes, _VARIANT_11608]
            | Annotated[ProjectileType11609, _VARIANT_11609]
            | Annotated[DeliveryType11610, _VARIANT_11610]
            | Annotated[CastingType11611, _VARIANT_11611],
            _VARIANT_11590,
        ]
        | Annotated[_values.FormId, _VARIANT_11612]
        | Annotated[_values.FormId, _VARIANT_11613]
        | Annotated[_values.FormId, _VARIANT_11614]
        | Annotated[PlayerAction11615, _VARIANT_11615]
        | Annotated[CastingType11616, _VARIANT_11616]
        | Annotated[_values.FormId, _VARIANT_11617]
        | Annotated[_values.FormId, _VARIANT_11618]
        | Annotated[_values.FormId, _VARIANT_11619]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11620,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11621,
        ]
        | Annotated[_values.FormId, _VARIANT_11622]
        | Annotated[FurnitureAnim11623, _VARIANT_11623]
        | Annotated[FurnitureEntry11624, _VARIANT_11624]
        | Annotated[_values.FormId, _VARIANT_11625]
        | Annotated[WardState11626, _VARIANT_11626]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11627,
        ]
        | Annotated[_values.FormId, _VARIANT_11628]
        | Annotated[_values.FormId, _VARIANT_11629]
        | Annotated[_values.FormId, _VARIANT_11630]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn11631]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11633,
        ]
        | Annotated[_values.FormId, _VARIANT_11634]
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


class Condition11482(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "COBJ/3:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="COBJ/3:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("COBJ/3:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("COBJ/3:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure11484] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure11484]]:
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


class ConstructibleObjectRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "COBJ"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "COBJ"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="COBJ/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "count": _base.Binding(
            path="COBJ/1:Count",
            kind="subrecord",
            name="Count",
        ),
        "items": _base.Binding(
            path="COBJ/2:Items",
            kind="repeat",
            name="Items",
            repeated_path="COBJ/2:Items/repeat/0:Item",
            child_kind="sequence",
        ),
        "conditions": _base.Binding(
            path="COBJ/3:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="COBJ/3:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "created_object": _base.Binding(
            path="COBJ/4:Created Object",
            kind="subrecord",
            name="Created Object",
        ),
        "workbench_keyword": _base.Binding(
            path="COBJ/5:Workbench Keyword",
            kind="subrecord",
            name="Workbench Keyword",
        ),
        "created_object_count": _base.Binding(
            path="COBJ/6:Created Object Count",
            kind="subrecord",
            name="Created Object Count",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    items: tuple[Item11468, ...] = ()
    """Value decoded from this schema node."""

    conditions: tuple[Condition11482, ...] = ()
    """Value decoded from this schema node."""

    created_object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    workbench_keyword: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    created_object_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
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
        self, name: Literal["items"]
    ) -> _base.FieldRef[tuple[Item11468, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition11482, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["created_object"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["workbench_keyword"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["created_object_count"]
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
