"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags15626(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type15630(_values.OpenIntEnum):
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


class Flags15631(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_15633: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV215635(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_15635: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV115639(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_15639: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_15634: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_15643: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_15644: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_15645: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool15646(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_15646: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV215649(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_15649: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV115653(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_15653: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_15647: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_15657: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_15659: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_15661: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element15664(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_15663: _base.Variant = _base.Variant(
    path=(
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property15628(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type15630
    """Value decoded from this schema node."""

    flags: Flags15631
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_15633]
        | Annotated[
            Annotated[ObjectV215635, _VARIANT_15635]
            | Annotated[ObjectV115639, _VARIANT_15639],
            _VARIANT_15634,
        ]
        | Annotated[str, _VARIANT_15643]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_15644,
        ]
        | Annotated[float, _VARIANT_15645]
        | Annotated[Bool15646, _VARIANT_15646]
        | Annotated[
            tuple[
                Annotated[ObjectV215649, _VARIANT_15649]
                | Annotated[ObjectV115653, _VARIANT_15653],
                ...,
            ],
            _VARIANT_15647,
        ]
        | Annotated[tuple[str, ...], _VARIANT_15657]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_15659,
        ]
        | Annotated[tuple[float, ...], _VARIANT_15661]
        | Annotated[tuple[Element15664, ...], _VARIANT_15663]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type15630]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15631]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_15633]
        | Annotated[
            Annotated[ObjectV215635, _VARIANT_15635]
            | Annotated[ObjectV115639, _VARIANT_15639],
            _VARIANT_15634,
        ]
        | Annotated[str, _VARIANT_15643]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_15644,
        ]
        | Annotated[float, _VARIANT_15645]
        | Annotated[Bool15646, _VARIANT_15646]
        | Annotated[
            tuple[
                Annotated[ObjectV215649, _VARIANT_15649]
                | Annotated[ObjectV115653, _VARIANT_15653],
                ...,
            ],
            _VARIANT_15647,
        ]
        | Annotated[tuple[str, ...], _VARIANT_15657]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_15659,
        ]
        | Annotated[tuple[float, ...], _VARIANT_15661]
        | Annotated[tuple[Element15664, ...], _VARIANT_15663]
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


class Script15624(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "REFR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags15626
    """Value decoded from this schema node."""

    properties: tuple[Property15628, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15626]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property15628, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15620(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="REFR/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("REFR/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="REFR/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script15624, ...]
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
    ) -> _base.FieldRef[tuple[Script15624, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15668(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/3:Bound Half Extents/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="REFR/3:Bound Half Extents/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="REFR/3:Bound Half Extents/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="REFR/3:Bound Half Extents/payload/2:Z",
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


class Bounds15674(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/4:Primitive/payload/0:Bounds"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="REFR/4:Primitive/payload/0:Bounds/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="REFR/4:Primitive/payload/0:Bounds/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="REFR/4:Primitive/payload/0:Bounds/2:Z",
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


class Color15678(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/4:Primitive/payload/1:Color"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="REFR/4:Primitive/payload/1:Color/0:Red",
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path="REFR/4:Primitive/payload/1:Color/1:Green",
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path="REFR/4:Primitive/payload/1:Color/2:Blue",
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


class Type15683(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    BOX = 1
    SPHERE = 2
    PORTAL_BOX = 3
    UNKNOWN_4 = 4


class Structure15673(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/4:Primitive/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "bounds": _base.Binding(
            path="REFR/4:Primitive/payload/0:Bounds",
            kind="struct",
            name="Bounds",
        ),
        "color": _base.Binding(
            path="REFR/4:Primitive/payload/1:Color",
            kind="struct",
            name="Color",
        ),
        "unknown": _base.Binding(
            path="REFR/4:Primitive/payload/2:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "type": _base.Binding(
            path="REFR/4:Primitive/payload/3:Type",
            kind="primitive",
            name="Type",
        ),
    }

    bounds: Bounds15674
    """Value decoded from this schema node."""

    color: Color15678
    """Value decoded from this schema node."""

    unknown: float
    """Value decoded from this schema node."""

    type: Type15683
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["bounds"]) -> _base.FieldRef[Bounds15674]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["color"]) -> _base.FieldRef[Color15678]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type15683]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Size15689(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/6:Occlusion Plane Data/payload/0:Size"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "width": _base.Binding(
            path=("REFR/6:Occlusion Plane Data/payload/0:Size/0:Width"),
            kind="primitive",
            name="Width",
        ),
        "height": _base.Binding(
            path=("REFR/6:Occlusion Plane Data/payload/0:Size/1:Height"),
            kind="primitive",
            name="Height",
        ),
    }

    width: float
    """Value decoded from this schema node."""

    height: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["width"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Position15692(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/6:Occlusion Plane Data/payload/1:Position"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("REFR/6:Occlusion Plane Data/payload/1:Position/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("REFR/6:Occlusion Plane Data/payload/1:Position/1:Y"),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=("REFR/6:Occlusion Plane Data/payload/1:Position/2:Z"),
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


class RotationQuaternion15696(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/6:Occlusion Plane Data/payload/2:Rotation (Quaternion?)"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "q1": _base.Binding(
            path=(
                "REFR/6:Occlusion Plane Data/payload/2:Rotation (Quater"
                "nion?)/0:q1"
            ),
            kind="primitive",
            name="q1",
        ),
        "q2": _base.Binding(
            path=(
                "REFR/6:Occlusion Plane Data/payload/2:Rotation (Quater"
                "nion?)/1:q2"
            ),
            kind="primitive",
            name="q2",
        ),
        "q3": _base.Binding(
            path=(
                "REFR/6:Occlusion Plane Data/payload/2:Rotation (Quater"
                "nion?)/2:q3"
            ),
            kind="primitive",
            name="q3",
        ),
        "q4": _base.Binding(
            path=(
                "REFR/6:Occlusion Plane Data/payload/2:Rotation (Quater"
                "nion?)/3:q4"
            ),
            kind="primitive",
            name="q4",
        ),
    }

    q1: float
    """Value decoded from this schema node."""

    q2: float
    """Value decoded from this schema node."""

    q3: float
    """Value decoded from this schema node."""

    q4: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["q1"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["q2"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["q3"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["q4"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15688(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/6:Occlusion Plane Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "size": _base.Binding(
            path="REFR/6:Occlusion Plane Data/payload/0:Size",
            kind="struct",
            name="Size",
        ),
        "position": _base.Binding(
            path="REFR/6:Occlusion Plane Data/payload/1:Position",
            kind="struct",
            name="Position",
        ),
        "rotation_quaternion": _base.Binding(
            path=(
                "REFR/6:Occlusion Plane Data/payload/2:Rotation (Quaternion?)"
            ),
            kind="struct",
            name="Rotation (Quaternion?)",
        ),
    }

    size: Size15689
    """Value decoded from this schema node."""

    position: Position15692
    """Value decoded from this schema node."""

    rotation_quaternion: RotationQuaternion15696
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["size"]) -> _base.FieldRef[Size15689]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position15692]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotation_quaternion"]
    ) -> _base.FieldRef[RotationQuaternion15696]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class References15703(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/7:Portal Data/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "origin": _base.Binding(
            path="REFR/7:Portal Data/payload/element/0:Origin",
            kind="primitive",
            name="Origin",
        ),
        "destination": _base.Binding(
            path="REFR/7:Portal Data/payload/element/1:Destination",
            kind="primitive",
            name="Destination",
        ),
    }

    origin: _values.FormId
    """Value decoded from this schema node."""

    destination: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["origin"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["destination"]
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


class Size15708(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/8:Room Portal (unused)/payload/0:Size"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "width": _base.Binding(
            path=("REFR/8:Room Portal (unused)/payload/0:Size/0:Width"),
            kind="primitive",
            name="Width",
        ),
        "height": _base.Binding(
            path=("REFR/8:Room Portal (unused)/payload/0:Size/1:Height"),
            kind="primitive",
            name="Height",
        ),
    }

    width: float
    """Value decoded from this schema node."""

    height: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["width"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["height"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Position15711(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/8:Room Portal (unused)/payload/1:Position"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("REFR/8:Room Portal (unused)/payload/1:Position/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("REFR/8:Room Portal (unused)/payload/1:Position/1:Y"),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=("REFR/8:Room Portal (unused)/payload/1:Position/2:Z"),
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


class RotationQuaternion15715(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/8:Room Portal (unused)/payload/2:Rotation (Quaternion?)"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "q1": _base.Binding(
            path=(
                "REFR/8:Room Portal (unused)/payload/2:Rotation (Quater"
                "nion?)/0:q1"
            ),
            kind="primitive",
            name="q1",
        ),
        "q2": _base.Binding(
            path=(
                "REFR/8:Room Portal (unused)/payload/2:Rotation (Quater"
                "nion?)/1:q2"
            ),
            kind="primitive",
            name="q2",
        ),
        "q3": _base.Binding(
            path=(
                "REFR/8:Room Portal (unused)/payload/2:Rotation (Quater"
                "nion?)/2:q3"
            ),
            kind="primitive",
            name="q3",
        ),
        "q4": _base.Binding(
            path=(
                "REFR/8:Room Portal (unused)/payload/2:Rotation (Quater"
                "nion?)/3:q4"
            ),
            kind="primitive",
            name="q4",
        ),
    }

    q1: float
    """Value decoded from this schema node."""

    q2: float
    """Value decoded from this schema node."""

    q3: float
    """Value decoded from this schema node."""

    q4: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["q1"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["q2"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["q3"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["q4"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15707(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/8:Room Portal (unused)/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "size": _base.Binding(
            path="REFR/8:Room Portal (unused)/payload/0:Size",
            kind="struct",
            name="Size",
        ),
        "position": _base.Binding(
            path="REFR/8:Room Portal (unused)/payload/1:Position",
            kind="struct",
            name="Position",
        ),
        "rotation_quaternion": _base.Binding(
            path=(
                "REFR/8:Room Portal (unused)/payload/2:Rotation (Quaternion?)"
            ),
            kind="struct",
            name="Rotation (Quaternion?)",
        ),
    }

    size: Size15708
    """Value decoded from this schema node."""

    position: Position15711
    """Value decoded from this schema node."""

    rotation_quaternion: RotationQuaternion15715
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["size"]) -> _base.FieldRef[Size15708]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position15711]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotation_quaternion"]
    ) -> _base.FieldRef[RotationQuaternion15715]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags15724(enum.IntFlag):
    """Named values from the pinned schema."""

    UNKNOWN_1 = 1
    UNKNOWN_2 = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    HAS_IMAGE_SPACE = 64
    HAS_LIGHTING_TEMPLATE = 128


class Structure15722(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/9:Bound Data/0:Header/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "linked_rooms_count": _base.Binding(
            path=("REFR/9:Bound Data/0:Header/payload/0:Linked Rooms Count"),
            kind="primitive",
            name="Linked Rooms Count",
        ),
        "flags": _base.Binding(
            path="REFR/9:Bound Data/0:Header/payload/1:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unknown": _base.Binding(
            path="REFR/9:Bound Data/0:Header/payload/2:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    linked_rooms_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    flags: Flags15724
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["linked_rooms_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15724]:
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


class BoundData15720(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/9:Bound Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="REFR/9:Bound Data/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "lighting_template": _base.Binding(
            path="REFR/9:Bound Data/1:Lighting Template",
            kind="subrecord",
            name="Lighting Template",
        ),
        "image_space": _base.Binding(
            path="REFR/9:Bound Data/2:Image Space",
            kind="subrecord",
            name="Image Space",
        ),
        "linked_rooms": _base.Binding(
            path="REFR/9:Bound Data/3:Linked Rooms",
            kind="repeat",
            name="Linked Rooms",
            repeated_path=(
                "REFR/9:Bound Data/3:Linked Rooms/repeat/0:Linked Room"
            ),
            child_kind="subrecord",
        ),
    }

    header: Optional[Structure15722] = None
    """Value decoded from this schema node."""

    lighting_template: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    image_space: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    linked_rooms: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure15722]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lighting_template"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["image_space"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["linked_rooms"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type15745(enum.IntFlag):
    """Named values from the pinned schema."""

    REFLECTION = 1
    REFRACTION = 2


class Structure15743(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/14:Reflected/Refracted By/repeat/0:Water/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path=(
                "REFR/14:Reflected/Refracted By/repeat/0:Water/payload/"
                "0:Reference"
            ),
            kind="primitive",
            name="Reference",
        ),
        "type": _base.Binding(
            path=(
                "REFR/14:Reflected/Refracted By/repeat/0:Water/payload/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
    }

    reference: _values.FormId
    """Value decoded from this schema node."""

    type: Optional[Type15745] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["type"]
    ) -> _base.FieldRef[Optional[Type15745]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15752(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/17:Light Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "fov_90": _base.Binding(
            path="REFR/17:Light Data/payload/0:FOV 90+/-",
            kind="primitive",
            name="FOV 90+/-",
        ),
        "fade_1_35": _base.Binding(
            path="REFR/17:Light Data/payload/1:Fade 1.35+/-",
            kind="primitive",
            name="Fade 1.35+/-",
        ),
        "end_distance_cap": _base.Binding(
            path="REFR/17:Light Data/payload/2:End Distance Cap",
            kind="primitive",
            name="End Distance Cap",
        ),
        "shadow_depth_bias": _base.Binding(
            path="REFR/17:Light Data/payload/3:Shadow Depth Bias",
            kind="primitive",
            name="Shadow Depth Bias",
        ),
        "unknown": _base.Binding(
            path="REFR/17:Light Data/payload/4:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    fov_90: float
    """Value decoded from this schema node."""

    fade_1_35: float
    """Value decoded from this schema node."""

    end_distance_cap: float
    """Value decoded from this schema node."""

    shadow_depth_bias: float
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["fov_90"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fade_1_35"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["end_distance_cap"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["shadow_depth_bias"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
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


class Structure15759(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/18:Alpha/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "cutoff": _base.Binding(
            path="REFR/18:Alpha/payload/0:Cutoff",
            kind="primitive",
            name="Cutoff",
        ),
        "base": _base.Binding(
            path="REFR/18:Alpha/payload/1:Base",
            kind="primitive",
            name="Base",
        ),
    }

    cutoff: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    base: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["cutoff"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base"]
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


class Position15766(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/19:Teleport Destination/payload/1:Position/Rotation/0:Position"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/0:Position/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/0:Position/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/0:Position/2:Z"
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


class Rotation15770(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/19:Teleport Destination/payload/1:Position/Rotation/1:Rotation"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/1:Rotation/0:X"
            ),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/1:Rotation/1:Y"
            ),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/1:Rotation/2:Z"
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


class PositionRotation15765(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/19:Teleport Destination/payload/1:Position/Rotation"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "position": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/0:Position"
            ),
            kind="struct",
            name="Position",
        ),
        "rotation": _base.Binding(
            path=(
                "REFR/19:Teleport Destination/payload/1:Position/Rotati"
                "on/1:Rotation"
            ),
            kind="struct",
            name="Rotation",
        ),
    }

    position: Position15766
    """Value decoded from this schema node."""

    rotation: Rotation15770
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position15766]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotation"]) -> _base.FieldRef[Rotation15770]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags15774(enum.IntFlag):
    """Named values from the pinned schema."""

    NO_ALARM = 1


class Structure15763(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/19:Teleport Destination/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "door": _base.Binding(
            path="REFR/19:Teleport Destination/payload/0:Door",
            kind="primitive",
            name="Door",
        ),
        "position_rotation": _base.Binding(
            path=("REFR/19:Teleport Destination/payload/1:Position/Rotation"),
            kind="struct",
            name="Position/Rotation",
        ),
        "flags": _base.Binding(
            path="REFR/19:Teleport Destination/payload/2:Flags",
            kind="primitive",
            name="Flags",
        ),
    }

    door: _values.FormId
    """Value decoded from this schema node."""

    position_rotation: PositionRotation15765
    """Value decoded from this schema node."""

    flags: Flags15774
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["door"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["position_rotation"]
    ) -> _base.FieldRef[PositionRotation15765]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15774]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LinearVelocity15785(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/24:Water Currents/payload/0:Linear Velocity"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("REFR/24:Water Currents/payload/0:Linear Velocity/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("REFR/24:Water Currents/payload/0:Linear Velocity/1:Y"),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=("REFR/24:Water Currents/payload/0:Linear Velocity/2:Z"),
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


class AngularVelocity15790(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/24:Water Currents/payload/2:Angular Velocity"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("REFR/24:Water Currents/payload/2:Angular Velocity/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("REFR/24:Water Currents/payload/2:Angular Velocity/1:Y"),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=("REFR/24:Water Currents/payload/2:Angular Velocity/2:Z"),
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


class UnknownVelocity15795(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/24:Water Currents/payload/4:Unknown Velocity"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("REFR/24:Water Currents/payload/4:Unknown Velocity/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("REFR/24:Water Currents/payload/4:Unknown Velocity/1:Y"),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=("REFR/24:Water Currents/payload/4:Unknown Velocity/2:Z"),
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


class Structure15784(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/24:Water Currents/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "linear_velocity": _base.Binding(
            path="REFR/24:Water Currents/payload/0:Linear Velocity",
            kind="struct",
            name="Linear Velocity",
        ),
        "unknown": _base.Binding(
            path="REFR/24:Water Currents/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "angular_velocity": _base.Binding(
            path="REFR/24:Water Currents/payload/2:Angular Velocity",
            kind="struct",
            name="Angular Velocity",
        ),
        "unknown_15794": _base.Binding(
            path="REFR/24:Water Currents/payload/3:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "unknown_velocity": _base.Binding(
            path="REFR/24:Water Currents/payload/4:Unknown Velocity",
            kind="struct",
            name="Unknown Velocity",
        ),
        "unknown_15799": _base.Binding(
            path="REFR/24:Water Currents/payload/5:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    linear_velocity: LinearVelocity15785
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    angular_velocity: AngularVelocity15790
    """Value decoded from this schema node."""

    unknown_15794: bytes
    """Value decoded from this schema node."""

    unknown_velocity: UnknownVelocity15795
    """Value decoded from this schema node."""

    unknown_15799: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["linear_velocity"]
    ) -> _base.FieldRef[LinearVelocity15785]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["angular_velocity"]
    ) -> _base.FieldRef[AngularVelocity15790]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15794"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_velocity"]
    ) -> _base.FieldRef[UnknownVelocity15795]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_15799"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure15801(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/25:Water Current Linear Velocity/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="REFR/25:Water Current Linear Velocity/payload/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="REFR/25:Water Current Linear Velocity/payload/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="REFR/25:Water Current Linear Velocity/payload/2:Z",
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


class Structure15806(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/26:Water Current Rotational Velocity/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path=("REFR/26:Water Current Rotational Velocity/payload/0:X"),
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path=("REFR/26:Water Current Rotational Velocity/payload/1:Y"),
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path=("REFR/26:Water Current Rotational Velocity/payload/2:Z"),
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


class ParentActivateOnly15822(enum.IntFlag):
    """Named values from the pinned schema."""

    PARENT_ACTIVATE_ONLY = 1


class Structure15825(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/32:Activate Parents/1:Activate Parent Refs/repeat"
        "/0:Activate Parent Ref/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path=(
                "REFR/32:Activate Parents/1:Activate Parent Refs/repeat"
                "/0:Activate Parent Ref/payload/0:Reference"
            ),
            kind="primitive",
            name="Reference",
        ),
        "delay": _base.Binding(
            path=(
                "REFR/32:Activate Parents/1:Activate Parent Refs/repeat"
                "/0:Activate Parent Ref/payload/1:Delay"
            ),
            kind="primitive",
            name="Delay",
        ),
    }

    reference: _values.FormId
    """Value decoded from this schema node."""

    delay: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["delay"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ActivateParents15820(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/32:Activate Parents"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="REFR/32:Activate Parents/0:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "activate_parent_refs": _base.Binding(
            path="REFR/32:Activate Parents/1:Activate Parent Refs",
            kind="repeat",
            name="Activate Parent Refs",
            repeated_path=(
                "REFR/32:Activate Parents/1:Activate Parent Refs/repeat"
                "/0:Activate Parent Ref"
            ),
            child_kind="subrecord",
        ),
    }

    flags: Optional[ParentActivateOnly15822] = None
    """Value decoded from this schema node."""

    activate_parent_refs: tuple[Structure15825, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[ParentActivateOnly15822]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["activate_parent_refs"]
    ) -> _base.FieldRef[tuple[Structure15825, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class EasyMediumHardVeryHard15831(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EASY = 0
    MEDIUM = 1
    HARD = 2
    VERY_HARD = 3


class Level15838(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NOVICE = 1
    APPRENTICE = 25
    ADEPT = 50
    EXPERT = 75
    MASTER = 100
    REQUIRES_KEY = 255


class Flags15841(enum.IntFlag):
    """Named values from the pinned schema."""

    VALUE = 1
    VALUE_1 = 2
    LEVELED_LOCK = 4


class Structure15837(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/37:Lock Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "level": _base.Binding(
            path="REFR/37:Lock Data/payload/0:Level",
            kind="primitive",
            name="Level",
        ),
        "unused": _base.Binding(
            path="REFR/37:Lock Data/payload/1:Unused",
            kind="primitive",
            name="Unused",
        ),
        "key": _base.Binding(
            path="REFR/37:Lock Data/payload/2:Key",
            kind="primitive",
            name="Key",
        ),
        "flags": _base.Binding(
            path="REFR/37:Lock Data/payload/3:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unused_15842": _base.Binding(
            path="REFR/37:Lock Data/payload/4:Unused",
            kind="primitive",
            name="Unused",
        ),
        "unused_15843": _base.Binding(
            path="REFR/37:Lock Data/payload/5:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    level: Level15838
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    key: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags15841
    """Value decoded from this schema node."""

    unused_15842: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_15843: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["level"]) -> _base.FieldRef[Level15838]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["key"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15841]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_15842"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_15843"]
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


class Structure15847(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/39:Navmesh Door Link/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "navmesh": _base.Binding(
            path="REFR/39:Navmesh Door Link/payload/0:Navmesh",
            kind="primitive",
            name="Navmesh",
        ),
        "teleport_marker_triangle": _base.Binding(
            path=(
                "REFR/39:Navmesh Door Link/payload/1:Teleport Marker Triangle"
            ),
            kind="primitive",
            name="Teleport Marker Triangle",
        ),
        "unused": _base.Binding(
            path="REFR/39:Navmesh Door Link/payload/2:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    navmesh: _values.FormId
    """Value decoded from this schema node."""

    teleport_marker_triangle: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["navmesh"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["teleport_marker_triangle"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
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


class Ownership15856(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/42:Ownership"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path="REFR/42:Ownership/0:Owner",
            kind="subrecord",
            name="Owner",
        ),
        "faction_rank": _base.Binding(
            path="REFR/42:Ownership/1:Faction rank",
            kind="subrecord",
            name="Faction rank",
        ),
    }

    owner: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    faction_rank: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["owner"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["faction_rank"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ]
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


class Flags15870(enum.IntFlag):
    """Named values from the pinned schema."""

    SET_ENABLE_STATE_TO_OPPOSITE_OF_PARENT = 1
    POP_IN = 2


class Structure15868(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/46:Enable Parent/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path="REFR/46:Enable Parent/payload/0:Reference",
            kind="primitive",
            name="Reference",
        ),
        "flags": _base.Binding(
            path="REFR/46:Enable Parent/payload/1:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unused": _base.Binding(
            path="REFR/46:Enable Parent/payload/2:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    reference: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags15870
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15870]:
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


class Structure15874(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/47:Linked References/repeat/0:Linked Reference/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "keyword_ref": _base.Binding(
            path=(
                "REFR/47:Linked References/repeat/0:Linked Reference/pa"
                "yload/0:Keyword/Ref"
            ),
            kind="primitive",
            name="Keyword/Ref",
        ),
        "ref": _base.Binding(
            path=(
                "REFR/47:Linked References/repeat/0:Linked Reference/pa"
                "yload/1:Ref"
            ),
            kind="primitive",
            name="Ref",
        ),
    }

    keyword_ref: _values.FormId
    """Value decoded from this schema node."""

    ref: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["keyword_ref"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ref"]
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


class Type15892(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TOPIC_REF = 0
    TOPIC_SUBTYPE = 1


_VARIANT_15894: _base.Variant = _base.Variant(
    path=(
        "REFR/48:Patrol/repeat/0:Data/5:Topic/repeat/0:Topic Da"
        "ta/payload/1:Data/variants/0:Topic"
    )
)


_VARIANT_15895: _base.Variant = _base.Variant(
    path=(
        "REFR/48:Patrol/repeat/0:Data/5:Topic/repeat/0:Topic Da"
        "ta/payload/1:Data/variants/1:Subtype"
    )
)


class Structure15891(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "REFR/48:Patrol/repeat/0:Data/5:Topic/repeat/0:Topic Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "REFR/48:Patrol/repeat/0:Data/5:Topic/repeat/0:Topic Da"
                "ta/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "data": _base.Binding(
            path=(
                "REFR/48:Patrol/repeat/0:Data/5:Topic/repeat/0:Topic Da"
                "ta/payload/1:Data"
            ),
            kind="union",
            name="Data",
        ),
    }

    type: Type15892
    """Value decoded from this schema node."""

    data: (
        Annotated[_values.FormId, _VARIANT_15894]
        | Annotated[str, _VARIANT_15895]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type15892]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_15894]
        | Annotated[str, _VARIANT_15895]
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


class Data15878(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/48:Patrol/repeat/0:Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "idle_time": _base.Binding(
            path="REFR/48:Patrol/repeat/0:Data/0:Idle Time",
            kind="subrecord",
            name="Idle Time",
        ),
        "patrol_script_marker": _base.Binding(
            path=("REFR/48:Patrol/repeat/0:Data/1:Patrol Script Marker"),
            kind="subrecord",
            name="Patrol Script Marker",
        ),
        "idle": _base.Binding(
            path="REFR/48:Patrol/repeat/0:Data/2:Idle",
            kind="subrecord",
            name="Idle",
        ),
        "unused": _base.Binding(
            path="REFR/48:Patrol/repeat/0:Data/3:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_15887": _base.Binding(
            path="REFR/48:Patrol/repeat/0:Data/4:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "topic": _base.Binding(
            path="REFR/48:Patrol/repeat/0:Data/5:Topic",
            kind="repeat",
            name="Topic",
            repeated_path=(
                "REFR/48:Patrol/repeat/0:Data/5:Topic/repeat/0:Topic Data"
            ),
            child_kind="subrecord",
        ),
    }

    idle_time: Optional[float] = None
    """Value decoded from this schema node."""

    patrol_script_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    idle: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_15887: Optional[bytes] = None
    """Value decoded from this schema node."""

    topic: tuple[Structure15891, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["idle_time"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["patrol_script_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["idle"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_15887"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[tuple[Structure15891, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class UseDefaultActivateOpenOpenByDefault15897(enum.IntFlag):
    """Named values from the pinned schema."""

    USE_DEFAULT = 1
    ACTIVATE = 2
    OPEN = 4
    OPEN_BY_DEFAULT = 8


class VisibleCanTravelToShowAllHidden15908(enum.IntFlag):
    """Named values from the pinned schema."""

    VISIBLE = 1
    CAN_TRAVEL_TO = 2
    SHOW_ALL_HIDDEN = 4


class Type15913(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    CITY = 1
    TOWN = 2
    SETTLEMENT = 3
    CAVE = 4
    CAMP = 5
    FORT = 6
    NORDIC_RUINS = 7
    DWEMER_RUIN = 8
    SHIPWRECK = 9
    GROVE = 10
    LANDMARK = 11
    DRAGON_LAIR = 12
    FARM = 13
    WOOD_MILL = 14
    MINE = 15
    IMPERIAL_CAMP = 16
    STORMCLOAK_CAMP = 17
    DOOMSTONE = 18
    WHEAT_MILL = 19
    SMELTER = 20
    STABLE = 21
    IMPERIAL_TOWER = 22
    CLEARING = 23
    PASS = 24
    ALTAR = 25
    ROCK = 26
    LIGHTHOUSE = 27
    ORC_STRONGHOLD = 28
    GIANT_CAMP = 29
    SHACK = 30
    NORDIC_TOWER = 31
    NORDIC_DWELLING = 32
    DOCKS = 33
    SHRINE = 34
    RIFTEN_CASTLE = 35
    RIFTEN_CAPITOL = 36
    WINDHELM_CASTLE = 37
    WINDHELM_CAPITOL = 38
    WHITERUN_CASTLE = 39
    WHITERUN_CAPITOL = 40
    SOLITUDE_CASTLE = 41
    SOLITUDE_CAPITOL = 42
    MARKARTH_CASTLE = 43
    MARKARTH_CAPITOL = 44
    WINTERHOLD_CASTLE = 45
    WINTERHOLD_CAPITOL = 46
    MORTHAL_CASTLE = 47
    MORTHAL_CAPITOL = 48
    FALKREATH_CASTLE = 49
    FALKREATH_CAPITOL = 50
    DAWNSTAR_CASTLE = 51
    DAWNSTAR_CAPITOL = 52
    DLC02_TEMPLE_OF_MIRAAK = 53
    DLC02_RAVEN_ROCK = 54
    DLC02_BEAST_STONE = 55
    DLC02_TEL_MITHRYN = 56
    DLC02_TO_SKYRIM = 57
    DLC02_TO_SOLSTHEIM = 58
    DLC02_CASTLE_KARSTAAG = 59


class Structure15912(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/53:Map Marker/3:TNAM/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path="REFR/53:Map Marker/3:TNAM/payload/0:Type",
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path="REFR/53:Map Marker/3:TNAM/payload/1:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    type: Type15913
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type15913]:
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


class MapMarker15904(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/53:Map Marker"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "map_marker_data": _base.Binding(
            path="REFR/53:Map Marker/0:Map Marker Data",
            kind="subrecord",
            name="Map Marker Data",
        ),
        "map_flags": _base.Binding(
            path="REFR/53:Map Marker/1:Map Flags",
            kind="subrecord",
            name="Map Flags",
        ),
        "name": _base.Binding(
            path="REFR/53:Map Marker/2:Name",
            kind="subrecord",
            name="Name",
        ),
        "tnam": _base.Binding(
            path="REFR/53:Map Marker/3:TNAM",
            kind="subrecord",
            name="TNAM",
        ),
    }

    map_marker_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    map_flags: Optional[VisibleCanTravelToShowAllHidden15908] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    tnam: Optional[Structure15912] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["map_marker_data"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["map_flags"]
    ) -> _base.FieldRef[Optional[VisibleCanTravelToShowAllHidden15908]]:
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
        self, name: Literal["tnam"]
    ) -> _base.FieldRef[Optional[Structure15912]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Position15922(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/56:Position/Rotation/payload/0:Position"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="REFR/56:Position/Rotation/payload/0:Position/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="REFR/56:Position/Rotation/payload/0:Position/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="REFR/56:Position/Rotation/payload/0:Position/2:Z",
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


class Rotation15926(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/56:Position/Rotation/payload/1:Rotation"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="REFR/56:Position/Rotation/payload/1:Rotation/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="REFR/56:Position/Rotation/payload/1:Rotation/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="REFR/56:Position/Rotation/payload/1:Rotation/2:Z",
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


class Structure15921(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR/56:Position/Rotation/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "position": _base.Binding(
            path="REFR/56:Position/Rotation/payload/0:Position",
            kind="struct",
            name="Position",
        ),
        "rotation": _base.Binding(
            path="REFR/56:Position/Rotation/payload/1:Rotation",
            kind="struct",
            name="Rotation",
        ),
    }

    position: Position15922
    """Value decoded from this schema node."""

    rotation: Rotation15926
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position15922]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotation"]) -> _base.FieldRef[Rotation15926]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class PlacedObjectRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REFR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "REFR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="REFR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="REFR/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "base": _base.Binding(
            path="REFR/2:Base",
            kind="subrecord",
            name="Base",
        ),
        "bound_half_extents": _base.Binding(
            path="REFR/3:Bound Half Extents",
            kind="subrecord",
            name="Bound Half Extents",
        ),
        "primitive": _base.Binding(
            path="REFR/4:Primitive",
            kind="subrecord",
            name="Primitive",
        ),
        "linked_occlusion_references": _base.Binding(
            path="REFR/5:Linked Occlusion References",
            kind="subrecord",
            name="Linked Occlusion References",
        ),
        "occlusion_plane_data": _base.Binding(
            path="REFR/6:Occlusion Plane Data",
            kind="subrecord",
            name="Occlusion Plane Data",
        ),
        "portal_data": _base.Binding(
            path="REFR/7:Portal Data",
            kind="subrecord",
            name="Portal Data",
        ),
        "room_portal_unused": _base.Binding(
            path="REFR/8:Room Portal (unused)",
            kind="subrecord",
            name="Room Portal (unused)",
        ),
        "bound_data": _base.Binding(
            path="REFR/9:Bound Data",
            kind="sequence",
            name="Bound Data",
        ),
        "multi_bound_primitive_marker": _base.Binding(
            path="REFR/10:MultiBound Primitive Marker",
            kind="subrecord",
            name="MultiBound Primitive Marker",
        ),
        "ragdoll_data": _base.Binding(
            path="REFR/11:Ragdoll Data",
            kind="subrecord",
            name="Ragdoll Data",
        ),
        "ragdoll_biped_data": _base.Binding(
            path="REFR/12:Ragdoll Biped Data",
            kind="subrecord",
            name="Ragdoll Biped Data",
        ),
        "radius": _base.Binding(
            path="REFR/13:Radius",
            kind="subrecord",
            name="Radius",
        ),
        "reflected_refracted_by": _base.Binding(
            path="REFR/14:Reflected/Refracted By",
            kind="repeat",
            name="Reflected/Refracted By",
            repeated_path="REFR/14:Reflected/Refracted By/repeat/0:Water",
            child_kind="subrecord",
        ),
        "lit_water": _base.Binding(
            path="REFR/15:Lit Water",
            kind="repeat",
            name="Lit Water",
            repeated_path="REFR/15:Lit Water/repeat/0:Water",
            child_kind="subrecord",
        ),
        "emittance": _base.Binding(
            path="REFR/16:Emittance",
            kind="subrecord",
            name="Emittance",
        ),
        "light_data": _base.Binding(
            path="REFR/17:Light Data",
            kind="subrecord",
            name="Light Data",
        ),
        "alpha": _base.Binding(
            path="REFR/18:Alpha",
            kind="subrecord",
            name="Alpha",
        ),
        "teleport_destination": _base.Binding(
            path="REFR/19:Teleport Destination",
            kind="subrecord",
            name="Teleport Destination",
        ),
        "teleport_message_box": _base.Binding(
            path="REFR/20:Teleport Message Box",
            kind="subrecord",
            name="Teleport Message Box",
        ),
        "multi_bound_reference": _base.Binding(
            path="REFR/21:MultiBound Reference",
            kind="subrecord",
            name="MultiBound Reference",
        ),
        "water_current_count": _base.Binding(
            path="REFR/22:Water Current Count",
            kind="subrecord",
            name="Water Current Count",
        ),
        "water_current_count_old": _base.Binding(
            path="REFR/23:Water Current Count (Old)",
            kind="subrecord",
            name="Water Current Count (Old)",
        ),
        "water_currents": _base.Binding(
            path="REFR/24:Water Currents",
            kind="subrecord",
            name="Water Currents",
        ),
        "water_current_linear_velocity": _base.Binding(
            path="REFR/25:Water Current Linear Velocity",
            kind="subrecord",
            name="Water Current Linear Velocity",
        ),
        "water_current_rotational_velocity": _base.Binding(
            path="REFR/26:Water Current Rotational Velocity",
            kind="subrecord",
            name="Water Current Rotational Velocity",
        ),
        "water_current_zone_cell": _base.Binding(
            path="REFR/27:Water Current Zone Cell",
            kind="subrecord",
            name="Water Current Zone Cell",
        ),
        "water_current_zone_reference": _base.Binding(
            path="REFR/28:Water Current Zone Reference",
            kind="subrecord",
            name="Water Current Zone Reference",
        ),
        "water_current_zone_action": _base.Binding(
            path="REFR/29:Water Current Zone Action",
            kind="subrecord",
            name="Water Current Zone Action",
        ),
        "scale": _base.Binding(
            path="REFR/30:Scale",
            kind="subrecord",
            name="Scale",
        ),
        "spawn_container": _base.Binding(
            path="REFR/31:Spawn Container",
            kind="subrecord",
            name="Spawn Container",
        ),
        "activate_parents": _base.Binding(
            path="REFR/32:Activate Parents",
            kind="sequence",
            name="Activate Parents",
        ),
        "leveled_item_base_object": _base.Binding(
            path="REFR/33:Leveled Item Base Object",
            kind="subrecord",
            name="Leveled Item Base Object",
        ),
        "level_modifier": _base.Binding(
            path="REFR/34:Level Modifier",
            kind="subrecord",
            name="Level Modifier",
        ),
        "persistent_location": _base.Binding(
            path="REFR/35:Persistent Location",
            kind="subrecord",
            name="Persistent Location",
        ),
        "collision_layer": _base.Binding(
            path="REFR/36:Collision Layer",
            kind="subrecord",
            name="Collision Layer",
        ),
        "lock_data": _base.Binding(
            path="REFR/37:Lock Data",
            kind="subrecord",
            name="Lock Data",
        ),
        "encounter_zone": _base.Binding(
            path="REFR/38:Encounter Zone",
            kind="subrecord",
            name="Encounter Zone",
        ),
        "navmesh_door_link": _base.Binding(
            path="REFR/39:Navmesh Door Link",
            kind="subrecord",
            name="Navmesh Door Link",
        ),
        "location_ref_type": _base.Binding(
            path="REFR/40:Location Ref Type",
            kind="subrecord",
            name="Location Ref Type",
        ),
        "ignored_by_sandbox": _base.Binding(
            path="REFR/41:Ignored by Sandbox",
            kind="subrecord",
            name="Ignored by Sandbox",
        ),
        "ownership": _base.Binding(
            path="REFR/42:Ownership",
            kind="sequence",
            name="Ownership",
        ),
        "item_count": _base.Binding(
            path="REFR/43:Item Count",
            kind="subrecord",
            name="Item Count",
        ),
        "charge": _base.Binding(
            path="REFR/44:Charge",
            kind="subrecord",
            name="Charge",
        ),
        "location_reference": _base.Binding(
            path="REFR/45:Location Reference",
            kind="subrecord",
            name="Location Reference",
        ),
        "enable_parent": _base.Binding(
            path="REFR/46:Enable Parent",
            kind="subrecord",
            name="Enable Parent",
        ),
        "linked_references": _base.Binding(
            path="REFR/47:Linked References",
            kind="repeat",
            name="Linked References",
            repeated_path=(
                "REFR/47:Linked References/repeat/0:Linked Reference"
            ),
            child_kind="subrecord",
        ),
        "patrol": _base.Binding(
            path="REFR/48:Patrol",
            kind="repeat",
            name="Patrol",
            repeated_path="REFR/48:Patrol/repeat/0:Data",
            child_kind="sequence",
        ),
        "action_flag": _base.Binding(
            path="REFR/49:Action Flag",
            kind="subrecord",
            name="Action Flag",
        ),
        "head_tracking_weight": _base.Binding(
            path="REFR/50:Head-Tracking Weight",
            kind="subrecord",
            name="Head-Tracking Weight",
        ),
        "favor_cost": _base.Binding(
            path="REFR/51:Favor Cost",
            kind="subrecord",
            name="Favor Cost",
        ),
        "open_by_default": _base.Binding(
            path="REFR/52:Open by Default",
            kind="subrecord",
            name="Open by Default",
        ),
        "map_marker": _base.Binding(
            path="REFR/53:Map Marker",
            kind="sequence",
            name="Map Marker",
        ),
        "attach_ref": _base.Binding(
            path="REFR/54:Attach Ref",
            kind="subrecord",
            name="Attach Ref",
        ),
        "distant_lod_data": _base.Binding(
            path="REFR/55:Distant LOD Data",
            kind="subrecord",
            name="Distant LOD Data",
        ),
        "position_rotation": _base.Binding(
            path="REFR/56:Position/Rotation",
            kind="subrecord",
            name="Position/Rotation",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure15620] = None
    """Value decoded from this schema node."""

    base: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    bound_half_extents: Optional[Structure15668] = None
    """Value decoded from this schema node."""

    primitive: Optional[Structure15673] = None
    """Value decoded from this schema node."""

    linked_occlusion_references: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    occlusion_plane_data: Optional[Structure15688] = None
    """Value decoded from this schema node."""

    portal_data: Optional[tuple[References15703, ...]] = None
    """Value decoded from this schema node."""

    room_portal_unused: Optional[Structure15707] = None
    """Value decoded from this schema node."""

    bound_data: Optional[BoundData15720] = None
    """Value decoded from this schema node."""

    multi_bound_primitive_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    ragdoll_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    ragdoll_biped_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    radius: Optional[float] = None
    """Value decoded from this schema node."""

    reflected_refracted_by: tuple[Structure15743, ...] = ()
    """Value decoded from this schema node."""

    lit_water: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    emittance: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    light_data: Optional[Structure15752] = None
    """Value decoded from this schema node."""

    alpha: Optional[Structure15759] = None
    """Value decoded from this schema node."""

    teleport_destination: Optional[Structure15763] = None
    """Value decoded from this schema node."""

    teleport_message_box: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    multi_bound_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    water_current_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    water_current_count_old: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    water_currents: Optional[Structure15784] = None
    """Value decoded from this schema node."""

    water_current_linear_velocity: Optional[Structure15801] = None
    """Value decoded from this schema node."""

    water_current_rotational_velocity: Optional[Structure15806] = None
    """Value decoded from this schema node."""

    water_current_zone_cell: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    water_current_zone_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    water_current_zone_action: Optional[bytes] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    spawn_container: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    activate_parents: Optional[ActivateParents15820] = None
    """Value decoded from this schema node."""

    leveled_item_base_object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    level_modifier: Optional[EasyMediumHardVeryHard15831] = None
    """Value decoded from this schema node."""

    persistent_location: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    collision_layer: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    lock_data: Optional[Structure15837] = None
    """Value decoded from this schema node."""

    encounter_zone: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    navmesh_door_link: Optional[Structure15847] = None
    """Value decoded from this schema node."""

    location_ref_type: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    ignored_by_sandbox: Optional[bytes] = None
    """Value decoded from this schema node."""

    ownership: Optional[Ownership15856] = None
    """Value decoded from this schema node."""

    item_count: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    charge: Optional[float] = None
    """Value decoded from this schema node."""

    location_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    enable_parent: Optional[Structure15868] = None
    """Value decoded from this schema node."""

    linked_references: tuple[Structure15874, ...] = ()
    """Value decoded from this schema node."""

    patrol: tuple[Data15878, ...] = ()
    """Value decoded from this schema node."""

    action_flag: Optional[UseDefaultActivateOpenOpenByDefault15897] = None
    """Value decoded from this schema node."""

    head_tracking_weight: Optional[float] = None
    """Value decoded from this schema node."""

    favor_cost: Optional[float] = None
    """Value decoded from this schema node."""

    open_by_default: Optional[bytes] = None
    """Value decoded from this schema node."""

    map_marker: Optional[MapMarker15904] = None
    """Value decoded from this schema node."""

    attach_ref: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    distant_lod_data: Optional[tuple[float, ...]] = None
    """Value decoded from this schema node."""

    position_rotation: Optional[Structure15921] = None
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
    ) -> _base.FieldRef[Optional[Structure15620]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["base"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bound_half_extents"]
    ) -> _base.FieldRef[Optional[Structure15668]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["primitive"]
    ) -> _base.FieldRef[Optional[Structure15673]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["linked_occlusion_references"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["occlusion_plane_data"]
    ) -> _base.FieldRef[Optional[Structure15688]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["portal_data"]
    ) -> _base.FieldRef[Optional[tuple[References15703, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["room_portal_unused"]
    ) -> _base.FieldRef[Optional[Structure15707]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bound_data"]
    ) -> _base.FieldRef[Optional[BoundData15720]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["multi_bound_primitive_marker"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ragdoll_data"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ragdoll_biped_data"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["radius"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reflected_refracted_by"]
    ) -> _base.FieldRef[tuple[Structure15743, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lit_water"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["emittance"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["light_data"]
    ) -> _base.FieldRef[Optional[Structure15752]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alpha"]
    ) -> _base.FieldRef[Optional[Structure15759]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["teleport_destination"]
    ) -> _base.FieldRef[Optional[Structure15763]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["teleport_message_box"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["multi_bound_reference"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_count_old"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_currents"]
    ) -> _base.FieldRef[Optional[Structure15784]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_linear_velocity"]
    ) -> _base.FieldRef[Optional[Structure15801]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_rotational_velocity"]
    ) -> _base.FieldRef[Optional[Structure15806]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_zone_cell"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_zone_reference"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["water_current_zone_action"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["scale"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["spawn_container"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["activate_parents"]
    ) -> _base.FieldRef[Optional[ActivateParents15820]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["leveled_item_base_object"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["level_modifier"]
    ) -> _base.FieldRef[Optional[EasyMediumHardVeryHard15831]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["persistent_location"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["collision_layer"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lock_data"]
    ) -> _base.FieldRef[Optional[Structure15837]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["encounter_zone"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["navmesh_door_link"]
    ) -> _base.FieldRef[Optional[Structure15847]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location_ref_type"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ignored_by_sandbox"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ownership"]
    ) -> _base.FieldRef[Optional[Ownership15856]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["item_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["charge"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location_reference"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enable_parent"]
    ) -> _base.FieldRef[Optional[Structure15868]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["linked_references"]
    ) -> _base.FieldRef[tuple[Structure15874, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["patrol"]
    ) -> _base.FieldRef[tuple[Data15878, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["action_flag"]
    ) -> _base.FieldRef[Optional[UseDefaultActivateOpenOpenByDefault15897]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["head_tracking_weight"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["favor_cost"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["open_by_default"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["map_marker"]
    ) -> _base.FieldRef[Optional[MapMarker15904]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attach_ref"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["distant_lod_data"]
    ) -> _base.FieldRef[Optional[tuple[float, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["position_rotation"]
    ) -> _base.FieldRef[Optional[Structure15921]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
