"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags16665(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type16669(_values.OpenIntEnum):
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


class Flags16670(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_16672: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV216674(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_16674: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV116678(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_16678: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_16673: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_16682: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_16683: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_16684: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool16685(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_16685: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV216688(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_16688: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV116692(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_16692: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_16686: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_16696: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_16698: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_16700: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element16703(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_16702: _base.Variant = _base.Variant(
    path=(
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property16667(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type16669
    """Value decoded from this schema node."""

    flags: Flags16670
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_16672]
        | Annotated[
            Annotated[ObjectV216674, _VARIANT_16674]
            | Annotated[ObjectV116678, _VARIANT_16678],
            _VARIANT_16673,
        ]
        | Annotated[str, _VARIANT_16682]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16683,
        ]
        | Annotated[float, _VARIANT_16684]
        | Annotated[Bool16685, _VARIANT_16685]
        | Annotated[
            tuple[
                Annotated[ObjectV216688, _VARIANT_16688]
                | Annotated[ObjectV116692, _VARIANT_16692],
                ...,
            ],
            _VARIANT_16686,
        ]
        | Annotated[tuple[str, ...], _VARIANT_16696]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_16698,
        ]
        | Annotated[tuple[float, ...], _VARIANT_16700]
        | Annotated[tuple[Element16703, ...], _VARIANT_16702]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type16669]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags16670]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_16672]
        | Annotated[
            Annotated[ObjectV216674, _VARIANT_16674]
            | Annotated[ObjectV116678, _VARIANT_16678],
            _VARIANT_16673,
        ]
        | Annotated[str, _VARIANT_16682]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_16683,
        ]
        | Annotated[float, _VARIANT_16684]
        | Annotated[Bool16685, _VARIANT_16685]
        | Annotated[
            tuple[
                Annotated[ObjectV216688, _VARIANT_16688]
                | Annotated[ObjectV116692, _VARIANT_16692],
                ...,
            ],
            _VARIANT_16686,
        ]
        | Annotated[tuple[str, ...], _VARIANT_16696]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_16698,
        ]
        | Annotated[tuple[float, ...], _VARIANT_16700]
        | Annotated[tuple[Element16703, ...], _VARIANT_16702]
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


class Script16663(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "TREE/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags16665
    """Value decoded from this schema node."""

    properties: tuple[Property16667, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags16665]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property16667, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure16659(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TREE/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="TREE/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("TREE/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="TREE/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script16663, ...]
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
    ) -> _base.FieldRef[tuple[Script16663, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure16705(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TREE/2:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="TREE/2:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="TREE/2:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="TREE/2:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="TREE/2:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="TREE/2:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="TREE/2:Object Bounds/payload/5:Z2",
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


class Structure16717(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16719": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16720": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16721": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_16719: bytes
    """Value decoded from this schema node."""

    unused_16720: bytes
    """Value decoded from this schema node."""

    unused_16721: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16719"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16720"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16721"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16717: _base.Variant = _base.Variant(
    path=("TREE/3:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure16722(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_16725": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16726": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/1:St"
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

    unused_16725: bytes
    """Value decoded from this schema node."""

    unused_16726: bytes
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
    def field(self, name: Literal["unused_16725"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16726"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16722: _base.Variant = _base.Variant(
    path=("TREE/3:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture16730(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/2:St"
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


class Structure16727(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_16734": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_16735": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture16730, ...]
    """Value decoded from this schema node."""

    unused_16734: bytes
    """Value decoded from this schema node."""

    unused_16735: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture16730, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16734"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_16735"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_16727: _base.Variant = _base.Variant(
    path=("TREE/3:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture16740(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
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


class Material16747(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
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


class Structure16736(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "TREE/3:Model/1:Model Information/payload/variants/3:St"
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

    textures: tuple[Texture16740, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material16747, ...]
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
    ) -> _base.FieldRef[tuple[Texture16740, ...]]:
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
    ) -> _base.FieldRef[tuple[Material16747, ...]]:
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


_VARIANT_16736: _base.Variant = _base.Variant(
    path=("TREE/3:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture16754(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "TREE/3:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "TREE/3:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "TREE/3:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "TREE/3:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model16712(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TREE/3:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="TREE/3:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="TREE/3:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="TREE/3:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure16717, _VARIANT_16717]
        | Annotated[Structure16722, _VARIANT_16722]
        | Annotated[Structure16727, _VARIANT_16727]
        | Annotated[Structure16736, _VARIANT_16736]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture16754, ...]] = None
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
            Annotated[Structure16717, _VARIANT_16717]
            | Annotated[Structure16722, _VARIANT_16722]
            | Annotated[Structure16727, _VARIANT_16727]
            | Annotated[Structure16736, _VARIANT_16736]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture16754, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure16763(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TREE/6:Ingredient Production/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "spring": _base.Binding(
            path="TREE/6:Ingredient Production/payload/0:Spring",
            kind="primitive",
            name="Spring",
        ),
        "summer": _base.Binding(
            path="TREE/6:Ingredient Production/payload/1:Summer",
            kind="primitive",
            name="Summer",
        ),
        "fall": _base.Binding(
            path="TREE/6:Ingredient Production/payload/2:Fall",
            kind="primitive",
            name="Fall",
        ),
        "winter": _base.Binding(
            path="TREE/6:Ingredient Production/payload/3:Winter",
            kind="primitive",
            name="Winter",
        ),
    }

    spring: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    summer: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    fall: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    winter: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["spring"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["summer"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fall"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["winter"]
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


class Structure16771(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TREE/8:Tree Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "trunk_flexibility": _base.Binding(
            path="TREE/8:Tree Data/payload/0:Trunk Flexibility",
            kind="primitive",
            name="Trunk Flexibility",
        ),
        "branch_flexibility": _base.Binding(
            path="TREE/8:Tree Data/payload/1:Branch Flexibility",
            kind="primitive",
            name="Branch Flexibility",
        ),
        "trunk_amplitude": _base.Binding(
            path="TREE/8:Tree Data/payload/2:Trunk Amplitude",
            kind="primitive",
            name="Trunk Amplitude",
        ),
        "front_amplitude": _base.Binding(
            path="TREE/8:Tree Data/payload/3:Front Amplitude",
            kind="primitive",
            name="Front Amplitude",
        ),
        "back_amplitude": _base.Binding(
            path="TREE/8:Tree Data/payload/4:Back Amplitude",
            kind="primitive",
            name="Back Amplitude",
        ),
        "side_amplitude": _base.Binding(
            path="TREE/8:Tree Data/payload/5:Side Amplitude",
            kind="primitive",
            name="Side Amplitude",
        ),
        "front_frequency": _base.Binding(
            path="TREE/8:Tree Data/payload/6:Front Frequency",
            kind="primitive",
            name="Front Frequency",
        ),
        "back_frequency": _base.Binding(
            path="TREE/8:Tree Data/payload/7:Back Frequency",
            kind="primitive",
            name="Back Frequency",
        ),
        "side_frequency": _base.Binding(
            path="TREE/8:Tree Data/payload/8:Side Frequency",
            kind="primitive",
            name="Side Frequency",
        ),
        "leaf_flexibility": _base.Binding(
            path="TREE/8:Tree Data/payload/9:Leaf Flexibility",
            kind="primitive",
            name="Leaf Flexibility",
        ),
        "leaf_amplitude": _base.Binding(
            path="TREE/8:Tree Data/payload/10:Leaf Amplitude",
            kind="primitive",
            name="Leaf Amplitude",
        ),
        "leaf_frequency": _base.Binding(
            path="TREE/8:Tree Data/payload/11:Leaf Frequency",
            kind="primitive",
            name="Leaf Frequency",
        ),
    }

    trunk_flexibility: float
    """Value decoded from this schema node."""

    branch_flexibility: float
    """Value decoded from this schema node."""

    trunk_amplitude: float
    """Value decoded from this schema node."""

    front_amplitude: float
    """Value decoded from this schema node."""

    back_amplitude: float
    """Value decoded from this schema node."""

    side_amplitude: float
    """Value decoded from this schema node."""

    front_frequency: float
    """Value decoded from this schema node."""

    back_frequency: float
    """Value decoded from this schema node."""

    side_frequency: float
    """Value decoded from this schema node."""

    leaf_flexibility: float
    """Value decoded from this schema node."""

    leaf_amplitude: float
    """Value decoded from this schema node."""

    leaf_frequency: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["trunk_flexibility"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["branch_flexibility"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["trunk_amplitude"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["front_amplitude"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["back_amplitude"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["side_amplitude"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["front_frequency"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["back_frequency"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["side_frequency"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["leaf_flexibility"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["leaf_amplitude"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["leaf_frequency"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class TreeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TREE"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "TREE"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="TREE/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="TREE/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "object_bounds": _base.Binding(
            path="TREE/2:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "model": _base.Binding(
            path="TREE/3:Model",
            kind="unordered",
            name="Model",
        ),
        "ingredient": _base.Binding(
            path="TREE/4:Ingredient",
            kind="subrecord",
            name="Ingredient",
        ),
        "harvest_sound": _base.Binding(
            path="TREE/5:Harvest Sound",
            kind="subrecord",
            name="Harvest Sound",
        ),
        "ingredient_production": _base.Binding(
            path="TREE/6:Ingredient Production",
            kind="subrecord",
            name="Ingredient Production",
        ),
        "name": _base.Binding(
            path="TREE/7:Name",
            kind="subrecord",
            name="Name",
        ),
        "tree_data": _base.Binding(
            path="TREE/8:Tree Data",
            kind="subrecord",
            name="Tree Data",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure16659] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure16705] = None
    """Value decoded from this schema node."""

    model: Optional[Model16712] = None
    """Value decoded from this schema node."""

    ingredient: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    harvest_sound: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ingredient_production: Optional[Structure16763] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    tree_data: Optional[Structure16771] = None
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
    ) -> _base.FieldRef[Optional[Structure16659]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[Structure16705]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model16712]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ingredient"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["harvest_sound"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ingredient_production"]
    ) -> _base.FieldRef[Optional[Structure16763]]:
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
        self, name: Literal["tree_data"]
    ) -> _base.FieldRef[Optional[Structure16771]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
