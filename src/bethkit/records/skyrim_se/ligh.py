"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags10259(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type10263(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    OBJECT = 1
    STRING = 2
    INT32 = 3
    FLOAT = 4
    BOOL = 5
    ARRAY_OF_OBJECT = 11
    ARRAY_OF_STRING = 12
    ARRAY_OF_INT32 = 13
    ARRAY_OF_FLOAT = 14
    ARRAY_OF_BOOL = 15


class Flags10264(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_10266: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV210268(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/2:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
    }

    unused: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    alias: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    form_id: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["form_id"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10268: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV110272(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    form_id: _values.FormId
    """Value decoded from this schema node."""

    alias: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    unused: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["form_id"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
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


_VARIANT_10272: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_10267: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_10276: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_10277: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_10278: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool10279(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_10279: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV210282(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/2:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
    }

    unused: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    alias: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    form_id: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["form_id"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10282: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV110286(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    form_id: _values.FormId
    """Value decoded from this schema node."""

    alias: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    unused: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["form_id"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
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


_VARIANT_10286: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_10280: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_10290: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_10292: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_10294: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element10297(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_10296: _base.Variant = _base.Variant(
    path=(
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property10261(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type10263
    """Value decoded from this schema node."""

    flags: Flags10264
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_10266]
        | Annotated[
            Annotated[ObjectV210268, _VARIANT_10268]
            | Annotated[ObjectV110272, _VARIANT_10272],
            _VARIANT_10267,
        ]
        | Annotated[str, _VARIANT_10276]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10277,
        ]
        | Annotated[float, _VARIANT_10278]
        | Annotated[Bool10279, _VARIANT_10279]
        | Annotated[
            tuple[
                Annotated[ObjectV210282, _VARIANT_10282]
                | Annotated[ObjectV110286, _VARIANT_10286],
                ...,
            ],
            _VARIANT_10280,
        ]
        | Annotated[tuple[str, ...], _VARIANT_10290]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_10292,
        ]
        | Annotated[tuple[float, ...], _VARIANT_10294]
        | Annotated[tuple[Element10297, ...], _VARIANT_10296]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type10263]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10264]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_10266]
        | Annotated[
            Annotated[ObjectV210268, _VARIANT_10268]
            | Annotated[ObjectV110272, _VARIANT_10272],
            _VARIANT_10267,
        ]
        | Annotated[str, _VARIANT_10276]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10277,
        ]
        | Annotated[float, _VARIANT_10278]
        | Annotated[Bool10279, _VARIANT_10279]
        | Annotated[
            tuple[
                Annotated[ObjectV210282, _VARIANT_10282]
                | Annotated[ObjectV110286, _VARIANT_10286],
                ...,
            ],
            _VARIANT_10280,
        ]
        | Annotated[tuple[str, ...], _VARIANT_10290]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_10292,
        ]
        | Annotated[tuple[float, ...], _VARIANT_10294]
        | Annotated[tuple[Element10297, ...], _VARIANT_10296]
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


class Script10257(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "LIGH/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags10259
    """Value decoded from this schema node."""

    properties: tuple[Property10261, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10259]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property10261, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure10253(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="LIGH/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("LIGH/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="LIGH/1:Virtual Machine Adapter/payload/2:Scripts",
            kind="array",
            name="Scripts",
        ),
    }

    version: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    object_format: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    scripts: tuple[Script10257, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["version"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_format"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["scripts"]
    ) -> _base.FieldRef[tuple[Script10257, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure10299(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/2:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="LIGH/2:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="LIGH/2:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="LIGH/2:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="LIGH/2:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="LIGH/2:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="LIGH/2:Object Bounds/payload/5:Z2",
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


class Structure10311(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10313": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10314": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10315": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_10313: bytes
    """Value decoded from this schema node."""

    unused_10314: bytes
    """Value decoded from this schema node."""

    unused_10315: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10313"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10314"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10315"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10311: _base.Variant = _base.Variant(
    path=("LIGH/3:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure10316(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_10319": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10320": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/1:St"
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

    unused_10319: bytes
    """Value decoded from this schema node."""

    unused_10320: bytes
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
    def field(self, name: Literal["unused_10319"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10320"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10316: _base.Variant = _base.Variant(
    path=("LIGH/3:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture10324(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/2:St"
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


class Structure10321(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_10328": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10329": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture10324, ...]
    """Value decoded from this schema node."""

    unused_10328: bytes
    """Value decoded from this schema node."""

    unused_10329: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture10324, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10328"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10329"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10321: _base.Variant = _base.Variant(
    path=("LIGH/3:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture10334(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
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


class Material10341(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
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


class Structure10330(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "LIGH/3:Model/1:Model Information/payload/variants/3:St"
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

    textures: tuple[Texture10334, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material10341, ...]
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
    ) -> _base.FieldRef[tuple[Texture10334, ...]]:
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
    ) -> _base.FieldRef[tuple[Material10341, ...]]:
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


_VARIANT_10330: _base.Variant = _base.Variant(
    path=("LIGH/3:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture10348(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/3:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "LIGH/3:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "LIGH/3:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "LIGH/3:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model10306(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/3:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="LIGH/3:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="LIGH/3:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="LIGH/3:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure10311, _VARIANT_10311]
        | Annotated[Structure10316, _VARIANT_10316]
        | Annotated[Structure10321, _VARIANT_10321]
        | Annotated[Structure10330, _VARIANT_10330]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture10348, ...]] = None
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
            Annotated[Structure10311, _VARIANT_10311]
            | Annotated[Structure10316, _VARIANT_10316]
            | Annotated[Structure10321, _VARIANT_10321]
            | Annotated[Structure10330, _VARIANT_10330]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture10348, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class VatsTargetable10357(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure10354(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/4:Destructible/0:Header/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path="LIGH/4:Destructible/0:Header/payload/0:Health",
            kind="primitive",
            name="Health",
        ),
        "dest_count": _base.Binding(
            path="LIGH/4:Destructible/0:Header/payload/1:DEST Count",
            kind="primitive",
            name="DEST Count",
        ),
        "vats_targetable": _base.Binding(
            path=("LIGH/4:Destructible/0:Header/payload/2:VATS Targetable"),
            kind="primitive",
            name="VATS Targetable",
        ),
        "unknown": _base.Binding(
            path="LIGH/4:Destructible/0:Header/payload/3:Unknown",
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

    vats_targetable: VatsTargetable10357
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
    ) -> _base.FieldRef[VatsTargetable10357]:
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


class Flags10366(enum.IntFlag):
    """Named values from the pinned schema."""

    CAP_DAMAGE = 1
    DISABLE = 2
    DESTROY = 4
    IGNORE_EXTERNAL_DMG = 8


class Structure10362(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
        "ion Stage Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/0:Health %"
            ),
            kind="primitive",
            name="Health %",
        ),
        "index": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/1:Index"
            ),
            kind="primitive",
            name="Index",
        ),
        "model_damage_stage_value": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/2:Model Damage Stage"
            ),
            kind="primitive",
            name="Model Damage Stage",
        ),
        "flags": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/3:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "self_damage_per_second": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/4:Self Damage per Second"
            ),
            kind="primitive",
            name="Self Damage per Second",
        ),
        "explosion": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/5:Explosion"
            ),
            kind="primitive",
            name="Explosion",
        ),
        "debris": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/6:Debris"
            ),
            kind="primitive",
            name="Debris",
        ),
        "debris_count": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
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

    flags: Flags10366
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10366]:
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


class Structure10376(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10378": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/1:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10379": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10380": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_10378: bytes
    """Value decoded from this schema node."""

    unused_10379: bytes
    """Value decoded from this schema node."""

    unused_10380: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10378"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10379"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10380"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10376: _base.Variant = _base.Variant(
    path=(
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
)


class Structure10381(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_10384": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10385": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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

    unused_10384: bytes
    """Value decoded from this schema node."""

    unused_10385: bytes
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
    def field(self, name: Literal["unused_10384"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10385"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10381: _base.Variant = _base.Variant(
    path=(
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
)


class Texture10389(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Structure10386(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_10393": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_10394": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture10389, ...]
    """Value decoded from this schema node."""

    unused_10393: bytes
    """Value decoded from this schema node."""

    unused_10394: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture10389, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10393"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_10394"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10386: _base.Variant = _base.Variant(
    path=(
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
)


class Texture10399(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Material10406(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/3:Mater"
        "ials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Structure10395(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/0:Heade"
                "rs"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/2:Addon"
                "s"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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

    textures: tuple[Texture10399, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material10406, ...]
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
    ) -> _base.FieldRef[tuple[Texture10399, ...]]:
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
    ) -> _base.FieldRef[tuple[Material10406, ...]]:
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


_VARIANT_10395: _base.Variant = _base.Variant(
    path=(
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
)


class AlternateTexture10413(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
        "Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
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


class Model10371(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/0:"
                "Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure10376, _VARIANT_10376]
        | Annotated[Structure10381, _VARIANT_10381]
        | Annotated[Structure10386, _VARIANT_10386]
        | Annotated[Structure10395, _VARIANT_10395]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture10413, ...]] = None
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
            Annotated[Structure10376, _VARIANT_10376]
            | Annotated[Structure10381, _VARIANT_10381]
            | Annotated[Structure10386, _VARIANT_10386]
            | Annotated[Structure10395, _VARIANT_10395]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture10413, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Stage10360(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/4:Destructible/1:Stages/repeat/0:Stage"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "destruction_stage_data": _base.Binding(
            path=(
                "LIGH/4:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data"
            ),
            kind="subrecord",
            name="Destruction Stage Data",
        ),
        "model": _base.Binding(
            path=("LIGH/4:Destructible/1:Stages/repeat/0:Stage/1:Model"),
            kind="sequence",
            name="Model",
        ),
        "end_marker": _base.Binding(
            path=("LIGH/4:Destructible/1:Stages/repeat/0:Stage/2:End Marker"),
            kind="subrecord",
            name="End Marker",
        ),
    }

    destruction_stage_data: Optional[Structure10362] = None
    """Value decoded from this schema node."""

    model: Optional[Model10371] = None
    """Value decoded from this schema node."""

    end_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["destruction_stage_data"]
    ) -> _base.FieldRef[Optional[Structure10362]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model10371]]:
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


class Destructible10352(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/4:Destructible"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="LIGH/4:Destructible/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "stages": _base.Binding(
            path="LIGH/4:Destructible/1:Stages",
            kind="repeat",
            name="Stages",
            repeated_path="LIGH/4:Destructible/1:Stages/repeat/0:Stage",
            child_kind="sequence",
        ),
    }

    header: Optional[Structure10354] = None
    """Value decoded from this schema node."""

    stages: tuple[Stage10360, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure10354]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stages"]
    ) -> _base.FieldRef[tuple[Stage10360, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Icon10421(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/6:Icon"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "large_icon_file_name": _base.Binding(
            path="LIGH/6:Icon/0:Large Icon FileName",
            kind="subrecord",
            name="Large Icon FileName",
        ),
        "small_icon_file_name": _base.Binding(
            path="LIGH/6:Icon/1:Small Icon FileName",
            kind="subrecord",
            name="Small Icon FileName",
        ),
    }

    large_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    small_icon_file_name: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["large_icon_file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["small_icon_file_name"]
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


class Color10430(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/7:DATA/payload/2:Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="LIGH/7:DATA/payload/2:Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="LIGH/7:DATA/payload/2:Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="LIGH/7:DATA/payload/2:Color/2:Blue",
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path="LIGH/7:DATA/payload/2:Color/3:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    red: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    green: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    blue: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused: bytes
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


class Flags10435(enum.IntFlag):
    """Named values from the pinned schema."""

    DYNAMIC = 1
    CAN_BE_CARRIED = 2
    NEGATIVE = 4
    FLICKER = 8
    UNKNOWN = 16
    OFF_BY_DEFAULT = 32
    FLICKER_SLOW = 64
    PULSE = 128
    PULSE_SLOW = 256
    SPOT_LIGHT = 512
    SHADOW_SPOTLIGHT = 1024
    SHADOW_HEMISPHERE = 2048
    SHADOW_OMNIDIRECTIONAL = 4096
    PORTAL_STRICT = 8192


class FlickerEffect10439(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/7:DATA/payload/7:Flicker Effect"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "period": _base.Binding(
            path="LIGH/7:DATA/payload/7:Flicker Effect/0:Period",
            kind="primitive",
            name="Period",
        ),
        "intensity_amplitude": _base.Binding(
            path=("LIGH/7:DATA/payload/7:Flicker Effect/1:Intensity Amplitude"),
            kind="primitive",
            name="Intensity Amplitude",
        ),
        "movement_amplitude": _base.Binding(
            path=("LIGH/7:DATA/payload/7:Flicker Effect/2:Movement Amplitude"),
            kind="primitive",
            name="Movement Amplitude",
        ),
    }

    period: float
    """Value decoded from this schema node."""

    intensity_amplitude: float
    """Value decoded from this schema node."""

    movement_amplitude: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["period"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["intensity_amplitude"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["movement_amplitude"]
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


class Structure10427(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH/7:DATA/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "time": _base.Binding(
            path="LIGH/7:DATA/payload/0:Time",
            kind="primitive",
            name="Time",
        ),
        "radius": _base.Binding(
            path="LIGH/7:DATA/payload/1:Radius",
            kind="primitive",
            name="Radius",
        ),
        "color": _base.Binding(
            path="LIGH/7:DATA/payload/2:Color",
            kind="struct",
            name="Color",
        ),
        "flags": _base.Binding(
            path="LIGH/7:DATA/payload/3:Flags",
            kind="primitive",
            name="Flags",
        ),
        "falloff_exponent": _base.Binding(
            path="LIGH/7:DATA/payload/4:Falloff Exponent",
            kind="primitive",
            name="Falloff Exponent",
        ),
        "fov": _base.Binding(
            path="LIGH/7:DATA/payload/5:FOV",
            kind="primitive",
            name="FOV",
        ),
        "near_clip": _base.Binding(
            path="LIGH/7:DATA/payload/6:Near Clip",
            kind="primitive",
            name="Near Clip",
        ),
        "flicker_effect": _base.Binding(
            path="LIGH/7:DATA/payload/7:Flicker Effect",
            kind="struct",
            name="Flicker Effect",
        ),
        "value": _base.Binding(
            path="LIGH/7:DATA/payload/8:Value",
            kind="primitive",
            name="Value",
        ),
        "weight": _base.Binding(
            path="LIGH/7:DATA/payload/9:Weight",
            kind="primitive",
            name="Weight",
        ),
    }

    time: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    radius: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    color: Color10430
    """Value decoded from this schema node."""

    flags: Flags10435
    """Value decoded from this schema node."""

    falloff_exponent: float
    """Value decoded from this schema node."""

    fov: float
    """Value decoded from this schema node."""

    near_clip: float
    """Value decoded from this schema node."""

    flicker_effect: FlickerEffect10439
    """Value decoded from this schema node."""

    value: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    weight: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["time"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radius"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["color"]) -> _base.FieldRef[Color10430]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10435]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["falloff_exponent"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fov"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["near_clip"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flicker_effect"]
    ) -> _base.FieldRef[FlickerEffect10439]:
        """Returns the typed field reference."""

        ...

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


class LightRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "LIGH"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "LIGH"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="LIGH/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="LIGH/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "object_bounds": _base.Binding(
            path="LIGH/2:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "model": _base.Binding(
            path="LIGH/3:Model",
            kind="unordered",
            name="Model",
        ),
        "destructible": _base.Binding(
            path="LIGH/4:Destructible",
            kind="sequence",
            name="Destructible",
        ),
        "name": _base.Binding(
            path="LIGH/5:Name",
            kind="subrecord",
            name="Name",
        ),
        "icon": _base.Binding(
            path="LIGH/6:Icon",
            kind="unordered",
            name="Icon",
        ),
        "data": _base.Binding(
            path="LIGH/7:DATA",
            kind="subrecord",
            name="DATA",
        ),
        "fade_value": _base.Binding(
            path="LIGH/8:Fade value",
            kind="subrecord",
            name="Fade value",
        ),
        "sound": _base.Binding(
            path="LIGH/9:Sound",
            kind="subrecord",
            name="Sound",
        ),
        "lens": _base.Binding(
            path="LIGH/10:Lens",
            kind="subrecord",
            name="Lens",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure10253] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure10299] = None
    """Value decoded from this schema node."""

    model: Optional[Model10306] = None
    """Value decoded from this schema node."""

    destructible: Optional[Destructible10352] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    icon: Optional[Icon10421] = None
    """Value decoded from this schema node."""

    data: Optional[Structure10427] = None
    """Value decoded from this schema node."""

    fade_value: Optional[float] = None
    """Value decoded from this schema node."""

    sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    lens: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["virtual_machine_adapter"]
    ) -> _base.FieldRef[Optional[Structure10253]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[Structure10299]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model10306]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["destructible"]
    ) -> _base.FieldRef[Optional[Destructible10352]]:
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
        self, name: Literal["icon"]
    ) -> _base.FieldRef[Optional[Icon10421]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure10427]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fade_value"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lens"]
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
