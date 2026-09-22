"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Reference17413(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/1:Large References/repeat/0:Grid/payload/2:References/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ref": _base.Binding(
            path=(
                "WRLD/1:Large References/repeat/0:Grid/payload/2:Refere"
                "nces/element/0:Ref"
            ),
            kind="primitive",
            name="Ref",
        ),
        "y": _base.Binding(
            path=(
                "WRLD/1:Large References/repeat/0:Grid/payload/2:Refere"
                "nces/element/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "x": _base.Binding(
            path=(
                "WRLD/1:Large References/repeat/0:Grid/payload/2:Refere"
                "nces/element/2:X"
            ),
            kind="primitive",
            name="X",
        ),
    }

    ref: _values.FormId
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["ref"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["x"]
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


class Structure17409(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/1:Large References/repeat/0:Grid/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "y": _base.Binding(
            path="WRLD/1:Large References/repeat/0:Grid/payload/0:Y",
            kind="primitive",
            name="Y",
        ),
        "x": _base.Binding(
            path="WRLD/1:Large References/repeat/0:Grid/payload/1:X",
            kind="primitive",
            name="X",
        ),
        "references": _base.Binding(
            path=("WRLD/1:Large References/repeat/0:Grid/payload/2:References"),
            kind="array",
            name="References",
        ),
    }

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    references: tuple[Reference17413, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["references"]
    ) -> _base.FieldRef[tuple[Reference17413, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Min17419(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/2:Max Height Data/payload/0:Min"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WRLD/2:Max Height Data/payload/0:Min/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WRLD/2:Max Height Data/payload/0:Min/1:Y",
            kind="primitive",
            name="Y",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
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


class Max17422(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/2:Max Height Data/payload/1:Max"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WRLD/2:Max Height Data/payload/1:Max/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WRLD/2:Max Height Data/payload/1:Max/1:Y",
            kind="primitive",
            name="Y",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
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


class Structure17418(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/2:Max Height Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "min": _base.Binding(
            path="WRLD/2:Max Height Data/payload/0:Min",
            kind="struct",
            name="Min",
        ),
        "max": _base.Binding(
            path="WRLD/2:Max Height Data/payload/1:Max",
            kind="struct",
            name="Max",
        ),
        "cell_data": _base.Binding(
            path="WRLD/2:Max Height Data/payload/2:Cell Data",
            kind="primitive",
            name="Cell Data",
        ),
    }

    min: Min17419
    """Value decoded from this schema node."""

    max: Max17422
    """Value decoded from this schema node."""

    cell_data: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["min"]) -> _base.FieldRef[Min17419]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max"]) -> _base.FieldRef[Max17422]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["cell_data"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17429(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/4:Fixed Dimensions Center Cell/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WRLD/4:Fixed Dimensions Center Cell/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WRLD/4:Fixed Dimensions Center Cell/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
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


class Flags17443(enum.IntFlag):
    """Named values from the pinned schema."""

    USE_LAND_DATA = 1
    USE_LOD_DATA = 2
    USE_MAP_DATA = 4
    USE_WATER_DATA = 8
    USE_CLIMATE_DATA = 16
    USE_IMAGE_SPACE_DATA_UNUSED = 32
    USE_SKY_CELL = 64


class Structure17442(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/8:Parent/1:PNAM/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="WRLD/8:Parent/1:PNAM/payload/0:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unknown": _base.Binding(
            path="WRLD/8:Parent/1:PNAM/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    flags: Flags17443
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags17443]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Parent17438(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/8:Parent"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "worldspace": _base.Binding(
            path="WRLD/8:Parent/0:Worldspace",
            kind="subrecord",
            name="Worldspace",
        ),
        "pnam": _base.Binding(
            path="WRLD/8:Parent/1:PNAM",
            kind="subrecord",
            name="PNAM",
        ),
    }

    worldspace: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    pnam: Optional[Structure17442] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["worldspace"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["pnam"]
    ) -> _base.FieldRef[Optional[Structure17442]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17454(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/13:Land Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "default_land_height": _base.Binding(
            path="WRLD/13:Land Data/payload/0:Default Land Height",
            kind="primitive",
            name="Default Land Height",
        ),
        "default_water_height": _base.Binding(
            path="WRLD/13:Land Data/payload/1:Default Water Height",
            kind="primitive",
            name="Default Water Height",
        ),
    }

    default_land_height: float
    """Value decoded from this schema node."""

    default_water_height: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["default_land_height"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_water_height"]
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


class Structure17465(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17467": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17468": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17469": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_17467: bytes
    """Value decoded from this schema node."""

    unused_17468: bytes
    """Value decoded from this schema node."""

    unused_17469: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17467"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17468"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17469"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17465: _base.Variant = _base.Variant(
    path=(
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/0:Structure"
    )
)


class Structure17470(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_17473": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17474": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_17473: bytes
    """Value decoded from this schema node."""

    unused_17474: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["error"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17473"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17474"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17470: _base.Variant = _base.Variant(
    path=(
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/1:Structure"
    )
)


class Texture17478(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/2:Structure/1:Textures/element/2:Folder Has"
                "h"
            ),
            kind="primitive",
            name="Folder Hash",
        ),
    }

    file_hash: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    extension: str
    """Value decoded from this schema node."""

    folder_hash: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["extension"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["folder_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class Structure17475(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_17482": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17483": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture17478, ...]
    """Value decoded from this schema node."""

    unused_17482: bytes
    """Value decoded from this schema node."""

    unused_17483: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture17478, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17482"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17483"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17475: _base.Variant = _base.Variant(
    path=(
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/2:Structure"
    )
)


class Texture17488(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/1:Textures/element/2:Folder Has"
                "h"
            ),
            kind="primitive",
            name="Folder Hash",
        ),
    }

    file_hash: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    extension: str
    """Value decoded from this schema node."""

    folder_hash: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["extension"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["folder_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class Material17495(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/3:Materials/element/2:Folder Ha"
                "sh"
            ),
            kind="primitive",
            name="Folder Hash",
        ),
    }

    file_hash: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    extension: str
    """Value decoded from this schema node."""

    folder_hash: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["extension"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["folder_hash"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class Structure17484(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
                "d/variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture17488, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material17495, ...]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["headers"]
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
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture17488, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["addons"]
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
        self, name: Literal["materials"]
    ) -> _base.FieldRef[tuple[Material17495, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17484: _base.Variant = _base.Variant(
    path=(
        "WRLD/15:Cloud Model/0:Model/1:Model Information/payloa"
        "d/variants/3:Structure"
    )
)


class AlternateTexture17502(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/15:Cloud Model/0:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/2:Alternate Textures/paylo"
                "ad/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/2:Alternate Textures/paylo"
                "ad/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "WRLD/15:Cloud Model/0:Model/2:Alternate Textures/paylo"
                "ad/element/2:3D Index"
            ),
            kind="primitive",
            name="3D Index",
        ),
    }

    value_3_d_name: str
    """Value decoded from this schema node."""

    new_texture: _values.FormId
    """Value decoded from this schema node."""

    value_3_d_index: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["value_3_d_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["new_texture"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value_3_d_index"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
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


class Model17460(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/15:Cloud Model/0:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="WRLD/15:Cloud Model/0:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="WRLD/15:Cloud Model/0:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="WRLD/15:Cloud Model/0:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure17465, _VARIANT_17465]
        | Annotated[Structure17470, _VARIANT_17470]
        | Annotated[Structure17475, _VARIANT_17475]
        | Annotated[Structure17484, _VARIANT_17484]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture17502, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["model_file_name_value"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_information_value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure17465, _VARIANT_17465]
            | Annotated[Structure17470, _VARIANT_17470]
            | Annotated[Structure17475, _VARIANT_17475]
            | Annotated[Structure17484, _VARIANT_17484]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture17502, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class CloudModel17459(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/15:Cloud Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model": _base.Binding(
            path="WRLD/15:Cloud Model/0:Model",
            kind="unordered",
            name="Model",
        ),
    }

    model: Optional[Model17460] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model17460]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class UsableDimensions17508(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/16:Map Data/payload/0:Usable Dimensions"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WRLD/16:Map Data/payload/0:Usable Dimensions/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WRLD/16:Map Data/payload/0:Usable Dimensions/1:Y",
            kind="primitive",
            name="Y",
        ),
    }

    x: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    y: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
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


class NwCell17512(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/16:Map Data/payload/1:Cell Coordinates/0:NW Cell"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("WRLD/16:Map Data/payload/1:Cell Coordinates/0:NW Cell/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("WRLD/16:Map Data/payload/1:Cell Coordinates/0:NW Cell/1:Y"),
            kind="primitive",
            name="Y",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
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


class SeCell17515(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WRLD/16:Map Data/payload/1:Cell Coordinates/1:SE Cell"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("WRLD/16:Map Data/payload/1:Cell Coordinates/1:SE Cell/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("WRLD/16:Map Data/payload/1:Cell Coordinates/1:SE Cell/1:Y"),
            kind="primitive",
            name="Y",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
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


class CellCoordinates17511(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/16:Map Data/payload/1:Cell Coordinates"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "nw_cell": _base.Binding(
            path=("WRLD/16:Map Data/payload/1:Cell Coordinates/0:NW Cell"),
            kind="struct",
            name="NW Cell",
        ),
        "se_cell": _base.Binding(
            path=("WRLD/16:Map Data/payload/1:Cell Coordinates/1:SE Cell"),
            kind="struct",
            name="SE Cell",
        ),
    }

    nw_cell: NwCell17512
    """Value decoded from this schema node."""

    se_cell: SeCell17515
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["nw_cell"]) -> _base.FieldRef[NwCell17512]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["se_cell"]) -> _base.FieldRef[SeCell17515]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class CameraData17518(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/16:Map Data/payload/2:Camera Data"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "min_height": _base.Binding(
            path=("WRLD/16:Map Data/payload/2:Camera Data/0:Min Height"),
            kind="primitive",
            name="Min Height",
        ),
        "max_height": _base.Binding(
            path=("WRLD/16:Map Data/payload/2:Camera Data/1:Max Height"),
            kind="primitive",
            name="Max Height",
        ),
        "initial_pitch": _base.Binding(
            path=("WRLD/16:Map Data/payload/2:Camera Data/2:Initial Pitch"),
            kind="primitive",
            name="Initial Pitch",
        ),
    }

    min_height: float
    """Value decoded from this schema node."""

    max_height: float
    """Value decoded from this schema node."""

    initial_pitch: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["min_height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["initial_pitch"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17507(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/16:Map Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "usable_dimensions": _base.Binding(
            path="WRLD/16:Map Data/payload/0:Usable Dimensions",
            kind="struct",
            name="Usable Dimensions",
        ),
        "cell_coordinates": _base.Binding(
            path="WRLD/16:Map Data/payload/1:Cell Coordinates",
            kind="struct",
            name="Cell Coordinates",
        ),
        "camera_data": _base.Binding(
            path="WRLD/16:Map Data/payload/2:Camera Data",
            kind="struct",
            name="Camera Data",
        ),
    }

    usable_dimensions: UsableDimensions17508
    """Value decoded from this schema node."""

    cell_coordinates: CellCoordinates17511
    """Value decoded from this schema node."""

    camera_data: Optional[CameraData17518] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["usable_dimensions"]
    ) -> _base.FieldRef[UsableDimensions17508]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cell_coordinates"]
    ) -> _base.FieldRef[CellCoordinates17511]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["camera_data"]
    ) -> _base.FieldRef[Optional[CameraData17518]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17523(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/17:World Map Offset Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "world_map_scale": _base.Binding(
            path=("WRLD/17:World Map Offset Data/payload/0:World Map Scale"),
            kind="primitive",
            name="World Map Scale",
        ),
        "cell_x_offset": _base.Binding(
            path=("WRLD/17:World Map Offset Data/payload/1:Cell X Offset"),
            kind="primitive",
            name="Cell X Offset",
        ),
        "cell_y_offset": _base.Binding(
            path=("WRLD/17:World Map Offset Data/payload/2:Cell Y Offset"),
            kind="primitive",
            name="Cell Y Offset",
        ),
        "cell_z_offset": _base.Binding(
            path=("WRLD/17:World Map Offset Data/payload/3:Cell Z Offset"),
            kind="primitive",
            name="Cell Z Offset",
        ),
    }

    world_map_scale: float
    """Value decoded from this schema node."""

    cell_x_offset: float
    """Value decoded from this schema node."""

    cell_y_offset: float
    """Value decoded from this schema node."""

    cell_z_offset: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["world_map_scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["cell_x_offset"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["cell_y_offset"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["cell_z_offset"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class SmallWorldCanTFastTravelUnknown3NoLoAf31064617531(enum.IntFlag):
    """Named values from the pinned schema."""

    SMALL_WORLD = 1
    CAN_T_FAST_TRAVEL = 2
    UNKNOWN_3 = 4
    NO_LOD_WATER = 8
    NO_LANDSCAPE = 16
    NO_SKY = 32
    FIXED_DIMENSIONS = 64
    NO_GRASS = 128


class Structure17534(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/20:Object Bounds/0:Min/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WRLD/20:Object Bounds/0:Min/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WRLD/20:Object Bounds/0:Min/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
    }

    x: float
    """Value decoded from this schema node."""

    y: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17538(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/20:Object Bounds/1:Max/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="WRLD/20:Object Bounds/1:Max/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="WRLD/20:Object Bounds/1:Max/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
    }

    x: float
    """Value decoded from this schema node."""

    y: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["x"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["y"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ObjectBounds17532(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD/20:Object Bounds"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "min": _base.Binding(
            path="WRLD/20:Object Bounds/0:Min",
            kind="subrecord",
            name="Min",
        ),
        "max": _base.Binding(
            path="WRLD/20:Object Bounds/1:Max",
            kind="subrecord",
            name="Max",
        ),
    }

    min: Optional[Structure17534] = None
    """Value decoded from this schema node."""

    max: Optional[Structure17538] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["min"]
    ) -> _base.FieldRef[Optional[Structure17534]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["max"]
    ) -> _base.FieldRef[Optional[Structure17538]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class WorldspaceRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WRLD"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "WRLD"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="WRLD/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "large_references": _base.Binding(
            path="WRLD/1:Large References",
            kind="repeat",
            name="Large References",
            repeated_path="WRLD/1:Large References/repeat/0:Grid",
            child_kind="subrecord",
        ),
        "max_height_data": _base.Binding(
            path="WRLD/2:Max Height Data",
            kind="subrecord",
            name="Max Height Data",
        ),
        "name": _base.Binding(
            path="WRLD/3:Name",
            kind="subrecord",
            name="Name",
        ),
        "fixed_dimensions_center_cell": _base.Binding(
            path="WRLD/4:Fixed Dimensions Center Cell",
            kind="subrecord",
            name="Fixed Dimensions Center Cell",
        ),
        "interior_lighting": _base.Binding(
            path="WRLD/5:Interior Lighting",
            kind="subrecord",
            name="Interior Lighting",
        ),
        "encounter_zone": _base.Binding(
            path="WRLD/6:Encounter Zone",
            kind="subrecord",
            name="Encounter Zone",
        ),
        "location": _base.Binding(
            path="WRLD/7:Location",
            kind="subrecord",
            name="Location",
        ),
        "parent": _base.Binding(
            path="WRLD/8:Parent",
            kind="sequence",
            name="Parent",
        ),
        "climate": _base.Binding(
            path="WRLD/9:Climate",
            kind="subrecord",
            name="Climate",
        ),
        "water": _base.Binding(
            path="WRLD/10:Water",
            kind="subrecord",
            name="Water",
        ),
        "lod_water_type": _base.Binding(
            path="WRLD/11:LOD Water Type",
            kind="subrecord",
            name="LOD Water Type",
        ),
        "lod_water_height": _base.Binding(
            path="WRLD/12:LOD Water Height",
            kind="subrecord",
            name="LOD Water Height",
        ),
        "land_data": _base.Binding(
            path="WRLD/13:Land Data",
            kind="subrecord",
            name="Land Data",
        ),
        "map_image": _base.Binding(
            path="WRLD/14:Map Image",
            kind="subrecord",
            name="Map Image",
        ),
        "cloud_model": _base.Binding(
            path="WRLD/15:Cloud Model",
            kind="sequence",
            name="Cloud Model",
        ),
        "map_data": _base.Binding(
            path="WRLD/16:Map Data",
            kind="subrecord",
            name="Map Data",
        ),
        "world_map_offset_data": _base.Binding(
            path="WRLD/17:World Map Offset Data",
            kind="subrecord",
            name="World Map Offset Data",
        ),
        "distant_lod_multiplier": _base.Binding(
            path="WRLD/18:Distant LOD Multiplier",
            kind="subrecord",
            name="Distant LOD Multiplier",
        ),
        "flags": _base.Binding(
            path="WRLD/19:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "object_bounds": _base.Binding(
            path="WRLD/20:Object Bounds",
            kind="sequence",
            name="Object Bounds",
        ),
        "music": _base.Binding(
            path="WRLD/21:Music",
            kind="subrecord",
            name="Music",
        ),
        "canopy_shadow_unused": _base.Binding(
            path="WRLD/22:Canopy Shadow (unused)",
            kind="subrecord",
            name="Canopy Shadow (unused)",
        ),
        "water_noise_texture": _base.Binding(
            path="WRLD/23:Water Noise Texture",
            kind="subrecord",
            name="Water Noise Texture",
        ),
        "hd_lod_diffuse_texture": _base.Binding(
            path="WRLD/24:HD LOD Diffuse Texture",
            kind="subrecord",
            name="HD LOD Diffuse Texture",
        ),
        "hd_lod_normal_texture": _base.Binding(
            path="WRLD/25:HD LOD Normal Texture",
            kind="subrecord",
            name="HD LOD Normal Texture",
        ),
        "water_environment_map_unused": _base.Binding(
            path="WRLD/26:Water Environment Map (unused)",
            kind="subrecord",
            name="Water Environment Map (unused)",
        ),
        "offset_data": _base.Binding(
            path="WRLD/27:Offset Data",
            kind="subrecord",
            name="Offset Data",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    large_references: tuple[Structure17409, ...] = ()
    """Value decoded from this schema node."""

    max_height_data: Optional[Structure17418] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    fixed_dimensions_center_cell: Optional[Structure17429] = None
    """Value decoded from this schema node."""

    interior_lighting: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    encounter_zone: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    location: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    parent: Optional[Parent17438] = None
    """Value decoded from this schema node."""

    climate: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    water: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    lod_water_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    lod_water_height: Optional[float] = None
    """Value decoded from this schema node."""

    land_data: Optional[Structure17454] = None
    """Value decoded from this schema node."""

    map_image: Optional[str] = None
    """Value decoded from this schema node."""

    cloud_model: Optional[CloudModel17459] = None
    """Value decoded from this schema node."""

    map_data: Optional[Structure17507] = None
    """Value decoded from this schema node."""

    world_map_offset_data: Optional[Structure17523] = None
    """Value decoded from this schema node."""

    distant_lod_multiplier: Optional[float] = None
    """Value decoded from this schema node."""

    flags: Optional[SmallWorldCanTFastTravelUnknown3NoLoAf31064617531] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[ObjectBounds17532] = None
    """Value decoded from this schema node."""

    music: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    canopy_shadow_unused: Optional[str] = None
    """Value decoded from this schema node."""

    water_noise_texture: Optional[str] = None
    """Value decoded from this schema node."""

    hd_lod_diffuse_texture: Optional[str] = None
    """Value decoded from this schema node."""

    hd_lod_normal_texture: Optional[str] = None
    """Value decoded from this schema node."""

    water_environment_map_unused: Optional[str] = None
    """Value decoded from this schema node."""

    offset_data: Optional[
        tuple[
            tuple[
                Annotated[
                    int, pydantic.Field(strict=True, ge=0, le=4294967295)
                ],
                ...,
            ],
            ...,
        ]
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
        self, name: Literal["large_references"]
    ) -> _base.FieldRef[tuple[Structure17409, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["max_height_data"]
    ) -> _base.FieldRef[Optional[Structure17418]]:
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
        self, name: Literal["fixed_dimensions_center_cell"]
    ) -> _base.FieldRef[Optional[Structure17429]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["interior_lighting"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["encounter_zone"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parent"]
    ) -> _base.FieldRef[Optional[Parent17438]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["climate"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lod_water_type"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lod_water_height"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["land_data"]
    ) -> _base.FieldRef[Optional[Structure17454]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["map_image"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cloud_model"]
    ) -> _base.FieldRef[Optional[CloudModel17459]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["map_data"]
    ) -> _base.FieldRef[Optional[Structure17507]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["world_map_offset_data"]
    ) -> _base.FieldRef[Optional[Structure17523]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["distant_lod_multiplier"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[SmallWorldCanTFastTravelUnknown3NoLoAf31064617531]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[ObjectBounds17532]]:
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
        self, name: Literal["canopy_shadow_unused"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_noise_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hd_lod_diffuse_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hd_lod_normal_texture"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_environment_map_unused"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["offset_data"]
    ) -> _base.FieldRef[
        Optional[
            tuple[
                tuple[
                    Annotated[
                        int, pydantic.Field(strict=True, ge=0, le=4294967295)
                    ],
                    ...,
                ],
                ...,
            ]
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
