"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags2003(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type2007(_values.OpenIntEnum):
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


class Flags2008(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_2010: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV22012(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_2012: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV12016(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_2016: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_2011: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_2020: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_2021: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_2022: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool2023(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_2023: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV22026(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_2026: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV12030(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_2030: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_2024: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_2034: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_2036: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_2038: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element2041(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_2040: _base.Variant = _base.Variant(
    path=(
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property2005(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type2007
    """Value decoded from this schema node."""

    flags: Flags2008
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_2010]
        | Annotated[
            Annotated[ObjectV22012, _VARIANT_2012]
            | Annotated[ObjectV12016, _VARIANT_2016],
            _VARIANT_2011,
        ]
        | Annotated[str, _VARIANT_2020]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_2021,
        ]
        | Annotated[float, _VARIANT_2022]
        | Annotated[Bool2023, _VARIANT_2023]
        | Annotated[
            tuple[
                Annotated[ObjectV22026, _VARIANT_2026]
                | Annotated[ObjectV12030, _VARIANT_2030],
                ...,
            ],
            _VARIANT_2024,
        ]
        | Annotated[tuple[str, ...], _VARIANT_2034]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_2036,
        ]
        | Annotated[tuple[float, ...], _VARIANT_2038]
        | Annotated[tuple[Element2041, ...], _VARIANT_2040]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type2007]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags2008]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_2010]
        | Annotated[
            Annotated[ObjectV22012, _VARIANT_2012]
            | Annotated[ObjectV12016, _VARIANT_2016],
            _VARIANT_2011,
        ]
        | Annotated[str, _VARIANT_2020]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_2021,
        ]
        | Annotated[float, _VARIANT_2022]
        | Annotated[Bool2023, _VARIANT_2023]
        | Annotated[
            tuple[
                Annotated[ObjectV22026, _VARIANT_2026]
                | Annotated[ObjectV12030, _VARIANT_2030],
                ...,
            ],
            _VARIANT_2024,
        ]
        | Annotated[tuple[str, ...], _VARIANT_2034]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_2036,
        ]
        | Annotated[tuple[float, ...], _VARIANT_2038]
        | Annotated[tuple[Element2041, ...], _VARIANT_2040]
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


class Script2001(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "PBEA/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags2003
    """Value decoded from this schema node."""

    properties: tuple[Property2005, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags2003]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property2005, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure1997(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="PBEA/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("PBEA/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="PBEA/1:Virtual Machine Adapter/payload/2:Scripts",
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

    scripts: tuple[Script2001, ...]
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
    ) -> _base.FieldRef[tuple[Script2001, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Ownership2046(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA/4:Ownership"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path="PBEA/4:Ownership/0:Owner",
            kind="subrecord",
            name="Owner",
        ),
        "faction_rank": _base.Binding(
            path="PBEA/4:Ownership/1:Faction rank",
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


class Type2059(enum.IntFlag):
    """Named values from the pinned schema."""

    REFLECTION = 1
    REFRACTION = 2


class Structure2057(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/7:Reflected/Refracted By/repeat/0:Water/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path=(
                "PBEA/7:Reflected/Refracted By/repeat/0:Water/payload/0"
                ":Reference"
            ),
            kind="primitive",
            name="Reference",
        ),
        "type": _base.Binding(
            path=(
                "PBEA/7:Reflected/Refracted By/repeat/0:Water/payload/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
    }

    reference: _values.FormId
    """Value decoded from this schema node."""

    type: Optional[Type2059] = None
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
    ) -> _base.FieldRef[Optional[Type2059]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure2062(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/8:Linked References/repeat/0:Linked Reference/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "keyword_ref": _base.Binding(
            path=(
                "PBEA/8:Linked References/repeat/0:Linked Reference/pay"
                "load/0:Keyword/Ref"
            ),
            kind="primitive",
            name="Keyword/Ref",
        ),
        "ref": _base.Binding(
            path=(
                "PBEA/8:Linked References/repeat/0:Linked Reference/pay"
                "load/1:Ref"
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


class ParentActivateOnly2067(enum.IntFlag):
    """Named values from the pinned schema."""

    PARENT_ACTIVATE_ONLY = 1


class Structure2070(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PBEA/9:Activate Parents/1:Activate Parent Refs/repeat/"
        "0:Activate Parent Ref/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path=(
                "PBEA/9:Activate Parents/1:Activate Parent Refs/repeat/"
                "0:Activate Parent Ref/payload/0:Reference"
            ),
            kind="primitive",
            name="Reference",
        ),
        "delay": _base.Binding(
            path=(
                "PBEA/9:Activate Parents/1:Activate Parent Refs/repeat/"
                "0:Activate Parent Ref/payload/1:Delay"
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


class ActivateParents2065(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA/9:Activate Parents"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="PBEA/9:Activate Parents/0:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "activate_parent_refs": _base.Binding(
            path="PBEA/9:Activate Parents/1:Activate Parent Refs",
            kind="repeat",
            name="Activate Parent Refs",
            repeated_path=(
                "PBEA/9:Activate Parents/1:Activate Parent Refs/repeat/"
                "0:Activate Parent Ref"
            ),
            child_kind="subrecord",
        ),
    }

    flags: Optional[ParentActivateOnly2067] = None
    """Value decoded from this schema node."""

    activate_parent_refs: tuple[Structure2070, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[ParentActivateOnly2067]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["activate_parent_refs"]
    ) -> _base.FieldRef[tuple[Structure2070, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags2076(enum.IntFlag):
    """Named values from the pinned schema."""

    SET_ENABLE_STATE_TO_OPPOSITE_OF_PARENT = 1
    POP_IN = 2


class Structure2074(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA/10:Enable Parent/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference": _base.Binding(
            path="PBEA/10:Enable Parent/payload/0:Reference",
            kind="primitive",
            name="Reference",
        ),
        "flags": _base.Binding(
            path="PBEA/10:Enable Parent/payload/1:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unused": _base.Binding(
            path="PBEA/10:Enable Parent/payload/2:Unused",
            kind="primitive",
            name="Unused",
        ),
    }

    reference: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags2076
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags2076]:
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


class Position2096(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA/18:Position/Rotation/payload/0:Position"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/0:Position/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/0:Position/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/0:Position/2:Z",
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


class Rotation2100(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA/18:Position/Rotation/payload/1:Rotation"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "x": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/1:Rotation/0:X",
            kind="primitive",
            name="X",
        ),
        "y": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/1:Rotation/1:Y",
            kind="primitive",
            name="Y",
        ),
        "z": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/1:Rotation/2:Z",
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


class Structure2095(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA/18:Position/Rotation/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "position": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/0:Position",
            kind="struct",
            name="Position",
        ),
        "rotation": _base.Binding(
            path="PBEA/18:Position/Rotation/payload/1:Rotation",
            kind="struct",
            name="Rotation",
        ),
    }

    position: Position2096
    """Value decoded from this schema node."""

    rotation: Rotation2100
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["position"]) -> _base.FieldRef[Position2096]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotation"]) -> _base.FieldRef[Rotation2100]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class PlacedBeamRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PBEA"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "PBEA"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="PBEA/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="PBEA/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "projectile": _base.Binding(
            path="PBEA/2:Projectile",
            kind="subrecord",
            name="Projectile",
        ),
        "encounter_zone": _base.Binding(
            path="PBEA/3:Encounter Zone",
            kind="subrecord",
            name="Encounter Zone",
        ),
        "ownership": _base.Binding(
            path="PBEA/4:Ownership",
            kind="sequence",
            name="Ownership",
        ),
        "head_tracking_weight": _base.Binding(
            path="PBEA/5:Head-Tracking Weight",
            kind="subrecord",
            name="Head-Tracking Weight",
        ),
        "favor_cost": _base.Binding(
            path="PBEA/6:Favor Cost",
            kind="subrecord",
            name="Favor Cost",
        ),
        "reflected_refracted_by": _base.Binding(
            path="PBEA/7:Reflected/Refracted By",
            kind="repeat",
            name="Reflected/Refracted By",
            repeated_path="PBEA/7:Reflected/Refracted By/repeat/0:Water",
            child_kind="subrecord",
        ),
        "linked_references": _base.Binding(
            path="PBEA/8:Linked References",
            kind="repeat",
            name="Linked References",
            repeated_path=(
                "PBEA/8:Linked References/repeat/0:Linked Reference"
            ),
            child_kind="subrecord",
        ),
        "activate_parents": _base.Binding(
            path="PBEA/9:Activate Parents",
            kind="sequence",
            name="Activate Parents",
        ),
        "enable_parent": _base.Binding(
            path="PBEA/10:Enable Parent",
            kind="subrecord",
            name="Enable Parent",
        ),
        "emittance": _base.Binding(
            path="PBEA/11:Emittance",
            kind="subrecord",
            name="Emittance",
        ),
        "multi_bound_reference": _base.Binding(
            path="PBEA/12:MultiBound Reference",
            kind="subrecord",
            name="MultiBound Reference",
        ),
        "ignored_by_sandbox": _base.Binding(
            path="PBEA/13:Ignored by Sandbox",
            kind="subrecord",
            name="Ignored by Sandbox",
        ),
        "location_ref_type": _base.Binding(
            path="PBEA/14:Location Ref Type",
            kind="subrecord",
            name="Location Ref Type",
        ),
        "location_reference": _base.Binding(
            path="PBEA/15:Location Reference",
            kind="subrecord",
            name="Location Reference",
        ),
        "distant_lod_data": _base.Binding(
            path="PBEA/16:Distant LOD Data",
            kind="subrecord",
            name="Distant LOD Data",
        ),
        "scale": _base.Binding(
            path="PBEA/17:Scale",
            kind="subrecord",
            name="Scale",
        ),
        "position_rotation": _base.Binding(
            path="PBEA/18:Position/Rotation",
            kind="subrecord",
            name="Position/Rotation",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure1997] = None
    """Value decoded from this schema node."""

    projectile: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    encounter_zone: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ownership: Optional[Ownership2046] = None
    """Value decoded from this schema node."""

    head_tracking_weight: Optional[float] = None
    """Value decoded from this schema node."""

    favor_cost: Optional[float] = None
    """Value decoded from this schema node."""

    reflected_refracted_by: tuple[Structure2057, ...] = ()
    """Value decoded from this schema node."""

    linked_references: tuple[Structure2062, ...] = ()
    """Value decoded from this schema node."""

    activate_parents: Optional[ActivateParents2065] = None
    """Value decoded from this schema node."""

    enable_parent: Optional[Structure2074] = None
    """Value decoded from this schema node."""

    emittance: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    multi_bound_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ignored_by_sandbox: Optional[bytes] = None
    """Value decoded from this schema node."""

    location_ref_type: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    location_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    distant_lod_data: Optional[tuple[float, ...]] = None
    """Value decoded from this schema node."""

    scale: Optional[float] = None
    """Value decoded from this schema node."""

    position_rotation: Optional[Structure2095] = None
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
    ) -> _base.FieldRef[Optional[Structure1997]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["projectile"]
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
        self, name: Literal["ownership"]
    ) -> _base.FieldRef[Optional[Ownership2046]]:
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
        self, name: Literal["reflected_refracted_by"]
    ) -> _base.FieldRef[tuple[Structure2057, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["linked_references"]
    ) -> _base.FieldRef[tuple[Structure2062, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["activate_parents"]
    ) -> _base.FieldRef[Optional[ActivateParents2065]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["enable_parent"]
    ) -> _base.FieldRef[Optional[Structure2074]]:
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
        self, name: Literal["location_reference"]
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
    def field(self, name: Literal["scale"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["position_rotation"]
    ) -> _base.FieldRef[Optional[Structure2095]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
