"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags10812(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type10816(_values.OpenIntEnum):
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


class Flags10817(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_10819: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV210821(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_10821: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV110825(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_10825: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_10820: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_10829: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_10830: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_10831: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool10832(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_10832: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV210835(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_10835: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV110839(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_10839: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_10833: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_10843: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_10845: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_10847: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element10850(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_10849: _base.Variant = _base.Variant(
    path=(
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property10814(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type10816
    """Value decoded from this schema node."""

    flags: Flags10817
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_10819]
        | Annotated[
            Annotated[ObjectV210821, _VARIANT_10821]
            | Annotated[ObjectV110825, _VARIANT_10825],
            _VARIANT_10820,
        ]
        | Annotated[str, _VARIANT_10829]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10830,
        ]
        | Annotated[float, _VARIANT_10831]
        | Annotated[Bool10832, _VARIANT_10832]
        | Annotated[
            tuple[
                Annotated[ObjectV210835, _VARIANT_10835]
                | Annotated[ObjectV110839, _VARIANT_10839],
                ...,
            ],
            _VARIANT_10833,
        ]
        | Annotated[tuple[str, ...], _VARIANT_10843]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_10845,
        ]
        | Annotated[tuple[float, ...], _VARIANT_10847]
        | Annotated[tuple[Element10850, ...], _VARIANT_10849]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type10816]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10817]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_10819]
        | Annotated[
            Annotated[ObjectV210821, _VARIANT_10821]
            | Annotated[ObjectV110825, _VARIANT_10825],
            _VARIANT_10820,
        ]
        | Annotated[str, _VARIANT_10829]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10830,
        ]
        | Annotated[float, _VARIANT_10831]
        | Annotated[Bool10832, _VARIANT_10832]
        | Annotated[
            tuple[
                Annotated[ObjectV210835, _VARIANT_10835]
                | Annotated[ObjectV110839, _VARIANT_10839],
                ...,
            ],
            _VARIANT_10833,
        ]
        | Annotated[tuple[str, ...], _VARIANT_10843]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_10845,
        ]
        | Annotated[tuple[float, ...], _VARIANT_10847]
        | Annotated[tuple[Element10850, ...], _VARIANT_10849]
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


class Script10810(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "MGEF/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags10812
    """Value decoded from this schema node."""

    properties: tuple[Property10814, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10812]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property10814, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure10806(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MGEF/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="MGEF/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("MGEF/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="MGEF/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script10810, ...]
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
    ) -> _base.FieldRef[tuple[Script10810, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags10863(enum.IntFlag):
    """Named values from the pinned schema."""

    HOSTILE = 1
    RECOVER = 2
    DETRIMENTAL = 4
    SNAP_TO_NAVMESH = 8
    NO_HIT_EVENT = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    UNKNOWN_8 = 128
    DISPEL_WITH_KEYWORDS = 256
    NO_DURATION = 512
    NO_MAGNITUDE = 1024
    NO_AREA = 2048
    FX_PERSIST = 4096
    UNKNOWN_14 = 8192
    GORY_VISUALS = 16384
    HIDE_IN_UI = 32768
    UNKNOWN_17 = 65536
    NO_RECAST = 131072
    UNKNOWN_19 = 262144
    UNKNOWN_20 = 524288
    UNKNOWN_21 = 1048576
    POWER_AFFECTS_MAGNITUDE = 2097152
    POWER_AFFECTS_DURATION = 4194304
    UNKNOWN_24 = 8388608
    UNKNOWN_25 = 16777216
    UNKNOWN_26 = 33554432
    PAINLESS = 67108864
    NO_HIT_EFFECT = 134217728
    NO_DEATH_DISPEL = 268435456
    UNKNOWN_30 = 536870912
    UNKNOWN_31 = 1073741824
    UNKNOWN_32 = 2147483648


_VARIANT_10866: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/0:Unused"
    )
)


_VARIANT_10867: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/1:Assoc. Item"
    )
)


_VARIANT_10868: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/2:Assoc. Item"
    )
)


_VARIANT_10869: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/3:Assoc. Item"
    )
)


_VARIANT_10870: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/4:Assoc. Item"
    )
)


_VARIANT_10871: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/5:Assoc. Item"
    )
)


_VARIANT_10872: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/6:Assoc. Item"
    )
)


_VARIANT_10873: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/7:Assoc. Item"
    )
)


_VARIANT_10874: _base.Variant = _base.Variant(
    path=(
        "MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item/"
        "variants/8:Assoc. Item"
    )
)


class MagicSkill10875(_values.OpenIntEnum):
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


class ResistValue10876(_values.OpenIntEnum):
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


class Spellmaking10884(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/6:Magic Effect Data/0:Data/payload/12:Spellmaking"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "area": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/12:Spellmaking/0:Area"
            ),
            kind="primitive",
            name="Area",
        ),
        "casting_time": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/12:Spellmaking"
                "/1:Casting Time"
            ),
            kind="primitive",
            name="Casting Time",
        ),
    }

    area: Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    """Value decoded from this schema node."""

    casting_time: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["area"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["casting_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Archtype10890(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    VALUE_MODIFIER = 0
    SCRIPT = 1
    DISPEL = 2
    CURE_DISEASE = 3
    ABSORB = 4
    DUAL_VALUE_MODIFIER = 5
    CALM = 6
    DEMORALIZE = 7
    FRENZY = 8
    DISARM = 9
    COMMAND_SUMMONED = 10
    INVISIBILITY = 11
    LIGHT = 12
    UNKNOWN_13 = 13
    UNKNOWN_14 = 14
    LOCK = 15
    OPEN = 16
    BOUND_WEAPON = 17
    SUMMON_CREATURE = 18
    DETECT_LIFE = 19
    TELEKINESIS = 20
    PARALYSIS = 21
    REANIMATE = 22
    SOUL_TRAP = 23
    TURN_UNDEAD = 24
    GUIDE = 25
    WEREWOLF_FEED = 26
    CURE_PARALYSIS = 27
    CURE_ADDICTION = 28
    CURE_POISON = 29
    CONCUSSION = 30
    VALUE_AND_PARTS = 31
    ACCUMULATE_MAGNITUDE = 32
    STAGGER = 33
    PEAK_VALUE_MODIFIER = 34
    CLOAK = 35
    WEREWOLF = 36
    SLOW_TIME = 37
    RALLY = 38
    ENHANCE_WEAPON = 39
    SPAWN_HAZARD = 40
    ETHEREALIZE = 41
    BANISH = 42
    SPAWN_SCRIPTED_REF = 43
    DISGUISE = 44
    GRAB_ACTOR = 45
    VAMPIRE_LORD = 46


class ActorValue10891(_values.OpenIntEnum):
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


class CastingType10894(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


class Delivery10895(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


class SecondActorValue10896(_values.OpenIntEnum):
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


class DualCasting10901(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/6:Magic Effect Data/0:Data/payload/27:Dual Casting"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "art": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/27:Dual Casting/0:Art"
            ),
            kind="primitive",
            name="Art",
        ),
        "scale": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/27:Dual Castin"
                "g/1:Scale"
            ),
            kind="primitive",
            name="Scale",
        ),
    }

    art: _values.FormId
    """Value decoded from this schema node."""

    scale: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["art"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["scale"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class CastingSoundLevel10910(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOUD = 0
    NORMAL = 1
    SILENT = 2
    VERY_LOUD = 3


class ScriptEffectAi10911(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/6:Magic Effect Data/0:Data/payload/35:Script Effect AI"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "score": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/35:Script Effe"
                "ct AI/0:Score"
            ),
            kind="primitive",
            name="Score",
        ),
        "delay_time": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/35:Script Effe"
                "ct AI/1:Delay Time"
            ),
            kind="primitive",
            name="Delay Time",
        ),
    }

    score: float
    """Value decoded from this schema node."""

    delay_time: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["score"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["delay_time"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure10862(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MGEF/6:Magic Effect Data/0:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="MGEF/6:Magic Effect Data/0:Data/payload/0:Flags",
            kind="primitive",
            name="Flags",
        ),
        "base_cost": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/1:Base Cost"),
            kind="primitive",
            name="Base Cost",
        ),
        "assoc_item": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/2:Assoc. Item"),
            kind="union",
            name="Assoc. Item",
        ),
        "magic_skill": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/3:Magic Skill"),
            kind="primitive",
            name="Magic Skill",
        ),
        "resist_value": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/4:Resist Value"),
            kind="primitive",
            name="Resist Value",
        ),
        "counter_effect_count": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/5:Counter Effect count"
            ),
            kind="primitive",
            name="Counter Effect count",
        ),
        "unused": _base.Binding(
            path="MGEF/6:Magic Effect Data/0:Data/payload/6:Unused",
            kind="primitive",
            name="Unused",
        ),
        "casting_light": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/7:Casting Light"),
            kind="primitive",
            name="Casting Light",
        ),
        "taper_weight": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/8:Taper Weight"),
            kind="primitive",
            name="Taper Weight",
        ),
        "hit_shader": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/9:Hit Shader"),
            kind="primitive",
            name="Hit Shader",
        ),
        "enchant_shader": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/10:Enchant Shader"),
            kind="primitive",
            name="Enchant Shader",
        ),
        "minimum_skill_level": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/11:Minimum Skill Level"
            ),
            kind="primitive",
            name="Minimum Skill Level",
        ),
        "spellmaking": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/12:Spellmaking"),
            kind="struct",
            name="Spellmaking",
        ),
        "taper_curve": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/13:Taper Curve"),
            kind="primitive",
            name="Taper Curve",
        ),
        "taper_duration": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/14:Taper Duration"),
            kind="primitive",
            name="Taper Duration",
        ),
        "second_av_weight": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/15:Second AV Weight"
            ),
            kind="primitive",
            name="Second AV Weight",
        ),
        "archtype": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/16:Archtype"),
            kind="primitive",
            name="Archtype",
        ),
        "actor_value": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/17:Actor Value"),
            kind="primitive",
            name="Actor Value",
        ),
        "projectile": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/18:Projectile"),
            kind="primitive",
            name="Projectile",
        ),
        "explosion": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/19:Explosion"),
            kind="primitive",
            name="Explosion",
        ),
        "casting_type": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/20:Casting Type"),
            kind="primitive",
            name="Casting Type",
        ),
        "delivery": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/21:Delivery"),
            kind="primitive",
            name="Delivery",
        ),
        "second_actor_value": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/22:Second Actor Value"
            ),
            kind="primitive",
            name="Second Actor Value",
        ),
        "casting_art": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/23:Casting Art"),
            kind="primitive",
            name="Casting Art",
        ),
        "hit_effect_art": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/24:Hit Effect Art"),
            kind="primitive",
            name="Hit Effect Art",
        ),
        "impact_data": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/25:Impact Data"),
            kind="primitive",
            name="Impact Data",
        ),
        "skill_usage_multiplier": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/26:Skill Usage"
                " Multiplier"
            ),
            kind="primitive",
            name="Skill Usage Multiplier",
        ),
        "dual_casting": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/27:Dual Casting"),
            kind="struct",
            name="Dual Casting",
        ),
        "enchant_art": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/28:Enchant Art"),
            kind="primitive",
            name="Enchant Art",
        ),
        "hit_visuals": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/29:Hit Visuals"),
            kind="primitive",
            name="Hit Visuals",
        ),
        "enchant_visuals": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/30:Enchant Visuals"),
            kind="primitive",
            name="Enchant Visuals",
        ),
        "equip_ability": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/31:Equip Ability"),
            kind="primitive",
            name="Equip Ability",
        ),
        "image_space_modifier": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/32:Image Space"
                " Modifier"
            ),
            kind="primitive",
            name="Image Space Modifier",
        ),
        "perk_to_apply": _base.Binding(
            path=("MGEF/6:Magic Effect Data/0:Data/payload/33:Perk to Apply"),
            kind="primitive",
            name="Perk to Apply",
        ),
        "casting_sound_level": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/34:Casting Sound Level"
            ),
            kind="primitive",
            name="Casting Sound Level",
        ),
        "script_effect_ai": _base.Binding(
            path=(
                "MGEF/6:Magic Effect Data/0:Data/payload/35:Script Effect AI"
            ),
            kind="struct",
            name="Script Effect AI",
        ),
    }

    flags: Flags10863
    """Value decoded from this schema node."""

    base_cost: float
    """Value decoded from this schema node."""

    assoc_item: (
        Annotated[_values.FormId, _VARIANT_10866]
        | Annotated[_values.FormId, _VARIANT_10867]
        | Annotated[_values.FormId, _VARIANT_10868]
        | Annotated[_values.FormId, _VARIANT_10869]
        | Annotated[_values.FormId, _VARIANT_10870]
        | Annotated[_values.FormId, _VARIANT_10871]
        | Annotated[_values.FormId, _VARIANT_10872]
        | Annotated[_values.FormId, _VARIANT_10873]
        | Annotated[_values.FormId, _VARIANT_10874]
    )
    """Value decoded from this schema node."""

    magic_skill: MagicSkill10875
    """Value decoded from this schema node."""

    resist_value: ResistValue10876
    """Value decoded from this schema node."""

    counter_effect_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=65535)
    ]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    casting_light: _values.FormId
    """Value decoded from this schema node."""

    taper_weight: float
    """Value decoded from this schema node."""

    hit_shader: _values.FormId
    """Value decoded from this schema node."""

    enchant_shader: _values.FormId
    """Value decoded from this schema node."""

    minimum_skill_level: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    spellmaking: Spellmaking10884
    """Value decoded from this schema node."""

    taper_curve: float
    """Value decoded from this schema node."""

    taper_duration: float
    """Value decoded from this schema node."""

    second_av_weight: float
    """Value decoded from this schema node."""

    archtype: Archtype10890
    """Value decoded from this schema node."""

    actor_value: ActorValue10891
    """Value decoded from this schema node."""

    projectile: _values.FormId
    """Value decoded from this schema node."""

    explosion: _values.FormId
    """Value decoded from this schema node."""

    casting_type: CastingType10894
    """Value decoded from this schema node."""

    delivery: Delivery10895
    """Value decoded from this schema node."""

    second_actor_value: SecondActorValue10896
    """Value decoded from this schema node."""

    casting_art: _values.FormId
    """Value decoded from this schema node."""

    hit_effect_art: _values.FormId
    """Value decoded from this schema node."""

    impact_data: _values.FormId
    """Value decoded from this schema node."""

    skill_usage_multiplier: float
    """Value decoded from this schema node."""

    dual_casting: DualCasting10901
    """Value decoded from this schema node."""

    enchant_art: _values.FormId
    """Value decoded from this schema node."""

    hit_visuals: _values.FormId
    """Value decoded from this schema node."""

    enchant_visuals: _values.FormId
    """Value decoded from this schema node."""

    equip_ability: _values.FormId
    """Value decoded from this schema node."""

    image_space_modifier: _values.FormId
    """Value decoded from this schema node."""

    perk_to_apply: _values.FormId
    """Value decoded from this schema node."""

    casting_sound_level: CastingSoundLevel10910
    """Value decoded from this schema node."""

    script_effect_ai: ScriptEffectAi10911
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags10863]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["base_cost"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["assoc_item"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_10866]
        | Annotated[_values.FormId, _VARIANT_10867]
        | Annotated[_values.FormId, _VARIANT_10868]
        | Annotated[_values.FormId, _VARIANT_10869]
        | Annotated[_values.FormId, _VARIANT_10870]
        | Annotated[_values.FormId, _VARIANT_10871]
        | Annotated[_values.FormId, _VARIANT_10872]
        | Annotated[_values.FormId, _VARIANT_10873]
        | Annotated[_values.FormId, _VARIANT_10874]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["magic_skill"]
    ) -> _base.FieldRef[MagicSkill10875]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["resist_value"]
    ) -> _base.FieldRef[ResistValue10876]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["counter_effect_count"]
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
        self, name: Literal["casting_light"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["taper_weight"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hit_shader"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enchant_shader"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["minimum_skill_level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["spellmaking"]
    ) -> _base.FieldRef[Spellmaking10884]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["taper_curve"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["taper_duration"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["second_av_weight"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["archtype"]) -> _base.FieldRef[Archtype10890]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actor_value"]
    ) -> _base.FieldRef[ActorValue10891]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["projectile"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["explosion"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["casting_type"]
    ) -> _base.FieldRef[CastingType10894]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["delivery"]) -> _base.FieldRef[Delivery10895]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["second_actor_value"]
    ) -> _base.FieldRef[SecondActorValue10896]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["casting_art"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hit_effect_art"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["impact_data"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["skill_usage_multiplier"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["dual_casting"]
    ) -> _base.FieldRef[DualCasting10901]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enchant_art"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hit_visuals"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enchant_visuals"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["equip_ability"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["image_space_modifier"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perk_to_apply"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["casting_sound_level"]
    ) -> _base.FieldRef[CastingSoundLevel10910]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_effect_ai"]
    ) -> _base.FieldRef[ScriptEffectAi10911]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class MagicEffectData10860(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MGEF/6:Magic Effect Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "data": _base.Binding(
            path="MGEF/6:Magic Effect Data/0:Data",
            kind="subrecord",
            name="Data",
        ),
    }

    data: Optional[Structure10862] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure10862]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type10920(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SHEATHE_DRAW = 0
    CHARGE = 1
    READY = 2
    RELEASE = 3
    CONCENTRATION_CAST_LOOP = 4
    ON_HIT = 5


class Structure10919(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MGEF/8:Sounds/payload/element"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path="MGEF/8:Sounds/payload/element/0:Type",
            kind="primitive",
            name="Type",
        ),
        "sound": _base.Binding(
            path="MGEF/8:Sounds/payload/element/1:Sound",
            kind="primitive",
            name="Sound",
        ),
    }

    type: Type10920
    """Value decoded from this schema node."""

    sound: _values.FormId
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type10920]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sound"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_10931: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_10932: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_10936: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_10937: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/1:None"
    )
)


_VARIANT_10938: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/2:Integer"
    )
)


_VARIANT_10939: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/3:Float"
    )
)


_VARIANT_10940: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/4:Variable Name"
    )
)


class Sex10941(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_10941: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/5:Sex"
    )
)


class ActorValue10942(_values.OpenIntEnum):
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


_VARIANT_10942: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType10943(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_10943: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/7:Crime Type"
    )
)


class Axis10944(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_10944: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/8:Axis"
    )
)


_VARIANT_10945: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat10946(_values.OpenIntEnum):
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


_VARIANT_10946: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment10947(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_10947: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_10948: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/12:Equip Type"
    )
)


class FormType10949(_values.OpenIntEnum):
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


_VARIANT_10949: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage10950(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_10950: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_10951: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_10952: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_10953: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/17:Actor"
    )
)


_VARIANT_10954: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_10955: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/19:Idle"
    )
)


_VARIANT_10956: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/20:Form List"
    )
)


_VARIANT_10957: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/21:Quest"
    )
)


_VARIANT_10958: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/22:Faction"
    )
)


_VARIANT_10959: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/23:Cell"
    )
)


_VARIANT_10960: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/24:Class"
    )
)


_VARIANT_10961: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/25:Race"
    )
)


_VARIANT_10962: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_10963: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/27:Global"
    )
)


_VARIANT_10964: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/28:Weather"
    )
)


_VARIANT_10965: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/29:Package"
    )
)


_VARIANT_10966: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_10967: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/31:Perk"
    )
)


_VARIANT_10968: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/32:Owner"
    )
)


_VARIANT_10969: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_10970: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_10971: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_10972: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction10973(_values.OpenIntEnum):
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


_VARIANT_10973: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_10974: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_10975: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_10976: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/40:Region"
    )
)


_VARIANT_10977: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction10978(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_10978: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/42:Player Action"
    )
)


class CastingType10979(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_10979: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_10980: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/44:Shout"
    )
)


_VARIANT_10981: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/45:Location"
    )
)


_VARIANT_10982: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_10983: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/47:Alias"
    )
)


_VARIANT_10984: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_10985: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim10986(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_10986: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry10987(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_10987: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_10988: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/52:Scene"
    )
)


class WardState10989(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_10989: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_10990: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/54:Event"
    )
)


_VARIANT_10991: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_10992: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_10993: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/57:Faction"
    )
)


_VARIANT_10995: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_10996: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/1:None"
    )
)


_VARIANT_10997: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/2:Integer"
    )
)


_VARIANT_10998: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/3:Float"
    )
)


_VARIANT_10999: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/4:Variable Name"
    )
)


class Sex11000(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_11000: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/5:Sex"
    )
)


class ActorValue11001(_values.OpenIntEnum):
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


_VARIANT_11001: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType11002(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_11002: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/7:Crime Type"
    )
)


class Axis11003(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_11003: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/8:Axis"
    )
)


_VARIANT_11004: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat11005(_values.OpenIntEnum):
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


_VARIANT_11005: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment11006(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_11006: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_11007: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/12:Equip Type"
    )
)


class FormType11008(_values.OpenIntEnum):
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


_VARIANT_11008: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage11009(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_11009: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_11010: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_11011: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_11012: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/17:Actor"
    )
)


_VARIANT_11013: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_11014: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/19:Idle"
    )
)


_VARIANT_11015: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/20:Form List"
    )
)


_VARIANT_11016: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/21:Quest"
    )
)


_VARIANT_11017: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/22:Faction"
    )
)


_VARIANT_11018: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/23:Cell"
    )
)


_VARIANT_11019: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/24:Class"
    )
)


_VARIANT_11020: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/25:Race"
    )
)


_VARIANT_11021: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_11022: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/27:Global"
    )
)


_VARIANT_11023: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/28:Weather"
    )
)


_VARIANT_11024: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/29:Package"
    )
)


_VARIANT_11025: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_11026: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/31:Perk"
    )
)


_VARIANT_11027: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/32:Owner"
    )
)


_VARIANT_11028: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_11029: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_11030: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_11031: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction11032(_values.OpenIntEnum):
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


_VARIANT_11032: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_11034: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/0:"
        "Weapon"
    )
)


_VARIANT_11035: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/1:"
        "Weapon List"
    )
)


_VARIANT_11036: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/2:"
        "Target"
    )
)


_VARIANT_11037: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/3:"
        "Target List"
    )
)


_VARIANT_11038: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/4:"
        "Unknown"
    )
)


class TargetPart11039(_values.OpenIntEnum):
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


_VARIANT_11039: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/5:"
        "Target Part"
    )
)


class VatsAction11040(_values.OpenIntEnum):
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


_VARIANT_11040: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/6:"
        "VATS Action"
    )
)


_VARIANT_11041: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/7:"
        "Unknown"
    )
)


_VARIANT_11042: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/8:"
        "Unknown"
    )
)


_VARIANT_11043: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/9:"
        "Critical Effect"
    )
)


_VARIANT_11044: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/10"
        ":Critical Effect List"
    )
)


_VARIANT_11045: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/11"
        ":Unknown"
    )
)


_VARIANT_11046: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/12"
        ":Unknown"
    )
)


_VARIANT_11047: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/13"
        ":Unknown"
    )
)


_VARIANT_11048: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/14"
        ":Unknown"
    )
)


class WeaponType11049(_values.OpenIntEnum):
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


_VARIANT_11049: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/15"
        ":Weapon Type"
    )
)


_VARIANT_11050: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/16"
        ":Unknown"
    )
)


_VARIANT_11051: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/17"
        ":Unknown"
    )
)


class ProjectileType11052(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_11052: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/18"
        ":Projectile Type"
    )
)


class DeliveryType11053(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_11053: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/19"
        ":Delivery Type"
    )
)


class CastingType11054(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_11054: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/20"
        ":Casting Type"
    )
)


_VARIANT_11033: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_11055: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_11056: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/40:Region"
    )
)


_VARIANT_11057: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction11058(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_11058: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/42:Player Action"
    )
)


class CastingType11059(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_11059: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_11060: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/44:Shout"
    )
)


_VARIANT_11061: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/45:Location"
    )
)


_VARIANT_11062: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_11063: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/47:Alias"
    )
)


_VARIANT_11064: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_11065: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim11066(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_11066: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry11067(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_11067: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_11068: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/52:Scene"
    )
)


class WardState11069(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_11069: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_11070: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/54:Event"
    )
)


_VARIANT_11071: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_11072: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_11073: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/57:Faction"
    )
)


class RunOn11074(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_11076: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/0:Unused"
    )
)


_VARIANT_11077: _base.Variant = _base.Variant(
    path=(
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/1:Reference"
    )
)


class Structure10927(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/2"
                ":Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/3"
                ":Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_10934": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
                ":Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
                ":Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/8"
                ":Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "MGEF/10:Conditions/repeat/0:Condition/0:CTDA/payload/9"
                ":Parameter #3"
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
        Annotated[float, _VARIANT_10931]
        | Annotated[_values.FormId, _VARIANT_10932]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_10934: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_10936]
        | Annotated[bytes, _VARIANT_10937]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10938,
        ]
        | Annotated[float, _VARIANT_10939]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10940,
        ]
        | Annotated[Sex10941, _VARIANT_10941]
        | Annotated[ActorValue10942, _VARIANT_10942]
        | Annotated[CrimeType10943, _VARIANT_10943]
        | Annotated[Axis10944, _VARIANT_10944]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10945,
        ]
        | Annotated[MiscStat10946, _VARIANT_10946]
        | Annotated[Alignment10947, _VARIANT_10947]
        | Annotated[_values.FormId, _VARIANT_10948]
        | Annotated[FormType10949, _VARIANT_10949]
        | Annotated[CriticalStage10950, _VARIANT_10950]
        | Annotated[_values.FormId, _VARIANT_10951]
        | Annotated[_values.FormId, _VARIANT_10952]
        | Annotated[_values.FormId, _VARIANT_10953]
        | Annotated[_values.FormId, _VARIANT_10954]
        | Annotated[_values.FormId, _VARIANT_10955]
        | Annotated[_values.FormId, _VARIANT_10956]
        | Annotated[_values.FormId, _VARIANT_10957]
        | Annotated[_values.FormId, _VARIANT_10958]
        | Annotated[_values.FormId, _VARIANT_10959]
        | Annotated[_values.FormId, _VARIANT_10960]
        | Annotated[_values.FormId, _VARIANT_10961]
        | Annotated[_values.FormId, _VARIANT_10962]
        | Annotated[_values.FormId, _VARIANT_10963]
        | Annotated[_values.FormId, _VARIANT_10964]
        | Annotated[_values.FormId, _VARIANT_10965]
        | Annotated[_values.FormId, _VARIANT_10966]
        | Annotated[_values.FormId, _VARIANT_10967]
        | Annotated[_values.FormId, _VARIANT_10968]
        | Annotated[_values.FormId, _VARIANT_10969]
        | Annotated[_values.FormId, _VARIANT_10970]
        | Annotated[_values.FormId, _VARIANT_10971]
        | Annotated[_values.FormId, _VARIANT_10972]
        | Annotated[VatsValueFunction10973, _VARIANT_10973]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10974,
        ]
        | Annotated[_values.FormId, _VARIANT_10975]
        | Annotated[_values.FormId, _VARIANT_10976]
        | Annotated[_values.FormId, _VARIANT_10977]
        | Annotated[PlayerAction10978, _VARIANT_10978]
        | Annotated[CastingType10979, _VARIANT_10979]
        | Annotated[_values.FormId, _VARIANT_10980]
        | Annotated[_values.FormId, _VARIANT_10981]
        | Annotated[_values.FormId, _VARIANT_10982]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10983,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10984,
        ]
        | Annotated[_values.FormId, _VARIANT_10985]
        | Annotated[FurnitureAnim10986, _VARIANT_10986]
        | Annotated[FurnitureEntry10987, _VARIANT_10987]
        | Annotated[_values.FormId, _VARIANT_10988]
        | Annotated[WardState10989, _VARIANT_10989]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10990,
        ]
        | Annotated[_values.FormId, _VARIANT_10991]
        | Annotated[_values.FormId, _VARIANT_10992]
        | Annotated[_values.FormId, _VARIANT_10993]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_10995]
        | Annotated[bytes, _VARIANT_10996]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10997,
        ]
        | Annotated[float, _VARIANT_10998]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10999,
        ]
        | Annotated[Sex11000, _VARIANT_11000]
        | Annotated[ActorValue11001, _VARIANT_11001]
        | Annotated[CrimeType11002, _VARIANT_11002]
        | Annotated[Axis11003, _VARIANT_11003]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11004,
        ]
        | Annotated[MiscStat11005, _VARIANT_11005]
        | Annotated[Alignment11006, _VARIANT_11006]
        | Annotated[_values.FormId, _VARIANT_11007]
        | Annotated[FormType11008, _VARIANT_11008]
        | Annotated[CriticalStage11009, _VARIANT_11009]
        | Annotated[_values.FormId, _VARIANT_11010]
        | Annotated[_values.FormId, _VARIANT_11011]
        | Annotated[_values.FormId, _VARIANT_11012]
        | Annotated[_values.FormId, _VARIANT_11013]
        | Annotated[_values.FormId, _VARIANT_11014]
        | Annotated[_values.FormId, _VARIANT_11015]
        | Annotated[_values.FormId, _VARIANT_11016]
        | Annotated[_values.FormId, _VARIANT_11017]
        | Annotated[_values.FormId, _VARIANT_11018]
        | Annotated[_values.FormId, _VARIANT_11019]
        | Annotated[_values.FormId, _VARIANT_11020]
        | Annotated[_values.FormId, _VARIANT_11021]
        | Annotated[_values.FormId, _VARIANT_11022]
        | Annotated[_values.FormId, _VARIANT_11023]
        | Annotated[_values.FormId, _VARIANT_11024]
        | Annotated[_values.FormId, _VARIANT_11025]
        | Annotated[_values.FormId, _VARIANT_11026]
        | Annotated[_values.FormId, _VARIANT_11027]
        | Annotated[_values.FormId, _VARIANT_11028]
        | Annotated[_values.FormId, _VARIANT_11029]
        | Annotated[_values.FormId, _VARIANT_11030]
        | Annotated[_values.FormId, _VARIANT_11031]
        | Annotated[VatsValueFunction11032, _VARIANT_11032]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_11034]
            | Annotated[_values.FormId, _VARIANT_11035]
            | Annotated[_values.FormId, _VARIANT_11036]
            | Annotated[_values.FormId, _VARIANT_11037]
            | Annotated[bytes, _VARIANT_11038]
            | Annotated[TargetPart11039, _VARIANT_11039]
            | Annotated[VatsAction11040, _VARIANT_11040]
            | Annotated[bytes, _VARIANT_11041]
            | Annotated[bytes, _VARIANT_11042]
            | Annotated[_values.FormId, _VARIANT_11043]
            | Annotated[_values.FormId, _VARIANT_11044]
            | Annotated[bytes, _VARIANT_11045]
            | Annotated[bytes, _VARIANT_11046]
            | Annotated[bytes, _VARIANT_11047]
            | Annotated[bytes, _VARIANT_11048]
            | Annotated[WeaponType11049, _VARIANT_11049]
            | Annotated[bytes, _VARIANT_11050]
            | Annotated[bytes, _VARIANT_11051]
            | Annotated[ProjectileType11052, _VARIANT_11052]
            | Annotated[DeliveryType11053, _VARIANT_11053]
            | Annotated[CastingType11054, _VARIANT_11054],
            _VARIANT_11033,
        ]
        | Annotated[_values.FormId, _VARIANT_11055]
        | Annotated[_values.FormId, _VARIANT_11056]
        | Annotated[_values.FormId, _VARIANT_11057]
        | Annotated[PlayerAction11058, _VARIANT_11058]
        | Annotated[CastingType11059, _VARIANT_11059]
        | Annotated[_values.FormId, _VARIANT_11060]
        | Annotated[_values.FormId, _VARIANT_11061]
        | Annotated[_values.FormId, _VARIANT_11062]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11063,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11064,
        ]
        | Annotated[_values.FormId, _VARIANT_11065]
        | Annotated[FurnitureAnim11066, _VARIANT_11066]
        | Annotated[FurnitureEntry11067, _VARIANT_11067]
        | Annotated[_values.FormId, _VARIANT_11068]
        | Annotated[WardState11069, _VARIANT_11069]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11070,
        ]
        | Annotated[_values.FormId, _VARIANT_11071]
        | Annotated[_values.FormId, _VARIANT_11072]
        | Annotated[_values.FormId, _VARIANT_11073]
    )
    """Value decoded from this schema node."""

    run_on: RunOn11074
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11076,
        ]
        | Annotated[_values.FormId, _VARIANT_11077]
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
        Annotated[float, _VARIANT_10931]
        | Annotated[_values.FormId, _VARIANT_10932]
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
    def field(self, name: Literal["unused_10934"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_10936]
        | Annotated[bytes, _VARIANT_10937]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10938,
        ]
        | Annotated[float, _VARIANT_10939]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10940,
        ]
        | Annotated[Sex10941, _VARIANT_10941]
        | Annotated[ActorValue10942, _VARIANT_10942]
        | Annotated[CrimeType10943, _VARIANT_10943]
        | Annotated[Axis10944, _VARIANT_10944]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10945,
        ]
        | Annotated[MiscStat10946, _VARIANT_10946]
        | Annotated[Alignment10947, _VARIANT_10947]
        | Annotated[_values.FormId, _VARIANT_10948]
        | Annotated[FormType10949, _VARIANT_10949]
        | Annotated[CriticalStage10950, _VARIANT_10950]
        | Annotated[_values.FormId, _VARIANT_10951]
        | Annotated[_values.FormId, _VARIANT_10952]
        | Annotated[_values.FormId, _VARIANT_10953]
        | Annotated[_values.FormId, _VARIANT_10954]
        | Annotated[_values.FormId, _VARIANT_10955]
        | Annotated[_values.FormId, _VARIANT_10956]
        | Annotated[_values.FormId, _VARIANT_10957]
        | Annotated[_values.FormId, _VARIANT_10958]
        | Annotated[_values.FormId, _VARIANT_10959]
        | Annotated[_values.FormId, _VARIANT_10960]
        | Annotated[_values.FormId, _VARIANT_10961]
        | Annotated[_values.FormId, _VARIANT_10962]
        | Annotated[_values.FormId, _VARIANT_10963]
        | Annotated[_values.FormId, _VARIANT_10964]
        | Annotated[_values.FormId, _VARIANT_10965]
        | Annotated[_values.FormId, _VARIANT_10966]
        | Annotated[_values.FormId, _VARIANT_10967]
        | Annotated[_values.FormId, _VARIANT_10968]
        | Annotated[_values.FormId, _VARIANT_10969]
        | Annotated[_values.FormId, _VARIANT_10970]
        | Annotated[_values.FormId, _VARIANT_10971]
        | Annotated[_values.FormId, _VARIANT_10972]
        | Annotated[VatsValueFunction10973, _VARIANT_10973]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10974,
        ]
        | Annotated[_values.FormId, _VARIANT_10975]
        | Annotated[_values.FormId, _VARIANT_10976]
        | Annotated[_values.FormId, _VARIANT_10977]
        | Annotated[PlayerAction10978, _VARIANT_10978]
        | Annotated[CastingType10979, _VARIANT_10979]
        | Annotated[_values.FormId, _VARIANT_10980]
        | Annotated[_values.FormId, _VARIANT_10981]
        | Annotated[_values.FormId, _VARIANT_10982]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10983,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10984,
        ]
        | Annotated[_values.FormId, _VARIANT_10985]
        | Annotated[FurnitureAnim10986, _VARIANT_10986]
        | Annotated[FurnitureEntry10987, _VARIANT_10987]
        | Annotated[_values.FormId, _VARIANT_10988]
        | Annotated[WardState10989, _VARIANT_10989]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10990,
        ]
        | Annotated[_values.FormId, _VARIANT_10991]
        | Annotated[_values.FormId, _VARIANT_10992]
        | Annotated[_values.FormId, _VARIANT_10993]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_10995]
        | Annotated[bytes, _VARIANT_10996]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_10997,
        ]
        | Annotated[float, _VARIANT_10998]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_10999,
        ]
        | Annotated[Sex11000, _VARIANT_11000]
        | Annotated[ActorValue11001, _VARIANT_11001]
        | Annotated[CrimeType11002, _VARIANT_11002]
        | Annotated[Axis11003, _VARIANT_11003]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11004,
        ]
        | Annotated[MiscStat11005, _VARIANT_11005]
        | Annotated[Alignment11006, _VARIANT_11006]
        | Annotated[_values.FormId, _VARIANT_11007]
        | Annotated[FormType11008, _VARIANT_11008]
        | Annotated[CriticalStage11009, _VARIANT_11009]
        | Annotated[_values.FormId, _VARIANT_11010]
        | Annotated[_values.FormId, _VARIANT_11011]
        | Annotated[_values.FormId, _VARIANT_11012]
        | Annotated[_values.FormId, _VARIANT_11013]
        | Annotated[_values.FormId, _VARIANT_11014]
        | Annotated[_values.FormId, _VARIANT_11015]
        | Annotated[_values.FormId, _VARIANT_11016]
        | Annotated[_values.FormId, _VARIANT_11017]
        | Annotated[_values.FormId, _VARIANT_11018]
        | Annotated[_values.FormId, _VARIANT_11019]
        | Annotated[_values.FormId, _VARIANT_11020]
        | Annotated[_values.FormId, _VARIANT_11021]
        | Annotated[_values.FormId, _VARIANT_11022]
        | Annotated[_values.FormId, _VARIANT_11023]
        | Annotated[_values.FormId, _VARIANT_11024]
        | Annotated[_values.FormId, _VARIANT_11025]
        | Annotated[_values.FormId, _VARIANT_11026]
        | Annotated[_values.FormId, _VARIANT_11027]
        | Annotated[_values.FormId, _VARIANT_11028]
        | Annotated[_values.FormId, _VARIANT_11029]
        | Annotated[_values.FormId, _VARIANT_11030]
        | Annotated[_values.FormId, _VARIANT_11031]
        | Annotated[VatsValueFunction11032, _VARIANT_11032]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_11034]
            | Annotated[_values.FormId, _VARIANT_11035]
            | Annotated[_values.FormId, _VARIANT_11036]
            | Annotated[_values.FormId, _VARIANT_11037]
            | Annotated[bytes, _VARIANT_11038]
            | Annotated[TargetPart11039, _VARIANT_11039]
            | Annotated[VatsAction11040, _VARIANT_11040]
            | Annotated[bytes, _VARIANT_11041]
            | Annotated[bytes, _VARIANT_11042]
            | Annotated[_values.FormId, _VARIANT_11043]
            | Annotated[_values.FormId, _VARIANT_11044]
            | Annotated[bytes, _VARIANT_11045]
            | Annotated[bytes, _VARIANT_11046]
            | Annotated[bytes, _VARIANT_11047]
            | Annotated[bytes, _VARIANT_11048]
            | Annotated[WeaponType11049, _VARIANT_11049]
            | Annotated[bytes, _VARIANT_11050]
            | Annotated[bytes, _VARIANT_11051]
            | Annotated[ProjectileType11052, _VARIANT_11052]
            | Annotated[DeliveryType11053, _VARIANT_11053]
            | Annotated[CastingType11054, _VARIANT_11054],
            _VARIANT_11033,
        ]
        | Annotated[_values.FormId, _VARIANT_11055]
        | Annotated[_values.FormId, _VARIANT_11056]
        | Annotated[_values.FormId, _VARIANT_11057]
        | Annotated[PlayerAction11058, _VARIANT_11058]
        | Annotated[CastingType11059, _VARIANT_11059]
        | Annotated[_values.FormId, _VARIANT_11060]
        | Annotated[_values.FormId, _VARIANT_11061]
        | Annotated[_values.FormId, _VARIANT_11062]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_11063,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11064,
        ]
        | Annotated[_values.FormId, _VARIANT_11065]
        | Annotated[FurnitureAnim11066, _VARIANT_11066]
        | Annotated[FurnitureEntry11067, _VARIANT_11067]
        | Annotated[_values.FormId, _VARIANT_11068]
        | Annotated[WardState11069, _VARIANT_11069]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11070,
        ]
        | Annotated[_values.FormId, _VARIANT_11071]
        | Annotated[_values.FormId, _VARIANT_11072]
        | Annotated[_values.FormId, _VARIANT_11073]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn11074]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_11076,
        ]
        | Annotated[_values.FormId, _VARIANT_11077]
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


class Condition10925(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MGEF/10:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="MGEF/10:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("MGEF/10:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("MGEF/10:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure10927] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure10927]]:
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


class MagicEffectRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MGEF"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "MGEF"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="MGEF/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="MGEF/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "name": _base.Binding(
            path="MGEF/2:Name",
            kind="subrecord",
            name="Name",
        ),
        "menu_display_object": _base.Binding(
            path="MGEF/3:Menu Display Object",
            kind="subrecord",
            name="Menu Display Object",
        ),
        "keyword_count": _base.Binding(
            path="MGEF/4:Keyword Count",
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path="MGEF/5:Keywords",
            kind="subrecord",
            name="Keywords",
        ),
        "magic_effect_data": _base.Binding(
            path="MGEF/6:Magic Effect Data",
            kind="sequence",
            name="Magic Effect Data",
        ),
        "counter_effects": _base.Binding(
            path="MGEF/7:Counter Effects",
            kind="repeat",
            name="Counter Effects",
            repeated_path="MGEF/7:Counter Effects/repeat/0:Effect",
            child_kind="subrecord",
        ),
        "sounds": _base.Binding(
            path="MGEF/8:Sounds",
            kind="subrecord",
            name="Sounds",
        ),
        "magic_item_description": _base.Binding(
            path="MGEF/9:Magic Item Description",
            kind="subrecord",
            name="Magic Item Description",
        ),
        "conditions": _base.Binding(
            path="MGEF/10:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="MGEF/10:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure10806] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    menu_display_object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    magic_effect_data: Optional[MagicEffectData10860] = None
    """Value decoded from this schema node."""

    counter_effects: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    sounds: Optional[tuple[Structure10919, ...]] = None
    """Value decoded from this schema node."""

    magic_item_description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition10925, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure10806]]:
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
        self, name: Literal["menu_display_object"]
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
        self, name: Literal["magic_effect_data"]
    ) -> _base.FieldRef[Optional[MagicEffectData10860]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["counter_effects"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sounds"]
    ) -> _base.FieldRef[Optional[tuple[Structure10919, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["magic_item_description"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition10925, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
