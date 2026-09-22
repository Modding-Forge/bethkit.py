"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class PlayerCommand7718(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    PLAYER = 0
    COMMAND = 1


class TopLevelBlockingExclusive7720(enum.IntFlag):
    """Named values from the pinned schema."""

    TOP_LEVEL = 1
    BLOCKING = 2
    EXCLUSIVE = 4


class DialogBranchRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "DLBR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "DLBR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="DLBR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "quest": _base.Binding(
            path="DLBR/1:Quest",
            kind="subrecord",
            name="Quest",
        ),
        "category": _base.Binding(
            path="DLBR/2:Category",
            kind="subrecord",
            name="Category",
        ),
        "flags": _base.Binding(
            path="DLBR/3:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "starting_topic": _base.Binding(
            path="DLBR/4:Starting Topic",
            kind="subrecord",
            name="Starting Topic",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    category: Optional[PlayerCommand7718] = None
    """Value decoded from this schema node."""

    flags: Optional[TopLevelBlockingExclusive7720] = None
    """Value decoded from this schema node."""

    starting_topic: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
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
        self, name: Literal["category"]
    ) -> _base.FieldRef[Optional[PlayerCommand7718]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[TopLevelBlockingExclusive7720]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["starting_topic"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
