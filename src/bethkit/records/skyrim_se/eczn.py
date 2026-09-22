"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure6713(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ECZN/1:DATA/payload/variants/0:Structure"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path="ECZN/1:DATA/payload/variants/0:Structure/0:Owner",
            kind="primitive",
            name="Owner",
        ),
        "location": _base.Binding(
            path=("ECZN/1:DATA/payload/variants/0:Structure/1:Location"),
            kind="primitive",
            name="Location",
        ),
    }

    owner: _values.FormId
    """Value decoded from this schema node."""

    location: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["owner"]) -> _base.FieldRef[_values.FormId]:
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


_VARIANT_6713: _base.Variant = _base.Variant(
    path="ECZN/1:DATA/payload/variants/0:Structure"
)


class Flags6721(enum.IntFlag):
    """Named values from the pinned schema."""

    NEVER_RESETS = 1
    MATCH_PC_BELOW_MINIMUM_LEVEL = 2
    DISABLE_COMBAT_BOUNDARY = 4


class Structure6716(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ECZN/1:DATA/payload/variants/1:Structure"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path="ECZN/1:DATA/payload/variants/1:Structure/0:Owner",
            kind="primitive",
            name="Owner",
        ),
        "location": _base.Binding(
            path=("ECZN/1:DATA/payload/variants/1:Structure/1:Location"),
            kind="primitive",
            name="Location",
        ),
        "rank": _base.Binding(
            path="ECZN/1:DATA/payload/variants/1:Structure/2:Rank",
            kind="primitive",
            name="Rank",
        ),
        "min_level": _base.Binding(
            path=("ECZN/1:DATA/payload/variants/1:Structure/3:Min Level"),
            kind="primitive",
            name="Min Level",
        ),
        "flags": _base.Binding(
            path="ECZN/1:DATA/payload/variants/1:Structure/4:Flags",
            kind="primitive",
            name="Flags",
        ),
        "max_level": _base.Binding(
            path=("ECZN/1:DATA/payload/variants/1:Structure/5:Max Level"),
            kind="primitive",
            name="Max Level",
        ),
    }

    owner: _values.FormId
    """Value decoded from this schema node."""

    location: _values.FormId
    """Value decoded from this schema node."""

    rank: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    min_level: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    flags: Flags6721
    """Value decoded from this schema node."""

    max_level: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["owner"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rank"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["min_level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags6721]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["max_level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
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


_VARIANT_6716: _base.Variant = _base.Variant(
    path="ECZN/1:DATA/payload/variants/1:Structure"
)


class EncounterZoneRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ECZN"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "ECZN"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="ECZN/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "data": _base.Binding(
            path="ECZN/1:DATA",
            kind="subrecord",
            name="DATA",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    data: Optional[
        Annotated[Structure6713, _VARIANT_6713]
        | Annotated[Structure6716, _VARIANT_6716]
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
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure6713, _VARIANT_6713]
            | Annotated[Structure6716, _VARIANT_6716]
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
