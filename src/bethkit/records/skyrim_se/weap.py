"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags17103(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type17107(_values.OpenIntEnum):
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


class Flags17108(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_17110: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV217112(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_17112: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV117116(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_17116: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_17111: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_17120: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_17121: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_17122: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool17123(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_17123: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV217126(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_17126: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV117130(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_17130: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_17124: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_17134: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_17136: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_17138: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element17141(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_17140: _base.Variant = _base.Variant(
    path=(
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property17105(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type17107
    """Value decoded from this schema node."""

    flags: Flags17108
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_17110]
        | Annotated[
            Annotated[ObjectV217112, _VARIANT_17112]
            | Annotated[ObjectV117116, _VARIANT_17116],
            _VARIANT_17111,
        ]
        | Annotated[str, _VARIANT_17120]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_17121,
        ]
        | Annotated[float, _VARIANT_17122]
        | Annotated[Bool17123, _VARIANT_17123]
        | Annotated[
            tuple[
                Annotated[ObjectV217126, _VARIANT_17126]
                | Annotated[ObjectV117130, _VARIANT_17130],
                ...,
            ],
            _VARIANT_17124,
        ]
        | Annotated[tuple[str, ...], _VARIANT_17134]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_17136,
        ]
        | Annotated[tuple[float, ...], _VARIANT_17138]
        | Annotated[tuple[Element17141, ...], _VARIANT_17140]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type17107]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags17108]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_17110]
        | Annotated[
            Annotated[ObjectV217112, _VARIANT_17112]
            | Annotated[ObjectV117116, _VARIANT_17116],
            _VARIANT_17111,
        ]
        | Annotated[str, _VARIANT_17120]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_17121,
        ]
        | Annotated[float, _VARIANT_17122]
        | Annotated[Bool17123, _VARIANT_17123]
        | Annotated[
            tuple[
                Annotated[ObjectV217126, _VARIANT_17126]
                | Annotated[ObjectV117130, _VARIANT_17130],
                ...,
            ],
            _VARIANT_17124,
        ]
        | Annotated[tuple[str, ...], _VARIANT_17134]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_17136,
        ]
        | Annotated[tuple[float, ...], _VARIANT_17138]
        | Annotated[tuple[Element17141, ...], _VARIANT_17140]
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


class Script17101(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "WEAP/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags17103
    """Value decoded from this schema node."""

    properties: tuple[Property17105, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags17103]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property17105, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17097(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="WEAP/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("WEAP/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="WEAP/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script17101, ...]
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
    ) -> _base.FieldRef[tuple[Script17101, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17143(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/2:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="WEAP/2:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="WEAP/2:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="WEAP/2:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="WEAP/2:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="WEAP/2:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="WEAP/2:Object Bounds/payload/5:Z2",
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


class Structure17157(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17159": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17160": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17161": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_17159: bytes
    """Value decoded from this schema node."""

    unused_17160: bytes
    """Value decoded from this schema node."""

    unused_17161: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17159"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17160"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17161"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17157: _base.Variant = _base.Variant(
    path=("WEAP/4:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure17162(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_17165": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17166": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/1:St"
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

    unused_17165: bytes
    """Value decoded from this schema node."""

    unused_17166: bytes
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
    def field(self, name: Literal["unused_17165"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17166"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17162: _base.Variant = _base.Variant(
    path=("WEAP/4:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture17170(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/2:St"
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


class Structure17167(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_17174": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17175": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture17170, ...]
    """Value decoded from this schema node."""

    unused_17174: bytes
    """Value decoded from this schema node."""

    unused_17175: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture17170, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17174"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17175"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17167: _base.Variant = _base.Variant(
    path=("WEAP/4:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture17180(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
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


class Material17187(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
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


class Structure17176(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "WEAP/4:Model/1:Model Information/payload/variants/3:St"
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

    textures: tuple[Texture17180, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material17187, ...]
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
    ) -> _base.FieldRef[tuple[Texture17180, ...]]:
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
    ) -> _base.FieldRef[tuple[Material17187, ...]]:
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


_VARIANT_17176: _base.Variant = _base.Variant(
    path=("WEAP/4:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture17194(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/4:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "WEAP/4:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "WEAP/4:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "WEAP/4:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model17152(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/4:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="WEAP/4:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="WEAP/4:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="WEAP/4:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure17157, _VARIANT_17157]
        | Annotated[Structure17162, _VARIANT_17162]
        | Annotated[Structure17167, _VARIANT_17167]
        | Annotated[Structure17176, _VARIANT_17176]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture17194, ...]] = None
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
            Annotated[Structure17157, _VARIANT_17157]
            | Annotated[Structure17162, _VARIANT_17162]
            | Annotated[Structure17167, _VARIANT_17167]
            | Annotated[Structure17176, _VARIANT_17176]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture17194, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Icon17198(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/5:Icon"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "large_icon_file_name": _base.Binding(
            path="WEAP/5:Icon/0:Large Icon FileName",
            kind="subrecord",
            name="Large Icon FileName",
        ),
        "small_icon_file_name": _base.Binding(
            path="WEAP/5:Icon/1:Small Icon FileName",
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


class VatsTargetable17212(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure17209(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/8:Destructible/0:Header/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path="WEAP/8:Destructible/0:Header/payload/0:Health",
            kind="primitive",
            name="Health",
        ),
        "dest_count": _base.Binding(
            path="WEAP/8:Destructible/0:Header/payload/1:DEST Count",
            kind="primitive",
            name="DEST Count",
        ),
        "vats_targetable": _base.Binding(
            path=("WEAP/8:Destructible/0:Header/payload/2:VATS Targetable"),
            kind="primitive",
            name="VATS Targetable",
        ),
        "unknown": _base.Binding(
            path="WEAP/8:Destructible/0:Header/payload/3:Unknown",
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

    vats_targetable: VatsTargetable17212
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
    ) -> _base.FieldRef[VatsTargetable17212]:
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


class Flags17221(enum.IntFlag):
    """Named values from the pinned schema."""

    CAP_DAMAGE = 1
    DISABLE = 2
    DESTROY = 4
    IGNORE_EXTERNAL_DMG = 8


class Structure17217(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
        "ion Stage Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/0:Health %"
            ),
            kind="primitive",
            name="Health %",
        ),
        "index": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/1:Index"
            ),
            kind="primitive",
            name="Index",
        ),
        "model_damage_stage_value": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/2:Model Damage Stage"
            ),
            kind="primitive",
            name="Model Damage Stage",
        ),
        "flags": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/3:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "self_damage_per_second": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/4:Self Damage per Second"
            ),
            kind="primitive",
            name="Self Damage per Second",
        ),
        "explosion": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/5:Explosion"
            ),
            kind="primitive",
            name="Explosion",
        ),
        "debris": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/6:Debris"
            ),
            kind="primitive",
            name="Debris",
        ),
        "debris_count": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
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

    flags: Flags17221
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags17221]:
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


class Structure17231(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17233": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/1:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17234": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17235": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_17233: bytes
    """Value decoded from this schema node."""

    unused_17234: bytes
    """Value decoded from this schema node."""

    unused_17235: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17233"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17234"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17235"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17231: _base.Variant = _base.Variant(
    path=(
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
)


class Structure17236(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_17239": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17240": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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

    unused_17239: bytes
    """Value decoded from this schema node."""

    unused_17240: bytes
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
    def field(self, name: Literal["unused_17239"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17240"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17236: _base.Variant = _base.Variant(
    path=(
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
)


class Texture17244(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Structure17241(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_17248": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17249": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture17244, ...]
    """Value decoded from this schema node."""

    unused_17248: bytes
    """Value decoded from this schema node."""

    unused_17249: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture17244, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17248"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17249"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17241: _base.Variant = _base.Variant(
    path=(
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
)


class Texture17254(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Material17261(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/3:Mater"
        "ials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Structure17250(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/0:Heade"
                "rs"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/2:Addon"
                "s"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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

    textures: tuple[Texture17254, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material17261, ...]
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
    ) -> _base.FieldRef[tuple[Texture17254, ...]]:
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
    ) -> _base.FieldRef[tuple[Material17261, ...]]:
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


_VARIANT_17250: _base.Variant = _base.Variant(
    path=(
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
)


class AlternateTexture17268(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
        "Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
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


class Model17226(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/0:"
                "Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure17231, _VARIANT_17231]
        | Annotated[Structure17236, _VARIANT_17236]
        | Annotated[Structure17241, _VARIANT_17241]
        | Annotated[Structure17250, _VARIANT_17250]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture17268, ...]] = None
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
            Annotated[Structure17231, _VARIANT_17231]
            | Annotated[Structure17236, _VARIANT_17236]
            | Annotated[Structure17241, _VARIANT_17241]
            | Annotated[Structure17250, _VARIANT_17250]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture17268, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Stage17215(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/8:Destructible/1:Stages/repeat/0:Stage"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "destruction_stage_data": _base.Binding(
            path=(
                "WEAP/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data"
            ),
            kind="subrecord",
            name="Destruction Stage Data",
        ),
        "model": _base.Binding(
            path=("WEAP/8:Destructible/1:Stages/repeat/0:Stage/1:Model"),
            kind="sequence",
            name="Model",
        ),
        "end_marker": _base.Binding(
            path=("WEAP/8:Destructible/1:Stages/repeat/0:Stage/2:End Marker"),
            kind="subrecord",
            name="End Marker",
        ),
    }

    destruction_stage_data: Optional[Structure17217] = None
    """Value decoded from this schema node."""

    model: Optional[Model17226] = None
    """Value decoded from this schema node."""

    end_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["destruction_stage_data"]
    ) -> _base.FieldRef[Optional[Structure17217]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model17226]]:
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


class Destructible17207(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/8:Destructible"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="WEAP/8:Destructible/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "stages": _base.Binding(
            path="WEAP/8:Destructible/1:Stages",
            kind="repeat",
            name="Stages",
            repeated_path="WEAP/8:Destructible/1:Stages/repeat/0:Stage",
            child_kind="sequence",
        ),
    }

    header: Optional[Structure17209] = None
    """Value decoded from this schema node."""

    stages: tuple[Stage17215, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure17209]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stages"]
    ) -> _base.FieldRef[tuple[Stage17215, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17296(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/0:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17298": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/0:Structure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17299": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/0:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17300": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/0:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_17298: bytes
    """Value decoded from this schema node."""

    unused_17299: bytes
    """Value decoded from this schema node."""

    unused_17300: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17298"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17299"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17300"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17296: _base.Variant = _base.Variant(
    path=("WEAP/17:Has Scope/1:Model Information/payload/variants/0:Structure")
)


class Structure17301(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/1:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_17304": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/1:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17305": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/1:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    error: bytes
    """Value decoded from this schema node."""

    unused_17304: bytes
    """Value decoded from this schema node."""

    unused_17305: bytes
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
    def field(self, name: Literal["unused_17304"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17305"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17301: _base.Variant = _base.Variant(
    path=("WEAP/17:Has Scope/1:Model Information/payload/variants/1:Structure")
)


class Texture17309(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/1:Model Information/payload/variants"
        "/2:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/2:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/2:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/2:Structure/1:Textures/element/2:Folder Hash"
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


class Structure17306(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/2:Structure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/2:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_17313": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/2:Structure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_17314": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/2:Structure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture17309, ...]
    """Value decoded from this schema node."""

    unused_17313: bytes
    """Value decoded from this schema node."""

    unused_17314: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture17309, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17313"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17314"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_17306: _base.Variant = _base.Variant(
    path=("WEAP/17:Has Scope/1:Model Information/payload/variants/2:Structure")
)


class Texture17319(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/1:Model Information/payload/variants"
        "/3:Structure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/1:Textures/element/2:Folder Hash"
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


class Material17326(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/1:Model Information/payload/variants"
        "/3:Structure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/3:Materials/element/2:Folder Hash"
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


class Structure17315(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "WEAP/17:Has Scope/1:Model Information/payload/variants"
                "/3:Structure/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    headers: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    textures: tuple[Texture17319, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material17326, ...]
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
    ) -> _base.FieldRef[tuple[Texture17319, ...]]:
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
    ) -> _base.FieldRef[tuple[Material17326, ...]]:
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


_VARIANT_17315: _base.Variant = _base.Variant(
    path=("WEAP/17:Has Scope/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture17333(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "WEAP/17:Has Scope/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "WEAP/17:Has Scope/2:Alternate Textures/payload/element"
                "/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "WEAP/17:Has Scope/2:Alternate Textures/payload/element"
                "/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "WEAP/17:Has Scope/2:Alternate Textures/payload/element"
                "/2:3D Index"
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


class HasScope17291(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/17:Has Scope"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="WEAP/17:Has Scope/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="WEAP/17:Has Scope/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="WEAP/17:Has Scope/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure17296, _VARIANT_17296]
        | Annotated[Structure17301, _VARIANT_17301]
        | Annotated[Structure17306, _VARIANT_17306]
        | Annotated[Structure17315, _VARIANT_17315]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture17333, ...]] = None
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
            Annotated[Structure17296, _VARIANT_17296]
            | Annotated[Structure17301, _VARIANT_17301]
            | Annotated[Structure17306, _VARIANT_17306]
            | Annotated[Structure17315, _VARIANT_17315]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture17333, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure17358(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/28:Game Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value": _base.Binding(
            path="WEAP/28:Game Data/payload/0:Value",
            kind="primitive",
            name="Value",
        ),
        "weight": _base.Binding(
            path="WEAP/28:Game Data/payload/1:Weight",
            kind="primitive",
            name="Weight",
        ),
        "damage": _base.Binding(
            path="WEAP/28:Game Data/payload/2:Damage",
            kind="primitive",
            name="Damage",
        ),
    }

    value: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    weight: float
    """Value decoded from this schema node."""

    damage: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
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
    def field(
        self, name: Literal["damage"]
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


class AnimationType17364(_values.OpenIntEnum):
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


class Flags17368(enum.IntFlag):
    """Named values from the pinned schema."""

    IGNORES_NORMAL_WEAPON_RESISTANCE = 1
    AUTOMATIC_UNUSED = 2
    HAS_SCOPE_UNUSED = 4
    CAN_T_DROP = 8
    HIDE_BACKPACK_UNUSED = 16
    EMBEDDED_WEAPON_UNUSED = 32
    DON_T_USE_1ST_PERSON_IS_ANIM_UNUSED = 64
    NON_PLAYABLE = 128


class AttackAnimation17373(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ATTACK_LEFT = 26
    ATTACK_RIGHT = 32
    ATTACK3 = 38
    ATTACK4 = 44
    ATTACK5 = 50
    ATTACK6 = 56
    ATTACK7 = 62
    ATTACK8 = 68
    ATTACK_LOOP = 74
    ATTACK_SPIN = 80
    ATTACK_SPIN2 = 86
    PLACE_MINE = 97
    PLACE_MINE2 = 103
    ATTACK_THROW = 109
    ATTACK_THROW2 = 115
    ATTACK_THROW3 = 121
    ATTACK_THROW4 = 127
    ATTACK_THROW5 = 133
    DEFAULT = 255


class OnHit17378(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NO_FORMULA_BEHAVIOUR = 0
    DISMEMBER_ONLY = 1
    EXPLODE_ONLY = 2
    NO_DISMEMBER_EXPLODE = 3


class Flags217379(enum.IntFlag):
    """Named values from the pinned schema."""

    PLAYER_ONLY = 1
    NPCS_USE_AMMO = 2
    NO_JAM_AFTER_RELOAD_UNUSED = 4
    UNKNOWN_4 = 8
    MINOR_CRIME = 16
    RANGE_FIXED = 32
    NOT_USED_IN_NORMAL_COMBAT = 64
    UNKNOWN_8 = 128
    DON_T_USE_3RD_PERSON_IS_ANIM_UNUSED = 256
    BURST_SHOT = 512
    RUMBLE_ALTERNATE = 1024
    LONG_BURSTS = 2048
    NON_HOSTILE = 4096
    BOUND_WEAPON = 8192


class Skill17386(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    UNKNOWN_1 = 0
    UNKNOWN_2 = 1
    UNKNOWN_3 = 2
    UNKNOWN_4 = 3
    UNKNOWN_5 = 4
    UNKNOWN_6 = 5
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


class Resist17388(_values.OpenIntEnum):
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


class Structure17363(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/29:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "animation_type": _base.Binding(
            path="WEAP/29:Data/payload/0:Animation Type",
            kind="primitive",
            name="Animation Type",
        ),
        "unused": _base.Binding(
            path="WEAP/29:Data/payload/1:Unused",
            kind="primitive",
            name="Unused",
        ),
        "speed": _base.Binding(
            path="WEAP/29:Data/payload/2:Speed",
            kind="primitive",
            name="Speed",
        ),
        "reach": _base.Binding(
            path="WEAP/29:Data/payload/3:Reach",
            kind="primitive",
            name="Reach",
        ),
        "flags": _base.Binding(
            path="WEAP/29:Data/payload/4:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unused_17369": _base.Binding(
            path="WEAP/29:Data/payload/5:Unused",
            kind="primitive",
            name="Unused",
        ),
        "sight_fov": _base.Binding(
            path="WEAP/29:Data/payload/6:Sight FOV",
            kind="primitive",
            name="Sight FOV",
        ),
        "unknown": _base.Binding(
            path="WEAP/29:Data/payload/7:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "base_vats_to_hit_chance": _base.Binding(
            path="WEAP/29:Data/payload/8:Base VATS To-Hit Chance",
            kind="primitive",
            name="Base VATS To-Hit Chance",
        ),
        "attack_animation": _base.Binding(
            path="WEAP/29:Data/payload/9:Attack Animation",
            kind="primitive",
            name="Attack Animation",
        ),
        "projectiles": _base.Binding(
            path="WEAP/29:Data/payload/10:# Projectiles",
            kind="primitive",
            name="# Projectiles",
        ),
        "embedded_weapon_av_unused": _base.Binding(
            path=("WEAP/29:Data/payload/11:Embedded Weapon AV (unused)"),
            kind="primitive",
            name="Embedded Weapon AV (unused)",
        ),
        "range_min": _base.Binding(
            path="WEAP/29:Data/payload/12:Range Min",
            kind="primitive",
            name="Range Min",
        ),
        "range_max": _base.Binding(
            path="WEAP/29:Data/payload/13:Range Max",
            kind="primitive",
            name="Range Max",
        ),
        "on_hit": _base.Binding(
            path="WEAP/29:Data/payload/14:On Hit",
            kind="primitive",
            name="On Hit",
        ),
        "flags2": _base.Binding(
            path="WEAP/29:Data/payload/15:Flags2",
            kind="primitive",
            name="Flags2",
        ),
        "animation_attack_mult": _base.Binding(
            path="WEAP/29:Data/payload/16:Animation Attack Mult",
            kind="primitive",
            name="Animation Attack Mult",
        ),
        "unknown_17381": _base.Binding(
            path="WEAP/29:Data/payload/17:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "rumble_left_motor_strength": _base.Binding(
            path=("WEAP/29:Data/payload/18:Rumble - Left Motor Strength"),
            kind="primitive",
            name="Rumble - Left Motor Strength",
        ),
        "rumble_right_motor_strength": _base.Binding(
            path=("WEAP/29:Data/payload/19:Rumble - Right Motor Strength"),
            kind="primitive",
            name="Rumble - Right Motor Strength",
        ),
        "rumble_duration": _base.Binding(
            path="WEAP/29:Data/payload/20:Rumble - Duration",
            kind="primitive",
            name="Rumble - Duration",
        ),
        "unknown_17385": _base.Binding(
            path="WEAP/29:Data/payload/21:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "skill": _base.Binding(
            path="WEAP/29:Data/payload/22:Skill",
            kind="primitive",
            name="Skill",
        ),
        "unknown_17387": _base.Binding(
            path="WEAP/29:Data/payload/23:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "resist": _base.Binding(
            path="WEAP/29:Data/payload/24:Resist",
            kind="primitive",
            name="Resist",
        ),
        "unknown_17389": _base.Binding(
            path="WEAP/29:Data/payload/25:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "stagger": _base.Binding(
            path="WEAP/29:Data/payload/26:Stagger",
            kind="primitive",
            name="Stagger",
        ),
    }

    animation_type: AnimationType17364
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    speed: float
    """Value decoded from this schema node."""

    reach: float
    """Value decoded from this schema node."""

    flags: Flags17368
    """Value decoded from this schema node."""

    unused_17369: bytes
    """Value decoded from this schema node."""

    sight_fov: float
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    base_vats_to_hit_chance: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    attack_animation: AttackAnimation17373
    """Value decoded from this schema node."""

    projectiles: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    embedded_weapon_av_unused: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    range_min: float
    """Value decoded from this schema node."""

    range_max: float
    """Value decoded from this schema node."""

    on_hit: OnHit17378
    """Value decoded from this schema node."""

    flags2: Flags217379
    """Value decoded from this schema node."""

    animation_attack_mult: float
    """Value decoded from this schema node."""

    unknown_17381: float
    """Value decoded from this schema node."""

    rumble_left_motor_strength: float
    """Value decoded from this schema node."""

    rumble_right_motor_strength: float
    """Value decoded from this schema node."""

    rumble_duration: float
    """Value decoded from this schema node."""

    unknown_17385: bytes
    """Value decoded from this schema node."""

    skill: Skill17386
    """Value decoded from this schema node."""

    unknown_17387: bytes
    """Value decoded from this schema node."""

    resist: Resist17388
    """Value decoded from this schema node."""

    unknown_17389: bytes
    """Value decoded from this schema node."""

    stagger: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["animation_type"]
    ) -> _base.FieldRef[AnimationType17364]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["speed"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["reach"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags17368]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17369"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sight_fov"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base_vats_to_hit_chance"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_animation"]
    ) -> _base.FieldRef[AttackAnimation17373]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["projectiles"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["embedded_weapon_av_unused"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["range_min"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["range_max"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["on_hit"]) -> _base.FieldRef[OnHit17378]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags2"]) -> _base.FieldRef[Flags217379]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["animation_attack_mult"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17381"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rumble_left_motor_strength"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rumble_right_motor_strength"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rumble_duration"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17385"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["skill"]) -> _base.FieldRef[Skill17386]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17387"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["resist"]) -> _base.FieldRef[Resist17388]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_17389"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["stagger"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags17396(enum.IntFlag):
    """Named values from the pinned schema."""

    ON_DEATH = 1


class Structure17392(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP/30:Critical Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "damage": _base.Binding(
            path="WEAP/30:Critical Data/payload/0:Damage",
            kind="primitive",
            name="Damage",
        ),
        "unused": _base.Binding(
            path="WEAP/30:Critical Data/payload/1:Unused",
            kind="primitive",
            name="Unused",
        ),
        "mult": _base.Binding(
            path="WEAP/30:Critical Data/payload/2:% Mult",
            kind="primitive",
            name="% Mult",
        ),
        "flags": _base.Binding(
            path="WEAP/30:Critical Data/payload/3:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unused_17397": _base.Binding(
            path="WEAP/30:Critical Data/payload/4:Unused",
            kind="primitive",
            name="Unused",
        ),
        "effect": _base.Binding(
            path="WEAP/30:Critical Data/payload/5:Effect",
            kind="primitive",
            name="Effect",
        ),
        "unused_17399": _base.Binding(
            path="WEAP/30:Critical Data/payload/6:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    damage: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    mult: float
    """Value decoded from this schema node."""

    flags: Flags17396
    """Value decoded from this schema node."""

    unused_17397: bytes
    """Value decoded from this schema node."""

    effect: _values.FormId
    """Value decoded from this schema node."""

    unused_17399: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["damage"]
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
    def field(self, name: Literal["mult"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags17396]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17397"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["effect"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_17399"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LoudNormalSilentVeryLoud17401(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOUD = 0
    NORMAL = 1
    SILENT = 2
    VERY_LOUD = 3


class WeaponRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "WEAP"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "WEAP"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="WEAP/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="WEAP/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "object_bounds": _base.Binding(
            path="WEAP/2:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "name": _base.Binding(
            path="WEAP/3:Name",
            kind="subrecord",
            name="Name",
        ),
        "model": _base.Binding(
            path="WEAP/4:Model",
            kind="unordered",
            name="Model",
        ),
        "icon": _base.Binding(
            path="WEAP/5:Icon",
            kind="unordered",
            name="Icon",
        ),
        "object_effect": _base.Binding(
            path="WEAP/6:Object Effect",
            kind="subrecord",
            name="Object Effect",
        ),
        "enchantment_amount": _base.Binding(
            path="WEAP/7:Enchantment Amount",
            kind="subrecord",
            name="Enchantment Amount",
        ),
        "destructible": _base.Binding(
            path="WEAP/8:Destructible",
            kind="sequence",
            name="Destructible",
        ),
        "equipment_type": _base.Binding(
            path="WEAP/9:Equipment Type",
            kind="subrecord",
            name="Equipment Type",
        ),
        "block_bash_impact_data_set": _base.Binding(
            path="WEAP/10:Block Bash Impact Data Set",
            kind="subrecord",
            name="Block Bash Impact Data Set",
        ),
        "alternate_block_material": _base.Binding(
            path="WEAP/11:Alternate Block Material",
            kind="subrecord",
            name="Alternate Block Material",
        ),
        "sound_pick_up": _base.Binding(
            path="WEAP/12:Sound - Pick Up",
            kind="subrecord",
            name="Sound - Pick Up",
        ),
        "sound_put_down": _base.Binding(
            path="WEAP/13:Sound - Put Down",
            kind="subrecord",
            name="Sound - Put Down",
        ),
        "keyword_count": _base.Binding(
            path="WEAP/14:Keyword Count",
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path="WEAP/15:Keywords",
            kind="subrecord",
            name="Keywords",
        ),
        "description": _base.Binding(
            path="WEAP/16:Description",
            kind="subrecord",
            name="Description",
        ),
        "has_scope": _base.Binding(
            path="WEAP/17:Has Scope",
            kind="sequence",
            name="Has Scope",
        ),
        "unused": _base.Binding(
            path="WEAP/18:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "impact_data_set": _base.Binding(
            path="WEAP/19:Impact Data Set",
            kind="subrecord",
            name="Impact Data Set",
        ),
        "value_1st_person_model_object": _base.Binding(
            path="WEAP/20:1st Person Model Object",
            kind="subrecord",
            name="1st Person Model Object",
        ),
        "attack_sound": _base.Binding(
            path="WEAP/21:Attack Sound",
            kind="subrecord",
            name="Attack Sound",
        ),
        "attack_sound_2_d": _base.Binding(
            path="WEAP/22:Attack Sound 2D",
            kind="subrecord",
            name="Attack Sound 2D",
        ),
        "attack_loop_sound": _base.Binding(
            path="WEAP/23:Attack Loop Sound",
            kind="subrecord",
            name="Attack Loop Sound",
        ),
        "attack_fail_sound": _base.Binding(
            path="WEAP/24:Attack Fail Sound",
            kind="subrecord",
            name="Attack Fail Sound",
        ),
        "idle_sound": _base.Binding(
            path="WEAP/25:Idle Sound",
            kind="subrecord",
            name="Idle Sound",
        ),
        "equip_sound": _base.Binding(
            path="WEAP/26:Equip Sound",
            kind="subrecord",
            name="Equip Sound",
        ),
        "unequip_sound": _base.Binding(
            path="WEAP/27:Unequip Sound",
            kind="subrecord",
            name="Unequip Sound",
        ),
        "game_data": _base.Binding(
            path="WEAP/28:Game Data",
            kind="subrecord",
            name="Game Data",
        ),
        "data": _base.Binding(
            path="WEAP/29:Data",
            kind="subrecord",
            name="Data",
        ),
        "critical_data": _base.Binding(
            path="WEAP/30:Critical Data",
            kind="subrecord",
            name="Critical Data",
        ),
        "detection_sound_level": _base.Binding(
            path="WEAP/31:Detection Sound Level",
            kind="subrecord",
            name="Detection Sound Level",
        ),
        "template": _base.Binding(
            path="WEAP/32:Template",
            kind="subrecord",
            name="Template",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure17097] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure17143] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    model: Optional[Model17152] = None
    """Value decoded from this schema node."""

    icon: Optional[Icon17198] = None
    """Value decoded from this schema node."""

    object_effect: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    enchantment_amount: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    destructible: Optional[Destructible17207] = None
    """Value decoded from this schema node."""

    equipment_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    block_bash_impact_data_set: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alternate_block_material: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sound_pick_up: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sound_put_down: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    has_scope: Optional[HasScope17291] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    impact_data_set: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    value_1st_person_model_object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    attack_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    attack_sound_2_d: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    attack_loop_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    attack_fail_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    idle_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    equip_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unequip_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    game_data: Optional[Structure17358] = None
    """Value decoded from this schema node."""

    data: Optional[Structure17363] = None
    """Value decoded from this schema node."""

    critical_data: Optional[Structure17392] = None
    """Value decoded from this schema node."""

    detection_sound_level: Optional[LoudNormalSilentVeryLoud17401] = None
    """Value decoded from this schema node."""

    template: Optional[_values.FormId] = None
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
    ) -> _base.FieldRef[Optional[Structure17097]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[Structure17143]]:
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
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model17152]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["icon"]
    ) -> _base.FieldRef[Optional[Icon17198]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_effect"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enchantment_amount"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["destructible"]
    ) -> _base.FieldRef[Optional[Destructible17207]]:
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
        self, name: Literal["block_bash_impact_data_set"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_block_material"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
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
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["has_scope"]
    ) -> _base.FieldRef[Optional[HasScope17291]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["impact_data_set"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value_1st_person_model_object"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_sound_2_d"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_loop_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attack_fail_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["idle_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equip_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unequip_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["game_data"]
    ) -> _base.FieldRef[Optional[Structure17358]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure17363]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["critical_data"]
    ) -> _base.FieldRef[Optional[Structure17392]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["detection_sound_level"]
    ) -> _base.FieldRef[Optional[LoudNormalSilentVeryLoud17401]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["template"]
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
