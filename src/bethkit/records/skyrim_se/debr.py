"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base


class Flags5213(enum.IntFlag):
    """Named values from the pinned schema."""

    HAS_COLLISION_DATA = 1


class Structure5210(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "DEBR/1:Models/repeat/0:Model/0:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "percentage": _base.Binding(
            path=("DEBR/1:Models/repeat/0:Model/0:Data/payload/0:Percentage"),
            kind="primitive",
            name="Percentage",
        ),
        "model_file_name_value": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/0:Data/payload/1:Model FileName"
            ),
            kind="primitive",
            name="Model FileName",
        ),
        "flags": _base.Binding(
            path=("DEBR/1:Models/repeat/0:Model/0:Data/payload/2:Flags"),
            kind="primitive",
            name="Flags",
        ),
    }

    percentage: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    model_file_name_value: str
    """Value decoded from this schema node."""

    flags: Flags5213
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["percentage"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_file_name_value"]
    ) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags5213]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure5216(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_5218": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_5219": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_5220": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_5218: bytes
    """Value decoded from this schema node."""

    unused_5219: bytes
    """Value decoded from this schema node."""

    unused_5220: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_5218"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_5219"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_5220"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_5216: _base.Variant = _base.Variant(
    path=(
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/0:Structure"
    )
)


class Structure5221(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_5224": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_5225": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_5224: bytes
    """Value decoded from this schema node."""

    unused_5225: bytes
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
    def field(self, name: Literal["unused_5224"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_5225"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_5221: _base.Variant = _base.Variant(
    path=(
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/1:Structure"
    )
)


class Texture5229(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/2:Structure/1:Textures/element/2:Folder Ha"
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


class Structure5226(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_5233": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_5234": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture5229, ...]
    """Value decoded from this schema node."""

    unused_5233: bytes
    """Value decoded from this schema node."""

    unused_5234: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture5229, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_5233"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_5234"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_5226: _base.Variant = _base.Variant(
    path=(
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/2:Structure"
    )
)


class Texture5239(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/1:Textures/element/2:Folder Ha"
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


class Material5246(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/3:Materials/element/0:File Has"
                "h"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/3:Materials/element/1:Extensio"
                "n"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/3:Materials/element/2:Folder H"
                "ash"
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


class Structure5235(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
                "ad/variants/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture5239, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material5246, ...]
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
    ) -> _base.FieldRef[tuple[Texture5239, ...]]:
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
    ) -> _base.FieldRef[tuple[Material5246, ...]]:
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


_VARIANT_5235: _base.Variant = _base.Variant(
    path=(
        "DEBR/1:Models/repeat/0:Model/1:Model Information/paylo"
        "ad/variants/3:Structure"
    )
)


class Model5208(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "DEBR/1:Models/repeat/0:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "data": _base.Binding(
            path="DEBR/1:Models/repeat/0:Model/0:Data",
            kind="subrecord",
            name="Data",
        ),
        "model_information_value": _base.Binding(
            path="DEBR/1:Models/repeat/0:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
    }

    data: Optional[Structure5210] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure5216, _VARIANT_5216]
        | Annotated[Structure5221, _VARIANT_5221]
        | Annotated[Structure5226, _VARIANT_5226]
        | Annotated[Structure5235, _VARIANT_5235]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure5210]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model_information_value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Structure5216, _VARIANT_5216]
            | Annotated[Structure5221, _VARIANT_5221]
            | Annotated[Structure5226, _VARIANT_5226]
            | Annotated[Structure5235, _VARIANT_5235]
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


class DebrisRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "DEBR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "DEBR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="DEBR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "models": _base.Binding(
            path="DEBR/1:Models",
            kind="repeat",
            name="Models",
            repeated_path="DEBR/1:Models/repeat/0:Model",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    models: tuple[Model5208, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["models"]
    ) -> _base.FieldRef[tuple[Model5208, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
