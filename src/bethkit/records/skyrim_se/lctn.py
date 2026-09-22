"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Reference6728(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/1:Added Persist Location References/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ref": _base.Binding(
            path=(
                "LCTN/1:Added Persist Location References/payload/element/0:Ref"
            ),
            kind="primitive",
            name="Ref",
        ),
        "world_cell": _base.Binding(
            path=(
                "LCTN/1:Added Persist Location References/payload/eleme"
                "nt/1:World/Cell"
            ),
            kind="primitive",
            name="World/Cell",
        ),
        "grid_y": _base.Binding(
            path=(
                "LCTN/1:Added Persist Location References/payload/eleme"
                "nt/2:Grid Y"
            ),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=(
                "LCTN/1:Added Persist Location References/payload/eleme"
                "nt/3:Grid X"
            ),
            kind="primitive",
            name="Grid X",
        ),
    }

    ref: _values.FormId
    """Value decoded from this schema node."""

    world_cell: _values.FormId
    """Value decoded from this schema node."""

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["ref"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["world_cell"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Reference6735(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/2:Master Persist Location References/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ref": _base.Binding(
            path=(
                "LCTN/2:Master Persist Location References/payload/elem"
                "ent/0:Ref"
            ),
            kind="primitive",
            name="Ref",
        ),
        "world_cell": _base.Binding(
            path=(
                "LCTN/2:Master Persist Location References/payload/elem"
                "ent/1:World/Cell"
            ),
            kind="primitive",
            name="World/Cell",
        ),
        "grid_y": _base.Binding(
            path=(
                "LCTN/2:Master Persist Location References/payload/elem"
                "ent/2:Grid Y"
            ),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=(
                "LCTN/2:Master Persist Location References/payload/elem"
                "ent/3:Grid X"
            ),
            kind="primitive",
            name="Grid X",
        ),
    }

    ref: _values.FormId
    """Value decoded from this schema node."""

    world_cell: _values.FormId
    """Value decoded from this schema node."""

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["ref"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["world_cell"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Actor6745(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LCTN/4:Added Unique NPCs/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "npc": _base.Binding(
            path="LCTN/4:Added Unique NPCs/payload/element/0:NPC",
            kind="primitive",
            name="NPC",
        ),
        "actor_ref": _base.Binding(
            path=("LCTN/4:Added Unique NPCs/payload/element/1:Actor Ref"),
            kind="primitive",
            name="Actor Ref",
        ),
        "location": _base.Binding(
            path=("LCTN/4:Added Unique NPCs/payload/element/2:Location"),
            kind="primitive",
            name="Location",
        ),
    }

    npc: _values.FormId
    """Value decoded from this schema node."""

    actor_ref: _values.FormId
    """Value decoded from this schema node."""

    location: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["npc"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actor_ref"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Actor6751(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LCTN/5:Master Unique NPCs/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "npc": _base.Binding(
            path="LCTN/5:Master Unique NPCs/payload/element/0:NPC",
            kind="primitive",
            name="NPC",
        ),
        "actor_ref": _base.Binding(
            path=("LCTN/5:Master Unique NPCs/payload/element/1:Actor Ref"),
            kind="primitive",
            name="Actor Ref",
        ),
        "location": _base.Binding(
            path=("LCTN/5:Master Unique NPCs/payload/element/2:Location"),
            kind="primitive",
            name="Location",
        ),
    }

    npc: _values.FormId
    """Value decoded from this schema node."""

    actor_ref: _values.FormId
    """Value decoded from this schema node."""

    location: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["npc"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actor_ref"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Reference6760(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/7:Added Special References/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "loc_ref_type": _base.Binding(
            path=(
                "LCTN/7:Added Special References/payload/element/0:Loc Ref Type"
            ),
            kind="primitive",
            name="Loc Ref Type",
        ),
        "ref": _base.Binding(
            path=("LCTN/7:Added Special References/payload/element/1:Ref"),
            kind="primitive",
            name="Ref",
        ),
        "world_cell": _base.Binding(
            path=(
                "LCTN/7:Added Special References/payload/element/2:World/Cell"
            ),
            kind="primitive",
            name="World/Cell",
        ),
        "grid_y": _base.Binding(
            path=("LCTN/7:Added Special References/payload/element/3:Grid Y"),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=("LCTN/7:Added Special References/payload/element/4:Grid X"),
            kind="primitive",
            name="Grid X",
        ),
    }

    loc_ref_type: _values.FormId
    """Value decoded from this schema node."""

    ref: _values.FormId
    """Value decoded from this schema node."""

    world_cell: _values.FormId
    """Value decoded from this schema node."""

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["loc_ref_type"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ref"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["world_cell"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Reference6768(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/8:Master Special References/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "loc_ref_type": _base.Binding(
            path=(
                "LCTN/8:Master Special References/payload/element/0:Loc"
                " Ref Type"
            ),
            kind="primitive",
            name="Loc Ref Type",
        ),
        "ref": _base.Binding(
            path=("LCTN/8:Master Special References/payload/element/1:Ref"),
            kind="primitive",
            name="Ref",
        ),
        "world_cell": _base.Binding(
            path=(
                "LCTN/8:Master Special References/payload/element/2:World/Cell"
            ),
            kind="primitive",
            name="World/Cell",
        ),
        "grid_y": _base.Binding(
            path=("LCTN/8:Master Special References/payload/element/3:Grid Y"),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=("LCTN/8:Master Special References/payload/element/4:Grid X"),
            kind="primitive",
            name="Grid X",
        ),
    }

    loc_ref_type: _values.FormId
    """Value decoded from this schema node."""

    ref: _values.FormId
    """Value decoded from this schema node."""

    world_cell: _values.FormId
    """Value decoded from this schema node."""

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["loc_ref_type"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["ref"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["world_cell"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Coords6782(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/10:Added Worldsapce Cells/repeat/0:Worldspace/pay"
        "load/1:Cells/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "grid_y": _base.Binding(
            path=(
                "LCTN/10:Added Worldsapce Cells/repeat/0:Worldspace/pay"
                "load/1:Cells/element/0:Grid Y"
            ),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=(
                "LCTN/10:Added Worldsapce Cells/repeat/0:Worldspace/pay"
                "load/1:Cells/element/1:Grid X"
            ),
            kind="primitive",
            name="Grid X",
        ),
    }

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Structure6779(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/10:Added Worldsapce Cells/repeat/0:Worldspace/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "world": _base.Binding(
            path=(
                "LCTN/10:Added Worldsapce Cells/repeat/0:Worldspace/pay"
                "load/0:World"
            ),
            kind="primitive",
            name="World",
        ),
        "cells": _base.Binding(
            path=(
                "LCTN/10:Added Worldsapce Cells/repeat/0:Worldspace/pay"
                "load/1:Cells"
            ),
            kind="array",
            name="Cells",
        ),
    }

    world: _values.FormId
    """Value decoded from this schema node."""

    cells: tuple[Coords6782, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["world"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cells"]
    ) -> _base.FieldRef[tuple[Coords6782, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Coords6790(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/11:Master Worldspace Cells/repeat/0:Worldspace/pa"
        "yload/1:Cells/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "grid_y": _base.Binding(
            path=(
                "LCTN/11:Master Worldspace Cells/repeat/0:Worldspace/pa"
                "yload/1:Cells/element/0:Grid Y"
            ),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=(
                "LCTN/11:Master Worldspace Cells/repeat/0:Worldspace/pa"
                "yload/1:Cells/element/1:Grid X"
            ),
            kind="primitive",
            name="Grid X",
        ),
    }

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Structure6787(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/11:Master Worldspace Cells/repeat/0:Worldspace/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "world": _base.Binding(
            path=(
                "LCTN/11:Master Worldspace Cells/repeat/0:Worldspace/pa"
                "yload/0:World"
            ),
            kind="primitive",
            name="World",
        ),
        "cells": _base.Binding(
            path=(
                "LCTN/11:Master Worldspace Cells/repeat/0:Worldspace/pa"
                "yload/1:Cells"
            ),
            kind="array",
            name="Cells",
        ),
    }

    world: _values.FormId
    """Value decoded from this schema node."""

    cells: tuple[Coords6790, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["world"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cells"]
    ) -> _base.FieldRef[tuple[Coords6790, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Coords6798(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/12:Removed Worldspace Cells/repeat/0:Worldspace/p"
        "ayload/1:Cells/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "grid_y": _base.Binding(
            path=(
                "LCTN/12:Removed Worldspace Cells/repeat/0:Worldspace/p"
                "ayload/1:Cells/element/0:Grid Y"
            ),
            kind="primitive",
            name="Grid Y",
        ),
        "grid_x": _base.Binding(
            path=(
                "LCTN/12:Removed Worldspace Cells/repeat/0:Worldspace/p"
                "ayload/1:Cells/element/1:Grid X"
            ),
            kind="primitive",
            name="Grid X",
        ),
    }

    grid_y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    grid_x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["grid_y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["grid_x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Structure6795(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/12:Removed Worldspace Cells/repeat/0:Worldspace/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "world": _base.Binding(
            path=(
                "LCTN/12:Removed Worldspace Cells/repeat/0:Worldspace/p"
                "ayload/0:World"
            ),
            kind="primitive",
            name="World",
        ),
        "cells": _base.Binding(
            path=(
                "LCTN/12:Removed Worldspace Cells/repeat/0:Worldspace/p"
                "ayload/1:Cells"
            ),
            kind="array",
            name="Cells",
        ),
    }

    world: _values.FormId
    """Value decoded from this schema node."""

    cells: tuple[Coords6798, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["world"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cells"]
    ) -> _base.FieldRef[tuple[Coords6798, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags6812(enum.IntFlag):
    """Named values from the pinned schema."""

    SET_ENABLE_STATE_TO_OPPOSITE_OF_PARENT = 1
    POP_IN = 2


class Reference6809(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/15:Added Enable Point References/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ref": _base.Binding(
            path=(
                "LCTN/15:Added Enable Point References/payload/element/0:Ref"
            ),
            kind="primitive",
            name="Ref",
        ),
        "enable_parent": _base.Binding(
            path=(
                "LCTN/15:Added Enable Point References/payload/element/"
                "1:Enable Parent"
            ),
            kind="primitive",
            name="Enable Parent",
        ),
        "flags": _base.Binding(
            path=(
                "LCTN/15:Added Enable Point References/payload/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "unused": _base.Binding(
            path=(
                "LCTN/15:Added Enable Point References/payload/element/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    ref: _values.FormId
    """Value decoded from this schema node."""

    enable_parent: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags6812
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["ref"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enable_parent"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags6812]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags6819(enum.IntFlag):
    """Named values from the pinned schema."""

    SET_ENABLE_STATE_TO_OPPOSITE_OF_PARENT = 1
    POP_IN = 2


class Reference6816(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LCTN/16:Master Enable Parent References/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ref": _base.Binding(
            path=(
                "LCTN/16:Master Enable Parent References/payload/element/0:Ref"
            ),
            kind="primitive",
            name="Ref",
        ),
        "enable_parent": _base.Binding(
            path=(
                "LCTN/16:Master Enable Parent References/payload/elemen"
                "t/1:Enable Parent"
            ),
            kind="primitive",
            name="Enable Parent",
        ),
        "flags": _base.Binding(
            path=(
                "LCTN/16:Master Enable Parent References/payload/elemen"
                "t/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "unused": _base.Binding(
            path=(
                "LCTN/16:Master Enable Parent References/payload/elemen"
                "t/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    ref: _values.FormId
    """Value decoded from this schema node."""

    enable_parent: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags6819
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["ref"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enable_parent"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags6819]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure6841(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LCTN/26:Color/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="LCTN/26:Color/payload/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="LCTN/26:Color/payload/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="LCTN/26:Color/payload/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "alpha": _base.Binding(
            path="LCTN/26:Color/payload/3:Alpha",
            kind="primitive",
            name="Alpha",
        ),
    }

    red: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    green: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    blue: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    alpha: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["red"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["green"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["blue"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alpha"]
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


class LocationRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LCTN"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LCTN"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LCTN/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "added_persist_location_references": _base.Binding(
            path="LCTN/1:Added Persist Location References",
            kind="subrecord",
            name="Added Persist Location References",
        ),
        "master_persist_location_references": _base.Binding(
            path="LCTN/2:Master Persist Location References",
            kind="subrecord",
            name="Master Persist Location References",
        ),
        "removed_persist_location_references": _base.Binding(
            path="LCTN/3:Removed Persist Location References",
            kind="subrecord",
            name="Removed Persist Location References",
        ),
        "added_unique_npcs": _base.Binding(
            path="LCTN/4:Added Unique NPCs",
            kind="subrecord",
            name="Added Unique NPCs",
        ),
        "master_unique_npcs": _base.Binding(
            path="LCTN/5:Master Unique NPCs",
            kind="subrecord",
            name="Master Unique NPCs",
        ),
        "removed_unique_npcs": _base.Binding(
            path="LCTN/6:Removed Unique NPCs",
            kind="subrecord",
            name="Removed Unique NPCs",
        ),
        "added_special_references": _base.Binding(
            path="LCTN/7:Added Special References",
            kind="subrecord",
            name="Added Special References",
        ),
        "master_special_references": _base.Binding(
            path="LCTN/8:Master Special References",
            kind="subrecord",
            name="Master Special References",
        ),
        "removed_special_references": _base.Binding(
            path="LCTN/9:Removed Special References",
            kind="subrecord",
            name="Removed Special References",
        ),
        "added_worldsapce_cells": _base.Binding(
            path="LCTN/10:Added Worldsapce Cells",
            kind="repeat",
            name="Added Worldsapce Cells",
            repeated_path=(
                "LCTN/10:Added Worldsapce Cells/repeat/0:Worldspace"
            ),
            child_kind="subrecord",
        ),
        "master_worldspace_cells": _base.Binding(
            path="LCTN/11:Master Worldspace Cells",
            kind="repeat",
            name="Master Worldspace Cells",
            repeated_path=(
                "LCTN/11:Master Worldspace Cells/repeat/0:Worldspace"
            ),
            child_kind="subrecord",
        ),
        "removed_worldspace_cells": _base.Binding(
            path="LCTN/12:Removed Worldspace Cells",
            kind="repeat",
            name="Removed Worldspace Cells",
            repeated_path=(
                "LCTN/12:Removed Worldspace Cells/repeat/0:Worldspace"
            ),
            child_kind="subrecord",
        ),
        "added_initially_disabled_references": _base.Binding(
            path="LCTN/13:Added Initially Disabled References",
            kind="subrecord",
            name="Added Initially Disabled References",
        ),
        "master_initially_disabled_references": _base.Binding(
            path="LCTN/14:Master Initially Disabled References",
            kind="subrecord",
            name="Master Initially Disabled References",
        ),
        "added_enable_point_references": _base.Binding(
            path="LCTN/15:Added Enable Point References",
            kind="subrecord",
            name="Added Enable Point References",
        ),
        "master_enable_parent_references": _base.Binding(
            path="LCTN/16:Master Enable Parent References",
            kind="subrecord",
            name="Master Enable Parent References",
        ),
        "name": _base.Binding(
            path="LCTN/17:Name",
            kind="subrecord",
            name="Name",
        ),
        "keyword_count": _base.Binding(
            path="LCTN/18:Keyword Count",
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path="LCTN/19:Keywords",
            kind="subrecord",
            name="Keywords",
        ),
        "parent_location": _base.Binding(
            path="LCTN/20:Parent Location",
            kind="subrecord",
            name="Parent Location",
        ),
        "music": _base.Binding(
            path="LCTN/21:Music",
            kind="subrecord",
            name="Music",
        ),
        "unreported_crime_faction": _base.Binding(
            path="LCTN/22:Unreported Crime Faction",
            kind="subrecord",
            name="Unreported Crime Faction",
        ),
        "world_location_marker_ref": _base.Binding(
            path="LCTN/23:World Location Marker Ref",
            kind="subrecord",
            name="World Location Marker Ref",
        ),
        "world_location_radius": _base.Binding(
            path="LCTN/24:World Location Radius",
            kind="subrecord",
            name="World Location Radius",
        ),
        "horse_marker_ref": _base.Binding(
            path="LCTN/25:Horse Marker Ref",
            kind="subrecord",
            name="Horse Marker Ref",
        ),
        "color": _base.Binding(
            path="LCTN/26:Color",
            kind="subrecord",
            name="Color",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    added_persist_location_references: Optional[tuple[Reference6728, ...]] = (
        None
    )
    """Value decoded from this schema node."""

    master_persist_location_references: Optional[tuple[Reference6735, ...]] = (
        None
    )
    """Value decoded from this schema node."""

    removed_persist_location_references: Optional[
        tuple[_values.FormId, ...]
    ] = None
    """Value decoded from this schema node."""

    added_unique_npcs: Optional[tuple[Actor6745, ...]] = None
    """Value decoded from this schema node."""

    master_unique_npcs: Optional[tuple[Actor6751, ...]] = None
    """Value decoded from this schema node."""

    removed_unique_npcs: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    added_special_references: Optional[tuple[Reference6760, ...]] = None
    """Value decoded from this schema node."""

    master_special_references: Optional[tuple[Reference6768, ...]] = None
    """Value decoded from this schema node."""

    removed_special_references: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    added_worldsapce_cells: tuple[Structure6779, ...] = ()
    """Value decoded from this schema node."""

    master_worldspace_cells: tuple[Structure6787, ...] = ()
    """Value decoded from this schema node."""

    removed_worldspace_cells: tuple[Structure6795, ...] = ()
    """Value decoded from this schema node."""

    added_initially_disabled_references: Optional[
        tuple[_values.FormId, ...]
    ] = None
    """Value decoded from this schema node."""

    master_initially_disabled_references: Optional[
        tuple[_values.FormId, ...]
    ] = None
    """Value decoded from this schema node."""

    added_enable_point_references: Optional[tuple[Reference6809, ...]] = None
    """Value decoded from this schema node."""

    master_enable_parent_references: Optional[tuple[Reference6816, ...]] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    parent_location: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    music: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unreported_crime_faction: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    world_location_marker_ref: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    world_location_radius: Optional[float] = None
    """Value decoded from this schema node."""

    horse_marker_ref: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    color: Optional[Structure6841] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["added_persist_location_references"]
    ) -> _base.FieldRef[Optional[tuple[Reference6728, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["master_persist_location_references"]
    ) -> _base.FieldRef[Optional[tuple[Reference6735, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["removed_persist_location_references"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["added_unique_npcs"]
    ) -> _base.FieldRef[Optional[tuple[Actor6745, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["master_unique_npcs"]
    ) -> _base.FieldRef[Optional[tuple[Actor6751, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["removed_unique_npcs"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["added_special_references"]
    ) -> _base.FieldRef[Optional[tuple[Reference6760, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["master_special_references"]
    ) -> _base.FieldRef[Optional[tuple[Reference6768, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["removed_special_references"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["added_worldsapce_cells"]
    ) -> _base.FieldRef[tuple[Structure6779, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["master_worldspace_cells"]
    ) -> _base.FieldRef[tuple[Structure6787, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["removed_worldspace_cells"]
    ) -> _base.FieldRef[tuple[Structure6795, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["added_initially_disabled_references"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["master_initially_disabled_references"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["added_enable_point_references"]
    ) -> _base.FieldRef[Optional[tuple[Reference6809, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["master_enable_parent_references"]
    ) -> _base.FieldRef[Optional[tuple[Reference6816, ...]]]:
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
        self, name: Literal["keyword_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["keywords"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parent_location"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["music"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unreported_crime_faction"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["world_location_marker_ref"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["world_location_radius"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["horse_marker_ref"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["color"]
    ) -> _base.FieldRef[Optional[Structure6841]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
