"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags9653(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type9657(_values.OpenIntEnum):
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


class Flags9658(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_9660: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV29662(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9662: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV19666(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9666: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_9661: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_9670: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_9671: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_9672: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool9673(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_9673: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV29676(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9676: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV19680(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9680: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_9674: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_9684: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_9686: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_9688: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element9691(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_9690: _base.Variant = _base.Variant(
    path=(
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property9655(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type9657
    """Value decoded from this schema node."""

    flags: Flags9658
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_9660]
        | Annotated[
            Annotated[ObjectV29662, _VARIANT_9662]
            | Annotated[ObjectV19666, _VARIANT_9666],
            _VARIANT_9661,
        ]
        | Annotated[str, _VARIANT_9670]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9671,
        ]
        | Annotated[float, _VARIANT_9672]
        | Annotated[Bool9673, _VARIANT_9673]
        | Annotated[
            tuple[
                Annotated[ObjectV29676, _VARIANT_9676]
                | Annotated[ObjectV19680, _VARIANT_9680],
                ...,
            ],
            _VARIANT_9674,
        ]
        | Annotated[tuple[str, ...], _VARIANT_9684]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_9686,
        ]
        | Annotated[tuple[float, ...], _VARIANT_9688]
        | Annotated[tuple[Element9691, ...], _VARIANT_9690]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type9657]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9658]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_9660]
        | Annotated[
            Annotated[ObjectV29662, _VARIANT_9662]
            | Annotated[ObjectV19666, _VARIANT_9666],
            _VARIANT_9661,
        ]
        | Annotated[str, _VARIANT_9670]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9671,
        ]
        | Annotated[float, _VARIANT_9672]
        | Annotated[Bool9673, _VARIANT_9673]
        | Annotated[
            tuple[
                Annotated[ObjectV29676, _VARIANT_9676]
                | Annotated[ObjectV19680, _VARIANT_9680],
                ...,
            ],
            _VARIANT_9674,
        ]
        | Annotated[tuple[str, ...], _VARIANT_9684]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_9686,
        ]
        | Annotated[tuple[float, ...], _VARIANT_9688]
        | Annotated[tuple[Element9691, ...], _VARIANT_9690]
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


class Script9651(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "INGR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags9653
    """Value decoded from this schema node."""

    properties: tuple[Property9655, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9653]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property9655, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure9647(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="INGR/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("INGR/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="INGR/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script9651, ...]
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
    ) -> _base.FieldRef[tuple[Script9651, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure9693(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/2:Object Bounds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x1": _base.Binding(
            path="INGR/2:Object Bounds/payload/0:X1",
            kind="primitive",
            name="X1",
        ),
        "y1": _base.Binding(
            path="INGR/2:Object Bounds/payload/1:Y1",
            kind="primitive",
            name="Y1",
        ),
        "z1": _base.Binding(
            path="INGR/2:Object Bounds/payload/2:Z1",
            kind="primitive",
            name="Z1",
        ),
        "x2": _base.Binding(
            path="INGR/2:Object Bounds/payload/3:X2",
            kind="primitive",
            name="X2",
        ),
        "y2": _base.Binding(
            path="INGR/2:Object Bounds/payload/4:Y2",
            kind="primitive",
            name="Y2",
        ),
        "z2": _base.Binding(
            path="INGR/2:Object Bounds/payload/5:Z2",
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


class Structure9712(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/1:Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/0:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9714": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/0:St"
                "ructure/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9715": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/0:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9716": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/0:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_9714: bytes
    """Value decoded from this schema node."""

    unused_9715: bytes
    """Value decoded from this schema node."""

    unused_9716: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9714"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9715"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9716"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_9712: _base.Variant = _base.Variant(
    path=("INGR/6:Model/1:Model Information/payload/variants/0:Structure")
)


class Structure9717(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/1:Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/1:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/1:St"
                "ructure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_9720": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/1:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9721": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/1:St"
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

    unused_9720: bytes
    """Value decoded from this schema node."""

    unused_9721: bytes
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
    def field(self, name: Literal["unused_9720"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9721"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_9717: _base.Variant = _base.Variant(
    path=("INGR/6:Model/1:Model Information/payload/variants/1:Structure")
)


class Texture9725(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/1:Model Information/payload/variants/2:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/2:St"
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


class Structure9722(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/1:Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/2:St"
                "ructure/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/2:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_9729": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/2:St"
                "ructure/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9730": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/2:St"
                "ructure/3:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture9725, ...]
    """Value decoded from this schema node."""

    unused_9729: bytes
    """Value decoded from this schema node."""

    unused_9730: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture9725, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9729"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9730"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_9722: _base.Variant = _base.Variant(
    path=("INGR/6:Model/1:Model Information/payload/variants/2:Structure")
)


class Texture9735(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/1:Model Information/payload/variants/3:St"
        "ructure/1:Textures/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
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


class Material9742(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/1:Model Information/payload/variants/3:St"
        "ructure/3:Materials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
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


class Structure9731(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/1:Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/0:Headers"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/1:Textures"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/2:Addons"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
                "ructure/3:Materials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "INGR/6:Model/1:Model Information/payload/variants/3:St"
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

    textures: tuple[Texture9735, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material9742, ...]
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
    ) -> _base.FieldRef[tuple[Texture9735, ...]]:
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
    ) -> _base.FieldRef[tuple[Material9742, ...]]:
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


_VARIANT_9731: _base.Variant = _base.Variant(
    path=("INGR/6:Model/1:Model Information/payload/variants/3:Structure")
)


class AlternateTexture9749(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/6:Model/2:Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "INGR/6:Model/2:Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "INGR/6:Model/2:Alternate Textures/payload/element/1:Ne"
                "w Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "INGR/6:Model/2:Alternate Textures/payload/element/2:3D Index"
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


class Model9707(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/6:Model"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path="INGR/6:Model/0:Model FileName",
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path="INGR/6:Model/1:Model Information",
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path="INGR/6:Model/2:Alternate Textures",
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure9712, _VARIANT_9712]
        | Annotated[Structure9717, _VARIANT_9717]
        | Annotated[Structure9722, _VARIANT_9722]
        | Annotated[Structure9731, _VARIANT_9731]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture9749, ...]] = None
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
            Annotated[Structure9712, _VARIANT_9712]
            | Annotated[Structure9717, _VARIANT_9717]
            | Annotated[Structure9722, _VARIANT_9722]
            | Annotated[Structure9731, _VARIANT_9731]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture9749, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Icon9753(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/7:Icon"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "large_icon_file_name": _base.Binding(
            path="INGR/7:Icon/0:Large Icon FileName",
            kind="subrecord",
            name="Large Icon FileName",
        ),
        "small_icon_file_name": _base.Binding(
            path="INGR/7:Icon/1:Small Icon FileName",
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


class VatsTargetable9763(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure9760(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/8:Destructible/0:Header/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path="INGR/8:Destructible/0:Header/payload/0:Health",
            kind="primitive",
            name="Health",
        ),
        "dest_count": _base.Binding(
            path="INGR/8:Destructible/0:Header/payload/1:DEST Count",
            kind="primitive",
            name="DEST Count",
        ),
        "vats_targetable": _base.Binding(
            path=("INGR/8:Destructible/0:Header/payload/2:VATS Targetable"),
            kind="primitive",
            name="VATS Targetable",
        ),
        "unknown": _base.Binding(
            path="INGR/8:Destructible/0:Header/payload/3:Unknown",
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

    vats_targetable: VatsTargetable9763
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
    ) -> _base.FieldRef[VatsTargetable9763]:
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


class Flags9772(enum.IntFlag):
    """Named values from the pinned schema."""

    CAP_DAMAGE = 1
    DISABLE = 2
    DESTROY = 4
    IGNORE_EXTERNAL_DMG = 8


class Structure9768(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
        "ion Stage Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "health": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/0:Health %"
            ),
            kind="primitive",
            name="Health %",
        ),
        "index": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/1:Index"
            ),
            kind="primitive",
            name="Index",
        ),
        "model_damage_stage_value": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/2:Model Damage Stage"
            ),
            kind="primitive",
            name="Model Damage Stage",
        ),
        "flags": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/3:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "self_damage_per_second": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/4:Self Damage per Second"
            ),
            kind="primitive",
            name="Self Damage per Second",
        ),
        "explosion": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/5:Explosion"
            ),
            kind="primitive",
            name="Explosion",
        ),
        "debris": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data/payload/6:Debris"
            ),
            kind="primitive",
            name="Debris",
        ),
        "debris_count": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
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

    flags: Flags9772
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9772]:
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


class Structure9782(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9784": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/1:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9785": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9786": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/0:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    unused_9784: bytes
    """Value decoded from this schema node."""

    unused_9785: bytes
    """Value decoded from this schema node."""

    unused_9786: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9784"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9785"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9786"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_9782: _base.Variant = _base.Variant(
    path=(
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/0:Structure"
    )
)


class Structure9787(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "error": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/1:ERROR"
            ),
            kind="primitive",
            name="ERROR",
        ),
        "unused_9790": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/1:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9791": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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

    unused_9790: bytes
    """Value decoded from this schema node."""

    unused_9791: bytes
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
    def field(self, name: Literal["unused_9790"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9791"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_9787: _base.Variant = _base.Variant(
    path=(
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/1:Structure"
    )
)


class Texture9795(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Structure9792(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "textures": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "unused_9799": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/2:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "unused_9800": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/2:Structure/3:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    unused: bytes
    """Value decoded from this schema node."""

    textures: tuple[Texture9795, ...]
    """Value decoded from this schema node."""

    unused_9799: bytes
    """Value decoded from this schema node."""

    unused_9800: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["textures"]
    ) -> _base.FieldRef[tuple[Texture9795, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9799"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9800"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_9792: _base.Variant = _base.Variant(
    path=(
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/2:Structure"
    )
)


class Texture9805(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/1:Textu"
        "res/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Material9812(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure/3:Mater"
        "ials/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_hash": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/0:File Hash"
            ),
            kind="primitive",
            name="File Hash",
        ),
        "extension": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials/element/1:Extension"
            ),
            kind="primitive",
            name="Extension",
        ),
        "folder_hash": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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


class Structure9801(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "headers": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/0:Heade"
                "rs"
            ),
            kind="array",
            name="Headers",
        ),
        "textures": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/1:Textu"
                "res"
            ),
            kind="array",
            name="Textures",
        ),
        "addons": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/2:Addon"
                "s"
            ),
            kind="array",
            name="Addons",
        ),
        "materials": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information/payload/variants/3:Structure/3:Mater"
                "ials"
            ),
            kind="array",
            name="Materials",
        ),
        "unknown": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
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

    textures: tuple[Texture9805, ...]
    """Value decoded from this schema node."""

    addons: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)], ...
    ]
    """Value decoded from this schema node."""

    materials: tuple[Material9812, ...]
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
    ) -> _base.FieldRef[tuple[Texture9805, ...]]:
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
    ) -> _base.FieldRef[tuple[Material9812, ...]]:
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


_VARIANT_9801: _base.Variant = _base.Variant(
    path=(
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
        "Model Information/payload/variants/3:Structure"
    )
)


class AlternateTexture9819(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
        "Alternate Textures/payload/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value_3_d_name": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/0:3D Name"
            ),
            kind="primitive",
            name="3D Name",
        ),
        "new_texture": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures/payload/element/1:New Texture"
            ),
            kind="primitive",
            name="New Texture",
        ),
        "value_3_d_index": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
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


class Model9777(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "model_file_name_value": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/0:"
                "Model FileName"
            ),
            kind="subrecord",
            name="Model FileName",
        ),
        "model_information_value": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/1:"
                "Model Information"
            ),
            kind="subrecord",
            name="Model Information",
        ),
        "alternate_textures": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model/2:"
                "Alternate Textures"
            ),
            kind="subrecord",
            name="Alternate Textures",
        ),
    }

    model_file_name_value: Optional[str] = None
    """Value decoded from this schema node."""

    model_information_value: Optional[
        Annotated[Structure9782, _VARIANT_9782]
        | Annotated[Structure9787, _VARIANT_9787]
        | Annotated[Structure9792, _VARIANT_9792]
        | Annotated[Structure9801, _VARIANT_9801]
    ] = None
    """Value decoded from this schema node."""

    alternate_textures: Optional[tuple[AlternateTexture9819, ...]] = None
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
            Annotated[Structure9782, _VARIANT_9782]
            | Annotated[Structure9787, _VARIANT_9787]
            | Annotated[Structure9792, _VARIANT_9792]
            | Annotated[Structure9801, _VARIANT_9801]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alternate_textures"]
    ) -> _base.FieldRef[Optional[tuple[AlternateTexture9819, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Stage9766(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/8:Destructible/1:Stages/repeat/0:Stage"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "destruction_stage_data": _base.Binding(
            path=(
                "INGR/8:Destructible/1:Stages/repeat/0:Stage/0:Destruct"
                "ion Stage Data"
            ),
            kind="subrecord",
            name="Destruction Stage Data",
        ),
        "model": _base.Binding(
            path=("INGR/8:Destructible/1:Stages/repeat/0:Stage/1:Model"),
            kind="sequence",
            name="Model",
        ),
        "end_marker": _base.Binding(
            path=("INGR/8:Destructible/1:Stages/repeat/0:Stage/2:End Marker"),
            kind="subrecord",
            name="End Marker",
        ),
    }

    destruction_stage_data: Optional[Structure9768] = None
    """Value decoded from this schema node."""

    model: Optional[Model9777] = None
    """Value decoded from this schema node."""

    end_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["destruction_stage_data"]
    ) -> _base.FieldRef[Optional[Structure9768]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model9777]]:
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


class Destructible9758(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/8:Destructible"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="INGR/8:Destructible/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "stages": _base.Binding(
            path="INGR/8:Destructible/1:Stages",
            kind="repeat",
            name="Stages",
            repeated_path="INGR/8:Destructible/1:Stages/repeat/0:Stage",
            child_kind="sequence",
        ),
    }

    header: Optional[Structure9760] = None
    """Value decoded from this schema node."""

    stages: tuple[Stage9766, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure9760]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stages"]
    ) -> _base.FieldRef[tuple[Stage9766, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure9832(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/12:DATA/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "value": _base.Binding(
            path="INGR/12:DATA/payload/0:Value",
            kind="primitive",
            name="Value",
        ),
        "weight": _base.Binding(
            path="INGR/12:DATA/payload/1:Weight",
            kind="primitive",
            name="Weight",
        ),
    }

    value: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    weight: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
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


class Flags9838(enum.IntFlag):
    """Named values from the pinned schema."""

    NO_AUTO_CALCULATION = 1
    FOOD_ITEM = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    UNKNOWN_8 = 128
    REFERENCES_PERSIST = 256


class Structure9836(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/13:Effect Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ingredient_value": _base.Binding(
            path="INGR/13:Effect Data/payload/0:Ingredient Value",
            kind="primitive",
            name="Ingredient Value",
        ),
        "flags": _base.Binding(
            path="INGR/13:Effect Data/payload/1:Flags",
            kind="primitive",
            name="Flags",
        ),
    }

    ingredient_value: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    flags: Flags9838
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ingredient_value"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9838]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure9844(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/14:Effects/repeat/0:Effect/1:EFIT/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "magnitude": _base.Binding(
            path=("INGR/14:Effects/repeat/0:Effect/1:EFIT/payload/0:Magnitude"),
            kind="primitive",
            name="Magnitude",
        ),
        "area": _base.Binding(
            path=("INGR/14:Effects/repeat/0:Effect/1:EFIT/payload/1:Area"),
            kind="primitive",
            name="Area",
        ),
        "duration": _base.Binding(
            path=("INGR/14:Effects/repeat/0:Effect/1:EFIT/payload/2:Duration"),
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


_VARIANT_9855: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/2:Comparison Value/variants/0"
        ":Comparison Value - Float"
    )
)


_VARIANT_9856: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/2:Comparison Value/variants/1"
        ":Comparison Value - Global"
    )
)


_VARIANT_9860: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/0:Unk"
        "nown"
    )
)


_VARIANT_9861: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/1:Non"
        "e"
    )
)


_VARIANT_9862: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/2:Int"
        "eger"
    )
)


_VARIANT_9863: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/3:Flo"
        "at"
    )
)


_VARIANT_9864: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/4:Var"
        "iable Name"
    )
)


class Sex9865(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_9865: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/5:Sex"
    )
)


class ActorValue9866(_values.OpenIntEnum):
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


_VARIANT_9866: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/6:Act"
        "or Value"
    )
)


class CrimeType9867(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_9867: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/7:Cri"
        "me Type"
    )
)


class Axis9868(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_9868: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/8:Axi"
        "s"
    )
)


_VARIANT_9869: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/9:Que"
        "st Stage (unused)"
    )
)


class MiscStat9870(_values.OpenIntEnum):
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


_VARIANT_9870: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/10:Mi"
        "sc Stat"
    )
)


class Alignment9871(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_9871: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/11:Al"
        "ignment"
    )
)


_VARIANT_9872: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/12:Eq"
        "uip Type"
    )
)


class FormType9873(_values.OpenIntEnum):
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


_VARIANT_9873: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/13:Fo"
        "rm Type"
    )
)


class CriticalStage9874(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_9874: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/14:Cr"
        "itical Stage"
    )
)


_VARIANT_9875: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/15:Ob"
        "ject Reference"
    )
)


_VARIANT_9876: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/16:In"
        "ventory Object"
    )
)


_VARIANT_9877: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/17:Ac"
        "tor"
    )
)


_VARIANT_9878: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/18:Vo"
        "ice Type"
    )
)


_VARIANT_9879: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/19:Id"
        "le"
    )
)


_VARIANT_9880: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/20:Fo"
        "rm List"
    )
)


_VARIANT_9881: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/21:Qu"
        "est"
    )
)


_VARIANT_9882: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/22:Fa"
        "ction"
    )
)


_VARIANT_9883: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/23:Ce"
        "ll"
    )
)


_VARIANT_9884: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/24:Cl"
        "ass"
    )
)


_VARIANT_9885: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/25:Ra"
        "ce"
    )
)


_VARIANT_9886: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/26:Ac"
        "tor Base"
    )
)


_VARIANT_9887: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/27:Gl"
        "obal"
    )
)


_VARIANT_9888: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/28:We"
        "ather"
    )
)


_VARIANT_9889: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/29:Pa"
        "ckage"
    )
)


_VARIANT_9890: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/30:En"
        "counter Zone"
    )
)


_VARIANT_9891: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/31:Pe"
        "rk"
    )
)


_VARIANT_9892: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/32:Ow"
        "ner"
    )
)


_VARIANT_9893: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/33:Fu"
        "rniture"
    )
)


_VARIANT_9894: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/34:Ef"
        "fect Item"
    )
)


_VARIANT_9895: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/35:Ba"
        "se Effect"
    )
)


_VARIANT_9896: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/36:Wo"
        "rldspace"
    )
)


class VatsValueFunction9897(_values.OpenIntEnum):
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


_VARIANT_9897: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/37:VA"
        "TS Value Function"
    )
)


_VARIANT_9898: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/38:VA"
        "TS Value Param (INVALID)"
    )
)


_VARIANT_9899: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/39:Re"
        "ferenceable Object"
    )
)


_VARIANT_9900: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/40:Re"
        "gion"
    )
)


_VARIANT_9901: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/41:Ke"
        "yword"
    )
)


class PlayerAction9902(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_9902: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/42:Pl"
        "ayer Action"
    )
)


class CastingType9903(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_9903: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/43:Ca"
        "sting Type"
    )
)


_VARIANT_9904: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/44:Sh"
        "out"
    )
)


_VARIANT_9905: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/45:Lo"
        "cation"
    )
)


_VARIANT_9906: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/46:Lo"
        "cation Ref Type"
    )
)


_VARIANT_9907: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/47:Al"
        "ias"
    )
)


_VARIANT_9908: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/48:Pa"
        "ckdata ID"
    )
)


_VARIANT_9909: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/49:As"
        "sociation Type"
    )
)


class FurnitureAnim9910(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_9910: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/50:Fu"
        "rniture Anim"
    )
)


class FurnitureEntry9911(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_9911: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/51:Fu"
        "rniture Entry"
    )
)


_VARIANT_9912: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/52:Sc"
        "ene"
    )
)


class WardState9913(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_9913: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/53:Wa"
        "rd State"
    )
)


_VARIANT_9914: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/54:Ev"
        "ent"
    )
)


_VARIANT_9915: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/55:Ev"
        "ent Data"
    )
)


_VARIANT_9916: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/56:Kn"
        "owable"
    )
)


_VARIANT_9917: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/57:Fa"
        "ction"
    )
)


_VARIANT_9919: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/0:Unk"
        "nown"
    )
)


_VARIANT_9920: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/1:Non"
        "e"
    )
)


_VARIANT_9921: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/2:Int"
        "eger"
    )
)


_VARIANT_9922: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/3:Flo"
        "at"
    )
)


_VARIANT_9923: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/4:Var"
        "iable Name"
    )
)


class Sex9924(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_9924: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/5:Sex"
    )
)


class ActorValue9925(_values.OpenIntEnum):
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


_VARIANT_9925: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/6:Act"
        "or Value"
    )
)


class CrimeType9926(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_9926: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/7:Cri"
        "me Type"
    )
)


class Axis9927(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_9927: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/8:Axi"
        "s"
    )
)


_VARIANT_9928: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/9:Que"
        "st Stage"
    )
)


class MiscStat9929(_values.OpenIntEnum):
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


_VARIANT_9929: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/10:Mi"
        "sc Stat"
    )
)


class Alignment9930(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_9930: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/11:Al"
        "ignment"
    )
)


_VARIANT_9931: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/12:Eq"
        "uip Type"
    )
)


class FormType9932(_values.OpenIntEnum):
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


_VARIANT_9932: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/13:Fo"
        "rm Type"
    )
)


class CriticalStage9933(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_9933: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/14:Cr"
        "itical Stage"
    )
)


_VARIANT_9934: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/15:Ob"
        "ject Reference"
    )
)


_VARIANT_9935: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/16:In"
        "ventory Object"
    )
)


_VARIANT_9936: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/17:Ac"
        "tor"
    )
)


_VARIANT_9937: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/18:Vo"
        "ice Type"
    )
)


_VARIANT_9938: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/19:Id"
        "le"
    )
)


_VARIANT_9939: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/20:Fo"
        "rm List"
    )
)


_VARIANT_9940: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/21:Qu"
        "est"
    )
)


_VARIANT_9941: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/22:Fa"
        "ction"
    )
)


_VARIANT_9942: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/23:Ce"
        "ll"
    )
)


_VARIANT_9943: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/24:Cl"
        "ass"
    )
)


_VARIANT_9944: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/25:Ra"
        "ce"
    )
)


_VARIANT_9945: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/26:Ac"
        "tor Base"
    )
)


_VARIANT_9946: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/27:Gl"
        "obal"
    )
)


_VARIANT_9947: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/28:We"
        "ather"
    )
)


_VARIANT_9948: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/29:Pa"
        "ckage"
    )
)


_VARIANT_9949: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/30:En"
        "counter Zone"
    )
)


_VARIANT_9950: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/31:Pe"
        "rk"
    )
)


_VARIANT_9951: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/32:Ow"
        "ner"
    )
)


_VARIANT_9952: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/33:Fu"
        "rniture"
    )
)


_VARIANT_9953: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/34:Ef"
        "fect Item"
    )
)


_VARIANT_9954: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/35:Ba"
        "se Effect"
    )
)


_VARIANT_9955: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/36:Wo"
        "rldspace"
    )
)


class VatsValueFunction9956(_values.OpenIntEnum):
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


_VARIANT_9956: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/37:VA"
        "TS Value Function"
    )
)


_VARIANT_9958: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/0:Weapon"
    )
)


_VARIANT_9959: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/1:Weapon List"
    )
)


_VARIANT_9960: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/2:Target"
    )
)


_VARIANT_9961: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/3:Target List"
    )
)


_VARIANT_9962: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/4:Unknown"
    )
)


class TargetPart9963(_values.OpenIntEnum):
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


_VARIANT_9963: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/5:Target Part"
    )
)


class VatsAction9964(_values.OpenIntEnum):
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


_VARIANT_9964: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/6:VATS Action"
    )
)


_VARIANT_9965: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/7:Unknown"
    )
)


_VARIANT_9966: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/8:Unknown"
    )
)


_VARIANT_9967: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/9:Critical Effect"
    )
)


_VARIANT_9968: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/10:Critical Effect List"
    )
)


_VARIANT_9969: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/11:Unknown"
    )
)


_VARIANT_9970: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/12:Unknown"
    )
)


_VARIANT_9971: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/13:Unknown"
    )
)


_VARIANT_9972: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/14:Unknown"
    )
)


class WeaponType9973(_values.OpenIntEnum):
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


_VARIANT_9973: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_9974: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/16:Unknown"
    )
)


_VARIANT_9975: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/17:Unknown"
    )
)


class ProjectileType9976(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_9976: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/18:Projectile Type"
    )
)


class DeliveryType9977(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_9977: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/19:Delivery Type"
    )
)


class CastingType9978(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_9978: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/20:Casting Type"
    )
)


_VARIANT_9957: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param"
    )
)


_VARIANT_9979: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/39:Re"
        "ferenceable Object"
    )
)


_VARIANT_9980: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/40:Re"
        "gion"
    )
)


_VARIANT_9981: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/41:Ke"
        "yword"
    )
)


class PlayerAction9982(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_9982: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/42:Pl"
        "ayer Action"
    )
)


class CastingType9983(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_9983: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/43:Ca"
        "sting Type"
    )
)


_VARIANT_9984: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/44:Sh"
        "out"
    )
)


_VARIANT_9985: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/45:Lo"
        "cation"
    )
)


_VARIANT_9986: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/46:Lo"
        "cation Ref Type"
    )
)


_VARIANT_9987: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/47:Al"
        "ias"
    )
)


_VARIANT_9988: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/48:Pa"
        "ckdata ID"
    )
)


_VARIANT_9989: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/49:As"
        "sociation Type"
    )
)


class FurnitureAnim9990(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_9990: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/50:Fu"
        "rniture Anim"
    )
)


class FurnitureEntry9991(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_9991: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/51:Fu"
        "rniture Entry"
    )
)


_VARIANT_9992: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/52:Sc"
        "ene"
    )
)


class WardState9993(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_9993: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/53:Wa"
        "rd State"
    )
)


_VARIANT_9994: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/54:Ev"
        "ent"
    )
)


_VARIANT_9995: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/55:Ev"
        "ent Data"
    )
)


_VARIANT_9996: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/56:Kn"
        "owable"
    )
)


_VARIANT_9997: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/57:Fa"
        "ction"
    )
)


class RunOn9998(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_10000: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/8:Reference/variants/0:Unused"
    )
)


_VARIANT_10001: _base.Variant = _base.Variant(
    path=(
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/8:Reference/variants/1:Refere"
        "nce"
    )
)


class Structure9851(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
        "Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_9858": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
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
        Annotated[float, _VARIANT_9855]
        | Annotated[_values.FormId, _VARIANT_9856]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_9858: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_9860]
        | Annotated[bytes, _VARIANT_9861]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9862,
        ]
        | Annotated[float, _VARIANT_9863]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9864,
        ]
        | Annotated[Sex9865, _VARIANT_9865]
        | Annotated[ActorValue9866, _VARIANT_9866]
        | Annotated[CrimeType9867, _VARIANT_9867]
        | Annotated[Axis9868, _VARIANT_9868]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9869,
        ]
        | Annotated[MiscStat9870, _VARIANT_9870]
        | Annotated[Alignment9871, _VARIANT_9871]
        | Annotated[_values.FormId, _VARIANT_9872]
        | Annotated[FormType9873, _VARIANT_9873]
        | Annotated[CriticalStage9874, _VARIANT_9874]
        | Annotated[_values.FormId, _VARIANT_9875]
        | Annotated[_values.FormId, _VARIANT_9876]
        | Annotated[_values.FormId, _VARIANT_9877]
        | Annotated[_values.FormId, _VARIANT_9878]
        | Annotated[_values.FormId, _VARIANT_9879]
        | Annotated[_values.FormId, _VARIANT_9880]
        | Annotated[_values.FormId, _VARIANT_9881]
        | Annotated[_values.FormId, _VARIANT_9882]
        | Annotated[_values.FormId, _VARIANT_9883]
        | Annotated[_values.FormId, _VARIANT_9884]
        | Annotated[_values.FormId, _VARIANT_9885]
        | Annotated[_values.FormId, _VARIANT_9886]
        | Annotated[_values.FormId, _VARIANT_9887]
        | Annotated[_values.FormId, _VARIANT_9888]
        | Annotated[_values.FormId, _VARIANT_9889]
        | Annotated[_values.FormId, _VARIANT_9890]
        | Annotated[_values.FormId, _VARIANT_9891]
        | Annotated[_values.FormId, _VARIANT_9892]
        | Annotated[_values.FormId, _VARIANT_9893]
        | Annotated[_values.FormId, _VARIANT_9894]
        | Annotated[_values.FormId, _VARIANT_9895]
        | Annotated[_values.FormId, _VARIANT_9896]
        | Annotated[VatsValueFunction9897, _VARIANT_9897]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9898,
        ]
        | Annotated[_values.FormId, _VARIANT_9899]
        | Annotated[_values.FormId, _VARIANT_9900]
        | Annotated[_values.FormId, _VARIANT_9901]
        | Annotated[PlayerAction9902, _VARIANT_9902]
        | Annotated[CastingType9903, _VARIANT_9903]
        | Annotated[_values.FormId, _VARIANT_9904]
        | Annotated[_values.FormId, _VARIANT_9905]
        | Annotated[_values.FormId, _VARIANT_9906]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9907,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9908,
        ]
        | Annotated[_values.FormId, _VARIANT_9909]
        | Annotated[FurnitureAnim9910, _VARIANT_9910]
        | Annotated[FurnitureEntry9911, _VARIANT_9911]
        | Annotated[_values.FormId, _VARIANT_9912]
        | Annotated[WardState9913, _VARIANT_9913]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9914,
        ]
        | Annotated[_values.FormId, _VARIANT_9915]
        | Annotated[_values.FormId, _VARIANT_9916]
        | Annotated[_values.FormId, _VARIANT_9917]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_9919]
        | Annotated[bytes, _VARIANT_9920]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9921,
        ]
        | Annotated[float, _VARIANT_9922]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9923,
        ]
        | Annotated[Sex9924, _VARIANT_9924]
        | Annotated[ActorValue9925, _VARIANT_9925]
        | Annotated[CrimeType9926, _VARIANT_9926]
        | Annotated[Axis9927, _VARIANT_9927]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9928,
        ]
        | Annotated[MiscStat9929, _VARIANT_9929]
        | Annotated[Alignment9930, _VARIANT_9930]
        | Annotated[_values.FormId, _VARIANT_9931]
        | Annotated[FormType9932, _VARIANT_9932]
        | Annotated[CriticalStage9933, _VARIANT_9933]
        | Annotated[_values.FormId, _VARIANT_9934]
        | Annotated[_values.FormId, _VARIANT_9935]
        | Annotated[_values.FormId, _VARIANT_9936]
        | Annotated[_values.FormId, _VARIANT_9937]
        | Annotated[_values.FormId, _VARIANT_9938]
        | Annotated[_values.FormId, _VARIANT_9939]
        | Annotated[_values.FormId, _VARIANT_9940]
        | Annotated[_values.FormId, _VARIANT_9941]
        | Annotated[_values.FormId, _VARIANT_9942]
        | Annotated[_values.FormId, _VARIANT_9943]
        | Annotated[_values.FormId, _VARIANT_9944]
        | Annotated[_values.FormId, _VARIANT_9945]
        | Annotated[_values.FormId, _VARIANT_9946]
        | Annotated[_values.FormId, _VARIANT_9947]
        | Annotated[_values.FormId, _VARIANT_9948]
        | Annotated[_values.FormId, _VARIANT_9949]
        | Annotated[_values.FormId, _VARIANT_9950]
        | Annotated[_values.FormId, _VARIANT_9951]
        | Annotated[_values.FormId, _VARIANT_9952]
        | Annotated[_values.FormId, _VARIANT_9953]
        | Annotated[_values.FormId, _VARIANT_9954]
        | Annotated[_values.FormId, _VARIANT_9955]
        | Annotated[VatsValueFunction9956, _VARIANT_9956]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_9958]
            | Annotated[_values.FormId, _VARIANT_9959]
            | Annotated[_values.FormId, _VARIANT_9960]
            | Annotated[_values.FormId, _VARIANT_9961]
            | Annotated[bytes, _VARIANT_9962]
            | Annotated[TargetPart9963, _VARIANT_9963]
            | Annotated[VatsAction9964, _VARIANT_9964]
            | Annotated[bytes, _VARIANT_9965]
            | Annotated[bytes, _VARIANT_9966]
            | Annotated[_values.FormId, _VARIANT_9967]
            | Annotated[_values.FormId, _VARIANT_9968]
            | Annotated[bytes, _VARIANT_9969]
            | Annotated[bytes, _VARIANT_9970]
            | Annotated[bytes, _VARIANT_9971]
            | Annotated[bytes, _VARIANT_9972]
            | Annotated[WeaponType9973, _VARIANT_9973]
            | Annotated[bytes, _VARIANT_9974]
            | Annotated[bytes, _VARIANT_9975]
            | Annotated[ProjectileType9976, _VARIANT_9976]
            | Annotated[DeliveryType9977, _VARIANT_9977]
            | Annotated[CastingType9978, _VARIANT_9978],
            _VARIANT_9957,
        ]
        | Annotated[_values.FormId, _VARIANT_9979]
        | Annotated[_values.FormId, _VARIANT_9980]
        | Annotated[_values.FormId, _VARIANT_9981]
        | Annotated[PlayerAction9982, _VARIANT_9982]
        | Annotated[CastingType9983, _VARIANT_9983]
        | Annotated[_values.FormId, _VARIANT_9984]
        | Annotated[_values.FormId, _VARIANT_9985]
        | Annotated[_values.FormId, _VARIANT_9986]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9987,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9988,
        ]
        | Annotated[_values.FormId, _VARIANT_9989]
        | Annotated[FurnitureAnim9990, _VARIANT_9990]
        | Annotated[FurnitureEntry9991, _VARIANT_9991]
        | Annotated[_values.FormId, _VARIANT_9992]
        | Annotated[WardState9993, _VARIANT_9993]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9994,
        ]
        | Annotated[_values.FormId, _VARIANT_9995]
        | Annotated[_values.FormId, _VARIANT_9996]
        | Annotated[_values.FormId, _VARIANT_9997]
    )
    """Value decoded from this schema node."""

    run_on: RunOn9998
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10000,
        ]
        | Annotated[_values.FormId, _VARIANT_10001]
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
        Annotated[float, _VARIANT_9855]
        | Annotated[_values.FormId, _VARIANT_9856]
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
    def field(self, name: Literal["unused_9858"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_9860]
        | Annotated[bytes, _VARIANT_9861]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9862,
        ]
        | Annotated[float, _VARIANT_9863]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9864,
        ]
        | Annotated[Sex9865, _VARIANT_9865]
        | Annotated[ActorValue9866, _VARIANT_9866]
        | Annotated[CrimeType9867, _VARIANT_9867]
        | Annotated[Axis9868, _VARIANT_9868]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9869,
        ]
        | Annotated[MiscStat9870, _VARIANT_9870]
        | Annotated[Alignment9871, _VARIANT_9871]
        | Annotated[_values.FormId, _VARIANT_9872]
        | Annotated[FormType9873, _VARIANT_9873]
        | Annotated[CriticalStage9874, _VARIANT_9874]
        | Annotated[_values.FormId, _VARIANT_9875]
        | Annotated[_values.FormId, _VARIANT_9876]
        | Annotated[_values.FormId, _VARIANT_9877]
        | Annotated[_values.FormId, _VARIANT_9878]
        | Annotated[_values.FormId, _VARIANT_9879]
        | Annotated[_values.FormId, _VARIANT_9880]
        | Annotated[_values.FormId, _VARIANT_9881]
        | Annotated[_values.FormId, _VARIANT_9882]
        | Annotated[_values.FormId, _VARIANT_9883]
        | Annotated[_values.FormId, _VARIANT_9884]
        | Annotated[_values.FormId, _VARIANT_9885]
        | Annotated[_values.FormId, _VARIANT_9886]
        | Annotated[_values.FormId, _VARIANT_9887]
        | Annotated[_values.FormId, _VARIANT_9888]
        | Annotated[_values.FormId, _VARIANT_9889]
        | Annotated[_values.FormId, _VARIANT_9890]
        | Annotated[_values.FormId, _VARIANT_9891]
        | Annotated[_values.FormId, _VARIANT_9892]
        | Annotated[_values.FormId, _VARIANT_9893]
        | Annotated[_values.FormId, _VARIANT_9894]
        | Annotated[_values.FormId, _VARIANT_9895]
        | Annotated[_values.FormId, _VARIANT_9896]
        | Annotated[VatsValueFunction9897, _VARIANT_9897]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9898,
        ]
        | Annotated[_values.FormId, _VARIANT_9899]
        | Annotated[_values.FormId, _VARIANT_9900]
        | Annotated[_values.FormId, _VARIANT_9901]
        | Annotated[PlayerAction9902, _VARIANT_9902]
        | Annotated[CastingType9903, _VARIANT_9903]
        | Annotated[_values.FormId, _VARIANT_9904]
        | Annotated[_values.FormId, _VARIANT_9905]
        | Annotated[_values.FormId, _VARIANT_9906]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9907,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9908,
        ]
        | Annotated[_values.FormId, _VARIANT_9909]
        | Annotated[FurnitureAnim9910, _VARIANT_9910]
        | Annotated[FurnitureEntry9911, _VARIANT_9911]
        | Annotated[_values.FormId, _VARIANT_9912]
        | Annotated[WardState9913, _VARIANT_9913]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9914,
        ]
        | Annotated[_values.FormId, _VARIANT_9915]
        | Annotated[_values.FormId, _VARIANT_9916]
        | Annotated[_values.FormId, _VARIANT_9917]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_9919]
        | Annotated[bytes, _VARIANT_9920]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9921,
        ]
        | Annotated[float, _VARIANT_9922]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9923,
        ]
        | Annotated[Sex9924, _VARIANT_9924]
        | Annotated[ActorValue9925, _VARIANT_9925]
        | Annotated[CrimeType9926, _VARIANT_9926]
        | Annotated[Axis9927, _VARIANT_9927]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9928,
        ]
        | Annotated[MiscStat9929, _VARIANT_9929]
        | Annotated[Alignment9930, _VARIANT_9930]
        | Annotated[_values.FormId, _VARIANT_9931]
        | Annotated[FormType9932, _VARIANT_9932]
        | Annotated[CriticalStage9933, _VARIANT_9933]
        | Annotated[_values.FormId, _VARIANT_9934]
        | Annotated[_values.FormId, _VARIANT_9935]
        | Annotated[_values.FormId, _VARIANT_9936]
        | Annotated[_values.FormId, _VARIANT_9937]
        | Annotated[_values.FormId, _VARIANT_9938]
        | Annotated[_values.FormId, _VARIANT_9939]
        | Annotated[_values.FormId, _VARIANT_9940]
        | Annotated[_values.FormId, _VARIANT_9941]
        | Annotated[_values.FormId, _VARIANT_9942]
        | Annotated[_values.FormId, _VARIANT_9943]
        | Annotated[_values.FormId, _VARIANT_9944]
        | Annotated[_values.FormId, _VARIANT_9945]
        | Annotated[_values.FormId, _VARIANT_9946]
        | Annotated[_values.FormId, _VARIANT_9947]
        | Annotated[_values.FormId, _VARIANT_9948]
        | Annotated[_values.FormId, _VARIANT_9949]
        | Annotated[_values.FormId, _VARIANT_9950]
        | Annotated[_values.FormId, _VARIANT_9951]
        | Annotated[_values.FormId, _VARIANT_9952]
        | Annotated[_values.FormId, _VARIANT_9953]
        | Annotated[_values.FormId, _VARIANT_9954]
        | Annotated[_values.FormId, _VARIANT_9955]
        | Annotated[VatsValueFunction9956, _VARIANT_9956]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_9958]
            | Annotated[_values.FormId, _VARIANT_9959]
            | Annotated[_values.FormId, _VARIANT_9960]
            | Annotated[_values.FormId, _VARIANT_9961]
            | Annotated[bytes, _VARIANT_9962]
            | Annotated[TargetPart9963, _VARIANT_9963]
            | Annotated[VatsAction9964, _VARIANT_9964]
            | Annotated[bytes, _VARIANT_9965]
            | Annotated[bytes, _VARIANT_9966]
            | Annotated[_values.FormId, _VARIANT_9967]
            | Annotated[_values.FormId, _VARIANT_9968]
            | Annotated[bytes, _VARIANT_9969]
            | Annotated[bytes, _VARIANT_9970]
            | Annotated[bytes, _VARIANT_9971]
            | Annotated[bytes, _VARIANT_9972]
            | Annotated[WeaponType9973, _VARIANT_9973]
            | Annotated[bytes, _VARIANT_9974]
            | Annotated[bytes, _VARIANT_9975]
            | Annotated[ProjectileType9976, _VARIANT_9976]
            | Annotated[DeliveryType9977, _VARIANT_9977]
            | Annotated[CastingType9978, _VARIANT_9978],
            _VARIANT_9957,
        ]
        | Annotated[_values.FormId, _VARIANT_9979]
        | Annotated[_values.FormId, _VARIANT_9980]
        | Annotated[_values.FormId, _VARIANT_9981]
        | Annotated[PlayerAction9982, _VARIANT_9982]
        | Annotated[CastingType9983, _VARIANT_9983]
        | Annotated[_values.FormId, _VARIANT_9984]
        | Annotated[_values.FormId, _VARIANT_9985]
        | Annotated[_values.FormId, _VARIANT_9986]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9987,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9988,
        ]
        | Annotated[_values.FormId, _VARIANT_9989]
        | Annotated[FurnitureAnim9990, _VARIANT_9990]
        | Annotated[FurnitureEntry9991, _VARIANT_9991]
        | Annotated[_values.FormId, _VARIANT_9992]
        | Annotated[WardState9993, _VARIANT_9993]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9994,
        ]
        | Annotated[_values.FormId, _VARIANT_9995]
        | Annotated[_values.FormId, _VARIANT_9996]
        | Annotated[_values.FormId, _VARIANT_9997]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn9998]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10000,
        ]
        | Annotated[_values.FormId, _VARIANT_10001]
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


class Condition9849(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure9851] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure9851]]:
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


class Effect9840(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR/14:Effects/repeat/0:Effect"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "base_effect": _base.Binding(
            path="INGR/14:Effects/repeat/0:Effect/0:Base Effect",
            kind="subrecord",
            name="Base Effect",
        ),
        "efit": _base.Binding(
            path="INGR/14:Effects/repeat/0:Effect/1:EFIT",
            kind="subrecord",
            name="EFIT",
        ),
        "conditions": _base.Binding(
            path="INGR/14:Effects/repeat/0:Effect/2:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "INGR/14:Effects/repeat/0:Effect/2:Conditions/repeat/0:"
                "Condition"
            ),
            child_kind="sequence",
        ),
    }

    base_effect: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    efit: Optional[Structure9844] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition9849, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure9844]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition9849, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class IngredientRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INGR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "INGR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="INGR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="INGR/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "object_bounds": _base.Binding(
            path="INGR/2:Object Bounds",
            kind="subrecord",
            name="Object Bounds",
        ),
        "name": _base.Binding(
            path="INGR/3:Name",
            kind="subrecord",
            name="Name",
        ),
        "keyword_count": _base.Binding(
            path="INGR/4:Keyword Count",
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path="INGR/5:Keywords",
            kind="subrecord",
            name="Keywords",
        ),
        "model": _base.Binding(
            path="INGR/6:Model",
            kind="unordered",
            name="Model",
        ),
        "icon": _base.Binding(
            path="INGR/7:Icon",
            kind="unordered",
            name="Icon",
        ),
        "destructible": _base.Binding(
            path="INGR/8:Destructible",
            kind="sequence",
            name="Destructible",
        ),
        "equipment_type": _base.Binding(
            path="INGR/9:Equipment Type",
            kind="subrecord",
            name="Equipment Type",
        ),
        "sound_pick_up": _base.Binding(
            path="INGR/10:Sound - Pick Up",
            kind="subrecord",
            name="Sound - Pick Up",
        ),
        "sound_put_down": _base.Binding(
            path="INGR/11:Sound - Put Down",
            kind="subrecord",
            name="Sound - Put Down",
        ),
        "data": _base.Binding(
            path="INGR/12:DATA",
            kind="subrecord",
            name="DATA",
        ),
        "effect_data": _base.Binding(
            path="INGR/13:Effect Data",
            kind="subrecord",
            name="Effect Data",
        ),
        "effects": _base.Binding(
            path="INGR/14:Effects",
            kind="repeat",
            name="Effects",
            repeated_path="INGR/14:Effects/repeat/0:Effect",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure9647] = None
    """Value decoded from this schema node."""

    object_bounds: Optional[Structure9693] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    model: Optional[Model9707] = None
    """Value decoded from this schema node."""

    icon: Optional[Icon9753] = None
    """Value decoded from this schema node."""

    destructible: Optional[Destructible9758] = None
    """Value decoded from this schema node."""

    equipment_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sound_pick_up: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    sound_put_down: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    data: Optional[Structure9832] = None
    """Value decoded from this schema node."""

    effect_data: Optional[Structure9836] = None
    """Value decoded from this schema node."""

    effects: tuple[Effect9840, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure9647]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_bounds"]
    ) -> _base.FieldRef[Optional[Structure9693]]:
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
        self, name: Literal["model"]
    ) -> _base.FieldRef[Optional[Model9707]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["icon"]
    ) -> _base.FieldRef[Optional[Icon9753]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["destructible"]
    ) -> _base.FieldRef[Optional[Destructible9758]]:
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
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure9832]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effect_data"]
    ) -> _base.FieldRef[Optional[Structure9836]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effects"]
    ) -> _base.FieldRef[tuple[Effect9840, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
