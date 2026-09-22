"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class MuteWhenSubmergedShouldAppearOnMenu9027(enum.IntFlag):
    """Named values from the pinned schema."""

    MUTE_WHEN_SUBMERGED = 1
    SHOULD_APPEAR_ON_MENU = 2


class SoundCategoryRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SNCT"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SNCT"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SNCT/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="SNCT/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "flags": _base.Binding(
            path="SNCT/2:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "parent": _base.Binding(
            path="SNCT/3:Parent",
            kind="subrecord",
            name="Parent",
        ),
        "static_volume_multiplier": _base.Binding(
            path="SNCT/4:Static Volume Multiplier",
            kind="subrecord",
            name="Static Volume Multiplier",
        ),
        "default_menu_value": _base.Binding(
            path="SNCT/5:Default Menu Value",
            kind="subrecord",
            name="Default Menu Value",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    flags: Optional[MuteWhenSubmergedShouldAppearOnMenu9027] = None
    """Value decoded from this schema node."""

    parent: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    static_volume_multiplier: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    default_menu_value: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
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
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[MuteWhenSubmergedShouldAppearOnMenu9027]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parent"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["static_volume_multiplier"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_menu_value"]
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
