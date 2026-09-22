"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base


class FamilyAssociation8654(enum.IntFlag):
    """Named values from the pinned schema."""

    FAMILY_ASSOCIATION = 1


class AssociationTypeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ASTP"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "ASTP"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="ASTP/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "male_parent_title": _base.Binding(
            path="ASTP/1:Male Parent Title",
            kind="subrecord",
            name="Male Parent Title",
        ),
        "female_parent_title": _base.Binding(
            path="ASTP/2:Female Parent Title",
            kind="subrecord",
            name="Female Parent Title",
        ),
        "male_child_title": _base.Binding(
            path="ASTP/3:Male Child Title",
            kind="subrecord",
            name="Male Child Title",
        ),
        "female_child_title": _base.Binding(
            path="ASTP/4:Female Child Title",
            kind="subrecord",
            name="Female Child Title",
        ),
        "flags": _base.Binding(
            path="ASTP/5:Flags",
            kind="subrecord",
            name="Flags",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    male_parent_title: Optional[str] = None
    """Value decoded from this schema node."""

    female_parent_title: Optional[str] = None
    """Value decoded from this schema node."""

    male_child_title: Optional[str] = None
    """Value decoded from this schema node."""

    female_child_title: Optional[str] = None
    """Value decoded from this schema node."""

    flags: Optional[FamilyAssociation8654] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_parent_title"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_parent_title"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["male_child_title"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["female_child_title"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[FamilyAssociation8654]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
