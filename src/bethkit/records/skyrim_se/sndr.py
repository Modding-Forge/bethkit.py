"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Value8817(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    STANDARD = 519001098


class SoundFiles8823(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SNDR/4:Sounds/repeat/0:Sound Files"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_name": _base.Binding(
            path="SNDR/4:Sounds/repeat/0:Sound Files/0:File Name",
            kind="subrecord",
            name="File Name",
        ),
    }

    file_name: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_name"]
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


_VARIANT_8837: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_8838: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_8842: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_8843: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/1:None"
    )
)


_VARIANT_8844: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/2:Integer"
    )
)


_VARIANT_8845: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/3:Float"
    )
)


_VARIANT_8846: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/4:Variable Name"
    )
)


class Sex8847(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8847: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/5:Sex"
    )
)


class ActorValue8848(_values.OpenIntEnum):
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


_VARIANT_8848: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType8849(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8849: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/7:Crime Type"
    )
)


class Axis8850(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8850: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/8:Axis"
    )
)


_VARIANT_8851: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat8852(_values.OpenIntEnum):
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


_VARIANT_8852: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment8853(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8853: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_8854: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/12:Equip Type"
    )
)


class FormType8855(_values.OpenIntEnum):
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


_VARIANT_8855: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage8856(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8856: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_8857: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_8858: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_8859: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/17:Actor"
    )
)


_VARIANT_8860: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_8861: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/19:Idle"
    )
)


_VARIANT_8862: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/20:Form List"
    )
)


_VARIANT_8863: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/21:Quest"
    )
)


_VARIANT_8864: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/22:Faction"
    )
)


_VARIANT_8865: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/23:Cell"
    )
)


_VARIANT_8866: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/24:Class"
    )
)


_VARIANT_8867: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/25:Race"
    )
)


_VARIANT_8868: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_8869: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/27:Global"
    )
)


_VARIANT_8870: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/28:Weather"
    )
)


_VARIANT_8871: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/29:Package"
    )
)


_VARIANT_8872: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_8873: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/31:Perk"
    )
)


_VARIANT_8874: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/32:Owner"
    )
)


_VARIANT_8875: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_8876: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_8877: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_8878: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction8879(_values.OpenIntEnum):
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


_VARIANT_8879: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_8880: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_8881: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_8882: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/40:Region"
    )
)


_VARIANT_8883: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction8884(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8884: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/42:Player Action"
    )
)


class CastingType8885(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8885: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_8886: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/44:Shout"
    )
)


_VARIANT_8887: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/45:Location"
    )
)


_VARIANT_8888: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_8889: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/47:Alias"
    )
)


_VARIANT_8890: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_8891: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim8892(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8892: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8893(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8893: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_8894: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/52:Scene"
    )
)


class WardState8895(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8895: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_8896: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/54:Event"
    )
)


_VARIANT_8897: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_8898: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_8899: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/57:Faction"
    )
)


_VARIANT_8901: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_8902: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/1:None"
    )
)


_VARIANT_8903: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/2:Integer"
    )
)


_VARIANT_8904: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/3:Float"
    )
)


_VARIANT_8905: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/4:Variable Name"
    )
)


class Sex8906(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8906: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/5:Sex"
    )
)


class ActorValue8907(_values.OpenIntEnum):
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


_VARIANT_8907: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType8908(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8908: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/7:Crime Type"
    )
)


class Axis8909(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8909: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/8:Axis"
    )
)


_VARIANT_8910: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat8911(_values.OpenIntEnum):
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


_VARIANT_8911: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment8912(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8912: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_8913: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/12:Equip Type"
    )
)


class FormType8914(_values.OpenIntEnum):
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


_VARIANT_8914: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage8915(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8915: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_8916: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_8917: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_8918: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/17:Actor"
    )
)


_VARIANT_8919: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_8920: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/19:Idle"
    )
)


_VARIANT_8921: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/20:Form List"
    )
)


_VARIANT_8922: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/21:Quest"
    )
)


_VARIANT_8923: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/22:Faction"
    )
)


_VARIANT_8924: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/23:Cell"
    )
)


_VARIANT_8925: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/24:Class"
    )
)


_VARIANT_8926: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/25:Race"
    )
)


_VARIANT_8927: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_8928: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/27:Global"
    )
)


_VARIANT_8929: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/28:Weather"
    )
)


_VARIANT_8930: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/29:Package"
    )
)


_VARIANT_8931: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_8932: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/31:Perk"
    )
)


_VARIANT_8933: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/32:Owner"
    )
)


_VARIANT_8934: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_8935: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_8936: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_8937: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction8938(_values.OpenIntEnum):
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


_VARIANT_8938: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_8940: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/0:W"
        "eapon"
    )
)


_VARIANT_8941: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/1:W"
        "eapon List"
    )
)


_VARIANT_8942: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/2:T"
        "arget"
    )
)


_VARIANT_8943: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/3:T"
        "arget List"
    )
)


_VARIANT_8944: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/4:U"
        "nknown"
    )
)


class TargetPart8945(_values.OpenIntEnum):
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


_VARIANT_8945: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/5:T"
        "arget Part"
    )
)


class VatsAction8946(_values.OpenIntEnum):
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


_VARIANT_8946: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/6:V"
        "ATS Action"
    )
)


_VARIANT_8947: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/7:U"
        "nknown"
    )
)


_VARIANT_8948: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/8:U"
        "nknown"
    )
)


_VARIANT_8949: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/9:C"
        "ritical Effect"
    )
)


_VARIANT_8950: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/10:"
        "Critical Effect List"
    )
)


_VARIANT_8951: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/11:"
        "Unknown"
    )
)


_VARIANT_8952: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/12:"
        "Unknown"
    )
)


_VARIANT_8953: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/13:"
        "Unknown"
    )
)


_VARIANT_8954: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/14:"
        "Unknown"
    )
)


class WeaponType8955(_values.OpenIntEnum):
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


_VARIANT_8955: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/15:"
        "Weapon Type"
    )
)


_VARIANT_8956: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/16:"
        "Unknown"
    )
)


_VARIANT_8957: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/17:"
        "Unknown"
    )
)


class ProjectileType8958(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_8958: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/18:"
        "Projectile Type"
    )
)


class DeliveryType8959(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_8959: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/19:"
        "Delivery Type"
    )
)


class CastingType8960(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_8960: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/20:"
        "Casting Type"
    )
)


_VARIANT_8939: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_8961: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_8962: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/40:Region"
    )
)


_VARIANT_8963: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction8964(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8964: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/42:Player Action"
    )
)


class CastingType8965(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8965: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_8966: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/44:Shout"
    )
)


_VARIANT_8967: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/45:Location"
    )
)


_VARIANT_8968: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_8969: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/47:Alias"
    )
)


_VARIANT_8970: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_8971: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim8972(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8972: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8973(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8973: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_8974: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/52:Scene"
    )
)


class WardState8975(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8975: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_8976: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/54:Event"
    )
)


_VARIANT_8977: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_8978: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_8979: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/57:Faction"
    )
)


class RunOn8980(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_8982: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/0:Unused"
    )
)


_VARIANT_8983: _base.Variant = _base.Variant(
    path=(
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/1:Reference"
    )
)


class Structure8833(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
                "Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_8840": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
                "Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
                "Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
                "Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "SNDR/7:Conditions/repeat/0:Condition/0:CTDA/payload/9:"
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
        Annotated[float, _VARIANT_8837]
        | Annotated[_values.FormId, _VARIANT_8838]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_8840: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_8842]
        | Annotated[bytes, _VARIANT_8843]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8844,
        ]
        | Annotated[float, _VARIANT_8845]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8846,
        ]
        | Annotated[Sex8847, _VARIANT_8847]
        | Annotated[ActorValue8848, _VARIANT_8848]
        | Annotated[CrimeType8849, _VARIANT_8849]
        | Annotated[Axis8850, _VARIANT_8850]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8851,
        ]
        | Annotated[MiscStat8852, _VARIANT_8852]
        | Annotated[Alignment8853, _VARIANT_8853]
        | Annotated[_values.FormId, _VARIANT_8854]
        | Annotated[FormType8855, _VARIANT_8855]
        | Annotated[CriticalStage8856, _VARIANT_8856]
        | Annotated[_values.FormId, _VARIANT_8857]
        | Annotated[_values.FormId, _VARIANT_8858]
        | Annotated[_values.FormId, _VARIANT_8859]
        | Annotated[_values.FormId, _VARIANT_8860]
        | Annotated[_values.FormId, _VARIANT_8861]
        | Annotated[_values.FormId, _VARIANT_8862]
        | Annotated[_values.FormId, _VARIANT_8863]
        | Annotated[_values.FormId, _VARIANT_8864]
        | Annotated[_values.FormId, _VARIANT_8865]
        | Annotated[_values.FormId, _VARIANT_8866]
        | Annotated[_values.FormId, _VARIANT_8867]
        | Annotated[_values.FormId, _VARIANT_8868]
        | Annotated[_values.FormId, _VARIANT_8869]
        | Annotated[_values.FormId, _VARIANT_8870]
        | Annotated[_values.FormId, _VARIANT_8871]
        | Annotated[_values.FormId, _VARIANT_8872]
        | Annotated[_values.FormId, _VARIANT_8873]
        | Annotated[_values.FormId, _VARIANT_8874]
        | Annotated[_values.FormId, _VARIANT_8875]
        | Annotated[_values.FormId, _VARIANT_8876]
        | Annotated[_values.FormId, _VARIANT_8877]
        | Annotated[_values.FormId, _VARIANT_8878]
        | Annotated[VatsValueFunction8879, _VARIANT_8879]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8880,
        ]
        | Annotated[_values.FormId, _VARIANT_8881]
        | Annotated[_values.FormId, _VARIANT_8882]
        | Annotated[_values.FormId, _VARIANT_8883]
        | Annotated[PlayerAction8884, _VARIANT_8884]
        | Annotated[CastingType8885, _VARIANT_8885]
        | Annotated[_values.FormId, _VARIANT_8886]
        | Annotated[_values.FormId, _VARIANT_8887]
        | Annotated[_values.FormId, _VARIANT_8888]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8889,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8890,
        ]
        | Annotated[_values.FormId, _VARIANT_8891]
        | Annotated[FurnitureAnim8892, _VARIANT_8892]
        | Annotated[FurnitureEntry8893, _VARIANT_8893]
        | Annotated[_values.FormId, _VARIANT_8894]
        | Annotated[WardState8895, _VARIANT_8895]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8896,
        ]
        | Annotated[_values.FormId, _VARIANT_8897]
        | Annotated[_values.FormId, _VARIANT_8898]
        | Annotated[_values.FormId, _VARIANT_8899]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_8901]
        | Annotated[bytes, _VARIANT_8902]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8903,
        ]
        | Annotated[float, _VARIANT_8904]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8905,
        ]
        | Annotated[Sex8906, _VARIANT_8906]
        | Annotated[ActorValue8907, _VARIANT_8907]
        | Annotated[CrimeType8908, _VARIANT_8908]
        | Annotated[Axis8909, _VARIANT_8909]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8910,
        ]
        | Annotated[MiscStat8911, _VARIANT_8911]
        | Annotated[Alignment8912, _VARIANT_8912]
        | Annotated[_values.FormId, _VARIANT_8913]
        | Annotated[FormType8914, _VARIANT_8914]
        | Annotated[CriticalStage8915, _VARIANT_8915]
        | Annotated[_values.FormId, _VARIANT_8916]
        | Annotated[_values.FormId, _VARIANT_8917]
        | Annotated[_values.FormId, _VARIANT_8918]
        | Annotated[_values.FormId, _VARIANT_8919]
        | Annotated[_values.FormId, _VARIANT_8920]
        | Annotated[_values.FormId, _VARIANT_8921]
        | Annotated[_values.FormId, _VARIANT_8922]
        | Annotated[_values.FormId, _VARIANT_8923]
        | Annotated[_values.FormId, _VARIANT_8924]
        | Annotated[_values.FormId, _VARIANT_8925]
        | Annotated[_values.FormId, _VARIANT_8926]
        | Annotated[_values.FormId, _VARIANT_8927]
        | Annotated[_values.FormId, _VARIANT_8928]
        | Annotated[_values.FormId, _VARIANT_8929]
        | Annotated[_values.FormId, _VARIANT_8930]
        | Annotated[_values.FormId, _VARIANT_8931]
        | Annotated[_values.FormId, _VARIANT_8932]
        | Annotated[_values.FormId, _VARIANT_8933]
        | Annotated[_values.FormId, _VARIANT_8934]
        | Annotated[_values.FormId, _VARIANT_8935]
        | Annotated[_values.FormId, _VARIANT_8936]
        | Annotated[_values.FormId, _VARIANT_8937]
        | Annotated[VatsValueFunction8938, _VARIANT_8938]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8940]
            | Annotated[_values.FormId, _VARIANT_8941]
            | Annotated[_values.FormId, _VARIANT_8942]
            | Annotated[_values.FormId, _VARIANT_8943]
            | Annotated[bytes, _VARIANT_8944]
            | Annotated[TargetPart8945, _VARIANT_8945]
            | Annotated[VatsAction8946, _VARIANT_8946]
            | Annotated[bytes, _VARIANT_8947]
            | Annotated[bytes, _VARIANT_8948]
            | Annotated[_values.FormId, _VARIANT_8949]
            | Annotated[_values.FormId, _VARIANT_8950]
            | Annotated[bytes, _VARIANT_8951]
            | Annotated[bytes, _VARIANT_8952]
            | Annotated[bytes, _VARIANT_8953]
            | Annotated[bytes, _VARIANT_8954]
            | Annotated[WeaponType8955, _VARIANT_8955]
            | Annotated[bytes, _VARIANT_8956]
            | Annotated[bytes, _VARIANT_8957]
            | Annotated[ProjectileType8958, _VARIANT_8958]
            | Annotated[DeliveryType8959, _VARIANT_8959]
            | Annotated[CastingType8960, _VARIANT_8960],
            _VARIANT_8939,
        ]
        | Annotated[_values.FormId, _VARIANT_8961]
        | Annotated[_values.FormId, _VARIANT_8962]
        | Annotated[_values.FormId, _VARIANT_8963]
        | Annotated[PlayerAction8964, _VARIANT_8964]
        | Annotated[CastingType8965, _VARIANT_8965]
        | Annotated[_values.FormId, _VARIANT_8966]
        | Annotated[_values.FormId, _VARIANT_8967]
        | Annotated[_values.FormId, _VARIANT_8968]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8969,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8970,
        ]
        | Annotated[_values.FormId, _VARIANT_8971]
        | Annotated[FurnitureAnim8972, _VARIANT_8972]
        | Annotated[FurnitureEntry8973, _VARIANT_8973]
        | Annotated[_values.FormId, _VARIANT_8974]
        | Annotated[WardState8975, _VARIANT_8975]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8976,
        ]
        | Annotated[_values.FormId, _VARIANT_8977]
        | Annotated[_values.FormId, _VARIANT_8978]
        | Annotated[_values.FormId, _VARIANT_8979]
    )
    """Value decoded from this schema node."""

    run_on: RunOn8980
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8982,
        ]
        | Annotated[_values.FormId, _VARIANT_8983]
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
        Annotated[float, _VARIANT_8837]
        | Annotated[_values.FormId, _VARIANT_8838]
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
    def field(self, name: Literal["unused_8840"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8842]
        | Annotated[bytes, _VARIANT_8843]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8844,
        ]
        | Annotated[float, _VARIANT_8845]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8846,
        ]
        | Annotated[Sex8847, _VARIANT_8847]
        | Annotated[ActorValue8848, _VARIANT_8848]
        | Annotated[CrimeType8849, _VARIANT_8849]
        | Annotated[Axis8850, _VARIANT_8850]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8851,
        ]
        | Annotated[MiscStat8852, _VARIANT_8852]
        | Annotated[Alignment8853, _VARIANT_8853]
        | Annotated[_values.FormId, _VARIANT_8854]
        | Annotated[FormType8855, _VARIANT_8855]
        | Annotated[CriticalStage8856, _VARIANT_8856]
        | Annotated[_values.FormId, _VARIANT_8857]
        | Annotated[_values.FormId, _VARIANT_8858]
        | Annotated[_values.FormId, _VARIANT_8859]
        | Annotated[_values.FormId, _VARIANT_8860]
        | Annotated[_values.FormId, _VARIANT_8861]
        | Annotated[_values.FormId, _VARIANT_8862]
        | Annotated[_values.FormId, _VARIANT_8863]
        | Annotated[_values.FormId, _VARIANT_8864]
        | Annotated[_values.FormId, _VARIANT_8865]
        | Annotated[_values.FormId, _VARIANT_8866]
        | Annotated[_values.FormId, _VARIANT_8867]
        | Annotated[_values.FormId, _VARIANT_8868]
        | Annotated[_values.FormId, _VARIANT_8869]
        | Annotated[_values.FormId, _VARIANT_8870]
        | Annotated[_values.FormId, _VARIANT_8871]
        | Annotated[_values.FormId, _VARIANT_8872]
        | Annotated[_values.FormId, _VARIANT_8873]
        | Annotated[_values.FormId, _VARIANT_8874]
        | Annotated[_values.FormId, _VARIANT_8875]
        | Annotated[_values.FormId, _VARIANT_8876]
        | Annotated[_values.FormId, _VARIANT_8877]
        | Annotated[_values.FormId, _VARIANT_8878]
        | Annotated[VatsValueFunction8879, _VARIANT_8879]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8880,
        ]
        | Annotated[_values.FormId, _VARIANT_8881]
        | Annotated[_values.FormId, _VARIANT_8882]
        | Annotated[_values.FormId, _VARIANT_8883]
        | Annotated[PlayerAction8884, _VARIANT_8884]
        | Annotated[CastingType8885, _VARIANT_8885]
        | Annotated[_values.FormId, _VARIANT_8886]
        | Annotated[_values.FormId, _VARIANT_8887]
        | Annotated[_values.FormId, _VARIANT_8888]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8889,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8890,
        ]
        | Annotated[_values.FormId, _VARIANT_8891]
        | Annotated[FurnitureAnim8892, _VARIANT_8892]
        | Annotated[FurnitureEntry8893, _VARIANT_8893]
        | Annotated[_values.FormId, _VARIANT_8894]
        | Annotated[WardState8895, _VARIANT_8895]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8896,
        ]
        | Annotated[_values.FormId, _VARIANT_8897]
        | Annotated[_values.FormId, _VARIANT_8898]
        | Annotated[_values.FormId, _VARIANT_8899]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8901]
        | Annotated[bytes, _VARIANT_8902]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8903,
        ]
        | Annotated[float, _VARIANT_8904]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8905,
        ]
        | Annotated[Sex8906, _VARIANT_8906]
        | Annotated[ActorValue8907, _VARIANT_8907]
        | Annotated[CrimeType8908, _VARIANT_8908]
        | Annotated[Axis8909, _VARIANT_8909]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8910,
        ]
        | Annotated[MiscStat8911, _VARIANT_8911]
        | Annotated[Alignment8912, _VARIANT_8912]
        | Annotated[_values.FormId, _VARIANT_8913]
        | Annotated[FormType8914, _VARIANT_8914]
        | Annotated[CriticalStage8915, _VARIANT_8915]
        | Annotated[_values.FormId, _VARIANT_8916]
        | Annotated[_values.FormId, _VARIANT_8917]
        | Annotated[_values.FormId, _VARIANT_8918]
        | Annotated[_values.FormId, _VARIANT_8919]
        | Annotated[_values.FormId, _VARIANT_8920]
        | Annotated[_values.FormId, _VARIANT_8921]
        | Annotated[_values.FormId, _VARIANT_8922]
        | Annotated[_values.FormId, _VARIANT_8923]
        | Annotated[_values.FormId, _VARIANT_8924]
        | Annotated[_values.FormId, _VARIANT_8925]
        | Annotated[_values.FormId, _VARIANT_8926]
        | Annotated[_values.FormId, _VARIANT_8927]
        | Annotated[_values.FormId, _VARIANT_8928]
        | Annotated[_values.FormId, _VARIANT_8929]
        | Annotated[_values.FormId, _VARIANT_8930]
        | Annotated[_values.FormId, _VARIANT_8931]
        | Annotated[_values.FormId, _VARIANT_8932]
        | Annotated[_values.FormId, _VARIANT_8933]
        | Annotated[_values.FormId, _VARIANT_8934]
        | Annotated[_values.FormId, _VARIANT_8935]
        | Annotated[_values.FormId, _VARIANT_8936]
        | Annotated[_values.FormId, _VARIANT_8937]
        | Annotated[VatsValueFunction8938, _VARIANT_8938]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8940]
            | Annotated[_values.FormId, _VARIANT_8941]
            | Annotated[_values.FormId, _VARIANT_8942]
            | Annotated[_values.FormId, _VARIANT_8943]
            | Annotated[bytes, _VARIANT_8944]
            | Annotated[TargetPart8945, _VARIANT_8945]
            | Annotated[VatsAction8946, _VARIANT_8946]
            | Annotated[bytes, _VARIANT_8947]
            | Annotated[bytes, _VARIANT_8948]
            | Annotated[_values.FormId, _VARIANT_8949]
            | Annotated[_values.FormId, _VARIANT_8950]
            | Annotated[bytes, _VARIANT_8951]
            | Annotated[bytes, _VARIANT_8952]
            | Annotated[bytes, _VARIANT_8953]
            | Annotated[bytes, _VARIANT_8954]
            | Annotated[WeaponType8955, _VARIANT_8955]
            | Annotated[bytes, _VARIANT_8956]
            | Annotated[bytes, _VARIANT_8957]
            | Annotated[ProjectileType8958, _VARIANT_8958]
            | Annotated[DeliveryType8959, _VARIANT_8959]
            | Annotated[CastingType8960, _VARIANT_8960],
            _VARIANT_8939,
        ]
        | Annotated[_values.FormId, _VARIANT_8961]
        | Annotated[_values.FormId, _VARIANT_8962]
        | Annotated[_values.FormId, _VARIANT_8963]
        | Annotated[PlayerAction8964, _VARIANT_8964]
        | Annotated[CastingType8965, _VARIANT_8965]
        | Annotated[_values.FormId, _VARIANT_8966]
        | Annotated[_values.FormId, _VARIANT_8967]
        | Annotated[_values.FormId, _VARIANT_8968]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8969,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8970,
        ]
        | Annotated[_values.FormId, _VARIANT_8971]
        | Annotated[FurnitureAnim8972, _VARIANT_8972]
        | Annotated[FurnitureEntry8973, _VARIANT_8973]
        | Annotated[_values.FormId, _VARIANT_8974]
        | Annotated[WardState8975, _VARIANT_8975]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8976,
        ]
        | Annotated[_values.FormId, _VARIANT_8977]
        | Annotated[_values.FormId, _VARIANT_8978]
        | Annotated[_values.FormId, _VARIANT_8979]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn8980]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8982,
        ]
        | Annotated[_values.FormId, _VARIANT_8983]
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


class Condition8831(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SNDR/7:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="SNDR/7:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("SNDR/7:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("SNDR/7:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure8833] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure8833]]:
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


class Looping8992(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    LOOP = 8
    ENVELOPE_FAST = 16
    ENVELOPE_SLOW = 32


class Structure8990(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SNDR/8:Values/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="SNDR/8:Values/payload/0:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "looping": _base.Binding(
            path="SNDR/8:Values/payload/1:Looping",
            kind="primitive",
            name="Looping",
        ),
        "unknown_8993": _base.Binding(
            path="SNDR/8:Values/payload/2:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "rumble_send_value_small_7_big_7_16": _base.Binding(
            path=(
                "SNDR/8:Values/payload/3:Rumble Send Value = (Small / 7"
                ") + ((Big / 7) * 16)"
            ),
            kind="primitive",
            name=("Rumble Send Value = (Small / 7) + ((Big / 7) * 16)"),
        ),
    }

    unknown: bytes
    """Value decoded from this schema node."""

    looping: Looping8992
    """Value decoded from this schema node."""

    unknown_8993: bytes
    """Value decoded from this schema node."""

    rumble_send_value_small_7_big_7_16: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["looping"]) -> _base.FieldRef[Looping8992]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_8993"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rumble_send_value_small_7_big_7_16"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
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


class Structure8996(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SNDR/9:Values/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "frequency_shift": _base.Binding(
            path="SNDR/9:Values/payload/0:% Frequency Shift",
            kind="primitive",
            name="% Frequency Shift",
        ),
        "frequency_variance": _base.Binding(
            path="SNDR/9:Values/payload/1:% Frequency Variance",
            kind="primitive",
            name="% Frequency Variance",
        ),
        "priority": _base.Binding(
            path="SNDR/9:Values/payload/2:Priority",
            kind="primitive",
            name="Priority",
        ),
        "db_variance": _base.Binding(
            path="SNDR/9:Values/payload/3:db Variance",
            kind="primitive",
            name="db Variance",
        ),
        "static_attenuation_db": _base.Binding(
            path="SNDR/9:Values/payload/4:Static Attenuation (db)",
            kind="primitive",
            name="Static Attenuation (db)",
        ),
    }

    frequency_shift: Annotated[
        int, pydantic.Field(strict=True, ge=-128, le=127)
    ]
    """Value decoded from this schema node."""

    frequency_variance: Annotated[
        int, pydantic.Field(strict=True, ge=-128, le=127)
    ]
    """Value decoded from this schema node."""

    priority: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    db_variance: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    static_attenuation_db: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=65535)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["frequency_shift"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["frequency_variance"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["priority"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["db_variance"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["static_attenuation_db"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
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


class SoundDescriptorRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SNDR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SNDR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SNDR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "descriptor_type": _base.Binding(
            path="SNDR/1:Descriptor Type",
            kind="subrecord",
            name="Descriptor Type",
        ),
        "category": _base.Binding(
            path="SNDR/2:Category",
            kind="subrecord",
            name="Category",
        ),
        "alternate_sound_for": _base.Binding(
            path="SNDR/3:Alternate Sound For",
            kind="subrecord",
            name="Alternate Sound For",
        ),
        "sounds": _base.Binding(
            path="SNDR/4:Sounds",
            kind="repeat",
            name="Sounds",
            repeated_path="SNDR/4:Sounds/repeat/0:Sound Files",
            child_kind="sequence",
        ),
        "output_model": _base.Binding(
            path="SNDR/5:Output Model",
            kind="subrecord",
            name="Output Model",
        ),
        "string": _base.Binding(
            path="SNDR/6:String",
            kind="subrecord",
            name="String",
        ),
        "conditions": _base.Binding(
            path="SNDR/7:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="SNDR/7:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "values": _base.Binding(
            path="SNDR/8:Values",
            kind="subrecord",
            name="Values",
        ),
        "values_8995": _base.Binding(
            path="SNDR/9:Values",
            kind="subrecord",
            name="Values",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    descriptor_type: Optional[Value8817] = None
    """Value decoded from this schema node."""

    category: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alternate_sound_for: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sounds: tuple[SoundFiles8823, ...] = ()
    """Value decoded from this schema node."""

    output_model: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    string: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition8831, ...] = ()
    """Value decoded from this schema node."""

    values: Optional[Structure8990] = None
    """Value decoded from this schema node."""

    values_8995: Optional[Structure8996] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["descriptor_type"]
    ) -> _base.FieldRef[Optional[Value8817]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["category"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_sound_for"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sounds"]
    ) -> _base.FieldRef[tuple[SoundFiles8823, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["output_model"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["string"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition8831, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["values"]
    ) -> _base.FieldRef[Optional[Structure8990]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["values_8995"]
    ) -> _base.FieldRef[Optional[Structure8996]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
