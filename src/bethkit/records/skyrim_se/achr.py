"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags10(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type14(_values.OpenIntEnum):
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


class Flags15(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_17: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV219(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_19: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV123(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_23: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_18: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_27: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_28: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_29: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool30(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_30: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV233(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_33: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV137(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_37: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_31: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_41: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_43: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_45: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element48(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_47: _base.Variant = _base.Variant(
    path=(
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property12(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type14
    """Value decoded from this schema node."""

    flags: Flags15
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_17]
        | Annotated[
            Annotated[ObjectV219, _VARIANT_19]
            | Annotated[ObjectV123, _VARIANT_23],
            _VARIANT_18,
        ]
        | Annotated[str, _VARIANT_27]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_28,
        ]
        | Annotated[float, _VARIANT_29]
        | Annotated[Bool30, _VARIANT_30]
        | Annotated[
            tuple[
                Annotated[ObjectV233, _VARIANT_33]
                | Annotated[ObjectV137, _VARIANT_37],
                ...,
            ],
            _VARIANT_31,
        ]
        | Annotated[tuple[str, ...], _VARIANT_41]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_43,
        ]
        | Annotated[tuple[float, ...], _VARIANT_45]
        | Annotated[tuple[Element48, ...], _VARIANT_47]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type14]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags15]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_17]
        | Annotated[
            Annotated[ObjectV219, _VARIANT_19]
            | Annotated[ObjectV123, _VARIANT_23],
            _VARIANT_18,
        ]
        | Annotated[str, _VARIANT_27]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_28,
        ]
        | Annotated[float, _VARIANT_29]
        | Annotated[Bool30, _VARIANT_30]
        | Annotated[
            tuple[
                Annotated[ObjectV233, _VARIANT_33]
                | Annotated[ObjectV137, _VARIANT_37],
                ...,
            ],
            _VARIANT_31,
        ]
        | Annotated[tuple[str, ...], _VARIANT_41]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_43,
        ]
        | Annotated[tuple[float, ...], _VARIANT_45]
        | Annotated[tuple[Element48, ...], _VARIANT_47]
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


class Script8(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "ACHR/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags10
    """Value decoded from this schema node."""

    properties: tuple[Property12, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property12, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure4(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="ACHR/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("ACHR/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="ACHR/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script8, ...]
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
    ) -> _base.FieldRef[tuple[Script8, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Unused64(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/6:Patrol Data/3:Unused"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="ACHR/6:Patrol Data/3:Unused/0:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_67": _base.Binding(
            path="ACHR/6:Patrol Data/3:Unused/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_69": _base.Binding(
            path="ACHR/6:Patrol Data/3:Unused/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_71": _base.Binding(
            path="ACHR/6:Patrol Data/3:Unused/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_73": _base.Binding(
            path="ACHR/6:Patrol Data/3:Unused/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_67: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_69: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_71: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_73: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_67"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_69"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_71"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_73"]
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


class Type78(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TOPIC_REF = 0
    TOPIC_SUBTYPE = 1


_VARIANT_80: _base.Variant = _base.Variant(
    path=(
        "ACHR/6:Patrol Data/4:Topic/repeat/0:Topic Data/payload"
        "/1:Data/variants/0:Topic"
    )
)


_VARIANT_81: _base.Variant = _base.Variant(
    path=(
        "ACHR/6:Patrol Data/4:Topic/repeat/0:Topic Data/payload"
        "/1:Data/variants/1:Subtype"
    )
)


class Structure77(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/6:Patrol Data/4:Topic/repeat/0:Topic Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "ACHR/6:Patrol Data/4:Topic/repeat/0:Topic Data/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "data": _base.Binding(
            path=(
                "ACHR/6:Patrol Data/4:Topic/repeat/0:Topic Data/payload/1:Data"
            ),
            kind="union",
            name="Data",
        ),
    }

    type: Type78
    """Value decoded from this schema node."""

    data: Annotated[_values.FormId, _VARIANT_80] | Annotated[str, _VARIANT_81]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type78]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_80] | Annotated[str, _VARIANT_81]
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


class PatrolData57(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/6:Patrol Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "idle_time": _base.Binding(
            path="ACHR/6:Patrol Data/0:Idle Time",
            kind="subrecord",
            name="Idle Time",
        ),
        "patrol_script_marker": _base.Binding(
            path="ACHR/6:Patrol Data/1:Patrol Script Marker",
            kind="subrecord",
            name="Patrol Script Marker",
        ),
        "idle": _base.Binding(
            path="ACHR/6:Patrol Data/2:Idle",
            kind="subrecord",
            name="Idle",
        ),
        "unused": _base.Binding(
            path="ACHR/6:Patrol Data/3:Unused",
            kind="sequence",
            name="Unused",
        ),
        "topic": _base.Binding(
            path="ACHR/6:Patrol Data/4:Topic",
            kind="repeat",
            name="Topic",
            repeated_path="ACHR/6:Patrol Data/4:Topic/repeat/0:Topic Data",
            child_kind="subrecord",
        ),
        "topic_82": _base.Binding(
            path="ACHR/6:Patrol Data/5:Topic",
            kind="subrecord",
            name="Topic",
        ),
    }

    idle_time: Optional[float] = None
    """Value decoded from this schema node."""

    patrol_script_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    idle: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused: Optional[Unused64] = None
    """Value decoded from this schema node."""

    topic: tuple[Structure77, ...] = ()
    """Value decoded from this schema node."""

    topic_82: Optional[_values.FormId] = None
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
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[Optional[Unused64]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[tuple[Structure77, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic_82"]
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


class EasyMediumHardVeryHard85(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EASY = 0
    MEDIUM = 1
    HARD = 2
    VERY_HARD = 3


class Structure96(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/12:Linked References/repeat/0:Linked Reference/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "keyword_ref": _base.Binding(
            path=(
                "ACHR/12:Linked References/repeat/0:Linked Reference/pa"
                "yload/0:Keyword/Ref"
            ),
            kind="primitive",
            name="Keyword/Ref",
        ),
        "ref": _base.Binding(
            path=(
                "ACHR/12:Linked References/repeat/0:Linked Reference/pa"
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


class ParentActivateOnly101(enum.IntFlag):
    """Named values from the pinned schema."""

    PARENT_ACTIVATE_ONLY = 1


class Structure104(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/13:Activate Parents/1:Activate Parent Refs/repeat"
        "/0:Activate Parent Ref/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path=(
                "ACHR/13:Activate Parents/1:Activate Parent Refs/repeat"
                "/0:Activate Parent Ref/payload/0:Reference"
            ),
            kind="primitive",
            name="Reference",
        ),
        "delay": _base.Binding(
            path=(
                "ACHR/13:Activate Parents/1:Activate Parent Refs/repeat"
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


class ActivateParents99(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/13:Activate Parents"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="ACHR/13:Activate Parents/0:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "activate_parent_refs": _base.Binding(
            path="ACHR/13:Activate Parents/1:Activate Parent Refs",
            kind="repeat",
            name="Activate Parent Refs",
            repeated_path=(
                "ACHR/13:Activate Parents/1:Activate Parent Refs/repeat"
                "/0:Activate Parent Ref"
            ),
            child_kind="subrecord",
        ),
    }

    flags: Optional[ParentActivateOnly101] = None
    """Value decoded from this schema node."""

    activate_parent_refs: tuple[Structure104, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[ParentActivateOnly101]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["activate_parent_refs"]
    ) -> _base.FieldRef[tuple[Structure104, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LinkStartColor109(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/14:Linked Reference Color/payload/0:Link Start Color"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/0:Link Start Co"
                "lor/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/0:Link Start Co"
                "lor/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/0:Link Start Co"
                "lor/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/0:Link Start Co"
                "lor/3:Unused"
            ),
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


class LinkEndColor114(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "ACHR/14:Linked Reference Color/payload/1:Link End Color"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/1:Link End Color/0:Red"
            ),
            kind="primitive",
            name="Red",
        ),
        "green": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/1:Link End Colo"
                "r/1:Green"
            ),
            kind="primitive",
            name="Green",
        ),
        "blue": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/1:Link End Color/2:Blue"
            ),
            kind="primitive",
            name="Blue",
        ),
        "unused": _base.Binding(
            path=(
                "ACHR/14:Linked Reference Color/payload/1:Link End Colo"
                "r/3:Unused"
            ),
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


class Structure108(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/14:Linked Reference Color/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "link_start_color": _base.Binding(
            path=("ACHR/14:Linked Reference Color/payload/0:Link Start Color"),
            kind="struct",
            name="Link Start Color",
        ),
        "link_end_color": _base.Binding(
            path=("ACHR/14:Linked Reference Color/payload/1:Link End Color"),
            kind="struct",
            name="Link End Color",
        ),
    }

    link_start_color: LinkStartColor109
    """Value decoded from this schema node."""

    link_end_color: LinkEndColor114
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["link_start_color"]
    ) -> _base.FieldRef[LinkStartColor109]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["link_end_color"]
    ) -> _base.FieldRef[LinkEndColor114]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags137(enum.IntFlag):
    """Named values from the pinned schema."""

    SET_ENABLE_STATE_TO_OPPOSITE_OF_PARENT = 1
    POP_IN = 2


class Structure135(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/22:Enable Parent/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path="ACHR/22:Enable Parent/payload/0:Reference",
            kind="primitive",
            name="Reference",
        ),
        "flags": _base.Binding(
            path="ACHR/22:Enable Parent/payload/1:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unused": _base.Binding(
            path="ACHR/22:Enable Parent/payload/2:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    reference: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags137
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags137]:
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


class Ownership139(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/23:Ownership"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path="ACHR/23:Ownership/0:Owner",
            kind="subrecord",
            name="Owner",
        ),
        "faction_rank": _base.Binding(
            path="ACHR/23:Ownership/1:Faction rank",
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


class Position154(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/28:Position/Rotation/payload/0:Position"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/0:Position/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/0:Position/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/0:Position/2:Z",
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


class Rotation158(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/28:Position/Rotation/payload/1:Rotation"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/1:Rotation/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/1:Rotation/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/1:Rotation/2:Z",
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


class Structure153(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR/28:Position/Rotation/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "position": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/0:Position",
            kind="struct",
            name="Position",
        ),
        "rotation": _base.Binding(
            path="ACHR/28:Position/Rotation/payload/1:Rotation",
            kind="struct",
            name="Rotation",
        ),
    }

    position: Position154
    """Value decoded from this schema node."""

    rotation: Rotation158
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position154]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotation"]) -> _base.FieldRef[Rotation158]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class PlacedNpcRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "ACHR"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "ACHR"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="ACHR/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="ACHR/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "base": _base.Binding(
            path="ACHR/2:Base",
            kind="subrecord",
            name="Base",
        ),
        "encounter_zone": _base.Binding(
            path="ACHR/3:Encounter Zone",
            kind="subrecord",
            name="Encounter Zone",
        ),
        "ragdoll_data": _base.Binding(
            path="ACHR/4:Ragdoll Data",
            kind="subrecord",
            name="Ragdoll Data",
        ),
        "ragdoll_biped_data": _base.Binding(
            path="ACHR/5:Ragdoll Biped Data",
            kind="subrecord",
            name="Ragdoll Biped Data",
        ),
        "patrol_data": _base.Binding(
            path="ACHR/6:Patrol Data",
            kind="sequence",
            name="Patrol Data",
        ),
        "level_modifier": _base.Binding(
            path="ACHR/7:Level Modifier",
            kind="subrecord",
            name="Level Modifier",
        ),
        "merchant_container": _base.Binding(
            path="ACHR/8:Merchant Container",
            kind="subrecord",
            name="Merchant Container",
        ),
        "count": _base.Binding(
            path="ACHR/9:Count",
            kind="subrecord",
            name="Count",
        ),
        "radius": _base.Binding(
            path="ACHR/10:Radius",
            kind="subrecord",
            name="Radius",
        ),
        "health": _base.Binding(
            path="ACHR/11:Health",
            kind="subrecord",
            name="Health",
        ),
        "linked_references": _base.Binding(
            path="ACHR/12:Linked References",
            kind="repeat",
            name="Linked References",
            repeated_path=(
                "ACHR/12:Linked References/repeat/0:Linked Reference"
            ),
            child_kind="subrecord",
        ),
        "activate_parents": _base.Binding(
            path="ACHR/13:Activate Parents",
            kind="sequence",
            name="Activate Parents",
        ),
        "linked_reference_color": _base.Binding(
            path="ACHR/14:Linked Reference Color",
            kind="subrecord",
            name="Linked Reference Color",
        ),
        "persistent_location": _base.Binding(
            path="ACHR/15:Persistent Location",
            kind="subrecord",
            name="Persistent Location",
        ),
        "location_reference": _base.Binding(
            path="ACHR/16:Location Reference",
            kind="subrecord",
            name="Location Reference",
        ),
        "ignored_by_sandbox": _base.Binding(
            path="ACHR/17:Ignored by Sandbox",
            kind="subrecord",
            name="Ignored by Sandbox",
        ),
        "location_ref_type": _base.Binding(
            path="ACHR/18:Location Ref Type",
            kind="subrecord",
            name="Location Ref Type",
        ),
        "horse": _base.Binding(
            path="ACHR/19:Horse",
            kind="subrecord",
            name="Horse",
        ),
        "head_tracking_weight": _base.Binding(
            path="ACHR/20:Head-Tracking Weight",
            kind="subrecord",
            name="Head-Tracking Weight",
        ),
        "favor_cost": _base.Binding(
            path="ACHR/21:Favor Cost",
            kind="subrecord",
            name="Favor Cost",
        ),
        "enable_parent": _base.Binding(
            path="ACHR/22:Enable Parent",
            kind="subrecord",
            name="Enable Parent",
        ),
        "ownership": _base.Binding(
            path="ACHR/23:Ownership",
            kind="sequence",
            name="Ownership",
        ),
        "emittance": _base.Binding(
            path="ACHR/24:Emittance",
            kind="subrecord",
            name="Emittance",
        ),
        "multi_bound_reference": _base.Binding(
            path="ACHR/25:MultiBound Reference",
            kind="subrecord",
            name="MultiBound Reference",
        ),
        "ignored_by_sandbox_148": _base.Binding(
            path="ACHR/26:Ignored By Sandbox",
            kind="subrecord",
            name="Ignored By Sandbox",
        ),
        "scale": _base.Binding(
            path="ACHR/27:Scale",
            kind="subrecord",
            name="Scale",
        ),
        "position_rotation": _base.Binding(
            path="ACHR/28:Position/Rotation",
            kind="subrecord",
            name="Position/Rotation",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure4] = None
    """Value decoded from this schema node."""

    base: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    encounter_zone: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ragdoll_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    ragdoll_biped_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    patrol_data: Optional[PatrolData57] = None
    """Value decoded from this schema node."""

    level_modifier: Optional[EasyMediumHardVeryHard85] = None
    """Value decoded from this schema node."""

    merchant_container: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    radius: Optional[float] = None
    """Value decoded from this schema node."""

    health: Optional[float] = None
    """Value decoded from this schema node."""

    linked_references: tuple[Structure96, ...] = ()
    """Value decoded from this schema node."""

    activate_parents: Optional[ActivateParents99] = None
    """Value decoded from this schema node."""

    linked_reference_color: Optional[Structure108] = None
    """Value decoded from this schema node."""

    persistent_location: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    location_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ignored_by_sandbox: Optional[bytes] = None
    """Value decoded from this schema node."""

    location_ref_type: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    horse: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    head_tracking_weight: Optional[float] = None
    """Value decoded from this schema node."""

    favor_cost: Optional[float] = None
    """Value decoded from this schema node."""

    enable_parent: Optional[Structure135] = None
    """Value decoded from this schema node."""

    ownership: Optional[Ownership139] = None
    """Value decoded from this schema node."""

    emittance: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    multi_bound_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ignored_by_sandbox_148: Optional[bytes] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    position_rotation: Optional[Structure153] = None
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
    ) -> _base.FieldRef[Optional[Structure4]]:
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
        self, name: Literal["encounter_zone"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
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
    def field(
        self, name: Literal["patrol_data"]
    ) -> _base.FieldRef[Optional[PatrolData57]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["level_modifier"]
    ) -> _base.FieldRef[Optional[EasyMediumHardVeryHard85]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["merchant_container"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
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
    def field(self, name: Literal["radius"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["health"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["linked_references"]
    ) -> _base.FieldRef[tuple[Structure96, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["activate_parents"]
    ) -> _base.FieldRef[Optional[ActivateParents99]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["linked_reference_color"]
    ) -> _base.FieldRef[Optional[Structure108]]:
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
        self, name: Literal["location_reference"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
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
        self, name: Literal["location_ref_type"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["horse"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
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
        self, name: Literal["enable_parent"]
    ) -> _base.FieldRef[Optional[Structure135]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ownership"]
    ) -> _base.FieldRef[Optional[Ownership139]]:
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
        self, name: Literal["multi_bound_reference"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ignored_by_sandbox_148"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["scale"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["position_rotation"]
    ) -> _base.FieldRef[Optional[Structure153]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
