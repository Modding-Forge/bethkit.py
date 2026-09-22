"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags5684(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type5688(_values.OpenIntEnum):
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


class Flags5689(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_5691: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV25693(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_5693: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV15697(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_5697: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_5692: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_5701: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_5702: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_5703: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool5704(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_5704: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV25707(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_5707: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV15711(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_5711: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_5705: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_5715: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_5717: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_5719: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element5722(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_5721: _base.Variant = _base.Variant(
    path=(
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property5686(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type5688
    """Value decoded from this schema node."""

    flags: Flags5689
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_5691]
        | Annotated[
            Annotated[ObjectV25693, _VARIANT_5693]
            | Annotated[ObjectV15697, _VARIANT_5697],
            _VARIANT_5692,
        ]
        | Annotated[str, _VARIANT_5701]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5702,
        ]
        | Annotated[float, _VARIANT_5703]
        | Annotated[Bool5704, _VARIANT_5704]
        | Annotated[
            tuple[
                Annotated[ObjectV25707, _VARIANT_5707]
                | Annotated[ObjectV15711, _VARIANT_5711],
                ...,
            ],
            _VARIANT_5705,
        ]
        | Annotated[tuple[str, ...], _VARIANT_5715]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_5717,
        ]
        | Annotated[tuple[float, ...], _VARIANT_5719]
        | Annotated[tuple[Element5722, ...], _VARIANT_5721]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type5688]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags5689]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_5691]
        | Annotated[
            Annotated[ObjectV25693, _VARIANT_5693]
            | Annotated[ObjectV15697, _VARIANT_5697],
            _VARIANT_5692,
        ]
        | Annotated[str, _VARIANT_5701]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5702,
        ]
        | Annotated[float, _VARIANT_5703]
        | Annotated[Bool5704, _VARIANT_5704]
        | Annotated[
            tuple[
                Annotated[ObjectV25707, _VARIANT_5707]
                | Annotated[ObjectV15711, _VARIANT_5711],
                ...,
            ],
            _VARIANT_5705,
        ]
        | Annotated[tuple[str, ...], _VARIANT_5715]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_5717,
        ]
        | Annotated[tuple[float, ...], _VARIANT_5719]
        | Annotated[tuple[Element5722, ...], _VARIANT_5721]
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


class Script5682(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags5684
    """Value decoded from this schema node."""

    properties: tuple[Property5686, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags5684]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property5686, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Fragment5727(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
        "nts/2:Fragments/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "fragment_index": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:Fragments/element/0:Fragment Index"
            ),
            kind="primitive",
            name="Fragment Index",
        ),
        "unknown": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:Fragments/element/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_5730": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:Fragments/element/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "script_name": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:Fragments/element/3:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "fragment_name": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:Fragments/element/4:FragmentName"
            ),
            kind="primitive",
            name="FragmentName",
        ),
    }

    fragment_index: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unknown: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    unknown_5730: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    script_name: str
    """Value decoded from this schema node."""

    fragment_name: str
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["fragment_index"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_5730"]
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


class ScriptFragments5723(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/1:Virtual Machine Adapter/payload/3:Script Fragments"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "extra_bind_data_version": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/0:Extra bind data version"
            ),
            kind="primitive",
            name="Extra bind data version",
        ),
        "file_name": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/1:FileName"
            ),
            kind="primitive",
            name="FileName",
        ),
        "fragments": _base.Binding(
            path=(
                "PERK/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:Fragments"
            ),
            kind="array",
            name="Fragments",
        ),
    }

    extra_bind_data_version: Annotated[
        int, pydantic.Field(strict=True, ge=-128, le=127)
    ]
    """Value decoded from this schema node."""

    file_name: str
    """Value decoded from this schema node."""

    fragments: tuple[Fragment5727, ...]
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
    def field(self, name: Literal["file_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fragments"]
    ) -> _base.FieldRef[tuple[Fragment5727, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure5678(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PERK/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="PERK/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("PERK/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="PERK/1:Virtual Machine Adapter/payload/2:Scripts",
            kind="array",
            name="Scripts",
        ),
        "script_fragments": _base.Binding(
            path=("PERK/1:Virtual Machine Adapter/payload/3:Script Fragments"),
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

    scripts: tuple[Script5682, ...]
    """Value decoded from this schema node."""

    script_fragments: Optional[ScriptFragments5723] = None
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
    ) -> _base.FieldRef[tuple[Script5682, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_fragments"]
    ) -> _base.FieldRef[Optional[ScriptFragments5723]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Icon5737(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PERK/4:Icon"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "large_icon_file_name": _base.Binding(
            path="PERK/4:Icon/0:Large Icon FileName",
            kind="subrecord",
            name="Large Icon FileName",
        ),
        "small_icon_file_name": _base.Binding(
            path="PERK/4:Icon/1:Small Icon FileName",
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


_VARIANT_5749: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_5750: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_5754: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_5755: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/1:None"
    )
)


_VARIANT_5756: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/2:Integer"
    )
)


_VARIANT_5757: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/3:Float"
    )
)


_VARIANT_5758: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/4:Variable Name"
    )
)


class Sex5759(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_5759: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/5:Sex"
    )
)


class ActorValue5760(_values.OpenIntEnum):
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


_VARIANT_5760: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType5761(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_5761: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/7:Crime Type"
    )
)


class Axis5762(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_5762: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/8:Axis"
    )
)


_VARIANT_5763: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat5764(_values.OpenIntEnum):
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


_VARIANT_5764: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment5765(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_5765: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_5766: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/12:Equip Type"
    )
)


class FormType5767(_values.OpenIntEnum):
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


_VARIANT_5767: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage5768(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_5768: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_5769: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_5770: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_5771: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/17:Actor"
    )
)


_VARIANT_5772: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_5773: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/19:Idle"
    )
)


_VARIANT_5774: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/20:Form List"
    )
)


_VARIANT_5775: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/21:Quest"
    )
)


_VARIANT_5776: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/22:Faction"
    )
)


_VARIANT_5777: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/23:Cell"
    )
)


_VARIANT_5778: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/24:Class"
    )
)


_VARIANT_5779: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/25:Race"
    )
)


_VARIANT_5780: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_5781: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/27:Global"
    )
)


_VARIANT_5782: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/28:Weather"
    )
)


_VARIANT_5783: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/29:Package"
    )
)


_VARIANT_5784: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_5785: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/31:Perk"
    )
)


_VARIANT_5786: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/32:Owner"
    )
)


_VARIANT_5787: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_5788: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_5789: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_5790: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction5791(_values.OpenIntEnum):
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


_VARIANT_5791: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_5792: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_5793: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_5794: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/40:Region"
    )
)


_VARIANT_5795: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction5796(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_5796: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/42:Player Action"
    )
)


class CastingType5797(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_5797: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_5798: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/44:Shout"
    )
)


_VARIANT_5799: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/45:Location"
    )
)


_VARIANT_5800: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_5801: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/47:Alias"
    )
)


_VARIANT_5802: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_5803: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim5804(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_5804: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry5805(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_5805: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_5806: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/52:Scene"
    )
)


class WardState5807(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_5807: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_5808: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/54:Event"
    )
)


_VARIANT_5809: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_5810: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_5811: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/57:Faction"
    )
)


_VARIANT_5813: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_5814: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/1:None"
    )
)


_VARIANT_5815: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/2:Integer"
    )
)


_VARIANT_5816: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/3:Float"
    )
)


_VARIANT_5817: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/4:Variable Name"
    )
)


class Sex5818(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_5818: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/5:Sex"
    )
)


class ActorValue5819(_values.OpenIntEnum):
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


_VARIANT_5819: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType5820(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_5820: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/7:Crime Type"
    )
)


class Axis5821(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_5821: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/8:Axis"
    )
)


_VARIANT_5822: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat5823(_values.OpenIntEnum):
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


_VARIANT_5823: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment5824(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_5824: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_5825: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/12:Equip Type"
    )
)


class FormType5826(_values.OpenIntEnum):
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


_VARIANT_5826: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage5827(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_5827: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_5828: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_5829: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_5830: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/17:Actor"
    )
)


_VARIANT_5831: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_5832: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/19:Idle"
    )
)


_VARIANT_5833: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/20:Form List"
    )
)


_VARIANT_5834: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/21:Quest"
    )
)


_VARIANT_5835: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/22:Faction"
    )
)


_VARIANT_5836: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/23:Cell"
    )
)


_VARIANT_5837: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/24:Class"
    )
)


_VARIANT_5838: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/25:Race"
    )
)


_VARIANT_5839: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_5840: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/27:Global"
    )
)


_VARIANT_5841: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/28:Weather"
    )
)


_VARIANT_5842: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/29:Package"
    )
)


_VARIANT_5843: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_5844: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/31:Perk"
    )
)


_VARIANT_5845: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/32:Owner"
    )
)


_VARIANT_5846: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_5847: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_5848: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_5849: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction5850(_values.OpenIntEnum):
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


_VARIANT_5850: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_5852: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/0:W"
        "eapon"
    )
)


_VARIANT_5853: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/1:W"
        "eapon List"
    )
)


_VARIANT_5854: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/2:T"
        "arget"
    )
)


_VARIANT_5855: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/3:T"
        "arget List"
    )
)


_VARIANT_5856: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/4:U"
        "nknown"
    )
)


class TargetPart5857(_values.OpenIntEnum):
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


_VARIANT_5857: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/5:T"
        "arget Part"
    )
)


class VatsAction5858(_values.OpenIntEnum):
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


_VARIANT_5858: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/6:V"
        "ATS Action"
    )
)


_VARIANT_5859: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/7:U"
        "nknown"
    )
)


_VARIANT_5860: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/8:U"
        "nknown"
    )
)


_VARIANT_5861: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/9:C"
        "ritical Effect"
    )
)


_VARIANT_5862: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/10:"
        "Critical Effect List"
    )
)


_VARIANT_5863: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/11:"
        "Unknown"
    )
)


_VARIANT_5864: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/12:"
        "Unknown"
    )
)


_VARIANT_5865: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/13:"
        "Unknown"
    )
)


_VARIANT_5866: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/14:"
        "Unknown"
    )
)


class WeaponType5867(_values.OpenIntEnum):
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


_VARIANT_5867: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/15:"
        "Weapon Type"
    )
)


_VARIANT_5868: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/16:"
        "Unknown"
    )
)


_VARIANT_5869: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/17:"
        "Unknown"
    )
)


class ProjectileType5870(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_5870: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/18:"
        "Projectile Type"
    )
)


class DeliveryType5871(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_5871: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/19:"
        "Delivery Type"
    )
)


class CastingType5872(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_5872: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/20:"
        "Casting Type"
    )
)


_VARIANT_5851: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_5873: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_5874: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/40:Region"
    )
)


_VARIANT_5875: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction5876(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_5876: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/42:Player Action"
    )
)


class CastingType5877(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_5877: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_5878: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/44:Shout"
    )
)


_VARIANT_5879: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/45:Location"
    )
)


_VARIANT_5880: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_5881: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/47:Alias"
    )
)


_VARIANT_5882: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_5883: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim5884(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_5884: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry5885(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_5885: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_5886: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/52:Scene"
    )
)


class WardState5887(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_5887: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_5888: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/54:Event"
    )
)


_VARIANT_5889: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_5890: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_5891: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/57:Faction"
    )
)


class RunOn5892(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_5894: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/0:Unused"
    )
)


_VARIANT_5895: _base.Variant = _base.Variant(
    path=(
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/1:Reference"
    )
)


class Structure5745(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
                "Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_5752": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
                "Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
                "Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
                "Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "PERK/5:Conditions/repeat/0:Condition/0:CTDA/payload/9:"
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
        Annotated[float, _VARIANT_5749]
        | Annotated[_values.FormId, _VARIANT_5750]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_5752: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_5754]
        | Annotated[bytes, _VARIANT_5755]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5756,
        ]
        | Annotated[float, _VARIANT_5757]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5758,
        ]
        | Annotated[Sex5759, _VARIANT_5759]
        | Annotated[ActorValue5760, _VARIANT_5760]
        | Annotated[CrimeType5761, _VARIANT_5761]
        | Annotated[Axis5762, _VARIANT_5762]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5763,
        ]
        | Annotated[MiscStat5764, _VARIANT_5764]
        | Annotated[Alignment5765, _VARIANT_5765]
        | Annotated[_values.FormId, _VARIANT_5766]
        | Annotated[FormType5767, _VARIANT_5767]
        | Annotated[CriticalStage5768, _VARIANT_5768]
        | Annotated[_values.FormId, _VARIANT_5769]
        | Annotated[_values.FormId, _VARIANT_5770]
        | Annotated[_values.FormId, _VARIANT_5771]
        | Annotated[_values.FormId, _VARIANT_5772]
        | Annotated[_values.FormId, _VARIANT_5773]
        | Annotated[_values.FormId, _VARIANT_5774]
        | Annotated[_values.FormId, _VARIANT_5775]
        | Annotated[_values.FormId, _VARIANT_5776]
        | Annotated[_values.FormId, _VARIANT_5777]
        | Annotated[_values.FormId, _VARIANT_5778]
        | Annotated[_values.FormId, _VARIANT_5779]
        | Annotated[_values.FormId, _VARIANT_5780]
        | Annotated[_values.FormId, _VARIANT_5781]
        | Annotated[_values.FormId, _VARIANT_5782]
        | Annotated[_values.FormId, _VARIANT_5783]
        | Annotated[_values.FormId, _VARIANT_5784]
        | Annotated[_values.FormId, _VARIANT_5785]
        | Annotated[_values.FormId, _VARIANT_5786]
        | Annotated[_values.FormId, _VARIANT_5787]
        | Annotated[_values.FormId, _VARIANT_5788]
        | Annotated[_values.FormId, _VARIANT_5789]
        | Annotated[_values.FormId, _VARIANT_5790]
        | Annotated[VatsValueFunction5791, _VARIANT_5791]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5792,
        ]
        | Annotated[_values.FormId, _VARIANT_5793]
        | Annotated[_values.FormId, _VARIANT_5794]
        | Annotated[_values.FormId, _VARIANT_5795]
        | Annotated[PlayerAction5796, _VARIANT_5796]
        | Annotated[CastingType5797, _VARIANT_5797]
        | Annotated[_values.FormId, _VARIANT_5798]
        | Annotated[_values.FormId, _VARIANT_5799]
        | Annotated[_values.FormId, _VARIANT_5800]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5801,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5802,
        ]
        | Annotated[_values.FormId, _VARIANT_5803]
        | Annotated[FurnitureAnim5804, _VARIANT_5804]
        | Annotated[FurnitureEntry5805, _VARIANT_5805]
        | Annotated[_values.FormId, _VARIANT_5806]
        | Annotated[WardState5807, _VARIANT_5807]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5808,
        ]
        | Annotated[_values.FormId, _VARIANT_5809]
        | Annotated[_values.FormId, _VARIANT_5810]
        | Annotated[_values.FormId, _VARIANT_5811]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_5813]
        | Annotated[bytes, _VARIANT_5814]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5815,
        ]
        | Annotated[float, _VARIANT_5816]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5817,
        ]
        | Annotated[Sex5818, _VARIANT_5818]
        | Annotated[ActorValue5819, _VARIANT_5819]
        | Annotated[CrimeType5820, _VARIANT_5820]
        | Annotated[Axis5821, _VARIANT_5821]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5822,
        ]
        | Annotated[MiscStat5823, _VARIANT_5823]
        | Annotated[Alignment5824, _VARIANT_5824]
        | Annotated[_values.FormId, _VARIANT_5825]
        | Annotated[FormType5826, _VARIANT_5826]
        | Annotated[CriticalStage5827, _VARIANT_5827]
        | Annotated[_values.FormId, _VARIANT_5828]
        | Annotated[_values.FormId, _VARIANT_5829]
        | Annotated[_values.FormId, _VARIANT_5830]
        | Annotated[_values.FormId, _VARIANT_5831]
        | Annotated[_values.FormId, _VARIANT_5832]
        | Annotated[_values.FormId, _VARIANT_5833]
        | Annotated[_values.FormId, _VARIANT_5834]
        | Annotated[_values.FormId, _VARIANT_5835]
        | Annotated[_values.FormId, _VARIANT_5836]
        | Annotated[_values.FormId, _VARIANT_5837]
        | Annotated[_values.FormId, _VARIANT_5838]
        | Annotated[_values.FormId, _VARIANT_5839]
        | Annotated[_values.FormId, _VARIANT_5840]
        | Annotated[_values.FormId, _VARIANT_5841]
        | Annotated[_values.FormId, _VARIANT_5842]
        | Annotated[_values.FormId, _VARIANT_5843]
        | Annotated[_values.FormId, _VARIANT_5844]
        | Annotated[_values.FormId, _VARIANT_5845]
        | Annotated[_values.FormId, _VARIANT_5846]
        | Annotated[_values.FormId, _VARIANT_5847]
        | Annotated[_values.FormId, _VARIANT_5848]
        | Annotated[_values.FormId, _VARIANT_5849]
        | Annotated[VatsValueFunction5850, _VARIANT_5850]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_5852]
            | Annotated[_values.FormId, _VARIANT_5853]
            | Annotated[_values.FormId, _VARIANT_5854]
            | Annotated[_values.FormId, _VARIANT_5855]
            | Annotated[bytes, _VARIANT_5856]
            | Annotated[TargetPart5857, _VARIANT_5857]
            | Annotated[VatsAction5858, _VARIANT_5858]
            | Annotated[bytes, _VARIANT_5859]
            | Annotated[bytes, _VARIANT_5860]
            | Annotated[_values.FormId, _VARIANT_5861]
            | Annotated[_values.FormId, _VARIANT_5862]
            | Annotated[bytes, _VARIANT_5863]
            | Annotated[bytes, _VARIANT_5864]
            | Annotated[bytes, _VARIANT_5865]
            | Annotated[bytes, _VARIANT_5866]
            | Annotated[WeaponType5867, _VARIANT_5867]
            | Annotated[bytes, _VARIANT_5868]
            | Annotated[bytes, _VARIANT_5869]
            | Annotated[ProjectileType5870, _VARIANT_5870]
            | Annotated[DeliveryType5871, _VARIANT_5871]
            | Annotated[CastingType5872, _VARIANT_5872],
            _VARIANT_5851,
        ]
        | Annotated[_values.FormId, _VARIANT_5873]
        | Annotated[_values.FormId, _VARIANT_5874]
        | Annotated[_values.FormId, _VARIANT_5875]
        | Annotated[PlayerAction5876, _VARIANT_5876]
        | Annotated[CastingType5877, _VARIANT_5877]
        | Annotated[_values.FormId, _VARIANT_5878]
        | Annotated[_values.FormId, _VARIANT_5879]
        | Annotated[_values.FormId, _VARIANT_5880]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5881,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5882,
        ]
        | Annotated[_values.FormId, _VARIANT_5883]
        | Annotated[FurnitureAnim5884, _VARIANT_5884]
        | Annotated[FurnitureEntry5885, _VARIANT_5885]
        | Annotated[_values.FormId, _VARIANT_5886]
        | Annotated[WardState5887, _VARIANT_5887]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5888,
        ]
        | Annotated[_values.FormId, _VARIANT_5889]
        | Annotated[_values.FormId, _VARIANT_5890]
        | Annotated[_values.FormId, _VARIANT_5891]
    )
    """Value decoded from this schema node."""

    run_on: RunOn5892
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5894,
        ]
        | Annotated[_values.FormId, _VARIANT_5895]
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
        Annotated[float, _VARIANT_5749]
        | Annotated[_values.FormId, _VARIANT_5750]
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
    def field(self, name: Literal["unused_5752"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_5754]
        | Annotated[bytes, _VARIANT_5755]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5756,
        ]
        | Annotated[float, _VARIANT_5757]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5758,
        ]
        | Annotated[Sex5759, _VARIANT_5759]
        | Annotated[ActorValue5760, _VARIANT_5760]
        | Annotated[CrimeType5761, _VARIANT_5761]
        | Annotated[Axis5762, _VARIANT_5762]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5763,
        ]
        | Annotated[MiscStat5764, _VARIANT_5764]
        | Annotated[Alignment5765, _VARIANT_5765]
        | Annotated[_values.FormId, _VARIANT_5766]
        | Annotated[FormType5767, _VARIANT_5767]
        | Annotated[CriticalStage5768, _VARIANT_5768]
        | Annotated[_values.FormId, _VARIANT_5769]
        | Annotated[_values.FormId, _VARIANT_5770]
        | Annotated[_values.FormId, _VARIANT_5771]
        | Annotated[_values.FormId, _VARIANT_5772]
        | Annotated[_values.FormId, _VARIANT_5773]
        | Annotated[_values.FormId, _VARIANT_5774]
        | Annotated[_values.FormId, _VARIANT_5775]
        | Annotated[_values.FormId, _VARIANT_5776]
        | Annotated[_values.FormId, _VARIANT_5777]
        | Annotated[_values.FormId, _VARIANT_5778]
        | Annotated[_values.FormId, _VARIANT_5779]
        | Annotated[_values.FormId, _VARIANT_5780]
        | Annotated[_values.FormId, _VARIANT_5781]
        | Annotated[_values.FormId, _VARIANT_5782]
        | Annotated[_values.FormId, _VARIANT_5783]
        | Annotated[_values.FormId, _VARIANT_5784]
        | Annotated[_values.FormId, _VARIANT_5785]
        | Annotated[_values.FormId, _VARIANT_5786]
        | Annotated[_values.FormId, _VARIANT_5787]
        | Annotated[_values.FormId, _VARIANT_5788]
        | Annotated[_values.FormId, _VARIANT_5789]
        | Annotated[_values.FormId, _VARIANT_5790]
        | Annotated[VatsValueFunction5791, _VARIANT_5791]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5792,
        ]
        | Annotated[_values.FormId, _VARIANT_5793]
        | Annotated[_values.FormId, _VARIANT_5794]
        | Annotated[_values.FormId, _VARIANT_5795]
        | Annotated[PlayerAction5796, _VARIANT_5796]
        | Annotated[CastingType5797, _VARIANT_5797]
        | Annotated[_values.FormId, _VARIANT_5798]
        | Annotated[_values.FormId, _VARIANT_5799]
        | Annotated[_values.FormId, _VARIANT_5800]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5801,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5802,
        ]
        | Annotated[_values.FormId, _VARIANT_5803]
        | Annotated[FurnitureAnim5804, _VARIANT_5804]
        | Annotated[FurnitureEntry5805, _VARIANT_5805]
        | Annotated[_values.FormId, _VARIANT_5806]
        | Annotated[WardState5807, _VARIANT_5807]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5808,
        ]
        | Annotated[_values.FormId, _VARIANT_5809]
        | Annotated[_values.FormId, _VARIANT_5810]
        | Annotated[_values.FormId, _VARIANT_5811]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_5813]
        | Annotated[bytes, _VARIANT_5814]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5815,
        ]
        | Annotated[float, _VARIANT_5816]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5817,
        ]
        | Annotated[Sex5818, _VARIANT_5818]
        | Annotated[ActorValue5819, _VARIANT_5819]
        | Annotated[CrimeType5820, _VARIANT_5820]
        | Annotated[Axis5821, _VARIANT_5821]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5822,
        ]
        | Annotated[MiscStat5823, _VARIANT_5823]
        | Annotated[Alignment5824, _VARIANT_5824]
        | Annotated[_values.FormId, _VARIANT_5825]
        | Annotated[FormType5826, _VARIANT_5826]
        | Annotated[CriticalStage5827, _VARIANT_5827]
        | Annotated[_values.FormId, _VARIANT_5828]
        | Annotated[_values.FormId, _VARIANT_5829]
        | Annotated[_values.FormId, _VARIANT_5830]
        | Annotated[_values.FormId, _VARIANT_5831]
        | Annotated[_values.FormId, _VARIANT_5832]
        | Annotated[_values.FormId, _VARIANT_5833]
        | Annotated[_values.FormId, _VARIANT_5834]
        | Annotated[_values.FormId, _VARIANT_5835]
        | Annotated[_values.FormId, _VARIANT_5836]
        | Annotated[_values.FormId, _VARIANT_5837]
        | Annotated[_values.FormId, _VARIANT_5838]
        | Annotated[_values.FormId, _VARIANT_5839]
        | Annotated[_values.FormId, _VARIANT_5840]
        | Annotated[_values.FormId, _VARIANT_5841]
        | Annotated[_values.FormId, _VARIANT_5842]
        | Annotated[_values.FormId, _VARIANT_5843]
        | Annotated[_values.FormId, _VARIANT_5844]
        | Annotated[_values.FormId, _VARIANT_5845]
        | Annotated[_values.FormId, _VARIANT_5846]
        | Annotated[_values.FormId, _VARIANT_5847]
        | Annotated[_values.FormId, _VARIANT_5848]
        | Annotated[_values.FormId, _VARIANT_5849]
        | Annotated[VatsValueFunction5850, _VARIANT_5850]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_5852]
            | Annotated[_values.FormId, _VARIANT_5853]
            | Annotated[_values.FormId, _VARIANT_5854]
            | Annotated[_values.FormId, _VARIANT_5855]
            | Annotated[bytes, _VARIANT_5856]
            | Annotated[TargetPart5857, _VARIANT_5857]
            | Annotated[VatsAction5858, _VARIANT_5858]
            | Annotated[bytes, _VARIANT_5859]
            | Annotated[bytes, _VARIANT_5860]
            | Annotated[_values.FormId, _VARIANT_5861]
            | Annotated[_values.FormId, _VARIANT_5862]
            | Annotated[bytes, _VARIANT_5863]
            | Annotated[bytes, _VARIANT_5864]
            | Annotated[bytes, _VARIANT_5865]
            | Annotated[bytes, _VARIANT_5866]
            | Annotated[WeaponType5867, _VARIANT_5867]
            | Annotated[bytes, _VARIANT_5868]
            | Annotated[bytes, _VARIANT_5869]
            | Annotated[ProjectileType5870, _VARIANT_5870]
            | Annotated[DeliveryType5871, _VARIANT_5871]
            | Annotated[CastingType5872, _VARIANT_5872],
            _VARIANT_5851,
        ]
        | Annotated[_values.FormId, _VARIANT_5873]
        | Annotated[_values.FormId, _VARIANT_5874]
        | Annotated[_values.FormId, _VARIANT_5875]
        | Annotated[PlayerAction5876, _VARIANT_5876]
        | Annotated[CastingType5877, _VARIANT_5877]
        | Annotated[_values.FormId, _VARIANT_5878]
        | Annotated[_values.FormId, _VARIANT_5879]
        | Annotated[_values.FormId, _VARIANT_5880]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5881,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5882,
        ]
        | Annotated[_values.FormId, _VARIANT_5883]
        | Annotated[FurnitureAnim5884, _VARIANT_5884]
        | Annotated[FurnitureEntry5885, _VARIANT_5885]
        | Annotated[_values.FormId, _VARIANT_5886]
        | Annotated[WardState5887, _VARIANT_5887]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5888,
        ]
        | Annotated[_values.FormId, _VARIANT_5889]
        | Annotated[_values.FormId, _VARIANT_5890]
        | Annotated[_values.FormId, _VARIANT_5891]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn5892]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5894,
        ]
        | Annotated[_values.FormId, _VARIANT_5895]
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


class Condition5743(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PERK/5:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="PERK/5:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("PERK/5:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("PERK/5:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure5745] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure5745]]:
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


class Trait5903(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Playable5906(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Hidden5907(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class Structure5902(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PERK/6:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "trait": _base.Binding(
            path="PERK/6:Data/payload/0:Trait",
            kind="primitive",
            name="Trait",
        ),
        "level": _base.Binding(
            path="PERK/6:Data/payload/1:Level",
            kind="primitive",
            name="Level",
        ),
        "num_ranks": _base.Binding(
            path="PERK/6:Data/payload/2:Num Ranks",
            kind="primitive",
            name="Num Ranks",
        ),
        "playable": _base.Binding(
            path="PERK/6:Data/payload/3:Playable",
            kind="primitive",
            name="Playable",
        ),
        "hidden": _base.Binding(
            path="PERK/6:Data/payload/4:Hidden",
            kind="primitive",
            name="Hidden",
        ),
    }

    trait: Trait5903
    """Value decoded from this schema node."""

    level: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    num_ranks: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    playable: Playable5906
    """Value decoded from this schema node."""

    hidden: Hidden5907
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["trait"]) -> _base.FieldRef[Trait5903]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["level"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["num_ranks"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["playable"]) -> _base.FieldRef[Playable5906]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["hidden"]) -> _base.FieldRef[Hidden5907]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Type5914(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    QUEST_STAGE = 0
    ABILITY = 1
    ENTRY_POINT = 2


class Structure5913(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/0:Header/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("PERK/8:Effects/repeat/0:Effect/0:Header/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "rank": _base.Binding(
            path=("PERK/8:Effects/repeat/0:Effect/0:Header/payload/1:Rank"),
            kind="primitive",
            name="Rank",
        ),
        "priority": _base.Binding(
            path=("PERK/8:Effects/repeat/0:Effect/0:Header/payload/2:Priority"),
            kind="primitive",
            name="Priority",
        ),
    }

    type: Type5914
    """Value decoded from this schema node."""

    rank: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    priority: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type5914]:
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
    def field(
        self, name: Literal["priority"]
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


class QuestStage5919(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
        "ariants/0:Quest + Stage"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "quest": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
                "ariants/0:Quest + Stage/0:Quest"
            ),
            kind="primitive",
            name="Quest",
        ),
        "quest_stage": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
                "ariants/0:Quest + Stage/1:Quest Stage"
            ),
            kind="primitive",
            name="Quest Stage",
        ),
        "unused": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
                "ariants/0:Quest + Stage/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    quest: _values.FormId
    """Value decoded from this schema node."""

    quest_stage: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["quest"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["quest_stage"]
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


_VARIANT_5919: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
        "ariants/0:Quest + Stage"
    )
)


_VARIANT_5923: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
        "ariants/1:Ability"
    )
)


class EntryPoint5925(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CALCULATE_WEAPON_DAMAGE = 0
    CALCULATE_MY_CRITICAL_HIT_CHANCE = 1
    CALCULATE_MY_CRITICAL_HIT_DAMAGE = 2
    CALCULATE_MINE_EXPLODE_CHANCE = 3
    ADJUST_LIMB_DAMAGE = 4
    ADJUST_BOOK_SKILL_POINTS = 5
    MOD_RECOVERED_HEALTH = 6
    GET_SHOULD_ATTACK = 7
    MOD_BUY_PRICES = 8
    ADD_LEVELED_LIST_ON_DEATH = 9
    GET_MAX_CARRY_WEIGHT = 10
    MOD_ADDICTION_CHANCE = 11
    MOD_ADDICTION_DURATION = 12
    MOD_POSITIVE_CHEM_DURATION = 13
    ACTIVATE = 14
    IGNORE_RUNNING_DURING_DETECTION = 15
    IGNORE_BROKEN_LOCK = 16
    MOD_ENEMY_CRITICAL_HIT_CHANCE = 17
    MOD_SNEAK_ATTACK_MULT = 18
    MOD_MAX_PLACEABLE_MINES = 19
    MOD_BOW_ZOOM = 20
    MOD_RECOVER_ARROW_CHANCE = 21
    MOD_SKILL_USE = 22
    MOD_TELEKINESIS_DISTANCE = 23
    MOD_TELEKINESIS_DAMAGE_MULT = 24
    MOD_TELEKINESIS_DAMAGE = 25
    MOD_BASHING_DAMAGE = 26
    MOD_POWER_ATTACK_STAMINA = 27
    MOD_POWER_ATTACK_DAMAGE = 28
    MOD_SPELL_MAGNITUDE = 29
    MOD_SPELL_DURATION = 30
    MOD_SECONDARY_VALUE_WEIGHT = 31
    MOD_ARMOR_WEIGHT = 32
    MOD_INCOMING_STAGGER = 33
    MOD_TARGET_STAGGER = 34
    MOD_ATTACK_DAMAGE = 35
    MOD_INCOMING_DAMAGE = 36
    MOD_TARGET_DAMAGE_RESISTANCE = 37
    MOD_SPELL_COST = 38
    MOD_PERCENT_BLOCKED = 39
    MOD_SHIELD_DEFLECT_ARROW_CHANCE = 40
    MOD_INCOMING_SPELL_MAGNITUDE = 41
    MOD_INCOMING_SPELL_DURATION = 42
    MOD_PLAYER_INTIMIDATION = 43
    MOD_PLAYER_REPUTATION = 44
    MOD_FAVOR_POINTS = 45
    MOD_BRIBE_AMOUNT = 46
    MOD_DETECTION_LIGHT = 47
    MOD_DETECTION_MOVEMENT = 48
    MOD_SOUL_GEM_RECHARGE = 49
    SET_SWEEP_ATTACK = 50
    APPLY_COMBAT_HIT_SPELL = 51
    APPLY_BASHING_SPELL = 52
    APPLY_REANIMATE_SPELL = 53
    SET_BOOLEAN_GRAPH_VARIABLE = 54
    MOD_SPELL_CASTING_SOUND_EVENT = 55
    MOD_PICKPOCKET_CHANCE = 56
    MOD_DETECTION_SNEAK_SKILL = 57
    MOD_FALLING_DAMAGE = 58
    MOD_LOCKPICK_SWEET_SPOT = 59
    MOD_SELL_PRICES = 60
    CAN_PICKPOCKET_EQUIPPED_ITEM = 61
    MOD_LOCKPICK_LEVEL_ALLOWED = 62
    SET_LOCKPICK_STARTING_ARC = 63
    SET_PROGRESSION_PICKING = 64
    MAKE_LOCKPICKS_UNBREAKABLE = 65
    MOD_ALCHEMY_EFFECTIVENESS = 66
    APPLY_WEAPON_SWING_SPELL = 67
    MOD_COMMANDED_ACTOR_LIMIT = 68
    APPLY_SNEAKING_SPELL = 69
    MOD_PLAYER_MAGIC_SLOWDOWN = 70
    MOD_WARD_MAGICKA_ABSORPTION_PCT = 71
    MOD_INITIAL_INGREDIENT_EFFECTS_LEARNED = 72
    PURIFY_ALCHEMY_INGREDIENTS = 73
    FILTER_ACTIVATION = 74
    CAN_DUAL_CAST_SPELL = 75
    MOD_TEMPERING_HEALTH = 76
    MOD_ENCHANTMENT_POWER = 77
    MOD_SOUL_PCT_CAPTURED_TO_WEAPON = 78
    MOD_SOUL_GEM_ENCHANTING = 79
    MOD_APPLIED_ENCHANTMENTS_ALLOWED = 80
    SET_ACTIVATE_LABEL = 81
    MOD_SHOUT_OK = 82
    MOD_POISON_DOSE_COUNT = 83
    SHOULD_APPLY_PLACED_ITEM = 84
    MOD_ARMOR_RATING = 85
    MOD_LOCKPICKING_CRIME_CHANCE = 86
    MOD_INGREDIENTS_HARVESTED = 87
    MOD_SPELL_RANGE_TARGET_LOC = 88
    MOD_POTIONS_CREATED = 89
    MOD_LOCKPICKING_KEY_REWARD_CHANCE = 90
    ALLOW_MOUNT_ACTOR = 91


class Function5926(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    UNKNOWN_0 = 0
    SET_VALUE = 1
    ADD_VALUE = 2
    MULTIPLY_VALUE = 3
    ADD_RANGE_TO_VALUE = 4
    ADD_ACTOR_VALUE_MULT = 5
    ABSOLUTE_VALUE = 6
    NEGATIVE_ABSOLUTE_VALUE = 7
    ADD_LEVELED_LIST = 8
    ADD_ACTIVATE_CHOICE = 9
    SELECT_SPELL = 10
    SELECT_TEXT = 11
    SET_TO_ACTOR_VALUE_MULT = 12
    MULTIPLY_ACTOR_VALUE_MULT = 13
    MULTIPLY_1_ACTOR_VALUE_MULT = 14
    SET_TEXT = 15


class EntryPoint5924(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
        "ariants/2:Entry Point"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "entry_point": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
                "ariants/2:Entry Point/0:Entry Point"
            ),
            kind="primitive",
            name="Entry Point",
        ),
        "function": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
                "ariants/2:Entry Point/1:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "perk_condition_tab_count": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
                "ariants/2:Entry Point/2:Perk Condition Tab Count"
            ),
            kind="primitive",
            name="Perk Condition Tab Count",
        ),
    }

    entry_point: EntryPoint5925
    """Value decoded from this schema node."""

    function: Function5926
    """Value decoded from this schema node."""

    perk_condition_tab_count: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["entry_point"]
    ) -> _base.FieldRef[EntryPoint5925]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["function"]) -> _base.FieldRef[Function5926]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perk_condition_tab_count"]
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


_VARIANT_5924: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/1:Effect Data/payload/v"
        "ariants/2:Entry Point"
    )
)


_VARIANT_5939: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/2:Comparison Value/variants/0:Comparison V"
        "alue - Float"
    )
)


_VARIANT_5940: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/2:Comparison Value/variants/1:Comparison V"
        "alue - Global"
    )
)


_VARIANT_5944: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_5945: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/1:None"
    )
)


_VARIANT_5946: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/2:Integer"
    )
)


_VARIANT_5947: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/3:Float"
    )
)


_VARIANT_5948: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/4:Variable Name"
    )
)


class Sex5949(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_5949: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/5:Sex"
    )
)


class ActorValue5950(_values.OpenIntEnum):
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


_VARIANT_5950: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType5951(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_5951: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/7:Crime Type"
    )
)


class Axis5952(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_5952: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/8:Axis"
    )
)


_VARIANT_5953: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/9:Quest Stage (unu"
        "sed)"
    )
)


class MiscStat5954(_values.OpenIntEnum):
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


_VARIANT_5954: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment5955(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_5955: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_5956: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/12:Equip Type"
    )
)


class FormType5957(_values.OpenIntEnum):
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


_VARIANT_5957: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage5958(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_5958: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_5959: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/15:Object Referenc"
        "e"
    )
)


_VARIANT_5960: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/16:Inventory Objec"
        "t"
    )
)


_VARIANT_5961: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/17:Actor"
    )
)


_VARIANT_5962: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_5963: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/19:Idle"
    )
)


_VARIANT_5964: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/20:Form List"
    )
)


_VARIANT_5965: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/21:Quest"
    )
)


_VARIANT_5966: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/22:Faction"
    )
)


_VARIANT_5967: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/23:Cell"
    )
)


_VARIANT_5968: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/24:Class"
    )
)


_VARIANT_5969: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/25:Race"
    )
)


_VARIANT_5970: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_5971: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/27:Global"
    )
)


_VARIANT_5972: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/28:Weather"
    )
)


_VARIANT_5973: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/29:Package"
    )
)


_VARIANT_5974: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_5975: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/31:Perk"
    )
)


_VARIANT_5976: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/32:Owner"
    )
)


_VARIANT_5977: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_5978: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_5979: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_5980: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction5981(_values.OpenIntEnum):
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


_VARIANT_5981: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/37:VATS Value Func"
        "tion"
    )
)


_VARIANT_5982: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/38:VATS Value Para"
        "m (INVALID)"
    )
)


_VARIANT_5983: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/39:Referenceable O"
        "bject"
    )
)


_VARIANT_5984: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/40:Region"
    )
)


_VARIANT_5985: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction5986(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_5986: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/42:Player Action"
    )
)


class CastingType5987(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_5987: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_5988: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/44:Shout"
    )
)


_VARIANT_5989: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/45:Location"
    )
)


_VARIANT_5990: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/46:Location Ref Ty"
        "pe"
    )
)


_VARIANT_5991: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/47:Alias"
    )
)


_VARIANT_5992: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_5993: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/49:Association Typ"
        "e"
    )
)


class FurnitureAnim5994(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_5994: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry5995(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_5995: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_5996: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/52:Scene"
    )
)


class WardState5997(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_5997: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_5998: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/54:Event"
    )
)


_VARIANT_5999: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_6000: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_6001: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/5:Parameter #1/variants/57:Faction"
    )
)


_VARIANT_6003: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_6004: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/1:None"
    )
)


_VARIANT_6005: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/2:Integer"
    )
)


_VARIANT_6006: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/3:Float"
    )
)


_VARIANT_6007: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/4:Variable Name"
    )
)


class Sex6008(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_6008: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/5:Sex"
    )
)


class ActorValue6009(_values.OpenIntEnum):
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


_VARIANT_6009: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType6010(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_6010: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/7:Crime Type"
    )
)


class Axis6011(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_6011: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/8:Axis"
    )
)


_VARIANT_6012: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat6013(_values.OpenIntEnum):
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


_VARIANT_6013: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment6014(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_6014: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_6015: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/12:Equip Type"
    )
)


class FormType6016(_values.OpenIntEnum):
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


_VARIANT_6016: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage6017(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_6017: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_6018: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/15:Object Referenc"
        "e"
    )
)


_VARIANT_6019: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/16:Inventory Objec"
        "t"
    )
)


_VARIANT_6020: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/17:Actor"
    )
)


_VARIANT_6021: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_6022: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/19:Idle"
    )
)


_VARIANT_6023: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/20:Form List"
    )
)


_VARIANT_6024: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/21:Quest"
    )
)


_VARIANT_6025: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/22:Faction"
    )
)


_VARIANT_6026: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/23:Cell"
    )
)


_VARIANT_6027: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/24:Class"
    )
)


_VARIANT_6028: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/25:Race"
    )
)


_VARIANT_6029: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_6030: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/27:Global"
    )
)


_VARIANT_6031: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/28:Weather"
    )
)


_VARIANT_6032: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/29:Package"
    )
)


_VARIANT_6033: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_6034: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/31:Perk"
    )
)


_VARIANT_6035: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/32:Owner"
    )
)


_VARIANT_6036: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_6037: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_6038: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_6039: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction6040(_values.OpenIntEnum):
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


_VARIANT_6040: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/37:VATS Value Func"
        "tion"
    )
)


_VARIANT_6042: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/0:Weapon"
    )
)


_VARIANT_6043: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/1:Weapon List"
    )
)


_VARIANT_6044: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/2:Target"
    )
)


_VARIANT_6045: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/3:Target List"
    )
)


_VARIANT_6046: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/4:Unknown"
    )
)


class TargetPart6047(_values.OpenIntEnum):
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


_VARIANT_6047: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/5:Target Part"
    )
)


class VatsAction6048(_values.OpenIntEnum):
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


_VARIANT_6048: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/6:VATS Action"
    )
)


_VARIANT_6049: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/7:Unknown"
    )
)


_VARIANT_6050: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/8:Unknown"
    )
)


_VARIANT_6051: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/9:Critical Effect"
    )
)


_VARIANT_6052: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/10:Critical Effect List"
    )
)


_VARIANT_6053: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/11:Unknown"
    )
)


_VARIANT_6054: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/12:Unknown"
    )
)


_VARIANT_6055: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/13:Unknown"
    )
)


_VARIANT_6056: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/14:Unknown"
    )
)


class WeaponType6057(_values.OpenIntEnum):
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


_VARIANT_6057: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/15:Weapon Type"
    )
)


_VARIANT_6058: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/16:Unknown"
    )
)


_VARIANT_6059: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/17:Unknown"
    )
)


class ProjectileType6060(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_6060: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/18:Projectile Type"
    )
)


class DeliveryType6061(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_6061: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/19:Delivery Type"
    )
)


class CastingType6062(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_6062: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m/variants/20:Casting Type"
    )
)


_VARIANT_6041: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/38:VATS Value Para"
        "m"
    )
)


_VARIANT_6063: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/39:Referenceable O"
        "bject"
    )
)


_VARIANT_6064: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/40:Region"
    )
)


_VARIANT_6065: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction6066(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_6066: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/42:Player Action"
    )
)


class CastingType6067(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_6067: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_6068: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/44:Shout"
    )
)


_VARIANT_6069: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/45:Location"
    )
)


_VARIANT_6070: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/46:Location Ref Ty"
        "pe"
    )
)


_VARIANT_6071: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/47:Alias"
    )
)


_VARIANT_6072: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_6073: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/49:Association Typ"
        "e"
    )
)


class FurnitureAnim6074(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_6074: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry6075(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_6075: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_6076: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/52:Scene"
    )
)


class WardState6077(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_6077: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_6078: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/54:Event"
    )
)


_VARIANT_6079: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_6080: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_6081: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/6:Parameter #2/variants/57:Faction"
    )
)


class RunOn6082(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_6084: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/8:Reference/variants/0:Unused"
    )
)


_VARIANT_6085: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload/8:Reference/variants/1:Reference"
    )
)


class Structure5935(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
        "TDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_5942": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA/payload/9:Parameter #3"
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
        Annotated[float, _VARIANT_5939]
        | Annotated[_values.FormId, _VARIANT_5940]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_5942: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_5944]
        | Annotated[bytes, _VARIANT_5945]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5946,
        ]
        | Annotated[float, _VARIANT_5947]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5948,
        ]
        | Annotated[Sex5949, _VARIANT_5949]
        | Annotated[ActorValue5950, _VARIANT_5950]
        | Annotated[CrimeType5951, _VARIANT_5951]
        | Annotated[Axis5952, _VARIANT_5952]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5953,
        ]
        | Annotated[MiscStat5954, _VARIANT_5954]
        | Annotated[Alignment5955, _VARIANT_5955]
        | Annotated[_values.FormId, _VARIANT_5956]
        | Annotated[FormType5957, _VARIANT_5957]
        | Annotated[CriticalStage5958, _VARIANT_5958]
        | Annotated[_values.FormId, _VARIANT_5959]
        | Annotated[_values.FormId, _VARIANT_5960]
        | Annotated[_values.FormId, _VARIANT_5961]
        | Annotated[_values.FormId, _VARIANT_5962]
        | Annotated[_values.FormId, _VARIANT_5963]
        | Annotated[_values.FormId, _VARIANT_5964]
        | Annotated[_values.FormId, _VARIANT_5965]
        | Annotated[_values.FormId, _VARIANT_5966]
        | Annotated[_values.FormId, _VARIANT_5967]
        | Annotated[_values.FormId, _VARIANT_5968]
        | Annotated[_values.FormId, _VARIANT_5969]
        | Annotated[_values.FormId, _VARIANT_5970]
        | Annotated[_values.FormId, _VARIANT_5971]
        | Annotated[_values.FormId, _VARIANT_5972]
        | Annotated[_values.FormId, _VARIANT_5973]
        | Annotated[_values.FormId, _VARIANT_5974]
        | Annotated[_values.FormId, _VARIANT_5975]
        | Annotated[_values.FormId, _VARIANT_5976]
        | Annotated[_values.FormId, _VARIANT_5977]
        | Annotated[_values.FormId, _VARIANT_5978]
        | Annotated[_values.FormId, _VARIANT_5979]
        | Annotated[_values.FormId, _VARIANT_5980]
        | Annotated[VatsValueFunction5981, _VARIANT_5981]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5982,
        ]
        | Annotated[_values.FormId, _VARIANT_5983]
        | Annotated[_values.FormId, _VARIANT_5984]
        | Annotated[_values.FormId, _VARIANT_5985]
        | Annotated[PlayerAction5986, _VARIANT_5986]
        | Annotated[CastingType5987, _VARIANT_5987]
        | Annotated[_values.FormId, _VARIANT_5988]
        | Annotated[_values.FormId, _VARIANT_5989]
        | Annotated[_values.FormId, _VARIANT_5990]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5991,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5992,
        ]
        | Annotated[_values.FormId, _VARIANT_5993]
        | Annotated[FurnitureAnim5994, _VARIANT_5994]
        | Annotated[FurnitureEntry5995, _VARIANT_5995]
        | Annotated[_values.FormId, _VARIANT_5996]
        | Annotated[WardState5997, _VARIANT_5997]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5998,
        ]
        | Annotated[_values.FormId, _VARIANT_5999]
        | Annotated[_values.FormId, _VARIANT_6000]
        | Annotated[_values.FormId, _VARIANT_6001]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_6003]
        | Annotated[bytes, _VARIANT_6004]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_6005,
        ]
        | Annotated[float, _VARIANT_6006]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6007,
        ]
        | Annotated[Sex6008, _VARIANT_6008]
        | Annotated[ActorValue6009, _VARIANT_6009]
        | Annotated[CrimeType6010, _VARIANT_6010]
        | Annotated[Axis6011, _VARIANT_6011]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_6012,
        ]
        | Annotated[MiscStat6013, _VARIANT_6013]
        | Annotated[Alignment6014, _VARIANT_6014]
        | Annotated[_values.FormId, _VARIANT_6015]
        | Annotated[FormType6016, _VARIANT_6016]
        | Annotated[CriticalStage6017, _VARIANT_6017]
        | Annotated[_values.FormId, _VARIANT_6018]
        | Annotated[_values.FormId, _VARIANT_6019]
        | Annotated[_values.FormId, _VARIANT_6020]
        | Annotated[_values.FormId, _VARIANT_6021]
        | Annotated[_values.FormId, _VARIANT_6022]
        | Annotated[_values.FormId, _VARIANT_6023]
        | Annotated[_values.FormId, _VARIANT_6024]
        | Annotated[_values.FormId, _VARIANT_6025]
        | Annotated[_values.FormId, _VARIANT_6026]
        | Annotated[_values.FormId, _VARIANT_6027]
        | Annotated[_values.FormId, _VARIANT_6028]
        | Annotated[_values.FormId, _VARIANT_6029]
        | Annotated[_values.FormId, _VARIANT_6030]
        | Annotated[_values.FormId, _VARIANT_6031]
        | Annotated[_values.FormId, _VARIANT_6032]
        | Annotated[_values.FormId, _VARIANT_6033]
        | Annotated[_values.FormId, _VARIANT_6034]
        | Annotated[_values.FormId, _VARIANT_6035]
        | Annotated[_values.FormId, _VARIANT_6036]
        | Annotated[_values.FormId, _VARIANT_6037]
        | Annotated[_values.FormId, _VARIANT_6038]
        | Annotated[_values.FormId, _VARIANT_6039]
        | Annotated[VatsValueFunction6040, _VARIANT_6040]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_6042]
            | Annotated[_values.FormId, _VARIANT_6043]
            | Annotated[_values.FormId, _VARIANT_6044]
            | Annotated[_values.FormId, _VARIANT_6045]
            | Annotated[bytes, _VARIANT_6046]
            | Annotated[TargetPart6047, _VARIANT_6047]
            | Annotated[VatsAction6048, _VARIANT_6048]
            | Annotated[bytes, _VARIANT_6049]
            | Annotated[bytes, _VARIANT_6050]
            | Annotated[_values.FormId, _VARIANT_6051]
            | Annotated[_values.FormId, _VARIANT_6052]
            | Annotated[bytes, _VARIANT_6053]
            | Annotated[bytes, _VARIANT_6054]
            | Annotated[bytes, _VARIANT_6055]
            | Annotated[bytes, _VARIANT_6056]
            | Annotated[WeaponType6057, _VARIANT_6057]
            | Annotated[bytes, _VARIANT_6058]
            | Annotated[bytes, _VARIANT_6059]
            | Annotated[ProjectileType6060, _VARIANT_6060]
            | Annotated[DeliveryType6061, _VARIANT_6061]
            | Annotated[CastingType6062, _VARIANT_6062],
            _VARIANT_6041,
        ]
        | Annotated[_values.FormId, _VARIANT_6063]
        | Annotated[_values.FormId, _VARIANT_6064]
        | Annotated[_values.FormId, _VARIANT_6065]
        | Annotated[PlayerAction6066, _VARIANT_6066]
        | Annotated[CastingType6067, _VARIANT_6067]
        | Annotated[_values.FormId, _VARIANT_6068]
        | Annotated[_values.FormId, _VARIANT_6069]
        | Annotated[_values.FormId, _VARIANT_6070]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_6071,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6072,
        ]
        | Annotated[_values.FormId, _VARIANT_6073]
        | Annotated[FurnitureAnim6074, _VARIANT_6074]
        | Annotated[FurnitureEntry6075, _VARIANT_6075]
        | Annotated[_values.FormId, _VARIANT_6076]
        | Annotated[WardState6077, _VARIANT_6077]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6078,
        ]
        | Annotated[_values.FormId, _VARIANT_6079]
        | Annotated[_values.FormId, _VARIANT_6080]
        | Annotated[_values.FormId, _VARIANT_6081]
    )
    """Value decoded from this schema node."""

    run_on: RunOn6082
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6084,
        ]
        | Annotated[_values.FormId, _VARIANT_6085]
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
        Annotated[float, _VARIANT_5939]
        | Annotated[_values.FormId, _VARIANT_5940]
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
    def field(self, name: Literal["unused_5942"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_5944]
        | Annotated[bytes, _VARIANT_5945]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5946,
        ]
        | Annotated[float, _VARIANT_5947]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5948,
        ]
        | Annotated[Sex5949, _VARIANT_5949]
        | Annotated[ActorValue5950, _VARIANT_5950]
        | Annotated[CrimeType5951, _VARIANT_5951]
        | Annotated[Axis5952, _VARIANT_5952]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5953,
        ]
        | Annotated[MiscStat5954, _VARIANT_5954]
        | Annotated[Alignment5955, _VARIANT_5955]
        | Annotated[_values.FormId, _VARIANT_5956]
        | Annotated[FormType5957, _VARIANT_5957]
        | Annotated[CriticalStage5958, _VARIANT_5958]
        | Annotated[_values.FormId, _VARIANT_5959]
        | Annotated[_values.FormId, _VARIANT_5960]
        | Annotated[_values.FormId, _VARIANT_5961]
        | Annotated[_values.FormId, _VARIANT_5962]
        | Annotated[_values.FormId, _VARIANT_5963]
        | Annotated[_values.FormId, _VARIANT_5964]
        | Annotated[_values.FormId, _VARIANT_5965]
        | Annotated[_values.FormId, _VARIANT_5966]
        | Annotated[_values.FormId, _VARIANT_5967]
        | Annotated[_values.FormId, _VARIANT_5968]
        | Annotated[_values.FormId, _VARIANT_5969]
        | Annotated[_values.FormId, _VARIANT_5970]
        | Annotated[_values.FormId, _VARIANT_5971]
        | Annotated[_values.FormId, _VARIANT_5972]
        | Annotated[_values.FormId, _VARIANT_5973]
        | Annotated[_values.FormId, _VARIANT_5974]
        | Annotated[_values.FormId, _VARIANT_5975]
        | Annotated[_values.FormId, _VARIANT_5976]
        | Annotated[_values.FormId, _VARIANT_5977]
        | Annotated[_values.FormId, _VARIANT_5978]
        | Annotated[_values.FormId, _VARIANT_5979]
        | Annotated[_values.FormId, _VARIANT_5980]
        | Annotated[VatsValueFunction5981, _VARIANT_5981]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5982,
        ]
        | Annotated[_values.FormId, _VARIANT_5983]
        | Annotated[_values.FormId, _VARIANT_5984]
        | Annotated[_values.FormId, _VARIANT_5985]
        | Annotated[PlayerAction5986, _VARIANT_5986]
        | Annotated[CastingType5987, _VARIANT_5987]
        | Annotated[_values.FormId, _VARIANT_5988]
        | Annotated[_values.FormId, _VARIANT_5989]
        | Annotated[_values.FormId, _VARIANT_5990]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_5991,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5992,
        ]
        | Annotated[_values.FormId, _VARIANT_5993]
        | Annotated[FurnitureAnim5994, _VARIANT_5994]
        | Annotated[FurnitureEntry5995, _VARIANT_5995]
        | Annotated[_values.FormId, _VARIANT_5996]
        | Annotated[WardState5997, _VARIANT_5997]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_5998,
        ]
        | Annotated[_values.FormId, _VARIANT_5999]
        | Annotated[_values.FormId, _VARIANT_6000]
        | Annotated[_values.FormId, _VARIANT_6001]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_6003]
        | Annotated[bytes, _VARIANT_6004]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_6005,
        ]
        | Annotated[float, _VARIANT_6006]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6007,
        ]
        | Annotated[Sex6008, _VARIANT_6008]
        | Annotated[ActorValue6009, _VARIANT_6009]
        | Annotated[CrimeType6010, _VARIANT_6010]
        | Annotated[Axis6011, _VARIANT_6011]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_6012,
        ]
        | Annotated[MiscStat6013, _VARIANT_6013]
        | Annotated[Alignment6014, _VARIANT_6014]
        | Annotated[_values.FormId, _VARIANT_6015]
        | Annotated[FormType6016, _VARIANT_6016]
        | Annotated[CriticalStage6017, _VARIANT_6017]
        | Annotated[_values.FormId, _VARIANT_6018]
        | Annotated[_values.FormId, _VARIANT_6019]
        | Annotated[_values.FormId, _VARIANT_6020]
        | Annotated[_values.FormId, _VARIANT_6021]
        | Annotated[_values.FormId, _VARIANT_6022]
        | Annotated[_values.FormId, _VARIANT_6023]
        | Annotated[_values.FormId, _VARIANT_6024]
        | Annotated[_values.FormId, _VARIANT_6025]
        | Annotated[_values.FormId, _VARIANT_6026]
        | Annotated[_values.FormId, _VARIANT_6027]
        | Annotated[_values.FormId, _VARIANT_6028]
        | Annotated[_values.FormId, _VARIANT_6029]
        | Annotated[_values.FormId, _VARIANT_6030]
        | Annotated[_values.FormId, _VARIANT_6031]
        | Annotated[_values.FormId, _VARIANT_6032]
        | Annotated[_values.FormId, _VARIANT_6033]
        | Annotated[_values.FormId, _VARIANT_6034]
        | Annotated[_values.FormId, _VARIANT_6035]
        | Annotated[_values.FormId, _VARIANT_6036]
        | Annotated[_values.FormId, _VARIANT_6037]
        | Annotated[_values.FormId, _VARIANT_6038]
        | Annotated[_values.FormId, _VARIANT_6039]
        | Annotated[VatsValueFunction6040, _VARIANT_6040]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_6042]
            | Annotated[_values.FormId, _VARIANT_6043]
            | Annotated[_values.FormId, _VARIANT_6044]
            | Annotated[_values.FormId, _VARIANT_6045]
            | Annotated[bytes, _VARIANT_6046]
            | Annotated[TargetPart6047, _VARIANT_6047]
            | Annotated[VatsAction6048, _VARIANT_6048]
            | Annotated[bytes, _VARIANT_6049]
            | Annotated[bytes, _VARIANT_6050]
            | Annotated[_values.FormId, _VARIANT_6051]
            | Annotated[_values.FormId, _VARIANT_6052]
            | Annotated[bytes, _VARIANT_6053]
            | Annotated[bytes, _VARIANT_6054]
            | Annotated[bytes, _VARIANT_6055]
            | Annotated[bytes, _VARIANT_6056]
            | Annotated[WeaponType6057, _VARIANT_6057]
            | Annotated[bytes, _VARIANT_6058]
            | Annotated[bytes, _VARIANT_6059]
            | Annotated[ProjectileType6060, _VARIANT_6060]
            | Annotated[DeliveryType6061, _VARIANT_6061]
            | Annotated[CastingType6062, _VARIANT_6062],
            _VARIANT_6041,
        ]
        | Annotated[_values.FormId, _VARIANT_6063]
        | Annotated[_values.FormId, _VARIANT_6064]
        | Annotated[_values.FormId, _VARIANT_6065]
        | Annotated[PlayerAction6066, _VARIANT_6066]
        | Annotated[CastingType6067, _VARIANT_6067]
        | Annotated[_values.FormId, _VARIANT_6068]
        | Annotated[_values.FormId, _VARIANT_6069]
        | Annotated[_values.FormId, _VARIANT_6070]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_6071,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6072,
        ]
        | Annotated[_values.FormId, _VARIANT_6073]
        | Annotated[FurnitureAnim6074, _VARIANT_6074]
        | Annotated[FurnitureEntry6075, _VARIANT_6075]
        | Annotated[_values.FormId, _VARIANT_6076]
        | Annotated[WardState6077, _VARIANT_6077]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6078,
        ]
        | Annotated[_values.FormId, _VARIANT_6079]
        | Annotated[_values.FormId, _VARIANT_6080]
        | Annotated[_values.FormId, _VARIANT_6081]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn6082]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_6084,
        ]
        | Annotated[_values.FormId, _VARIANT_6085]
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


class Condition5933(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition/1:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/0:C"
                "TDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/1:P"
                "arameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition/2:P"
                "arameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure5935] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure5935]]:
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


class PerkCondition5929(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
        "t/0:Perk Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "run_on_tab_index": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/0:Run On (Tab Index)"
            ),
            kind="subrecord",
            name="Run On (Tab Index)",
        ),
        "conditions": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions"
            ),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition/1:Conditions/repeat/0:Condition"
            ),
            child_kind="sequence",
        ),
    }

    run_on_tab_index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition5933, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["run_on_tab_index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition5933, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class NoneFloatFloatAvFloatLvliSpelLstringF63877E726093(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    FLOAT = 1
    FLOAT_AV_FLOAT = 2
    LVLI = 3
    SPEL_LSTRING_FLAGS = 4
    SPEL = 5
    STRING = 6
    LSTRING = 7


class ScriptFlags6098(enum.IntFlag):
    """Named values from the pinned schema."""

    RUN_IMMEDIATELY = 1
    REPLACE_DEFAULT = 2


class Structure6097(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/2"
        ":Script Flags/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_flags": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/2"
                ":Script Flags/payload/0:Script Flags"
            ),
            kind="primitive",
            name="Script Flags",
        ),
        "fragment_index": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/2"
                ":Script Flags/payload/1:Fragment Index"
            ),
            kind="primitive",
            name="Fragment Index",
        ),
    }

    script_flags: ScriptFlags6098
    """Value decoded from this schema node."""

    fragment_index: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["script_flags"]
    ) -> _base.FieldRef[ScriptFlags6098]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fragment_index"]
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


_VARIANT_6102: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/0:Unknown"
    )
)


_VARIANT_6103: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/1:Float"
    )
)


class FloatFloat6104(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/2:Float, Float"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "float_1": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
                ":Data/payload/variants/2:Float, Float/0:Float 1"
            ),
            kind="primitive",
            name="Float 1",
        ),
        "float_2": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
                ":Data/payload/variants/2:Float, Float/1:Float 2"
            ),
            kind="primitive",
            name="Float 2",
        ),
    }

    float_1: float
    """Value decoded from this schema node."""

    float_2: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["float_1"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["float_2"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6104: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/2:Float, Float"
    )
)


_VARIANT_6107: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/3:Leveled Item"
    )
)


_VARIANT_6108: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/4:Spell"
    )
)


_VARIANT_6109: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/5:Spell"
    )
)


_VARIANT_6110: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/6:Text"
    )
)


_VARIANT_6111: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/7:Text"
    )
)


class ActorValueFloat6112(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/8:Actor Value, Float"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "actor_value": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
                ":Data/payload/variants/8:Actor Value, Float/0:Actor Va"
                "lue"
            ),
            kind="primitive",
            name="Actor Value",
        ),
        "float": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
                ":Data/payload/variants/8:Actor Value, Float/1:Float"
            ),
            kind="primitive",
            name="Float",
        ),
    }

    actor_value: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    float: float
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["actor_value"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["float"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_6112: _base.Variant = _base.Variant(
    path=(
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3"
        ":Data/payload/variants/8:Actor Value, Float"
    )
)


class FunctionParameters6091(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "PERK/8:Effects/repeat/0:Effect/3:Function Parameters"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/0:Type"
            ),
            kind="subrecord",
            name="Type",
        ),
        "button_label": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/1"
                ":Button Label"
            ),
            kind="subrecord",
            name="Button Label",
        ),
        "script_flags": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/2"
                ":Script Flags"
            ),
            kind="subrecord",
            name="Script Flags",
        ),
        "data": _base.Binding(
            path=(
                "PERK/8:Effects/repeat/0:Effect/3:Function Parameters/3:Data"
            ),
            kind="subrecord",
            name="Data",
        ),
    }

    type: Optional[NoneFloatFloatAvFloatLvliSpelLstringF63877E726093] = None
    """Value decoded from this schema node."""

    button_label: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    script_flags: Optional[Structure6097] = None
    """Value decoded from this schema node."""

    data: Optional[
        Annotated[bytes, _VARIANT_6102]
        | Annotated[float, _VARIANT_6103]
        | Annotated[FloatFloat6104, _VARIANT_6104]
        | Annotated[_values.FormId, _VARIANT_6107]
        | Annotated[_values.FormId, _VARIANT_6108]
        | Annotated[_values.FormId, _VARIANT_6109]
        | Annotated[str, _VARIANT_6110]
        | Annotated[str | _values.UInt32, _VARIANT_6111]
        | Annotated[ActorValueFloat6112, _VARIANT_6112]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["type"]
    ) -> _base.FieldRef[
        Optional[NoneFloatFloatAvFloatLvliSpelLstringF63877E726093]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["button_label"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_flags"]
    ) -> _base.FieldRef[Optional[Structure6097]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[bytes, _VARIANT_6102]
            | Annotated[float, _VARIANT_6103]
            | Annotated[FloatFloat6104, _VARIANT_6104]
            | Annotated[_values.FormId, _VARIANT_6107]
            | Annotated[_values.FormId, _VARIANT_6108]
            | Annotated[_values.FormId, _VARIANT_6109]
            | Annotated[str, _VARIANT_6110]
            | Annotated[str | _values.UInt32, _VARIANT_6111]
            | Annotated[ActorValueFloat6112, _VARIANT_6112]
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


class Effect5911(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PERK/8:Effects/repeat/0:Effect"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="PERK/8:Effects/repeat/0:Effect/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "effect_data": _base.Binding(
            path="PERK/8:Effects/repeat/0:Effect/1:Effect Data",
            kind="subrecord",
            name="Effect Data",
        ),
        "perk_conditions": _base.Binding(
            path="PERK/8:Effects/repeat/0:Effect/2:Perk Conditions",
            kind="repeat",
            name="Perk Conditions",
            repeated_path=(
                "PERK/8:Effects/repeat/0:Effect/2:Perk Conditions/repea"
                "t/0:Perk Condition"
            ),
            child_kind="sequence",
        ),
        "function_parameters": _base.Binding(
            path=("PERK/8:Effects/repeat/0:Effect/3:Function Parameters"),
            kind="sequence",
            name="Function Parameters",
        ),
        "end_marker": _base.Binding(
            path="PERK/8:Effects/repeat/0:Effect/4:End Marker",
            kind="subrecord",
            name="End Marker",
        ),
    }

    header: Optional[Structure5913] = None
    """Value decoded from this schema node."""

    effect_data: Optional[
        Annotated[QuestStage5919, _VARIANT_5919]
        | Annotated[_values.FormId, _VARIANT_5923]
        | Annotated[EntryPoint5924, _VARIANT_5924]
    ] = None
    """Value decoded from this schema node."""

    perk_conditions: tuple[PerkCondition5929, ...] = ()
    """Value decoded from this schema node."""

    function_parameters: Optional[FunctionParameters6091] = None
    """Value decoded from this schema node."""

    end_marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure5913]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effect_data"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[QuestStage5919, _VARIANT_5919]
            | Annotated[_values.FormId, _VARIANT_5923]
            | Annotated[EntryPoint5924, _VARIANT_5924]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["perk_conditions"]
    ) -> _base.FieldRef[tuple[PerkCondition5929, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["function_parameters"]
    ) -> _base.FieldRef[Optional[FunctionParameters6091]]:
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


class PerkRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "PERK"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "PERK"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="PERK/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="PERK/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "name": _base.Binding(
            path="PERK/2:Name",
            kind="subrecord",
            name="Name",
        ),
        "description": _base.Binding(
            path="PERK/3:Description",
            kind="subrecord",
            name="Description",
        ),
        "icon": _base.Binding(
            path="PERK/4:Icon",
            kind="unordered",
            name="Icon",
        ),
        "conditions": _base.Binding(
            path="PERK/5:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="PERK/5:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "data": _base.Binding(
            path="PERK/6:Data",
            kind="subrecord",
            name="Data",
        ),
        "next_perk": _base.Binding(
            path="PERK/7:Next Perk",
            kind="subrecord",
            name="Next Perk",
        ),
        "effects": _base.Binding(
            path="PERK/8:Effects",
            kind="repeat",
            name="Effects",
            repeated_path="PERK/8:Effects/repeat/0:Effect",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure5678] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    description: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    icon: Optional[Icon5737] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition5743, ...] = ()
    """Value decoded from this schema node."""

    data: Optional[Structure5902] = None
    """Value decoded from this schema node."""

    next_perk: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    effects: tuple[Effect5911, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure5678]]:
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
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["icon"]
    ) -> _base.FieldRef[Optional[Icon5737]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition5743, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure5902]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["next_perk"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["effects"]
    ) -> _base.FieldRef[tuple[Effect5911, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
