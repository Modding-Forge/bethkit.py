"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Icon2803(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CLAS/3:Icon"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "large_icon_file_name": _base.Binding(
            path="CLAS/3:Icon/0:Large Icon FileName",
            kind="subrecord",
            name="Large Icon FileName",
        ),
        "small_icon_file_name": _base.Binding(
            path="CLAS/3:Icon/1:Small Icon FileName",
            kind="subrecord",
            name="Small Icon FileName",
        ),
    }

    large_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    small_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["large_icon_file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["small_icon_file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Teaches2811(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ONE_HANDED = 0
    TWO_HANDED = 1
    ARCHERY = 2
    BLOCK = 3
    SMITHING = 4
    HEAVY_ARMOR = 5
    LIGHT_ARMOR = 6
    PICKPOCKET = 7
    LOCKPICKING = 8
    SNEAK = 9
    ALCHEMY = 10
    SPEECH = 11
    ALTERATION = 12
    CONJURATION = 13
    DESTRUCTION = 14
    ILLUSION = 15
    RESTORATION = 16
    ENCHANTING = 17


class Structure2809(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CLAS/4:DATA/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="CLAS/4:DATA/payload/0:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "teaches": _base.Binding(
            path="CLAS/4:DATA/payload/1:Teaches",
            kind="primitive",
            name="Teaches",
        ),
        "maximum_training_level": _base.Binding(
            path="CLAS/4:DATA/payload/2:Maximum training level",
            kind="primitive",
            name="Maximum training level",
        ),
        "skill_weights": _base.Binding(
            path="CLAS/4:DATA/payload/3:Skill Weights",
            kind="array",
            name="Skill Weights",
        ),
        "bleedout_default": _base.Binding(
            path="CLAS/4:DATA/payload/4:Bleedout Default",
            kind="primitive",
            name="Bleedout Default",
        ),
        "voice_points": _base.Binding(
            path="CLAS/4:DATA/payload/5:Voice Points",
            kind="primitive",
            name="Voice Points",
        ),
        "attribute_weights": _base.Binding(
            path="CLAS/4:DATA/payload/6:Attribute Weights",
            kind="array",
            name="Attribute Weights",
        ),
    }

    unknown: bytes
    """Value decoded from this schema node."""

    teaches: Teaches2811
    """Value decoded from this schema node."""

    maximum_training_level: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    skill_weights: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...
    ]
    """Value decoded from this schema node."""

    bleedout_default: float
    """Value decoded from this schema node."""

    voice_points: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    attribute_weights: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["teaches"]) -> _base.FieldRef[Teaches2811]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["maximum_training_level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skill_weights"]
    ) -> _base.FieldRef[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["bleedout_default"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["voice_points"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attribute_weights"]
    ) -> _base.FieldRef[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
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


class ClassValueRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CLAS"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "CLAS"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="CLAS/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="CLAS/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "description": _base.Binding(
            path="CLAS/2:Description",
            kind="subrecord",
            name="Description",
        ),
        "icon": _base.Binding(
            path="CLAS/3:Icon",
            kind="unordered",
            name="Icon",
        ),
        "data": _base.Binding(
            path="CLAS/4:DATA",
            kind="subrecord",
            name="DATA",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    icon: Optional[Icon2803] = None
    """Value decoded from this schema node."""

    data: Optional[Structure2809] = None
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
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["icon"]
    ) -> _base.FieldRef[Optional[Icon2803]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure2809]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
