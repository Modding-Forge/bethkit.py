"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure18364(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCOL/1:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="SCOL/1:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="SCOL/1:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="SCOL/1:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="SCOL/1:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="SCOL/1:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="SCOL/1:Object Bounds/payload/5:Z2",
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


class Structure18376(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18378": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18379": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18380": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_18378: bytes
    """Value decoded from this schema node."""

    unused_18379: bytes
    """Value decoded from this schema node."""

    unused_18380: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18378"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18379"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18380"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_18376: _base.Variant = _base.Variant(
    path=("SCOL/2:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure18381(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_18384": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18385": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/1:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_18384: bytes
    """Value decoded from this schema node."""

    unused_18385: bytes
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
    def field(self, name: Literal["unused_18384"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18385"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_18381: _base.Variant = _base.Variant(
    path=("SCOL/2:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture18389(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/2:Folder Hash"
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


class Structure18386(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_18393": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_18394": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture18389, ...]
    """Value decoded from this schema node."""

    unused_18393: bytes
    """Value decoded from this schema node."""

    unused_18394: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture18389, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18393"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_18394"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_18386: _base.Variant = _base.Variant(
    path=("SCOL/2:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture18399(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/2:Folder Hash"
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


class Material18406(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/2:Folder Hash"
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


class Structure18395(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "SCOL/2:Model/1:Model Information/payload/variants/3:St"
                "ructure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture18399, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material18406, ...]
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
    ) -> _base.FieldRef[tuple[Texture18399, ...]]:
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
    ) -> _base.FieldRef[tuple[Material18406, ...]]:
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


_VARIANT_18395: _base.Variant = _base.Variant(
    path=("SCOL/2:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture18413(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/2:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "SCOL/2:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "SCOL/2:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "SCOL/2:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model18371(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCOL/2:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="SCOL/2:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="SCOL/2:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="SCOL/2:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure18376, _VARIANT_18376]
        | Annotated[Structure18381, _VARIANT_18381]
        | Annotated[Structure18386, _VARIANT_18386]
        | Annotated[Structure18395, _VARIANT_18395]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture18413, ...]] = None
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
            Annotated[Structure18376, _VARIANT_18376]
            | Annotated[Structure18381, _VARIANT_18381]
            | Annotated[Structure18386, _VARIANT_18386]
            | Annotated[Structure18395, _VARIANT_18395]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture18413, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Position18424(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/element/0:Position"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/0:Position/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/0:Position/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/0:Position/2:Z"
            ),
            kind="primitive",
            name="Z",
        ),
    }

    x: float
    """Value decoded from this schema node."""

    y: float
    """Value decoded from this schema node."""

    z: float
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
    def field(self, name: Literal["z"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Rotation18428(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/element/1:Rotation"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/1:Rotation/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/1:Rotation/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/1:Rotation/2:Z"
            ),
            kind="primitive",
            name="Z",
        ),
    }

    x: float
    """Value decoded from this schema node."""

    y: float
    """Value decoded from this schema node."""

    z: float
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
    def field(self, name: Literal["z"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Placement18423(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "position": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/0:Position"
            ),
            kind="struct",
            name="Position",
        ),
        "rotation": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/1:Rotation"
            ),
            kind="struct",
            name="Rotation",
        ),
        "scale": _base.Binding(
            path=(
                "SCOL/3:Parts/repeat/0:Part/1:Placements/payload/elemen"
                "t/2:Scale"
            ),
            kind="primitive",
            name="Scale",
        ),
    }

    position: Position18424
    """Value decoded from this schema node."""

    rotation: Rotation18428
    """Value decoded from this schema node."""

    scale: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position18424]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotation"]) -> _base.FieldRef[Rotation18428]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Part18418(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCOL/3:Parts/repeat/0:Part"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "static": _base.Binding(
            path="SCOL/3:Parts/repeat/0:Part/0:Static",
            kind="subrecord",
            name="Static",
        ),
        "placements": _base.Binding(
            path="SCOL/3:Parts/repeat/0:Part/1:Placements",
            kind="subrecord",
            name="Placements",
        ),
    }

    static: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    placements: Optional[tuple[Placement18423, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["static"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["placements"]
    ) -> _base.FieldRef[Optional[tuple[Placement18423, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class StaticCollectionRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCOL"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SCOL"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SCOL/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "object_bounds": _base.Binding(
            path="SCOL/1:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "model": _base.Binding(
            path="SCOL/2:Model",
            kind="unordered",
            name="Model",
        ),
        "parts": _base.Binding(
            path="SCOL/3:Parts",
            kind="repeat",
            name="Parts",
            repeated_path="SCOL/3:Parts/repeat/0:Part",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure18364] = None
    """Value decoded from this schema node."""

    model: Optional[Model18371] = None
    """Value decoded from this schema node."""

    parts: tuple[Part18418, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure18364]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model18371]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parts"]
    ) -> _base.FieldRef[tuple[Part18418, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
