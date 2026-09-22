"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Icon10454(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LSCR/1:Icon"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "large_icon_file_name": _base.Binding(
            path="LSCR/1:Icon/0:Large Icon FileName",
            kind="subrecord",
            name="Large Icon FileName",
        ),
        "small_icon_file_name": _base.Binding(
            path="LSCR/1:Icon/1:Small Icon FileName",
            kind="subrecord",
            name="Small Icon FileName",
        ),
    }

    large_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    small_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["large_icon_file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["small_icon_file_name"]
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


_VARIANT_10468: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_10469: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_10473: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_10474: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/1:None"
    )
)


_VARIANT_10475: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/2:Integer"
    )
)


_VARIANT_10476: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/3:Float"
    )
)


_VARIANT_10477: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/4:Variable Name"
    )
)


class Sex10478(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_10478: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/5:Sex"
    )
)


class ActorValue10479(_values.OpenIntEnum):
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


_VARIANT_10479: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType10480(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_10480: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/7:Crime Type"
    )
)


class Axis10481(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_10481: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/8:Axis"
    )
)


_VARIANT_10482: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat10483(_values.OpenIntEnum):
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


_VARIANT_10483: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment10484(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_10484: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_10485: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/12:Equip Type"
    )
)


class FormType10486(_values.OpenIntEnum):
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


_VARIANT_10486: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage10487(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_10487: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_10488: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_10489: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_10490: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/17:Actor"
    )
)


_VARIANT_10491: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_10492: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/19:Idle"
    )
)


_VARIANT_10493: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/20:Form List"
    )
)


_VARIANT_10494: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/21:Quest"
    )
)


_VARIANT_10495: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/22:Faction"
    )
)


_VARIANT_10496: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/23:Cell"
    )
)


_VARIANT_10497: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/24:Class"
    )
)


_VARIANT_10498: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/25:Race"
    )
)


_VARIANT_10499: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_10500: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/27:Global"
    )
)


_VARIANT_10501: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/28:Weather"
    )
)


_VARIANT_10502: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/29:Package"
    )
)


_VARIANT_10503: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_10504: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/31:Perk"
    )
)


_VARIANT_10505: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/32:Owner"
    )
)


_VARIANT_10506: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_10507: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_10508: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_10509: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction10510(_values.OpenIntEnum):
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


_VARIANT_10510: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_10511: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_10512: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_10513: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/40:Region"
    )
)


_VARIANT_10514: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction10515(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_10515: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/42:Player Action"
    )
)


class CastingType10516(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_10516: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_10517: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/44:Shout"
    )
)


_VARIANT_10518: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/45:Location"
    )
)


_VARIANT_10519: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_10520: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/47:Alias"
    )
)


_VARIANT_10521: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_10522: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim10523(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_10523: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry10524(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_10524: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_10525: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/52:Scene"
    )
)


class WardState10526(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_10526: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_10527: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/54:Event"
    )
)


_VARIANT_10528: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_10529: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_10530: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/57:Faction"
    )
)


_VARIANT_10532: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_10533: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/1:None"
    )
)


_VARIANT_10534: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/2:Integer"
    )
)


_VARIANT_10535: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/3:Float"
    )
)


_VARIANT_10536: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/4:Variable Name"
    )
)


class Sex10537(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_10537: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/5:Sex"
    )
)


class ActorValue10538(_values.OpenIntEnum):
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


_VARIANT_10538: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType10539(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_10539: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/7:Crime Type"
    )
)


class Axis10540(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_10540: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/8:Axis"
    )
)


_VARIANT_10541: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat10542(_values.OpenIntEnum):
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


_VARIANT_10542: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment10543(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_10543: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_10544: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/12:Equip Type"
    )
)


class FormType10545(_values.OpenIntEnum):
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


_VARIANT_10545: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage10546(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_10546: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_10547: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_10548: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_10549: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/17:Actor"
    )
)


_VARIANT_10550: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_10551: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/19:Idle"
    )
)


_VARIANT_10552: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/20:Form List"
    )
)


_VARIANT_10553: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/21:Quest"
    )
)


_VARIANT_10554: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/22:Faction"
    )
)


_VARIANT_10555: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/23:Cell"
    )
)


_VARIANT_10556: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/24:Class"
    )
)


_VARIANT_10557: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/25:Race"
    )
)


_VARIANT_10558: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_10559: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/27:Global"
    )
)


_VARIANT_10560: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/28:Weather"
    )
)


_VARIANT_10561: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/29:Package"
    )
)


_VARIANT_10562: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_10563: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/31:Perk"
    )
)


_VARIANT_10564: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/32:Owner"
    )
)


_VARIANT_10565: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_10566: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_10567: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_10568: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction10569(_values.OpenIntEnum):
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


_VARIANT_10569: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_10571: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/0:W"
        "eapon"
    )
)


_VARIANT_10572: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/1:W"
        "eapon List"
    )
)


_VARIANT_10573: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/2:T"
        "arget"
    )
)


_VARIANT_10574: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/3:T"
        "arget List"
    )
)


_VARIANT_10575: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/4:U"
        "nknown"
    )
)


class TargetPart10576(_values.OpenIntEnum):
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


_VARIANT_10576: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/5:T"
        "arget Part"
    )
)


class VatsAction10577(_values.OpenIntEnum):
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


_VARIANT_10577: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/6:V"
        "ATS Action"
    )
)


_VARIANT_10578: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/7:U"
        "nknown"
    )
)


_VARIANT_10579: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/8:U"
        "nknown"
    )
)


_VARIANT_10580: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/9:C"
        "ritical Effect"
    )
)


_VARIANT_10581: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/10:"
        "Critical Effect List"
    )
)


_VARIANT_10582: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/11:"
        "Unknown"
    )
)


_VARIANT_10583: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/12:"
        "Unknown"
    )
)


_VARIANT_10584: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/13:"
        "Unknown"
    )
)


_VARIANT_10585: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/14:"
        "Unknown"
    )
)


class WeaponType10586(_values.OpenIntEnum):
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


_VARIANT_10586: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/15:"
        "Weapon Type"
    )
)


_VARIANT_10587: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/16:"
        "Unknown"
    )
)


_VARIANT_10588: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/17:"
        "Unknown"
    )
)


class ProjectileType10589(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_10589: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/18:"
        "Projectile Type"
    )
)


class DeliveryType10590(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_10590: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/19:"
        "Delivery Type"
    )
)


class CastingType10591(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_10591: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/20:"
        "Casting Type"
    )
)


_VARIANT_10570: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_10592: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_10593: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/40:Region"
    )
)


_VARIANT_10594: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction10595(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_10595: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/42:Player Action"
    )
)


class CastingType10596(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_10596: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_10597: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/44:Shout"
    )
)


_VARIANT_10598: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/45:Location"
    )
)


_VARIANT_10599: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_10600: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/47:Alias"
    )
)


_VARIANT_10601: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_10602: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim10603(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_10603: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry10604(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_10604: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_10605: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/52:Scene"
    )
)


class WardState10606(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_10606: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_10607: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/54:Event"
    )
)


_VARIANT_10608: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_10609: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_10610: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/57:Faction"
    )
)


class RunOn10611(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_10613: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/0:Unused"
    )
)


_VARIANT_10614: _base.Variant = _base.Variant(
    path=(
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/1:Reference"
    )
)


class Structure10464(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
                "Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_10471": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
                "Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
                "Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
                "Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "LSCR/3:Conditions/repeat/0:Condition/0:CTDA/payload/9:"
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
        Annotated[float, _VARIANT_10468]
        | Annotated[_values.FormId, _VARIANT_10469]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_10471: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_10473]
        | Annotated[bytes, _VARIANT_10474]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10475,
        ]
        | Annotated[float, _VARIANT_10476]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10477,
        ]
        | Annotated[Sex10478, _VARIANT_10478]
        | Annotated[ActorValue10479, _VARIANT_10479]
        | Annotated[CrimeType10480, _VARIANT_10480]
        | Annotated[Axis10481, _VARIANT_10481]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10482,
        ]
        | Annotated[MiscStat10483, _VARIANT_10483]
        | Annotated[Alignment10484, _VARIANT_10484]
        | Annotated[_values.FormId, _VARIANT_10485]
        | Annotated[FormType10486, _VARIANT_10486]
        | Annotated[CriticalStage10487, _VARIANT_10487]
        | Annotated[_values.FormId, _VARIANT_10488]
        | Annotated[_values.FormId, _VARIANT_10489]
        | Annotated[_values.FormId, _VARIANT_10490]
        | Annotated[_values.FormId, _VARIANT_10491]
        | Annotated[_values.FormId, _VARIANT_10492]
        | Annotated[_values.FormId, _VARIANT_10493]
        | Annotated[_values.FormId, _VARIANT_10494]
        | Annotated[_values.FormId, _VARIANT_10495]
        | Annotated[_values.FormId, _VARIANT_10496]
        | Annotated[_values.FormId, _VARIANT_10497]
        | Annotated[_values.FormId, _VARIANT_10498]
        | Annotated[_values.FormId, _VARIANT_10499]
        | Annotated[_values.FormId, _VARIANT_10500]
        | Annotated[_values.FormId, _VARIANT_10501]
        | Annotated[_values.FormId, _VARIANT_10502]
        | Annotated[_values.FormId, _VARIANT_10503]
        | Annotated[_values.FormId, _VARIANT_10504]
        | Annotated[_values.FormId, _VARIANT_10505]
        | Annotated[_values.FormId, _VARIANT_10506]
        | Annotated[_values.FormId, _VARIANT_10507]
        | Annotated[_values.FormId, _VARIANT_10508]
        | Annotated[_values.FormId, _VARIANT_10509]
        | Annotated[VatsValueFunction10510, _VARIANT_10510]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10511,
        ]
        | Annotated[_values.FormId, _VARIANT_10512]
        | Annotated[_values.FormId, _VARIANT_10513]
        | Annotated[_values.FormId, _VARIANT_10514]
        | Annotated[PlayerAction10515, _VARIANT_10515]
        | Annotated[CastingType10516, _VARIANT_10516]
        | Annotated[_values.FormId, _VARIANT_10517]
        | Annotated[_values.FormId, _VARIANT_10518]
        | Annotated[_values.FormId, _VARIANT_10519]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10520,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10521,
        ]
        | Annotated[_values.FormId, _VARIANT_10522]
        | Annotated[FurnitureAnim10523, _VARIANT_10523]
        | Annotated[FurnitureEntry10524, _VARIANT_10524]
        | Annotated[_values.FormId, _VARIANT_10525]
        | Annotated[WardState10526, _VARIANT_10526]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10527,
        ]
        | Annotated[_values.FormId, _VARIANT_10528]
        | Annotated[_values.FormId, _VARIANT_10529]
        | Annotated[_values.FormId, _VARIANT_10530]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_10532]
        | Annotated[bytes, _VARIANT_10533]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10534,
        ]
        | Annotated[float, _VARIANT_10535]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10536,
        ]
        | Annotated[Sex10537, _VARIANT_10537]
        | Annotated[ActorValue10538, _VARIANT_10538]
        | Annotated[CrimeType10539, _VARIANT_10539]
        | Annotated[Axis10540, _VARIANT_10540]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10541,
        ]
        | Annotated[MiscStat10542, _VARIANT_10542]
        | Annotated[Alignment10543, _VARIANT_10543]
        | Annotated[_values.FormId, _VARIANT_10544]
        | Annotated[FormType10545, _VARIANT_10545]
        | Annotated[CriticalStage10546, _VARIANT_10546]
        | Annotated[_values.FormId, _VARIANT_10547]
        | Annotated[_values.FormId, _VARIANT_10548]
        | Annotated[_values.FormId, _VARIANT_10549]
        | Annotated[_values.FormId, _VARIANT_10550]
        | Annotated[_values.FormId, _VARIANT_10551]
        | Annotated[_values.FormId, _VARIANT_10552]
        | Annotated[_values.FormId, _VARIANT_10553]
        | Annotated[_values.FormId, _VARIANT_10554]
        | Annotated[_values.FormId, _VARIANT_10555]
        | Annotated[_values.FormId, _VARIANT_10556]
        | Annotated[_values.FormId, _VARIANT_10557]
        | Annotated[_values.FormId, _VARIANT_10558]
        | Annotated[_values.FormId, _VARIANT_10559]
        | Annotated[_values.FormId, _VARIANT_10560]
        | Annotated[_values.FormId, _VARIANT_10561]
        | Annotated[_values.FormId, _VARIANT_10562]
        | Annotated[_values.FormId, _VARIANT_10563]
        | Annotated[_values.FormId, _VARIANT_10564]
        | Annotated[_values.FormId, _VARIANT_10565]
        | Annotated[_values.FormId, _VARIANT_10566]
        | Annotated[_values.FormId, _VARIANT_10567]
        | Annotated[_values.FormId, _VARIANT_10568]
        | Annotated[VatsValueFunction10569, _VARIANT_10569]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_10571]
            | Annotated[_values.FormId, _VARIANT_10572]
            | Annotated[_values.FormId, _VARIANT_10573]
            | Annotated[_values.FormId, _VARIANT_10574]
            | Annotated[bytes, _VARIANT_10575]
            | Annotated[TargetPart10576, _VARIANT_10576]
            | Annotated[VatsAction10577, _VARIANT_10577]
            | Annotated[bytes, _VARIANT_10578]
            | Annotated[bytes, _VARIANT_10579]
            | Annotated[_values.FormId, _VARIANT_10580]
            | Annotated[_values.FormId, _VARIANT_10581]
            | Annotated[bytes, _VARIANT_10582]
            | Annotated[bytes, _VARIANT_10583]
            | Annotated[bytes, _VARIANT_10584]
            | Annotated[bytes, _VARIANT_10585]
            | Annotated[WeaponType10586, _VARIANT_10586]
            | Annotated[bytes, _VARIANT_10587]
            | Annotated[bytes, _VARIANT_10588]
            | Annotated[ProjectileType10589, _VARIANT_10589]
            | Annotated[DeliveryType10590, _VARIANT_10590]
            | Annotated[CastingType10591, _VARIANT_10591],
            _VARIANT_10570,
        ]
        | Annotated[_values.FormId, _VARIANT_10592]
        | Annotated[_values.FormId, _VARIANT_10593]
        | Annotated[_values.FormId, _VARIANT_10594]
        | Annotated[PlayerAction10595, _VARIANT_10595]
        | Annotated[CastingType10596, _VARIANT_10596]
        | Annotated[_values.FormId, _VARIANT_10597]
        | Annotated[_values.FormId, _VARIANT_10598]
        | Annotated[_values.FormId, _VARIANT_10599]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10600,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10601,
        ]
        | Annotated[_values.FormId, _VARIANT_10602]
        | Annotated[FurnitureAnim10603, _VARIANT_10603]
        | Annotated[FurnitureEntry10604, _VARIANT_10604]
        | Annotated[_values.FormId, _VARIANT_10605]
        | Annotated[WardState10606, _VARIANT_10606]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10607,
        ]
        | Annotated[_values.FormId, _VARIANT_10608]
        | Annotated[_values.FormId, _VARIANT_10609]
        | Annotated[_values.FormId, _VARIANT_10610]
    )
    """Value decoded from this schema node."""

    run_on: RunOn10611
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10613,
        ]
        | Annotated[_values.FormId, _VARIANT_10614]
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
        Annotated[float, _VARIANT_10468]
        | Annotated[_values.FormId, _VARIANT_10469]
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
    def field(self, name: Literal["unused_10471"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_10473]
        | Annotated[bytes, _VARIANT_10474]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10475,
        ]
        | Annotated[float, _VARIANT_10476]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10477,
        ]
        | Annotated[Sex10478, _VARIANT_10478]
        | Annotated[ActorValue10479, _VARIANT_10479]
        | Annotated[CrimeType10480, _VARIANT_10480]
        | Annotated[Axis10481, _VARIANT_10481]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10482,
        ]
        | Annotated[MiscStat10483, _VARIANT_10483]
        | Annotated[Alignment10484, _VARIANT_10484]
        | Annotated[_values.FormId, _VARIANT_10485]
        | Annotated[FormType10486, _VARIANT_10486]
        | Annotated[CriticalStage10487, _VARIANT_10487]
        | Annotated[_values.FormId, _VARIANT_10488]
        | Annotated[_values.FormId, _VARIANT_10489]
        | Annotated[_values.FormId, _VARIANT_10490]
        | Annotated[_values.FormId, _VARIANT_10491]
        | Annotated[_values.FormId, _VARIANT_10492]
        | Annotated[_values.FormId, _VARIANT_10493]
        | Annotated[_values.FormId, _VARIANT_10494]
        | Annotated[_values.FormId, _VARIANT_10495]
        | Annotated[_values.FormId, _VARIANT_10496]
        | Annotated[_values.FormId, _VARIANT_10497]
        | Annotated[_values.FormId, _VARIANT_10498]
        | Annotated[_values.FormId, _VARIANT_10499]
        | Annotated[_values.FormId, _VARIANT_10500]
        | Annotated[_values.FormId, _VARIANT_10501]
        | Annotated[_values.FormId, _VARIANT_10502]
        | Annotated[_values.FormId, _VARIANT_10503]
        | Annotated[_values.FormId, _VARIANT_10504]
        | Annotated[_values.FormId, _VARIANT_10505]
        | Annotated[_values.FormId, _VARIANT_10506]
        | Annotated[_values.FormId, _VARIANT_10507]
        | Annotated[_values.FormId, _VARIANT_10508]
        | Annotated[_values.FormId, _VARIANT_10509]
        | Annotated[VatsValueFunction10510, _VARIANT_10510]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10511,
        ]
        | Annotated[_values.FormId, _VARIANT_10512]
        | Annotated[_values.FormId, _VARIANT_10513]
        | Annotated[_values.FormId, _VARIANT_10514]
        | Annotated[PlayerAction10515, _VARIANT_10515]
        | Annotated[CastingType10516, _VARIANT_10516]
        | Annotated[_values.FormId, _VARIANT_10517]
        | Annotated[_values.FormId, _VARIANT_10518]
        | Annotated[_values.FormId, _VARIANT_10519]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10520,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10521,
        ]
        | Annotated[_values.FormId, _VARIANT_10522]
        | Annotated[FurnitureAnim10523, _VARIANT_10523]
        | Annotated[FurnitureEntry10524, _VARIANT_10524]
        | Annotated[_values.FormId, _VARIANT_10525]
        | Annotated[WardState10526, _VARIANT_10526]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10527,
        ]
        | Annotated[_values.FormId, _VARIANT_10528]
        | Annotated[_values.FormId, _VARIANT_10529]
        | Annotated[_values.FormId, _VARIANT_10530]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_10532]
        | Annotated[bytes, _VARIANT_10533]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10534,
        ]
        | Annotated[float, _VARIANT_10535]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10536,
        ]
        | Annotated[Sex10537, _VARIANT_10537]
        | Annotated[ActorValue10538, _VARIANT_10538]
        | Annotated[CrimeType10539, _VARIANT_10539]
        | Annotated[Axis10540, _VARIANT_10540]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10541,
        ]
        | Annotated[MiscStat10542, _VARIANT_10542]
        | Annotated[Alignment10543, _VARIANT_10543]
        | Annotated[_values.FormId, _VARIANT_10544]
        | Annotated[FormType10545, _VARIANT_10545]
        | Annotated[CriticalStage10546, _VARIANT_10546]
        | Annotated[_values.FormId, _VARIANT_10547]
        | Annotated[_values.FormId, _VARIANT_10548]
        | Annotated[_values.FormId, _VARIANT_10549]
        | Annotated[_values.FormId, _VARIANT_10550]
        | Annotated[_values.FormId, _VARIANT_10551]
        | Annotated[_values.FormId, _VARIANT_10552]
        | Annotated[_values.FormId, _VARIANT_10553]
        | Annotated[_values.FormId, _VARIANT_10554]
        | Annotated[_values.FormId, _VARIANT_10555]
        | Annotated[_values.FormId, _VARIANT_10556]
        | Annotated[_values.FormId, _VARIANT_10557]
        | Annotated[_values.FormId, _VARIANT_10558]
        | Annotated[_values.FormId, _VARIANT_10559]
        | Annotated[_values.FormId, _VARIANT_10560]
        | Annotated[_values.FormId, _VARIANT_10561]
        | Annotated[_values.FormId, _VARIANT_10562]
        | Annotated[_values.FormId, _VARIANT_10563]
        | Annotated[_values.FormId, _VARIANT_10564]
        | Annotated[_values.FormId, _VARIANT_10565]
        | Annotated[_values.FormId, _VARIANT_10566]
        | Annotated[_values.FormId, _VARIANT_10567]
        | Annotated[_values.FormId, _VARIANT_10568]
        | Annotated[VatsValueFunction10569, _VARIANT_10569]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_10571]
            | Annotated[_values.FormId, _VARIANT_10572]
            | Annotated[_values.FormId, _VARIANT_10573]
            | Annotated[_values.FormId, _VARIANT_10574]
            | Annotated[bytes, _VARIANT_10575]
            | Annotated[TargetPart10576, _VARIANT_10576]
            | Annotated[VatsAction10577, _VARIANT_10577]
            | Annotated[bytes, _VARIANT_10578]
            | Annotated[bytes, _VARIANT_10579]
            | Annotated[_values.FormId, _VARIANT_10580]
            | Annotated[_values.FormId, _VARIANT_10581]
            | Annotated[bytes, _VARIANT_10582]
            | Annotated[bytes, _VARIANT_10583]
            | Annotated[bytes, _VARIANT_10584]
            | Annotated[bytes, _VARIANT_10585]
            | Annotated[WeaponType10586, _VARIANT_10586]
            | Annotated[bytes, _VARIANT_10587]
            | Annotated[bytes, _VARIANT_10588]
            | Annotated[ProjectileType10589, _VARIANT_10589]
            | Annotated[DeliveryType10590, _VARIANT_10590]
            | Annotated[CastingType10591, _VARIANT_10591],
            _VARIANT_10570,
        ]
        | Annotated[_values.FormId, _VARIANT_10592]
        | Annotated[_values.FormId, _VARIANT_10593]
        | Annotated[_values.FormId, _VARIANT_10594]
        | Annotated[PlayerAction10595, _VARIANT_10595]
        | Annotated[CastingType10596, _VARIANT_10596]
        | Annotated[_values.FormId, _VARIANT_10597]
        | Annotated[_values.FormId, _VARIANT_10598]
        | Annotated[_values.FormId, _VARIANT_10599]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10600,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10601,
        ]
        | Annotated[_values.FormId, _VARIANT_10602]
        | Annotated[FurnitureAnim10603, _VARIANT_10603]
        | Annotated[FurnitureEntry10604, _VARIANT_10604]
        | Annotated[_values.FormId, _VARIANT_10605]
        | Annotated[WardState10606, _VARIANT_10606]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10607,
        ]
        | Annotated[_values.FormId, _VARIANT_10608]
        | Annotated[_values.FormId, _VARIANT_10609]
        | Annotated[_values.FormId, _VARIANT_10610]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn10611]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10613,
        ]
        | Annotated[_values.FormId, _VARIANT_10614]
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


class Condition10462(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LSCR/3:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="LSCR/3:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("LSCR/3:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("LSCR/3:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure10464] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure10464]]:
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


class Structure10625(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LSCR/6:Initial Rotation/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="LSCR/6:Initial Rotation/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="LSCR/6:Initial Rotation/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="LSCR/6:Initial Rotation/payload/2:Z",
            kind="primitive",
            name="Z",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    z: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z"]
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


class Structure10630(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LSCR/7:Rotation Offset Constraints/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "min": _base.Binding(
            path="LSCR/7:Rotation Offset Constraints/payload/0:Min",
            kind="primitive",
            name="Min",
        ),
        "max": _base.Binding(
            path="LSCR/7:Rotation Offset Constraints/payload/1:Max",
            kind="primitive",
            name="Max",
        ),
    }

    min: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    max: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["min"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["max"]
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


class Structure10634(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LSCR/8:Initial Translation Offset/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="LSCR/8:Initial Translation Offset/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="LSCR/8:Initial Translation Offset/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="LSCR/8:Initial Translation Offset/payload/2:Z",
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


class LoadScreenRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LSCR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LSCR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LSCR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "icon": _base.Binding(
            path="LSCR/1:Icon",
            kind="unordered",
            name="Icon",
        ),
        "description": _base.Binding(
            path="LSCR/2:Description",
            kind="subrecord",
            name="Description",
        ),
        "conditions": _base.Binding(
            path="LSCR/3:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="LSCR/3:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "loading_screen_nif": _base.Binding(
            path="LSCR/4:Loading Screen NIF",
            kind="subrecord",
            name="Loading Screen NIF",
        ),
        "initial_scale": _base.Binding(
            path="LSCR/5:Initial Scale",
            kind="subrecord",
            name="Initial Scale",
        ),
        "initial_rotation": _base.Binding(
            path="LSCR/6:Initial Rotation",
            kind="subrecord",
            name="Initial Rotation",
        ),
        "rotation_offset_constraints": _base.Binding(
            path="LSCR/7:Rotation Offset Constraints",
            kind="subrecord",
            name="Rotation Offset Constraints",
        ),
        "initial_translation_offset": _base.Binding(
            path="LSCR/8:Initial Translation Offset",
            kind="subrecord",
            name="Initial Translation Offset",
        ),
        "camera_path": _base.Binding(
            path="LSCR/9:Camera Path",
            kind="subrecord",
            name="Camera Path",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    icon: Optional[Icon10454] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition10462, ...] = ()
    """Value decoded from this schema node."""

    loading_screen_nif: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    initial_scale: Optional[float] = None
    """Value decoded from this schema node."""

    initial_rotation: Optional[Structure10625] = None
    """Value decoded from this schema node."""

    rotation_offset_constraints: Optional[Structure10630] = None
    """Value decoded from this schema node."""

    initial_translation_offset: Optional[Structure10634] = None
    """Value decoded from this schema node."""

    camera_path: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["icon"]
    ) -> _base.FieldRef[Optional[Icon10454]]:
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
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition10462, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["loading_screen_nif"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["initial_scale"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["initial_rotation"]
    ) -> _base.FieldRef[Optional[Structure10625]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotation_offset_constraints"]
    ) -> _base.FieldRef[Optional[Structure10630]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["initial_translation_offset"]
    ) -> _base.FieldRef[Optional[Structure10634]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["camera_path"]
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
