"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class PlaysOneSelectionAbruptTransitionCycleT7D482Ec67150(enum.IntFlag):
    """Named values from the pinned schema."""

    PLAYS_ONE_SELECTION = 1
    ABRUPT_TRANSITION = 2
    CYCLE_TRACKS = 4
    MAINTAIN_TRACK_ORDER = 8
    UNKNOWN_4 = 16
    DUCKS_CURRENT_TRACK = 32
    DOESN_T_QUEUE = 64


class Structure7152(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MUSC/2:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "priority": _base.Binding(
            path="MUSC/2:Data/payload/0:Priority",
            kind="primitive",
            name="Priority",
        ),
        "ducking_d_b": _base.Binding(
            path="MUSC/2:Data/payload/1:Ducking (dB)",
            kind="primitive",
            name="Ducking (dB)",
        ),
    }

    priority: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    ducking_d_b: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["priority"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ducking_d_b"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
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


class MusicTypeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MUSC"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "MUSC"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="MUSC/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "flags": _base.Binding(
            path="MUSC/1:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "data": _base.Binding(
            path="MUSC/2:Data",
            kind="subrecord",
            name="Data",
        ),
        "fade_duration": _base.Binding(
            path="MUSC/3:Fade Duration",
            kind="subrecord",
            name="Fade Duration",
        ),
        "music_tracks": _base.Binding(
            path="MUSC/4:Music Tracks",
            kind="subrecord",
            name="Music Tracks",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    flags: Optional[PlaysOneSelectionAbruptTransitionCycleT7D482Ec67150] = None
    """Value decoded from this schema node."""

    data: Optional[Structure7152] = None
    """Value decoded from this schema node."""

    fade_duration: Optional[float] = None
    """Value decoded from this schema node."""

    music_tracks: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[PlaysOneSelectionAbruptTransitionCycleT7D482Ec67150]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure7152]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fade_duration"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["music_tracks"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
