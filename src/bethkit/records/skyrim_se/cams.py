"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure6363(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6365": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6366": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6367": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_6365: bytes
    """Value decoded from this schema node."""

    unused_6366: bytes
    """Value decoded from this schema node."""

    unused_6367: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6365"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6366"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6367"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6363: _base.Variant = _base.Variant(
    path=("CAMS/1:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure6368(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_6371": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6372": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/1:St"
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

    unused_6371: bytes
    """Value decoded from this schema node."""

    unused_6372: bytes
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
    def field(self, name: Literal["unused_6371"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6372"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6368: _base.Variant = _base.Variant(
    path=("CAMS/1:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture6376(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/2:St"
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


class Structure6373(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_6380": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_6381": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture6376, ...]
    """Value decoded from this schema node."""

    unused_6380: bytes
    """Value decoded from this schema node."""

    unused_6381: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture6376, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6380"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_6381"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6373: _base.Variant = _base.Variant(
    path=("CAMS/1:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture6386(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
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


class Material6393(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
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


class Structure6382(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "CAMS/1:Model/1:Model Information/payload/variants/3:St"
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

    textures: tuple[Texture6386, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material6393, ...]
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
    ) -> _base.FieldRef[tuple[Texture6386, ...]]:
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
    ) -> _base.FieldRef[tuple[Material6393, ...]]:
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


_VARIANT_6382: _base.Variant = _base.Variant(
    path=("CAMS/1:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture6400(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "CAMS/1:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "CAMS/1:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "CAMS/1:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "CAMS/1:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model6358(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CAMS/1:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="CAMS/1:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="CAMS/1:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="CAMS/1:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure6363, _VARIANT_6363]
        | Annotated[Structure6368, _VARIANT_6368]
        | Annotated[Structure6373, _VARIANT_6373]
        | Annotated[Structure6382, _VARIANT_6382]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture6400, ...]] = None
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
            Annotated[Structure6363, _VARIANT_6363]
            | Annotated[Structure6368, _VARIANT_6368]
            | Annotated[Structure6373, _VARIANT_6373]
            | Annotated[Structure6382, _VARIANT_6382]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture6400, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Action6406(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SHOOT = 0
    FLY = 1
    HIT = 2
    ZOOM = 3


class Location6407(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ATTACKER = 0
    PROJECTILE = 1
    TARGET = 2
    LEAD_ACTOR = 3


class Target6408(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ATTACKER = 0
    PROJECTILE = 1
    TARGET = 2
    LEAD_ACTOR = 3


class Flags6409(enum.IntFlag):
    """Named values from the pinned schema."""

    POSITION_FOLLOWS_LOCATION = 1
    ROTATION_FOLLOWS_TARGET = 2
    DON_T_FOLLOW_BONE = 4
    FIRST_PERSON_CAMERA = 8
    NO_TRACER = 16
    START_AT_TIME_ZERO = 32


class TimeMultipliers6410(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CAMS/2:Data/payload/4:Time Multipliers"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "player": _base.Binding(
            path="CAMS/2:Data/payload/4:Time Multipliers/0:Player",
            kind="primitive",
            name="Player",
        ),
        "target": _base.Binding(
            path="CAMS/2:Data/payload/4:Time Multipliers/1:Target",
            kind="primitive",
            name="Target",
        ),
        "global_value": _base.Binding(
            path="CAMS/2:Data/payload/4:Time Multipliers/2:Global",
            kind="primitive",
            name="Global",
        ),
    }

    player: float
    """Value decoded from this schema node."""

    target: float
    """Value decoded from this schema node."""

    global_value: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["player"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["target"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["global_value"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure6405(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CAMS/2:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "action": _base.Binding(
            path="CAMS/2:Data/payload/0:Action",
            kind="primitive",
            name="Action",
        ),
        "location": _base.Binding(
            path="CAMS/2:Data/payload/1:Location",
            kind="primitive",
            name="Location",
        ),
        "target": _base.Binding(
            path="CAMS/2:Data/payload/2:Target",
            kind="primitive",
            name="Target",
        ),
        "flags": _base.Binding(
            path="CAMS/2:Data/payload/3:Flags",
            kind="primitive",
            name="Flags",
        ),
        "time_multipliers": _base.Binding(
            path="CAMS/2:Data/payload/4:Time Multipliers",
            kind="struct",
            name="Time Multipliers",
        ),
        "max_time": _base.Binding(
            path="CAMS/2:Data/payload/5:Max Time",
            kind="primitive",
            name="Max Time",
        ),
        "min_time": _base.Binding(
            path="CAMS/2:Data/payload/6:Min Time",
            kind="primitive",
            name="Min Time",
        ),
        "target_between_actors": _base.Binding(
            path="CAMS/2:Data/payload/7:Target % Between Actors",
            kind="primitive",
            name="Target % Between Actors",
        ),
        "near_target_distance": _base.Binding(
            path="CAMS/2:Data/payload/8:Near Target Distance",
            kind="primitive",
            name="Near Target Distance",
        ),
    }

    action: Action6406
    """Value decoded from this schema node."""

    location: Location6407
    """Value decoded from this schema node."""

    target: Target6408
    """Value decoded from this schema node."""

    flags: Flags6409
    """Value decoded from this schema node."""

    time_multipliers: TimeMultipliers6410
    """Value decoded from this schema node."""

    max_time: float
    """Value decoded from this schema node."""

    min_time: float
    """Value decoded from this schema node."""

    target_between_actors: float
    """Value decoded from this schema node."""

    near_target_distance: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["action"]) -> _base.FieldRef[Action6406]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["location"]) -> _base.FieldRef[Location6407]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["target"]) -> _base.FieldRef[Target6408]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags6409]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["time_multipliers"]
    ) -> _base.FieldRef[TimeMultipliers6410]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["min_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target_between_actors"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["near_target_distance"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class CameraShotRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "CAMS"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "CAMS"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="CAMS/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "model": _base.Binding(
            path="CAMS/1:Model",
            kind="unordered",
            name="Model",
        ),
        "data": _base.Binding(
            path="CAMS/2:Data",
            kind="subrecord",
            name="Data",
        ),
        "image_space_modifier": _base.Binding(
            path="CAMS/3:Image Space Modifier",
            kind="subrecord",
            name="Image Space Modifier",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    model: Optional[Model6358] = None
    """Value decoded from this schema node."""

    data: Optional[Structure6405] = None
    """Value decoded from this schema node."""

    image_space_modifier: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model6358]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure6405]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["image_space_modifier"]
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
