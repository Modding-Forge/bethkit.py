"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags11997(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type12001(_values.OpenIntEnum):
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


class Flags12002(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_12004: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV212006(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12006: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV112010(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12010: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_12005: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_12014: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_12015: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_12016: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool12017(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_12017: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV212020(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12020: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV112024(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12024: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_12018: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_12028: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_12030: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_12032: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element12035(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_12034: _base.Variant = _base.Variant(
    path=(
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property11999(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type12001
    """Value decoded from this schema node."""

    flags: Flags12002
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_12004]
        | Annotated[
            Annotated[ObjectV212006, _VARIANT_12006]
            | Annotated[ObjectV112010, _VARIANT_12010],
            _VARIANT_12005,
        ]
        | Annotated[str, _VARIANT_12014]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12015,
        ]
        | Annotated[float, _VARIANT_12016]
        | Annotated[Bool12017, _VARIANT_12017]
        | Annotated[
            tuple[
                Annotated[ObjectV212020, _VARIANT_12020]
                | Annotated[ObjectV112024, _VARIANT_12024],
                ...,
            ],
            _VARIANT_12018,
        ]
        | Annotated[tuple[str, ...], _VARIANT_12028]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_12030,
        ]
        | Annotated[tuple[float, ...], _VARIANT_12032]
        | Annotated[tuple[Element12035, ...], _VARIANT_12034]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12001]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12002]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12004]
        | Annotated[
            Annotated[ObjectV212006, _VARIANT_12006]
            | Annotated[ObjectV112010, _VARIANT_12010],
            _VARIANT_12005,
        ]
        | Annotated[str, _VARIANT_12014]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12015,
        ]
        | Annotated[float, _VARIANT_12016]
        | Annotated[Bool12017, _VARIANT_12017]
        | Annotated[
            tuple[
                Annotated[ObjectV212020, _VARIANT_12020]
                | Annotated[ObjectV112024, _VARIANT_12024],
                ...,
            ],
            _VARIANT_12018,
        ]
        | Annotated[tuple[str, ...], _VARIANT_12028]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_12030,
        ]
        | Annotated[tuple[float, ...], _VARIANT_12032]
        | Annotated[tuple[Element12035, ...], _VARIANT_12034]
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


class Script11995(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags11997
    """Value decoded from this schema node."""

    properties: tuple[Property11999, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags11997]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property11999, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags12038(enum.IntFlag):
    """Named values from the pinned schema."""

    ON_BEGIN = 1
    ON_END = 2
    ON_CHANGE = 4


class Fragment12041(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
        "nts/3:Fragments/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/0:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "script_name": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/1:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "fragment_name": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/2:FragmentName"
            ),
            kind="primitive",
            name="FragmentName",
        ),
    }

    unknown: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    script_name: str
    """Value decoded from this schema node."""

    fragment_name: str
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["fragment_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ScriptFragments12036(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/1:Virtual Machine Adapter/payload/3:Script Fragments"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "extra_bind_data_version": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/0:Extra bind data version"
            ),
            kind="primitive",
            name="Extra bind data version",
        ),
        "flags": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "file_name": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:FileName"
            ),
            kind="primitive",
            name="FileName",
        ),
        "fragments": _base.Binding(
            path=(
                "PACK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments"
            ),
            kind="array",
            name="Fragments",
        ),
    }

    extra_bind_data_version: Annotated[
        int, pydantic.Field(strict=True, ge=-128, le=127)
    ]
    """Value decoded from this schema node."""

    flags: Flags12038
    """Value decoded from this schema node."""

    file_name: str
    """Value decoded from this schema node."""

    fragments: tuple[Fragment12041, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["extra_bind_data_version"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12038]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["file_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fragments"]
    ) -> _base.FieldRef[tuple[Fragment12041, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure11991(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="PACK/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("PACK/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="PACK/1:Virtual Machine Adapter/payload/2:Scripts",
            kind="array",
            name="Scripts",
        ),
        "script_fragments": _base.Binding(
            path=("PACK/1:Virtual Machine Adapter/payload/3:Script Fragments"),
            kind="struct",
            name="Script Fragments",
        ),
    }

    version: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    object_format: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    scripts: tuple[Script11995, ...]
    """Value decoded from this schema node."""

    script_fragments: Optional[ScriptFragments12036] = None
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
    ) -> _base.FieldRef[tuple[Script11995, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_fragments"]
    ) -> _base.FieldRef[Optional[ScriptFragments12036]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class GeneralFlags12047(enum.IntFlag):
    """Named values from the pinned schema."""

    OFFERS_SERVICES = 1
    UNKNOWN_2 = 2
    MUST_COMPLETE = 4
    MAINTAIN_SPEED_AT_GOAL = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNLOCK_DOORS_AT_PACKAGE_START = 64
    UNLOCK_DOORS_AT_PACKAGE_END = 128
    UNKNOWN_9 = 256
    CONTINUE_IF_PC_NEAR = 512
    ONCE_PER_DAY = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    PREFERRED_SPEED = 8192
    UNKNOWN_15 = 16384
    UNKNOWN_16 = 32768
    UNKNOWN_17 = 65536
    ALWAYS_SNEAK = 131072
    ALLOW_SWIMMING = 262144
    UNKNOWN_20 = 524288
    IGNORE_COMBAT = 1048576
    WEAPONS_UNEQUIPPED = 2097152
    UNKNOWN_23 = 4194304
    WEAPON_DRAWN = 8388608
    UNKNOWN_25 = 16777216
    UNKNOWN_26 = 33554432
    UNKNOWN_27 = 67108864
    NO_COMBAT_ALERT = 134217728
    UNKNOWN_29 = 268435456
    WEAR_SLEEP_OUTFIT_UNUSED = 536870912
    UNKNOWN_31 = 1073741824
    UNKNOWN_32 = 2147483648


class Type12048(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    PACKAGE = 18
    PACKAGE_TEMPLATE = 19


class InterruptOverride12049(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    SPECTATOR = 1
    OBSERVE_DEAD = 2
    GUARD_WARN = 3
    COMBAT = 4


class PreferredSpeed12050(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    WALK = 0
    JOG = 1
    RUN = 2
    FAST_WALK = 3


class InterruptFlags12052(enum.IntFlag):
    """Named values from the pinned schema."""

    HELLOS_TO_PLAYER = 1
    RANDOM_CONVERSATIONS = 2
    OBSERVE_COMBAT_BEHAVIOR = 4
    GREET_CORPSE_BEHAVIOR = 8
    REACTION_TO_PLAYER_ACTIONS = 16
    FRIENDLY_FIRE_COMMENTS = 32
    AGGRO_RADIUS_BEHAVIOR = 64
    ALLOW_IDLE_CHATTER = 128
    UNKNOWN_9 = 256
    WORLD_INTERACTIONS = 512
    UNKNOWN_11 = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    UNKNOWN_14 = 8192
    UNKNOWN_15 = 16384
    UNKNOWN_16 = 32768


class Structure12046(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/2:Pack Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "general_flags": _base.Binding(
            path="PACK/2:Pack Data/payload/0:General Flags",
            kind="primitive",
            name="General Flags",
        ),
        "type": _base.Binding(
            path="PACK/2:Pack Data/payload/1:Type",
            kind="primitive",
            name="Type",
        ),
        "interrupt_override": _base.Binding(
            path="PACK/2:Pack Data/payload/2:Interrupt Override",
            kind="primitive",
            name="Interrupt Override",
        ),
        "preferred_speed": _base.Binding(
            path="PACK/2:Pack Data/payload/3:Preferred Speed",
            kind="primitive",
            name="Preferred Speed",
        ),
        "unknown": _base.Binding(
            path="PACK/2:Pack Data/payload/4:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "interrupt_flags": _base.Binding(
            path="PACK/2:Pack Data/payload/5:Interrupt Flags",
            kind="primitive",
            name="Interrupt Flags",
        ),
        "unknown_12053": _base.Binding(
            path="PACK/2:Pack Data/payload/6:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    general_flags: GeneralFlags12047
    """Value decoded from this schema node."""

    type: Type12048
    """Value decoded from this schema node."""

    interrupt_override: InterruptOverride12049
    """Value decoded from this schema node."""

    preferred_speed: PreferredSpeed12050
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    interrupt_flags: InterruptFlags12052
    """Value decoded from this schema node."""

    unknown_12053: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["general_flags"]
    ) -> _base.FieldRef[GeneralFlags12047]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12048]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["interrupt_override"]
    ) -> _base.FieldRef[InterruptOverride12049]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["preferred_speed"]
    ) -> _base.FieldRef[PreferredSpeed12050]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["interrupt_flags"]
    ) -> _base.FieldRef[InterruptFlags12052]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_12053"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class DayOfWeek12057(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    ANY = -1
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    WEEKDAYS = 7
    WEEKENDS = 8
    MONDAY_WEDNESDAY_FRIDAY = 9
    TUESDAY_THURSDAY = 10


class Structure12055(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/3:Schedule/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "month": _base.Binding(
            path="PACK/3:Schedule/payload/0:Month",
            kind="primitive",
            name="Month",
        ),
        "day_of_week": _base.Binding(
            path="PACK/3:Schedule/payload/1:Day of week",
            kind="primitive",
            name="Day of week",
        ),
        "date": _base.Binding(
            path="PACK/3:Schedule/payload/2:Date",
            kind="primitive",
            name="Date",
        ),
        "hour": _base.Binding(
            path="PACK/3:Schedule/payload/3:Hour",
            kind="primitive",
            name="Hour",
        ),
        "minute": _base.Binding(
            path="PACK/3:Schedule/payload/4:Minute",
            kind="primitive",
            name="Minute",
        ),
        "unused": _base.Binding(
            path="PACK/3:Schedule/payload/5:Unused",
            kind="primitive",
            name="Unused",
        ),
        "duration_minutes": _base.Binding(
            path="PACK/3:Schedule/payload/6:Duration (minutes)",
            kind="primitive",
            name="Duration (minutes)",
        ),
    }

    month: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    day_of_week: DayOfWeek12057
    """Value decoded from this schema node."""

    date: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    hour: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    minute: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    duration_minutes: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["month"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["day_of_week"]
    ) -> _base.FieldRef[DayOfWeek12057]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["date"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hour"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["minute"]
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
    def field(
        self, name: Literal["duration_minutes"]
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


_VARIANT_12070: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_12071: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_12075: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_12076: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/1:None"
    )
)


_VARIANT_12077: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/2:Integer"
    )
)


_VARIANT_12078: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/3:Float"
    )
)


_VARIANT_12079: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/4:Variable Name"
    )
)


class Sex12080(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12080: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/5:Sex"
    )
)


class ActorValue12081(_values.OpenIntEnum):
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


_VARIANT_12081: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType12082(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12082: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/7:Crime Type"
    )
)


class Axis12083(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12083: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/8:Axis"
    )
)


_VARIANT_12084: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat12085(_values.OpenIntEnum):
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


_VARIANT_12085: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment12086(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12086: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_12087: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/12:Equip Type"
    )
)


class FormType12088(_values.OpenIntEnum):
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


_VARIANT_12088: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage12089(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12089: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_12090: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_12091: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_12092: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/17:Actor"
    )
)


_VARIANT_12093: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_12094: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/19:Idle"
    )
)


_VARIANT_12095: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/20:Form List"
    )
)


_VARIANT_12096: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/21:Quest"
    )
)


_VARIANT_12097: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/22:Faction"
    )
)


_VARIANT_12098: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/23:Cell"
    )
)


_VARIANT_12099: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/24:Class"
    )
)


_VARIANT_12100: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/25:Race"
    )
)


_VARIANT_12101: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_12102: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/27:Global"
    )
)


_VARIANT_12103: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/28:Weather"
    )
)


_VARIANT_12104: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/29:Package"
    )
)


_VARIANT_12105: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_12106: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/31:Perk"
    )
)


_VARIANT_12107: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/32:Owner"
    )
)


_VARIANT_12108: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_12109: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_12110: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_12111: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction12112(_values.OpenIntEnum):
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


_VARIANT_12112: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_12113: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_12114: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_12115: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/40:Region"
    )
)


_VARIANT_12116: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction12117(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12117: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/42:Player Action"
    )
)


class CastingType12118(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12118: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_12119: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/44:Shout"
    )
)


_VARIANT_12120: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/45:Location"
    )
)


_VARIANT_12121: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_12122: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/47:Alias"
    )
)


_VARIANT_12123: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_12124: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim12125(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_12125: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry12126(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_12126: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_12127: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/52:Scene"
    )
)


class WardState12128(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_12128: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_12129: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/54:Event"
    )
)


_VARIANT_12130: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_12131: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_12132: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/57:Faction"
    )
)


_VARIANT_12134: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_12135: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/1:None"
    )
)


_VARIANT_12136: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/2:Integer"
    )
)


_VARIANT_12137: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/3:Float"
    )
)


_VARIANT_12138: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/4:Variable Name"
    )
)


class Sex12139(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12139: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/5:Sex"
    )
)


class ActorValue12140(_values.OpenIntEnum):
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


_VARIANT_12140: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType12141(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12141: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/7:Crime Type"
    )
)


class Axis12142(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12142: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/8:Axis"
    )
)


_VARIANT_12143: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat12144(_values.OpenIntEnum):
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


_VARIANT_12144: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment12145(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12145: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_12146: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/12:Equip Type"
    )
)


class FormType12147(_values.OpenIntEnum):
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


_VARIANT_12147: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage12148(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12148: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_12149: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_12150: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_12151: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/17:Actor"
    )
)


_VARIANT_12152: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_12153: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/19:Idle"
    )
)


_VARIANT_12154: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/20:Form List"
    )
)


_VARIANT_12155: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/21:Quest"
    )
)


_VARIANT_12156: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/22:Faction"
    )
)


_VARIANT_12157: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/23:Cell"
    )
)


_VARIANT_12158: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/24:Class"
    )
)


_VARIANT_12159: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/25:Race"
    )
)


_VARIANT_12160: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_12161: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/27:Global"
    )
)


_VARIANT_12162: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/28:Weather"
    )
)


_VARIANT_12163: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/29:Package"
    )
)


_VARIANT_12164: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_12165: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/31:Perk"
    )
)


_VARIANT_12166: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/32:Owner"
    )
)


_VARIANT_12167: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_12168: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_12169: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_12170: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction12171(_values.OpenIntEnum):
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


_VARIANT_12171: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_12173: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/0:W"
        "eapon"
    )
)


_VARIANT_12174: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/1:W"
        "eapon List"
    )
)


_VARIANT_12175: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/2:T"
        "arget"
    )
)


_VARIANT_12176: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/3:T"
        "arget List"
    )
)


_VARIANT_12177: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/4:U"
        "nknown"
    )
)


class TargetPart12178(_values.OpenIntEnum):
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


_VARIANT_12178: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/5:T"
        "arget Part"
    )
)


class VatsAction12179(_values.OpenIntEnum):
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


_VARIANT_12179: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/6:V"
        "ATS Action"
    )
)


_VARIANT_12180: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/7:U"
        "nknown"
    )
)


_VARIANT_12181: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/8:U"
        "nknown"
    )
)


_VARIANT_12182: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/9:C"
        "ritical Effect"
    )
)


_VARIANT_12183: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/10:"
        "Critical Effect List"
    )
)


_VARIANT_12184: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/11:"
        "Unknown"
    )
)


_VARIANT_12185: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/12:"
        "Unknown"
    )
)


_VARIANT_12186: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/13:"
        "Unknown"
    )
)


_VARIANT_12187: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/14:"
        "Unknown"
    )
)


class WeaponType12188(_values.OpenIntEnum):
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


_VARIANT_12188: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/15:"
        "Weapon Type"
    )
)


_VARIANT_12189: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/16:"
        "Unknown"
    )
)


_VARIANT_12190: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/17:"
        "Unknown"
    )
)


class ProjectileType12191(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_12191: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/18:"
        "Projectile Type"
    )
)


class DeliveryType12192(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_12192: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/19:"
        "Delivery Type"
    )
)


class CastingType12193(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_12193: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/20:"
        "Casting Type"
    )
)


_VARIANT_12172: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_12194: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_12195: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/40:Region"
    )
)


_VARIANT_12196: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction12197(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12197: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/42:Player Action"
    )
)


class CastingType12198(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12198: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_12199: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/44:Shout"
    )
)


_VARIANT_12200: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/45:Location"
    )
)


_VARIANT_12201: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_12202: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/47:Alias"
    )
)


_VARIANT_12203: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_12204: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim12205(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_12205: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry12206(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_12206: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_12207: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/52:Scene"
    )
)


class WardState12208(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_12208: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_12209: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/54:Event"
    )
)


_VARIANT_12210: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_12211: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_12212: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/57:Faction"
    )
)


class RunOn12213(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_12215: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/0:Unused"
    )
)


_VARIANT_12216: _base.Variant = _base.Variant(
    path=(
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/1:Reference"
    )
)


class Structure12066(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
                "Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_12073": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
                "Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
                "Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
                "Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "PACK/4:Conditions/repeat/0:Condition/0:CTDA/payload/9:"
                "Parameter #3"
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
        Annotated[float, _VARIANT_12070]
        | Annotated[_values.FormId, _VARIANT_12071]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_12073: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_12075]
        | Annotated[bytes, _VARIANT_12076]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12077,
        ]
        | Annotated[float, _VARIANT_12078]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12079,
        ]
        | Annotated[Sex12080, _VARIANT_12080]
        | Annotated[ActorValue12081, _VARIANT_12081]
        | Annotated[CrimeType12082, _VARIANT_12082]
        | Annotated[Axis12083, _VARIANT_12083]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12084,
        ]
        | Annotated[MiscStat12085, _VARIANT_12085]
        | Annotated[Alignment12086, _VARIANT_12086]
        | Annotated[_values.FormId, _VARIANT_12087]
        | Annotated[FormType12088, _VARIANT_12088]
        | Annotated[CriticalStage12089, _VARIANT_12089]
        | Annotated[_values.FormId, _VARIANT_12090]
        | Annotated[_values.FormId, _VARIANT_12091]
        | Annotated[_values.FormId, _VARIANT_12092]
        | Annotated[_values.FormId, _VARIANT_12093]
        | Annotated[_values.FormId, _VARIANT_12094]
        | Annotated[_values.FormId, _VARIANT_12095]
        | Annotated[_values.FormId, _VARIANT_12096]
        | Annotated[_values.FormId, _VARIANT_12097]
        | Annotated[_values.FormId, _VARIANT_12098]
        | Annotated[_values.FormId, _VARIANT_12099]
        | Annotated[_values.FormId, _VARIANT_12100]
        | Annotated[_values.FormId, _VARIANT_12101]
        | Annotated[_values.FormId, _VARIANT_12102]
        | Annotated[_values.FormId, _VARIANT_12103]
        | Annotated[_values.FormId, _VARIANT_12104]
        | Annotated[_values.FormId, _VARIANT_12105]
        | Annotated[_values.FormId, _VARIANT_12106]
        | Annotated[_values.FormId, _VARIANT_12107]
        | Annotated[_values.FormId, _VARIANT_12108]
        | Annotated[_values.FormId, _VARIANT_12109]
        | Annotated[_values.FormId, _VARIANT_12110]
        | Annotated[_values.FormId, _VARIANT_12111]
        | Annotated[VatsValueFunction12112, _VARIANT_12112]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12113,
        ]
        | Annotated[_values.FormId, _VARIANT_12114]
        | Annotated[_values.FormId, _VARIANT_12115]
        | Annotated[_values.FormId, _VARIANT_12116]
        | Annotated[PlayerAction12117, _VARIANT_12117]
        | Annotated[CastingType12118, _VARIANT_12118]
        | Annotated[_values.FormId, _VARIANT_12119]
        | Annotated[_values.FormId, _VARIANT_12120]
        | Annotated[_values.FormId, _VARIANT_12121]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12122,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12123,
        ]
        | Annotated[_values.FormId, _VARIANT_12124]
        | Annotated[FurnitureAnim12125, _VARIANT_12125]
        | Annotated[FurnitureEntry12126, _VARIANT_12126]
        | Annotated[_values.FormId, _VARIANT_12127]
        | Annotated[WardState12128, _VARIANT_12128]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12129,
        ]
        | Annotated[_values.FormId, _VARIANT_12130]
        | Annotated[_values.FormId, _VARIANT_12131]
        | Annotated[_values.FormId, _VARIANT_12132]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_12134]
        | Annotated[bytes, _VARIANT_12135]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12136,
        ]
        | Annotated[float, _VARIANT_12137]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12138,
        ]
        | Annotated[Sex12139, _VARIANT_12139]
        | Annotated[ActorValue12140, _VARIANT_12140]
        | Annotated[CrimeType12141, _VARIANT_12141]
        | Annotated[Axis12142, _VARIANT_12142]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12143,
        ]
        | Annotated[MiscStat12144, _VARIANT_12144]
        | Annotated[Alignment12145, _VARIANT_12145]
        | Annotated[_values.FormId, _VARIANT_12146]
        | Annotated[FormType12147, _VARIANT_12147]
        | Annotated[CriticalStage12148, _VARIANT_12148]
        | Annotated[_values.FormId, _VARIANT_12149]
        | Annotated[_values.FormId, _VARIANT_12150]
        | Annotated[_values.FormId, _VARIANT_12151]
        | Annotated[_values.FormId, _VARIANT_12152]
        | Annotated[_values.FormId, _VARIANT_12153]
        | Annotated[_values.FormId, _VARIANT_12154]
        | Annotated[_values.FormId, _VARIANT_12155]
        | Annotated[_values.FormId, _VARIANT_12156]
        | Annotated[_values.FormId, _VARIANT_12157]
        | Annotated[_values.FormId, _VARIANT_12158]
        | Annotated[_values.FormId, _VARIANT_12159]
        | Annotated[_values.FormId, _VARIANT_12160]
        | Annotated[_values.FormId, _VARIANT_12161]
        | Annotated[_values.FormId, _VARIANT_12162]
        | Annotated[_values.FormId, _VARIANT_12163]
        | Annotated[_values.FormId, _VARIANT_12164]
        | Annotated[_values.FormId, _VARIANT_12165]
        | Annotated[_values.FormId, _VARIANT_12166]
        | Annotated[_values.FormId, _VARIANT_12167]
        | Annotated[_values.FormId, _VARIANT_12168]
        | Annotated[_values.FormId, _VARIANT_12169]
        | Annotated[_values.FormId, _VARIANT_12170]
        | Annotated[VatsValueFunction12171, _VARIANT_12171]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12173]
            | Annotated[_values.FormId, _VARIANT_12174]
            | Annotated[_values.FormId, _VARIANT_12175]
            | Annotated[_values.FormId, _VARIANT_12176]
            | Annotated[bytes, _VARIANT_12177]
            | Annotated[TargetPart12178, _VARIANT_12178]
            | Annotated[VatsAction12179, _VARIANT_12179]
            | Annotated[bytes, _VARIANT_12180]
            | Annotated[bytes, _VARIANT_12181]
            | Annotated[_values.FormId, _VARIANT_12182]
            | Annotated[_values.FormId, _VARIANT_12183]
            | Annotated[bytes, _VARIANT_12184]
            | Annotated[bytes, _VARIANT_12185]
            | Annotated[bytes, _VARIANT_12186]
            | Annotated[bytes, _VARIANT_12187]
            | Annotated[WeaponType12188, _VARIANT_12188]
            | Annotated[bytes, _VARIANT_12189]
            | Annotated[bytes, _VARIANT_12190]
            | Annotated[ProjectileType12191, _VARIANT_12191]
            | Annotated[DeliveryType12192, _VARIANT_12192]
            | Annotated[CastingType12193, _VARIANT_12193],
            _VARIANT_12172,
        ]
        | Annotated[_values.FormId, _VARIANT_12194]
        | Annotated[_values.FormId, _VARIANT_12195]
        | Annotated[_values.FormId, _VARIANT_12196]
        | Annotated[PlayerAction12197, _VARIANT_12197]
        | Annotated[CastingType12198, _VARIANT_12198]
        | Annotated[_values.FormId, _VARIANT_12199]
        | Annotated[_values.FormId, _VARIANT_12200]
        | Annotated[_values.FormId, _VARIANT_12201]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12202,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12203,
        ]
        | Annotated[_values.FormId, _VARIANT_12204]
        | Annotated[FurnitureAnim12205, _VARIANT_12205]
        | Annotated[FurnitureEntry12206, _VARIANT_12206]
        | Annotated[_values.FormId, _VARIANT_12207]
        | Annotated[WardState12208, _VARIANT_12208]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12209,
        ]
        | Annotated[_values.FormId, _VARIANT_12210]
        | Annotated[_values.FormId, _VARIANT_12211]
        | Annotated[_values.FormId, _VARIANT_12212]
    )
    """Value decoded from this schema node."""

    run_on: RunOn12213
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12215,
        ]
        | Annotated[_values.FormId, _VARIANT_12216]
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
        Annotated[float, _VARIANT_12070]
        | Annotated[_values.FormId, _VARIANT_12071]
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
    def field(self, name: Literal["unused_12073"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12075]
        | Annotated[bytes, _VARIANT_12076]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12077,
        ]
        | Annotated[float, _VARIANT_12078]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12079,
        ]
        | Annotated[Sex12080, _VARIANT_12080]
        | Annotated[ActorValue12081, _VARIANT_12081]
        | Annotated[CrimeType12082, _VARIANT_12082]
        | Annotated[Axis12083, _VARIANT_12083]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12084,
        ]
        | Annotated[MiscStat12085, _VARIANT_12085]
        | Annotated[Alignment12086, _VARIANT_12086]
        | Annotated[_values.FormId, _VARIANT_12087]
        | Annotated[FormType12088, _VARIANT_12088]
        | Annotated[CriticalStage12089, _VARIANT_12089]
        | Annotated[_values.FormId, _VARIANT_12090]
        | Annotated[_values.FormId, _VARIANT_12091]
        | Annotated[_values.FormId, _VARIANT_12092]
        | Annotated[_values.FormId, _VARIANT_12093]
        | Annotated[_values.FormId, _VARIANT_12094]
        | Annotated[_values.FormId, _VARIANT_12095]
        | Annotated[_values.FormId, _VARIANT_12096]
        | Annotated[_values.FormId, _VARIANT_12097]
        | Annotated[_values.FormId, _VARIANT_12098]
        | Annotated[_values.FormId, _VARIANT_12099]
        | Annotated[_values.FormId, _VARIANT_12100]
        | Annotated[_values.FormId, _VARIANT_12101]
        | Annotated[_values.FormId, _VARIANT_12102]
        | Annotated[_values.FormId, _VARIANT_12103]
        | Annotated[_values.FormId, _VARIANT_12104]
        | Annotated[_values.FormId, _VARIANT_12105]
        | Annotated[_values.FormId, _VARIANT_12106]
        | Annotated[_values.FormId, _VARIANT_12107]
        | Annotated[_values.FormId, _VARIANT_12108]
        | Annotated[_values.FormId, _VARIANT_12109]
        | Annotated[_values.FormId, _VARIANT_12110]
        | Annotated[_values.FormId, _VARIANT_12111]
        | Annotated[VatsValueFunction12112, _VARIANT_12112]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12113,
        ]
        | Annotated[_values.FormId, _VARIANT_12114]
        | Annotated[_values.FormId, _VARIANT_12115]
        | Annotated[_values.FormId, _VARIANT_12116]
        | Annotated[PlayerAction12117, _VARIANT_12117]
        | Annotated[CastingType12118, _VARIANT_12118]
        | Annotated[_values.FormId, _VARIANT_12119]
        | Annotated[_values.FormId, _VARIANT_12120]
        | Annotated[_values.FormId, _VARIANT_12121]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12122,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12123,
        ]
        | Annotated[_values.FormId, _VARIANT_12124]
        | Annotated[FurnitureAnim12125, _VARIANT_12125]
        | Annotated[FurnitureEntry12126, _VARIANT_12126]
        | Annotated[_values.FormId, _VARIANT_12127]
        | Annotated[WardState12128, _VARIANT_12128]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12129,
        ]
        | Annotated[_values.FormId, _VARIANT_12130]
        | Annotated[_values.FormId, _VARIANT_12131]
        | Annotated[_values.FormId, _VARIANT_12132]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12134]
        | Annotated[bytes, _VARIANT_12135]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12136,
        ]
        | Annotated[float, _VARIANT_12137]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12138,
        ]
        | Annotated[Sex12139, _VARIANT_12139]
        | Annotated[ActorValue12140, _VARIANT_12140]
        | Annotated[CrimeType12141, _VARIANT_12141]
        | Annotated[Axis12142, _VARIANT_12142]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12143,
        ]
        | Annotated[MiscStat12144, _VARIANT_12144]
        | Annotated[Alignment12145, _VARIANT_12145]
        | Annotated[_values.FormId, _VARIANT_12146]
        | Annotated[FormType12147, _VARIANT_12147]
        | Annotated[CriticalStage12148, _VARIANT_12148]
        | Annotated[_values.FormId, _VARIANT_12149]
        | Annotated[_values.FormId, _VARIANT_12150]
        | Annotated[_values.FormId, _VARIANT_12151]
        | Annotated[_values.FormId, _VARIANT_12152]
        | Annotated[_values.FormId, _VARIANT_12153]
        | Annotated[_values.FormId, _VARIANT_12154]
        | Annotated[_values.FormId, _VARIANT_12155]
        | Annotated[_values.FormId, _VARIANT_12156]
        | Annotated[_values.FormId, _VARIANT_12157]
        | Annotated[_values.FormId, _VARIANT_12158]
        | Annotated[_values.FormId, _VARIANT_12159]
        | Annotated[_values.FormId, _VARIANT_12160]
        | Annotated[_values.FormId, _VARIANT_12161]
        | Annotated[_values.FormId, _VARIANT_12162]
        | Annotated[_values.FormId, _VARIANT_12163]
        | Annotated[_values.FormId, _VARIANT_12164]
        | Annotated[_values.FormId, _VARIANT_12165]
        | Annotated[_values.FormId, _VARIANT_12166]
        | Annotated[_values.FormId, _VARIANT_12167]
        | Annotated[_values.FormId, _VARIANT_12168]
        | Annotated[_values.FormId, _VARIANT_12169]
        | Annotated[_values.FormId, _VARIANT_12170]
        | Annotated[VatsValueFunction12171, _VARIANT_12171]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12173]
            | Annotated[_values.FormId, _VARIANT_12174]
            | Annotated[_values.FormId, _VARIANT_12175]
            | Annotated[_values.FormId, _VARIANT_12176]
            | Annotated[bytes, _VARIANT_12177]
            | Annotated[TargetPart12178, _VARIANT_12178]
            | Annotated[VatsAction12179, _VARIANT_12179]
            | Annotated[bytes, _VARIANT_12180]
            | Annotated[bytes, _VARIANT_12181]
            | Annotated[_values.FormId, _VARIANT_12182]
            | Annotated[_values.FormId, _VARIANT_12183]
            | Annotated[bytes, _VARIANT_12184]
            | Annotated[bytes, _VARIANT_12185]
            | Annotated[bytes, _VARIANT_12186]
            | Annotated[bytes, _VARIANT_12187]
            | Annotated[WeaponType12188, _VARIANT_12188]
            | Annotated[bytes, _VARIANT_12189]
            | Annotated[bytes, _VARIANT_12190]
            | Annotated[ProjectileType12191, _VARIANT_12191]
            | Annotated[DeliveryType12192, _VARIANT_12192]
            | Annotated[CastingType12193, _VARIANT_12193],
            _VARIANT_12172,
        ]
        | Annotated[_values.FormId, _VARIANT_12194]
        | Annotated[_values.FormId, _VARIANT_12195]
        | Annotated[_values.FormId, _VARIANT_12196]
        | Annotated[PlayerAction12197, _VARIANT_12197]
        | Annotated[CastingType12198, _VARIANT_12198]
        | Annotated[_values.FormId, _VARIANT_12199]
        | Annotated[_values.FormId, _VARIANT_12200]
        | Annotated[_values.FormId, _VARIANT_12201]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12202,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12203,
        ]
        | Annotated[_values.FormId, _VARIANT_12204]
        | Annotated[FurnitureAnim12205, _VARIANT_12205]
        | Annotated[FurnitureEntry12206, _VARIANT_12206]
        | Annotated[_values.FormId, _VARIANT_12207]
        | Annotated[WardState12208, _VARIANT_12208]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12209,
        ]
        | Annotated[_values.FormId, _VARIANT_12210]
        | Annotated[_values.FormId, _VARIANT_12211]
        | Annotated[_values.FormId, _VARIANT_12212]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn12213]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12215,
        ]
        | Annotated[_values.FormId, _VARIANT_12216]
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


class Condition12064(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/4:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="PACK/4:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("PACK/4:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("PACK/4:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure12066] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure12066]]:
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


class Value12224(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    UNKNOWN = 0
    RANDOM = 8
    RUN_IN_SEQUENCE = 9
    RANDOM_DO_ONCE = 12
    RUN_IN_SEQUENCE_DO_ONCE = 13


class Structure12226(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/5:Idle Animations/1:IDLC/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "animation_count": _base.Binding(
            path=("PACK/5:Idle Animations/1:IDLC/payload/0:Animation Count"),
            kind="primitive",
            name="Animation Count",
        ),
        "unknown": _base.Binding(
            path="PACK/5:Idle Animations/1:IDLC/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    animation_count: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["animation_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
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


class IdleAnimations12222(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/5:Idle Animations"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="PACK/5:Idle Animations/0:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "idlc": _base.Binding(
            path="PACK/5:Idle Animations/1:IDLC",
            kind="subrecord",
            name="IDLC",
        ),
        "idle_timer_setting": _base.Binding(
            path="PACK/5:Idle Animations/2:Idle Timer Setting",
            kind="subrecord",
            name="Idle Timer Setting",
        ),
        "animations": _base.Binding(
            path="PACK/5:Idle Animations/3:Animations",
            kind="subrecord",
            name="Animations",
        ),
        "unknown": _base.Binding(
            path="PACK/5:Idle Animations/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
    }

    flags: Optional[Value12224] = None
    """Value decoded from this schema node."""

    idlc: Optional[Structure12226] = None
    """Value decoded from this schema node."""

    idle_timer_setting: Optional[float] = None
    """Value decoded from this schema node."""

    animations: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[Value12224]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["idlc"]
    ) -> _base.FieldRef[Optional[Structure12226]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["idle_timer_setting"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["animations"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
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


class Structure12241(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/8:Counter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "data_input_count": _base.Binding(
            path="PACK/8:Counter/payload/0:Data Input Count",
            kind="primitive",
            name="Data Input Count",
        ),
        "package_template": _base.Binding(
            path="PACK/8:Counter/payload/1:Package Template",
            kind="primitive",
            name="Package Template",
        ),
        "version_counter_autoincremented": _base.Binding(
            path=("PACK/8:Counter/payload/2:Version Counter (autoincremented)"),
            kind="primitive",
            name="Version Counter (autoincremented)",
        ),
    }

    data_input_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    package_template: _values.FormId
    """Value decoded from this schema node."""

    version_counter_autoincremented: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["data_input_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["package_template"]
    ) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["version_counter_autoincremented"]
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


_VARIANT_12252: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/1:Value/payload/variants/0:Unknown"
    )
)


class Bool12253(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_12253: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/1:Value/payload/variants/1:Bool"
    )
)


_VARIANT_12254: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/1:Value/payload/variants/2:Integer"
    )
)


_VARIANT_12255: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/1:Value/payload/variants/3:Float"
    )
)


class Type12261(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TOPIC_REF = 0
    TOPIC_SUBTYPE = 1


_VARIANT_12263: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/3:Topic/repeat/0:Topic Data/payload/1:Data/variants/0"
        ":Topic"
    )
)


_VARIANT_12264: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/3:Topic/repeat/0:Topic Data/payload/1:Data/variants/1"
        ":Subtype"
    )
)


class Structure12260(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/3:Topic/repeat/0:Topic Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/3:Topic/repeat/0:Topic Data/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "data": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/3:Topic/repeat/0:Topic Data/payload/1:Data"
            ),
            kind="union",
            name="Data",
        ),
    }

    type: Type12261
    """Value decoded from this schema node."""

    data: (
        Annotated[_values.FormId, _VARIANT_12263]
        | Annotated[str, _VARIANT_12264]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12261]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_12263]
        | Annotated[str, _VARIANT_12264]
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


class Type12267(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NEAR_REFERENCE = 0
    IN_CELL = 1
    NEAR_PACKAGE_START_LOCATION = 2
    NEAR_EDITOR_LOCATION = 3
    OBJECT_ID = 4
    OBJECT_TYPE = 5
    NEAR_LINKED_REFERENCE = 6
    AT_PACKAGE_LOCATION = 7
    ALIAS_REFERENCE = 8
    ALIAS_LOCATION = 9
    UNKNOWN_10 = 10
    UNKNOWN_11 = 11
    NEAR_SELF = 12


_VARIANT_12269: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/0:Refere"
        "nce"
    )
)


_VARIANT_12270: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/1:Cell"
    )
)


_VARIANT_12271: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/2:Near P"
        "ackage Start Location"
    )
)


_VARIANT_12272: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/3:Near E"
        "ditor Location"
    )
)


_VARIANT_12273: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/4:Object"
        " ID"
    )
)


_VARIANT_12274: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/5:Object"
        " Type"
    )
)


_VARIANT_12275: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/6:Keywor"
        "d"
    )
)


_VARIANT_12276: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/7:Unused"
    )
)


_VARIANT_12277: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/8:Alias"
    )
)


_VARIANT_12278: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/9:Refere"
        "nce"
    )
)


_VARIANT_12279: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/10:Unkno"
        "wn"
    )
)


_VARIANT_12280: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/11:Unkno"
        "wn"
    )
)


_VARIANT_12281: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload/1:Location Value/variants/12:Unkno"
        "wn"
    )
)


class Structure12266(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/4:Location/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/4:Location/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "location_value": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/4:Location/payload/1:Location Value"
            ),
            kind="union",
            name="Location Value",
        ),
        "radius": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/4:Location/payload/2:Radius"
            ),
            kind="primitive",
            name="Radius",
        ),
    }

    type: Type12267
    """Value decoded from this schema node."""

    location_value: (
        Annotated[_values.FormId, _VARIANT_12269]
        | Annotated[_values.FormId, _VARIANT_12270]
        | Annotated[bytes, _VARIANT_12271]
        | Annotated[bytes, _VARIANT_12272]
        | Annotated[_values.FormId, _VARIANT_12273]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12274,
        ]
        | Annotated[_values.FormId, _VARIANT_12275]
        | Annotated[bytes, _VARIANT_12276]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12277,
        ]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12278,
        ]
        | Annotated[bytes, _VARIANT_12279]
        | Annotated[bytes, _VARIANT_12280]
        | Annotated[bytes, _VARIANT_12281]
    )
    """Value decoded from this schema node."""

    radius: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12267]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location_value"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_12269]
        | Annotated[_values.FormId, _VARIANT_12270]
        | Annotated[bytes, _VARIANT_12271]
        | Annotated[bytes, _VARIANT_12272]
        | Annotated[_values.FormId, _VARIANT_12273]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12274,
        ]
        | Annotated[_values.FormId, _VARIANT_12275]
        | Annotated[bytes, _VARIANT_12276]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12277,
        ]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12278,
        ]
        | Annotated[bytes, _VARIANT_12279]
        | Annotated[bytes, _VARIANT_12280]
        | Annotated[bytes, _VARIANT_12281]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["radius"]
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


class Type12286(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SPECIFIC_REFERENCE = 0
    OBJECT_ID = 1
    OBJECT_TYPE = 2
    LINKED_REFERENCE = 3
    REF_ALIAS = 4
    UNKNOWN_5 = 5
    SELF = 6


_VARIANT_12288: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data/1:Target/variants/0:Re"
        "ference"
    )
)


_VARIANT_12289: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data/1:Target/variants/1:Ob"
        "ject ID"
    )
)


_VARIANT_12290: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data/1:Target/variants/2:Ob"
        "ject Type"
    )
)


_VARIANT_12291: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data/1:Target/variants/3:Re"
        "ference"
    )
)


_VARIANT_12292: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data/1:Target/variants/4:Al"
        "ias"
    )
)


_VARIANT_12293: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data/1:Target/variants/5:Un"
        "known"
    )
)


_VARIANT_12294: _base.Variant = _base.Variant(
    path=(
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data/1:Target/variants/6:Un"
        "known"
    )
)


class TargetData12285(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload/0:Target Data"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/5:Target/payload/0:Target Data/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "target": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/5:Target/payload/0:Target Data/1:Target"
            ),
            kind="union",
            name="Target",
        ),
        "count_distance": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/5:Target/payload/0:Target Data/2:Count / Distance"
            ),
            kind="primitive",
            name="Count / Distance",
        ),
    }

    type: Type12286
    """Value decoded from this schema node."""

    target: (
        Annotated[_values.FormId, _VARIANT_12288]
        | Annotated[_values.FormId, _VARIANT_12289]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12290,
        ]
        | Annotated[_values.FormId, _VARIANT_12291]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12292,
        ]
        | Annotated[bytes, _VARIANT_12293]
        | Annotated[bytes, _VARIANT_12294]
    )
    """Value decoded from this schema node."""

    count_distance: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12286]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_12288]
        | Annotated[_values.FormId, _VARIANT_12289]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12290,
        ]
        | Annotated[_values.FormId, _VARIANT_12291]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12292,
        ]
        | Annotated[bytes, _VARIANT_12293]
        | Annotated[bytes, _VARIANT_12294]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count_distance"]
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


class Structure12284(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
        "/5:Target/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "target_data": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/5:Target/payload/0:Target Data"
            ),
            kind="struct",
            name="Target Data",
        ),
    }

    target_data: TargetData12285
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["target_data"]
    ) -> _base.FieldRef[TargetData12285]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Value12247(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value/0:Type"
            ),
            kind="subrecord",
            name="Type",
        ),
        "value": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value/1:Value"
            ),
            kind="subrecord",
            name="Value",
        ),
        "unknown": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/2:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
        "topic": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value/3:Topic"
            ),
            kind="repeat",
            name="Topic",
            repeated_path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/3:Topic/repeat/0:Topic Data"
            ),
            child_kind="subrecord",
        ),
        "location": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/4:Location"
            ),
            kind="subrecord",
            name="Location",
        ),
        "target": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/5:Target"
            ),
            kind="subrecord",
            name="Target",
        ),
        "unknown_12296": _base.Binding(
            path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
                "/6:Unknown"
            ),
            kind="subrecord",
            name="Unknown",
        ),
    }

    type: Optional[str] = None
    """Value decoded from this schema node."""

    value: Optional[
        Annotated[bytes, _VARIANT_12252]
        | Annotated[Bool12253, _VARIANT_12253]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12254,
        ]
        | Annotated[float, _VARIANT_12255]
    ] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    topic: tuple[Structure12260, ...] = ()
    """Value decoded from this schema node."""

    location: Optional[Structure12266] = None
    """Value decoded from this schema node."""

    target: Optional[Structure12284] = None
    """Value decoded from this schema node."""

    unknown_12296: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[bytes, _VARIANT_12252]
            | Annotated[Bool12253, _VARIANT_12253]
            | Annotated[
                Annotated[
                    int, pydantic.Field(strict=True, ge=0, le=4294967295)
                ],
                _VARIANT_12254,
            ]
            | Annotated[float, _VARIANT_12255]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[tuple[Structure12260, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location"]
    ) -> _base.FieldRef[Optional[Structure12266]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["target"]
    ) -> _base.FieldRef[Optional[Structure12284]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_12296"]
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


class Public12305(enum.IntFlag):
    """Named values from the pinned schema."""

    PUBLIC = 1


class DataInput12299(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/9:Package Data/1:Data Inputs/repeat/0:Data Input"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "index": _base.Binding(
            path=(
                "PACK/9:Package Data/1:Data Inputs/repeat/0:Data Input/0:Index"
            ),
            kind="subrecord",
            name="Index",
        ),
        "name": _base.Binding(
            path=(
                "PACK/9:Package Data/1:Data Inputs/repeat/0:Data Input/1:Name"
            ),
            kind="subrecord",
            name="Name",
        ),
        "flags": _base.Binding(
            path=(
                "PACK/9:Package Data/1:Data Inputs/repeat/0:Data Input/2:Flags"
            ),
            kind="subrecord",
            name="Flags",
        ),
    }

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ] = None
    """Value decoded from this schema node."""

    name: Optional[str] = None
    """Value decoded from this schema node."""

    flags: Optional[Public12305] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["name"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[Public12305]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class PackageData12245(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/9:Package Data"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "data_input_values": _base.Binding(
            path="PACK/9:Package Data/0:Data Input Values",
            kind="repeat",
            name="Data Input Values",
            repeated_path=(
                "PACK/9:Package Data/0:Data Input Values/repeat/0:Value"
            ),
            child_kind="sequence",
        ),
        "data_inputs": _base.Binding(
            path="PACK/9:Package Data/1:Data Inputs",
            kind="repeat",
            name="Data Inputs",
            repeated_path=(
                "PACK/9:Package Data/1:Data Inputs/repeat/0:Data Input"
            ),
            child_kind="sequence",
        ),
    }

    data_input_values: tuple[Value12247, ...] = ()
    """Value decoded from this schema node."""

    data_inputs: tuple[DataInput12299, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["data_input_values"]
    ) -> _base.FieldRef[tuple[Value12247, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data_inputs"]
    ) -> _base.FieldRef[tuple[DataInput12299, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_12322: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/2:Compariso"
        "n Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_12323: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/2:Compariso"
        "n Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_12327: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/0:Unknown"
    )
)


_VARIANT_12328: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/1:None"
    )
)


_VARIANT_12329: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/2:Integer"
    )
)


_VARIANT_12330: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/3:Float"
    )
)


_VARIANT_12331: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/4:Variable Name"
    )
)


class Sex12332(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12332: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/5:Sex"
    )
)


class ActorValue12333(_values.OpenIntEnum):
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


_VARIANT_12333: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/6:Actor Value"
    )
)


class CrimeType12334(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12334: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/7:Crime Type"
    )
)


class Axis12335(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12335: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/8:Axis"
    )
)


_VARIANT_12336: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat12337(_values.OpenIntEnum):
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


_VARIANT_12337: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/10:Misc Stat"
    )
)


class Alignment12338(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12338: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/11:Alignment"
    )
)


_VARIANT_12339: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/12:Equip Type"
    )
)


class FormType12340(_values.OpenIntEnum):
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


_VARIANT_12340: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/13:Form Type"
    )
)


class CriticalStage12341(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12341: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/14:Critical Stage"
    )
)


_VARIANT_12342: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/15:Object Reference"
    )
)


_VARIANT_12343: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/16:Inventory Object"
    )
)


_VARIANT_12344: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/17:Actor"
    )
)


_VARIANT_12345: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/18:Voice Type"
    )
)


_VARIANT_12346: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/19:Idle"
    )
)


_VARIANT_12347: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/20:Form List"
    )
)


_VARIANT_12348: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/21:Quest"
    )
)


_VARIANT_12349: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/22:Faction"
    )
)


_VARIANT_12350: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/23:Cell"
    )
)


_VARIANT_12351: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/24:Class"
    )
)


_VARIANT_12352: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/25:Race"
    )
)


_VARIANT_12353: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/26:Actor Base"
    )
)


_VARIANT_12354: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/27:Global"
    )
)


_VARIANT_12355: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/28:Weather"
    )
)


_VARIANT_12356: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/29:Package"
    )
)


_VARIANT_12357: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/30:Encounter Zone"
    )
)


_VARIANT_12358: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/31:Perk"
    )
)


_VARIANT_12359: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/32:Owner"
    )
)


_VARIANT_12360: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/33:Furniture"
    )
)


_VARIANT_12361: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/34:Effect Item"
    )
)


_VARIANT_12362: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/35:Base Effect"
    )
)


_VARIANT_12363: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/36:Worldspace"
    )
)


class VatsValueFunction12364(_values.OpenIntEnum):
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


_VARIANT_12364: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/37:VATS Value Function"
    )
)


_VARIANT_12365: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_12366: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/39:Referenceable Object"
    )
)


_VARIANT_12367: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/40:Region"
    )
)


_VARIANT_12368: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/41:Keyword"
    )
)


class PlayerAction12369(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12369: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/42:Player Action"
    )
)


class CastingType12370(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12370: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/43:Casting Type"
    )
)


_VARIANT_12371: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/44:Shout"
    )
)


_VARIANT_12372: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/45:Location"
    )
)


_VARIANT_12373: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/46:Location Ref Type"
    )
)


_VARIANT_12374: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/47:Alias"
    )
)


_VARIANT_12375: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/48:Packdata ID"
    )
)


_VARIANT_12376: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/49:Association Type"
    )
)


class FurnitureAnim12377(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_12377: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry12378(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_12378: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/51:Furniture Entry"
    )
)


_VARIANT_12379: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/52:Scene"
    )
)


class WardState12380(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_12380: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/53:Ward State"
    )
)


_VARIANT_12381: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/54:Event"
    )
)


_VARIANT_12382: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/55:Event Data"
    )
)


_VARIANT_12383: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/56:Knowable"
    )
)


_VARIANT_12384: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
        " #1/variants/57:Faction"
    )
)


_VARIANT_12386: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/0:Unknown"
    )
)


_VARIANT_12387: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/1:None"
    )
)


_VARIANT_12388: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/2:Integer"
    )
)


_VARIANT_12389: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/3:Float"
    )
)


_VARIANT_12390: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/4:Variable Name"
    )
)


class Sex12391(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12391: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/5:Sex"
    )
)


class ActorValue12392(_values.OpenIntEnum):
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


_VARIANT_12392: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/6:Actor Value"
    )
)


class CrimeType12393(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12393: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/7:Crime Type"
    )
)


class Axis12394(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12394: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/8:Axis"
    )
)


_VARIANT_12395: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/9:Quest Stage"
    )
)


class MiscStat12396(_values.OpenIntEnum):
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


_VARIANT_12396: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/10:Misc Stat"
    )
)


class Alignment12397(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12397: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/11:Alignment"
    )
)


_VARIANT_12398: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/12:Equip Type"
    )
)


class FormType12399(_values.OpenIntEnum):
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


_VARIANT_12399: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/13:Form Type"
    )
)


class CriticalStage12400(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12400: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/14:Critical Stage"
    )
)


_VARIANT_12401: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/15:Object Reference"
    )
)


_VARIANT_12402: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/16:Inventory Object"
    )
)


_VARIANT_12403: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/17:Actor"
    )
)


_VARIANT_12404: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/18:Voice Type"
    )
)


_VARIANT_12405: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/19:Idle"
    )
)


_VARIANT_12406: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/20:Form List"
    )
)


_VARIANT_12407: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/21:Quest"
    )
)


_VARIANT_12408: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/22:Faction"
    )
)


_VARIANT_12409: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/23:Cell"
    )
)


_VARIANT_12410: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/24:Class"
    )
)


_VARIANT_12411: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/25:Race"
    )
)


_VARIANT_12412: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/26:Actor Base"
    )
)


_VARIANT_12413: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/27:Global"
    )
)


_VARIANT_12414: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/28:Weather"
    )
)


_VARIANT_12415: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/29:Package"
    )
)


_VARIANT_12416: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/30:Encounter Zone"
    )
)


_VARIANT_12417: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/31:Perk"
    )
)


_VARIANT_12418: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/32:Owner"
    )
)


_VARIANT_12419: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/33:Furniture"
    )
)


_VARIANT_12420: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/34:Effect Item"
    )
)


_VARIANT_12421: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/35:Base Effect"
    )
)


_VARIANT_12422: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/36:Worldspace"
    )
)


class VatsValueFunction12423(_values.OpenIntEnum):
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


_VARIANT_12423: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/37:VATS Value Function"
    )
)


_VARIANT_12425: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/0:Weapon"
    )
)


_VARIANT_12426: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/1:Weapon Lis"
        "t"
    )
)


_VARIANT_12427: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/2:Target"
    )
)


_VARIANT_12428: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/3:Target Lis"
        "t"
    )
)


_VARIANT_12429: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/4:Unknown"
    )
)


class TargetPart12430(_values.OpenIntEnum):
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


_VARIANT_12430: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/5:Target Par"
        "t"
    )
)


class VatsAction12431(_values.OpenIntEnum):
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


_VARIANT_12431: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/6:VATS Actio"
        "n"
    )
)


_VARIANT_12432: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/7:Unknown"
    )
)


_VARIANT_12433: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/8:Unknown"
    )
)


_VARIANT_12434: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/9:Critical E"
        "ffect"
    )
)


_VARIANT_12435: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/10:Critical "
        "Effect List"
    )
)


_VARIANT_12436: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/11:Unknown"
    )
)


_VARIANT_12437: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/12:Unknown"
    )
)


_VARIANT_12438: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/13:Unknown"
    )
)


_VARIANT_12439: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/14:Unknown"
    )
)


class WeaponType12440(_values.OpenIntEnum):
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


_VARIANT_12440: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/15:Weapon Ty"
        "pe"
    )
)


_VARIANT_12441: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/16:Unknown"
    )
)


_VARIANT_12442: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/17:Unknown"
    )
)


class ProjectileType12443(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_12443: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/18:Projectil"
        "e Type"
    )
)


class DeliveryType12444(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_12444: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/19:Delivery "
        "Type"
    )
)


class CastingType12445(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_12445: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param/variants/20:Casting T"
        "ype"
    )
)


_VARIANT_12424: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/38:VATS Value Param"
    )
)


_VARIANT_12446: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/39:Referenceable Object"
    )
)


_VARIANT_12447: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/40:Region"
    )
)


_VARIANT_12448: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/41:Keyword"
    )
)


class PlayerAction12449(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12449: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/42:Player Action"
    )
)


class CastingType12450(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12450: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/43:Casting Type"
    )
)


_VARIANT_12451: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/44:Shout"
    )
)


_VARIANT_12452: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/45:Location"
    )
)


_VARIANT_12453: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/46:Location Ref Type"
    )
)


_VARIANT_12454: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/47:Alias"
    )
)


_VARIANT_12455: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/48:Packdata ID"
    )
)


_VARIANT_12456: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/49:Association Type"
    )
)


class FurnitureAnim12457(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_12457: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry12458(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_12458: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/51:Furniture Entry"
    )
)


_VARIANT_12459: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/52:Scene"
    )
)


class WardState12460(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_12460: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/53:Ward State"
    )
)


_VARIANT_12461: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/54:Event"
    )
)


_VARIANT_12462: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/55:Event Data"
    )
)


_VARIANT_12463: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/56:Knowable"
    )
)


_VARIANT_12464: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
        " #2/variants/57:Faction"
    )
)


class RunOn12465(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_12467: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/8:Reference"
        "/variants/0:Unused"
    )
)


_VARIANT_12468: _base.Variant = _base.Variant(
    path=(
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload/8:Reference"
        "/variants/1:Reference"
    )
)


class Structure12318(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/2:Compariso"
                "n Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_12325": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/5:Parameter"
                " #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/6:Parameter"
                " #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA/payload/9:Parameter"
                " #3"
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
        Annotated[float, _VARIANT_12322]
        | Annotated[_values.FormId, _VARIANT_12323]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_12325: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_12327]
        | Annotated[bytes, _VARIANT_12328]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12329,
        ]
        | Annotated[float, _VARIANT_12330]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12331,
        ]
        | Annotated[Sex12332, _VARIANT_12332]
        | Annotated[ActorValue12333, _VARIANT_12333]
        | Annotated[CrimeType12334, _VARIANT_12334]
        | Annotated[Axis12335, _VARIANT_12335]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12336,
        ]
        | Annotated[MiscStat12337, _VARIANT_12337]
        | Annotated[Alignment12338, _VARIANT_12338]
        | Annotated[_values.FormId, _VARIANT_12339]
        | Annotated[FormType12340, _VARIANT_12340]
        | Annotated[CriticalStage12341, _VARIANT_12341]
        | Annotated[_values.FormId, _VARIANT_12342]
        | Annotated[_values.FormId, _VARIANT_12343]
        | Annotated[_values.FormId, _VARIANT_12344]
        | Annotated[_values.FormId, _VARIANT_12345]
        | Annotated[_values.FormId, _VARIANT_12346]
        | Annotated[_values.FormId, _VARIANT_12347]
        | Annotated[_values.FormId, _VARIANT_12348]
        | Annotated[_values.FormId, _VARIANT_12349]
        | Annotated[_values.FormId, _VARIANT_12350]
        | Annotated[_values.FormId, _VARIANT_12351]
        | Annotated[_values.FormId, _VARIANT_12352]
        | Annotated[_values.FormId, _VARIANT_12353]
        | Annotated[_values.FormId, _VARIANT_12354]
        | Annotated[_values.FormId, _VARIANT_12355]
        | Annotated[_values.FormId, _VARIANT_12356]
        | Annotated[_values.FormId, _VARIANT_12357]
        | Annotated[_values.FormId, _VARIANT_12358]
        | Annotated[_values.FormId, _VARIANT_12359]
        | Annotated[_values.FormId, _VARIANT_12360]
        | Annotated[_values.FormId, _VARIANT_12361]
        | Annotated[_values.FormId, _VARIANT_12362]
        | Annotated[_values.FormId, _VARIANT_12363]
        | Annotated[VatsValueFunction12364, _VARIANT_12364]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12365,
        ]
        | Annotated[_values.FormId, _VARIANT_12366]
        | Annotated[_values.FormId, _VARIANT_12367]
        | Annotated[_values.FormId, _VARIANT_12368]
        | Annotated[PlayerAction12369, _VARIANT_12369]
        | Annotated[CastingType12370, _VARIANT_12370]
        | Annotated[_values.FormId, _VARIANT_12371]
        | Annotated[_values.FormId, _VARIANT_12372]
        | Annotated[_values.FormId, _VARIANT_12373]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12374,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12375,
        ]
        | Annotated[_values.FormId, _VARIANT_12376]
        | Annotated[FurnitureAnim12377, _VARIANT_12377]
        | Annotated[FurnitureEntry12378, _VARIANT_12378]
        | Annotated[_values.FormId, _VARIANT_12379]
        | Annotated[WardState12380, _VARIANT_12380]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12381,
        ]
        | Annotated[_values.FormId, _VARIANT_12382]
        | Annotated[_values.FormId, _VARIANT_12383]
        | Annotated[_values.FormId, _VARIANT_12384]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_12386]
        | Annotated[bytes, _VARIANT_12387]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12388,
        ]
        | Annotated[float, _VARIANT_12389]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12390,
        ]
        | Annotated[Sex12391, _VARIANT_12391]
        | Annotated[ActorValue12392, _VARIANT_12392]
        | Annotated[CrimeType12393, _VARIANT_12393]
        | Annotated[Axis12394, _VARIANT_12394]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12395,
        ]
        | Annotated[MiscStat12396, _VARIANT_12396]
        | Annotated[Alignment12397, _VARIANT_12397]
        | Annotated[_values.FormId, _VARIANT_12398]
        | Annotated[FormType12399, _VARIANT_12399]
        | Annotated[CriticalStage12400, _VARIANT_12400]
        | Annotated[_values.FormId, _VARIANT_12401]
        | Annotated[_values.FormId, _VARIANT_12402]
        | Annotated[_values.FormId, _VARIANT_12403]
        | Annotated[_values.FormId, _VARIANT_12404]
        | Annotated[_values.FormId, _VARIANT_12405]
        | Annotated[_values.FormId, _VARIANT_12406]
        | Annotated[_values.FormId, _VARIANT_12407]
        | Annotated[_values.FormId, _VARIANT_12408]
        | Annotated[_values.FormId, _VARIANT_12409]
        | Annotated[_values.FormId, _VARIANT_12410]
        | Annotated[_values.FormId, _VARIANT_12411]
        | Annotated[_values.FormId, _VARIANT_12412]
        | Annotated[_values.FormId, _VARIANT_12413]
        | Annotated[_values.FormId, _VARIANT_12414]
        | Annotated[_values.FormId, _VARIANT_12415]
        | Annotated[_values.FormId, _VARIANT_12416]
        | Annotated[_values.FormId, _VARIANT_12417]
        | Annotated[_values.FormId, _VARIANT_12418]
        | Annotated[_values.FormId, _VARIANT_12419]
        | Annotated[_values.FormId, _VARIANT_12420]
        | Annotated[_values.FormId, _VARIANT_12421]
        | Annotated[_values.FormId, _VARIANT_12422]
        | Annotated[VatsValueFunction12423, _VARIANT_12423]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12425]
            | Annotated[_values.FormId, _VARIANT_12426]
            | Annotated[_values.FormId, _VARIANT_12427]
            | Annotated[_values.FormId, _VARIANT_12428]
            | Annotated[bytes, _VARIANT_12429]
            | Annotated[TargetPart12430, _VARIANT_12430]
            | Annotated[VatsAction12431, _VARIANT_12431]
            | Annotated[bytes, _VARIANT_12432]
            | Annotated[bytes, _VARIANT_12433]
            | Annotated[_values.FormId, _VARIANT_12434]
            | Annotated[_values.FormId, _VARIANT_12435]
            | Annotated[bytes, _VARIANT_12436]
            | Annotated[bytes, _VARIANT_12437]
            | Annotated[bytes, _VARIANT_12438]
            | Annotated[bytes, _VARIANT_12439]
            | Annotated[WeaponType12440, _VARIANT_12440]
            | Annotated[bytes, _VARIANT_12441]
            | Annotated[bytes, _VARIANT_12442]
            | Annotated[ProjectileType12443, _VARIANT_12443]
            | Annotated[DeliveryType12444, _VARIANT_12444]
            | Annotated[CastingType12445, _VARIANT_12445],
            _VARIANT_12424,
        ]
        | Annotated[_values.FormId, _VARIANT_12446]
        | Annotated[_values.FormId, _VARIANT_12447]
        | Annotated[_values.FormId, _VARIANT_12448]
        | Annotated[PlayerAction12449, _VARIANT_12449]
        | Annotated[CastingType12450, _VARIANT_12450]
        | Annotated[_values.FormId, _VARIANT_12451]
        | Annotated[_values.FormId, _VARIANT_12452]
        | Annotated[_values.FormId, _VARIANT_12453]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12454,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12455,
        ]
        | Annotated[_values.FormId, _VARIANT_12456]
        | Annotated[FurnitureAnim12457, _VARIANT_12457]
        | Annotated[FurnitureEntry12458, _VARIANT_12458]
        | Annotated[_values.FormId, _VARIANT_12459]
        | Annotated[WardState12460, _VARIANT_12460]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12461,
        ]
        | Annotated[_values.FormId, _VARIANT_12462]
        | Annotated[_values.FormId, _VARIANT_12463]
        | Annotated[_values.FormId, _VARIANT_12464]
    )
    """Value decoded from this schema node."""

    run_on: RunOn12465
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12467,
        ]
        | Annotated[_values.FormId, _VARIANT_12468]
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
        Annotated[float, _VARIANT_12322]
        | Annotated[_values.FormId, _VARIANT_12323]
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
    def field(self, name: Literal["unused_12325"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12327]
        | Annotated[bytes, _VARIANT_12328]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12329,
        ]
        | Annotated[float, _VARIANT_12330]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12331,
        ]
        | Annotated[Sex12332, _VARIANT_12332]
        | Annotated[ActorValue12333, _VARIANT_12333]
        | Annotated[CrimeType12334, _VARIANT_12334]
        | Annotated[Axis12335, _VARIANT_12335]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12336,
        ]
        | Annotated[MiscStat12337, _VARIANT_12337]
        | Annotated[Alignment12338, _VARIANT_12338]
        | Annotated[_values.FormId, _VARIANT_12339]
        | Annotated[FormType12340, _VARIANT_12340]
        | Annotated[CriticalStage12341, _VARIANT_12341]
        | Annotated[_values.FormId, _VARIANT_12342]
        | Annotated[_values.FormId, _VARIANT_12343]
        | Annotated[_values.FormId, _VARIANT_12344]
        | Annotated[_values.FormId, _VARIANT_12345]
        | Annotated[_values.FormId, _VARIANT_12346]
        | Annotated[_values.FormId, _VARIANT_12347]
        | Annotated[_values.FormId, _VARIANT_12348]
        | Annotated[_values.FormId, _VARIANT_12349]
        | Annotated[_values.FormId, _VARIANT_12350]
        | Annotated[_values.FormId, _VARIANT_12351]
        | Annotated[_values.FormId, _VARIANT_12352]
        | Annotated[_values.FormId, _VARIANT_12353]
        | Annotated[_values.FormId, _VARIANT_12354]
        | Annotated[_values.FormId, _VARIANT_12355]
        | Annotated[_values.FormId, _VARIANT_12356]
        | Annotated[_values.FormId, _VARIANT_12357]
        | Annotated[_values.FormId, _VARIANT_12358]
        | Annotated[_values.FormId, _VARIANT_12359]
        | Annotated[_values.FormId, _VARIANT_12360]
        | Annotated[_values.FormId, _VARIANT_12361]
        | Annotated[_values.FormId, _VARIANT_12362]
        | Annotated[_values.FormId, _VARIANT_12363]
        | Annotated[VatsValueFunction12364, _VARIANT_12364]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12365,
        ]
        | Annotated[_values.FormId, _VARIANT_12366]
        | Annotated[_values.FormId, _VARIANT_12367]
        | Annotated[_values.FormId, _VARIANT_12368]
        | Annotated[PlayerAction12369, _VARIANT_12369]
        | Annotated[CastingType12370, _VARIANT_12370]
        | Annotated[_values.FormId, _VARIANT_12371]
        | Annotated[_values.FormId, _VARIANT_12372]
        | Annotated[_values.FormId, _VARIANT_12373]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12374,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12375,
        ]
        | Annotated[_values.FormId, _VARIANT_12376]
        | Annotated[FurnitureAnim12377, _VARIANT_12377]
        | Annotated[FurnitureEntry12378, _VARIANT_12378]
        | Annotated[_values.FormId, _VARIANT_12379]
        | Annotated[WardState12380, _VARIANT_12380]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12381,
        ]
        | Annotated[_values.FormId, _VARIANT_12382]
        | Annotated[_values.FormId, _VARIANT_12383]
        | Annotated[_values.FormId, _VARIANT_12384]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12386]
        | Annotated[bytes, _VARIANT_12387]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12388,
        ]
        | Annotated[float, _VARIANT_12389]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12390,
        ]
        | Annotated[Sex12391, _VARIANT_12391]
        | Annotated[ActorValue12392, _VARIANT_12392]
        | Annotated[CrimeType12393, _VARIANT_12393]
        | Annotated[Axis12394, _VARIANT_12394]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12395,
        ]
        | Annotated[MiscStat12396, _VARIANT_12396]
        | Annotated[Alignment12397, _VARIANT_12397]
        | Annotated[_values.FormId, _VARIANT_12398]
        | Annotated[FormType12399, _VARIANT_12399]
        | Annotated[CriticalStage12400, _VARIANT_12400]
        | Annotated[_values.FormId, _VARIANT_12401]
        | Annotated[_values.FormId, _VARIANT_12402]
        | Annotated[_values.FormId, _VARIANT_12403]
        | Annotated[_values.FormId, _VARIANT_12404]
        | Annotated[_values.FormId, _VARIANT_12405]
        | Annotated[_values.FormId, _VARIANT_12406]
        | Annotated[_values.FormId, _VARIANT_12407]
        | Annotated[_values.FormId, _VARIANT_12408]
        | Annotated[_values.FormId, _VARIANT_12409]
        | Annotated[_values.FormId, _VARIANT_12410]
        | Annotated[_values.FormId, _VARIANT_12411]
        | Annotated[_values.FormId, _VARIANT_12412]
        | Annotated[_values.FormId, _VARIANT_12413]
        | Annotated[_values.FormId, _VARIANT_12414]
        | Annotated[_values.FormId, _VARIANT_12415]
        | Annotated[_values.FormId, _VARIANT_12416]
        | Annotated[_values.FormId, _VARIANT_12417]
        | Annotated[_values.FormId, _VARIANT_12418]
        | Annotated[_values.FormId, _VARIANT_12419]
        | Annotated[_values.FormId, _VARIANT_12420]
        | Annotated[_values.FormId, _VARIANT_12421]
        | Annotated[_values.FormId, _VARIANT_12422]
        | Annotated[VatsValueFunction12423, _VARIANT_12423]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12425]
            | Annotated[_values.FormId, _VARIANT_12426]
            | Annotated[_values.FormId, _VARIANT_12427]
            | Annotated[_values.FormId, _VARIANT_12428]
            | Annotated[bytes, _VARIANT_12429]
            | Annotated[TargetPart12430, _VARIANT_12430]
            | Annotated[VatsAction12431, _VARIANT_12431]
            | Annotated[bytes, _VARIANT_12432]
            | Annotated[bytes, _VARIANT_12433]
            | Annotated[_values.FormId, _VARIANT_12434]
            | Annotated[_values.FormId, _VARIANT_12435]
            | Annotated[bytes, _VARIANT_12436]
            | Annotated[bytes, _VARIANT_12437]
            | Annotated[bytes, _VARIANT_12438]
            | Annotated[bytes, _VARIANT_12439]
            | Annotated[WeaponType12440, _VARIANT_12440]
            | Annotated[bytes, _VARIANT_12441]
            | Annotated[bytes, _VARIANT_12442]
            | Annotated[ProjectileType12443, _VARIANT_12443]
            | Annotated[DeliveryType12444, _VARIANT_12444]
            | Annotated[CastingType12445, _VARIANT_12445],
            _VARIANT_12424,
        ]
        | Annotated[_values.FormId, _VARIANT_12446]
        | Annotated[_values.FormId, _VARIANT_12447]
        | Annotated[_values.FormId, _VARIANT_12448]
        | Annotated[PlayerAction12449, _VARIANT_12449]
        | Annotated[CastingType12450, _VARIANT_12450]
        | Annotated[_values.FormId, _VARIANT_12451]
        | Annotated[_values.FormId, _VARIANT_12452]
        | Annotated[_values.FormId, _VARIANT_12453]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12454,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12455,
        ]
        | Annotated[_values.FormId, _VARIANT_12456]
        | Annotated[FurnitureAnim12457, _VARIANT_12457]
        | Annotated[FurnitureEntry12458, _VARIANT_12458]
        | Annotated[_values.FormId, _VARIANT_12459]
        | Annotated[WardState12460, _VARIANT_12460]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12461,
        ]
        | Annotated[_values.FormId, _VARIANT_12462]
        | Annotated[_values.FormId, _VARIANT_12463]
        | Annotated[_values.FormId, _VARIANT_12464]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn12465]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12467,
        ]
        | Annotated[_values.FormId, _VARIANT_12468]
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


class Condition12316(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
        "nditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure12318] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure12318]]:
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


class Flags12477(enum.IntFlag):
    """Named values from the pinned schema."""

    REPEAT_WHEN_COMPLETE = 1
    UNKNOWN_1 = 2


class Structure12475(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/3:Root/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "branch_count": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/3:Ro"
                "ot/payload/0:Branch Count"
            ),
            kind="primitive",
            name="Branch Count",
        ),
        "flags": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/3:Ro"
                "ot/payload/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
    }

    branch_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    flags: Flags12477
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["branch_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12477]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class SuccessCompletesPackage12481(enum.IntFlag):
    """Named values from the pinned schema."""

    SUCCESS_COMPLETES_PACKAGE = 1


class SetGeneralFlags12488(enum.IntFlag):
    """Named values from the pinned schema."""

    OFFERS_SERVICES = 1
    UNKNOWN_2 = 2
    MUST_COMPLETE = 4
    MAINTAIN_SPEED_AT_GOAL = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNLOCK_DOORS_AT_PACKAGE_START = 64
    UNLOCK_DOORS_AT_PACKAGE_END = 128
    UNKNOWN_9 = 256
    CONTINUE_IF_PC_NEAR = 512
    ONCE_PER_DAY = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    PREFERRED_SPEED = 8192
    UNKNOWN_15 = 16384
    UNKNOWN_16 = 32768
    UNKNOWN_17 = 65536
    ALWAYS_SNEAK = 131072
    ALLOW_SWIMMING = 262144
    UNKNOWN_20 = 524288
    IGNORE_COMBAT = 1048576
    WEAPONS_UNEQUIPPED = 2097152
    UNKNOWN_23 = 4194304
    WEAPON_DRAWN = 8388608
    UNKNOWN_25 = 16777216
    UNKNOWN_26 = 33554432
    UNKNOWN_27 = 67108864
    NO_COMBAT_ALERT = 134217728
    UNKNOWN_29 = 268435456
    WEAR_SLEEP_OUTFIT_UNUSED = 536870912
    UNKNOWN_31 = 1073741824
    UNKNOWN_32 = 2147483648


class ClearGeneralFlags12489(enum.IntFlag):
    """Named values from the pinned schema."""

    OFFERS_SERVICES = 1
    UNKNOWN_2 = 2
    MUST_COMPLETE = 4
    MAINTAIN_SPEED_AT_GOAL = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNLOCK_DOORS_AT_PACKAGE_START = 64
    UNLOCK_DOORS_AT_PACKAGE_END = 128
    UNKNOWN_9 = 256
    CONTINUE_IF_PC_NEAR = 512
    ONCE_PER_DAY = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    PREFERRED_SPEED = 8192
    UNKNOWN_15 = 16384
    UNKNOWN_16 = 32768
    UNKNOWN_17 = 65536
    ALWAYS_SNEAK = 131072
    ALLOW_SWIMMING = 262144
    UNKNOWN_20 = 524288
    IGNORE_COMBAT = 1048576
    WEAPONS_UNEQUIPPED = 2097152
    UNKNOWN_23 = 4194304
    WEAPON_DRAWN = 8388608
    UNKNOWN_25 = 16777216
    UNKNOWN_26 = 33554432
    UNKNOWN_27 = 67108864
    NO_COMBAT_ALERT = 134217728
    UNKNOWN_29 = 268435456
    WEAR_SLEEP_OUTFIT_UNUSED = 536870912
    UNKNOWN_31 = 1073741824
    UNKNOWN_32 = 2147483648


class SetInterruptFlags12490(enum.IntFlag):
    """Named values from the pinned schema."""

    HELLOS_TO_PLAYER = 1
    RANDOM_CONVERSATIONS = 2
    OBSERVE_COMBAT_BEHAVIOR = 4
    GREET_CORPSE_BEHAVIOR = 8
    REACTION_TO_PLAYER_ACTIONS = 16
    FRIENDLY_FIRE_COMMENTS = 32
    AGGRO_RADIUS_BEHAVIOR = 64
    ALLOW_IDLE_CHATTER = 128
    UNKNOWN_9 = 256
    WORLD_INTERACTIONS = 512
    UNKNOWN_11 = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    UNKNOWN_14 = 8192
    UNKNOWN_15 = 16384
    UNKNOWN_16 = 32768


class ClearInterruptFlags12491(enum.IntFlag):
    """Named values from the pinned schema."""

    HELLOS_TO_PLAYER = 1
    RANDOM_CONVERSATIONS = 2
    OBSERVE_COMBAT_BEHAVIOR = 4
    GREET_CORPSE_BEHAVIOR = 8
    REACTION_TO_PLAYER_ACTIONS = 16
    FRIENDLY_FIRE_COMMENTS = 32
    AGGRO_RADIUS_BEHAVIOR = 64
    ALLOW_IDLE_CHATTER = 128
    UNKNOWN_9 = 256
    WORLD_INTERACTIONS = 512
    UNKNOWN_11 = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    UNKNOWN_14 = 8192
    UNKNOWN_15 = 16384
    UNKNOWN_16 = 32768


class PreferredSpeedOverride12492(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    WALK = 0
    JOG = 1
    RUN = 2
    FAST_WALK = 3


class Structure12487(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
        "ags Override/repeat/0:Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "set_general_flags": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override/repeat/0:Data/payload/0:Set General Flags"
            ),
            kind="primitive",
            name="Set General Flags",
        ),
        "clear_general_flags": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override/repeat/0:Data/payload/1:Clear General Fla"
                "gs"
            ),
            kind="primitive",
            name="Clear General Flags",
        ),
        "set_interrupt_flags": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override/repeat/0:Data/payload/2:Set Interrupt Fla"
                "gs"
            ),
            kind="primitive",
            name="Set Interrupt Flags",
        ),
        "clear_interrupt_flags": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override/repeat/0:Data/payload/3:Clear Interrupt F"
                "lags"
            ),
            kind="primitive",
            name="Clear Interrupt Flags",
        ),
        "preferred_speed_override": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override/repeat/0:Data/payload/4:Preferred Speed O"
                "verride"
            ),
            kind="primitive",
            name="Preferred Speed Override",
        ),
        "unknown": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override/repeat/0:Data/payload/5:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    set_general_flags: SetGeneralFlags12488
    """Value decoded from this schema node."""

    clear_general_flags: ClearGeneralFlags12489
    """Value decoded from this schema node."""

    set_interrupt_flags: SetInterruptFlags12490
    """Value decoded from this schema node."""

    clear_interrupt_flags: ClearInterruptFlags12491
    """Value decoded from this schema node."""

    preferred_speed_override: PreferredSpeedOverride12492
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["set_general_flags"]
    ) -> _base.FieldRef[SetGeneralFlags12488]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["clear_general_flags"]
    ) -> _base.FieldRef[ClearGeneralFlags12489]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["set_interrupt_flags"]
    ) -> _base.FieldRef[SetInterruptFlags12490]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["clear_interrupt_flags"]
    ) -> _base.FieldRef[ClearInterruptFlags12491]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["preferred_speed_override"]
    ) -> _base.FieldRef[PreferredSpeedOverride12492]:
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


class Branch12310(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "branch_type": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/0:Br"
                "anch Type"
            ),
            kind="subrecord",
            name="Branch Type",
        ),
        "condition_count": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/1:Co"
                "ndition Count"
            ),
            kind="subrecord",
            name="Condition Count",
        ),
        "conditions": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Conditions"
            ),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/2:Co"
                "nditions/repeat/0:Condition"
            ),
            child_kind="sequence",
        ),
        "root": _base.Binding(
            path=("PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/3:Root"),
            kind="subrecord",
            name="Root",
        ),
        "procedure_type": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/4:Pr"
                "ocedure Type"
            ),
            kind="subrecord",
            name="Procedure Type",
        ),
        "flags": _base.Binding(
            path=("PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/5:Flags"),
            kind="subrecord",
            name="Flags",
        ),
        "data_input_indexes": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/6:Da"
                "ta Input Indexes"
            ),
            kind="repeat",
            name="Data Input Indexes",
            repeated_path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/6:Da"
                "ta Input Indexes/repeat/0:Index"
            ),
            child_kind="subrecord",
        ),
        "flags_override": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override"
            ),
            kind="repeat",
            name="Flags Override",
            repeated_path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/7:Fl"
                "ags Override/repeat/0:Data"
            ),
            child_kind="subrecord",
        ),
        "unknown": _base.Binding(
            path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/8:Unknown"
            ),
            kind="repeat",
            name="Unknown",
            repeated_path=(
                "PACK/11:Procedure Tree/0:Branches/repeat/0:Branch/8:Un"
                "known/repeat/0:Unknown"
            ),
            child_kind="subrecord",
        ),
    }

    branch_type: Optional[str] = None
    """Value decoded from this schema node."""

    condition_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition12316, ...] = ()
    """Value decoded from this schema node."""

    root: Optional[Structure12475] = None
    """Value decoded from this schema node."""

    procedure_type: Optional[str] = None
    """Value decoded from this schema node."""

    flags: Optional[SuccessCompletesPackage12481] = None
    """Value decoded from this schema node."""

    data_input_indexes: tuple[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...
    ] = ()
    """Value decoded from this schema node."""

    flags_override: tuple[Structure12487, ...] = ()
    """Value decoded from this schema node."""

    unknown: tuple[bytes, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["branch_type"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["condition_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition12316, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["root"]
    ) -> _base.FieldRef[Optional[Structure12475]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["procedure_type"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[SuccessCompletesPackage12481]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data_input_indexes"]
    ) -> _base.FieldRef[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags_override"]
    ) -> _base.FieldRef[tuple[Structure12487, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[tuple[bytes, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ProcedureTree12308(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/11:Procedure Tree"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "branches": _base.Binding(
            path="PACK/11:Procedure Tree/0:Branches",
            kind="repeat",
            name="Branches",
            repeated_path="PACK/11:Procedure Tree/0:Branches/repeat/0:Branch",
            child_kind="sequence",
        ),
    }

    branches: tuple[Branch12310, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["branches"]
    ) -> _base.FieldRef[tuple[Branch12310, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Public12504(enum.IntFlag):
    """Named values from the pinned schema."""

    PUBLIC = 1


class DataInput12498(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/12:Data Inputs/repeat/0:Data Input"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "index": _base.Binding(
            path="PACK/12:Data Inputs/repeat/0:Data Input/0:Index",
            kind="subrecord",
            name="Index",
        ),
        "name": _base.Binding(
            path="PACK/12:Data Inputs/repeat/0:Data Input/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "flags": _base.Binding(
            path="PACK/12:Data Inputs/repeat/0:Data Input/2:Flags",
            kind="subrecord",
            name="Flags",
        ),
    }

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ] = None
    """Value decoded from this schema node."""

    name: Optional[str] = None
    """Value decoded from this schema node."""

    flags: Optional[Public12504] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["name"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[Public12504]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type12521(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TOPIC_REF = 0
    TOPIC_SUBTYPE = 1


_VARIANT_12523: _base.Variant = _base.Variant(
    path=(
        "PACK/13:OnBegin/6:Topic/repeat/0:Topic Data/payload/1:"
        "Data/variants/0:Topic"
    )
)


_VARIANT_12524: _base.Variant = _base.Variant(
    path=(
        "PACK/13:OnBegin/6:Topic/repeat/0:Topic Data/payload/1:"
        "Data/variants/1:Subtype"
    )
)


class Structure12520(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/13:OnBegin/6:Topic/repeat/0:Topic Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("PACK/13:OnBegin/6:Topic/repeat/0:Topic Data/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "data": _base.Binding(
            path=("PACK/13:OnBegin/6:Topic/repeat/0:Topic Data/payload/1:Data"),
            kind="union",
            name="Data",
        ),
    }

    type: Type12521
    """Value decoded from this schema node."""

    data: (
        Annotated[_values.FormId, _VARIANT_12523]
        | Annotated[str, _VARIANT_12524]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12521]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_12523]
        | Annotated[str, _VARIANT_12524]
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


class OnBegin12505(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/13:OnBegin"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "on_begin_marker": _base.Binding(
            path="PACK/13:OnBegin/0:OnBegin Marker",
            kind="subrecord",
            name="OnBegin Marker",
        ),
        "idle": _base.Binding(
            path="PACK/13:OnBegin/1:Idle",
            kind="subrecord",
            name="Idle",
        ),
        "unused": _base.Binding(
            path="PACK/13:OnBegin/2:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12512": _base.Binding(
            path="PACK/13:OnBegin/3:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12514": _base.Binding(
            path="PACK/13:OnBegin/4:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12516": _base.Binding(
            path="PACK/13:OnBegin/5:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "topic": _base.Binding(
            path="PACK/13:OnBegin/6:Topic",
            kind="repeat",
            name="Topic",
            repeated_path="PACK/13:OnBegin/6:Topic/repeat/0:Topic Data",
            child_kind="subrecord",
        ),
    }

    on_begin_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    idle: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12512: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12514: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12516: Optional[bytes] = None
    """Value decoded from this schema node."""

    topic: tuple[Structure12520, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["on_begin_marker"]
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
        self, name: Literal["unused_12512"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_12514"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_12516"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[tuple[Structure12520, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type12541(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TOPIC_REF = 0
    TOPIC_SUBTYPE = 1


_VARIANT_12543: _base.Variant = _base.Variant(
    path=(
        "PACK/14:OnEnd/6:Topic/repeat/0:Topic Data/payload/1:Da"
        "ta/variants/0:Topic"
    )
)


_VARIANT_12544: _base.Variant = _base.Variant(
    path=(
        "PACK/14:OnEnd/6:Topic/repeat/0:Topic Data/payload/1:Da"
        "ta/variants/1:Subtype"
    )
)


class Structure12540(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/14:OnEnd/6:Topic/repeat/0:Topic Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("PACK/14:OnEnd/6:Topic/repeat/0:Topic Data/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "data": _base.Binding(
            path=("PACK/14:OnEnd/6:Topic/repeat/0:Topic Data/payload/1:Data"),
            kind="union",
            name="Data",
        ),
    }

    type: Type12541
    """Value decoded from this schema node."""

    data: (
        Annotated[_values.FormId, _VARIANT_12543]
        | Annotated[str, _VARIANT_12544]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12541]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_12543]
        | Annotated[str, _VARIANT_12544]
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


class OnEnd12525(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/14:OnEnd"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "on_end_marker": _base.Binding(
            path="PACK/14:OnEnd/0:OnEnd Marker",
            kind="subrecord",
            name="OnEnd Marker",
        ),
        "idle": _base.Binding(
            path="PACK/14:OnEnd/1:Idle",
            kind="subrecord",
            name="Idle",
        ),
        "unused": _base.Binding(
            path="PACK/14:OnEnd/2:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12532": _base.Binding(
            path="PACK/14:OnEnd/3:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12534": _base.Binding(
            path="PACK/14:OnEnd/4:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12536": _base.Binding(
            path="PACK/14:OnEnd/5:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "topic": _base.Binding(
            path="PACK/14:OnEnd/6:Topic",
            kind="repeat",
            name="Topic",
            repeated_path="PACK/14:OnEnd/6:Topic/repeat/0:Topic Data",
            child_kind="subrecord",
        ),
    }

    on_end_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    idle: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12532: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12534: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12536: Optional[bytes] = None
    """Value decoded from this schema node."""

    topic: tuple[Structure12540, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["on_end_marker"]
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
        self, name: Literal["unused_12532"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_12534"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_12536"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[tuple[Structure12540, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type12563(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    TOPIC_REF = 0
    TOPIC_SUBTYPE = 1


_VARIANT_12565: _base.Variant = _base.Variant(
    path=(
        "PACK/15:OnChange/7:Topic/repeat/0:Topic Data/payload/1"
        ":Data/variants/0:Topic"
    )
)


_VARIANT_12566: _base.Variant = _base.Variant(
    path=(
        "PACK/15:OnChange/7:Topic/repeat/0:Topic Data/payload/1"
        ":Data/variants/1:Subtype"
    )
)


class Structure12562(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PACK/15:OnChange/7:Topic/repeat/0:Topic Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PACK/15:OnChange/7:Topic/repeat/0:Topic Data/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "data": _base.Binding(
            path=(
                "PACK/15:OnChange/7:Topic/repeat/0:Topic Data/payload/1:Data"
            ),
            kind="union",
            name="Data",
        ),
    }

    type: Type12563
    """Value decoded from this schema node."""

    data: (
        Annotated[_values.FormId, _VARIANT_12565]
        | Annotated[str, _VARIANT_12566]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12563]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Annotated[_values.FormId, _VARIANT_12565]
        | Annotated[str, _VARIANT_12566]
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


class OnChange12545(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK/15:OnChange"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "on_change_marker": _base.Binding(
            path="PACK/15:OnChange/0:OnChange Marker",
            kind="subrecord",
            name="OnChange Marker",
        ),
        "idle": _base.Binding(
            path="PACK/15:OnChange/1:Idle",
            kind="subrecord",
            name="Idle",
        ),
        "unused": _base.Binding(
            path="PACK/15:OnChange/2:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12552": _base.Binding(
            path="PACK/15:OnChange/3:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12554": _base.Binding(
            path="PACK/15:OnChange/4:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12556": _base.Binding(
            path="PACK/15:OnChange/5:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "unused_12558": _base.Binding(
            path="PACK/15:OnChange/6:Unused",
            kind="subrecord",
            name="Unused",
        ),
        "topic": _base.Binding(
            path="PACK/15:OnChange/7:Topic",
            kind="repeat",
            name="Topic",
            repeated_path="PACK/15:OnChange/7:Topic/repeat/0:Topic Data",
            child_kind="subrecord",
        ),
    }

    on_change_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    idle: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12552: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12554: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12556: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_12558: Optional[bytes] = None
    """Value decoded from this schema node."""

    topic: tuple[Structure12562, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["on_change_marker"]
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
        self, name: Literal["unused_12552"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_12554"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_12556"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_12558"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[tuple[Structure12562, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class PackageRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PACK"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "PACK"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="PACK/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="PACK/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "pack_data": _base.Binding(
            path="PACK/2:Pack Data",
            kind="subrecord",
            name="Pack Data",
        ),
        "schedule": _base.Binding(
            path="PACK/3:Schedule",
            kind="subrecord",
            name="Schedule",
        ),
        "conditions": _base.Binding(
            path="PACK/4:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="PACK/4:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "idle_animations": _base.Binding(
            path="PACK/5:Idle Animations",
            kind="sequence",
            name="Idle Animations",
        ),
        "combat_style": _base.Binding(
            path="PACK/6:Combat Style",
            kind="subrecord",
            name="Combat Style",
        ),
        "owner_quest": _base.Binding(
            path="PACK/7:Owner Quest",
            kind="subrecord",
            name="Owner Quest",
        ),
        "counter": _base.Binding(
            path="PACK/8:Counter",
            kind="subrecord",
            name="Counter",
        ),
        "package_data": _base.Binding(
            path="PACK/9:Package Data",
            kind="sequence",
            name="Package Data",
        ),
        "marker": _base.Binding(
            path="PACK/10:Marker",
            kind="subrecord",
            name="Marker",
        ),
        "procedure_tree": _base.Binding(
            path="PACK/11:Procedure Tree",
            kind="sequence",
            name="Procedure Tree",
        ),
        "data_inputs": _base.Binding(
            path="PACK/12:Data Inputs",
            kind="repeat",
            name="Data Inputs",
            repeated_path="PACK/12:Data Inputs/repeat/0:Data Input",
            child_kind="sequence",
        ),
        "on_begin": _base.Binding(
            path="PACK/13:OnBegin",
            kind="sequence",
            name="OnBegin",
        ),
        "on_end": _base.Binding(
            path="PACK/14:OnEnd",
            kind="sequence",
            name="OnEnd",
        ),
        "on_change": _base.Binding(
            path="PACK/15:OnChange",
            kind="sequence",
            name="OnChange",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure11991] = None
    """Value decoded from this schema node."""

    pack_data: Optional[Structure12046] = None
    """Value decoded from this schema node."""

    schedule: Optional[Structure12055] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition12064, ...] = ()
    """Value decoded from this schema node."""

    idle_animations: Optional[IdleAnimations12222] = None
    """Value decoded from this schema node."""

    combat_style: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    owner_quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    counter: Optional[Structure12241] = None
    """Value decoded from this schema node."""

    package_data: Optional[PackageData12245] = None
    """Value decoded from this schema node."""

    marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    procedure_tree: Optional[ProcedureTree12308] = None
    """Value decoded from this schema node."""

    data_inputs: tuple[DataInput12498, ...] = ()
    """Value decoded from this schema node."""

    on_begin: Optional[OnBegin12505] = None
    """Value decoded from this schema node."""

    on_end: Optional[OnEnd12525] = None
    """Value decoded from this schema node."""

    on_change: Optional[OnChange12545] = None
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
    ) -> _base.FieldRef[Optional[Structure11991]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["pack_data"]
    ) -> _base.FieldRef[Optional[Structure12046]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["schedule"]
    ) -> _base.FieldRef[Optional[Structure12055]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition12064, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["idle_animations"]
    ) -> _base.FieldRef[Optional[IdleAnimations12222]]:
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
        self, name: Literal["owner_quest"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["counter"]
    ) -> _base.FieldRef[Optional[Structure12241]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["package_data"]
    ) -> _base.FieldRef[Optional[PackageData12245]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["marker"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["procedure_tree"]
    ) -> _base.FieldRef[Optional[ProcedureTree12308]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data_inputs"]
    ) -> _base.FieldRef[tuple[DataInput12498, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["on_begin"]
    ) -> _base.FieldRef[Optional[OnBegin12505]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["on_end"]
    ) -> _base.FieldRef[Optional[OnEnd12525]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["on_change"]
    ) -> _base.FieldRef[Optional[OnChange12545]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
