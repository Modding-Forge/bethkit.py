"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class Structure7941(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SHOU/4:Words of Power/repeat/0:SNAM/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "word": _base.Binding(
            path=("SHOU/4:Words of Power/repeat/0:SNAM/payload/0:Word"),
            kind="primitive",
            name="Word",
        ),
        "spell": _base.Binding(
            path=("SHOU/4:Words of Power/repeat/0:SNAM/payload/1:Spell"),
            kind="primitive",
            name="Spell",
        ),
        "recovery_time": _base.Binding(
            path=(
                "SHOU/4:Words of Power/repeat/0:SNAM/payload/2:Recovery Time"
            ),
            kind="primitive",
            name="Recovery Time",
        ),
    }

    word: _values.FormId
    """Value decoded from this schema node."""

    spell: _values.FormId
    """Value decoded from this schema node."""

    recovery_time: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["word"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["spell"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["recovery_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ShoutRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SHOU"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SHOU"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SHOU/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="SHOU/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "menu_display_object": _base.Binding(
            path="SHOU/2:Menu Display Object",
            kind="subrecord",
            name="Menu Display Object",
        ),
        "description": _base.Binding(
            path="SHOU/3:Description",
            kind="subrecord",
            name="Description",
        ),
        "words_of_power": _base.Binding(
            path="SHOU/4:Words of Power",
            kind="repeat",
            name="Words of Power",
            repeated_path="SHOU/4:Words of Power/repeat/0:SNAM",
            child_kind="subrecord",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    menu_display_object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    words_of_power: tuple[Structure7941, ...] = ()
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
        self, name: Literal["menu_display_object"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["words_of_power"]
    ) -> _base.FieldRef[tuple[Structure7941, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
