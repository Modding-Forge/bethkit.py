"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class TopicFlags3172(enum.IntFlag):
    """Named values from the pinned schema."""

    DO_ALL_BEFORE_REPEATING = 1


class Category3173(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TOPIC = 0
    FAVOR = 1
    SCENE = 2
    COMBAT = 3
    FAVORS = 4
    DETECTION = 5
    SERVICE = 6
    MISCELLANEOUS = 7


class Subtype3174(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CUSTOM = 0
    FORCE_GREET = 1
    RUMORS = 2
    CUSTOM_3 = 3
    INTIMIDATE = 4
    FLATTER = 5
    BRIBE = 6
    ASK_GIFT = 7
    GIFT = 8
    ASK_FAVOR = 9
    FAVOR = 10
    SHOW_RELATIONSHIPS = 11
    FOLLOW = 12
    REJECT = 13
    SCENE = 14
    SHOW = 15
    AGREE = 16
    REFUSE = 17
    EXIT_FAVOR_STATE = 18
    MORAL_REFUSAL = 19
    FLYING_MOUNT_LAND = 20
    FLYING_MOUNT_CANCEL_LAND = 21
    FLYING_MOUNT_ACCEPT_TARGET = 22
    FLYING_MOUNT_REJECT_TARGET = 23
    FLYING_MOUNT_NO_TARGET = 24
    FLYING_MOUNT_DESTINATION_REACHED = 25
    ATTACK = 26
    POWER_ATTACK = 27
    BASH = 28
    HIT = 29
    FLEE = 30
    BLEEDOUT = 31
    AVOID_THREAT = 32
    DEATH = 33
    GROUP_STRATEGY = 34
    BLOCK = 35
    TAUNT = 36
    ALLY_KILLED = 37
    STEAL = 38
    YIELD = 39
    ACCEPT_YIELD = 40
    PICKPOCKET_COMBAT = 41
    ASSAULT = 42
    MURDER = 43
    ASSAULT_NC = 44
    MURDER_NC = 45
    PICKPOCKET_NC = 46
    STEAL_FROM_NC = 47
    TRESPASS_AGAINST_NC = 48
    TRESPASS = 49
    WERE_TRANSFORM_CRIME = 50
    VOICE_POWER_START_SHORT = 51
    VOICE_POWER_START_LONG = 52
    VOICE_POWER_END_SHORT = 53
    VOICE_POWER_END_LONG = 54
    ALERT_IDLE = 55
    LOST_IDLE = 56
    NORMAL_TO_ALERT = 57
    ALERT_TO_COMBAT = 58
    NORMAL_TO_COMBAT = 59
    ALERT_TO_NORMAL = 60
    COMBAT_TO_NORMAL = 61
    COMBAT_TO_LOST = 62
    LOST_TO_NORMAL = 63
    LOST_TO_COMBAT = 64
    DETECT_FRIEND_DIE = 65
    SERVICE_REFUSAL = 66
    REPAIR = 67
    TRAVEL = 68
    TRAINING = 69
    BARTER_EXIT = 70
    REPAIR_EXIT = 71
    RECHARGE = 72
    RECHARGE_EXIT = 73
    TRAINING_EXIT = 74
    OBSERVE_COMBAT = 75
    NOTICE_CORPSE = 76
    TIME_TO_GO = 77
    GOOD_BYE = 78
    HELLO = 79
    SWING_MELEE_WEAPON = 80
    SHOOT_BOW = 81
    ZKEY_OBJECT = 82
    JUMP = 83
    KNOCK_OVER_OBJECT = 84
    DESTROY_OBJECT = 85
    STANDON_FURNITURE = 86
    LOCKED_OBJECT = 87
    PICKPOCKET_TOPIC = 88
    PURSUE_IDLE_TOPIC = 89
    SHARED_INFO = 90
    PLAYER_CAST_PROJECTILE_SPELL = 91
    PLAYER_CAST_SELF_SPELL = 92
    PLAYER_SHOUT = 93
    IDLE = 94
    ENTER_SPRINT_BREATH = 95
    ENTER_BOW_ZOOM_BREATH = 96
    EXIT_BOW_ZOOM_BREATH = 97
    ACTOR_COLLIDEWITH_ACTOR = 98
    PLAYERIN_IRON_SIGHTS = 99
    OUTOF_BREATH = 100
    COMBAT_GRUNT = 101
    LEAVE_WATER_BREATH = 102


class Structure3171(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "DIAL/5:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "topic_flags": _base.Binding(
            path="DIAL/5:Data/payload/0:Topic Flags",
            kind="primitive",
            name="Topic Flags",
        ),
        "category": _base.Binding(
            path="DIAL/5:Data/payload/1:Category",
            kind="primitive",
            name="Category",
        ),
        "subtype": _base.Binding(
            path="DIAL/5:Data/payload/2:Subtype",
            kind="primitive",
            name="Subtype",
        ),
    }

    topic_flags: TopicFlags3172
    """Value decoded from this schema node."""

    category: Category3173
    """Value decoded from this schema node."""

    subtype: Subtype3174
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["topic_flags"]
    ) -> _base.FieldRef[TopicFlags3172]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["category"]) -> _base.FieldRef[Category3173]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["subtype"]) -> _base.FieldRef[Subtype3174]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Value3176(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    DETECT_FRIEND_DIE = 1094993476
    ENTER_SPRINT_BREATH = 1095062082
    STEAL = 1095062611
    REPAIR = 1095779666
    ASSAULT = 1095979841
    NORMAL_TO_ALERT = 1096044366
    BRIBE = 1112101442
    DESTROY_OBJECT = 1112491332
    LOCKED_OBJECT = 1112493900
    OUTOF_BREATH = 1112823119
    ACTOR_COLLIDEWITH_ACTOR = 1128350529
    PICKPOCKET_COMBAT = 1128483152
    ASSAULT_NC = 1129206593
    MURDER_NC = 1129207117
    BLOCK = 1129270338
    ALERT_TO_COMBAT = 1129598017
    LOST_TO_COMBAT = 1129598796
    NORMAL_TO_COMBAT = 1129598798
    BLEED_OUT = 1145392194
    MURDER = 1146246477
    FLEE = 1162169414
    IDLE = 1162626121
    AGREE = 1163020097
    SHOW_RELATIONSHIPS = 1163020371
    SHOOT_BOW = 1163348294
    GOODBYE = 1163477575
    MORAL_REFUSAL = 1178948173
    GIFT = 1179011399
    ASK_FAVOR = 1179341633
    STANDON_FURNITURE = 1179604051
    ASK_GIFT = 1196118849
    TIME_TO_GO = 1196706132
    RECHARGE = 1212368210
    BASH = 1213415746
    PLAYER_SHOUT = 1213416272
    DEATH = 1213482308
    AVOID_THREAT = 1213486657
    TRAINING = 1229017684
    INTIMIDATE = 1230261833
    NOTICE_CORPSE = 1230262094
    ACCEPT_YIELD = 1230586689
    ATTACK = 1262703681
    CUSTOM = 1279546950
    YIELD = 1279609177
    VOICE_POWER_END_LONG = 1279610966
    ALERT_IDLE = 1279872065
    LOST_IDLE = 1279872844
    ALLY_KILLED = 1280003137
    FOLLOW = 1280069446
    VOICE_POWER_START_LONG = 1280528470
    FLYING_MOUNT_CANCEL_LAND = 1280855366
    TRESPASS_AGAINST_NC = 1312903764
    PICKPOCKET_NC = 1313032528
    SCENE = 1313162067
    STEAL_FROM_NC = 1313231955
    PLAYERIN_IRON_SIGHTS = 1314015568
    ALERT_TO_NORMAL = 1314147393
    COMBAT_TO_NORMAL = 1314148163
    LOST_TO_NORMAL = 1314148172
    OBSERVE_COMBAT = 1329807951
    HELLO = 1330398536
    COMBAT_TO_LOST = 1330401091
    RUMORS = 1330468178
    KNOCK_OVER_OBJECT = 1330597451
    FAVOR = 1331052870
    JUMP = 1347245386
    WERE_TRANSFORM_CRIME = 1380144215
    FLYING_MOUNT_DESTINATION_REACHED = 1380207942
    LEAVE_WATER_BREATH = 1396856652
    VOICE_POWER_END_SHORT = 1397051478
    TRESPASS = 1397051988
    PLAYER_CAST_PROJECTILE_SPELL = 1397769040
    PURSUE_IDLE_TOPIC = 1397904720
    PLAYER_CAST_SELF_SPELL = 1397965648
    VOICE_POWER_START_SHORT = 1397968982
    SHARED_INFO = 1413563465
    FLATTER = 1413565510
    FLYING_MOUNT_ACCEPT_TARGET = 1413565766
    POWER_ATTACK = 1413566288
    PICKPOCKET_TOPIC = 1413695824
    FORCE_GREET = 1413957200
    REJECT = 1414156870
    FLYING_MOUNT_NO_TARGET = 1414417734
    COMBAT_GRUNT = 1414419015
    FLYING_MOUNT_REJECT_TARGET = 1414679878
    GROUP_STRATEGY = 1414746695
    CUSTOM_86 = 1414747459
    TAUNT = 1414873428
    EXIT_FAVOR_STATE = 1415071046
    REFUSE = 1430668626
    SERVICE_REFUSAL = 1431455059
    TRAVEL = 1447121492
    SWING_MELEE_WEAPON = 1464686419
    SHOW = 1464813651
    BARTER_EXIT = 1480933698
    RECHARGE_EXIT = 1480934226
    REPAIR_EXIT = 1480934738
    TRAINING_EXIT = 1480938068
    FLYING_MOUNT_LAND = 1481395526
    ZKEY_OBJECT = 1497713498
    ENTER_BOW_ZOOM_BREATH = 1514294853
    EXIT_BOW_ZOOM_BREATH = 1514297413
    HIT = 1599359304


class DialogTopicRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "DIAL"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "DIAL"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="DIAL/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="DIAL/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "priority": _base.Binding(
            path="DIAL/2:Priority",
            kind="subrecord",
            name="Priority",
        ),
        "branch": _base.Binding(
            path="DIAL/3:Branch",
            kind="subrecord",
            name="Branch",
        ),
        "quest": _base.Binding(
            path="DIAL/4:Quest",
            kind="subrecord",
            name="Quest",
        ),
        "data": _base.Binding(
            path="DIAL/5:Data",
            kind="subrecord",
            name="Data",
        ),
        "subtype_name": _base.Binding(
            path="DIAL/6:Subtype Name",
            kind="subrecord",
            name="Subtype Name",
        ),
        "info_count": _base.Binding(
            path="DIAL/7:Info Count",
            kind="subrecord",
            name="Info Count",
        ),
        "info_order_masters_only": _base.Binding(
            path="DIAL/8:INFO Order (Masters only)",
            kind="subrecord",
            name="INFO Order (Masters only)",
        ),
        "info_order_all_previous_modules": _base.Binding(
            path="DIAL/9:INFO Order (All previous modules)",
            kind="subrecord",
            name="INFO Order (All previous modules)",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    priority: Optional[float] = None
    """Value decoded from this schema node."""

    branch: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    data: Optional[Structure3171] = None
    """Value decoded from this schema node."""

    subtype_name: Optional[Value3176] = None
    """Value decoded from this schema node."""

    info_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    info_order_masters_only: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    info_order_all_previous_modules: Optional[tuple[_values.FormId, ...]] = None
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
        self, name: Literal["priority"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["branch"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["quest"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure3171]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["subtype_name"]
    ) -> _base.FieldRef[Optional[Value3176]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["info_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["info_order_masters_only"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["info_order_all_previous_modules"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
