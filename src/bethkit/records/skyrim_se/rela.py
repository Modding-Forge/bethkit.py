"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class Rank7960(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOVER = 0
    ALLY = 1
    CONFIDANT = 2
    FRIEND = 3
    ACQUAINTANCE = 4
    RIVAL = 5
    FOE = 6
    ENEMY = 7
    ARCHNEMESIS = 8


class Flags7962(enum.IntFlag):
    """Named values from the pinned schema."""

    UNKNOWN_1 = 1
    UNKNOWN_2 = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    SECRET = 128


class Structure7957(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RELA/1:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "parent": _base.Binding(
            path="RELA/1:Data/payload/0:Parent",
            kind="primitive",
            name="Parent",
        ),
        "child": _base.Binding(
            path="RELA/1:Data/payload/1:Child",
            kind="primitive",
            name="Child",
        ),
        "rank": _base.Binding(
            path="RELA/1:Data/payload/2:Rank",
            kind="primitive",
            name="Rank",
        ),
        "unknown": _base.Binding(
            path="RELA/1:Data/payload/3:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "flags": _base.Binding(
            path="RELA/1:Data/payload/4:Flags",
            kind="primitive",
            name="Flags",
        ),
        "association_type": _base.Binding(
            path="RELA/1:Data/payload/5:Association Type",
            kind="primitive",
            name="Association Type",
        ),
    }

    parent: _values.FormId
    """Value decoded from this schema node."""

    child: _values.FormId
    """Value decoded from this schema node."""

    rank: Rank7960
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    flags: Flags7962
    """Value decoded from this schema node."""

    association_type: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["parent"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["child"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rank"]) -> _base.FieldRef[Rank7960]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags7962]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["association_type"]
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


class RelationshipRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RELA"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "RELA"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="RELA/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "data": _base.Binding(
            path="RELA/1:Data",
            kind="subrecord",
            name="Data",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    data: Optional[Structure7957] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure7957]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
