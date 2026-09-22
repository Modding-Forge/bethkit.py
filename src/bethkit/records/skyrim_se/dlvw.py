"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class Value7920(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    DIALOGUE_BRANCHES = 0
    DIALOGUE_TOPICS = 7


class Value7922(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class DialogViewRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "DLVW"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "DLVW"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="DLVW/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "quest": _base.Binding(
            path="DLVW/1:Quest",
            kind="subrecord",
            name="Quest",
        ),
        "branches": _base.Binding(
            path="DLVW/2:Branches",
            kind="repeat",
            name="Branches",
            repeated_path="DLVW/2:Branches/repeat/0:Branch",
            child_kind="subrecord",
        ),
        "topics": _base.Binding(
            path="DLVW/3:Topics",
            kind="repeat",
            name="Topics",
            repeated_path="DLVW/3:Topics/repeat/0:Topic",
            child_kind="subrecord",
        ),
        "view_category": _base.Binding(
            path="DLVW/4:View Category",
            kind="subrecord",
            name="View Category",
        ),
        "show_all_text": _base.Binding(
            path="DLVW/5:Show All Text",
            kind="subrecord",
            name="Show All Text",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    branches: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    topics: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    view_category: Optional[Value7920] = None
    """Value decoded from this schema node."""

    show_all_text: Optional[Value7922] = None
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
        self, name: Literal["branches"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topics"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["view_category"]
    ) -> _base.FieldRef[Optional[Value7920]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["show_all_text"]
    ) -> _base.FieldRef[Optional[Value7922]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
