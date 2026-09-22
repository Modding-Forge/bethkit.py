"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base


class Structure3115(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CSTY/1:General/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "offensive_mult": _base.Binding(
            path="CSTY/1:General/payload/0:Offensive Mult",
            kind="primitive",
            name="Offensive Mult",
        ),
        "defensive_mult": _base.Binding(
            path="CSTY/1:General/payload/1:Defensive Mult",
            kind="primitive",
            name="Defensive Mult",
        ),
        "group_offensive_mult": _base.Binding(
            path="CSTY/1:General/payload/2:Group Offensive Mult",
            kind="primitive",
            name="Group Offensive Mult",
        ),
        "equipment_score_mult_melee": _base.Binding(
            path=("CSTY/1:General/payload/3:Equipment Score Mult - Melee"),
            kind="primitive",
            name="Equipment Score Mult - Melee",
        ),
        "equipment_score_mult_magic": _base.Binding(
            path=("CSTY/1:General/payload/4:Equipment Score Mult - Magic"),
            kind="primitive",
            name="Equipment Score Mult - Magic",
        ),
        "equipment_score_mult_ranged": _base.Binding(
            path=("CSTY/1:General/payload/5:Equipment Score Mult - Ranged"),
            kind="primitive",
            name="Equipment Score Mult - Ranged",
        ),
        "equipment_score_mult_shout": _base.Binding(
            path=("CSTY/1:General/payload/6:Equipment Score Mult - Shout"),
            kind="primitive",
            name="Equipment Score Mult - Shout",
        ),
        "equipment_score_mult_unarmed": _base.Binding(
            path=("CSTY/1:General/payload/7:Equipment Score Mult - Unarmed"),
            kind="primitive",
            name="Equipment Score Mult - Unarmed",
        ),
        "equipment_score_mult_staff": _base.Binding(
            path=("CSTY/1:General/payload/8:Equipment Score Mult - Staff"),
            kind="primitive",
            name="Equipment Score Mult - Staff",
        ),
        "avoid_threat_chance": _base.Binding(
            path="CSTY/1:General/payload/9:Avoid Threat Chance",
            kind="primitive",
            name="Avoid Threat Chance",
        ),
    }

    offensive_mult: Optional[float] = None
    """Value decoded from this schema node."""

    defensive_mult: Optional[float] = None
    """Value decoded from this schema node."""

    group_offensive_mult: Optional[float] = None
    """Value decoded from this schema node."""

    equipment_score_mult_melee: Optional[float] = None
    """Value decoded from this schema node."""

    equipment_score_mult_magic: Optional[float] = None
    """Value decoded from this schema node."""

    equipment_score_mult_ranged: Optional[float] = None
    """Value decoded from this schema node."""

    equipment_score_mult_shout: Optional[float] = None
    """Value decoded from this schema node."""

    equipment_score_mult_unarmed: Optional[float] = None
    """Value decoded from this schema node."""

    equipment_score_mult_staff: Optional[float] = None
    """Value decoded from this schema node."""

    avoid_threat_chance: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["offensive_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["defensive_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["group_offensive_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_score_mult_melee"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_score_mult_magic"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_score_mult_ranged"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_score_mult_shout"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_score_mult_unarmed"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_score_mult_staff"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["avoid_threat_chance"]
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


class Structure3129(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CSTY/3:Melee/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "attack_staggered_mult": _base.Binding(
            path="CSTY/3:Melee/payload/0:Attack Staggered Mult",
            kind="primitive",
            name="Attack Staggered Mult",
        ),
        "power_attack_staggered_mult": _base.Binding(
            path=("CSTY/3:Melee/payload/1:Power Attack Staggered Mult"),
            kind="primitive",
            name="Power Attack Staggered Mult",
        ),
        "power_attack_blocking_mult": _base.Binding(
            path="CSTY/3:Melee/payload/2:Power Attack Blocking Mult",
            kind="primitive",
            name="Power Attack Blocking Mult",
        ),
        "bash_mult": _base.Binding(
            path="CSTY/3:Melee/payload/3:Bash Mult",
            kind="primitive",
            name="Bash Mult",
        ),
        "bash_recoil_mult": _base.Binding(
            path="CSTY/3:Melee/payload/4:Bash Recoil Mult",
            kind="primitive",
            name="Bash Recoil Mult",
        ),
        "bash_attack_mult": _base.Binding(
            path="CSTY/3:Melee/payload/5:Bash Attack Mult",
            kind="primitive",
            name="Bash Attack Mult",
        ),
        "bash_power_attack_mult": _base.Binding(
            path="CSTY/3:Melee/payload/6:Bash Power Attack Mult",
            kind="primitive",
            name="Bash Power Attack Mult",
        ),
        "special_attack_mult": _base.Binding(
            path="CSTY/3:Melee/payload/7:Special Attack Mult",
            kind="primitive",
            name="Special Attack Mult",
        ),
    }

    attack_staggered_mult: Optional[float] = None
    """Value decoded from this schema node."""

    power_attack_staggered_mult: Optional[float] = None
    """Value decoded from this schema node."""

    power_attack_blocking_mult: Optional[float] = None
    """Value decoded from this schema node."""

    bash_mult: Optional[float] = None
    """Value decoded from this schema node."""

    bash_recoil_mult: Optional[float] = None
    """Value decoded from this schema node."""

    bash_attack_mult: Optional[float] = None
    """Value decoded from this schema node."""

    bash_power_attack_mult: Optional[float] = None
    """Value decoded from this schema node."""

    special_attack_mult: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["attack_staggered_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["power_attack_staggered_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["power_attack_blocking_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bash_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bash_recoil_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bash_attack_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bash_power_attack_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["special_attack_mult"]
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


class Structure3139(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CSTY/4:Close Range/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "circle_mult": _base.Binding(
            path="CSTY/4:Close Range/payload/0:Circle Mult",
            kind="primitive",
            name="Circle Mult",
        ),
        "fallback_mult": _base.Binding(
            path="CSTY/4:Close Range/payload/1:Fallback Mult",
            kind="primitive",
            name="Fallback Mult",
        ),
        "flank_distance": _base.Binding(
            path="CSTY/4:Close Range/payload/2:Flank Distance",
            kind="primitive",
            name="Flank Distance",
        ),
        "stalk_time": _base.Binding(
            path="CSTY/4:Close Range/payload/3:Stalk Time",
            kind="primitive",
            name="Stalk Time",
        ),
    }

    circle_mult: Optional[float] = None
    """Value decoded from this schema node."""

    fallback_mult: Optional[float] = None
    """Value decoded from this schema node."""

    flank_distance: Optional[float] = None
    """Value decoded from this schema node."""

    stalk_time: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["circle_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fallback_mult"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flank_distance"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stalk_time"]
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


class Structure3145(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CSTY/5:Long Range/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "strafe_mult": _base.Binding(
            path="CSTY/5:Long Range/payload/0:Strafe Mult",
            kind="primitive",
            name="Strafe Mult",
        ),
    }

    strafe_mult: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["strafe_mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure3148(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CSTY/6:Flight/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "hover_chance": _base.Binding(
            path="CSTY/6:Flight/payload/0:Hover Chance",
            kind="primitive",
            name="Hover Chance",
        ),
        "dive_bomb_chance": _base.Binding(
            path="CSTY/6:Flight/payload/1:Dive Bomb Chance",
            kind="primitive",
            name="Dive Bomb Chance",
        ),
        "ground_attack_chance": _base.Binding(
            path="CSTY/6:Flight/payload/2:Ground Attack Chance",
            kind="primitive",
            name="Ground Attack Chance",
        ),
        "hover_time": _base.Binding(
            path="CSTY/6:Flight/payload/3:Hover Time",
            kind="primitive",
            name="Hover Time",
        ),
        "ground_attack_time": _base.Binding(
            path="CSTY/6:Flight/payload/4:Ground Attack Time",
            kind="primitive",
            name="Ground Attack Time",
        ),
        "perch_attack_chance": _base.Binding(
            path="CSTY/6:Flight/payload/5:Perch Attack Chance",
            kind="primitive",
            name="Perch Attack Chance",
        ),
        "perch_attack_time": _base.Binding(
            path="CSTY/6:Flight/payload/6:Perch Attack Time",
            kind="primitive",
            name="Perch Attack Time",
        ),
        "flying_attack_chance": _base.Binding(
            path="CSTY/6:Flight/payload/7:Flying Attack Chance",
            kind="primitive",
            name="Flying Attack Chance",
        ),
    }

    hover_chance: Optional[float] = None
    """Value decoded from this schema node."""

    dive_bomb_chance: Optional[float] = None
    """Value decoded from this schema node."""

    ground_attack_chance: Optional[float] = None
    """Value decoded from this schema node."""

    hover_time: Optional[float] = None
    """Value decoded from this schema node."""

    ground_attack_time: Optional[float] = None
    """Value decoded from this schema node."""

    perch_attack_chance: Optional[float] = None
    """Value decoded from this schema node."""

    perch_attack_time: Optional[float] = None
    """Value decoded from this schema node."""

    flying_attack_chance: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["hover_chance"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["dive_bomb_chance"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ground_attack_chance"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hover_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ground_attack_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perch_attack_chance"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perch_attack_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flying_attack_chance"]
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


class DuelingFlankingAllowDualWielding3158(enum.IntFlag):
    """Named values from the pinned schema."""

    DUELING = 1
    FLANKING = 2
    ALLOW_DUAL_WIELDING = 4


class CombatStyleRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CSTY"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "CSTY"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="CSTY/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "general": _base.Binding(
            path="CSTY/1:General",
            kind="subrecord",
            name="General",
        ),
        "unknown": _base.Binding(
            path="CSTY/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "melee": _base.Binding(
            path="CSTY/3:Melee",
            kind="subrecord",
            name="Melee",
        ),
        "close_range": _base.Binding(
            path="CSTY/4:Close Range",
            kind="subrecord",
            name="Close Range",
        ),
        "long_range": _base.Binding(
            path="CSTY/5:Long Range",
            kind="subrecord",
            name="Long Range",
        ),
        "flight": _base.Binding(
            path="CSTY/6:Flight",
            kind="subrecord",
            name="Flight",
        ),
        "flags": _base.Binding(
            path="CSTY/7:Flags",
            kind="subrecord",
            name="Flags",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    general: Optional[Structure3115] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    melee: Optional[Structure3129] = None
    """Value decoded from this schema node."""

    close_range: Optional[Structure3139] = None
    """Value decoded from this schema node."""

    long_range: Optional[Structure3145] = None
    """Value decoded from this schema node."""

    flight: Optional[Structure3148] = None
    """Value decoded from this schema node."""

    flags: Optional[DuelingFlankingAllowDualWielding3158] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["general"]
    ) -> _base.FieldRef[Optional[Structure3115]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["melee"]
    ) -> _base.FieldRef[Optional[Structure3129]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["close_range"]
    ) -> _base.FieldRef[Optional[Structure3139]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["long_range"]
    ) -> _base.FieldRef[Optional[Structure3145]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flight"]
    ) -> _base.FieldRef[Optional[Structure3148]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[DuelingFlankingAllowDualWielding3158]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
