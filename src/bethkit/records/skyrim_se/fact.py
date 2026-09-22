"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class GroupCombatReaction3728(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NEUTRAL = 0
    ENEMY = 1
    ALLY = 2
    FRIEND = 3


class Structure3725(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT/2:Relations/repeat/0:Relation/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "faction": _base.Binding(
            path=("FACT/2:Relations/repeat/0:Relation/payload/0:Faction"),
            kind="primitive",
            name="Faction",
        ),
        "modifier": _base.Binding(
            path=("FACT/2:Relations/repeat/0:Relation/payload/1:Modifier"),
            kind="primitive",
            name="Modifier",
        ),
        "group_combat_reaction": _base.Binding(
            path=(
                "FACT/2:Relations/repeat/0:Relation/payload/2:Group Com"
                "bat Reaction"
            ),
            kind="primitive",
            name="Group Combat Reaction",
        ),
    }

    faction: _values.FormId
    """Value decoded from this schema node."""

    modifier: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    group_combat_reaction: GroupCombatReaction3728
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["faction"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["modifier"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["group_combat_reaction"]
    ) -> _base.FieldRef[GroupCombatReaction3728]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags3731(enum.IntFlag):
    """Named values from the pinned schema."""

    HIDDEN_FROM_NPC = 1
    SPECIAL_COMBAT = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    TRACK_CRIME = 64
    IGNORE_CRIMES_MURDER = 128
    IGNORE_CRIMES_ASSAULT = 256
    IGNORE_CRIMES_STEALING = 512
    IGNORE_CRIMES_TRESPASS = 1024
    DO_NOT_REPORT_CRIMES_AGAINST_MEMBERS = 2048
    CRIME_GOLD_USE_DEFAULTS = 4096
    IGNORE_CRIMES_PICKPOCKET = 8192
    VENDOR = 16384
    CAN_BE_OWNER = 32768
    IGNORE_CRIMES_WEREWOLF = 65536
    UNKNOWN_18 = 131072
    UNKNOWN_19 = 262144
    UNKNOWN_20 = 524288
    UNKNOWN_21 = 1048576
    UNKNOWN_22 = 2097152
    UNKNOWN_23 = 4194304
    UNKNOWN_24 = 8388608
    UNKNOWN_25 = 16777216
    UNKNOWN_26 = 33554432
    UNKNOWN_27 = 67108864
    UNKNOWN_28 = 134217728
    UNKNOWN_29 = 268435456
    UNKNOWN_30 = 536870912
    UNKNOWN_31 = 1073741824
    UNKNOWN_32 = 2147483648


class Structure3730(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT/3:Flags/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="FACT/3:Flags/payload/0:Flags",
            kind="primitive",
            name="Flags",
        ),
    }

    flags: Flags3731
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags3731]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Arrest3746(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class AttackOnSight3747(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure3745(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT/10:Crime Values/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "arrest": _base.Binding(
            path="FACT/10:Crime Values/payload/0:Arrest",
            kind="primitive",
            name="Arrest",
        ),
        "attack_on_sight": _base.Binding(
            path="FACT/10:Crime Values/payload/1:Attack On Sight",
            kind="primitive",
            name="Attack On Sight",
        ),
        "murder": _base.Binding(
            path="FACT/10:Crime Values/payload/2:Murder",
            kind="primitive",
            name="Murder",
        ),
        "assault": _base.Binding(
            path="FACT/10:Crime Values/payload/3:Assault",
            kind="primitive",
            name="Assault",
        ),
        "trespass": _base.Binding(
            path="FACT/10:Crime Values/payload/4:Trespass",
            kind="primitive",
            name="Trespass",
        ),
        "pickpocket": _base.Binding(
            path="FACT/10:Crime Values/payload/5:Pickpocket",
            kind="primitive",
            name="Pickpocket",
        ),
        "unknown": _base.Binding(
            path="FACT/10:Crime Values/payload/6:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "steal_multiplier": _base.Binding(
            path="FACT/10:Crime Values/payload/7:Steal Multiplier",
            kind="primitive",
            name="Steal Multiplier",
        ),
        "escape": _base.Binding(
            path="FACT/10:Crime Values/payload/8:Escape",
            kind="primitive",
            name="Escape",
        ),
        "werewolf": _base.Binding(
            path="FACT/10:Crime Values/payload/9:Werewolf",
            kind="primitive",
            name="Werewolf",
        ),
    }

    arrest: Arrest3746
    """Value decoded from this schema node."""

    attack_on_sight: AttackOnSight3747
    """Value decoded from this schema node."""

    murder: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    assault: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    trespass: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    pickpocket: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unknown: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    steal_multiplier: Optional[float] = None
    """Value decoded from this schema node."""

    escape: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    werewolf: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["arrest"]) -> _base.FieldRef[Arrest3746]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_on_sight"]
    ) -> _base.FieldRef[AttackOnSight3747]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["murder"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["assault"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["trespass"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["pickpocket"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["steal_multiplier"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["escape"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["werewolf"]
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


class Rank3757(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT/11:Ranks/repeat/0:Rank"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "rank": _base.Binding(
            path="FACT/11:Ranks/repeat/0:Rank/0:Rank#",
            kind="subrecord",
            name="Rank#",
        ),
        "male_title": _base.Binding(
            path="FACT/11:Ranks/repeat/0:Rank/1:Male Title",
            kind="subrecord",
            name="Male Title",
        ),
        "female_title": _base.Binding(
            path="FACT/11:Ranks/repeat/0:Rank/2:Female Title",
            kind="subrecord",
            name="Female Title",
        ),
        "insignia_unused": _base.Binding(
            path="FACT/11:Ranks/repeat/0:Rank/3:Insignia Unused",
            kind="subrecord",
            name="Insignia Unused",
        ),
    }

    rank: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    male_title: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    female_title: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    insignia_unused: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["rank"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_title"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_title"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["insignia_unused"]
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


class OnlyBuysStolenItems3776(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class NotSellBuy3777(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure3771(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT/14:Vendor Values/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "start_hour": _base.Binding(
            path="FACT/14:Vendor Values/payload/0:Start Hour",
            kind="primitive",
            name="Start Hour",
        ),
        "end_hour": _base.Binding(
            path="FACT/14:Vendor Values/payload/1:End Hour",
            kind="primitive",
            name="End Hour",
        ),
        "radius": _base.Binding(
            path="FACT/14:Vendor Values/payload/2:Radius",
            kind="primitive",
            name="Radius",
        ),
        "unknown_1": _base.Binding(
            path="FACT/14:Vendor Values/payload/3:Unknown 1",
            kind="primitive",
            name="Unknown 1",
        ),
        "only_buys_stolen_items": _base.Binding(
            path=("FACT/14:Vendor Values/payload/4:Only Buys Stolen Items"),
            kind="primitive",
            name="Only Buys Stolen Items",
        ),
        "not_sell_buy": _base.Binding(
            path="FACT/14:Vendor Values/payload/5:Not/Sell Buy",
            kind="primitive",
            name="Not/Sell Buy",
        ),
        "unknown_2": _base.Binding(
            path="FACT/14:Vendor Values/payload/6:Unknown 2",
            kind="primitive",
            name="Unknown 2",
        ),
    }

    start_hour: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    end_hour: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    radius: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unknown_1: bytes
    """Value decoded from this schema node."""

    only_buys_stolen_items: OnlyBuysStolenItems3776
    """Value decoded from this schema node."""

    not_sell_buy: NotSellBuy3777
    """Value decoded from this schema node."""

    unknown_2: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["start_hour"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["end_hour"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radius"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_1"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["only_buys_stolen_items"]
    ) -> _base.FieldRef[OnlyBuysStolenItems3776]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["not_sell_buy"]
    ) -> _base.FieldRef[NotSellBuy3777]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_2"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type3781(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NEAR_REFERENCE = 0
    IN_CELL = 1
    NEAR_PACKAGE_START_LOCATION = 2
    NEAR_EDITOR_LOCATION = 3
    OBJECT_ID = 4
    OBJECT_TYPE = 5
    NEAR_LINKED_REFERENCE = 6
    AT_PACKAGE_LOCATION = 7
    ALIAS_REFERENCE = 8
    ALIAS_LOCATION = 9
    UNKNOWN_10 = 10
    UNKNOWN_11 = 11
    NEAR_SELF = 12


_VARIANT_3783: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/0:Reference")
)


_VARIANT_3784: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/1:Cell")
)


_VARIANT_3785: _base.Variant = _base.Variant(
    path=(
        "FACT/15:Location/payload/1:Location Value/variants/2:N"
        "ear Package Start Location"
    )
)


_VARIANT_3786: _base.Variant = _base.Variant(
    path=(
        "FACT/15:Location/payload/1:Location Value/variants/3:N"
        "ear Editor Location"
    )
)


_VARIANT_3787: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/4:Object ID")
)


_VARIANT_3788: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/5:Object Type")
)


_VARIANT_3789: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/6:Keyword")
)


_VARIANT_3790: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/7:Unused")
)


_VARIANT_3791: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/8:Alias")
)


_VARIANT_3792: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/9:Reference")
)


_VARIANT_3793: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/10:Unknown")
)


_VARIANT_3794: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/11:Unknown")
)


_VARIANT_3795: _base.Variant = _base.Variant(
    path=("FACT/15:Location/payload/1:Location Value/variants/12:Unknown")
)


class Structure3780(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT/15:Location/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path="FACT/15:Location/payload/0:Type",
            kind="primitive",
            name="Type",
        ),
        "location_value": _base.Binding(
            path="FACT/15:Location/payload/1:Location Value",
            kind="union",
            name="Location Value",
        ),
        "radius": _base.Binding(
            path="FACT/15:Location/payload/2:Radius",
            kind="primitive",
            name="Radius",
        ),
    }

    type: Type3781
    """Value decoded from this schema node."""

    location_value: (
        Annotated[_values.FormId, _VARIANT_3783]
        | Annotated[_values.FormId, _VARIANT_3784]
        | Annotated[bytes, _VARIANT_3785]
        | Annotated[bytes, _VARIANT_3786]
        | Annotated[_values.FormId, _VARIANT_3787]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3788,
        ]
        | Annotated[_values.FormId, _VARIANT_3789]
        | Annotated[bytes, _VARIANT_3790]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3791,
        ]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3792,
        ]
        | Annotated[bytes, _VARIANT_3793]
        | Annotated[bytes, _VARIANT_3794]
        | Annotated[bytes, _VARIANT_3795]
    )
    """Value decoded from this schema node."""

    radius: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type3781]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location_value"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_3783]
        | Annotated[_values.FormId, _VARIANT_3784]
        | Annotated[bytes, _VARIANT_3785]
        | Annotated[bytes, _VARIANT_3786]
        | Annotated[_values.FormId, _VARIANT_3787]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3788,
        ]
        | Annotated[_values.FormId, _VARIANT_3789]
        | Annotated[bytes, _VARIANT_3790]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3791,
        ]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3792,
        ]
        | Annotated[bytes, _VARIANT_3793]
        | Annotated[bytes, _VARIANT_3794]
        | Annotated[bytes, _VARIANT_3795]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radius"]
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


_VARIANT_3806: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_3807: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_3811: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_3812: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/1:None"
    )
)


_VARIANT_3813: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/2:Integer"
    )
)


_VARIANT_3814: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/3:Float"
    )
)


_VARIANT_3815: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/4:Variable Name"
    )
)


class Sex3816(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_3816: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/5:Sex"
    )
)


class ActorValue3817(_values.OpenIntEnum):
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


_VARIANT_3817: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType3818(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_3818: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/7:Crime Type"
    )
)


class Axis3819(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_3819: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/8:Axis"
    )
)


_VARIANT_3820: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat3821(_values.OpenIntEnum):
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


_VARIANT_3821: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment3822(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_3822: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_3823: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/12:Equip Type"
    )
)


class FormType3824(_values.OpenIntEnum):
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


_VARIANT_3824: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage3825(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_3825: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_3826: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_3827: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_3828: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/17:Actor"
    )
)


_VARIANT_3829: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_3830: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/19:Idle"
    )
)


_VARIANT_3831: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/20:Form List"
    )
)


_VARIANT_3832: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/21:Quest"
    )
)


_VARIANT_3833: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/22:Faction"
    )
)


_VARIANT_3834: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/23:Cell"
    )
)


_VARIANT_3835: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/24:Class"
    )
)


_VARIANT_3836: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/25:Race"
    )
)


_VARIANT_3837: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_3838: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/27:Global"
    )
)


_VARIANT_3839: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/28:Weather"
    )
)


_VARIANT_3840: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/29:Package"
    )
)


_VARIANT_3841: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_3842: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/31:Perk"
    )
)


_VARIANT_3843: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/32:Owner"
    )
)


_VARIANT_3844: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_3845: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_3846: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_3847: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction3848(_values.OpenIntEnum):
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


_VARIANT_3848: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_3849: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_3850: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_3851: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/40:Region"
    )
)


_VARIANT_3852: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction3853(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_3853: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/42:Player Action"
    )
)


class CastingType3854(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_3854: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_3855: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/44:Shout"
    )
)


_VARIANT_3856: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/45:Location"
    )
)


_VARIANT_3857: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_3858: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/47:Alias"
    )
)


_VARIANT_3859: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_3860: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim3861(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_3861: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry3862(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_3862: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_3863: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/52:Scene"
    )
)


class WardState3864(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_3864: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_3865: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/54:Event"
    )
)


_VARIANT_3866: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_3867: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_3868: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/57:Faction"
    )
)


_VARIANT_3870: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_3871: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/1:None"
    )
)


_VARIANT_3872: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/2:Integer"
    )
)


_VARIANT_3873: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/3:Float"
    )
)


_VARIANT_3874: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/4:Variable Name"
    )
)


class Sex3875(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_3875: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/5:Sex"
    )
)


class ActorValue3876(_values.OpenIntEnum):
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


_VARIANT_3876: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType3877(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_3877: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/7:Crime Type"
    )
)


class Axis3878(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_3878: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/8:Axis"
    )
)


_VARIANT_3879: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat3880(_values.OpenIntEnum):
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


_VARIANT_3880: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment3881(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_3881: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_3882: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/12:Equip Type"
    )
)


class FormType3883(_values.OpenIntEnum):
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


_VARIANT_3883: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage3884(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_3884: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_3885: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_3886: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_3887: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/17:Actor"
    )
)


_VARIANT_3888: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_3889: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/19:Idle"
    )
)


_VARIANT_3890: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/20:Form List"
    )
)


_VARIANT_3891: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/21:Quest"
    )
)


_VARIANT_3892: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/22:Faction"
    )
)


_VARIANT_3893: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/23:Cell"
    )
)


_VARIANT_3894: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/24:Class"
    )
)


_VARIANT_3895: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/25:Race"
    )
)


_VARIANT_3896: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_3897: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/27:Global"
    )
)


_VARIANT_3898: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/28:Weather"
    )
)


_VARIANT_3899: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/29:Package"
    )
)


_VARIANT_3900: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_3901: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/31:Perk"
    )
)


_VARIANT_3902: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/32:Owner"
    )
)


_VARIANT_3903: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_3904: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_3905: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_3906: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction3907(_values.OpenIntEnum):
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


_VARIANT_3907: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_3909: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/0:"
        "Weapon"
    )
)


_VARIANT_3910: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/1:"
        "Weapon List"
    )
)


_VARIANT_3911: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/2:"
        "Target"
    )
)


_VARIANT_3912: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/3:"
        "Target List"
    )
)


_VARIANT_3913: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/4:"
        "Unknown"
    )
)


class TargetPart3914(_values.OpenIntEnum):
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


_VARIANT_3914: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/5:"
        "Target Part"
    )
)


class VatsAction3915(_values.OpenIntEnum):
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


_VARIANT_3915: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/6:"
        "VATS Action"
    )
)


_VARIANT_3916: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/7:"
        "Unknown"
    )
)


_VARIANT_3917: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/8:"
        "Unknown"
    )
)


_VARIANT_3918: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/9:"
        "Critical Effect"
    )
)


_VARIANT_3919: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/10"
        ":Critical Effect List"
    )
)


_VARIANT_3920: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/11"
        ":Unknown"
    )
)


_VARIANT_3921: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/12"
        ":Unknown"
    )
)


_VARIANT_3922: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/13"
        ":Unknown"
    )
)


_VARIANT_3923: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/14"
        ":Unknown"
    )
)


class WeaponType3924(_values.OpenIntEnum):
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


_VARIANT_3924: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/15"
        ":Weapon Type"
    )
)


_VARIANT_3925: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/16"
        ":Unknown"
    )
)


_VARIANT_3926: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/17"
        ":Unknown"
    )
)


class ProjectileType3927(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_3927: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/18"
        ":Projectile Type"
    )
)


class DeliveryType3928(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_3928: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/19"
        ":Delivery Type"
    )
)


class CastingType3929(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_3929: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/20"
        ":Casting Type"
    )
)


_VARIANT_3908: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_3930: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_3931: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/40:Region"
    )
)


_VARIANT_3932: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction3933(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_3933: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/42:Player Action"
    )
)


class CastingType3934(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_3934: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_3935: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/44:Shout"
    )
)


_VARIANT_3936: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/45:Location"
    )
)


_VARIANT_3937: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_3938: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/47:Alias"
    )
)


_VARIANT_3939: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_3940: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim3941(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_3941: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry3942(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_3942: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_3943: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/52:Scene"
    )
)


class WardState3944(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_3944: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_3945: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/54:Event"
    )
)


_VARIANT_3946: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_3947: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_3948: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/57:Faction"
    )
)


class RunOn3949(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_3951: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/0:Unused"
    )
)


_VARIANT_3952: _base.Variant = _base.Variant(
    path=(
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/1:Reference"
    )
)


class Structure3802(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/2"
                ":Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/3"
                ":Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_3809": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/5"
                ":Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/6"
                ":Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/8"
                ":Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "FACT/17:Conditions/repeat/0:Condition/0:CTDA/payload/9"
                ":Parameter #3"
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
        Annotated[float, _VARIANT_3806]
        | Annotated[_values.FormId, _VARIANT_3807]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_3809: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_3811]
        | Annotated[bytes, _VARIANT_3812]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3813,
        ]
        | Annotated[float, _VARIANT_3814]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3815,
        ]
        | Annotated[Sex3816, _VARIANT_3816]
        | Annotated[ActorValue3817, _VARIANT_3817]
        | Annotated[CrimeType3818, _VARIANT_3818]
        | Annotated[Axis3819, _VARIANT_3819]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3820,
        ]
        | Annotated[MiscStat3821, _VARIANT_3821]
        | Annotated[Alignment3822, _VARIANT_3822]
        | Annotated[_values.FormId, _VARIANT_3823]
        | Annotated[FormType3824, _VARIANT_3824]
        | Annotated[CriticalStage3825, _VARIANT_3825]
        | Annotated[_values.FormId, _VARIANT_3826]
        | Annotated[_values.FormId, _VARIANT_3827]
        | Annotated[_values.FormId, _VARIANT_3828]
        | Annotated[_values.FormId, _VARIANT_3829]
        | Annotated[_values.FormId, _VARIANT_3830]
        | Annotated[_values.FormId, _VARIANT_3831]
        | Annotated[_values.FormId, _VARIANT_3832]
        | Annotated[_values.FormId, _VARIANT_3833]
        | Annotated[_values.FormId, _VARIANT_3834]
        | Annotated[_values.FormId, _VARIANT_3835]
        | Annotated[_values.FormId, _VARIANT_3836]
        | Annotated[_values.FormId, _VARIANT_3837]
        | Annotated[_values.FormId, _VARIANT_3838]
        | Annotated[_values.FormId, _VARIANT_3839]
        | Annotated[_values.FormId, _VARIANT_3840]
        | Annotated[_values.FormId, _VARIANT_3841]
        | Annotated[_values.FormId, _VARIANT_3842]
        | Annotated[_values.FormId, _VARIANT_3843]
        | Annotated[_values.FormId, _VARIANT_3844]
        | Annotated[_values.FormId, _VARIANT_3845]
        | Annotated[_values.FormId, _VARIANT_3846]
        | Annotated[_values.FormId, _VARIANT_3847]
        | Annotated[VatsValueFunction3848, _VARIANT_3848]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3849,
        ]
        | Annotated[_values.FormId, _VARIANT_3850]
        | Annotated[_values.FormId, _VARIANT_3851]
        | Annotated[_values.FormId, _VARIANT_3852]
        | Annotated[PlayerAction3853, _VARIANT_3853]
        | Annotated[CastingType3854, _VARIANT_3854]
        | Annotated[_values.FormId, _VARIANT_3855]
        | Annotated[_values.FormId, _VARIANT_3856]
        | Annotated[_values.FormId, _VARIANT_3857]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3858,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3859,
        ]
        | Annotated[_values.FormId, _VARIANT_3860]
        | Annotated[FurnitureAnim3861, _VARIANT_3861]
        | Annotated[FurnitureEntry3862, _VARIANT_3862]
        | Annotated[_values.FormId, _VARIANT_3863]
        | Annotated[WardState3864, _VARIANT_3864]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3865,
        ]
        | Annotated[_values.FormId, _VARIANT_3866]
        | Annotated[_values.FormId, _VARIANT_3867]
        | Annotated[_values.FormId, _VARIANT_3868]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_3870]
        | Annotated[bytes, _VARIANT_3871]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3872,
        ]
        | Annotated[float, _VARIANT_3873]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3874,
        ]
        | Annotated[Sex3875, _VARIANT_3875]
        | Annotated[ActorValue3876, _VARIANT_3876]
        | Annotated[CrimeType3877, _VARIANT_3877]
        | Annotated[Axis3878, _VARIANT_3878]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3879,
        ]
        | Annotated[MiscStat3880, _VARIANT_3880]
        | Annotated[Alignment3881, _VARIANT_3881]
        | Annotated[_values.FormId, _VARIANT_3882]
        | Annotated[FormType3883, _VARIANT_3883]
        | Annotated[CriticalStage3884, _VARIANT_3884]
        | Annotated[_values.FormId, _VARIANT_3885]
        | Annotated[_values.FormId, _VARIANT_3886]
        | Annotated[_values.FormId, _VARIANT_3887]
        | Annotated[_values.FormId, _VARIANT_3888]
        | Annotated[_values.FormId, _VARIANT_3889]
        | Annotated[_values.FormId, _VARIANT_3890]
        | Annotated[_values.FormId, _VARIANT_3891]
        | Annotated[_values.FormId, _VARIANT_3892]
        | Annotated[_values.FormId, _VARIANT_3893]
        | Annotated[_values.FormId, _VARIANT_3894]
        | Annotated[_values.FormId, _VARIANT_3895]
        | Annotated[_values.FormId, _VARIANT_3896]
        | Annotated[_values.FormId, _VARIANT_3897]
        | Annotated[_values.FormId, _VARIANT_3898]
        | Annotated[_values.FormId, _VARIANT_3899]
        | Annotated[_values.FormId, _VARIANT_3900]
        | Annotated[_values.FormId, _VARIANT_3901]
        | Annotated[_values.FormId, _VARIANT_3902]
        | Annotated[_values.FormId, _VARIANT_3903]
        | Annotated[_values.FormId, _VARIANT_3904]
        | Annotated[_values.FormId, _VARIANT_3905]
        | Annotated[_values.FormId, _VARIANT_3906]
        | Annotated[VatsValueFunction3907, _VARIANT_3907]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_3909]
            | Annotated[_values.FormId, _VARIANT_3910]
            | Annotated[_values.FormId, _VARIANT_3911]
            | Annotated[_values.FormId, _VARIANT_3912]
            | Annotated[bytes, _VARIANT_3913]
            | Annotated[TargetPart3914, _VARIANT_3914]
            | Annotated[VatsAction3915, _VARIANT_3915]
            | Annotated[bytes, _VARIANT_3916]
            | Annotated[bytes, _VARIANT_3917]
            | Annotated[_values.FormId, _VARIANT_3918]
            | Annotated[_values.FormId, _VARIANT_3919]
            | Annotated[bytes, _VARIANT_3920]
            | Annotated[bytes, _VARIANT_3921]
            | Annotated[bytes, _VARIANT_3922]
            | Annotated[bytes, _VARIANT_3923]
            | Annotated[WeaponType3924, _VARIANT_3924]
            | Annotated[bytes, _VARIANT_3925]
            | Annotated[bytes, _VARIANT_3926]
            | Annotated[ProjectileType3927, _VARIANT_3927]
            | Annotated[DeliveryType3928, _VARIANT_3928]
            | Annotated[CastingType3929, _VARIANT_3929],
            _VARIANT_3908,
        ]
        | Annotated[_values.FormId, _VARIANT_3930]
        | Annotated[_values.FormId, _VARIANT_3931]
        | Annotated[_values.FormId, _VARIANT_3932]
        | Annotated[PlayerAction3933, _VARIANT_3933]
        | Annotated[CastingType3934, _VARIANT_3934]
        | Annotated[_values.FormId, _VARIANT_3935]
        | Annotated[_values.FormId, _VARIANT_3936]
        | Annotated[_values.FormId, _VARIANT_3937]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3938,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3939,
        ]
        | Annotated[_values.FormId, _VARIANT_3940]
        | Annotated[FurnitureAnim3941, _VARIANT_3941]
        | Annotated[FurnitureEntry3942, _VARIANT_3942]
        | Annotated[_values.FormId, _VARIANT_3943]
        | Annotated[WardState3944, _VARIANT_3944]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3945,
        ]
        | Annotated[_values.FormId, _VARIANT_3946]
        | Annotated[_values.FormId, _VARIANT_3947]
        | Annotated[_values.FormId, _VARIANT_3948]
    )
    """Value decoded from this schema node."""

    run_on: RunOn3949
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3951,
        ]
        | Annotated[_values.FormId, _VARIANT_3952]
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
        Annotated[float, _VARIANT_3806]
        | Annotated[_values.FormId, _VARIANT_3807]
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
    def field(self, name: Literal["unused_3809"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_3811]
        | Annotated[bytes, _VARIANT_3812]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3813,
        ]
        | Annotated[float, _VARIANT_3814]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3815,
        ]
        | Annotated[Sex3816, _VARIANT_3816]
        | Annotated[ActorValue3817, _VARIANT_3817]
        | Annotated[CrimeType3818, _VARIANT_3818]
        | Annotated[Axis3819, _VARIANT_3819]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3820,
        ]
        | Annotated[MiscStat3821, _VARIANT_3821]
        | Annotated[Alignment3822, _VARIANT_3822]
        | Annotated[_values.FormId, _VARIANT_3823]
        | Annotated[FormType3824, _VARIANT_3824]
        | Annotated[CriticalStage3825, _VARIANT_3825]
        | Annotated[_values.FormId, _VARIANT_3826]
        | Annotated[_values.FormId, _VARIANT_3827]
        | Annotated[_values.FormId, _VARIANT_3828]
        | Annotated[_values.FormId, _VARIANT_3829]
        | Annotated[_values.FormId, _VARIANT_3830]
        | Annotated[_values.FormId, _VARIANT_3831]
        | Annotated[_values.FormId, _VARIANT_3832]
        | Annotated[_values.FormId, _VARIANT_3833]
        | Annotated[_values.FormId, _VARIANT_3834]
        | Annotated[_values.FormId, _VARIANT_3835]
        | Annotated[_values.FormId, _VARIANT_3836]
        | Annotated[_values.FormId, _VARIANT_3837]
        | Annotated[_values.FormId, _VARIANT_3838]
        | Annotated[_values.FormId, _VARIANT_3839]
        | Annotated[_values.FormId, _VARIANT_3840]
        | Annotated[_values.FormId, _VARIANT_3841]
        | Annotated[_values.FormId, _VARIANT_3842]
        | Annotated[_values.FormId, _VARIANT_3843]
        | Annotated[_values.FormId, _VARIANT_3844]
        | Annotated[_values.FormId, _VARIANT_3845]
        | Annotated[_values.FormId, _VARIANT_3846]
        | Annotated[_values.FormId, _VARIANT_3847]
        | Annotated[VatsValueFunction3848, _VARIANT_3848]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3849,
        ]
        | Annotated[_values.FormId, _VARIANT_3850]
        | Annotated[_values.FormId, _VARIANT_3851]
        | Annotated[_values.FormId, _VARIANT_3852]
        | Annotated[PlayerAction3853, _VARIANT_3853]
        | Annotated[CastingType3854, _VARIANT_3854]
        | Annotated[_values.FormId, _VARIANT_3855]
        | Annotated[_values.FormId, _VARIANT_3856]
        | Annotated[_values.FormId, _VARIANT_3857]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3858,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3859,
        ]
        | Annotated[_values.FormId, _VARIANT_3860]
        | Annotated[FurnitureAnim3861, _VARIANT_3861]
        | Annotated[FurnitureEntry3862, _VARIANT_3862]
        | Annotated[_values.FormId, _VARIANT_3863]
        | Annotated[WardState3864, _VARIANT_3864]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3865,
        ]
        | Annotated[_values.FormId, _VARIANT_3866]
        | Annotated[_values.FormId, _VARIANT_3867]
        | Annotated[_values.FormId, _VARIANT_3868]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_3870]
        | Annotated[bytes, _VARIANT_3871]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3872,
        ]
        | Annotated[float, _VARIANT_3873]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3874,
        ]
        | Annotated[Sex3875, _VARIANT_3875]
        | Annotated[ActorValue3876, _VARIANT_3876]
        | Annotated[CrimeType3877, _VARIANT_3877]
        | Annotated[Axis3878, _VARIANT_3878]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3879,
        ]
        | Annotated[MiscStat3880, _VARIANT_3880]
        | Annotated[Alignment3881, _VARIANT_3881]
        | Annotated[_values.FormId, _VARIANT_3882]
        | Annotated[FormType3883, _VARIANT_3883]
        | Annotated[CriticalStage3884, _VARIANT_3884]
        | Annotated[_values.FormId, _VARIANT_3885]
        | Annotated[_values.FormId, _VARIANT_3886]
        | Annotated[_values.FormId, _VARIANT_3887]
        | Annotated[_values.FormId, _VARIANT_3888]
        | Annotated[_values.FormId, _VARIANT_3889]
        | Annotated[_values.FormId, _VARIANT_3890]
        | Annotated[_values.FormId, _VARIANT_3891]
        | Annotated[_values.FormId, _VARIANT_3892]
        | Annotated[_values.FormId, _VARIANT_3893]
        | Annotated[_values.FormId, _VARIANT_3894]
        | Annotated[_values.FormId, _VARIANT_3895]
        | Annotated[_values.FormId, _VARIANT_3896]
        | Annotated[_values.FormId, _VARIANT_3897]
        | Annotated[_values.FormId, _VARIANT_3898]
        | Annotated[_values.FormId, _VARIANT_3899]
        | Annotated[_values.FormId, _VARIANT_3900]
        | Annotated[_values.FormId, _VARIANT_3901]
        | Annotated[_values.FormId, _VARIANT_3902]
        | Annotated[_values.FormId, _VARIANT_3903]
        | Annotated[_values.FormId, _VARIANT_3904]
        | Annotated[_values.FormId, _VARIANT_3905]
        | Annotated[_values.FormId, _VARIANT_3906]
        | Annotated[VatsValueFunction3907, _VARIANT_3907]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_3909]
            | Annotated[_values.FormId, _VARIANT_3910]
            | Annotated[_values.FormId, _VARIANT_3911]
            | Annotated[_values.FormId, _VARIANT_3912]
            | Annotated[bytes, _VARIANT_3913]
            | Annotated[TargetPart3914, _VARIANT_3914]
            | Annotated[VatsAction3915, _VARIANT_3915]
            | Annotated[bytes, _VARIANT_3916]
            | Annotated[bytes, _VARIANT_3917]
            | Annotated[_values.FormId, _VARIANT_3918]
            | Annotated[_values.FormId, _VARIANT_3919]
            | Annotated[bytes, _VARIANT_3920]
            | Annotated[bytes, _VARIANT_3921]
            | Annotated[bytes, _VARIANT_3922]
            | Annotated[bytes, _VARIANT_3923]
            | Annotated[WeaponType3924, _VARIANT_3924]
            | Annotated[bytes, _VARIANT_3925]
            | Annotated[bytes, _VARIANT_3926]
            | Annotated[ProjectileType3927, _VARIANT_3927]
            | Annotated[DeliveryType3928, _VARIANT_3928]
            | Annotated[CastingType3929, _VARIANT_3929],
            _VARIANT_3908,
        ]
        | Annotated[_values.FormId, _VARIANT_3930]
        | Annotated[_values.FormId, _VARIANT_3931]
        | Annotated[_values.FormId, _VARIANT_3932]
        | Annotated[PlayerAction3933, _VARIANT_3933]
        | Annotated[CastingType3934, _VARIANT_3934]
        | Annotated[_values.FormId, _VARIANT_3935]
        | Annotated[_values.FormId, _VARIANT_3936]
        | Annotated[_values.FormId, _VARIANT_3937]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_3938,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3939,
        ]
        | Annotated[_values.FormId, _VARIANT_3940]
        | Annotated[FurnitureAnim3941, _VARIANT_3941]
        | Annotated[FurnitureEntry3942, _VARIANT_3942]
        | Annotated[_values.FormId, _VARIANT_3943]
        | Annotated[WardState3944, _VARIANT_3944]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3945,
        ]
        | Annotated[_values.FormId, _VARIANT_3946]
        | Annotated[_values.FormId, _VARIANT_3947]
        | Annotated[_values.FormId, _VARIANT_3948]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn3949]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_3951,
        ]
        | Annotated[_values.FormId, _VARIANT_3952]
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


class Condition3800(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT/17:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="FACT/17:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("FACT/17:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("FACT/17:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure3802] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure3802]]:
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


class FactionRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FACT"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "FACT"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="FACT/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="FACT/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "relations": _base.Binding(
            path="FACT/2:Relations",
            kind="repeat",
            name="Relations",
            repeated_path="FACT/2:Relations/repeat/0:Relation",
            child_kind="subrecord",
        ),
        "flags": _base.Binding(
            path="FACT/3:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "exterior_jail_marker": _base.Binding(
            path="FACT/4:Exterior Jail Marker",
            kind="subrecord",
            name="Exterior Jail Marker",
        ),
        "follower_wait_marker": _base.Binding(
            path="FACT/5:Follower Wait Marker",
            kind="subrecord",
            name="Follower Wait Marker",
        ),
        "stolen_goods_container": _base.Binding(
            path="FACT/6:Stolen Goods Container",
            kind="subrecord",
            name="Stolen Goods Container",
        ),
        "player_inventory_container": _base.Binding(
            path="FACT/7:Player Inventory Container",
            kind="subrecord",
            name="Player Inventory Container",
        ),
        "shared_crime_faction_list": _base.Binding(
            path="FACT/8:Shared Crime Faction List",
            kind="subrecord",
            name="Shared Crime Faction List",
        ),
        "jail_outfit": _base.Binding(
            path="FACT/9:Jail Outfit",
            kind="subrecord",
            name="Jail Outfit",
        ),
        "crime_values": _base.Binding(
            path="FACT/10:Crime Values",
            kind="subrecord",
            name="Crime Values",
        ),
        "ranks": _base.Binding(
            path="FACT/11:Ranks",
            kind="repeat",
            name="Ranks",
            repeated_path="FACT/11:Ranks/repeat/0:Rank",
            child_kind="sequence",
        ),
        "vendor_buy_sell_list": _base.Binding(
            path="FACT/12:Vendor Buy/Sell List",
            kind="subrecord",
            name="Vendor Buy/Sell List",
        ),
        "merchant_container": _base.Binding(
            path="FACT/13:Merchant Container",
            kind="subrecord",
            name="Merchant Container",
        ),
        "vendor_values": _base.Binding(
            path="FACT/14:Vendor Values",
            kind="subrecord",
            name="Vendor Values",
        ),
        "location": _base.Binding(
            path="FACT/15:Location",
            kind="subrecord",
            name="Location",
        ),
        "condition_count": _base.Binding(
            path="FACT/16:Condition Count",
            kind="subrecord",
            name="Condition Count",
        ),
        "conditions": _base.Binding(
            path="FACT/17:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="FACT/17:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    relations: tuple[Structure3725, ...] = ()
    """Value decoded from this schema node."""

    flags: Optional[Structure3730] = None
    """Value decoded from this schema node."""

    exterior_jail_marker: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    follower_wait_marker: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    stolen_goods_container: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    player_inventory_container: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    shared_crime_faction_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    jail_outfit: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    crime_values: Optional[Structure3745] = None
    """Value decoded from this schema node."""

    ranks: tuple[Rank3757, ...] = ()
    """Value decoded from this schema node."""

    vendor_buy_sell_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    merchant_container: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    vendor_values: Optional[Structure3771] = None
    """Value decoded from this schema node."""

    location: Optional[Structure3780] = None
    """Value decoded from this schema node."""

    condition_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition3800, ...] = ()
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
        self, name: Literal["relations"]
    ) -> _base.FieldRef[tuple[Structure3725, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[Structure3730]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["exterior_jail_marker"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["follower_wait_marker"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stolen_goods_container"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["player_inventory_container"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["shared_crime_faction_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["jail_outfit"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["crime_values"]
    ) -> _base.FieldRef[Optional[Structure3745]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ranks"]
    ) -> _base.FieldRef[tuple[Rank3757, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vendor_buy_sell_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["merchant_container"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vendor_values"]
    ) -> _base.FieldRef[Optional[Structure3771]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location"]
    ) -> _base.FieldRef[Optional[Structure3780]]:
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
    ) -> _base.FieldRef[tuple[Condition3800, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
