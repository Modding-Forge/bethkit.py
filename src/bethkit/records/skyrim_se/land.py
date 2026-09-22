"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class HasVertexNormalsHeightMapHasVertexColoE11F3Af510199(enum.IntFlag):
    """Named values from the pinned schema."""

    HAS_VERTEX_NORMALS_HEIGHT_MAP = 1
    HAS_VERTEX_COLOURS = 2
    HAS_LAYERS = 4
    UNKNOWN_4 = 8
    AUTO_CALC_NORMALS = 16
    VALUE = 32
    VALUE_6 = 64
    VALUE_7 = 128
    VALUE_8 = 256
    VALUE_9 = 512
    MPCD = 1024


class Column10204(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LAND/1:Vertex Normals/payload/element/0:Columns/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "LAND/1:Vertex Normals/payload/element/0:Columns/element/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "LAND/1:Vertex Normals/payload/element/0:Columns/element/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "LAND/1:Vertex Normals/payload/element/0:Columns/element/2:Z"
            ),
            kind="primitive",
            name="Z",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    z: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z"]
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


class Row10202(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LAND/1:Vertex Normals/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "columns": _base.Binding(
            path="LAND/1:Vertex Normals/payload/element/0:Columns",
            kind="array",
            name="Columns",
        ),
    }

    columns: tuple[Column10204, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["columns"]
    ) -> _base.FieldRef[tuple[Column10204, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Row10212(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LAND/2:Vertex Height Map/payload/1:Rows/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "columns": _base.Binding(
            path=("LAND/2:Vertex Height Map/payload/1:Rows/element/0:Columns"),
            kind="array",
            name="Columns",
        ),
    }

    columns: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)], ...
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["columns"]
    ) -> _base.FieldRef[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)], ...]
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


class Structure10209(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LAND/2:Vertex Height Map/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "offset": _base.Binding(
            path="LAND/2:Vertex Height Map/payload/0:Offset",
            kind="primitive",
            name="Offset",
        ),
        "rows": _base.Binding(
            path="LAND/2:Vertex Height Map/payload/1:Rows",
            kind="array",
            name="Rows",
        ),
        "unused": _base.Binding(
            path="LAND/2:Vertex Height Map/payload/2:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    offset: float
    """Value decoded from this schema node."""

    rows: tuple[Row10212, ...]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["offset"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rows"]
    ) -> _base.FieldRef[tuple[Row10212, ...]]:
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


class Column10220(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LAND/3:Vertex Colours/payload/element/0:Columns/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "LAND/3:Vertex Colours/payload/element/0:Columns/element/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "LAND/3:Vertex Colours/payload/element/0:Columns/element/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "LAND/3:Vertex Colours/payload/element/0:Columns/element/2:Z"
            ),
            kind="primitive",
            name="Z",
        ),
    }

    x: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    y: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    z: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["x"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["y"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["z"]
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


class Row10218(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LAND/3:Vertex Colours/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "columns": _base.Binding(
            path="LAND/3:Vertex Colours/payload/element/0:Columns",
            kind="array",
            name="Columns",
        ),
    }

    columns: tuple[Column10220, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["columns"]
    ) -> _base.FieldRef[tuple[Column10220, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Quadrant10230(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    BOTTOM_LEFT = 0
    BOTTOM_RIGHT = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3


class Structure10228(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LAND/4:Layers/repeat/0:Layer/0:Base Layer/0:Base Layer Header/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "texture": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/0:Base Layer/0:Base Layer"
                " Header/payload/0:Texture"
            ),
            kind="primitive",
            name="Texture",
        ),
        "quadrant": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/0:Base Layer/0:Base Layer"
                " Header/payload/1:Quadrant"
            ),
            kind="primitive",
            name="Quadrant",
        ),
        "unused": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/0:Base Layer/0:Base Layer"
                " Header/payload/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "layer": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/0:Base Layer/0:Base Layer"
                " Header/payload/3:Layer"
            ),
            kind="primitive",
            name="Layer",
        ),
    }

    texture: _values.FormId
    """Value decoded from this schema node."""

    quadrant: Quadrant10230
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    layer: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["texture"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["quadrant"]) -> _base.FieldRef[Quadrant10230]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["layer"]
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


class BaseLayer10226(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LAND/4:Layers/repeat/0:Layer/0:Base Layer"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "base_layer_header": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/0:Base Layer/0:Base Layer Header"
            ),
            kind="subrecord",
            name="Base Layer Header",
        ),
    }

    base_layer_header: Optional[Structure10228] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["base_layer_header"]
    ) -> _base.FieldRef[Optional[Structure10228]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10226: _base.Variant = _base.Variant(
    path="LAND/4:Layers/repeat/0:Layer/0:Base Layer"
)


class Quadrant10237(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    BOTTOM_LEFT = 0
    BOTTOM_RIGHT = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3


class Structure10235(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/0:Alpha Lay"
        "er Header/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "texture": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/0:Alpha Lay"
                "er Header/payload/0:Texture"
            ),
            kind="primitive",
            name="Texture",
        ),
        "quadrant": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/0:Alpha Lay"
                "er Header/payload/1:Quadrant"
            ),
            kind="primitive",
            name="Quadrant",
        ),
        "unused": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/0:Alpha Lay"
                "er Header/payload/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "layer": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/0:Alpha Lay"
                "er Header/payload/3:Layer"
            ),
            kind="primitive",
            name="Layer",
        ),
    }

    texture: _values.FormId
    """Value decoded from this schema node."""

    quadrant: Quadrant10237
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    layer: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["texture"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["quadrant"]) -> _base.FieldRef[Quadrant10237]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["layer"]
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


class Cell10242(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/1:Alpha Lay"
        "er Data/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "position": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/1:Alpha Lay"
                "er Data/payload/element/0:Position"
            ),
            kind="primitive",
            name="Position",
        ),
        "unused": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/1:Alpha Lay"
                "er Data/payload/element/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "opacity": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/1:Alpha Lay"
                "er Data/payload/element/2:Opacity"
            ),
            kind="primitive",
            name="Opacity",
        ),
    }

    position: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    opacity: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["position"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["opacity"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class AlphaLayer10233(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alpha_layer_header": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/0:Alpha Lay"
                "er Header"
            ),
            kind="subrecord",
            name="Alpha Layer Header",
        ),
        "alpha_layer_data": _base.Binding(
            path=(
                "LAND/4:Layers/repeat/0:Layer/1:Alpha Layer/1:Alpha Layer Data"
            ),
            kind="subrecord",
            name="Alpha Layer Data",
        ),
    }

    alpha_layer_header: Optional[Structure10235] = None
    """Value decoded from this schema node."""

    alpha_layer_data: Optional[tuple[Cell10242, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alpha_layer_header"]
    ) -> _base.FieldRef[Optional[Structure10235]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alpha_layer_data"]
    ) -> _base.FieldRef[Optional[tuple[Cell10242, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10233: _base.Variant = _base.Variant(
    path="LAND/4:Layers/repeat/0:Layer/1:Alpha Layer"
)


class LandscapeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LAND"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LAND"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="LAND/0:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "vertex_normals": _base.Binding(
            path="LAND/1:Vertex Normals",
            kind="subrecord",
            name="Vertex Normals",
        ),
        "vertex_height_map": _base.Binding(
            path="LAND/2:Vertex Height Map",
            kind="subrecord",
            name="Vertex Height Map",
        ),
        "vertex_colours": _base.Binding(
            path="LAND/3:Vertex Colours",
            kind="subrecord",
            name="Vertex Colours",
        ),
        "layers": _base.Binding(
            path="LAND/4:Layers",
            kind="repeat",
            name="Layers",
            repeated_path="LAND/4:Layers/repeat/0:Layer",
            child_kind="choice",
        ),
        "unknown": _base.Binding(
            path="LAND/5:Unknown",
            kind="repeat",
            name="Unknown",
            repeated_path="LAND/5:Unknown/repeat/0:Unknown",
            child_kind="subrecord",
        ),
    }

    flags: Optional[HasVertexNormalsHeightMapHasVertexColoE11F3Af510199] = None
    """Value decoded from this schema node."""

    vertex_normals: Optional[tuple[Row10202, ...]] = None
    """Value decoded from this schema node."""

    vertex_height_map: Optional[Structure10209] = None
    """Value decoded from this schema node."""

    vertex_colours: Optional[tuple[Row10218, ...]] = None
    """Value decoded from this schema node."""

    layers: tuple[
        Annotated[BaseLayer10226, _VARIANT_10226]
        | Annotated[AlphaLayer10233, _VARIANT_10233],
        ...,
    ] = ()
    """Value decoded from this schema node."""

    unknown: tuple[bytes, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[HasVertexNormalsHeightMapHasVertexColoE11F3Af510199]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vertex_normals"]
    ) -> _base.FieldRef[Optional[tuple[Row10202, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vertex_height_map"]
    ) -> _base.FieldRef[Optional[Structure10209]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vertex_colours"]
    ) -> _base.FieldRef[Optional[tuple[Row10218, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["layers"]
    ) -> _base.FieldRef[
        tuple[
            Annotated[BaseLayer10226, _VARIANT_10226]
            | Annotated[AlphaLayer10233, _VARIANT_10233],
            ...,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[tuple[bytes, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
