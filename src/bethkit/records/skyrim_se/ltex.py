"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure10648(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LTEX/3:Havok Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "friction": _base.Binding(
            path="LTEX/3:Havok Data/payload/0:Friction",
            kind="primitive",
            name="Friction",
        ),
        "restitution": _base.Binding(
            path="LTEX/3:Havok Data/payload/1:Restitution",
            kind="primitive",
            name="Restitution",
        ),
    }

    friction: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    restitution: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["friction"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["restitution"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
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


class IsSnow10657(enum.IntFlag):
    """Named values from the pinned schema."""

    IS_SNOW = 1


class LandscapeTextureRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LTEX"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LTEX"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LTEX/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "texture_set": _base.Binding(
            path="LTEX/1:Texture Set",
            kind="subrecord",
            name="Texture Set",
        ),
        "material_type": _base.Binding(
            path="LTEX/2:Material Type",
            kind="subrecord",
            name="Material Type",
        ),
        "havok_data": _base.Binding(
            path="LTEX/3:Havok Data",
            kind="subrecord",
            name="Havok Data",
        ),
        "texture_specular_exponent": _base.Binding(
            path="LTEX/4:Texture Specular Exponent",
            kind="subrecord",
            name="Texture Specular Exponent",
        ),
        "grasses": _base.Binding(
            path="LTEX/5:Grasses",
            kind="repeat",
            name="Grasses",
            repeated_path="LTEX/5:Grasses/repeat/0:Grass",
            child_kind="subrecord",
        ),
        "flags": _base.Binding(
            path="LTEX/6:Flags",
            kind="subrecord",
            name="Flags",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    texture_set: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    material_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    havok_data: Optional[Structure10648] = None
    """Value decoded from this schema node."""

    texture_specular_exponent: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ] = None
    """Value decoded from this schema node."""

    grasses: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    flags: Optional[IsSnow10657] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["texture_set"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["material_type"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["havok_data"]
    ) -> _base.FieldRef[Optional[Structure10648]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["texture_specular_exponent"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grasses"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[IsSnow10657]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
