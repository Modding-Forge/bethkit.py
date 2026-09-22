"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class PlayableNotMaleNotFemaleUnknown4Unknow8C749Be83717(enum.IntFlag):
    """Named values from the pinned schema."""

    PLAYABLE = 1
    NOT_MALE = 2
    NOT_FEMALE = 4
    UNKNOWN_4 = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    UNKNOWN_8 = 128


class EyesRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EYES"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "EYES"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="EYES/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="EYES/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "texture": _base.Binding(
            path="EYES/2:Texture",
            kind="subrecord",
            name="Texture",
        ),
        "flags": _base.Binding(
            path="EYES/3:Flags",
            kind="subrecord",
            name="Flags",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    texture: Optional[str] = None
    """Value decoded from this schema node."""

    flags: Optional[PlayableNotMaleNotFemaleUnknown4Unknow8C749Be83717] = None
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
    def field(self, name: Literal["texture"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[PlayableNotMaleNotFemaleUnknown4Unknow8C749Be83717]
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
