"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class Flags2914(enum.IntFlag):
    """Named values from the pinned schema."""

    ROTATE_TO_FACE_TARGET = 1
    ATTACH_TO_CAMERA = 2
    INHERIT_ROTATION = 4


class Structure2911(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RFCT/1:Effect Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "effect_art": _base.Binding(
            path="RFCT/1:Effect Data/payload/0:Effect Art",
            kind="primitive",
            name="Effect Art",
        ),
        "shader": _base.Binding(
            path="RFCT/1:Effect Data/payload/1:Shader",
            kind="primitive",
            name="Shader",
        ),
        "flags": _base.Binding(
            path="RFCT/1:Effect Data/payload/2:Flags",
            kind="primitive",
            name="Flags",
        ),
    }

    effect_art: _values.FormId
    """Value decoded from this schema node."""

    shader: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags2914
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["effect_art"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["shader"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags2914]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class VisualEffectRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "RFCT"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "RFCT"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="RFCT/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "effect_data": _base.Binding(
            path="RFCT/1:Effect Data",
            kind="subrecord",
            name="Effect Data",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    effect_data: Optional[Structure2911] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effect_data"]
    ) -> _base.FieldRef[Optional[Structure2911]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
