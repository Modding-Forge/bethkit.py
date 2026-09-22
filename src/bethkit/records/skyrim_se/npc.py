"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags11656(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type11660(_values.OpenIntEnum):
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


class Flags11661(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_11663: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV211665(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_11665: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV111669(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_11669: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_11664: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_11673: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_11674: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_11675: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool11676(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_11676: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV211679(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_11679: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV111683(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_11683: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_11677: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_11687: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_11689: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_11691: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element11694(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_11693: _base.Variant = _base.Variant(
    path=(
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property11658(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type11660
    """Value decoded from this schema node."""

    flags: Flags11661
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_11663]
        | Annotated[
            Annotated[ObjectV211665, _VARIANT_11665]
            | Annotated[ObjectV111669, _VARIANT_11669],
            _VARIANT_11664,
        ]
        | Annotated[str, _VARIANT_11673]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11674,
        ]
        | Annotated[float, _VARIANT_11675]
        | Annotated[Bool11676, _VARIANT_11676]
        | Annotated[
            tuple[
                Annotated[ObjectV211679, _VARIANT_11679]
                | Annotated[ObjectV111683, _VARIANT_11683],
                ...,
            ],
            _VARIANT_11677,
        ]
        | Annotated[tuple[str, ...], _VARIANT_11687]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_11689,
        ]
        | Annotated[tuple[float, ...], _VARIANT_11691]
        | Annotated[tuple[Element11694, ...], _VARIANT_11693]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type11660]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags11661]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_11663]
        | Annotated[
            Annotated[ObjectV211665, _VARIANT_11665]
            | Annotated[ObjectV111669, _VARIANT_11669],
            _VARIANT_11664,
        ]
        | Annotated[str, _VARIANT_11673]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11674,
        ]
        | Annotated[float, _VARIANT_11675]
        | Annotated[Bool11676, _VARIANT_11676]
        | Annotated[
            tuple[
                Annotated[ObjectV211679, _VARIANT_11679]
                | Annotated[ObjectV111683, _VARIANT_11683],
                ...,
            ],
            _VARIANT_11677,
        ]
        | Annotated[tuple[str, ...], _VARIANT_11687]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_11689,
        ]
        | Annotated[tuple[float, ...], _VARIANT_11691]
        | Annotated[tuple[Element11694, ...], _VARIANT_11693]
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


class Script11654(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "NPC_/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags11656
    """Value decoded from this schema node."""

    properties: tuple[Property11658, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags11656]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property11658, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure11650(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="NPC_/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("NPC_/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="NPC_/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script11654, ...]
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
    ) -> _base.FieldRef[tuple[Script11654, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure11696(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/2:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="NPC_/2:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="NPC_/2:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="NPC_/2:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="NPC_/2:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="NPC_/2:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="NPC_/2:Object Bounds/payload/5:Z2",
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


class Flags11705(enum.IntFlag):
    """Named values from the pinned schema."""

    FEMALE = 1
    ESSENTIAL = 2
    IS_CHAR_GEN_FACE_PRESET = 4
    RESPAWN = 8
    AUTO_CALC_STATS = 16
    UNIQUE = 32
    DOESN_T_AFFECT_STEALTH_METER = 64
    PC_LEVEL_MULT = 128
    USE_TEMPLATE = 256
    UNKNOWN_9 = 512
    UNKNOWN_10 = 1024
    PROTECTED = 2048
    UNKNOWN_12 = 4096
    UNKNOWN_13 = 8192
    SUMMONABLE = 16384
    UNKNOWN_15 = 32768
    DOESN_T_BLEED = 65536
    UNKNOWN_17 = 131072
    BLEEDOUT_OVERRIDE = 262144
    OPPOSITE_GENDER_ANIMS = 524288
    SIMPLE_ACTOR = 1048576
    LOOPED_SCRIPT = 2097152
    UNKNOWN_22 = 4194304
    UNKNOWN_23 = 8388608
    UNKNOWN_24 = 16777216
    UNKNOWN_25 = 33554432
    UNKNOWN_26 = 67108864
    UNKNOWN_27 = 134217728
    LOOPED_AUDIO = 268435456
    IS_GHOST = 536870912
    UNKNOWN_30 = 1073741824
    INVULNERABLE = 2147483648


_VARIANT_11709: _base.Variant = _base.Variant(
    path="NPC_/3:Configuration/payload/3:Level/variants/0:Level"
)


_VARIANT_11710: _base.Variant = _base.Variant(
    path=("NPC_/3:Configuration/payload/3:Level/variants/1:Level Mult")
)


class TemplateFlags11715(enum.IntFlag):
    """Named values from the pinned schema."""

    USE_TRAITS = 1
    USE_STATS = 2
    USE_FACTIONS = 4
    USE_SPELL_LIST = 8
    USE_AI_DATA = 16
    USE_AI_PACKAGES = 32
    USE_MODEL_ANIMATION = 64
    USE_BASE_DATA = 128
    USE_INVENTORY = 256
    USE_SCRIPT = 512
    USE_DEF_PACK_LIST = 1024
    USE_ATTACK_DATA = 2048
    USE_KEYWORDS = 4096


class Structure11704(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/3:Configuration/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="NPC_/3:Configuration/payload/0:Flags",
            kind="primitive",
            name="Flags",
        ),
        "magicka_offset": _base.Binding(
            path="NPC_/3:Configuration/payload/1:Magicka Offset",
            kind="primitive",
            name="Magicka Offset",
        ),
        "stamina_offset": _base.Binding(
            path="NPC_/3:Configuration/payload/2:Stamina Offset",
            kind="primitive",
            name="Stamina Offset",
        ),
        "level": _base.Binding(
            path="NPC_/3:Configuration/payload/3:Level",
            kind="union",
            name="Level",
        ),
        "calc_min_level": _base.Binding(
            path="NPC_/3:Configuration/payload/4:Calc min level",
            kind="primitive",
            name="Calc min level",
        ),
        "calc_max_level": _base.Binding(
            path="NPC_/3:Configuration/payload/5:Calc max level",
            kind="primitive",
            name="Calc max level",
        ),
        "speed_multiplier": _base.Binding(
            path="NPC_/3:Configuration/payload/6:Speed Multiplier",
            kind="primitive",
            name="Speed Multiplier",
        ),
        "disposition_base_unused": _base.Binding(
            path=("NPC_/3:Configuration/payload/7:Disposition Base (unused)"),
            kind="primitive",
            name="Disposition Base (unused)",
        ),
        "template_flags": _base.Binding(
            path="NPC_/3:Configuration/payload/8:Template Flags",
            kind="primitive",
            name="Template Flags",
        ),
        "health_offset": _base.Binding(
            path="NPC_/3:Configuration/payload/9:Health Offset",
            kind="primitive",
            name="Health Offset",
        ),
        "bleedout_override": _base.Binding(
            path="NPC_/3:Configuration/payload/10:Bleedout Override",
            kind="primitive",
            name="Bleedout Override",
        ),
    }

    flags: Flags11705
    """Value decoded from this schema node."""

    magicka_offset: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    stamina_offset: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    level: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)],
            _VARIANT_11709,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)],
            _VARIANT_11710,
        ]
    )
    """Value decoded from this schema node."""

    calc_min_level: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    calc_max_level: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    speed_multiplier: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=65535)
    ]
    """Value decoded from this schema node."""

    disposition_base_unused: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    template_flags: TemplateFlags11715
    """Value decoded from this schema node."""

    health_offset: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    bleedout_override: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=65535)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags11705]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["magicka_offset"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stamina_offset"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["level"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)],
            _VARIANT_11709,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)],
            _VARIANT_11710,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["calc_min_level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["calc_max_level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["speed_multiplier"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["disposition_base_unused"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["template_flags"]
    ) -> _base.FieldRef[TemplateFlags11715]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["health_offset"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bleedout_override"]
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


class Structure11720(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/4:Factions/repeat/0:Faction/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "faction": _base.Binding(
            path=("NPC_/4:Factions/repeat/0:Faction/payload/0:Faction"),
            kind="primitive",
            name="Faction",
        ),
        "rank": _base.Binding(
            path="NPC_/4:Factions/repeat/0:Faction/payload/1:Rank",
            kind="primitive",
            name="Rank",
        ),
        "unused": _base.Binding(
            path="NPC_/4:Factions/repeat/0:Faction/payload/2:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    faction: _values.FormId
    """Value decoded from this schema node."""

    rank: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["faction"]) -> _base.FieldRef[_values.FormId]:
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


class VatsTargetable11742(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure11739(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/11:Destructible/0:Header/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path="NPC_/11:Destructible/0:Header/payload/0:Health",
            kind="primitive",
            name="Health",
        ),
        "dest_count": _base.Binding(
            path=("NPC_/11:Destructible/0:Header/payload/1:DEST Count"),
            kind="primitive",
            name="DEST Count",
        ),
        "vats_targetable": _base.Binding(
            path=("NPC_/11:Destructible/0:Header/payload/2:VATS Targetable"),
            kind="primitive",
            name="VATS Targetable",
        ),
        "unknown": _base.Binding(
            path="NPC_/11:Destructible/0:Header/payload/3:Unknown",
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

    vats_targetable: VatsTargetable11742
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
    ) -> _base.FieldRef[VatsTargetable11742]:
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


class Flags11751(enum.IntFlag):
    """Named values from the pinned schema."""

    CAP_DAMAGE = 1
    DISABLE = 2
    DESTROY = 4
    IGNORE_EXTERNAL_DMG = 8


class Structure11747(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
        "tion Stage Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/0:Health %"
            ),
            kind="primitive",
            name="Health %",
        ),
        "index": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/1:Index"
            ),
            kind="primitive",
            name="Index",
        ),
        "model_damage_stage_value": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/2:Model Damage Stage"
            ),
            kind="primitive",
            name="Model Damage Stage",
        ),
        "flags": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/3:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "self_damage_per_second": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/4:Self Damage per Second"
            ),
            kind="primitive",
            name="Self Damage per Second",
        ),
        "explosion": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/5:Explosion"
            ),
            kind="primitive",
            name="Explosion",
        ),
        "debris": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/6:Debris"
            ),
            kind="primitive",
            name="Debris",
        ),
        "debris_count": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data/payload/7:Debris Count"
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

    flags: Flags11751
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags11751]:
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


class Structure11761(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/0:Structure/0:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_11763": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/0:Structure/1:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_11764": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/0:Structure/2:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_11765": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/0:Structure/3:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_11763: bytes
    """Value decoded from this schema node."""

    unused_11764: bytes
    """Value decoded from this schema node."""

    unused_11765: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_11763"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_11764"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_11765"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_11761: _base.Variant = _base.Variant(
    path=(
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/0:Structure"
    )
)


class Structure11766(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/1:Structure/0:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/1:Structure/1:ERRO"
                "R"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_11769": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/1:Structure/2:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_11770": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/1:Structure/3:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_11769: bytes
    """Value decoded from this schema node."""

    unused_11770: bytes
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
    def field(self, name: Literal["unused_11769"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_11770"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_11766: _base.Variant = _base.Variant(
    path=(
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/1:Structure"
    )
)


class Texture11774(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/2:Structure/1:Text"
        "ures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/2:Structure/1:Text"
                "ures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/2:Structure/1:Text"
                "ures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/2:Structure/1:Text"
                "ures/element/2:Folder Hash"
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


class Structure11771(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/2:Structure/0:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/2:Structure/1:Text"
                "ures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_11778": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/2:Structure/2:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_11779": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/2:Structure/3:Unus"
                "ed"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture11774, ...]
    """Value decoded from this schema node."""

    unused_11778: bytes
    """Value decoded from this schema node."""

    unused_11779: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture11774, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_11778"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_11779"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_11771: _base.Variant = _base.Variant(
    path=(
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/2:Structure"
    )
)


class Texture11784(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/3:Structure/1:Text"
        "ures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/1:Text"
                "ures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/1:Text"
                "ures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/1:Text"
                "ures/element/2:Folder Hash"
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


class Material11791(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/3:Structure/3:Mate"
        "rials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/3:Mate"
                "rials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/3:Mate"
                "rials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/3:Mate"
                "rials/element/2:Folder Hash"
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


class Structure11780(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/0:Head"
                "ers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/1:Text"
                "ures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/2:Addo"
                "ns"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/3:Mate"
                "rials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information/payload/variants/3:Structure/4:Unkn"
                "own"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture11784, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material11791, ...]
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
    ) -> _base.FieldRef[tuple[Texture11784, ...]]:
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
    ) -> _base.FieldRef[tuple[Material11791, ...]]:
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


_VARIANT_11780: _base.Variant = _base.Variant(
    path=(
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
        ":Model Information/payload/variants/3:Structure"
    )
)


class AlternateTexture11798(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/2"
        ":Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/2"
                ":Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/2"
                ":Alternate Textures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/2"
                ":Alternate Textures/payload/element/2:3D Index"
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


class Model11756(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/0"
                ":Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/1"
                ":Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model/2"
                ":Alternate Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure11761, _VARIANT_11761]
        | Annotated[Structure11766, _VARIANT_11766]
        | Annotated[Structure11771, _VARIANT_11771]
        | Annotated[Structure11780, _VARIANT_11780]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture11798, ...]] = None
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
            Annotated[Structure11761, _VARIANT_11761]
            | Annotated[Structure11766, _VARIANT_11766]
            | Annotated[Structure11771, _VARIANT_11771]
            | Annotated[Structure11780, _VARIANT_11780]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture11798, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Stage11745(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/11:Destructible/1:Stages/repeat/0:Stage"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "destruction_stage_data": _base.Binding(
            path=(
                "NPC_/11:Destructible/1:Stages/repeat/0:Stage/0:Destruc"
                "tion Stage Data"
            ),
            kind="subrecord",
            name="Destruction Stage Data",
        ),
        "model": _base.Binding(
            path=("NPC_/11:Destructible/1:Stages/repeat/0:Stage/1:Model"),
            kind="sequence",
            name="Model",
        ),
        "end_marker": _base.Binding(
            path=("NPC_/11:Destructible/1:Stages/repeat/0:Stage/2:End Marker"),
            kind="subrecord",
            name="End Marker",
        ),
    }

    destruction_stage_data: Optional[Structure11747] = None
    """Value decoded from this schema node."""

    model: Optional[Model11756] = None
    """Value decoded from this schema node."""

    end_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["destruction_stage_data"]
    ) -> _base.FieldRef[Optional[Structure11747]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model11756]]:
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


class Destructible11737(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/11:Destructible"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="NPC_/11:Destructible/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "stages": _base.Binding(
            path="NPC_/11:Destructible/1:Stages",
            kind="repeat",
            name="Stages",
            repeated_path="NPC_/11:Destructible/1:Stages/repeat/0:Stage",
            child_kind="sequence",
        ),
    }

    header: Optional[Structure11739] = None
    """Value decoded from this schema node."""

    stages: tuple[Stage11745, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure11739]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stages"]
    ) -> _base.FieldRef[tuple[Stage11745, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class AttackFlags11817(enum.IntFlag):
    """Named values from the pinned schema."""

    IGNORE_WEAPON = 1
    BASH_ATTACK = 2
    POWER_ATTACK = 4
    LEFT_ATTACK = 8
    ROTATING_ATTACK = 16
    UNKNOWN_5 = 32
    UNKNOWN_6 = 64
    UNKNOWN_7 = 128
    UNKNOWN_8 = 256
    UNKNOWN_9 = 512
    UNKNOWN_10 = 1024
    UNKNOWN_11 = 2048
    UNKNOWN_12 = 4096
    UNKNOWN_13 = 8192
    UNKNOWN_14 = 16384
    UNKNOWN_15 = 32768
    UNKNOWN_16 = 65536
    UNKNOWN_17 = 131072
    UNKNOWN_18 = 262144
    UNKNOWN_19 = 524288
    UNKNOWN_20 = 1048576
    UNKNOWN_21 = 2097152
    UNKNOWN_22 = 4194304
    UNKNOWN_23 = 8388608
    UNKNOWN_24 = 16777216
    UNKNOWN_25 = 33554432
    UNKNOWN_26 = 67108864
    UNKNOWN_27 = 134217728
    UNKNOWN_28 = 268435456
    UNKNOWN_29 = 536870912
    UNKNOWN_30 = 1073741824
    OVERRIDE_DATA = 2147483648


class Structure11813(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "damage_mult": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "0:Damage Mult"
            ),
            kind="primitive",
            name="Damage Mult",
        ),
        "attack_chance": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "1:Attack Chance"
            ),
            kind="primitive",
            name="Attack Chance",
        ),
        "attack_spell": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "2:Attack Spell"
            ),
            kind="primitive",
            name="Attack Spell",
        ),
        "attack_flags": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "3:Attack Flags"
            ),
            kind="primitive",
            name="Attack Flags",
        ),
        "attack_angle": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "4:Attack Angle"
            ),
            kind="primitive",
            name="Attack Angle",
        ),
        "strike_angle": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "5:Strike Angle"
            ),
            kind="primitive",
            name="Strike Angle",
        ),
        "stagger": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "6:Stagger"
            ),
            kind="primitive",
            name="Stagger",
        ),
        "attack_type": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "7:Attack Type"
            ),
            kind="primitive",
            name="Attack Type",
        ),
        "knockdown": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "8:Knockdown"
            ),
            kind="primitive",
            name="Knockdown",
        ),
        "recovery_time": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "9:Recovery Time"
            ),
            kind="primitive",
            name="Recovery Time",
        ),
        "stamina_mult": _base.Binding(
            path=(
                "NPC_/15:Attacks/repeat/0:Attack/0:Attack Data/payload/"
                "10:Stamina Mult"
            ),
            kind="primitive",
            name="Stamina Mult",
        ),
    }

    damage_mult: float
    """Value decoded from this schema node."""

    attack_chance: float
    """Value decoded from this schema node."""

    attack_spell: _values.FormId
    """Value decoded from this schema node."""

    attack_flags: AttackFlags11817
    """Value decoded from this schema node."""

    attack_angle: float
    """Value decoded from this schema node."""

    strike_angle: float
    """Value decoded from this schema node."""

    stagger: float
    """Value decoded from this schema node."""

    attack_type: _values.FormId
    """Value decoded from this schema node."""

    knockdown: float
    """Value decoded from this schema node."""

    recovery_time: float
    """Value decoded from this schema node."""

    stamina_mult: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["damage_mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["attack_chance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_spell"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_flags"]
    ) -> _base.FieldRef[AttackFlags11817]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["attack_angle"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["strike_angle"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["stagger"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_type"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["knockdown"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["recovery_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["stamina_mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Attack11811(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/15:Attacks/repeat/0:Attack"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "attack_data": _base.Binding(
            path="NPC_/15:Attacks/repeat/0:Attack/0:Attack Data",
            kind="subrecord",
            name="Attack Data",
        ),
        "attack_event": _base.Binding(
            path="NPC_/15:Attacks/repeat/0:Attack/1:Attack Event",
            kind="subrecord",
            name="Attack Event",
        ),
    }

    attack_data: Optional[Structure11813] = None
    """Value decoded from this schema node."""

    attack_event: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["attack_data"]
    ) -> _base.FieldRef[Optional[Structure11813]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_event"]
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


class Structure11839(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/21:Perks/repeat/0:Perk/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "perk": _base.Binding(
            path="NPC_/21:Perks/repeat/0:Perk/payload/0:Perk",
            kind="primitive",
            name="Perk",
        ),
        "rank": _base.Binding(
            path="NPC_/21:Perks/repeat/0:Perk/payload/1:Rank",
            kind="primitive",
            name="Rank",
        ),
        "unused": _base.Binding(
            path="NPC_/21:Perks/repeat/0:Perk/payload/2:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    perk: _values.FormId
    """Value decoded from this schema node."""

    rank: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["perk"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rank"]
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


class Structure11848(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/23:Items/repeat/0:Item/0:Item/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path="NPC_/23:Items/repeat/0:Item/0:Item/payload/0:Item",
            kind="primitive",
            name="Item",
        ),
        "count": _base.Binding(
            path=("NPC_/23:Items/repeat/0:Item/0:Item/payload/1:Count"),
            kind="primitive",
            name="Count",
        ),
    }

    item: _values.FormId
    """Value decoded from this schema node."""

    count: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["item"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
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


_VARIANT_11855: _base.Variant = _base.Variant(
    path=(
        "NPC_/23:Items/repeat/0:Item/1:Extra Data/payload/1:Glo"
        "bal Variable / Required Rank/variants/0:Unused"
    )
)


_VARIANT_11856: _base.Variant = _base.Variant(
    path=(
        "NPC_/23:Items/repeat/0:Item/1:Extra Data/payload/1:Glo"
        "bal Variable / Required Rank/variants/1:Global Variabl"
        "e"
    )
)


_VARIANT_11857: _base.Variant = _base.Variant(
    path=(
        "NPC_/23:Items/repeat/0:Item/1:Extra Data/payload/1:Glo"
        "bal Variable / Required Rank/variants/2:Required Rank"
    )
)


class Structure11852(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/23:Items/repeat/0:Item/1:Extra Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path=("NPC_/23:Items/repeat/0:Item/1:Extra Data/payload/0:Owner"),
            kind="primitive",
            name="Owner",
        ),
        "global_variable_required_rank": _base.Binding(
            path=(
                "NPC_/23:Items/repeat/0:Item/1:Extra Data/payload/1:Glo"
                "bal Variable / Required Rank"
            ),
            kind="union",
            name="Global Variable / Required Rank",
        ),
        "item_condition": _base.Binding(
            path=(
                "NPC_/23:Items/repeat/0:Item/1:Extra Data/payload/2:Ite"
                "m Condition"
            ),
            kind="primitive",
            name="Item Condition",
        ),
    }

    owner: _values.FormId
    """Value decoded from this schema node."""

    global_variable_required_rank: (
        Annotated[bytes, _VARIANT_11855]
        | Annotated[_values.FormId, _VARIANT_11856]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11857,
        ]
    )
    """Value decoded from this schema node."""

    item_condition: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["owner"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["global_variable_required_rank"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_11855]
        | Annotated[_values.FormId, _VARIANT_11856]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11857,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["item_condition"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Item11846(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/23:Items/repeat/0:Item"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path="NPC_/23:Items/repeat/0:Item/0:Item",
            kind="subrecord",
            name="Item",
        ),
        "extra_data": _base.Binding(
            path="NPC_/23:Items/repeat/0:Item/1:Extra Data",
            kind="subrecord",
            name="Extra Data",
        ),
    }

    item: Optional[Structure11848] = None
    """Value decoded from this schema node."""

    extra_data: Optional[Structure11852] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["item"]
    ) -> _base.FieldRef[Optional[Structure11848]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["extra_data"]
    ) -> _base.FieldRef[Optional[Structure11852]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Aggression11861(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    UNAGGRESSIVE = 0
    AGGRESSIVE = 1
    VERY_AGGRESSIVE = 2
    FRENZIED = 3


class Confidence11862(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    COWARDLY = 0
    CAUTIOUS = 1
    AVERAGE = 2
    BRAVE = 3
    FOOLHARDY = 4


class Responsibility11864(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ANY_CRIME = 0
    VIOLENCE_AGAINST_ENEMIES = 1
    PROPERTY_CRIME_ONLY = 2
    NO_CRIME = 3


class Mood11865(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NEUTRAL = 0
    ANGRY = 1
    FEAR = 2
    HAPPY = 3
    SAD = 4
    SURPRISED = 5
    PUZZLED = 6
    DISGUSTED = 7


class Assistance11866(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    HELPS_NOBODY = 0
    HELPS_ALLIES = 1
    HELPS_FRIENDS_AND_ALLIES = 2


class AggroRadiusBehavior11868(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Aggro11867(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/24:AI Data/payload/6:Aggro"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aggro_radius_behavior": _base.Binding(
            path=("NPC_/24:AI Data/payload/6:Aggro/0:Aggro Radius Behavior"),
            kind="primitive",
            name="Aggro Radius Behavior",
        ),
        "unused": _base.Binding(
            path="NPC_/24:AI Data/payload/6:Aggro/1:Unused",
            kind="primitive",
            name="Unused",
        ),
        "warn": _base.Binding(
            path="NPC_/24:AI Data/payload/6:Aggro/2:Warn",
            kind="primitive",
            name="Warn",
        ),
        "warn_attack": _base.Binding(
            path="NPC_/24:AI Data/payload/6:Aggro/3:Warn/Attack",
            kind="primitive",
            name="Warn/Attack",
        ),
        "attack": _base.Binding(
            path="NPC_/24:AI Data/payload/6:Aggro/4:Attack",
            kind="primitive",
            name="Attack",
        ),
    }

    aggro_radius_behavior: AggroRadiusBehavior11868
    """Value decoded from this schema node."""

    unused: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    warn: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    warn_attack: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    attack: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["aggro_radius_behavior"]
    ) -> _base.FieldRef[AggroRadiusBehavior11868]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["warn"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["warn_attack"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack"]
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


class Structure11860(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/24:AI Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "aggression": _base.Binding(
            path="NPC_/24:AI Data/payload/0:Aggression",
            kind="primitive",
            name="Aggression",
        ),
        "confidence": _base.Binding(
            path="NPC_/24:AI Data/payload/1:Confidence",
            kind="primitive",
            name="Confidence",
        ),
        "energy_level": _base.Binding(
            path="NPC_/24:AI Data/payload/2:Energy Level",
            kind="primitive",
            name="Energy Level",
        ),
        "responsibility": _base.Binding(
            path="NPC_/24:AI Data/payload/3:Responsibility",
            kind="primitive",
            name="Responsibility",
        ),
        "mood": _base.Binding(
            path="NPC_/24:AI Data/payload/4:Mood",
            kind="primitive",
            name="Mood",
        ),
        "assistance": _base.Binding(
            path="NPC_/24:AI Data/payload/5:Assistance",
            kind="primitive",
            name="Assistance",
        ),
        "aggro": _base.Binding(
            path="NPC_/24:AI Data/payload/6:Aggro",
            kind="struct",
            name="Aggro",
        ),
    }

    aggression: Aggression11861
    """Value decoded from this schema node."""

    confidence: Confidence11862
    """Value decoded from this schema node."""

    energy_level: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    responsibility: Responsibility11864
    """Value decoded from this schema node."""

    mood: Mood11865
    """Value decoded from this schema node."""

    assistance: Assistance11866
    """Value decoded from this schema node."""

    aggro: Aggro11867
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["aggression"]
    ) -> _base.FieldRef[Aggression11861]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["confidence"]
    ) -> _base.FieldRef[Confidence11862]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["energy_level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["responsibility"]
    ) -> _base.FieldRef[Responsibility11864]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["mood"]) -> _base.FieldRef[Mood11865]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["assistance"]
    ) -> _base.FieldRef[Assistance11866]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["aggro"]) -> _base.FieldRef[Aggro11867]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure11890(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/32:Player Skills/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "skill_values": _base.Binding(
            path="NPC_/32:Player Skills/payload/0:Skill Values",
            kind="array",
            name="Skill Values",
        ),
        "skill_offsets": _base.Binding(
            path="NPC_/32:Player Skills/payload/1:Skill Offsets",
            kind="array",
            name="Skill Offsets",
        ),
        "health": _base.Binding(
            path="NPC_/32:Player Skills/payload/2:Health",
            kind="primitive",
            name="Health",
        ),
        "magicka": _base.Binding(
            path="NPC_/32:Player Skills/payload/3:Magicka",
            kind="primitive",
            name="Magicka",
        ),
        "stamina": _base.Binding(
            path="NPC_/32:Player Skills/payload/4:Stamina",
            kind="primitive",
            name="Stamina",
        ),
        "unused": _base.Binding(
            path="NPC_/32:Player Skills/payload/5:Unused",
            kind="primitive",
            name="Unused",
        ),
        "far_away_model_distance": _base.Binding(
            path=("NPC_/32:Player Skills/payload/6:Far away model distance"),
            kind="primitive",
            name="Far away model distance",
        ),
        "geared_up_weapons": _base.Binding(
            path="NPC_/32:Player Skills/payload/7:Geared up weapons",
            kind="primitive",
            name="Geared up weapons",
        ),
        "unused_11901": _base.Binding(
            path="NPC_/32:Player Skills/payload/8:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    skill_values: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...
    ]
    """Value decoded from this schema node."""

    skill_offsets: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...
    ]
    """Value decoded from this schema node."""

    health: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    magicka: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    stamina: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    far_away_model_distance: float
    """Value decoded from this schema node."""

    geared_up_weapons: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused_11901: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["skill_values"]
    ) -> _base.FieldRef[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skill_offsets"]
    ) -> _base.FieldRef[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["health"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["magicka"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stamina"]
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
    def field(
        self, name: Literal["far_away_model_distance"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["geared_up_weapons"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_11901"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LoudNormalSilentVeryLoud11918(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOUD = 0
    NORMAL = 1
    SILENT = 2
    VERY_LOUD = 3


class LeftFootRightFootLeftBackFootRightBacD9Cfb5E211922(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT_FOOT = 0
    RIGHT_FOOT = 1
    LEFT_BACK_FOOT = 2
    RIGHT_BACK_FOOT = 3
    IDLE = 4
    AWARE = 5
    ATTACK = 6
    HIT = 7
    DEATH = 8
    WEAPON = 9
    MOVEMENT_LOOP = 10
    CONSCIOUS_LOOP = 11
    AUXILIARY_1 = 12
    AUXILIARY_2 = 13
    AUXILIARY_3 = 14
    AUXILIARY_4 = 15
    AUXILIARY_5 = 16
    AUXILIARY_6 = 17
    AUXILIARY_7 = 18
    AUXILIARY_8 = 19
    AUXILIARY_8_20 = 20
    JUMP = 21
    PLAY_RANDOM_LOOP = 22


class Sound11924(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/41:Sound Types/repeat/0:Sound Type/1:Sounds/repeat/0:Sound"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "sound": _base.Binding(
            path=(
                "NPC_/41:Sound Types/repeat/0:Sound Type/1:Sounds/repea"
                "t/0:Sound/0:Sound"
            ),
            kind="subrecord",
            name="Sound",
        ),
        "sound_chance": _base.Binding(
            path=(
                "NPC_/41:Sound Types/repeat/0:Sound Type/1:Sounds/repea"
                "t/0:Sound/1:Sound Chance"
            ),
            kind="subrecord",
            name="Sound Chance",
        ),
    }

    sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sound_chance: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sound_chance"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]]
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


class SoundType11920(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/41:Sound Types/repeat/0:Sound Type"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path="NPC_/41:Sound Types/repeat/0:Sound Type/0:Type",
            kind="subrecord",
            name="Type",
        ),
        "sounds": _base.Binding(
            path="NPC_/41:Sound Types/repeat/0:Sound Type/1:Sounds",
            kind="repeat",
            name="Sounds",
            repeated_path=(
                "NPC_/41:Sound Types/repeat/0:Sound Type/1:Sounds/repea"
                "t/0:Sound"
            ),
            child_kind="sequence",
        ),
    }

    type: Optional[LeftFootRightFootLeftBackFootRightBacD9Cfb5E211922] = None
    """Value decoded from this schema node."""

    sounds: tuple[Sound11924, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["type"]
    ) -> _base.FieldRef[
        Optional[LeftFootRightFootLeftBackFootRightBacD9Cfb5E211922]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sounds"]
    ) -> _base.FieldRef[tuple[Sound11924, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure11942(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/48:Texture lighting/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="NPC_/48:Texture lighting/payload/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="NPC_/48:Texture lighting/payload/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="NPC_/48:Texture lighting/payload/2:Blue",
            kind="primitive",
            name="Blue",
        ),
    }

    red: float
    """Value decoded from this schema node."""

    green: float
    """Value decoded from this schema node."""

    blue: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["red"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["green"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["blue"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure11947(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/49:Face morph/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "nose_long_short": _base.Binding(
            path="NPC_/49:Face morph/payload/0:Nose Long/Short",
            kind="primitive",
            name="Nose Long/Short",
        ),
        "nose_up_down": _base.Binding(
            path="NPC_/49:Face morph/payload/1:Nose Up/Down",
            kind="primitive",
            name="Nose Up/Down",
        ),
        "jaw_up_down": _base.Binding(
            path="NPC_/49:Face morph/payload/2:Jaw Up/Down",
            kind="primitive",
            name="Jaw Up/Down",
        ),
        "jaw_narrow_wide": _base.Binding(
            path="NPC_/49:Face morph/payload/3:Jaw Narrow/Wide",
            kind="primitive",
            name="Jaw Narrow/Wide",
        ),
        "jaw_farward_back": _base.Binding(
            path="NPC_/49:Face morph/payload/4:Jaw Farward/Back",
            kind="primitive",
            name="Jaw Farward/Back",
        ),
        "cheeks_up_down": _base.Binding(
            path="NPC_/49:Face morph/payload/5:Cheeks Up/Down",
            kind="primitive",
            name="Cheeks Up/Down",
        ),
        "cheeks_farward_back": _base.Binding(
            path="NPC_/49:Face morph/payload/6:Cheeks Farward/Back",
            kind="primitive",
            name="Cheeks Farward/Back",
        ),
        "eyes_up_down": _base.Binding(
            path="NPC_/49:Face morph/payload/7:Eyes Up/Down",
            kind="primitive",
            name="Eyes Up/Down",
        ),
        "eyes_in_out": _base.Binding(
            path="NPC_/49:Face morph/payload/8:Eyes In/Out",
            kind="primitive",
            name="Eyes In/Out",
        ),
        "brows_up_down": _base.Binding(
            path="NPC_/49:Face morph/payload/9:Brows Up/Down",
            kind="primitive",
            name="Brows Up/Down",
        ),
        "brows_in_out": _base.Binding(
            path="NPC_/49:Face morph/payload/10:Brows In/Out",
            kind="primitive",
            name="Brows In/Out",
        ),
        "brows_farward_back": _base.Binding(
            path="NPC_/49:Face morph/payload/11:Brows Farward/Back",
            kind="primitive",
            name="Brows Farward/Back",
        ),
        "lips_up_down": _base.Binding(
            path="NPC_/49:Face morph/payload/12:Lips Up/Down",
            kind="primitive",
            name="Lips Up/Down",
        ),
        "lips_in_out": _base.Binding(
            path="NPC_/49:Face morph/payload/13:Lips In/Out",
            kind="primitive",
            name="Lips In/Out",
        ),
        "chin_narrow_wide": _base.Binding(
            path="NPC_/49:Face morph/payload/14:Chin Narrow/Wide",
            kind="primitive",
            name="Chin Narrow/Wide",
        ),
        "chin_up_down": _base.Binding(
            path="NPC_/49:Face morph/payload/15:Chin Up/Down",
            kind="primitive",
            name="Chin Up/Down",
        ),
        "chin_underbite_overbite": _base.Binding(
            path=("NPC_/49:Face morph/payload/16:Chin Underbite/Overbite"),
            kind="primitive",
            name="Chin Underbite/Overbite",
        ),
        "eyes_farward_back": _base.Binding(
            path="NPC_/49:Face morph/payload/17:Eyes Farward/Back",
            kind="primitive",
            name="Eyes Farward/Back",
        ),
        "unknown": _base.Binding(
            path="NPC_/49:Face morph/payload/18:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    nose_long_short: float
    """Value decoded from this schema node."""

    nose_up_down: float
    """Value decoded from this schema node."""

    jaw_up_down: float
    """Value decoded from this schema node."""

    jaw_narrow_wide: float
    """Value decoded from this schema node."""

    jaw_farward_back: float
    """Value decoded from this schema node."""

    cheeks_up_down: float
    """Value decoded from this schema node."""

    cheeks_farward_back: float
    """Value decoded from this schema node."""

    eyes_up_down: float
    """Value decoded from this schema node."""

    eyes_in_out: float
    """Value decoded from this schema node."""

    brows_up_down: float
    """Value decoded from this schema node."""

    brows_in_out: float
    """Value decoded from this schema node."""

    brows_farward_back: float
    """Value decoded from this schema node."""

    lips_up_down: float
    """Value decoded from this schema node."""

    lips_in_out: float
    """Value decoded from this schema node."""

    chin_narrow_wide: float
    """Value decoded from this schema node."""

    chin_up_down: float
    """Value decoded from this schema node."""

    chin_underbite_overbite: float
    """Value decoded from this schema node."""

    eyes_farward_back: float
    """Value decoded from this schema node."""

    unknown: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["nose_long_short"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["nose_up_down"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["jaw_up_down"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["jaw_narrow_wide"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["jaw_farward_back"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["cheeks_up_down"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["cheeks_farward_back"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eyes_up_down"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["eyes_in_out"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["brows_up_down"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["brows_in_out"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["brows_farward_back"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["lips_up_down"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["lips_in_out"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["chin_narrow_wide"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["chin_up_down"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["chin_underbite_overbite"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eyes_farward_back"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure11968(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/50:Face parts/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "nose": _base.Binding(
            path="NPC_/50:Face parts/payload/0:Nose",
            kind="primitive",
            name="Nose",
        ),
        "unknown": _base.Binding(
            path="NPC_/50:Face parts/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "eyes": _base.Binding(
            path="NPC_/50:Face parts/payload/2:Eyes",
            kind="primitive",
            name="Eyes",
        ),
        "mouth": _base.Binding(
            path="NPC_/50:Face parts/payload/3:Mouth",
            kind="primitive",
            name="Mouth",
        ),
    }

    nose: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    unknown: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    eyes: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    mouth: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["nose"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["eyes"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["mouth"]
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


class Structure11978(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "NPC_/51:Tint Layers/repeat/0:Layer/1:Tint Color/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "NPC_/51:Tint Layers/repeat/0:Layer/1:Tint Color/payload/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "NPC_/51:Tint Layers/repeat/0:Layer/1:Tint Color/payloa"
                "d/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "NPC_/51:Tint Layers/repeat/0:Layer/1:Tint Color/payload/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "alpha": _base.Binding(
            path=(
                "NPC_/51:Tint Layers/repeat/0:Layer/1:Tint Color/payloa"
                "d/3:Alpha"
            ),
            kind="primitive",
            name="Alpha",
        ),
    }

    red: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    green: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    blue: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    alpha: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
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
    def field(
        self, name: Literal["alpha"]
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


class Layer11974(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_/51:Tint Layers/repeat/0:Layer"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "tint_index": _base.Binding(
            path="NPC_/51:Tint Layers/repeat/0:Layer/0:Tint Index",
            kind="subrecord",
            name="Tint Index",
        ),
        "tint_color": _base.Binding(
            path="NPC_/51:Tint Layers/repeat/0:Layer/1:Tint Color",
            kind="subrecord",
            name="Tint Color",
        ),
        "interpolation_value": _base.Binding(
            path=("NPC_/51:Tint Layers/repeat/0:Layer/2:Interpolation Value"),
            kind="subrecord",
            name="Interpolation Value",
        ),
        "preset": _base.Binding(
            path="NPC_/51:Tint Layers/repeat/0:Layer/3:Preset",
            kind="subrecord",
            name="Preset",
        ),
    }

    tint_index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    tint_color: Optional[Structure11978] = None
    """Value decoded from this schema node."""

    interpolation_value: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    preset: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["tint_index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tint_color"]
    ) -> _base.FieldRef[Optional[Structure11978]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["interpolation_value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["preset"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class NpcRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "NPC_"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "NPC_"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="NPC_/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="NPC_/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "object_bounds": _base.Binding(
            path="NPC_/2:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "configuration": _base.Binding(
            path="NPC_/3:Configuration",
            kind="subrecord",
            name="Configuration",
        ),
        "factions": _base.Binding(
            path="NPC_/4:Factions",
            kind="repeat",
            name="Factions",
            repeated_path="NPC_/4:Factions/repeat/0:Faction",
            child_kind="subrecord",
        ),
        "death_item": _base.Binding(
            path="NPC_/5:Death item",
            kind="subrecord",
            name="Death item",
        ),
        "voice": _base.Binding(
            path="NPC_/6:Voice",
            kind="subrecord",
            name="Voice",
        ),
        "template": _base.Binding(
            path="NPC_/7:Template",
            kind="subrecord",
            name="Template",
        ),
        "race": _base.Binding(
            path="NPC_/8:Race",
            kind="subrecord",
            name="Race",
        ),
        "count": _base.Binding(
            path="NPC_/9:Count",
            kind="subrecord",
            name="Count",
        ),
        "actor_effects": _base.Binding(
            path="NPC_/10:Actor Effects",
            kind="repeat",
            name="Actor Effects",
            repeated_path="NPC_/10:Actor Effects/repeat/0:Actor Effect",
            child_kind="subrecord",
        ),
        "destructible": _base.Binding(
            path="NPC_/11:Destructible",
            kind="sequence",
            name="Destructible",
        ),
        "worn_armor": _base.Binding(
            path="NPC_/12:Worn Armor",
            kind="subrecord",
            name="Worn Armor",
        ),
        "far_away_model": _base.Binding(
            path="NPC_/13:Far away model",
            kind="subrecord",
            name="Far away model",
        ),
        "attack_race": _base.Binding(
            path="NPC_/14:Attack Race",
            kind="subrecord",
            name="Attack Race",
        ),
        "attacks": _base.Binding(
            path="NPC_/15:Attacks",
            kind="repeat",
            name="Attacks",
            repeated_path="NPC_/15:Attacks/repeat/0:Attack",
            child_kind="sequence",
        ),
        "spectator_override_package_list": _base.Binding(
            path="NPC_/16:Spectator override package list",
            kind="subrecord",
            name="Spectator override package list",
        ),
        "observe_dead_body_override_package_list": _base.Binding(
            path="NPC_/17:Observe dead body override package list",
            kind="subrecord",
            name="Observe dead body override package list",
        ),
        "guard_warn_override_package_list": _base.Binding(
            path="NPC_/18:Guard warn override package list",
            kind="subrecord",
            name="Guard warn override package list",
        ),
        "combat_override_package_list": _base.Binding(
            path="NPC_/19:Combat override package list",
            kind="subrecord",
            name="Combat override package list",
        ),
        "perk_count": _base.Binding(
            path="NPC_/20:Perk Count",
            kind="subrecord",
            name="Perk Count",
        ),
        "perks": _base.Binding(
            path="NPC_/21:Perks",
            kind="repeat",
            name="Perks",
            repeated_path="NPC_/21:Perks/repeat/0:Perk",
            child_kind="subrecord",
        ),
        "count_11843": _base.Binding(
            path="NPC_/22:Count",
            kind="subrecord",
            name="Count",
        ),
        "items": _base.Binding(
            path="NPC_/23:Items",
            kind="repeat",
            name="Items",
            repeated_path="NPC_/23:Items/repeat/0:Item",
            child_kind="sequence",
        ),
        "ai_data": _base.Binding(
            path="NPC_/24:AI Data",
            kind="subrecord",
            name="AI Data",
        ),
        "packages": _base.Binding(
            path="NPC_/25:Packages",
            kind="repeat",
            name="Packages",
            repeated_path="NPC_/25:Packages/repeat/0:Package",
            child_kind="subrecord",
        ),
        "keyword_count": _base.Binding(
            path="NPC_/26:Keyword Count",
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path="NPC_/27:Keywords",
            kind="subrecord",
            name="Keywords",
        ),
        "class_value": _base.Binding(
            path="NPC_/28:Class",
            kind="subrecord",
            name="Class",
        ),
        "name": _base.Binding(
            path="NPC_/29:Name",
            kind="subrecord",
            name="Name",
        ),
        "short_name": _base.Binding(
            path="NPC_/30:Short Name",
            kind="subrecord",
            name="Short Name",
        ),
        "marker": _base.Binding(
            path="NPC_/31:Marker",
            kind="subrecord",
            name="Marker",
        ),
        "player_skills": _base.Binding(
            path="NPC_/32:Player Skills",
            kind="subrecord",
            name="Player Skills",
        ),
        "head_parts": _base.Binding(
            path="NPC_/33:Head Parts",
            kind="repeat",
            name="Head Parts",
            repeated_path="NPC_/33:Head Parts/repeat/0:Head Part",
            child_kind="subrecord",
        ),
        "hair_color": _base.Binding(
            path="NPC_/34:Hair Color",
            kind="subrecord",
            name="Hair Color",
        ),
        "combat_style": _base.Binding(
            path="NPC_/35:Combat Style",
            kind="subrecord",
            name="Combat Style",
        ),
        "gift_filter": _base.Binding(
            path="NPC_/36:Gift Filter",
            kind="subrecord",
            name="Gift Filter",
        ),
        "unknown": _base.Binding(
            path="NPC_/37:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "height": _base.Binding(
            path="NPC_/38:Height",
            kind="subrecord",
            name="Height",
        ),
        "weight": _base.Binding(
            path="NPC_/39:Weight",
            kind="subrecord",
            name="Weight",
        ),
        "sound_level": _base.Binding(
            path="NPC_/40:Sound Level",
            kind="subrecord",
            name="Sound Level",
        ),
        "sound_types": _base.Binding(
            path="NPC_/41:Sound Types",
            kind="repeat",
            name="Sound Types",
            repeated_path="NPC_/41:Sound Types/repeat/0:Sound Type",
            child_kind="sequence",
        ),
        "inherits_sounds_from": _base.Binding(
            path="NPC_/42:Inherits Sounds From",
            kind="subrecord",
            name="Inherits Sounds From",
        ),
        "default_outfit": _base.Binding(
            path="NPC_/43:Default outfit",
            kind="subrecord",
            name="Default outfit",
        ),
        "sleeping_outfit": _base.Binding(
            path="NPC_/44:Sleeping outfit",
            kind="subrecord",
            name="Sleeping outfit",
        ),
        "default_package_list": _base.Binding(
            path="NPC_/45:Default Package List",
            kind="subrecord",
            name="Default Package List",
        ),
        "crime_faction": _base.Binding(
            path="NPC_/46:Crime faction",
            kind="subrecord",
            name="Crime faction",
        ),
        "head_texture": _base.Binding(
            path="NPC_/47:Head texture",
            kind="subrecord",
            name="Head texture",
        ),
        "texture_lighting": _base.Binding(
            path="NPC_/48:Texture lighting",
            kind="subrecord",
            name="Texture lighting",
        ),
        "face_morph": _base.Binding(
            path="NPC_/49:Face morph",
            kind="subrecord",
            name="Face morph",
        ),
        "face_parts": _base.Binding(
            path="NPC_/50:Face parts",
            kind="subrecord",
            name="Face parts",
        ),
        "tint_layers": _base.Binding(
            path="NPC_/51:Tint Layers",
            kind="repeat",
            name="Tint Layers",
            repeated_path="NPC_/51:Tint Layers/repeat/0:Layer",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure11650] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure11696] = None
    """Value decoded from this schema node."""

    configuration: Optional[Structure11704] = None
    """Value decoded from this schema node."""

    factions: tuple[Structure11720, ...] = ()
    """Value decoded from this schema node."""

    death_item: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    voice: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    template: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    race: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    actor_effects: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    destructible: Optional[Destructible11737] = None
    """Value decoded from this schema node."""

    worn_armor: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    far_away_model: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    attack_race: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    attacks: tuple[Attack11811, ...] = ()
    """Value decoded from this schema node."""

    spectator_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    observe_dead_body_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    guard_warn_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    combat_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    perk_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    perks: tuple[Structure11839, ...] = ()
    """Value decoded from this schema node."""

    count_11843: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    items: tuple[Item11846, ...] = ()
    """Value decoded from this schema node."""

    ai_data: Optional[Structure11860] = None
    """Value decoded from this schema node."""

    packages: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    class_value: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    short_name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    player_skills: Optional[Structure11890] = None
    """Value decoded from this schema node."""

    head_parts: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    hair_color: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    combat_style: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    gift_filter: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    height: Optional[float] = None
    """Value decoded from this schema node."""

    weight: Optional[float] = None
    """Value decoded from this schema node."""

    sound_level: Optional[LoudNormalSilentVeryLoud11918] = None
    """Value decoded from this schema node."""

    sound_types: tuple[SoundType11920, ...] = ()
    """Value decoded from this schema node."""

    inherits_sounds_from: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    default_outfit: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sleeping_outfit: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    default_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    crime_faction: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    head_texture: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    texture_lighting: Optional[Structure11942] = None
    """Value decoded from this schema node."""

    face_morph: Optional[Structure11947] = None
    """Value decoded from this schema node."""

    face_parts: Optional[Structure11968] = None
    """Value decoded from this schema node."""

    tint_layers: tuple[Layer11974, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure11650]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[Structure11696]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["configuration"]
    ) -> _base.FieldRef[Optional[Structure11704]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["factions"]
    ) -> _base.FieldRef[tuple[Structure11720, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["death_item"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["voice"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["template"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["race"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actor_effects"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["destructible"]
    ) -> _base.FieldRef[Optional[Destructible11737]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["worn_armor"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["far_away_model"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_race"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attacks"]
    ) -> _base.FieldRef[tuple[Attack11811, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["spectator_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["observe_dead_body_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["guard_warn_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["combat_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perk_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perks"]
    ) -> _base.FieldRef[tuple[Structure11839, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count_11843"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["items"]
    ) -> _base.FieldRef[tuple[Item11846, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ai_data"]
    ) -> _base.FieldRef[Optional[Structure11860]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["packages"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
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
        self, name: Literal["class_value"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
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
        self, name: Literal["short_name"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["marker"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["player_skills"]
    ) -> _base.FieldRef[Optional[Structure11890]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head_parts"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hair_color"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["combat_style"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["gift_filter"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["height"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["weight"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sound_level"]
    ) -> _base.FieldRef[Optional[LoudNormalSilentVeryLoud11918]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sound_types"]
    ) -> _base.FieldRef[tuple[SoundType11920, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["inherits_sounds_from"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_outfit"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sleeping_outfit"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["crime_faction"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head_texture"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["texture_lighting"]
    ) -> _base.FieldRef[Optional[Structure11942]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["face_morph"]
    ) -> _base.FieldRef[Optional[Structure11947]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["face_parts"]
    ) -> _base.FieldRef[Optional[Structure11968]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["tint_layers"]
    ) -> _base.FieldRef[tuple[Layer11974, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
