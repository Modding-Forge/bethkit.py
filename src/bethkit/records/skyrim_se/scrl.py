"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure16232(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/1:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="SCRL/1:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="SCRL/1:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="SCRL/1:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="SCRL/1:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="SCRL/1:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="SCRL/1:Object Bounds/payload/5:Z2",
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


class Structure16257(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16259": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16260": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16261": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_16259: bytes
    """Value decoded from this schema node."""

    unused_16260: bytes
    """Value decoded from this schema node."""

    unused_16261: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16259"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16260"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16261"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16257: _base.Variant = _base.Variant(
    path=("SCRL/8:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure16262(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_16265": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16266": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/1:St"
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

    unused_16265: bytes
    """Value decoded from this schema node."""

    unused_16266: bytes
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
    def field(self, name: Literal["unused_16265"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16266"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16262: _base.Variant = _base.Variant(
    path=("SCRL/8:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture16270(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/2:St"
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


class Structure16267(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_16274": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16275": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture16270, ...]
    """Value decoded from this schema node."""

    unused_16274: bytes
    """Value decoded from this schema node."""

    unused_16275: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture16270, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16274"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16275"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16267: _base.Variant = _base.Variant(
    path=("SCRL/8:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture16280(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
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


class Material16287(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
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


class Structure16276(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "SCRL/8:Model/1:Model Information/payload/variants/3:St"
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

    textures: tuple[Texture16280, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material16287, ...]
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
    ) -> _base.FieldRef[tuple[Texture16280, ...]]:
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
    ) -> _base.FieldRef[tuple[Material16287, ...]]:
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


_VARIANT_16276: _base.Variant = _base.Variant(
    path=("SCRL/8:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture16294(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/8:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "SCRL/8:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "SCRL/8:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "SCRL/8:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model16252(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/8:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="SCRL/8:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="SCRL/8:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="SCRL/8:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure16257, _VARIANT_16257]
        | Annotated[Structure16262, _VARIANT_16262]
        | Annotated[Structure16267, _VARIANT_16267]
        | Annotated[Structure16276, _VARIANT_16276]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture16294, ...]] = None
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
            Annotated[Structure16257, _VARIANT_16257]
            | Annotated[Structure16262, _VARIANT_16262]
            | Annotated[Structure16267, _VARIANT_16267]
            | Annotated[Structure16276, _VARIANT_16276]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture16294, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class VatsTargetable16303(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure16300(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/9:Destructible/0:Header/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path="SCRL/9:Destructible/0:Header/payload/0:Health",
            kind="primitive",
            name="Health",
        ),
        "dest_count": _base.Binding(
            path="SCRL/9:Destructible/0:Header/payload/1:DEST Count",
            kind="primitive",
            name="DEST Count",
        ),
        "vats_targetable": _base.Binding(
            path=("SCRL/9:Destructible/0:Header/payload/2:VATS Targetable"),
            kind="primitive",
            name="VATS Targetable",
        ),
        "unknown": _base.Binding(
            path="SCRL/9:Destructible/0:Header/payload/3:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    health: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    dest_count: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    vats_targetable: VatsTargetable16303
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["health"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["dest_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["vats_targetable"]
    ) -> _base.FieldRef[VatsTargetable16303]:
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


class Flags16312(enum.IntFlag):
    """Named values from the pinned schema."""

    CAP_DAMAGE = 1
    DISABLE = 2
    DESTROY = 4
    IGNORE_EXTERNAL_DMG = 8


class Structure16308(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
        "ion Stage Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/0:Health %"
            ),
            kind="primitive",
            name="Health %",
        ),
        "index": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/1:Index"
            ),
            kind="primitive",
            name="Index",
        ),
        "model_damage_stage_value": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/2:Model Damage Stage"
            ),
            kind="primitive",
            name="Model Damage Stage",
        ),
        "flags": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/3:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "self_damage_per_second": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/4:Self Damage per Second"
            ),
            kind="primitive",
            name="Self Damage per Second",
        ),
        "explosion": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/5:Explosion"
            ),
            kind="primitive",
            name="Explosion",
        ),
        "debris": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/6:Debris"
            ),
            kind="primitive",
            name="Debris",
        ),
        "debris_count": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/7:Debris Count"
            ),
            kind="primitive",
            name="Debris Count",
        ),
    }

    health: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    index: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    model_damage_stage_value: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    flags: Flags16312
    """Value decoded from this schema node."""

    self_damage_per_second: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    explosion: _values.FormId
    """Value decoded from this schema node."""

    debris: _values.FormId
    """Value decoded from this schema node."""

    debris_count: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["health"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_damage_stage_value"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags16312]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["self_damage_per_second"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explosion"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["debris"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["debris_count"]
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


class Structure16322(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16324": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/1:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16325": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16326": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_16324: bytes
    """Value decoded from this schema node."""

    unused_16325: bytes
    """Value decoded from this schema node."""

    unused_16326: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16324"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16325"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16326"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16322: _base.Variant = _base.Variant(
    path=(
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
)


class Structure16327(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_16330": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16331": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_16330: bytes
    """Value decoded from this schema node."""

    unused_16331: bytes
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
    def field(self, name: Literal["unused_16330"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16331"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16327: _base.Variant = _base.Variant(
    path=(
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
)


class Texture16335(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/2:Folder Hash"
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


class Structure16332(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_16339": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16340": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture16335, ...]
    """Value decoded from this schema node."""

    unused_16339: bytes
    """Value decoded from this schema node."""

    unused_16340: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture16335, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16339"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16340"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16332: _base.Variant = _base.Variant(
    path=(
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
)


class Texture16345(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/2:Folder Hash"
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


class Material16352(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/3:Mater"
        "ials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/2:Folder Hash"
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


class Structure16341(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/0:Heade"
                "rs"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/2:Addon"
                "s"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/4:Unkno"
                "wn"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture16345, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material16352, ...]
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
    ) -> _base.FieldRef[tuple[Texture16345, ...]]:
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
    ) -> _base.FieldRef[tuple[Material16352, ...]]:
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


_VARIANT_16341: _base.Variant = _base.Variant(
    path=(
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
)


class AlternateTexture16359(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
        "Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/2:3D Index"
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


class Model16317(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/0:"
                "Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure16322, _VARIANT_16322]
        | Annotated[Structure16327, _VARIANT_16327]
        | Annotated[Structure16332, _VARIANT_16332]
        | Annotated[Structure16341, _VARIANT_16341]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture16359, ...]] = None
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
            Annotated[Structure16322, _VARIANT_16322]
            | Annotated[Structure16327, _VARIANT_16327]
            | Annotated[Structure16332, _VARIANT_16332]
            | Annotated[Structure16341, _VARIANT_16341]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture16359, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Stage16306(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/9:Destructible/1:Stages/repeat/0:Stage"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "destruction_stage_data": _base.Binding(
            path=(
                "SCRL/9:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data"
            ),
            kind="subrecord",
            name="Destruction Stage Data",
        ),
        "model": _base.Binding(
            path=("SCRL/9:Destructible/1:Stages/repeat/0:Stage/1:Model"),
            kind="sequence",
            name="Model",
        ),
        "end_marker": _base.Binding(
            path=("SCRL/9:Destructible/1:Stages/repeat/0:Stage/2:End Marker"),
            kind="subrecord",
            name="End Marker",
        ),
    }

    destruction_stage_data: Optional[Structure16308] = None
    """Value decoded from this schema node."""

    model: Optional[Model16317] = None
    """Value decoded from this schema node."""

    end_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["destruction_stage_data"]
    ) -> _base.FieldRef[Optional[Structure16308]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model16317]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["end_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Destructible16298(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/9:Destructible"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="SCRL/9:Destructible/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "stages": _base.Binding(
            path="SCRL/9:Destructible/1:Stages",
            kind="repeat",
            name="Stages",
            repeated_path="SCRL/9:Destructible/1:Stages/repeat/0:Stage",
            child_kind="sequence",
        ),
    }

    header: Optional[Structure16300] = None
    """Value decoded from this schema node."""

    stages: tuple[Stage16306, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure16300]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stages"]
    ) -> _base.FieldRef[tuple[Stage16306, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure16370(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/12:Item/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value": _base.Binding(
            path="SCRL/12:Item/payload/0:Value",
            kind="primitive",
            name="Value",
        ),
        "weight": _base.Binding(
            path="SCRL/12:Item/payload/1:Weight",
            kind="primitive",
            name="Weight",
        ),
    }

    value: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    weight: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["weight"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags16376(enum.IntFlag):
    """Named values from the pinned schema."""

    MANUAL_COST_CALC = 1
    UNKNOWN_2 = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    UNKNOWN_8 = 128
    UNKNOWN_9 = 256
    UNKNOWN_10 = 512
    UNKNOWN_11 = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    UNKNOWN_14 = 8192
    UNKNOWN_15 = 16384
    UNKNOWN_16 = 32768
    UNKNOWN_17 = 65536
    PC_START_SPELL = 131072
    UNKNOWN_19 = 262144
    AREA_EFFECT_IGNORES_LOS = 524288
    IGNORE_RESISTANCE = 1048576
    NO_ABSORB_REFLECT = 2097152
    UNKNOWN_23 = 4194304
    NO_DUAL_CAST_MODIFICATION = 8388608
    UNKNOWN_25 = 16777216
    UNKNOWN_26 = 33554432
    UNKNOWN_27 = 67108864
    UNKNOWN_28 = 134217728
    UNKNOWN_29 = 268435456
    UNKNOWN_30 = 536870912
    UNKNOWN_31 = 1073741824
    UNKNOWN_32 = 2147483648


class Type16377(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SPELL = 0
    DISEASE = 1
    POWER = 2
    LESSER_POWER = 3
    ABILITY = 4
    POISON = 5
    UNKNOWN_6 = 6
    UNKNOWN_7 = 7
    UNKNOWN_8 = 8
    UNKNOWN_9 = 9
    ADDICTION = 10
    VOICE = 11


class CastType16379(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


class TargetType16380(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


class Structure16374(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/13:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "base_cost": _base.Binding(
            path="SCRL/13:Data/payload/0:Base Cost",
            kind="primitive",
            name="Base Cost",
        ),
        "flags": _base.Binding(
            path="SCRL/13:Data/payload/1:Flags",
            kind="primitive",
            name="Flags",
        ),
        "type": _base.Binding(
            path="SCRL/13:Data/payload/2:Type",
            kind="primitive",
            name="Type",
        ),
        "charge_time": _base.Binding(
            path="SCRL/13:Data/payload/3:Charge Time",
            kind="primitive",
            name="Charge Time",
        ),
        "cast_type": _base.Binding(
            path="SCRL/13:Data/payload/4:Cast Type",
            kind="primitive",
            name="Cast Type",
        ),
        "target_type": _base.Binding(
            path="SCRL/13:Data/payload/5:Target Type",
            kind="primitive",
            name="Target Type",
        ),
        "cast_duration": _base.Binding(
            path="SCRL/13:Data/payload/6:Cast Duration",
            kind="primitive",
            name="Cast Duration",
        ),
        "range": _base.Binding(
            path="SCRL/13:Data/payload/7:Range",
            kind="primitive",
            name="Range",
        ),
        "half_cost_perk": _base.Binding(
            path="SCRL/13:Data/payload/8:Half-cost Perk",
            kind="primitive",
            name="Half-cost Perk",
        ),
    }

    base_cost: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    flags: Flags16376
    """Value decoded from this schema node."""

    type: Type16377
    """Value decoded from this schema node."""

    charge_time: float
    """Value decoded from this schema node."""

    cast_type: CastType16379
    """Value decoded from this schema node."""

    target_type: TargetType16380
    """Value decoded from this schema node."""

    cast_duration: float
    """Value decoded from this schema node."""

    range: float
    """Value decoded from this schema node."""

    half_cost_perk: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["base_cost"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags16376]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type16377]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["charge_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cast_type"]
    ) -> _base.FieldRef[CastType16379]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_type"]
    ) -> _base.FieldRef[TargetType16380]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["cast_duration"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["range"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["half_cost_perk"]
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


class Structure16389(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/14:Effects/repeat/0:Effect/1:EFIT/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "magnitude": _base.Binding(
            path=("SCRL/14:Effects/repeat/0:Effect/1:EFIT/payload/0:Magnitude"),
            kind="primitive",
            name="Magnitude",
        ),
        "area": _base.Binding(
            path=("SCRL/14:Effects/repeat/0:Effect/1:EFIT/payload/1:Area"),
            kind="primitive",
            name="Area",
        ),
        "duration": _base.Binding(
            path=("SCRL/14:Effects/repeat/0:Effect/1:EFIT/payload/2:Duration"),
            kind="primitive",
            name="Duration",
        ),
    }

    magnitude: float
    """Value decoded from this schema node."""

    area: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    duration: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["magnitude"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["area"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["duration"]
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


_VARIANT_16400: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/2:Comparison Value/variants/0"
        ":Comparison Value - Float"
    )
)


_VARIANT_16401: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/2:Comparison Value/variants/1"
        ":Comparison Value - Global"
    )
)


_VARIANT_16405: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/0:Unk"
        "nown"
    )
)


_VARIANT_16406: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/1:Non"
        "e"
    )
)


_VARIANT_16407: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/2:Int"
        "eger"
    )
)


_VARIANT_16408: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/3:Flo"
        "at"
    )
)


_VARIANT_16409: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/4:Var"
        "iable Name"
    )
)


class Sex16410(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_16410: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/5:Sex"
    )
)


class ActorValue16411(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    AGGRESSION = 0
    CONFIDENCE = 1
    ENERGY = 2
    MORALITY = 3
    MOOD = 4
    ASSISTANCE = 5
    ONE_HANDED = 6
    TWO_HANDED = 7
    ARCHERY = 8
    BLOCK = 9
    SMITHING = 10
    HEAVY_ARMOR = 11
    LIGHT_ARMOR = 12
    PICKPOCKET = 13
    LOCKPICKING = 14
    SNEAK = 15
    ALCHEMY = 16
    SPEECH = 17
    ALTERATION = 18
    CONJURATION = 19
    DESTRUCTION = 20
    ILLUSION = 21
    RESTORATION = 22
    ENCHANTING = 23
    HEALTH = 24
    MAGICKA = 25
    STAMINA = 26
    HEAL_RATE = 27
    MAGICKA_RATE = 28
    STAMINA_RATE = 29
    SPEED_MULT = 30
    INVENTORY_WEIGHT = 31
    CARRY_WEIGHT = 32
    CRITICAL_CHANCE = 33
    MELEE_DAMAGE = 34
    UNARMED_DAMAGE = 35
    MASS = 36
    VOICE_POINTS = 37
    VOICE_RATE = 38
    DAMAGE_RESIST = 39
    POISON_RESIST = 40
    RESIST_FIRE = 41
    RESIST_SHOCK = 42
    RESIST_FROST = 43
    RESIST_MAGIC = 44
    RESIST_DISEASE = 45
    UNKNOWN_46 = 46
    UNKNOWN_47 = 47
    UNKNOWN_48 = 48
    UNKNOWN_49 = 49
    UNKNOWN_50 = 50
    UNKNOWN_51 = 51
    UNKNOWN_52 = 52
    PARALYSIS = 53
    INVISIBILITY = 54
    NIGHT_EYE = 55
    DETECT_LIFE_RANGE = 56
    WATER_BREATHING = 57
    WATER_WALKING = 58
    UNKNOWN_59 = 59
    FAME = 60
    INFAMY = 61
    JUMPING_BONUS = 62
    WARD_POWER = 63
    RIGHT_ITEM_CHARGE = 64
    ARMOR_PERKS = 65
    SHIELD_PERKS = 66
    WARD_DEFLECTION = 67
    VARIABLE01 = 68
    VARIABLE02 = 69
    VARIABLE03 = 70
    VARIABLE04 = 71
    VARIABLE05 = 72
    VARIABLE06 = 73
    VARIABLE07 = 74
    VARIABLE08 = 75
    VARIABLE09 = 76
    VARIABLE10 = 77
    BOW_SPEED_BONUS = 78
    FAVOR_ACTIVE = 79
    FAVORS_PER_DAY = 80
    FAVORS_PER_DAY_TIMER = 81
    LEFT_ITEM_CHARGE = 82
    ABSORB_CHANCE = 83
    BLINDNESS = 84
    WEAPON_SPEED_MULT = 85
    SHOUT_RECOVERY_MULT = 86
    BOW_STAGGER_BONUS = 87
    TELEKINESIS = 88
    FAVOR_POINTS_BONUS = 89
    LAST_BRIBED_INTIMIDATED = 90
    LAST_FLATTERED = 91
    MOVEMENT_NOISE_MULT = 92
    BYPASS_VENDOR_STOLEN_CHECK = 93
    BYPASS_VENDOR_KEYWORD_CHECK = 94
    WAITING_FOR_PLAYER = 95
    ONE_HANDED_MODIFIER = 96
    TWO_HANDED_MODIFIER = 97
    MARKSMAN_MODIFIER = 98
    BLOCK_MODIFIER = 99
    SMITHING_MODIFIER = 100
    HEAVY_ARMOR_MODIFIER = 101
    LIGHT_ARMOR_MODIFIER = 102
    PICKPOCKET_MODIFIER = 103
    LOCKPICKING_MODIFIER = 104
    SNEAKING_MODIFIER = 105
    ALCHEMY_MODIFIER = 106
    SPEECHCRAFT_MODIFIER = 107
    ALTERATION_MODIFIER = 108
    CONJURATION_MODIFIER = 109
    DESTRUCTION_MODIFIER = 110
    ILLUSION_MODIFIER = 111
    RESTORATION_MODIFIER = 112
    ENCHANTING_MODIFIER = 113
    ONE_HANDED_SKILL_ADVANCE = 114
    TWO_HANDED_SKILL_ADVANCE = 115
    MARKSMAN_SKILL_ADVANCE = 116
    BLOCK_SKILL_ADVANCE = 117
    SMITHING_SKILL_ADVANCE = 118
    HEAVY_ARMOR_SKILL_ADVANCE = 119
    LIGHT_ARMOR_SKILL_ADVANCE = 120
    PICKPOCKET_SKILL_ADVANCE = 121
    LOCKPICKING_SKILL_ADVANCE = 122
    SNEAKING_SKILL_ADVANCE = 123
    ALCHEMY_SKILL_ADVANCE = 124
    SPEECHCRAFT_SKILL_ADVANCE = 125
    ALTERATION_SKILL_ADVANCE = 126
    CONJURATION_SKILL_ADVANCE = 127
    DESTRUCTION_SKILL_ADVANCE = 128
    ILLUSION_SKILL_ADVANCE = 129
    RESTORATION_SKILL_ADVANCE = 130
    ENCHANTING_SKILL_ADVANCE = 131
    LEFT_WEAPON_SPEED_MULTIPLY = 132
    DRAGON_SOULS = 133
    COMBAT_HEALTH_REGEN_MULTIPLY = 134
    ONE_HANDED_POWER_MODIFIER = 135
    TWO_HANDED_POWER_MODIFIER = 136
    MARKSMAN_POWER_MODIFIER = 137
    BLOCK_POWER_MODIFIER = 138
    SMITHING_POWER_MODIFIER = 139
    HEAVY_ARMOR_POWER_MODIFIER = 140
    LIGHT_ARMOR_POWER_MODIFIER = 141
    PICKPOCKET_POWER_MODIFIER = 142
    LOCKPICKING_POWER_MODIFIER = 143
    SNEAKING_POWER_MODIFIER = 144
    ALCHEMY_POWER_MODIFIER = 145
    SPEECHCRAFT_POWER_MODIFIER = 146
    ALTERATION_POWER_MODIFIER = 147
    CONJURATION_POWER_MODIFIER = 148
    DESTRUCTION_POWER_MODIFIER = 149
    ILLUSION_POWER_MODIFIER = 150
    RESTORATION_POWER_MODIFIER = 151
    ENCHANTING_POWER_MODIFIER = 152
    DRAGON_REND = 153
    ATTACK_DAMAGE_MULT = 154
    HEAL_RATE_MULT = 155
    MAGICKA_RATE_MULT = 156
    STAMINA_RATE_MULT = 157
    WEREWOLF_PERKS = 158
    VAMPIRE_PERKS = 159
    GRAB_ACTOR_OFFSET = 160
    GRABBED = 161
    UNKNOWN_162 = 162
    REFLECT_DAMAGE = 163


_VARIANT_16411: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/6:Act"
        "or Value"
    )
)


class CrimeType16412(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_16412: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/7:Cri"
        "me Type"
    )
)


class Axis16413(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_16413: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/8:Axi"
        "s"
    )
)


_VARIANT_16414: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/9:Que"
        "st Stage (unused)"
    )
)


class MiscStat16415(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ARMOR_MADE = 37001190
    STORES_INVESTED_IN = 97801986
    QUESTS_COMPLETED = 226200342
    FAVORITE_WEAPON = 387732369
    POISONS_MIXED = 398870120
    EASTMARCH_BOUNTY = 439874358
    WEAPONS_IMPROVED = 490448964
    BRIBES = 494469227
    NECKS_BITTEN = 583191504
    CRITICAL_STRIKES = 584432184
    WEAPONS_MADE = 636611109
    DAYS_AS_A_VAMPIRE = 735757167
    WORDS_OF_POWER_UNLOCKED = 745422784
    BRAWLS_WON = 830376780
    LARGEST_BOUNTY = 891348752
    DAEDRIC_QUESTS_COMPLETED = 894973771
    BUNNIES_SLAUGHTERED = 906157711
    ARMOR_IMPROVED = 913147087
    DAWNGUARD_QUESTS_COMPLETED = 933717029
    WEREWOLF_TRANSFORMATIONS = 950197606
    DAYS_PASSED = 1013082768
    THE_PALE_BOUNTY = 1042709879
    CREATURES_KILLED = 1085349630
    UNDEAD_KILLED = 1104460815
    FAVORITE_SPELL = 1105033126
    POTIONS_MIXED = 1109974661
    WHITERUN_BOUNTY = 1110571599
    DRAGON_SOULS_COLLECTED = 1188494268
    PERSUASIONS = 1202160743
    INGREDIENTS_EATEN = 1203019797
    TRAINING_SESSIONS = 1277502353
    FINES_PAID = 1325669026
    THE_RIFT_BOUNTY = 1352810345
    TIMES_SHOUTED = 1353365043
    HJAALMARCH_BOUNTY = 1366050925
    FAVORITE_SHOUT = 1368112206
    HOUSES_OWNED = 1383987287
    THE_DARK_BROTHERHOOD_QUESTS_COMPLETED = 1387948235
    CHESTS_LOOTED = 1406790069
    NUM_VAMPIRE_PERKS = 1456274516
    AUTOMATIONS_KILLED = 1470102133
    GOLD_FOUND = 1472236023
    LOCKS_PICKED = 1479134254
    FALKREATH_BOUNTY = 1522772205
    SPELLS_LEARNED = 1590206234
    WEAPONS_DISARMED = 1638253993
    THIEVES_GUILD_QUESTS_COMPLETED = 1655892317
    JAIL_ESCAPES = 1713849931
    COLLEGE_OF_WINTERHOLD_QUESTS_COMPLETED = 1724695818
    CIVIL_WAR_QUESTS_COMPLETED = 1748769152
    THE_REACH_BOUNTY = 1773437303
    DAYS_AS_A_WEREWOLF = 1852327312
    MAULS = 1904714248
    SHOUTS_MASTERED = 1931170611
    NUM_WEREWOLF_PERKS = 1990305216
    TRESPASSES = 2062195755
    INTIMIDATIONS = 2100189120
    POISONS_USED = 2106535590
    MAIN_QUESTS_COMPLETED = 2124573741
    ITEMS_STOLEN = 2196869314
    DISEASES_CONTRACTED = 2237050248
    FAVORITE_SCHOOL = 2276536012
    MAGIC_ITEMS_MADE = 2282264953
    LOCATIONS_DISCOVERED = 2317680098
    ASSAULTS = 2384517065
    WINGS_PLUCKED = 2455132007
    FOOD_EATEN = 2467410475
    TIMES_JAILED = 2488068755
    WORDS_OF_POWER_LEARNED = 2493491132
    POTIONS_USED = 2519854097
    MISC_OBJECTIVES_COMPLETED = 2565756380
    TOTAL_LIFETIME_BOUNTY = 2579203800
    TRIBAL_ORCS_BOUNTY = 2792761076
    SOUL_GEMS_USED = 2806824579
    DAEDRA_KILLED = 2838534159
    DUNGEONS_CLEARED = 2856601237
    SKILL_BOOKS_READ = 2900652247
    HORSES_OWNED = 2963399470
    SIDE_QUESTS_COMPLETED = 2980988818
    STANDING_STONES_FOUND = 2991694662
    SNEAK_ATTACKS = 3042364498
    DAYS_JAILED = 3069253851
    BACKSTABS = 3115648805
    SHOUTS_LEARNED = 3141089694
    NIRNROOTS_FOUND = 3203124359
    ITEMS_PICKPOCKETED = 3256287925
    SOULS_TRAPPED = 3268010547
    WINTERHOLD_BOUNTY = 3355201933
    HOURS_WAITING = 3402820769
    BOOKS_READ = 3434697422
    INGREDIENTS_HARVESTED = 3464766294
    THE_COMPANIONS_QUESTS_COMPLETED = 3506335793
    HAAFINGAR_BOUNTY = 3524188751
    MURDERS = 3548145929
    QUESTLINES_COMPLETED = 3731649534
    HORSES_STOLEN = 3954062824
    BARTERS = 3983150834
    PEOPLE_KILLED = 4062871859
    POCKETS_PICKED = 4072325684
    SKILL_INCREASES = 4080087246
    VAMPIRISM_CURES = 4086456481
    SHOUTS_UNLOCKED = 4179744954
    HOURS_SLEPT = 4194451480
    MOST_GOLD_CARRIED = 4194706187
    ANIMALS_KILLED = 4242362385


_VARIANT_16415: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/10:Mi"
        "sc Stat"
    )
)


class Alignment16416(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_16416: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/11:Al"
        "ignment"
    )
)


_VARIANT_16417: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/12:Eq"
        "uip Type"
    )
)


class FormType16418(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ACTIVATOR = 0
    ARMOR = 1
    BOOK = 2
    CONTAINER = 3
    DOOR = 4
    INGREDIENT = 5
    LIGHT = 6
    MISC_ITEM = 7
    STATIC = 8
    GRASS = 9
    TREE = 10
    WEAPON = 12
    ACTOR = 13
    LEVELED_CHARACTER = 14
    SPELL = 15
    ENCHANTMENT = 16
    POTION = 17
    LEVELED_ITEM = 18
    KEY = 19
    AMMO = 20
    FLORA = 21
    FURNITURE = 22
    SOUND_MARKER = 23
    LAND_TEXTURE = 24
    COMBAT_STYLE = 25
    LOAD_SCREEN = 26
    LEVELED_SPELL = 27
    ANIM_OBJECT = 28
    WATER_TYPE = 29
    IDLE_MARKER = 30
    EFFECT_SHADER = 31
    PROJECTILE = 32
    TALKING_ACTIVATOR = 33
    EXPLOSION = 34
    TEXTURE_SET = 35
    DEBRIS = 36
    MENU_ICON = 37
    FORM_LIST = 38
    PERK = 39
    BODY_PART_DATA = 40
    ADD_ON_NODE = 41
    MOVABLE_STATIC = 42
    CAMERA_SHOT = 43
    IMPACT_DATA = 44
    IMPACT_DATA_SET = 45
    QUEST = 46
    PACKAGE = 47
    VOICE_TYPE = 48
    CLASS = 49
    RACE = 50
    EYES = 51
    HEAD_PART = 52
    FACTION = 53
    NOTE = 54
    WEATHER = 55
    CLIMATE = 56
    ARMOR_ADDON = 57
    GLOBAL = 58
    IMAGESPACE = 59
    IMAGESPACE_MODIFIER = 60
    ENCOUNTER_ZONE = 61
    MESSAGE = 62
    CONSTRUCTIBLE_OBJECT = 63
    ACOUSTIC_SPACE = 64
    RAGDOLL = 65
    SCRIPT = 66
    MAGIC_EFFECT = 67
    MUSIC_TYPE = 68
    STATIC_COLLECTION = 69
    KEYWORD = 70
    LOCATION = 71
    LOCATION_REF_TYPE = 72
    FOOTSTEP = 73
    FOOTSTEP_SET = 74
    MATERIAL_TYPE = 75
    ACTOR_ACTION = 76
    MUSIC_TRACK = 77
    WORD_OF_POWER = 78
    SHOUT = 79
    RELATIONSHIP = 80
    EQUIP_SLOT = 81
    ASSOCIATION_TYPE = 82
    OUTFIT = 83
    ART_OBJECT = 84
    MATERIAL_OBJECT = 85
    LIGHTING_TEMPLATE = 87
    SHADER_PARTICLE_GEOMETRY = 88
    VISUAL_EFFECT = 89
    APPARATUS = 90
    MOVEMENT_TYPE = 91
    HAZARD = 92
    SM_EVENT_NODE = 93
    SOUND_DESCRIPTOR = 94
    DUAL_CAST_DATA = 95
    SOUND_CATEGORY = 96
    SOUL_GEM = 97
    SOUND_OUTPUT_MODEL = 98
    COLLISION_LAYER = 99
    SCROLL = 100
    COLOR_FORM = 101
    REVERB_PARAMETERS = 102


_VARIANT_16418: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/13:Fo"
        "rm Type"
    )
)


class CriticalStage16419(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_16419: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/14:Cr"
        "itical Stage"
    )
)


_VARIANT_16420: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/15:Ob"
        "ject Reference"
    )
)


_VARIANT_16421: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/16:In"
        "ventory Object"
    )
)


_VARIANT_16422: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/17:Ac"
        "tor"
    )
)


_VARIANT_16423: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/18:Vo"
        "ice Type"
    )
)


_VARIANT_16424: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/19:Id"
        "le"
    )
)


_VARIANT_16425: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/20:Fo"
        "rm List"
    )
)


_VARIANT_16426: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/21:Qu"
        "est"
    )
)


_VARIANT_16427: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/22:Fa"
        "ction"
    )
)


_VARIANT_16428: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/23:Ce"
        "ll"
    )
)


_VARIANT_16429: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/24:Cl"
        "ass"
    )
)


_VARIANT_16430: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/25:Ra"
        "ce"
    )
)


_VARIANT_16431: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/26:Ac"
        "tor Base"
    )
)


_VARIANT_16432: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/27:Gl"
        "obal"
    )
)


_VARIANT_16433: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/28:We"
        "ather"
    )
)


_VARIANT_16434: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/29:Pa"
        "ckage"
    )
)


_VARIANT_16435: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/30:En"
        "counter Zone"
    )
)


_VARIANT_16436: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/31:Pe"
        "rk"
    )
)


_VARIANT_16437: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/32:Ow"
        "ner"
    )
)


_VARIANT_16438: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/33:Fu"
        "rniture"
    )
)


_VARIANT_16439: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/34:Ef"
        "fect Item"
    )
)


_VARIANT_16440: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/35:Ba"
        "se Effect"
    )
)


_VARIANT_16441: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/36:Wo"
        "rldspace"
    )
)


class VatsValueFunction16442(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    WEAPON_IS = 0
    WEAPON_IN_LIST = 1
    TARGET_IS = 2
    TARGET_IN_LIST = 3
    TARGET_DISTANCE = 4
    TARGET_PART = 5
    VATS_ACTION = 6
    IS_SUCCESS = 7
    IS_CRITICAL = 8
    CRITICAL_EFFECT_IS = 9
    CRITICAL_EFFECT_IN_LIST = 10
    IS_FATAL = 11
    EXPLODE_PART = 12
    DISMEMBER_PART = 13
    CRIPPLE_PART = 14
    WEAPON_TYPE_IS = 15
    IS_STRANGER = 16
    IS_PARALYZING_PALM = 17
    PROJECTILE_TYPE_IS = 18
    DELIVERY_TYPE_IS = 19
    CASTING_TYPE_IS = 20


_VARIANT_16442: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/37:VA"
        "TS Value Function"
    )
)


_VARIANT_16443: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/38:VA"
        "TS Value Param (INVALID)"
    )
)


_VARIANT_16444: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/39:Re"
        "ferenceable Object"
    )
)


_VARIANT_16445: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/40:Re"
        "gion"
    )
)


_VARIANT_16446: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/41:Ke"
        "yword"
    )
)


class PlayerAction16447(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_16447: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/42:Pl"
        "ayer Action"
    )
)


class CastingType16448(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_16448: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/43:Ca"
        "sting Type"
    )
)


_VARIANT_16449: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/44:Sh"
        "out"
    )
)


_VARIANT_16450: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/45:Lo"
        "cation"
    )
)


_VARIANT_16451: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/46:Lo"
        "cation Ref Type"
    )
)


_VARIANT_16452: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/47:Al"
        "ias"
    )
)


_VARIANT_16453: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/48:Pa"
        "ckdata ID"
    )
)


_VARIANT_16454: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/49:As"
        "sociation Type"
    )
)


class FurnitureAnim16455(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_16455: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/50:Fu"
        "rniture Anim"
    )
)


class FurnitureEntry16456(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_16456: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/51:Fu"
        "rniture Entry"
    )
)


_VARIANT_16457: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/52:Sc"
        "ene"
    )
)


class WardState16458(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_16458: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/53:Wa"
        "rd State"
    )
)


_VARIANT_16459: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/54:Ev"
        "ent"
    )
)


_VARIANT_16460: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/55:Ev"
        "ent Data"
    )
)


_VARIANT_16461: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/56:Kn"
        "owable"
    )
)


_VARIANT_16462: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/57:Fa"
        "ction"
    )
)


_VARIANT_16464: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/0:Unk"
        "nown"
    )
)


_VARIANT_16465: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/1:Non"
        "e"
    )
)


_VARIANT_16466: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/2:Int"
        "eger"
    )
)


_VARIANT_16467: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/3:Flo"
        "at"
    )
)


_VARIANT_16468: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/4:Var"
        "iable Name"
    )
)


class Sex16469(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_16469: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/5:Sex"
    )
)


class ActorValue16470(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    AGGRESSION = 0
    CONFIDENCE = 1
    ENERGY = 2
    MORALITY = 3
    MOOD = 4
    ASSISTANCE = 5
    ONE_HANDED = 6
    TWO_HANDED = 7
    ARCHERY = 8
    BLOCK = 9
    SMITHING = 10
    HEAVY_ARMOR = 11
    LIGHT_ARMOR = 12
    PICKPOCKET = 13
    LOCKPICKING = 14
    SNEAK = 15
    ALCHEMY = 16
    SPEECH = 17
    ALTERATION = 18
    CONJURATION = 19
    DESTRUCTION = 20
    ILLUSION = 21
    RESTORATION = 22
    ENCHANTING = 23
    HEALTH = 24
    MAGICKA = 25
    STAMINA = 26
    HEAL_RATE = 27
    MAGICKA_RATE = 28
    STAMINA_RATE = 29
    SPEED_MULT = 30
    INVENTORY_WEIGHT = 31
    CARRY_WEIGHT = 32
    CRITICAL_CHANCE = 33
    MELEE_DAMAGE = 34
    UNARMED_DAMAGE = 35
    MASS = 36
    VOICE_POINTS = 37
    VOICE_RATE = 38
    DAMAGE_RESIST = 39
    POISON_RESIST = 40
    RESIST_FIRE = 41
    RESIST_SHOCK = 42
    RESIST_FROST = 43
    RESIST_MAGIC = 44
    RESIST_DISEASE = 45
    UNKNOWN_46 = 46
    UNKNOWN_47 = 47
    UNKNOWN_48 = 48
    UNKNOWN_49 = 49
    UNKNOWN_50 = 50
    UNKNOWN_51 = 51
    UNKNOWN_52 = 52
    PARALYSIS = 53
    INVISIBILITY = 54
    NIGHT_EYE = 55
    DETECT_LIFE_RANGE = 56
    WATER_BREATHING = 57
    WATER_WALKING = 58
    UNKNOWN_59 = 59
    FAME = 60
    INFAMY = 61
    JUMPING_BONUS = 62
    WARD_POWER = 63
    RIGHT_ITEM_CHARGE = 64
    ARMOR_PERKS = 65
    SHIELD_PERKS = 66
    WARD_DEFLECTION = 67
    VARIABLE01 = 68
    VARIABLE02 = 69
    VARIABLE03 = 70
    VARIABLE04 = 71
    VARIABLE05 = 72
    VARIABLE06 = 73
    VARIABLE07 = 74
    VARIABLE08 = 75
    VARIABLE09 = 76
    VARIABLE10 = 77
    BOW_SPEED_BONUS = 78
    FAVOR_ACTIVE = 79
    FAVORS_PER_DAY = 80
    FAVORS_PER_DAY_TIMER = 81
    LEFT_ITEM_CHARGE = 82
    ABSORB_CHANCE = 83
    BLINDNESS = 84
    WEAPON_SPEED_MULT = 85
    SHOUT_RECOVERY_MULT = 86
    BOW_STAGGER_BONUS = 87
    TELEKINESIS = 88
    FAVOR_POINTS_BONUS = 89
    LAST_BRIBED_INTIMIDATED = 90
    LAST_FLATTERED = 91
    MOVEMENT_NOISE_MULT = 92
    BYPASS_VENDOR_STOLEN_CHECK = 93
    BYPASS_VENDOR_KEYWORD_CHECK = 94
    WAITING_FOR_PLAYER = 95
    ONE_HANDED_MODIFIER = 96
    TWO_HANDED_MODIFIER = 97
    MARKSMAN_MODIFIER = 98
    BLOCK_MODIFIER = 99
    SMITHING_MODIFIER = 100
    HEAVY_ARMOR_MODIFIER = 101
    LIGHT_ARMOR_MODIFIER = 102
    PICKPOCKET_MODIFIER = 103
    LOCKPICKING_MODIFIER = 104
    SNEAKING_MODIFIER = 105
    ALCHEMY_MODIFIER = 106
    SPEECHCRAFT_MODIFIER = 107
    ALTERATION_MODIFIER = 108
    CONJURATION_MODIFIER = 109
    DESTRUCTION_MODIFIER = 110
    ILLUSION_MODIFIER = 111
    RESTORATION_MODIFIER = 112
    ENCHANTING_MODIFIER = 113
    ONE_HANDED_SKILL_ADVANCE = 114
    TWO_HANDED_SKILL_ADVANCE = 115
    MARKSMAN_SKILL_ADVANCE = 116
    BLOCK_SKILL_ADVANCE = 117
    SMITHING_SKILL_ADVANCE = 118
    HEAVY_ARMOR_SKILL_ADVANCE = 119
    LIGHT_ARMOR_SKILL_ADVANCE = 120
    PICKPOCKET_SKILL_ADVANCE = 121
    LOCKPICKING_SKILL_ADVANCE = 122
    SNEAKING_SKILL_ADVANCE = 123
    ALCHEMY_SKILL_ADVANCE = 124
    SPEECHCRAFT_SKILL_ADVANCE = 125
    ALTERATION_SKILL_ADVANCE = 126
    CONJURATION_SKILL_ADVANCE = 127
    DESTRUCTION_SKILL_ADVANCE = 128
    ILLUSION_SKILL_ADVANCE = 129
    RESTORATION_SKILL_ADVANCE = 130
    ENCHANTING_SKILL_ADVANCE = 131
    LEFT_WEAPON_SPEED_MULTIPLY = 132
    DRAGON_SOULS = 133
    COMBAT_HEALTH_REGEN_MULTIPLY = 134
    ONE_HANDED_POWER_MODIFIER = 135
    TWO_HANDED_POWER_MODIFIER = 136
    MARKSMAN_POWER_MODIFIER = 137
    BLOCK_POWER_MODIFIER = 138
    SMITHING_POWER_MODIFIER = 139
    HEAVY_ARMOR_POWER_MODIFIER = 140
    LIGHT_ARMOR_POWER_MODIFIER = 141
    PICKPOCKET_POWER_MODIFIER = 142
    LOCKPICKING_POWER_MODIFIER = 143
    SNEAKING_POWER_MODIFIER = 144
    ALCHEMY_POWER_MODIFIER = 145
    SPEECHCRAFT_POWER_MODIFIER = 146
    ALTERATION_POWER_MODIFIER = 147
    CONJURATION_POWER_MODIFIER = 148
    DESTRUCTION_POWER_MODIFIER = 149
    ILLUSION_POWER_MODIFIER = 150
    RESTORATION_POWER_MODIFIER = 151
    ENCHANTING_POWER_MODIFIER = 152
    DRAGON_REND = 153
    ATTACK_DAMAGE_MULT = 154
    HEAL_RATE_MULT = 155
    MAGICKA_RATE_MULT = 156
    STAMINA_RATE_MULT = 157
    WEREWOLF_PERKS = 158
    VAMPIRE_PERKS = 159
    GRAB_ACTOR_OFFSET = 160
    GRABBED = 161
    UNKNOWN_162 = 162
    REFLECT_DAMAGE = 163


_VARIANT_16470: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/6:Act"
        "or Value"
    )
)


class CrimeType16471(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_16471: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/7:Cri"
        "me Type"
    )
)


class Axis16472(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_16472: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/8:Axi"
        "s"
    )
)


_VARIANT_16473: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/9:Que"
        "st Stage"
    )
)


class MiscStat16474(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ARMOR_MADE = 37001190
    STORES_INVESTED_IN = 97801986
    QUESTS_COMPLETED = 226200342
    FAVORITE_WEAPON = 387732369
    POISONS_MIXED = 398870120
    EASTMARCH_BOUNTY = 439874358
    WEAPONS_IMPROVED = 490448964
    BRIBES = 494469227
    NECKS_BITTEN = 583191504
    CRITICAL_STRIKES = 584432184
    WEAPONS_MADE = 636611109
    DAYS_AS_A_VAMPIRE = 735757167
    WORDS_OF_POWER_UNLOCKED = 745422784
    BRAWLS_WON = 830376780
    LARGEST_BOUNTY = 891348752
    DAEDRIC_QUESTS_COMPLETED = 894973771
    BUNNIES_SLAUGHTERED = 906157711
    ARMOR_IMPROVED = 913147087
    DAWNGUARD_QUESTS_COMPLETED = 933717029
    WEREWOLF_TRANSFORMATIONS = 950197606
    DAYS_PASSED = 1013082768
    THE_PALE_BOUNTY = 1042709879
    CREATURES_KILLED = 1085349630
    UNDEAD_KILLED = 1104460815
    FAVORITE_SPELL = 1105033126
    POTIONS_MIXED = 1109974661
    WHITERUN_BOUNTY = 1110571599
    DRAGON_SOULS_COLLECTED = 1188494268
    PERSUASIONS = 1202160743
    INGREDIENTS_EATEN = 1203019797
    TRAINING_SESSIONS = 1277502353
    FINES_PAID = 1325669026
    THE_RIFT_BOUNTY = 1352810345
    TIMES_SHOUTED = 1353365043
    HJAALMARCH_BOUNTY = 1366050925
    FAVORITE_SHOUT = 1368112206
    HOUSES_OWNED = 1383987287
    THE_DARK_BROTHERHOOD_QUESTS_COMPLETED = 1387948235
    CHESTS_LOOTED = 1406790069
    NUM_VAMPIRE_PERKS = 1456274516
    AUTOMATIONS_KILLED = 1470102133
    GOLD_FOUND = 1472236023
    LOCKS_PICKED = 1479134254
    FALKREATH_BOUNTY = 1522772205
    SPELLS_LEARNED = 1590206234
    WEAPONS_DISARMED = 1638253993
    THIEVES_GUILD_QUESTS_COMPLETED = 1655892317
    JAIL_ESCAPES = 1713849931
    COLLEGE_OF_WINTERHOLD_QUESTS_COMPLETED = 1724695818
    CIVIL_WAR_QUESTS_COMPLETED = 1748769152
    THE_REACH_BOUNTY = 1773437303
    DAYS_AS_A_WEREWOLF = 1852327312
    MAULS = 1904714248
    SHOUTS_MASTERED = 1931170611
    NUM_WEREWOLF_PERKS = 1990305216
    TRESPASSES = 2062195755
    INTIMIDATIONS = 2100189120
    POISONS_USED = 2106535590
    MAIN_QUESTS_COMPLETED = 2124573741
    ITEMS_STOLEN = 2196869314
    DISEASES_CONTRACTED = 2237050248
    FAVORITE_SCHOOL = 2276536012
    MAGIC_ITEMS_MADE = 2282264953
    LOCATIONS_DISCOVERED = 2317680098
    ASSAULTS = 2384517065
    WINGS_PLUCKED = 2455132007
    FOOD_EATEN = 2467410475
    TIMES_JAILED = 2488068755
    WORDS_OF_POWER_LEARNED = 2493491132
    POTIONS_USED = 2519854097
    MISC_OBJECTIVES_COMPLETED = 2565756380
    TOTAL_LIFETIME_BOUNTY = 2579203800
    TRIBAL_ORCS_BOUNTY = 2792761076
    SOUL_GEMS_USED = 2806824579
    DAEDRA_KILLED = 2838534159
    DUNGEONS_CLEARED = 2856601237
    SKILL_BOOKS_READ = 2900652247
    HORSES_OWNED = 2963399470
    SIDE_QUESTS_COMPLETED = 2980988818
    STANDING_STONES_FOUND = 2991694662
    SNEAK_ATTACKS = 3042364498
    DAYS_JAILED = 3069253851
    BACKSTABS = 3115648805
    SHOUTS_LEARNED = 3141089694
    NIRNROOTS_FOUND = 3203124359
    ITEMS_PICKPOCKETED = 3256287925
    SOULS_TRAPPED = 3268010547
    WINTERHOLD_BOUNTY = 3355201933
    HOURS_WAITING = 3402820769
    BOOKS_READ = 3434697422
    INGREDIENTS_HARVESTED = 3464766294
    THE_COMPANIONS_QUESTS_COMPLETED = 3506335793
    HAAFINGAR_BOUNTY = 3524188751
    MURDERS = 3548145929
    QUESTLINES_COMPLETED = 3731649534
    HORSES_STOLEN = 3954062824
    BARTERS = 3983150834
    PEOPLE_KILLED = 4062871859
    POCKETS_PICKED = 4072325684
    SKILL_INCREASES = 4080087246
    VAMPIRISM_CURES = 4086456481
    SHOUTS_UNLOCKED = 4179744954
    HOURS_SLEPT = 4194451480
    MOST_GOLD_CARRIED = 4194706187
    ANIMALS_KILLED = 4242362385


_VARIANT_16474: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/10:Mi"
        "sc Stat"
    )
)


class Alignment16475(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_16475: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/11:Al"
        "ignment"
    )
)


_VARIANT_16476: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/12:Eq"
        "uip Type"
    )
)


class FormType16477(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ACTIVATOR = 0
    ARMOR = 1
    BOOK = 2
    CONTAINER = 3
    DOOR = 4
    INGREDIENT = 5
    LIGHT = 6
    MISC_ITEM = 7
    STATIC = 8
    GRASS = 9
    TREE = 10
    WEAPON = 12
    ACTOR = 13
    LEVELED_CHARACTER = 14
    SPELL = 15
    ENCHANTMENT = 16
    POTION = 17
    LEVELED_ITEM = 18
    KEY = 19
    AMMO = 20
    FLORA = 21
    FURNITURE = 22
    SOUND_MARKER = 23
    LAND_TEXTURE = 24
    COMBAT_STYLE = 25
    LOAD_SCREEN = 26
    LEVELED_SPELL = 27
    ANIM_OBJECT = 28
    WATER_TYPE = 29
    IDLE_MARKER = 30
    EFFECT_SHADER = 31
    PROJECTILE = 32
    TALKING_ACTIVATOR = 33
    EXPLOSION = 34
    TEXTURE_SET = 35
    DEBRIS = 36
    MENU_ICON = 37
    FORM_LIST = 38
    PERK = 39
    BODY_PART_DATA = 40
    ADD_ON_NODE = 41
    MOVABLE_STATIC = 42
    CAMERA_SHOT = 43
    IMPACT_DATA = 44
    IMPACT_DATA_SET = 45
    QUEST = 46
    PACKAGE = 47
    VOICE_TYPE = 48
    CLASS = 49
    RACE = 50
    EYES = 51
    HEAD_PART = 52
    FACTION = 53
    NOTE = 54
    WEATHER = 55
    CLIMATE = 56
    ARMOR_ADDON = 57
    GLOBAL = 58
    IMAGESPACE = 59
    IMAGESPACE_MODIFIER = 60
    ENCOUNTER_ZONE = 61
    MESSAGE = 62
    CONSTRUCTIBLE_OBJECT = 63
    ACOUSTIC_SPACE = 64
    RAGDOLL = 65
    SCRIPT = 66
    MAGIC_EFFECT = 67
    MUSIC_TYPE = 68
    STATIC_COLLECTION = 69
    KEYWORD = 70
    LOCATION = 71
    LOCATION_REF_TYPE = 72
    FOOTSTEP = 73
    FOOTSTEP_SET = 74
    MATERIAL_TYPE = 75
    ACTOR_ACTION = 76
    MUSIC_TRACK = 77
    WORD_OF_POWER = 78
    SHOUT = 79
    RELATIONSHIP = 80
    EQUIP_SLOT = 81
    ASSOCIATION_TYPE = 82
    OUTFIT = 83
    ART_OBJECT = 84
    MATERIAL_OBJECT = 85
    LIGHTING_TEMPLATE = 87
    SHADER_PARTICLE_GEOMETRY = 88
    VISUAL_EFFECT = 89
    APPARATUS = 90
    MOVEMENT_TYPE = 91
    HAZARD = 92
    SM_EVENT_NODE = 93
    SOUND_DESCRIPTOR = 94
    DUAL_CAST_DATA = 95
    SOUND_CATEGORY = 96
    SOUL_GEM = 97
    SOUND_OUTPUT_MODEL = 98
    COLLISION_LAYER = 99
    SCROLL = 100
    COLOR_FORM = 101
    REVERB_PARAMETERS = 102


_VARIANT_16477: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/13:Fo"
        "rm Type"
    )
)


class CriticalStage16478(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_16478: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/14:Cr"
        "itical Stage"
    )
)


_VARIANT_16479: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/15:Ob"
        "ject Reference"
    )
)


_VARIANT_16480: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/16:In"
        "ventory Object"
    )
)


_VARIANT_16481: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/17:Ac"
        "tor"
    )
)


_VARIANT_16482: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/18:Vo"
        "ice Type"
    )
)


_VARIANT_16483: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/19:Id"
        "le"
    )
)


_VARIANT_16484: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/20:Fo"
        "rm List"
    )
)


_VARIANT_16485: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/21:Qu"
        "est"
    )
)


_VARIANT_16486: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/22:Fa"
        "ction"
    )
)


_VARIANT_16487: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/23:Ce"
        "ll"
    )
)


_VARIANT_16488: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/24:Cl"
        "ass"
    )
)


_VARIANT_16489: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/25:Ra"
        "ce"
    )
)


_VARIANT_16490: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/26:Ac"
        "tor Base"
    )
)


_VARIANT_16491: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/27:Gl"
        "obal"
    )
)


_VARIANT_16492: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/28:We"
        "ather"
    )
)


_VARIANT_16493: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/29:Pa"
        "ckage"
    )
)


_VARIANT_16494: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/30:En"
        "counter Zone"
    )
)


_VARIANT_16495: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/31:Pe"
        "rk"
    )
)


_VARIANT_16496: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/32:Ow"
        "ner"
    )
)


_VARIANT_16497: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/33:Fu"
        "rniture"
    )
)


_VARIANT_16498: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/34:Ef"
        "fect Item"
    )
)


_VARIANT_16499: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/35:Ba"
        "se Effect"
    )
)


_VARIANT_16500: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/36:Wo"
        "rldspace"
    )
)


class VatsValueFunction16501(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    WEAPON_IS = 0
    WEAPON_IN_LIST = 1
    TARGET_IS = 2
    TARGET_IN_LIST = 3
    TARGET_DISTANCE = 4
    TARGET_PART = 5
    VATS_ACTION = 6
    IS_SUCCESS = 7
    IS_CRITICAL = 8
    CRITICAL_EFFECT_IS = 9
    CRITICAL_EFFECT_IN_LIST = 10
    IS_FATAL = 11
    EXPLODE_PART = 12
    DISMEMBER_PART = 13
    CRIPPLE_PART = 14
    WEAPON_TYPE_IS = 15
    IS_STRANGER = 16
    IS_PARALYZING_PALM = 17
    PROJECTILE_TYPE_IS = 18
    DELIVERY_TYPE_IS = 19
    CASTING_TYPE_IS = 20


_VARIANT_16501: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/37:VA"
        "TS Value Function"
    )
)


_VARIANT_16503: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/0:Weapon"
    )
)


_VARIANT_16504: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/1:Weapon List"
    )
)


_VARIANT_16505: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/2:Target"
    )
)


_VARIANT_16506: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/3:Target List"
    )
)


_VARIANT_16507: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/4:Unknown"
    )
)


class TargetPart16508(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    AGGRESSION = 0
    CONFIDENCE = 1
    ENERGY = 2
    MORALITY = 3
    MOOD = 4
    ASSISTANCE = 5
    ONE_HANDED = 6
    TWO_HANDED = 7
    ARCHERY = 8
    BLOCK = 9
    SMITHING = 10
    HEAVY_ARMOR = 11
    LIGHT_ARMOR = 12
    PICKPOCKET = 13
    LOCKPICKING = 14
    SNEAK = 15
    ALCHEMY = 16
    SPEECH = 17
    ALTERATION = 18
    CONJURATION = 19
    DESTRUCTION = 20
    ILLUSION = 21
    RESTORATION = 22
    ENCHANTING = 23
    HEALTH = 24
    MAGICKA = 25
    STAMINA = 26
    HEAL_RATE = 27
    MAGICKA_RATE = 28
    STAMINA_RATE = 29
    SPEED_MULT = 30
    INVENTORY_WEIGHT = 31
    CARRY_WEIGHT = 32
    CRITICAL_CHANCE = 33
    MELEE_DAMAGE = 34
    UNARMED_DAMAGE = 35
    MASS = 36
    VOICE_POINTS = 37
    VOICE_RATE = 38
    DAMAGE_RESIST = 39
    POISON_RESIST = 40
    RESIST_FIRE = 41
    RESIST_SHOCK = 42
    RESIST_FROST = 43
    RESIST_MAGIC = 44
    RESIST_DISEASE = 45
    UNKNOWN_46 = 46
    UNKNOWN_47 = 47
    UNKNOWN_48 = 48
    UNKNOWN_49 = 49
    UNKNOWN_50 = 50
    UNKNOWN_51 = 51
    UNKNOWN_52 = 52
    PARALYSIS = 53
    INVISIBILITY = 54
    NIGHT_EYE = 55
    DETECT_LIFE_RANGE = 56
    WATER_BREATHING = 57
    WATER_WALKING = 58
    UNKNOWN_59 = 59
    FAME = 60
    INFAMY = 61
    JUMPING_BONUS = 62
    WARD_POWER = 63
    RIGHT_ITEM_CHARGE = 64
    ARMOR_PERKS = 65
    SHIELD_PERKS = 66
    WARD_DEFLECTION = 67
    VARIABLE01 = 68
    VARIABLE02 = 69
    VARIABLE03 = 70
    VARIABLE04 = 71
    VARIABLE05 = 72
    VARIABLE06 = 73
    VARIABLE07 = 74
    VARIABLE08 = 75
    VARIABLE09 = 76
    VARIABLE10 = 77
    BOW_SPEED_BONUS = 78
    FAVOR_ACTIVE = 79
    FAVORS_PER_DAY = 80
    FAVORS_PER_DAY_TIMER = 81
    LEFT_ITEM_CHARGE = 82
    ABSORB_CHANCE = 83
    BLINDNESS = 84
    WEAPON_SPEED_MULT = 85
    SHOUT_RECOVERY_MULT = 86
    BOW_STAGGER_BONUS = 87
    TELEKINESIS = 88
    FAVOR_POINTS_BONUS = 89
    LAST_BRIBED_INTIMIDATED = 90
    LAST_FLATTERED = 91
    MOVEMENT_NOISE_MULT = 92
    BYPASS_VENDOR_STOLEN_CHECK = 93
    BYPASS_VENDOR_KEYWORD_CHECK = 94
    WAITING_FOR_PLAYER = 95
    ONE_HANDED_MODIFIER = 96
    TWO_HANDED_MODIFIER = 97
    MARKSMAN_MODIFIER = 98
    BLOCK_MODIFIER = 99
    SMITHING_MODIFIER = 100
    HEAVY_ARMOR_MODIFIER = 101
    LIGHT_ARMOR_MODIFIER = 102
    PICKPOCKET_MODIFIER = 103
    LOCKPICKING_MODIFIER = 104
    SNEAKING_MODIFIER = 105
    ALCHEMY_MODIFIER = 106
    SPEECHCRAFT_MODIFIER = 107
    ALTERATION_MODIFIER = 108
    CONJURATION_MODIFIER = 109
    DESTRUCTION_MODIFIER = 110
    ILLUSION_MODIFIER = 111
    RESTORATION_MODIFIER = 112
    ENCHANTING_MODIFIER = 113
    ONE_HANDED_SKILL_ADVANCE = 114
    TWO_HANDED_SKILL_ADVANCE = 115
    MARKSMAN_SKILL_ADVANCE = 116
    BLOCK_SKILL_ADVANCE = 117
    SMITHING_SKILL_ADVANCE = 118
    HEAVY_ARMOR_SKILL_ADVANCE = 119
    LIGHT_ARMOR_SKILL_ADVANCE = 120
    PICKPOCKET_SKILL_ADVANCE = 121
    LOCKPICKING_SKILL_ADVANCE = 122
    SNEAKING_SKILL_ADVANCE = 123
    ALCHEMY_SKILL_ADVANCE = 124
    SPEECHCRAFT_SKILL_ADVANCE = 125
    ALTERATION_SKILL_ADVANCE = 126
    CONJURATION_SKILL_ADVANCE = 127
    DESTRUCTION_SKILL_ADVANCE = 128
    ILLUSION_SKILL_ADVANCE = 129
    RESTORATION_SKILL_ADVANCE = 130
    ENCHANTING_SKILL_ADVANCE = 131
    LEFT_WEAPON_SPEED_MULTIPLY = 132
    DRAGON_SOULS = 133
    COMBAT_HEALTH_REGEN_MULTIPLY = 134
    ONE_HANDED_POWER_MODIFIER = 135
    TWO_HANDED_POWER_MODIFIER = 136
    MARKSMAN_POWER_MODIFIER = 137
    BLOCK_POWER_MODIFIER = 138
    SMITHING_POWER_MODIFIER = 139
    HEAVY_ARMOR_POWER_MODIFIER = 140
    LIGHT_ARMOR_POWER_MODIFIER = 141
    PICKPOCKET_POWER_MODIFIER = 142
    LOCKPICKING_POWER_MODIFIER = 143
    SNEAKING_POWER_MODIFIER = 144
    ALCHEMY_POWER_MODIFIER = 145
    SPEECHCRAFT_POWER_MODIFIER = 146
    ALTERATION_POWER_MODIFIER = 147
    CONJURATION_POWER_MODIFIER = 148
    DESTRUCTION_POWER_MODIFIER = 149
    ILLUSION_POWER_MODIFIER = 150
    RESTORATION_POWER_MODIFIER = 151
    ENCHANTING_POWER_MODIFIER = 152
    DRAGON_REND = 153
    ATTACK_DAMAGE_MULT = 154
    HEAL_RATE_MULT = 155
    MAGICKA_RATE_MULT = 156
    STAMINA_RATE_MULT = 157
    WEREWOLF_PERKS = 158
    VAMPIRE_PERKS = 159
    GRAB_ACTOR_OFFSET = 160
    GRABBED = 161
    UNKNOWN_162 = 162
    REFLECT_DAMAGE = 163


_VARIANT_16508: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/5:Target Part"
    )
)


class VatsAction16509(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    UNARMED_ATTACK = 0
    ONE_HAND_MELEE_ATTACK = 1
    TWO_HAND_MELEE_ATTACK = 2
    MAGIC_ATTACK = 3
    RANGED_ATTACK = 4
    RELOAD = 5
    CROUCH = 6
    STAND = 7
    SWITCH_WEAPON = 8
    TOGGLE_WEAPON_DRAWN = 9
    HEAL = 10
    PLAYER_DEATH = 11


_VARIANT_16509: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/6:VATS Action"
    )
)


_VARIANT_16510: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/7:Unknown"
    )
)


_VARIANT_16511: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/8:Unknown"
    )
)


_VARIANT_16512: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/9:Critical Effect"
    )
)


_VARIANT_16513: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/10:Critical Effect List"
    )
)


_VARIANT_16514: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/11:Unknown"
    )
)


_VARIANT_16515: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/12:Unknown"
    )
)


_VARIANT_16516: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/13:Unknown"
    )
)


_VARIANT_16517: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/14:Unknown"
    )
)


class WeaponType16518(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    HAND_TO_HAND_MELEE = 0
    ONE_HAND_SWORD = 1
    ONE_HAND_DAGGER = 2
    ONE_HAND_AXE = 3
    ONE_HAND_MACE = 4
    TWO_HAND_SWORD = 5
    TWO_HAND_AXE = 6
    BOW = 7
    STAFF = 8
    CROSSBOW = 9


_VARIANT_16518: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_16519: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/16:Unknown"
    )
)


_VARIANT_16520: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/17:Unknown"
    )
)


class ProjectileType16521(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_16521: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/18:Projectile Type"
    )
)


class DeliveryType16522(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_16522: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/19:Delivery Type"
    )
)


class CastingType16523(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_16523: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/20:Casting Type"
    )
)


_VARIANT_16502: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param"
    )
)


_VARIANT_16524: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/39:Re"
        "ferenceable Object"
    )
)


_VARIANT_16525: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/40:Re"
        "gion"
    )
)


_VARIANT_16526: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/41:Ke"
        "yword"
    )
)


class PlayerAction16527(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_16527: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/42:Pl"
        "ayer Action"
    )
)


class CastingType16528(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_16528: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/43:Ca"
        "sting Type"
    )
)


_VARIANT_16529: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/44:Sh"
        "out"
    )
)


_VARIANT_16530: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/45:Lo"
        "cation"
    )
)


_VARIANT_16531: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/46:Lo"
        "cation Ref Type"
    )
)


_VARIANT_16532: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/47:Al"
        "ias"
    )
)


_VARIANT_16533: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/48:Pa"
        "ckdata ID"
    )
)


_VARIANT_16534: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/49:As"
        "sociation Type"
    )
)


class FurnitureAnim16535(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_16535: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/50:Fu"
        "rniture Anim"
    )
)


class FurnitureEntry16536(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_16536: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/51:Fu"
        "rniture Entry"
    )
)


_VARIANT_16537: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/52:Sc"
        "ene"
    )
)


class WardState16538(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_16538: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/53:Wa"
        "rd State"
    )
)


_VARIANT_16539: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/54:Ev"
        "ent"
    )
)


_VARIANT_16540: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/55:Ev"
        "ent Data"
    )
)


_VARIANT_16541: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/56:Kn"
        "owable"
    )
)


_VARIANT_16542: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/57:Fa"
        "ction"
    )
)


class RunOn16543(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_16545: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/8:Reference/variants/0:Unused"
    )
)


_VARIANT_16546: _base.Variant = _base.Variant(
    path=(
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/8:Reference/variants/1:Refere"
        "nce"
    )
)


class Structure16396(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_16403": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/9:Parameter #3"
            ),
            kind="primitive",
            name="Parameter #3",
        ),
    }

    type: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    comparison_value: (
        Annotated[float, _VARIANT_16400]
        | Annotated[_values.FormId, _VARIANT_16401]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_16403: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_16405]
        | Annotated[bytes, _VARIANT_16406]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16407,
        ]
        | Annotated[float, _VARIANT_16408]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16409,
        ]
        | Annotated[Sex16410, _VARIANT_16410]
        | Annotated[ActorValue16411, _VARIANT_16411]
        | Annotated[CrimeType16412, _VARIANT_16412]
        | Annotated[Axis16413, _VARIANT_16413]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16414,
        ]
        | Annotated[MiscStat16415, _VARIANT_16415]
        | Annotated[Alignment16416, _VARIANT_16416]
        | Annotated[_values.FormId, _VARIANT_16417]
        | Annotated[FormType16418, _VARIANT_16418]
        | Annotated[CriticalStage16419, _VARIANT_16419]
        | Annotated[_values.FormId, _VARIANT_16420]
        | Annotated[_values.FormId, _VARIANT_16421]
        | Annotated[_values.FormId, _VARIANT_16422]
        | Annotated[_values.FormId, _VARIANT_16423]
        | Annotated[_values.FormId, _VARIANT_16424]
        | Annotated[_values.FormId, _VARIANT_16425]
        | Annotated[_values.FormId, _VARIANT_16426]
        | Annotated[_values.FormId, _VARIANT_16427]
        | Annotated[_values.FormId, _VARIANT_16428]
        | Annotated[_values.FormId, _VARIANT_16429]
        | Annotated[_values.FormId, _VARIANT_16430]
        | Annotated[_values.FormId, _VARIANT_16431]
        | Annotated[_values.FormId, _VARIANT_16432]
        | Annotated[_values.FormId, _VARIANT_16433]
        | Annotated[_values.FormId, _VARIANT_16434]
        | Annotated[_values.FormId, _VARIANT_16435]
        | Annotated[_values.FormId, _VARIANT_16436]
        | Annotated[_values.FormId, _VARIANT_16437]
        | Annotated[_values.FormId, _VARIANT_16438]
        | Annotated[_values.FormId, _VARIANT_16439]
        | Annotated[_values.FormId, _VARIANT_16440]
        | Annotated[_values.FormId, _VARIANT_16441]
        | Annotated[VatsValueFunction16442, _VARIANT_16442]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16443,
        ]
        | Annotated[_values.FormId, _VARIANT_16444]
        | Annotated[_values.FormId, _VARIANT_16445]
        | Annotated[_values.FormId, _VARIANT_16446]
        | Annotated[PlayerAction16447, _VARIANT_16447]
        | Annotated[CastingType16448, _VARIANT_16448]
        | Annotated[_values.FormId, _VARIANT_16449]
        | Annotated[_values.FormId, _VARIANT_16450]
        | Annotated[_values.FormId, _VARIANT_16451]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16452,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16453,
        ]
        | Annotated[_values.FormId, _VARIANT_16454]
        | Annotated[FurnitureAnim16455, _VARIANT_16455]
        | Annotated[FurnitureEntry16456, _VARIANT_16456]
        | Annotated[_values.FormId, _VARIANT_16457]
        | Annotated[WardState16458, _VARIANT_16458]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16459,
        ]
        | Annotated[_values.FormId, _VARIANT_16460]
        | Annotated[_values.FormId, _VARIANT_16461]
        | Annotated[_values.FormId, _VARIANT_16462]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_16464]
        | Annotated[bytes, _VARIANT_16465]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16466,
        ]
        | Annotated[float, _VARIANT_16467]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16468,
        ]
        | Annotated[Sex16469, _VARIANT_16469]
        | Annotated[ActorValue16470, _VARIANT_16470]
        | Annotated[CrimeType16471, _VARIANT_16471]
        | Annotated[Axis16472, _VARIANT_16472]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16473,
        ]
        | Annotated[MiscStat16474, _VARIANT_16474]
        | Annotated[Alignment16475, _VARIANT_16475]
        | Annotated[_values.FormId, _VARIANT_16476]
        | Annotated[FormType16477, _VARIANT_16477]
        | Annotated[CriticalStage16478, _VARIANT_16478]
        | Annotated[_values.FormId, _VARIANT_16479]
        | Annotated[_values.FormId, _VARIANT_16480]
        | Annotated[_values.FormId, _VARIANT_16481]
        | Annotated[_values.FormId, _VARIANT_16482]
        | Annotated[_values.FormId, _VARIANT_16483]
        | Annotated[_values.FormId, _VARIANT_16484]
        | Annotated[_values.FormId, _VARIANT_16485]
        | Annotated[_values.FormId, _VARIANT_16486]
        | Annotated[_values.FormId, _VARIANT_16487]
        | Annotated[_values.FormId, _VARIANT_16488]
        | Annotated[_values.FormId, _VARIANT_16489]
        | Annotated[_values.FormId, _VARIANT_16490]
        | Annotated[_values.FormId, _VARIANT_16491]
        | Annotated[_values.FormId, _VARIANT_16492]
        | Annotated[_values.FormId, _VARIANT_16493]
        | Annotated[_values.FormId, _VARIANT_16494]
        | Annotated[_values.FormId, _VARIANT_16495]
        | Annotated[_values.FormId, _VARIANT_16496]
        | Annotated[_values.FormId, _VARIANT_16497]
        | Annotated[_values.FormId, _VARIANT_16498]
        | Annotated[_values.FormId, _VARIANT_16499]
        | Annotated[_values.FormId, _VARIANT_16500]
        | Annotated[VatsValueFunction16501, _VARIANT_16501]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_16503]
            | Annotated[_values.FormId, _VARIANT_16504]
            | Annotated[_values.FormId, _VARIANT_16505]
            | Annotated[_values.FormId, _VARIANT_16506]
            | Annotated[bytes, _VARIANT_16507]
            | Annotated[TargetPart16508, _VARIANT_16508]
            | Annotated[VatsAction16509, _VARIANT_16509]
            | Annotated[bytes, _VARIANT_16510]
            | Annotated[bytes, _VARIANT_16511]
            | Annotated[_values.FormId, _VARIANT_16512]
            | Annotated[_values.FormId, _VARIANT_16513]
            | Annotated[bytes, _VARIANT_16514]
            | Annotated[bytes, _VARIANT_16515]
            | Annotated[bytes, _VARIANT_16516]
            | Annotated[bytes, _VARIANT_16517]
            | Annotated[WeaponType16518, _VARIANT_16518]
            | Annotated[bytes, _VARIANT_16519]
            | Annotated[bytes, _VARIANT_16520]
            | Annotated[ProjectileType16521, _VARIANT_16521]
            | Annotated[DeliveryType16522, _VARIANT_16522]
            | Annotated[CastingType16523, _VARIANT_16523],
            _VARIANT_16502,
        ]
        | Annotated[_values.FormId, _VARIANT_16524]
        | Annotated[_values.FormId, _VARIANT_16525]
        | Annotated[_values.FormId, _VARIANT_16526]
        | Annotated[PlayerAction16527, _VARIANT_16527]
        | Annotated[CastingType16528, _VARIANT_16528]
        | Annotated[_values.FormId, _VARIANT_16529]
        | Annotated[_values.FormId, _VARIANT_16530]
        | Annotated[_values.FormId, _VARIANT_16531]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16532,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16533,
        ]
        | Annotated[_values.FormId, _VARIANT_16534]
        | Annotated[FurnitureAnim16535, _VARIANT_16535]
        | Annotated[FurnitureEntry16536, _VARIANT_16536]
        | Annotated[_values.FormId, _VARIANT_16537]
        | Annotated[WardState16538, _VARIANT_16538]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16539,
        ]
        | Annotated[_values.FormId, _VARIANT_16540]
        | Annotated[_values.FormId, _VARIANT_16541]
        | Annotated[_values.FormId, _VARIANT_16542]
    )
    """Value decoded from this schema node."""

    run_on: RunOn16543
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16545,
        ]
        | Annotated[_values.FormId, _VARIANT_16546]
    )
    """Value decoded from this schema node."""

    parameter_3: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["type"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["comparison_value"]
    ) -> _base.FieldRef[
        Annotated[float, _VARIANT_16400]
        | Annotated[_values.FormId, _VARIANT_16401]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["function"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16403"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_16405]
        | Annotated[bytes, _VARIANT_16406]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16407,
        ]
        | Annotated[float, _VARIANT_16408]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16409,
        ]
        | Annotated[Sex16410, _VARIANT_16410]
        | Annotated[ActorValue16411, _VARIANT_16411]
        | Annotated[CrimeType16412, _VARIANT_16412]
        | Annotated[Axis16413, _VARIANT_16413]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16414,
        ]
        | Annotated[MiscStat16415, _VARIANT_16415]
        | Annotated[Alignment16416, _VARIANT_16416]
        | Annotated[_values.FormId, _VARIANT_16417]
        | Annotated[FormType16418, _VARIANT_16418]
        | Annotated[CriticalStage16419, _VARIANT_16419]
        | Annotated[_values.FormId, _VARIANT_16420]
        | Annotated[_values.FormId, _VARIANT_16421]
        | Annotated[_values.FormId, _VARIANT_16422]
        | Annotated[_values.FormId, _VARIANT_16423]
        | Annotated[_values.FormId, _VARIANT_16424]
        | Annotated[_values.FormId, _VARIANT_16425]
        | Annotated[_values.FormId, _VARIANT_16426]
        | Annotated[_values.FormId, _VARIANT_16427]
        | Annotated[_values.FormId, _VARIANT_16428]
        | Annotated[_values.FormId, _VARIANT_16429]
        | Annotated[_values.FormId, _VARIANT_16430]
        | Annotated[_values.FormId, _VARIANT_16431]
        | Annotated[_values.FormId, _VARIANT_16432]
        | Annotated[_values.FormId, _VARIANT_16433]
        | Annotated[_values.FormId, _VARIANT_16434]
        | Annotated[_values.FormId, _VARIANT_16435]
        | Annotated[_values.FormId, _VARIANT_16436]
        | Annotated[_values.FormId, _VARIANT_16437]
        | Annotated[_values.FormId, _VARIANT_16438]
        | Annotated[_values.FormId, _VARIANT_16439]
        | Annotated[_values.FormId, _VARIANT_16440]
        | Annotated[_values.FormId, _VARIANT_16441]
        | Annotated[VatsValueFunction16442, _VARIANT_16442]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16443,
        ]
        | Annotated[_values.FormId, _VARIANT_16444]
        | Annotated[_values.FormId, _VARIANT_16445]
        | Annotated[_values.FormId, _VARIANT_16446]
        | Annotated[PlayerAction16447, _VARIANT_16447]
        | Annotated[CastingType16448, _VARIANT_16448]
        | Annotated[_values.FormId, _VARIANT_16449]
        | Annotated[_values.FormId, _VARIANT_16450]
        | Annotated[_values.FormId, _VARIANT_16451]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16452,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16453,
        ]
        | Annotated[_values.FormId, _VARIANT_16454]
        | Annotated[FurnitureAnim16455, _VARIANT_16455]
        | Annotated[FurnitureEntry16456, _VARIANT_16456]
        | Annotated[_values.FormId, _VARIANT_16457]
        | Annotated[WardState16458, _VARIANT_16458]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16459,
        ]
        | Annotated[_values.FormId, _VARIANT_16460]
        | Annotated[_values.FormId, _VARIANT_16461]
        | Annotated[_values.FormId, _VARIANT_16462]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_16464]
        | Annotated[bytes, _VARIANT_16465]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16466,
        ]
        | Annotated[float, _VARIANT_16467]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16468,
        ]
        | Annotated[Sex16469, _VARIANT_16469]
        | Annotated[ActorValue16470, _VARIANT_16470]
        | Annotated[CrimeType16471, _VARIANT_16471]
        | Annotated[Axis16472, _VARIANT_16472]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16473,
        ]
        | Annotated[MiscStat16474, _VARIANT_16474]
        | Annotated[Alignment16475, _VARIANT_16475]
        | Annotated[_values.FormId, _VARIANT_16476]
        | Annotated[FormType16477, _VARIANT_16477]
        | Annotated[CriticalStage16478, _VARIANT_16478]
        | Annotated[_values.FormId, _VARIANT_16479]
        | Annotated[_values.FormId, _VARIANT_16480]
        | Annotated[_values.FormId, _VARIANT_16481]
        | Annotated[_values.FormId, _VARIANT_16482]
        | Annotated[_values.FormId, _VARIANT_16483]
        | Annotated[_values.FormId, _VARIANT_16484]
        | Annotated[_values.FormId, _VARIANT_16485]
        | Annotated[_values.FormId, _VARIANT_16486]
        | Annotated[_values.FormId, _VARIANT_16487]
        | Annotated[_values.FormId, _VARIANT_16488]
        | Annotated[_values.FormId, _VARIANT_16489]
        | Annotated[_values.FormId, _VARIANT_16490]
        | Annotated[_values.FormId, _VARIANT_16491]
        | Annotated[_values.FormId, _VARIANT_16492]
        | Annotated[_values.FormId, _VARIANT_16493]
        | Annotated[_values.FormId, _VARIANT_16494]
        | Annotated[_values.FormId, _VARIANT_16495]
        | Annotated[_values.FormId, _VARIANT_16496]
        | Annotated[_values.FormId, _VARIANT_16497]
        | Annotated[_values.FormId, _VARIANT_16498]
        | Annotated[_values.FormId, _VARIANT_16499]
        | Annotated[_values.FormId, _VARIANT_16500]
        | Annotated[VatsValueFunction16501, _VARIANT_16501]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_16503]
            | Annotated[_values.FormId, _VARIANT_16504]
            | Annotated[_values.FormId, _VARIANT_16505]
            | Annotated[_values.FormId, _VARIANT_16506]
            | Annotated[bytes, _VARIANT_16507]
            | Annotated[TargetPart16508, _VARIANT_16508]
            | Annotated[VatsAction16509, _VARIANT_16509]
            | Annotated[bytes, _VARIANT_16510]
            | Annotated[bytes, _VARIANT_16511]
            | Annotated[_values.FormId, _VARIANT_16512]
            | Annotated[_values.FormId, _VARIANT_16513]
            | Annotated[bytes, _VARIANT_16514]
            | Annotated[bytes, _VARIANT_16515]
            | Annotated[bytes, _VARIANT_16516]
            | Annotated[bytes, _VARIANT_16517]
            | Annotated[WeaponType16518, _VARIANT_16518]
            | Annotated[bytes, _VARIANT_16519]
            | Annotated[bytes, _VARIANT_16520]
            | Annotated[ProjectileType16521, _VARIANT_16521]
            | Annotated[DeliveryType16522, _VARIANT_16522]
            | Annotated[CastingType16523, _VARIANT_16523],
            _VARIANT_16502,
        ]
        | Annotated[_values.FormId, _VARIANT_16524]
        | Annotated[_values.FormId, _VARIANT_16525]
        | Annotated[_values.FormId, _VARIANT_16526]
        | Annotated[PlayerAction16527, _VARIANT_16527]
        | Annotated[CastingType16528, _VARIANT_16528]
        | Annotated[_values.FormId, _VARIANT_16529]
        | Annotated[_values.FormId, _VARIANT_16530]
        | Annotated[_values.FormId, _VARIANT_16531]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16532,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16533,
        ]
        | Annotated[_values.FormId, _VARIANT_16534]
        | Annotated[FurnitureAnim16535, _VARIANT_16535]
        | Annotated[FurnitureEntry16536, _VARIANT_16536]
        | Annotated[_values.FormId, _VARIANT_16537]
        | Annotated[WardState16538, _VARIANT_16538]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16539,
        ]
        | Annotated[_values.FormId, _VARIANT_16540]
        | Annotated[_values.FormId, _VARIANT_16541]
        | Annotated[_values.FormId, _VARIANT_16542]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn16543]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_16545,
        ]
        | Annotated[_values.FormId, _VARIANT_16546]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_3"]
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


class Condition16394(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure16396] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure16396]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
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


class Effect16385(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL/14:Effects/repeat/0:Effect"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "base_effect": _base.Binding(
            path="SCRL/14:Effects/repeat/0:Effect/0:Base Effect",
            kind="subrecord",
            name="Base Effect",
        ),
        "efit": _base.Binding(
            path="SCRL/14:Effects/repeat/0:Effect/1:EFIT",
            kind="subrecord",
            name="EFIT",
        ),
        "conditions": _base.Binding(
            path="SCRL/14:Effects/repeat/0:Effect/2:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "SCRL/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition"
            ),
            child_kind="sequence",
        ),
    }

    base_effect: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    efit: Optional[Structure16389] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition16394, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["base_effect"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["efit"]
    ) -> _base.FieldRef[Optional[Structure16389]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition16394, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ScrollRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCRL"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SCRL"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SCRL/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "object_bounds": _base.Binding(
            path="SCRL/1:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "name": _base.Binding(
            path="SCRL/2:Name",
            kind="subrecord",
            name="Name",
        ),
        "keyword_count": _base.Binding(
            path="SCRL/3:Keyword Count",
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path="SCRL/4:Keywords",
            kind="subrecord",
            name="Keywords",
        ),
        "menu_display_object": _base.Binding(
            path="SCRL/5:Menu Display Object",
            kind="subrecord",
            name="Menu Display Object",
        ),
        "equipment_type": _base.Binding(
            path="SCRL/6:Equipment Type",
            kind="subrecord",
            name="Equipment Type",
        ),
        "description": _base.Binding(
            path="SCRL/7:Description",
            kind="subrecord",
            name="Description",
        ),
        "model": _base.Binding(
            path="SCRL/8:Model",
            kind="unordered",
            name="Model",
        ),
        "destructible": _base.Binding(
            path="SCRL/9:Destructible",
            kind="sequence",
            name="Destructible",
        ),
        "sound_pick_up": _base.Binding(
            path="SCRL/10:Sound - Pick Up",
            kind="subrecord",
            name="Sound - Pick Up",
        ),
        "sound_put_down": _base.Binding(
            path="SCRL/11:Sound - Put Down",
            kind="subrecord",
            name="Sound - Put Down",
        ),
        "item": _base.Binding(
            path="SCRL/12:Item",
            kind="subrecord",
            name="Item",
        ),
        "data": _base.Binding(
            path="SCRL/13:Data",
            kind="subrecord",
            name="Data",
        ),
        "effects": _base.Binding(
            path="SCRL/14:Effects",
            kind="repeat",
            name="Effects",
            repeated_path="SCRL/14:Effects/repeat/0:Effect",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure16232] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    menu_display_object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    equipment_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    model: Optional[Model16252] = None
    """Value decoded from this schema node."""

    destructible: Optional[Destructible16298] = None
    """Value decoded from this schema node."""

    sound_pick_up: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sound_put_down: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    item: Optional[Structure16370] = None
    """Value decoded from this schema node."""

    data: Optional[Structure16374] = None
    """Value decoded from this schema node."""

    effects: tuple[Effect16385, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure16232]]:
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
        self, name: Literal["menu_display_object"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equipment_type"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
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
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model16252]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["destructible"]
    ) -> _base.FieldRef[Optional[Destructible16298]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sound_pick_up"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sound_put_down"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["item"]
    ) -> _base.FieldRef[Optional[Structure16370]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure16374]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effects"]
    ) -> _base.FieldRef[tuple[Effect16385, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
