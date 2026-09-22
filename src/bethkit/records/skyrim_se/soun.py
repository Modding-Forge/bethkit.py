"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure16012(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SOUN/1:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="SOUN/1:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="SOUN/1:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="SOUN/1:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="SOUN/1:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="SOUN/1:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="SOUN/1:Object Bounds/payload/5:Z2",
            kind="primitive",
            name="Z2",
        ),
    }

    x1: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y1: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    z1: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    x2: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y2: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    z2: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x1"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y1"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z1"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["x2"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y2"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z2"]
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


class SoundMarkerRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SOUN"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SOUN"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SOUN/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "object_bounds": _base.Binding(
            path="SOUN/1:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "unknown": _base.Binding(
            path="SOUN/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_16021": _base.Binding(
            path="SOUN/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "sound_descriptor": _base.Binding(
            path="SOUN/4:Sound Descriptor",
            kind="subrecord",
            name="Sound Descriptor",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure16012] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_16021: Optional[bytes] = None
    """Value decoded from this schema node."""

    sound_descriptor: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[Structure16012]]:
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
        self, name: Literal["unknown_16021"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sound_descriptor"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
