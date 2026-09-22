"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure10780(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LVSP/1:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="LVSP/1:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="LVSP/1:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="LVSP/1:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="LVSP/1:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="LVSP/1:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="LVSP/1:Object Bounds/payload/5:Z2",
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


class CalculateFromAllLevelsPlayerSLevelCalc7295F0A910790(enum.IntFlag):
    """Named values from the pinned schema."""

    CALCULATE_FROM_ALL_LEVELS_PLAYER_S_LEVEL = 1
    CALCULATE_FOR_EACH_ITEM_IN_COUNT = 2
    USE_ALL_SPELLS = 4


class Structure10796(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entr"
        "y/0:Base Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "level": _base.Binding(
            path=(
                "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/0:Level"
            ),
            kind="primitive",
            name="Level",
        ),
        "unknown": _base.Binding(
            path=(
                "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "reference": _base.Binding(
            path=(
                "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/2:Reference"
            ),
            kind="primitive",
            name="Reference",
        ),
        "count": _base.Binding(
            path=(
                "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data/payload/3:Count"
            ),
            kind="primitive",
            name="Count",
        ),
        "unknown_10801": _base.Binding(
            path=(
                "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entr"
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

    unknown_10801: bytes
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
    def field(self, name: Literal["unknown_10801"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LeveledListEntry10794(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entry"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "base_data": _base.Binding(
            path=(
                "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entr"
                "y/0:Base Data"
            ),
            kind="subrecord",
            name="Base Data",
        ),
    }

    base_data: Optional[Structure10796] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["base_data"]
    ) -> _base.FieldRef[Optional[Structure10796]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LeveledSpellRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LVSP"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LVSP"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LVSP/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "object_bounds": _base.Binding(
            path="LVSP/1:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "chance_none": _base.Binding(
            path="LVSP/2:Chance None",
            kind="subrecord",
            name="Chance None",
        ),
        "flags": _base.Binding(
            path="LVSP/3:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "count": _base.Binding(
            path="LVSP/4:Count",
            kind="subrecord",
            name="Count",
        ),
        "leveled_list_entries": _base.Binding(
            path="LVSP/5:Leveled List Entries",
            kind="repeat",
            name="Leveled List Entries",
            repeated_path=(
                "LVSP/5:Leveled List Entries/repeat/0:Leveled List Entry"
            ),
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure10780] = None
    """Value decoded from this schema node."""

    chance_none: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ] = None
    """Value decoded from this schema node."""

    flags: Optional[CalculateFromAllLevelsPlayerSLevelCalc7295F0A910790] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ] = None
    """Value decoded from this schema node."""

    leveled_list_entries: tuple[LeveledListEntry10794, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure10780]]:
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
        Optional[CalculateFromAllLevelsPlayerSLevelCalc7295F0A910790]
    ]:
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
    ) -> _base.FieldRef[tuple[LeveledListEntry10794, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
