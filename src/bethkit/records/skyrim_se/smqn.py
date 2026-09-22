"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values

_VARIANT_7368: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_7369: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_7373: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_7374: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/1:None"
    )
)


_VARIANT_7375: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/2:Integer"
    )
)


_VARIANT_7376: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/3:Float"
    )
)


_VARIANT_7377: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/4:Variable Name"
    )
)


class Sex7378(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_7378: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/5:Sex"
    )
)


class ActorValue7379(_values.OpenIntEnum):
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


_VARIANT_7379: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType7380(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_7380: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/7:Crime Type"
    )
)


class Axis7381(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_7381: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/8:Axis"
    )
)


_VARIANT_7382: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat7383(_values.OpenIntEnum):
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


_VARIANT_7383: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment7384(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_7384: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_7385: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/12:Equip Type"
    )
)


class FormType7386(_values.OpenIntEnum):
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


_VARIANT_7386: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage7387(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_7387: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_7388: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_7389: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_7390: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/17:Actor"
    )
)


_VARIANT_7391: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_7392: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/19:Idle"
    )
)


_VARIANT_7393: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/20:Form List"
    )
)


_VARIANT_7394: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/21:Quest"
    )
)


_VARIANT_7395: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/22:Faction"
    )
)


_VARIANT_7396: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/23:Cell"
    )
)


_VARIANT_7397: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/24:Class"
    )
)


_VARIANT_7398: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/25:Race"
    )
)


_VARIANT_7399: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_7400: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/27:Global"
    )
)


_VARIANT_7401: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/28:Weather"
    )
)


_VARIANT_7402: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/29:Package"
    )
)


_VARIANT_7403: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_7404: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/31:Perk"
    )
)


_VARIANT_7405: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/32:Owner"
    )
)


_VARIANT_7406: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_7407: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_7408: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_7409: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction7410(_values.OpenIntEnum):
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


_VARIANT_7410: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_7411: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_7412: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_7413: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/40:Region"
    )
)


_VARIANT_7414: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction7415(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_7415: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/42:Player Action"
    )
)


class CastingType7416(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_7416: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_7417: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/44:Shout"
    )
)


_VARIANT_7418: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/45:Location"
    )
)


_VARIANT_7419: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_7420: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/47:Alias"
    )
)


_VARIANT_7421: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_7422: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim7423(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_7423: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry7424(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_7424: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_7425: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/52:Scene"
    )
)


class WardState7426(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_7426: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_7427: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/54:Event"
    )
)


_VARIANT_7428: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_7429: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_7430: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/57:Faction"
    )
)


_VARIANT_7432: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_7433: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/1:None"
    )
)


_VARIANT_7434: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/2:Integer"
    )
)


_VARIANT_7435: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/3:Float"
    )
)


_VARIANT_7436: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/4:Variable Name"
    )
)


class Sex7437(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_7437: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/5:Sex"
    )
)


class ActorValue7438(_values.OpenIntEnum):
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


_VARIANT_7438: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType7439(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_7439: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/7:Crime Type"
    )
)


class Axis7440(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_7440: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/8:Axis"
    )
)


_VARIANT_7441: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat7442(_values.OpenIntEnum):
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


_VARIANT_7442: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment7443(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_7443: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_7444: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/12:Equip Type"
    )
)


class FormType7445(_values.OpenIntEnum):
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


_VARIANT_7445: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage7446(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_7446: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_7447: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_7448: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_7449: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/17:Actor"
    )
)


_VARIANT_7450: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_7451: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/19:Idle"
    )
)


_VARIANT_7452: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/20:Form List"
    )
)


_VARIANT_7453: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/21:Quest"
    )
)


_VARIANT_7454: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/22:Faction"
    )
)


_VARIANT_7455: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/23:Cell"
    )
)


_VARIANT_7456: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/24:Class"
    )
)


_VARIANT_7457: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/25:Race"
    )
)


_VARIANT_7458: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_7459: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/27:Global"
    )
)


_VARIANT_7460: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/28:Weather"
    )
)


_VARIANT_7461: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/29:Package"
    )
)


_VARIANT_7462: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_7463: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/31:Perk"
    )
)


_VARIANT_7464: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/32:Owner"
    )
)


_VARIANT_7465: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_7466: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_7467: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_7468: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction7469(_values.OpenIntEnum):
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


_VARIANT_7469: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_7471: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/0:W"
        "eapon"
    )
)


_VARIANT_7472: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/1:W"
        "eapon List"
    )
)


_VARIANT_7473: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/2:T"
        "arget"
    )
)


_VARIANT_7474: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/3:T"
        "arget List"
    )
)


_VARIANT_7475: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/4:U"
        "nknown"
    )
)


class TargetPart7476(_values.OpenIntEnum):
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


_VARIANT_7476: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/5:T"
        "arget Part"
    )
)


class VatsAction7477(_values.OpenIntEnum):
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


_VARIANT_7477: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/6:V"
        "ATS Action"
    )
)


_VARIANT_7478: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/7:U"
        "nknown"
    )
)


_VARIANT_7479: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/8:U"
        "nknown"
    )
)


_VARIANT_7480: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/9:C"
        "ritical Effect"
    )
)


_VARIANT_7481: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/10:"
        "Critical Effect List"
    )
)


_VARIANT_7482: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/11:"
        "Unknown"
    )
)


_VARIANT_7483: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/12:"
        "Unknown"
    )
)


_VARIANT_7484: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/13:"
        "Unknown"
    )
)


_VARIANT_7485: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/14:"
        "Unknown"
    )
)


class WeaponType7486(_values.OpenIntEnum):
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


_VARIANT_7486: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/15:"
        "Weapon Type"
    )
)


_VARIANT_7487: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/16:"
        "Unknown"
    )
)


_VARIANT_7488: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/17:"
        "Unknown"
    )
)


class ProjectileType7489(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_7489: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/18:"
        "Projectile Type"
    )
)


class DeliveryType7490(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_7490: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/19:"
        "Delivery Type"
    )
)


class CastingType7491(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_7491: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/20:"
        "Casting Type"
    )
)


_VARIANT_7470: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_7492: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_7493: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/40:Region"
    )
)


_VARIANT_7494: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction7495(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_7495: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/42:Player Action"
    )
)


class CastingType7496(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_7496: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_7497: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/44:Shout"
    )
)


_VARIANT_7498: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/45:Location"
    )
)


_VARIANT_7499: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_7500: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/47:Alias"
    )
)


_VARIANT_7501: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_7502: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim7503(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_7503: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry7504(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_7504: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_7505: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/52:Scene"
    )
)


class WardState7506(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_7506: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_7507: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/54:Event"
    )
)


_VARIANT_7508: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_7509: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_7510: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/57:Faction"
    )
)


class RunOn7511(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_7513: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/0:Unused"
    )
)


_VARIANT_7514: _base.Variant = _base.Variant(
    path=(
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/1:Reference"
    )
)


class Structure7364(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
                "Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_7371": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
                "Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
                "Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
                "Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "SMQN/4:Conditions/repeat/0:Condition/0:CTDA/payload/9:"
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
        Annotated[float, _VARIANT_7368]
        | Annotated[_values.FormId, _VARIANT_7369]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_7371: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_7373]
        | Annotated[bytes, _VARIANT_7374]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7375,
        ]
        | Annotated[float, _VARIANT_7376]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7377,
        ]
        | Annotated[Sex7378, _VARIANT_7378]
        | Annotated[ActorValue7379, _VARIANT_7379]
        | Annotated[CrimeType7380, _VARIANT_7380]
        | Annotated[Axis7381, _VARIANT_7381]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7382,
        ]
        | Annotated[MiscStat7383, _VARIANT_7383]
        | Annotated[Alignment7384, _VARIANT_7384]
        | Annotated[_values.FormId, _VARIANT_7385]
        | Annotated[FormType7386, _VARIANT_7386]
        | Annotated[CriticalStage7387, _VARIANT_7387]
        | Annotated[_values.FormId, _VARIANT_7388]
        | Annotated[_values.FormId, _VARIANT_7389]
        | Annotated[_values.FormId, _VARIANT_7390]
        | Annotated[_values.FormId, _VARIANT_7391]
        | Annotated[_values.FormId, _VARIANT_7392]
        | Annotated[_values.FormId, _VARIANT_7393]
        | Annotated[_values.FormId, _VARIANT_7394]
        | Annotated[_values.FormId, _VARIANT_7395]
        | Annotated[_values.FormId, _VARIANT_7396]
        | Annotated[_values.FormId, _VARIANT_7397]
        | Annotated[_values.FormId, _VARIANT_7398]
        | Annotated[_values.FormId, _VARIANT_7399]
        | Annotated[_values.FormId, _VARIANT_7400]
        | Annotated[_values.FormId, _VARIANT_7401]
        | Annotated[_values.FormId, _VARIANT_7402]
        | Annotated[_values.FormId, _VARIANT_7403]
        | Annotated[_values.FormId, _VARIANT_7404]
        | Annotated[_values.FormId, _VARIANT_7405]
        | Annotated[_values.FormId, _VARIANT_7406]
        | Annotated[_values.FormId, _VARIANT_7407]
        | Annotated[_values.FormId, _VARIANT_7408]
        | Annotated[_values.FormId, _VARIANT_7409]
        | Annotated[VatsValueFunction7410, _VARIANT_7410]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7411,
        ]
        | Annotated[_values.FormId, _VARIANT_7412]
        | Annotated[_values.FormId, _VARIANT_7413]
        | Annotated[_values.FormId, _VARIANT_7414]
        | Annotated[PlayerAction7415, _VARIANT_7415]
        | Annotated[CastingType7416, _VARIANT_7416]
        | Annotated[_values.FormId, _VARIANT_7417]
        | Annotated[_values.FormId, _VARIANT_7418]
        | Annotated[_values.FormId, _VARIANT_7419]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7420,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7421,
        ]
        | Annotated[_values.FormId, _VARIANT_7422]
        | Annotated[FurnitureAnim7423, _VARIANT_7423]
        | Annotated[FurnitureEntry7424, _VARIANT_7424]
        | Annotated[_values.FormId, _VARIANT_7425]
        | Annotated[WardState7426, _VARIANT_7426]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7427,
        ]
        | Annotated[_values.FormId, _VARIANT_7428]
        | Annotated[_values.FormId, _VARIANT_7429]
        | Annotated[_values.FormId, _VARIANT_7430]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_7432]
        | Annotated[bytes, _VARIANT_7433]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7434,
        ]
        | Annotated[float, _VARIANT_7435]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7436,
        ]
        | Annotated[Sex7437, _VARIANT_7437]
        | Annotated[ActorValue7438, _VARIANT_7438]
        | Annotated[CrimeType7439, _VARIANT_7439]
        | Annotated[Axis7440, _VARIANT_7440]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7441,
        ]
        | Annotated[MiscStat7442, _VARIANT_7442]
        | Annotated[Alignment7443, _VARIANT_7443]
        | Annotated[_values.FormId, _VARIANT_7444]
        | Annotated[FormType7445, _VARIANT_7445]
        | Annotated[CriticalStage7446, _VARIANT_7446]
        | Annotated[_values.FormId, _VARIANT_7447]
        | Annotated[_values.FormId, _VARIANT_7448]
        | Annotated[_values.FormId, _VARIANT_7449]
        | Annotated[_values.FormId, _VARIANT_7450]
        | Annotated[_values.FormId, _VARIANT_7451]
        | Annotated[_values.FormId, _VARIANT_7452]
        | Annotated[_values.FormId, _VARIANT_7453]
        | Annotated[_values.FormId, _VARIANT_7454]
        | Annotated[_values.FormId, _VARIANT_7455]
        | Annotated[_values.FormId, _VARIANT_7456]
        | Annotated[_values.FormId, _VARIANT_7457]
        | Annotated[_values.FormId, _VARIANT_7458]
        | Annotated[_values.FormId, _VARIANT_7459]
        | Annotated[_values.FormId, _VARIANT_7460]
        | Annotated[_values.FormId, _VARIANT_7461]
        | Annotated[_values.FormId, _VARIANT_7462]
        | Annotated[_values.FormId, _VARIANT_7463]
        | Annotated[_values.FormId, _VARIANT_7464]
        | Annotated[_values.FormId, _VARIANT_7465]
        | Annotated[_values.FormId, _VARIANT_7466]
        | Annotated[_values.FormId, _VARIANT_7467]
        | Annotated[_values.FormId, _VARIANT_7468]
        | Annotated[VatsValueFunction7469, _VARIANT_7469]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_7471]
            | Annotated[_values.FormId, _VARIANT_7472]
            | Annotated[_values.FormId, _VARIANT_7473]
            | Annotated[_values.FormId, _VARIANT_7474]
            | Annotated[bytes, _VARIANT_7475]
            | Annotated[TargetPart7476, _VARIANT_7476]
            | Annotated[VatsAction7477, _VARIANT_7477]
            | Annotated[bytes, _VARIANT_7478]
            | Annotated[bytes, _VARIANT_7479]
            | Annotated[_values.FormId, _VARIANT_7480]
            | Annotated[_values.FormId, _VARIANT_7481]
            | Annotated[bytes, _VARIANT_7482]
            | Annotated[bytes, _VARIANT_7483]
            | Annotated[bytes, _VARIANT_7484]
            | Annotated[bytes, _VARIANT_7485]
            | Annotated[WeaponType7486, _VARIANT_7486]
            | Annotated[bytes, _VARIANT_7487]
            | Annotated[bytes, _VARIANT_7488]
            | Annotated[ProjectileType7489, _VARIANT_7489]
            | Annotated[DeliveryType7490, _VARIANT_7490]
            | Annotated[CastingType7491, _VARIANT_7491],
            _VARIANT_7470,
        ]
        | Annotated[_values.FormId, _VARIANT_7492]
        | Annotated[_values.FormId, _VARIANT_7493]
        | Annotated[_values.FormId, _VARIANT_7494]
        | Annotated[PlayerAction7495, _VARIANT_7495]
        | Annotated[CastingType7496, _VARIANT_7496]
        | Annotated[_values.FormId, _VARIANT_7497]
        | Annotated[_values.FormId, _VARIANT_7498]
        | Annotated[_values.FormId, _VARIANT_7499]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7500,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7501,
        ]
        | Annotated[_values.FormId, _VARIANT_7502]
        | Annotated[FurnitureAnim7503, _VARIANT_7503]
        | Annotated[FurnitureEntry7504, _VARIANT_7504]
        | Annotated[_values.FormId, _VARIANT_7505]
        | Annotated[WardState7506, _VARIANT_7506]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7507,
        ]
        | Annotated[_values.FormId, _VARIANT_7508]
        | Annotated[_values.FormId, _VARIANT_7509]
        | Annotated[_values.FormId, _VARIANT_7510]
    )
    """Value decoded from this schema node."""

    run_on: RunOn7511
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7513,
        ]
        | Annotated[_values.FormId, _VARIANT_7514]
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
        Annotated[float, _VARIANT_7368]
        | Annotated[_values.FormId, _VARIANT_7369]
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
    def field(self, name: Literal["unused_7371"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_7373]
        | Annotated[bytes, _VARIANT_7374]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7375,
        ]
        | Annotated[float, _VARIANT_7376]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7377,
        ]
        | Annotated[Sex7378, _VARIANT_7378]
        | Annotated[ActorValue7379, _VARIANT_7379]
        | Annotated[CrimeType7380, _VARIANT_7380]
        | Annotated[Axis7381, _VARIANT_7381]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7382,
        ]
        | Annotated[MiscStat7383, _VARIANT_7383]
        | Annotated[Alignment7384, _VARIANT_7384]
        | Annotated[_values.FormId, _VARIANT_7385]
        | Annotated[FormType7386, _VARIANT_7386]
        | Annotated[CriticalStage7387, _VARIANT_7387]
        | Annotated[_values.FormId, _VARIANT_7388]
        | Annotated[_values.FormId, _VARIANT_7389]
        | Annotated[_values.FormId, _VARIANT_7390]
        | Annotated[_values.FormId, _VARIANT_7391]
        | Annotated[_values.FormId, _VARIANT_7392]
        | Annotated[_values.FormId, _VARIANT_7393]
        | Annotated[_values.FormId, _VARIANT_7394]
        | Annotated[_values.FormId, _VARIANT_7395]
        | Annotated[_values.FormId, _VARIANT_7396]
        | Annotated[_values.FormId, _VARIANT_7397]
        | Annotated[_values.FormId, _VARIANT_7398]
        | Annotated[_values.FormId, _VARIANT_7399]
        | Annotated[_values.FormId, _VARIANT_7400]
        | Annotated[_values.FormId, _VARIANT_7401]
        | Annotated[_values.FormId, _VARIANT_7402]
        | Annotated[_values.FormId, _VARIANT_7403]
        | Annotated[_values.FormId, _VARIANT_7404]
        | Annotated[_values.FormId, _VARIANT_7405]
        | Annotated[_values.FormId, _VARIANT_7406]
        | Annotated[_values.FormId, _VARIANT_7407]
        | Annotated[_values.FormId, _VARIANT_7408]
        | Annotated[_values.FormId, _VARIANT_7409]
        | Annotated[VatsValueFunction7410, _VARIANT_7410]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7411,
        ]
        | Annotated[_values.FormId, _VARIANT_7412]
        | Annotated[_values.FormId, _VARIANT_7413]
        | Annotated[_values.FormId, _VARIANT_7414]
        | Annotated[PlayerAction7415, _VARIANT_7415]
        | Annotated[CastingType7416, _VARIANT_7416]
        | Annotated[_values.FormId, _VARIANT_7417]
        | Annotated[_values.FormId, _VARIANT_7418]
        | Annotated[_values.FormId, _VARIANT_7419]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7420,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7421,
        ]
        | Annotated[_values.FormId, _VARIANT_7422]
        | Annotated[FurnitureAnim7423, _VARIANT_7423]
        | Annotated[FurnitureEntry7424, _VARIANT_7424]
        | Annotated[_values.FormId, _VARIANT_7425]
        | Annotated[WardState7426, _VARIANT_7426]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7427,
        ]
        | Annotated[_values.FormId, _VARIANT_7428]
        | Annotated[_values.FormId, _VARIANT_7429]
        | Annotated[_values.FormId, _VARIANT_7430]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_7432]
        | Annotated[bytes, _VARIANT_7433]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7434,
        ]
        | Annotated[float, _VARIANT_7435]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7436,
        ]
        | Annotated[Sex7437, _VARIANT_7437]
        | Annotated[ActorValue7438, _VARIANT_7438]
        | Annotated[CrimeType7439, _VARIANT_7439]
        | Annotated[Axis7440, _VARIANT_7440]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7441,
        ]
        | Annotated[MiscStat7442, _VARIANT_7442]
        | Annotated[Alignment7443, _VARIANT_7443]
        | Annotated[_values.FormId, _VARIANT_7444]
        | Annotated[FormType7445, _VARIANT_7445]
        | Annotated[CriticalStage7446, _VARIANT_7446]
        | Annotated[_values.FormId, _VARIANT_7447]
        | Annotated[_values.FormId, _VARIANT_7448]
        | Annotated[_values.FormId, _VARIANT_7449]
        | Annotated[_values.FormId, _VARIANT_7450]
        | Annotated[_values.FormId, _VARIANT_7451]
        | Annotated[_values.FormId, _VARIANT_7452]
        | Annotated[_values.FormId, _VARIANT_7453]
        | Annotated[_values.FormId, _VARIANT_7454]
        | Annotated[_values.FormId, _VARIANT_7455]
        | Annotated[_values.FormId, _VARIANT_7456]
        | Annotated[_values.FormId, _VARIANT_7457]
        | Annotated[_values.FormId, _VARIANT_7458]
        | Annotated[_values.FormId, _VARIANT_7459]
        | Annotated[_values.FormId, _VARIANT_7460]
        | Annotated[_values.FormId, _VARIANT_7461]
        | Annotated[_values.FormId, _VARIANT_7462]
        | Annotated[_values.FormId, _VARIANT_7463]
        | Annotated[_values.FormId, _VARIANT_7464]
        | Annotated[_values.FormId, _VARIANT_7465]
        | Annotated[_values.FormId, _VARIANT_7466]
        | Annotated[_values.FormId, _VARIANT_7467]
        | Annotated[_values.FormId, _VARIANT_7468]
        | Annotated[VatsValueFunction7469, _VARIANT_7469]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_7471]
            | Annotated[_values.FormId, _VARIANT_7472]
            | Annotated[_values.FormId, _VARIANT_7473]
            | Annotated[_values.FormId, _VARIANT_7474]
            | Annotated[bytes, _VARIANT_7475]
            | Annotated[TargetPart7476, _VARIANT_7476]
            | Annotated[VatsAction7477, _VARIANT_7477]
            | Annotated[bytes, _VARIANT_7478]
            | Annotated[bytes, _VARIANT_7479]
            | Annotated[_values.FormId, _VARIANT_7480]
            | Annotated[_values.FormId, _VARIANT_7481]
            | Annotated[bytes, _VARIANT_7482]
            | Annotated[bytes, _VARIANT_7483]
            | Annotated[bytes, _VARIANT_7484]
            | Annotated[bytes, _VARIANT_7485]
            | Annotated[WeaponType7486, _VARIANT_7486]
            | Annotated[bytes, _VARIANT_7487]
            | Annotated[bytes, _VARIANT_7488]
            | Annotated[ProjectileType7489, _VARIANT_7489]
            | Annotated[DeliveryType7490, _VARIANT_7490]
            | Annotated[CastingType7491, _VARIANT_7491],
            _VARIANT_7470,
        ]
        | Annotated[_values.FormId, _VARIANT_7492]
        | Annotated[_values.FormId, _VARIANT_7493]
        | Annotated[_values.FormId, _VARIANT_7494]
        | Annotated[PlayerAction7495, _VARIANT_7495]
        | Annotated[CastingType7496, _VARIANT_7496]
        | Annotated[_values.FormId, _VARIANT_7497]
        | Annotated[_values.FormId, _VARIANT_7498]
        | Annotated[_values.FormId, _VARIANT_7499]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7500,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7501,
        ]
        | Annotated[_values.FormId, _VARIANT_7502]
        | Annotated[FurnitureAnim7503, _VARIANT_7503]
        | Annotated[FurnitureEntry7504, _VARIANT_7504]
        | Annotated[_values.FormId, _VARIANT_7505]
        | Annotated[WardState7506, _VARIANT_7506]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7507,
        ]
        | Annotated[_values.FormId, _VARIANT_7508]
        | Annotated[_values.FormId, _VARIANT_7509]
        | Annotated[_values.FormId, _VARIANT_7510]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn7511]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_7513,
        ]
        | Annotated[_values.FormId, _VARIANT_7514]
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


class Condition7362(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SMQN/4:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="SMQN/4:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("SMQN/4:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("SMQN/4:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure7364] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure7364]]:
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


class NodeFlags7522(enum.IntFlag):
    """Named values from the pinned schema."""

    RANDOM = 1
    WARN_IF_NO_CHILD_QUEST_STARTED = 2


class QuestFlags7523(enum.IntFlag):
    """Named values from the pinned schema."""

    DO_ALL_BEFORE_REPEATING = 1
    SHARES_EVENT = 2
    NUM_QUESTS_TO_RUN = 4


class Structure7521(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SMQN/5:Flags/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "node_flags": _base.Binding(
            path="SMQN/5:Flags/payload/0:Node Flags",
            kind="primitive",
            name="Node Flags",
        ),
        "quest_flags": _base.Binding(
            path="SMQN/5:Flags/payload/1:Quest Flags",
            kind="primitive",
            name="Quest Flags",
        ),
    }

    node_flags: NodeFlags7522
    """Value decoded from this schema node."""

    quest_flags: QuestFlags7523
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["node_flags"]
    ) -> _base.FieldRef[NodeFlags7522]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["quest_flags"]
    ) -> _base.FieldRef[QuestFlags7523]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Unknown0Unknown1Unknown2Unknown3UnknoC6B3E5847535(enum.IntFlag):
    """Named values from the pinned schema."""

    UNKNOWN_0 = 1
    UNKNOWN_1 = 2
    UNKNOWN_2 = 4
    UNKNOWN_3 = 8
    UNKNOWN_4 = 16
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
    UNKNOWN_31 = 2147483648


class Quest7531(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SMQN/9:Quests/repeat/0:Quest"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "quest": _base.Binding(
            path="SMQN/9:Quests/repeat/0:Quest/0:Quest",
            kind="subrecord",
            name="Quest",
        ),
        "flags": _base.Binding(
            path="SMQN/9:Quests/repeat/0:Quest/1:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "hours_until_reset": _base.Binding(
            path="SMQN/9:Quests/repeat/0:Quest/2:Hours until reset",
            kind="subrecord",
            name="Hours until reset",
        ),
    }

    quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    flags: Optional[Unknown0Unknown1Unknown2Unknown3UnknoC6B3E5847535] = None
    """Value decoded from this schema node."""

    hours_until_reset: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["quest"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[Unknown0Unknown1Unknown2Unknown3UnknoC6B3E5847535]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hours_until_reset"]
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


class StoryManagerQuestNodeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SMQN"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SMQN"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SMQN/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "parent": _base.Binding(
            path="SMQN/1:Parent ",
            kind="subrecord",
            name="Parent ",
        ),
        "previous_sibling": _base.Binding(
            path="SMQN/2:Previous Sibling ",
            kind="subrecord",
            name="Previous Sibling ",
        ),
        "condition_count": _base.Binding(
            path="SMQN/3:Condition Count",
            kind="subrecord",
            name="Condition Count",
        ),
        "conditions": _base.Binding(
            path="SMQN/4:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="SMQN/4:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "flags": _base.Binding(
            path="SMQN/5:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "max_concurrent_quests": _base.Binding(
            path="SMQN/6:Max concurrent quests",
            kind="subrecord",
            name="Max concurrent quests",
        ),
        "num_quests_to_run": _base.Binding(
            path="SMQN/7:Num quests to run",
            kind="subrecord",
            name="Num quests to run",
        ),
        "quest_count": _base.Binding(
            path="SMQN/8:Quest Count",
            kind="subrecord",
            name="Quest Count",
        ),
        "quests": _base.Binding(
            path="SMQN/9:Quests",
            kind="repeat",
            name="Quests",
            repeated_path="SMQN/9:Quests/repeat/0:Quest",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    parent: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    previous_sibling: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    condition_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition7362, ...] = ()
    """Value decoded from this schema node."""

    flags: Optional[Structure7521] = None
    """Value decoded from this schema node."""

    max_concurrent_quests: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    num_quests_to_run: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    quest_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    quests: tuple[Quest7531, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parent"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["previous_sibling"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["condition_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition7362, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[Structure7521]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["max_concurrent_quests"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["num_quests_to_run"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["quest_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["quests"]
    ) -> _base.FieldRef[tuple[Quest7531, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
