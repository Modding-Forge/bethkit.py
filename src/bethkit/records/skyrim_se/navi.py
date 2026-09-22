"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Category5028(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    IS_EDITED = 0
    IS_ISLAND = 32
    NOT_EDITED = 64


class CrcHash5039(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    MOVEMENT_MESSAGE_JUMP = 14452494
    COMBAT_PATHING_GOAL_POLICY_WITHDRAW = 29441422
    COMBAT_MAGIC_CASTER_SCRIPT = 35728048
    COMBAT_PATHING_REQUEST_COVERED = 35767353
    COMBAT_MAGIC_CASTER_REANIMATE = 50654367
    PATHING_REQUEST_HIDE = 86566743
    BSPATHING_REQUEST = 87354673
    COMBAT_AREA_SHAPE = 99096483
    PATHING_REQUEST_COVER = 102294899
    COMBAT_PATH_DESTINATION_ACTOR = 106194021
    COMBAT_PATHING_REQUEST_STANDARD = 190505960
    COMBAT_PATHING_GOAL_POLICY_FIND_COVER = 198349747
    COMBAT_INVENTORY_ITEM_SCROLL = 200156176
    MOVEMENT_PARAMETERS = 204001733
    COMBAT_PATHING_GOAL_POLICY_SEARCH = 208145108
    COMBAT_PATHING_GOAL_POLICY_RETREAT = 232922975
    COMBAT_PATHING_DEBUG_DATA = 246093354
    COMBAT_MAGIC_CASTER_ARMOR = 286420040
    COMBAT_PATH_REQUEST_WEIGHTED_MULTI_GOAL = 287766061
    MOVEMENT_MESSAGE_PLAY_IDLE = 295003110
    COVERED_PATH_SHAPE = 302482169
    PATHING_STREAM_LOAD_GAME = 329436994
    COMBAT_SUPPRESSIVE_FIRE_BEHAVIOR = 353054625
    COMBAT_PATH_REQUEST_STRAIGHT_PATH = 404367197
    BSDELAY_EFFECT = 411269967
    COMBAT_APPROACH_TARGET_PATH_CONTROLLER = 431820143
    COMBAT_PATH_BUILDER_STANDARD = 515638094
    COMBAT_TARGET_LOCATION = 518336529
    BGSSTANDARD_SOUND_DEF = 519001098
    COMBAT_MAGIC_CASTER_CLOAK = 578309796
    COMBAT_MAGIC_CASTER_WARD = 587060949
    BGSMUSIC_PALETTE_TRACK = 603355331
    COMBAT_PATHING_GOAL_POLICY_FLEE = 635157103
    COMBAT_INVENTORY_ITEM_THROWN = 637767439
    COMBAT_CHARGING_SEARCH = 745932271
    COMBAT_COVERED_PATH = 796348462
    COMBAT_PATHING_SEARCH_AREA = 807994985
    PATHING_REQUEST = 856600803
    COMBAT_TUNNEL_PATH_CONTROLLER = 888574894
    COMBAT_PATHING_REQUEST_GENERIC = 901039520
    COMBAT_THREAT_EXPLOSION = 929553599
    COMBAT_PATHING_TWEENER = 954547474
    MOVEMENT_NODE_GOAL = 991465547
    COMBAT_COVER_SEARCH_RESULT = 1003533399
    MOVEMENT_MESSAGE_FREEZE_DIRECTION = 1005404939
    COMBAT_THREAT_LOF = 1009668116
    PATHING_REQUEST_FLY = 1012920628
    MOVEMENT_MESSAGE_WARP_TO_MULTIPLE = 1022584044
    COMBAT_MAGIC_CASTER_BOUND_ITEM = 1035615386
    COMBAT_PATH_BUILDER_OPEN = 1048893803
    MASTER_FILE_PATHING_STREAM_WRITE_TO_BUFFER = 1057996340
    COMBAT_MAGIC_CASTER_OFFENSIVE = 1101483921
    COMBAT_PATH_REQUEST_FLYING_ATTACK = 1108373874
    COMBAT_ENTER_COVER_PATH_CONTROLLER = 1190525213
    PATHING_REQUEST_SAFE_STRAIGHT_LINE = 1198764317
    COMBAT_MOVEMENT_REQUEST_FOLLOW_ACTOR = 1286478577
    COMBAT_MATCH_TARGET_AIM_CONTROLLER = 1289411745
    COMBAT_COVER_LOCATION = 1326546475
    COMBAT_VIEW_CONTROLLER_GLANCE = 1378018103
    BGSCOMPOUND_SOUND_DEF = 1415912003
    PATHING_REQUEST_LOS = 1423624789
    COMBAT_AREA_REFERENCE = 1438721403
    COMBAT_AREA_HOLD_POSITION = 1442493525
    COMBAT_TARGET_SELECTOR_PREFERRED = 1458032841
    PATHING_LOCK_DATA = 1478927837
    DIVE_BOMB_PATH_CONTROLLER = 1486147445
    COMBAT_MAGIC_CASTER_RESTORE = 1487276769
    COMBAT_MANTLE_PATH_CONTROLLER = 1490205698
    COMBAT_INVENTORY_ITEM_MELEE = 1523292616
    COMBAT_MAGIC_CASTER_TARGET_EFFECT = 1523759377
    COMBAT_TRACK_TARGET_AIM_CONTROLLER = 1524217151
    COMBAT_PATHING_GOAL_POLICY_FIND_POTENTIAL_COV_48ef8cdf = 1528549127
    COMBAT_PATHING_SEARCH_POLICY_CHARGE = 1551233374
    MOVEMENT_MESSAGE_ACTIVATE_DOOR = 1556259383
    MOVEMENT_MESSAGE_SET_STATIC_PATH = 1634096085
    EQUIPPED_WEAPON_DATA = 1648478049
    COMBAT_PATH_REQUEST_ROTATE_PATH = 1649733113
    COMBAT_MELEE_AIM_CONTROLLER = 1687321468
    COMBAT_INVENTORY_ITEM_TORCH = 1725290782
    MOVEMENT_MESSAGE_WARP_TO_LOCATION = 1742376995
    COMBAT_PATH_TELEPORT_EVENT = 1774313050
    QUEST_PATHING_REQUEST = 1794183568
    BGSMUSIC_SINGLE_TRACK = 1859641416
    COMBAT_PATHING_SEARCH_POLICY_FLANK = 1859670927
    COMBAT_ACQUIRE_SEARCH_DEBUG_DATA = 1864149639
    COMBAT_PATHING_SEARCH_POLICY_WITHDRAW = 1880384041
    COMBAT_INVENTORY_ITEM_RANGED = 1907830321
    MOVEMENT_NODE_AVOIDANCE = 1922115098
    PATHING_STREAM_MASTER_FILE_READ = 1937243600
    MOVEMENT_MESSAGE_APPROACHING_DOOR = 1986263146
    MASTER_FILE_PATHING_STREAM_GET_SIZE = 1996237907
    MOVEMENT_MESSAGE_ACTOR_COLLISION = 2007202810
    BSPATHING_SOLUTION = 2086792155
    COMBAT_PATH_MOVEMENT_MESSAGE = 2164507637
    COMBAT_INVENTORY_ITEM_ONE_HANDED_BLOCK = 2166446109
    PATHING_REQUEST_FLY_HOVER = 2203258939
    COMBAT_INVENTORY_ITEM_MAGIC_T = 2216848341
    BSOVERDRIVE = 2252866750
    COMBAT_AIM_CONTROLLER = 2261987488
    COMBAT_FIND_COVER_PATH_SPEED_CONTROLLER = 2286368726
    PATHING_REQUEST_STOP_MOVING = 2334216879
    COMBAT_PATH_REQUEST_LANDING = 2338449283
    COMBAT_PATHING_GOAL_POLICY_DISTRACT = 2345494319
    MOVEMENT_MESSAGE_PATH_FAILED = 2345596612
    COMBAT_PATH_DESTINATION_FOLLOW_ACTOR = 2369910579
    COMBAT_CHANGE_POSITION_PATH_CONTROLLER = 2381779083
    COMBAT_PATHING_GOAL_POLICY_FIND_TARGET_LOCATION = 2390329851
    COMBAT_PATHING_GOAL_POLICY_FIND_FLANK_COVER = 2424607453
    COMBAT_PATHING_GOAL_POLICY_AVOID_THREAT = 2437945004
    COMBAT_COVER_SEARCH = 2470484821
    COMBAT_PATHING_REQUEST_MULTI_GOAL = 2511090863
    PATHING_REQUEST_FLY_TAKE_OFF = 2563032697
    COMBAT_COVERED_PATH_DEBUG_DATA = 2600789703
    COMBAT_INVENTORY_ITEM_MAGIC = 2620001095
    COMBAT_TARGET_LOCATION_SEARCH = 2620140026
    COMBAT_MELEE_DEBUG_DATA = 2673651155
    COMBAT_POSITION_TRACKER = 2698846825
    COMBAT_THREAT_PROJECTILE = 2707468047
    BGSMUSIC_SILENCE_TRACK = 2712257749
    COMBAT_MAGIC_CASTER_INVISIBILITY = 2735037691
    PATHING_REQUEST_FLY_ACTION = 2768377681
    COMBAT_PATHING_GOAL_POLICY_FIND_VALID_LOCATION = 2769519817
    PATHING_CELL = 2783551548
    COMBAT_THREAT_MELEE = 2812417382
    COMBAT_AREA_STANDARD = 2847779582
    COMBAT_PROJECTILE_DEBUG_DATA = 2865735682
    COMBAT_PATH_REQUEST_HOVER = 2878481748
    COMBAT_PATHING_GOAL_POLICY_INVESTIGATE_LOCATION = 2878835861
    COMBAT_INVENTORY_ITEM_POTION = 2890902078
    COVERED_PATH = 2980725208
    COMBAT_PATHING_GOAL_POLICY_SEARCH_WANDER = 3018353308
    COMBAT_MAGIC_CASTER_DISARM = 3065052333
    BSPATHING_STREAM_SIMPLE_BUFFER_WRITE = 3099141803
    COMBAT_PATHING_REQUEST_ADAPTER = 3123118095
    COMBAT_PATHING_GOAL_POLICY_COVERED = 3127703440
    COMBAT_PATHING_GOAL_POLICY_FIND_ATTACK_LOCATION = 3165609079
    MOVEMENT_PARAMETERS_FIXED = 3168597800
    COMBAT_DISABLE_AIM_CONTROLLER = 3189992137
    COMBAT_PATH_REQUEST_MULTI_GOAL = 3200829835
    COMBAT_CLUSTER = 3234170005
    COMBAT_TARGET_LOCATION_SEARCH_RESULT = 3274785694
    COMBAT_TARGET_SELECTOR_STANDARD = 3279002501
    MOVEMENT_MESSAGE_NEW_PATH_IMMEDIATE = 3302487377
    COMBAT_MAGIC_CASTER_LIGHT = 3308244547
    COMBAT_VIEW_CONTROLLER_PATH = 3311675475
    PATHING_STREAM_SAVE_GAME = 3317009419
    PATHING_REQUEST_ROTATE = 3338845019
    COMBAT_ANIMATED_PATH = 3342165380
    COMBAT_PATH_DESTINATION_REFS = 3355824744
    MOVEMENT_MESSAGE_BLOCKED = 3367245118
    COMBAT_VIEW_CONTROLLER_STANDARD = 3368846076
    PATHING_REQUEST_OPTIMAL_LOCATION = 3395429672
    COMBAT_VIEW_CONTROLLER = 3415245644
    NO_SUPPORT = 3444467653
    MOVEMENT_MESSAGE_NEW_PATH = 3454881635
    PATHING_REQUEST_FLY_ORBIT = 3455689468
    COMBAT_TARGET_SELECTOR_RANDOM = 3461407690
    COMBAT_COVER_SEARCH_DEBUG_DATA = 3472009340
    COMBAT_DEBUG_TASK_PATH = 3499289866
    COMBAT_PATHING_GOAL_POLICY_FOLLOW = 3500971267
    COMBAT_INVENTORY_ITEM_GRENADE = 3506583512
    COMBAT_PATH_DESTINATION_REF = 3531860033
    CHARACTER_BUMPER = 3534855040
    COMBAT_MAGIC_CASTER_SUMMON = 3536474211
    COMBAT_SHARED_PATH = 3573784222
    COMBAT_PATHING_SEARCH_POLICY_STANDARD = 3577604656
    COMBAT_SEARCH_LOCK_DATA = 3579642195
    COMBAT_FLANKING_SEARCH = 3602691990
    COMBAT_TARGET_SELECTOR = 3605617543
    COMBAT_INVENTORY_ITEM_STAFF = 3611431419
    MOVEMENT_MESSAGE_PATH_COMPLETE = 3612839833
    COMBAT_PATHING_GOAL_POLICY_FLANK_DISTANT = 3669662748
    COMBAT_PATH_REQUEST_STANDARD = 3690812754
    COMBAT_PATHING_SEARCH_POLICY_COVERED = 3736525268
    COMBAT_AREA_SHAPE_175 = 3755594389
    COMBAT_MAGIC_CASTER_CHAMELEON = 3784306040
    COMBAT_PATH_DESTINATION_NONE = 3813703872
    COMBAT_PATHING_GOAL_POLICY_FLANK = 3820318388
    COMBAT_PATH = 3829955501
    PATHING_DOOR = 3834344435
    COMBAT_PATH_REQUEST_ORBIT = 3845691283
    COMBAT_MAGIC_CASTER_STAGGER = 3868507153
    COMBAT_PATHING_GOAL_POLICY_LOCATION = 3934383067
    PATHING_REQUEST_CLOSE_POINT = 3948861556
    COMBAT_MAGIC_CASTER_PARALYZE = 3959506843
    BGSAUTO_WEAPON_SOUND_DEF = 3977607907
    COMBAT_PATHING_GOAL_POLICY_CHARGE = 3992155463
    COMBAT_DISABLE_ACTION_CONTROLLER = 3994862791
    COMBAT_PATHING_GOAL_POLICY_RETURN_TO_COMBAT_AREA = 4005394292
    BSSTATE_VARIABLE_FILTER = 4015480703
    COMBAT_PROJECTILE_AIM_CONTROLLER = 4033772177
    PATHING_REQUEST_FLY_LAND = 4034260727
    COMBAT_PATH_REQUEST_GENERIC = 4061431877
    COMBAT_PATH_DESTINATION_LOCATIONS = 4069969691
    PATHING_REQUEST_CLOSEST_GOAL = 4078257067
    COMBAT_PATH_DESTINATION_LOCATION = 4107228448
    COMBAT_TARGET_SELECTOR_FIXED = 4155603900
    COMBAT_INVENTORY_ITEM_SHIELD = 4167747707
    COMBAT_PATH_MOVEMENT_MESSAGE_EVENT = 4173290280
    COMBAT_PATHING_SEARCH_POLICY_DISTRACT = 4195891336
    PATHING_REQUEST_FLEE = 4196885454
    COMBAT_CLUSTER_SHAPE = 4216207720
    WATER = 4241542339
    COMBAT_FOLLOW_TARGET_PATH_CONTROLLER = 4246130165
    COMBAT_PATH_REQUEST_FLIGHT = 4257005617
    BSPATHING_STREAM_SIMPLE_BUFFER_READ = 4284120057


class Door5038(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/8:D"
        "oor Links/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "crc_hash": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/8:D"
                "oor Links/element/0:CRC Hash"
            ),
            kind="primitive",
            name="CRC Hash",
        ),
        "door_ref": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/8:D"
                "oor Links/element/1:Door Ref"
            ),
            kind="primitive",
            name="Door Ref",
        ),
    }

    crc_hash: CrcHash5039
    """Value decoded from this schema node."""

    door_ref: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["crc_hash"]) -> _base.FieldRef[CrcHash5039]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["door_ref"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class IsIsland5041(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_5043: _base.Variant = _base.Variant(
    path=(
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
        "Island/variants/0:Unused"
    )
)


class Triangle5052(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
        "Island/variants/1:Island Data/6:Triangles/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "vertices": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/6:Triangles/element/0:Ve"
                "rtices"
            ),
            kind="array",
            name="Vertices",
        ),
    }

    vertices: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)], ...
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["vertices"]
    ) -> _base.FieldRef[
        tuple[
            Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)],
            ...,
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


class Vertex5056(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
        "Island/variants/1:Island Data/7:Vertices/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/7:Vertices/element/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/7:Vertices/element/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/7:Vertices/element/2:Z"
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


class IslandData5044(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
        "Island/variants/1:Island Data"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "min_x": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/0:Min X"
            ),
            kind="primitive",
            name="Min X",
        ),
        "min_y": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/1:Min Y"
            ),
            kind="primitive",
            name="Min Y",
        ),
        "min_z": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/2:Min Z"
            ),
            kind="primitive",
            name="Min Z",
        ),
        "max_x": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/3:Max X"
            ),
            kind="primitive",
            name="Max X",
        ),
        "max_y": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/4:Max Y"
            ),
            kind="primitive",
            name="Max Y",
        ),
        "max_z": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/5:Max Z"
            ),
            kind="primitive",
            name="Max Z",
        ),
        "triangles": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/6:Triangles"
            ),
            kind="array",
            name="Triangles",
        ),
        "vertices": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
                "Island/variants/1:Island Data/7:Vertices"
            ),
            kind="array",
            name="Vertices",
        ),
    }

    min_x: float
    """Value decoded from this schema node."""

    min_y: float
    """Value decoded from this schema node."""

    min_z: float
    """Value decoded from this schema node."""

    max_x: float
    """Value decoded from this schema node."""

    max_y: float
    """Value decoded from this schema node."""

    max_z: float
    """Value decoded from this schema node."""

    triangles: tuple[Triangle5052, ...]
    """Value decoded from this schema node."""

    vertices: tuple[Vertex5056, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["min_x"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["min_y"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["min_z"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_x"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_y"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_z"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["triangles"]
    ) -> _base.FieldRef[tuple[Triangle5052, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vertices"]
    ) -> _base.FieldRef[tuple[Vertex5056, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_5044: _base.Variant = _base.Variant(
    path=(
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:"
        "Island/variants/1:Island Data"
    )
)


class CrcHash5061(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    MOVEMENT_MESSAGE_JUMP = 14452494
    COMBAT_PATHING_GOAL_POLICY_WITHDRAW = 29441422
    COMBAT_MAGIC_CASTER_SCRIPT = 35728048
    COMBAT_PATHING_REQUEST_COVERED = 35767353
    COMBAT_MAGIC_CASTER_REANIMATE = 50654367
    PATHING_REQUEST_HIDE = 86566743
    BSPATHING_REQUEST = 87354673
    COMBAT_AREA_SHAPE = 99096483
    PATHING_REQUEST_COVER = 102294899
    COMBAT_PATH_DESTINATION_ACTOR = 106194021
    COMBAT_PATHING_REQUEST_STANDARD = 190505960
    COMBAT_PATHING_GOAL_POLICY_FIND_COVER = 198349747
    COMBAT_INVENTORY_ITEM_SCROLL = 200156176
    MOVEMENT_PARAMETERS = 204001733
    COMBAT_PATHING_GOAL_POLICY_SEARCH = 208145108
    COMBAT_PATHING_GOAL_POLICY_RETREAT = 232922975
    COMBAT_PATHING_DEBUG_DATA = 246093354
    COMBAT_MAGIC_CASTER_ARMOR = 286420040
    COMBAT_PATH_REQUEST_WEIGHTED_MULTI_GOAL = 287766061
    MOVEMENT_MESSAGE_PLAY_IDLE = 295003110
    COVERED_PATH_SHAPE = 302482169
    PATHING_STREAM_LOAD_GAME = 329436994
    COMBAT_SUPPRESSIVE_FIRE_BEHAVIOR = 353054625
    COMBAT_PATH_REQUEST_STRAIGHT_PATH = 404367197
    BSDELAY_EFFECT = 411269967
    COMBAT_APPROACH_TARGET_PATH_CONTROLLER = 431820143
    COMBAT_PATH_BUILDER_STANDARD = 515638094
    COMBAT_TARGET_LOCATION = 518336529
    BGSSTANDARD_SOUND_DEF = 519001098
    COMBAT_MAGIC_CASTER_CLOAK = 578309796
    COMBAT_MAGIC_CASTER_WARD = 587060949
    BGSMUSIC_PALETTE_TRACK = 603355331
    COMBAT_PATHING_GOAL_POLICY_FLEE = 635157103
    COMBAT_INVENTORY_ITEM_THROWN = 637767439
    COMBAT_CHARGING_SEARCH = 745932271
    COMBAT_COVERED_PATH = 796348462
    COMBAT_PATHING_SEARCH_AREA = 807994985
    PATHING_REQUEST = 856600803
    COMBAT_TUNNEL_PATH_CONTROLLER = 888574894
    COMBAT_PATHING_REQUEST_GENERIC = 901039520
    COMBAT_THREAT_EXPLOSION = 929553599
    COMBAT_PATHING_TWEENER = 954547474
    MOVEMENT_NODE_GOAL = 991465547
    COMBAT_COVER_SEARCH_RESULT = 1003533399
    MOVEMENT_MESSAGE_FREEZE_DIRECTION = 1005404939
    COMBAT_THREAT_LOF = 1009668116
    PATHING_REQUEST_FLY = 1012920628
    MOVEMENT_MESSAGE_WARP_TO_MULTIPLE = 1022584044
    COMBAT_MAGIC_CASTER_BOUND_ITEM = 1035615386
    COMBAT_PATH_BUILDER_OPEN = 1048893803
    MASTER_FILE_PATHING_STREAM_WRITE_TO_BUFFER = 1057996340
    COMBAT_MAGIC_CASTER_OFFENSIVE = 1101483921
    COMBAT_PATH_REQUEST_FLYING_ATTACK = 1108373874
    COMBAT_ENTER_COVER_PATH_CONTROLLER = 1190525213
    PATHING_REQUEST_SAFE_STRAIGHT_LINE = 1198764317
    COMBAT_MOVEMENT_REQUEST_FOLLOW_ACTOR = 1286478577
    COMBAT_MATCH_TARGET_AIM_CONTROLLER = 1289411745
    COMBAT_COVER_LOCATION = 1326546475
    COMBAT_VIEW_CONTROLLER_GLANCE = 1378018103
    BGSCOMPOUND_SOUND_DEF = 1415912003
    PATHING_REQUEST_LOS = 1423624789
    COMBAT_AREA_REFERENCE = 1438721403
    COMBAT_AREA_HOLD_POSITION = 1442493525
    COMBAT_TARGET_SELECTOR_PREFERRED = 1458032841
    PATHING_LOCK_DATA = 1478927837
    DIVE_BOMB_PATH_CONTROLLER = 1486147445
    COMBAT_MAGIC_CASTER_RESTORE = 1487276769
    COMBAT_MANTLE_PATH_CONTROLLER = 1490205698
    COMBAT_INVENTORY_ITEM_MELEE = 1523292616
    COMBAT_MAGIC_CASTER_TARGET_EFFECT = 1523759377
    COMBAT_TRACK_TARGET_AIM_CONTROLLER = 1524217151
    COMBAT_PATHING_GOAL_POLICY_FIND_POTENTIAL_COV_48ef8cdf = 1528549127
    COMBAT_PATHING_SEARCH_POLICY_CHARGE = 1551233374
    MOVEMENT_MESSAGE_ACTIVATE_DOOR = 1556259383
    MOVEMENT_MESSAGE_SET_STATIC_PATH = 1634096085
    EQUIPPED_WEAPON_DATA = 1648478049
    COMBAT_PATH_REQUEST_ROTATE_PATH = 1649733113
    COMBAT_MELEE_AIM_CONTROLLER = 1687321468
    COMBAT_INVENTORY_ITEM_TORCH = 1725290782
    MOVEMENT_MESSAGE_WARP_TO_LOCATION = 1742376995
    COMBAT_PATH_TELEPORT_EVENT = 1774313050
    QUEST_PATHING_REQUEST = 1794183568
    BGSMUSIC_SINGLE_TRACK = 1859641416
    COMBAT_PATHING_SEARCH_POLICY_FLANK = 1859670927
    COMBAT_ACQUIRE_SEARCH_DEBUG_DATA = 1864149639
    COMBAT_PATHING_SEARCH_POLICY_WITHDRAW = 1880384041
    COMBAT_INVENTORY_ITEM_RANGED = 1907830321
    MOVEMENT_NODE_AVOIDANCE = 1922115098
    PATHING_STREAM_MASTER_FILE_READ = 1937243600
    MOVEMENT_MESSAGE_APPROACHING_DOOR = 1986263146
    MASTER_FILE_PATHING_STREAM_GET_SIZE = 1996237907
    MOVEMENT_MESSAGE_ACTOR_COLLISION = 2007202810
    BSPATHING_SOLUTION = 2086792155
    COMBAT_PATH_MOVEMENT_MESSAGE = 2164507637
    COMBAT_INVENTORY_ITEM_ONE_HANDED_BLOCK = 2166446109
    PATHING_REQUEST_FLY_HOVER = 2203258939
    COMBAT_INVENTORY_ITEM_MAGIC_T = 2216848341
    BSOVERDRIVE = 2252866750
    COMBAT_AIM_CONTROLLER = 2261987488
    COMBAT_FIND_COVER_PATH_SPEED_CONTROLLER = 2286368726
    PATHING_REQUEST_STOP_MOVING = 2334216879
    COMBAT_PATH_REQUEST_LANDING = 2338449283
    COMBAT_PATHING_GOAL_POLICY_DISTRACT = 2345494319
    MOVEMENT_MESSAGE_PATH_FAILED = 2345596612
    COMBAT_PATH_DESTINATION_FOLLOW_ACTOR = 2369910579
    COMBAT_CHANGE_POSITION_PATH_CONTROLLER = 2381779083
    COMBAT_PATHING_GOAL_POLICY_FIND_TARGET_LOCATION = 2390329851
    COMBAT_PATHING_GOAL_POLICY_FIND_FLANK_COVER = 2424607453
    COMBAT_PATHING_GOAL_POLICY_AVOID_THREAT = 2437945004
    COMBAT_COVER_SEARCH = 2470484821
    COMBAT_PATHING_REQUEST_MULTI_GOAL = 2511090863
    PATHING_REQUEST_FLY_TAKE_OFF = 2563032697
    COMBAT_COVERED_PATH_DEBUG_DATA = 2600789703
    COMBAT_INVENTORY_ITEM_MAGIC = 2620001095
    COMBAT_TARGET_LOCATION_SEARCH = 2620140026
    COMBAT_MELEE_DEBUG_DATA = 2673651155
    COMBAT_POSITION_TRACKER = 2698846825
    COMBAT_THREAT_PROJECTILE = 2707468047
    BGSMUSIC_SILENCE_TRACK = 2712257749
    COMBAT_MAGIC_CASTER_INVISIBILITY = 2735037691
    PATHING_REQUEST_FLY_ACTION = 2768377681
    COMBAT_PATHING_GOAL_POLICY_FIND_VALID_LOCATION = 2769519817
    PATHING_CELL = 2783551548
    COMBAT_THREAT_MELEE = 2812417382
    COMBAT_AREA_STANDARD = 2847779582
    COMBAT_PROJECTILE_DEBUG_DATA = 2865735682
    COMBAT_PATH_REQUEST_HOVER = 2878481748
    COMBAT_PATHING_GOAL_POLICY_INVESTIGATE_LOCATION = 2878835861
    COMBAT_INVENTORY_ITEM_POTION = 2890902078
    COVERED_PATH = 2980725208
    COMBAT_PATHING_GOAL_POLICY_SEARCH_WANDER = 3018353308
    COMBAT_MAGIC_CASTER_DISARM = 3065052333
    BSPATHING_STREAM_SIMPLE_BUFFER_WRITE = 3099141803
    COMBAT_PATHING_REQUEST_ADAPTER = 3123118095
    COMBAT_PATHING_GOAL_POLICY_COVERED = 3127703440
    COMBAT_PATHING_GOAL_POLICY_FIND_ATTACK_LOCATION = 3165609079
    MOVEMENT_PARAMETERS_FIXED = 3168597800
    COMBAT_DISABLE_AIM_CONTROLLER = 3189992137
    COMBAT_PATH_REQUEST_MULTI_GOAL = 3200829835
    COMBAT_CLUSTER = 3234170005
    COMBAT_TARGET_LOCATION_SEARCH_RESULT = 3274785694
    COMBAT_TARGET_SELECTOR_STANDARD = 3279002501
    MOVEMENT_MESSAGE_NEW_PATH_IMMEDIATE = 3302487377
    COMBAT_MAGIC_CASTER_LIGHT = 3308244547
    COMBAT_VIEW_CONTROLLER_PATH = 3311675475
    PATHING_STREAM_SAVE_GAME = 3317009419
    PATHING_REQUEST_ROTATE = 3338845019
    COMBAT_ANIMATED_PATH = 3342165380
    COMBAT_PATH_DESTINATION_REFS = 3355824744
    MOVEMENT_MESSAGE_BLOCKED = 3367245118
    COMBAT_VIEW_CONTROLLER_STANDARD = 3368846076
    PATHING_REQUEST_OPTIMAL_LOCATION = 3395429672
    COMBAT_VIEW_CONTROLLER = 3415245644
    NO_SUPPORT = 3444467653
    MOVEMENT_MESSAGE_NEW_PATH = 3454881635
    PATHING_REQUEST_FLY_ORBIT = 3455689468
    COMBAT_TARGET_SELECTOR_RANDOM = 3461407690
    COMBAT_COVER_SEARCH_DEBUG_DATA = 3472009340
    COMBAT_DEBUG_TASK_PATH = 3499289866
    COMBAT_PATHING_GOAL_POLICY_FOLLOW = 3500971267
    COMBAT_INVENTORY_ITEM_GRENADE = 3506583512
    COMBAT_PATH_DESTINATION_REF = 3531860033
    CHARACTER_BUMPER = 3534855040
    COMBAT_MAGIC_CASTER_SUMMON = 3536474211
    COMBAT_SHARED_PATH = 3573784222
    COMBAT_PATHING_SEARCH_POLICY_STANDARD = 3577604656
    COMBAT_SEARCH_LOCK_DATA = 3579642195
    COMBAT_FLANKING_SEARCH = 3602691990
    COMBAT_TARGET_SELECTOR = 3605617543
    COMBAT_INVENTORY_ITEM_STAFF = 3611431419
    MOVEMENT_MESSAGE_PATH_COMPLETE = 3612839833
    COMBAT_PATHING_GOAL_POLICY_FLANK_DISTANT = 3669662748
    COMBAT_PATH_REQUEST_STANDARD = 3690812754
    COMBAT_PATHING_SEARCH_POLICY_COVERED = 3736525268
    COMBAT_AREA_SHAPE_175 = 3755594389
    COMBAT_MAGIC_CASTER_CHAMELEON = 3784306040
    COMBAT_PATH_DESTINATION_NONE = 3813703872
    COMBAT_PATHING_GOAL_POLICY_FLANK = 3820318388
    COMBAT_PATH = 3829955501
    PATHING_DOOR = 3834344435
    COMBAT_PATH_REQUEST_ORBIT = 3845691283
    COMBAT_MAGIC_CASTER_STAGGER = 3868507153
    COMBAT_PATHING_GOAL_POLICY_LOCATION = 3934383067
    PATHING_REQUEST_CLOSE_POINT = 3948861556
    COMBAT_MAGIC_CASTER_PARALYZE = 3959506843
    BGSAUTO_WEAPON_SOUND_DEF = 3977607907
    COMBAT_PATHING_GOAL_POLICY_CHARGE = 3992155463
    COMBAT_DISABLE_ACTION_CONTROLLER = 3994862791
    COMBAT_PATHING_GOAL_POLICY_RETURN_TO_COMBAT_AREA = 4005394292
    BSSTATE_VARIABLE_FILTER = 4015480703
    COMBAT_PROJECTILE_AIM_CONTROLLER = 4033772177
    PATHING_REQUEST_FLY_LAND = 4034260727
    COMBAT_PATH_REQUEST_GENERIC = 4061431877
    COMBAT_PATH_DESTINATION_LOCATIONS = 4069969691
    PATHING_REQUEST_CLOSEST_GOAL = 4078257067
    COMBAT_PATH_DESTINATION_LOCATION = 4107228448
    COMBAT_TARGET_SELECTOR_FIXED = 4155603900
    COMBAT_INVENTORY_ITEM_SHIELD = 4167747707
    COMBAT_PATH_MOVEMENT_MESSAGE_EVENT = 4173290280
    COMBAT_PATHING_SEARCH_POLICY_DISTRACT = 4195891336
    PATHING_REQUEST_FLEE = 4196885454
    COMBAT_CLUSTER_SHAPE = 4216207720
    WATER = 4241542339
    COMBAT_FOLLOW_TARGET_PATH_CONTROLLER = 4246130165
    COMBAT_PATH_REQUEST_FLIGHT = 4257005617
    BSPATHING_STREAM_SIMPLE_BUFFER_READ = 4284120057


class Coordinates5064(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
        "PathingCell/2:Parent/variants/0:Coordinates"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "grid_y": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
                "PathingCell/2:Parent/variants/0:Coordinates/0:Grid Y"
            ),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
                "PathingCell/2:Parent/variants/0:Coordinates/1:Grid X"
            ),
            kind="primitive",
            name="Grid X",
        ),
    }

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
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


_VARIANT_5064: _base.Variant = _base.Variant(
    path=(
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
        "PathingCell/2:Parent/variants/0:Coordinates"
    )
)


_VARIANT_5067: _base.Variant = _base.Variant(
    path=(
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
        "PathingCell/2:Parent/variants/1:Parent Cell"
    )
)


class PathingCell5060(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:PathingCell"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "crc_hash": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
                "PathingCell/0:CRC Hash"
            ),
            kind="primitive",
            name="CRC Hash",
        ),
        "parent_worldspace": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
                "PathingCell/1:Parent Worldspace"
            ),
            kind="primitive",
            name="Parent Worldspace",
        ),
        "parent": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
                "PathingCell/2:Parent"
            ),
            kind="union",
            name="Parent",
        ),
    }

    crc_hash: CrcHash5061
    """Value decoded from this schema node."""

    parent_worldspace: _values.FormId
    """Value decoded from this schema node."""

    parent: (
        Annotated[Coordinates5064, _VARIANT_5064]
        | Annotated[_values.FormId, _VARIANT_5067]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["crc_hash"]) -> _base.FieldRef[CrcHash5061]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parent_worldspace"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parent"]
    ) -> _base.FieldRef[
        Annotated[Coordinates5064, _VARIANT_5064]
        | Annotated[_values.FormId, _VARIANT_5067]
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


class Structure5026(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "navmesh": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/0:Navmesh"
            ),
            kind="primitive",
            name="Navmesh",
        ),
        "category": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/1:Category"
            ),
            kind="primitive",
            name="Category",
        ),
        "x": _base.Binding(
            path=("NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/2:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/3:Y"),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=("NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/4:Z"),
            kind="primitive",
            name="Z",
        ),
        "preferred_merges_flag": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/5:P"
                "referred Merges Flag"
            ),
            kind="primitive",
            name="Preferred Merges Flag",
        ),
        "edge_links": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/6:E"
                "dge Links"
            ),
            kind="array",
            name="Edge Links",
        ),
        "preferred_edge_links": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/7:P"
                "referred Edge Links"
            ),
            kind="array",
            name="Preferred Edge Links",
        ),
        "door_links": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/8:D"
                "oor Links"
            ),
            kind="array",
            name="Door Links",
        ),
        "is_island": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/9:Is Island"
            ),
            kind="primitive",
            name="Is Island",
        ),
        "island": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/10:Island"
            ),
            kind="union",
            name="Island",
        ),
        "pathing_cell": _base.Binding(
            path=(
                "NAVI/2:Navmesh Infos/repeat/0:Navmesh Info/payload/11:"
                "PathingCell"
            ),
            kind="struct",
            name="PathingCell",
        ),
    }

    navmesh: _values.FormId
    """Value decoded from this schema node."""

    category: Category5028
    """Value decoded from this schema node."""

    x: float
    """Value decoded from this schema node."""

    y: float
    """Value decoded from this schema node."""

    z: float
    """Value decoded from this schema node."""

    preferred_merges_flag: bytes
    """Value decoded from this schema node."""

    edge_links: tuple[_values.FormId, ...]
    """Value decoded from this schema node."""

    preferred_edge_links: tuple[_values.FormId, ...]
    """Value decoded from this schema node."""

    door_links: tuple[Door5038, ...]
    """Value decoded from this schema node."""

    is_island: IsIsland5041
    """Value decoded from this schema node."""

    island: (
        Annotated[bytes, _VARIANT_5043]
        | Annotated[IslandData5044, _VARIANT_5044]
    )
    """Value decoded from this schema node."""

    pathing_cell: PathingCell5060
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["navmesh"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["category"]) -> _base.FieldRef[Category5028]:
        """Returns the typed field reference."""

        ...

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
    def field(
        self, name: Literal["preferred_merges_flag"]
    ) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["edge_links"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["preferred_edge_links"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["door_links"]
    ) -> _base.FieldRef[tuple[Door5038, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["is_island"]) -> _base.FieldRef[IsIsland5041]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["island"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_5043]
        | Annotated[IslandData5044, _VARIANT_5044]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["pathing_cell"]
    ) -> _base.FieldRef[PathingCell5060]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class RoadMarker5074(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NAVI/3:Precomputed Pathing/payload/1:Road Marker Index/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "navmesh": _base.Binding(
            path=(
                "NAVI/3:Precomputed Pathing/payload/1:Road Marker Index"
                "/element/0:Navmesh"
            ),
            kind="primitive",
            name="Navmesh",
        ),
        "index": _base.Binding(
            path=(
                "NAVI/3:Precomputed Pathing/payload/1:Road Marker Index"
                "/element/1:Index"
            ),
            kind="primitive",
            name="Index",
        ),
    }

    navmesh: _values.FormId
    """Value decoded from this schema node."""

    index: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["navmesh"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["index"]
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


class Structure5069(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NAVI/3:Precomputed Pathing/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "precomputed_paths": _base.Binding(
            path=("NAVI/3:Precomputed Pathing/payload/0:Precomputed Paths"),
            kind="array",
            name="Precomputed Paths",
        ),
        "road_marker_index": _base.Binding(
            path=("NAVI/3:Precomputed Pathing/payload/1:Road Marker Index"),
            kind="array",
            name="Road Marker Index",
        ),
    }

    precomputed_paths: tuple[tuple[_values.FormId, ...], ...]
    """Value decoded from this schema node."""

    road_marker_index: tuple[RoadMarker5074, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["precomputed_paths"]
    ) -> _base.FieldRef[tuple[tuple[_values.FormId, ...], ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["road_marker_index"]
    ) -> _base.FieldRef[tuple[RoadMarker5074, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class NavmeshInfoMapRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NAVI"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "NAVI"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="NAVI/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "version": _base.Binding(
            path="NAVI/1:Version",
            kind="subrecord",
            name="Version",
        ),
        "navmesh_infos": _base.Binding(
            path="NAVI/2:Navmesh Infos",
            kind="repeat",
            name="Navmesh Infos",
            repeated_path="NAVI/2:Navmesh Infos/repeat/0:Navmesh Info",
            child_kind="subrecord",
        ),
        "precomputed_pathing": _base.Binding(
            path="NAVI/3:Precomputed Pathing",
            kind="subrecord",
            name="Precomputed Pathing",
        ),
        "deleted_navmeshes": _base.Binding(
            path="NAVI/4:Deleted Navmeshes",
            kind="subrecord",
            name="Deleted Navmeshes",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    version: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    navmesh_infos: tuple[Structure5026, ...] = ()
    """Value decoded from this schema node."""

    precomputed_pathing: Optional[Structure5069] = None
    """Value decoded from this schema node."""

    deleted_navmeshes: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["version"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["navmesh_infos"]
    ) -> _base.FieldRef[tuple[Structure5026, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["precomputed_pathing"]
    ) -> _base.FieldRef[Optional[Structure5069]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["deleted_navmeshes"]
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
