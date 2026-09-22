"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure10744(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LVLI/1:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="LVLI/1:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="LVLI/1:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="LVLI/1:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="LVLI/1:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="LVLI/1:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="LVLI/1:Object Bounds/payload/5:Z2",
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


class CalculateFromAllLevelsPlayerSLevelCalc5E026Df010754(enum.IntFlag):
    """Named values from the pinned schema."""

    CALCULATE_FROM_ALL_LEVELS_PLAYER_S_LEVEL = 1
    CALCULATE_FOR_EACH_ITEM_IN_COUNT = 2
    USE_ALL = 4
    SPECIAL_LOOT = 8


class Structure10762(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
        "y/0:Base Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "level": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/0:Level"
            ),
            kind="primitive",
            name="Level",
        ),
        "unknown": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "reference": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/2:Reference"
            ),
            kind="primitive",
            name="Reference",
        ),
        "count": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/3:Count"
            ),
            kind="primitive",
            name="Count",
        ),
        "unknown_10767": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    level: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    reference: _values.FormId
    """Value decoded from this schema node."""

    count: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unknown_10767: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_10767"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10772: _base.Variant = _base.Variant(
    path=(
        "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
        "y/1:Extra Data/payload/1:Global Variable / Required Ra"
        "nk/variants/0:Unused"
    )
)


_VARIANT_10773: _base.Variant = _base.Variant(
    path=(
        "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
        "y/1:Extra Data/payload/1:Global Variable / Required Ra"
        "nk/variants/1:Global Variable"
    )
)


_VARIANT_10774: _base.Variant = _base.Variant(
    path=(
        "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
        "y/1:Extra Data/payload/1:Global Variable / Required Ra"
        "nk/variants/2:Required Rank"
    )
)


class Structure10769(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
        "y/1:Extra Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/1:Extra Data/payload/0:Owner"
            ),
            kind="primitive",
            name="Owner",
        ),
        "global_variable_required_rank": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/1:Extra Data/payload/1:Global Variable / Required Ra"
                "nk"
            ),
            kind="union",
            name="Global Variable / Required Rank",
        ),
        "item_condition": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/1:Extra Data/payload/2:Item Condition"
            ),
            kind="primitive",
            name="Item Condition",
        ),
    }

    owner: _values.FormId
    """Value decoded from this schema node."""

    global_variable_required_rank: (
        Annotated[bytes, _VARIANT_10772]
        | Annotated[_values.FormId, _VARIANT_10773]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10774,
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
        Annotated[bytes, _VARIANT_10772]
        | Annotated[_values.FormId, _VARIANT_10773]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10774,
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


class LeveledListEntry10760(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entry"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "base_data": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data"
            ),
            kind="subrecord",
            name="Base Data",
        ),
        "extra_data": _base.Binding(
            path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/1:Extra Data"
            ),
            kind="subrecord",
            name="Extra Data",
        ),
    }

    base_data: Optional[Structure10762] = None
    """Value decoded from this schema node."""

    extra_data: Optional[Structure10769] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["base_data"]
    ) -> _base.FieldRef[Optional[Structure10762]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["extra_data"]
    ) -> _base.FieldRef[Optional[Structure10769]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LeveledItemRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LVLI"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LVLI"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LVLI/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "object_bounds": _base.Binding(
            path="LVLI/1:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "chance_none": _base.Binding(
            path="LVLI/2:Chance None",
            kind="subrecord",
            name="Chance None",
        ),
        "flags": _base.Binding(
            path="LVLI/3:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "global_value": _base.Binding(
            path="LVLI/4:Global",
            kind="subrecord",
            name="Global",
        ),
        "count": _base.Binding(
            path="LVLI/5:Count",
            kind="subrecord",
            name="Count",
        ),
        "leveled_list_entries": _base.Binding(
            path="LVLI/6:Leveled List Entries",
            kind="repeat",
            name="Leveled List Entries",
            repeated_path=(
                "LVLI/6:Leveled List Entries/repeat/0:Leveled List Entry"
            ),
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure10744] = None
    """Value decoded from this schema node."""

    chance_none: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ] = None
    """Value decoded from this schema node."""

    flags: Optional[CalculateFromAllLevelsPlayerSLevelCalc5E026Df010754] = None
    """Value decoded from this schema node."""

    global_value: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ] = None
    """Value decoded from this schema node."""

    leveled_list_entries: tuple[LeveledListEntry10760, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure10744]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["chance_none"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[CalculateFromAllLevelsPlayerSLevelCalc5E026Df010754]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["global_value"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["leveled_list_entries"]
    ) -> _base.FieldRef[tuple[LeveledListEntry10760, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
