"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure6329(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "AVIF/5:Skill/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "skill_use_mult": _base.Binding(
            path="AVIF/5:Skill/payload/0:Skill Use Mult",
            kind="primitive",
            name="Skill Use Mult",
        ),
        "skill_offset_mult": _base.Binding(
            path="AVIF/5:Skill/payload/1:Skill Offset Mult",
            kind="primitive",
            name="Skill Offset Mult",
        ),
        "skill_improve_mult": _base.Binding(
            path="AVIF/5:Skill/payload/2:Skill Improve Mult",
            kind="primitive",
            name="Skill Improve Mult",
        ),
        "skill_improve_offset": _base.Binding(
            path="AVIF/5:Skill/payload/3:Skill Improve Offset",
            kind="primitive",
            name="Skill Improve Offset",
        ),
    }

    skill_use_mult: float
    """Value decoded from this schema node."""

    skill_offset_mult: float
    """Value decoded from this schema node."""

    skill_improve_mult: float
    """Value decoded from this schema node."""

    skill_improve_offset: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["skill_use_mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skill_offset_mult"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skill_improve_mult"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skill_improve_offset"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Node6335(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "AVIF/6:Perk Tree/repeat/0:Node"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "perk": _base.Binding(
            path="AVIF/6:Perk Tree/repeat/0:Node/0:Perk",
            kind="subrecord",
            name="Perk",
        ),
        "unknown": _base.Binding(
            path="AVIF/6:Perk Tree/repeat/0:Node/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "perk_grid_x": _base.Binding(
            path="AVIF/6:Perk Tree/repeat/0:Node/2:Perk-Grid X",
            kind="subrecord",
            name="Perk-Grid X",
        ),
        "perk_grid_y": _base.Binding(
            path="AVIF/6:Perk Tree/repeat/0:Node/3:Perk-Grid Y",
            kind="subrecord",
            name="Perk-Grid Y",
        ),
        "horizontal_position": _base.Binding(
            path=("AVIF/6:Perk Tree/repeat/0:Node/4:Horizontal Position"),
            kind="subrecord",
            name="Horizontal Position",
        ),
        "vertical_position": _base.Binding(
            path=("AVIF/6:Perk Tree/repeat/0:Node/5:Vertical Position"),
            kind="subrecord",
            name="Vertical Position",
        ),
        "associated_skill": _base.Binding(
            path="AVIF/6:Perk Tree/repeat/0:Node/6:Associated Skill",
            kind="subrecord",
            name="Associated Skill",
        ),
        "connections": _base.Binding(
            path="AVIF/6:Perk Tree/repeat/0:Node/7:Connections",
            kind="repeat",
            name="Connections",
            repeated_path=(
                "AVIF/6:Perk Tree/repeat/0:Node/7:Connections/repeat/0:"
                "Line to Index"
            ),
            child_kind="subrecord",
        ),
        "index": _base.Binding(
            path="AVIF/6:Perk Tree/repeat/0:Node/8:Index",
            kind="subrecord",
            name="Index",
        ),
    }

    perk: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    perk_grid_x: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    perk_grid_y: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    horizontal_position: Optional[float] = None
    """Value decoded from this schema node."""

    vertical_position: Optional[float] = None
    """Value decoded from this schema node."""

    associated_skill: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    connections: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ] = ()
    """Value decoded from this schema node."""

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["perk"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perk_grid_x"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perk_grid_y"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["horizontal_position"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vertical_position"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["associated_skill"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["connections"]
    ) -> _base.FieldRef[
        tuple[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            ...,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
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


class ActorValueInformationRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "AVIF"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "AVIF"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="AVIF/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="AVIF/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "description": _base.Binding(
            path="AVIF/2:Description",
            kind="subrecord",
            name="Description",
        ),
        "abbreviation": _base.Binding(
            path="AVIF/3:Abbreviation",
            kind="subrecord",
            name="Abbreviation",
        ),
        "unknown": _base.Binding(
            path="AVIF/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "skill": _base.Binding(
            path="AVIF/5:Skill",
            kind="subrecord",
            name="Skill",
        ),
        "perk_tree": _base.Binding(
            path="AVIF/6:Perk Tree",
            kind="repeat",
            name="Perk Tree",
            repeated_path="AVIF/6:Perk Tree/repeat/0:Node",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    abbreviation: Optional[str] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    skill: Optional[Structure6329] = None
    """Value decoded from this schema node."""

    perk_tree: tuple[Node6335, ...] = ()
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
        self, name: Literal["abbreviation"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skill"]
    ) -> _base.FieldRef[Optional[Structure6329]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perk_tree"]
    ) -> _base.FieldRef[tuple[Node6335, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
