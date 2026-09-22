"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags7974(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type7978(_values.OpenIntEnum):
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


class Flags7979(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_7981: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV27983(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_7983: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV17987(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_7987: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_7982: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_7991: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_7992: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_7993: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool7994(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_7994: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV27997(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_7997: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV18001(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_8001: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_7995: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_8005: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_8007: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_8009: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element8012(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_8011: _base.Variant = _base.Variant(
    path=(
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property7976(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type7978
    """Value decoded from this schema node."""

    flags: Flags7979
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_7981]
        | Annotated[
            Annotated[ObjectV27983, _VARIANT_7983]
            | Annotated[ObjectV17987, _VARIANT_7987],
            _VARIANT_7982,
        ]
        | Annotated[str, _VARIANT_7991]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7992,
        ]
        | Annotated[float, _VARIANT_7993]
        | Annotated[Bool7994, _VARIANT_7994]
        | Annotated[
            tuple[
                Annotated[ObjectV27997, _VARIANT_7997]
                | Annotated[ObjectV18001, _VARIANT_8001],
                ...,
            ],
            _VARIANT_7995,
        ]
        | Annotated[tuple[str, ...], _VARIANT_8005]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_8007,
        ]
        | Annotated[tuple[float, ...], _VARIANT_8009]
        | Annotated[tuple[Element8012, ...], _VARIANT_8011]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type7978]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags7979]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_7981]
        | Annotated[
            Annotated[ObjectV27983, _VARIANT_7983]
            | Annotated[ObjectV17987, _VARIANT_7987],
            _VARIANT_7982,
        ]
        | Annotated[str, _VARIANT_7991]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_7992,
        ]
        | Annotated[float, _VARIANT_7993]
        | Annotated[Bool7994, _VARIANT_7994]
        | Annotated[
            tuple[
                Annotated[ObjectV27997, _VARIANT_7997]
                | Annotated[ObjectV18001, _VARIANT_8001],
                ...,
            ],
            _VARIANT_7995,
        ]
        | Annotated[tuple[str, ...], _VARIANT_8005]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_8007,
        ]
        | Annotated[tuple[float, ...], _VARIANT_8009]
        | Annotated[tuple[Element8012, ...], _VARIANT_8011]
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


class Script7972(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags7974
    """Value decoded from this schema node."""

    properties: tuple[Property7976, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags7974]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property7976, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags8015(enum.IntFlag):
    """Named values from the pinned schema."""

    ON_BEGIN = 1
    ON_END = 2


class Fragment8018(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
        "nts/3:Fragments/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/0:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "script_name": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/1:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "fragment_name": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
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


class PhaseFlag8024(enum.IntFlag):
    """Named values from the pinned schema."""

    ON_START = 1
    ON_COMPLETION = 2


class PhaseFragment8023(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
        "nts/4:Phase Fragments/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "phase_flag": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments/element/0:Phase Flag"
            ),
            kind="primitive",
            name="Phase Flag",
        ),
        "phase_index": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments/element/1:Phase Index"
            ),
            kind="primitive",
            name="Phase Index",
        ),
        "unknown": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments/element/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_8027": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments/element/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "unknown_8028": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments/element/4:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "script_name": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments/element/5:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "fragment_name": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments/element/6:FragmentName"
            ),
            kind="primitive",
            name="FragmentName",
        ),
    }

    phase_flag: PhaseFlag8024
    """Value decoded from this schema node."""

    phase_index: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unknown: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    unknown_8027: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    unknown_8028: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    script_name: str
    """Value decoded from this schema node."""

    fragment_name: str
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["phase_flag"]
    ) -> _base.FieldRef[PhaseFlag8024]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["phase_index"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
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
        self, name: Literal["unknown_8027"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8028"]
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


class ScriptFragments8013(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragments"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "extra_bind_data_version": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/0:Extra bind data version"
            ),
            kind="primitive",
            name="Extra bind data version",
        ),
        "flags": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "file_name": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:FileName"
            ),
            kind="primitive",
            name="FileName",
        ),
        "fragments": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments"
            ),
            kind="array",
            name="Fragments",
        ),
        "phase_fragments": _base.Binding(
            path=(
                "SCEN/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/4:Phase Fragments"
            ),
            kind="array",
            name="Phase Fragments",
        ),
    }

    extra_bind_data_version: Annotated[
        int, pydantic.Field(strict=True, ge=-128, le=127)
    ]
    """Value decoded from this schema node."""

    flags: Flags8015
    """Value decoded from this schema node."""

    file_name: str
    """Value decoded from this schema node."""

    fragments: tuple[Fragment8018, ...]
    """Value decoded from this schema node."""

    phase_fragments: tuple[PhaseFragment8023, ...]
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags8015]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["file_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fragments"]
    ) -> _base.FieldRef[tuple[Fragment8018, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["phase_fragments"]
    ) -> _base.FieldRef[tuple[PhaseFragment8023, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure7968(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="SCEN/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("SCEN/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="SCEN/1:Virtual Machine Adapter/payload/2:Scripts",
            kind="array",
            name="Scripts",
        ),
        "script_fragments": _base.Binding(
            path=("SCEN/1:Virtual Machine Adapter/payload/3:Script Fragments"),
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

    scripts: tuple[Script7972, ...]
    """Value decoded from this schema node."""

    script_fragments: Optional[ScriptFragments8013] = None
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
    ) -> _base.FieldRef[tuple[Script7972, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_fragments"]
    ) -> _base.FieldRef[Optional[ScriptFragments8013]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class BeginOnQuestStartStopQuestOnEndShowA0D148Fed8032(enum.IntFlag):
    """Named values from the pinned schema."""

    BEGIN_ON_QUEST_START = 1
    STOP_QUEST_ON_END = 2
    SHOW_ALL_TEXT = 4
    REPEAT_CONDITIONS_WHILE_TRUE = 8
    INTERRUPTIBLE = 16


_VARIANT_8047: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/2:Comparison "
        "Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_8048: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/2:Comparison "
        "Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_8052: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/0:Unknown"
    )
)


_VARIANT_8053: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/1:None"
    )
)


_VARIANT_8054: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/2:Integer"
    )
)


_VARIANT_8055: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/3:Float"
    )
)


_VARIANT_8056: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/4:Variable Name"
    )
)


class Sex8057(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8057: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/5:Sex"
    )
)


class ActorValue8058(_values.OpenIntEnum):
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


_VARIANT_8058: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/6:Actor Value"
    )
)


class CrimeType8059(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8059: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/7:Crime Type"
    )
)


class Axis8060(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8060: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/8:Axis"
    )
)


_VARIANT_8061: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat8062(_values.OpenIntEnum):
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


_VARIANT_8062: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/10:Misc Stat"
    )
)


class Alignment8063(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8063: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/11:Alignment"
    )
)


_VARIANT_8064: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/12:Equip Type"
    )
)


class FormType8065(_values.OpenIntEnum):
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


_VARIANT_8065: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/13:Form Type"
    )
)


class CriticalStage8066(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8066: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/14:Critical Stage"
    )
)


_VARIANT_8067: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/15:Object Reference"
    )
)


_VARIANT_8068: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/16:Inventory Object"
    )
)


_VARIANT_8069: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/17:Actor"
    )
)


_VARIANT_8070: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/18:Voice Type"
    )
)


_VARIANT_8071: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/19:Idle"
    )
)


_VARIANT_8072: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/20:Form List"
    )
)


_VARIANT_8073: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/21:Quest"
    )
)


_VARIANT_8074: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/22:Faction"
    )
)


_VARIANT_8075: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/23:Cell"
    )
)


_VARIANT_8076: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/24:Class"
    )
)


_VARIANT_8077: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/25:Race"
    )
)


_VARIANT_8078: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/26:Actor Base"
    )
)


_VARIANT_8079: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/27:Global"
    )
)


_VARIANT_8080: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/28:Weather"
    )
)


_VARIANT_8081: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/29:Package"
    )
)


_VARIANT_8082: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/30:Encounter Zone"
    )
)


_VARIANT_8083: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/31:Perk"
    )
)


_VARIANT_8084: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/32:Owner"
    )
)


_VARIANT_8085: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/33:Furniture"
    )
)


_VARIANT_8086: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/34:Effect Item"
    )
)


_VARIANT_8087: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/35:Base Effect"
    )
)


_VARIANT_8088: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/36:Worldspace"
    )
)


class VatsValueFunction8089(_values.OpenIntEnum):
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


_VARIANT_8089: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/37:VATS Value Function"
    )
)


_VARIANT_8090: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_8091: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/39:Referenceable Object"
    )
)


_VARIANT_8092: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/40:Region"
    )
)


_VARIANT_8093: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/41:Keyword"
    )
)


class PlayerAction8094(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8094: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/42:Player Action"
    )
)


class CastingType8095(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8095: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/43:Casting Type"
    )
)


_VARIANT_8096: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/44:Shout"
    )
)


_VARIANT_8097: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/45:Location"
    )
)


_VARIANT_8098: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/46:Location Ref Type"
    )
)


_VARIANT_8099: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/47:Alias"
    )
)


_VARIANT_8100: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/48:Packdata ID"
    )
)


_VARIANT_8101: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/49:Association Type"
    )
)


class FurnitureAnim8102(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8102: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8103(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8103: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/51:Furniture Entry"
    )
)


_VARIANT_8104: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/52:Scene"
    )
)


class WardState8105(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8105: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/53:Ward State"
    )
)


_VARIANT_8106: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/54:Event"
    )
)


_VARIANT_8107: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/55:Event Data"
    )
)


_VARIANT_8108: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/56:Knowable"
    )
)


_VARIANT_8109: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
        "1/variants/57:Faction"
    )
)


_VARIANT_8111: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/0:Unknown"
    )
)


_VARIANT_8112: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/1:None"
    )
)


_VARIANT_8113: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/2:Integer"
    )
)


_VARIANT_8114: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/3:Float"
    )
)


_VARIANT_8115: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/4:Variable Name"
    )
)


class Sex8116(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8116: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/5:Sex"
    )
)


class ActorValue8117(_values.OpenIntEnum):
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


_VARIANT_8117: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/6:Actor Value"
    )
)


class CrimeType8118(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8118: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/7:Crime Type"
    )
)


class Axis8119(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8119: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/8:Axis"
    )
)


_VARIANT_8120: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/9:Quest Stage"
    )
)


class MiscStat8121(_values.OpenIntEnum):
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


_VARIANT_8121: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/10:Misc Stat"
    )
)


class Alignment8122(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8122: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/11:Alignment"
    )
)


_VARIANT_8123: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/12:Equip Type"
    )
)


class FormType8124(_values.OpenIntEnum):
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


_VARIANT_8124: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/13:Form Type"
    )
)


class CriticalStage8125(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8125: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/14:Critical Stage"
    )
)


_VARIANT_8126: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/15:Object Reference"
    )
)


_VARIANT_8127: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/16:Inventory Object"
    )
)


_VARIANT_8128: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/17:Actor"
    )
)


_VARIANT_8129: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/18:Voice Type"
    )
)


_VARIANT_8130: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/19:Idle"
    )
)


_VARIANT_8131: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/20:Form List"
    )
)


_VARIANT_8132: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/21:Quest"
    )
)


_VARIANT_8133: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/22:Faction"
    )
)


_VARIANT_8134: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/23:Cell"
    )
)


_VARIANT_8135: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/24:Class"
    )
)


_VARIANT_8136: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/25:Race"
    )
)


_VARIANT_8137: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/26:Actor Base"
    )
)


_VARIANT_8138: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/27:Global"
    )
)


_VARIANT_8139: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/28:Weather"
    )
)


_VARIANT_8140: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/29:Package"
    )
)


_VARIANT_8141: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/30:Encounter Zone"
    )
)


_VARIANT_8142: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/31:Perk"
    )
)


_VARIANT_8143: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/32:Owner"
    )
)


_VARIANT_8144: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/33:Furniture"
    )
)


_VARIANT_8145: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/34:Effect Item"
    )
)


_VARIANT_8146: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/35:Base Effect"
    )
)


_VARIANT_8147: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/36:Worldspace"
    )
)


class VatsValueFunction8148(_values.OpenIntEnum):
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


_VARIANT_8148: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/37:VATS Value Function"
    )
)


_VARIANT_8150: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/0:Weapon"
    )
)


_VARIANT_8151: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/1:Weapon List"
    )
)


_VARIANT_8152: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/2:Target"
    )
)


_VARIANT_8153: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/3:Target List"
    )
)


_VARIANT_8154: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/4:Unknown"
    )
)


class TargetPart8155(_values.OpenIntEnum):
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


_VARIANT_8155: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/5:Target Part"
    )
)


class VatsAction8156(_values.OpenIntEnum):
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


_VARIANT_8156: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/6:VATS Action"
    )
)


_VARIANT_8157: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/7:Unknown"
    )
)


_VARIANT_8158: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/8:Unknown"
    )
)


_VARIANT_8159: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/9:Critical Eff"
        "ect"
    )
)


_VARIANT_8160: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/10:Critical Ef"
        "fect List"
    )
)


_VARIANT_8161: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/11:Unknown"
    )
)


_VARIANT_8162: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/12:Unknown"
    )
)


_VARIANT_8163: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/13:Unknown"
    )
)


_VARIANT_8164: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/14:Unknown"
    )
)


class WeaponType8165(_values.OpenIntEnum):
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


_VARIANT_8165: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_8166: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/16:Unknown"
    )
)


_VARIANT_8167: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/17:Unknown"
    )
)


class ProjectileType8168(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_8168: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/18:Projectile "
        "Type"
    )
)


class DeliveryType8169(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_8169: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/19:Delivery Ty"
        "pe"
    )
)


class CastingType8170(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_8170: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param/variants/20:Casting Typ"
        "e"
    )
)


_VARIANT_8149: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/38:VATS Value Param"
    )
)


_VARIANT_8171: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/39:Referenceable Object"
    )
)


_VARIANT_8172: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/40:Region"
    )
)


_VARIANT_8173: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/41:Keyword"
    )
)


class PlayerAction8174(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8174: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/42:Player Action"
    )
)


class CastingType8175(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8175: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/43:Casting Type"
    )
)


_VARIANT_8176: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/44:Shout"
    )
)


_VARIANT_8177: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/45:Location"
    )
)


_VARIANT_8178: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/46:Location Ref Type"
    )
)


_VARIANT_8179: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/47:Alias"
    )
)


_VARIANT_8180: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/48:Packdata ID"
    )
)


_VARIANT_8181: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/49:Association Type"
    )
)


class FurnitureAnim8182(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8182: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8183(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8183: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/51:Furniture Entry"
    )
)


_VARIANT_8184: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/52:Scene"
    )
)


class WardState8185(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8185: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/53:Ward State"
    )
)


_VARIANT_8186: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/54:Event"
    )
)


_VARIANT_8187: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/55:Event Data"
    )
)


_VARIANT_8188: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/56:Knowable"
    )
)


_VARIANT_8189: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
        "2/variants/57:Faction"
    )
)


class RunOn8190(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_8192: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/8:Reference/v"
        "ariants/0:Unused"
    )
)


_VARIANT_8193: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload/8:Reference/v"
        "ariants/1:Reference"
    )
)


class Structure8043(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/2:Comparison "
                "Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_8050": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/5:Parameter #"
                "1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/6:Parameter #"
                "2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA/payload/9:Parameter #"
                "3"
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
        Annotated[float, _VARIANT_8047]
        | Annotated[_values.FormId, _VARIANT_8048]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_8050: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_8052]
        | Annotated[bytes, _VARIANT_8053]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8054,
        ]
        | Annotated[float, _VARIANT_8055]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8056,
        ]
        | Annotated[Sex8057, _VARIANT_8057]
        | Annotated[ActorValue8058, _VARIANT_8058]
        | Annotated[CrimeType8059, _VARIANT_8059]
        | Annotated[Axis8060, _VARIANT_8060]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8061,
        ]
        | Annotated[MiscStat8062, _VARIANT_8062]
        | Annotated[Alignment8063, _VARIANT_8063]
        | Annotated[_values.FormId, _VARIANT_8064]
        | Annotated[FormType8065, _VARIANT_8065]
        | Annotated[CriticalStage8066, _VARIANT_8066]
        | Annotated[_values.FormId, _VARIANT_8067]
        | Annotated[_values.FormId, _VARIANT_8068]
        | Annotated[_values.FormId, _VARIANT_8069]
        | Annotated[_values.FormId, _VARIANT_8070]
        | Annotated[_values.FormId, _VARIANT_8071]
        | Annotated[_values.FormId, _VARIANT_8072]
        | Annotated[_values.FormId, _VARIANT_8073]
        | Annotated[_values.FormId, _VARIANT_8074]
        | Annotated[_values.FormId, _VARIANT_8075]
        | Annotated[_values.FormId, _VARIANT_8076]
        | Annotated[_values.FormId, _VARIANT_8077]
        | Annotated[_values.FormId, _VARIANT_8078]
        | Annotated[_values.FormId, _VARIANT_8079]
        | Annotated[_values.FormId, _VARIANT_8080]
        | Annotated[_values.FormId, _VARIANT_8081]
        | Annotated[_values.FormId, _VARIANT_8082]
        | Annotated[_values.FormId, _VARIANT_8083]
        | Annotated[_values.FormId, _VARIANT_8084]
        | Annotated[_values.FormId, _VARIANT_8085]
        | Annotated[_values.FormId, _VARIANT_8086]
        | Annotated[_values.FormId, _VARIANT_8087]
        | Annotated[_values.FormId, _VARIANT_8088]
        | Annotated[VatsValueFunction8089, _VARIANT_8089]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8090,
        ]
        | Annotated[_values.FormId, _VARIANT_8091]
        | Annotated[_values.FormId, _VARIANT_8092]
        | Annotated[_values.FormId, _VARIANT_8093]
        | Annotated[PlayerAction8094, _VARIANT_8094]
        | Annotated[CastingType8095, _VARIANT_8095]
        | Annotated[_values.FormId, _VARIANT_8096]
        | Annotated[_values.FormId, _VARIANT_8097]
        | Annotated[_values.FormId, _VARIANT_8098]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8099,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8100,
        ]
        | Annotated[_values.FormId, _VARIANT_8101]
        | Annotated[FurnitureAnim8102, _VARIANT_8102]
        | Annotated[FurnitureEntry8103, _VARIANT_8103]
        | Annotated[_values.FormId, _VARIANT_8104]
        | Annotated[WardState8105, _VARIANT_8105]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8106,
        ]
        | Annotated[_values.FormId, _VARIANT_8107]
        | Annotated[_values.FormId, _VARIANT_8108]
        | Annotated[_values.FormId, _VARIANT_8109]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_8111]
        | Annotated[bytes, _VARIANT_8112]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8113,
        ]
        | Annotated[float, _VARIANT_8114]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8115,
        ]
        | Annotated[Sex8116, _VARIANT_8116]
        | Annotated[ActorValue8117, _VARIANT_8117]
        | Annotated[CrimeType8118, _VARIANT_8118]
        | Annotated[Axis8119, _VARIANT_8119]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8120,
        ]
        | Annotated[MiscStat8121, _VARIANT_8121]
        | Annotated[Alignment8122, _VARIANT_8122]
        | Annotated[_values.FormId, _VARIANT_8123]
        | Annotated[FormType8124, _VARIANT_8124]
        | Annotated[CriticalStage8125, _VARIANT_8125]
        | Annotated[_values.FormId, _VARIANT_8126]
        | Annotated[_values.FormId, _VARIANT_8127]
        | Annotated[_values.FormId, _VARIANT_8128]
        | Annotated[_values.FormId, _VARIANT_8129]
        | Annotated[_values.FormId, _VARIANT_8130]
        | Annotated[_values.FormId, _VARIANT_8131]
        | Annotated[_values.FormId, _VARIANT_8132]
        | Annotated[_values.FormId, _VARIANT_8133]
        | Annotated[_values.FormId, _VARIANT_8134]
        | Annotated[_values.FormId, _VARIANT_8135]
        | Annotated[_values.FormId, _VARIANT_8136]
        | Annotated[_values.FormId, _VARIANT_8137]
        | Annotated[_values.FormId, _VARIANT_8138]
        | Annotated[_values.FormId, _VARIANT_8139]
        | Annotated[_values.FormId, _VARIANT_8140]
        | Annotated[_values.FormId, _VARIANT_8141]
        | Annotated[_values.FormId, _VARIANT_8142]
        | Annotated[_values.FormId, _VARIANT_8143]
        | Annotated[_values.FormId, _VARIANT_8144]
        | Annotated[_values.FormId, _VARIANT_8145]
        | Annotated[_values.FormId, _VARIANT_8146]
        | Annotated[_values.FormId, _VARIANT_8147]
        | Annotated[VatsValueFunction8148, _VARIANT_8148]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8150]
            | Annotated[_values.FormId, _VARIANT_8151]
            | Annotated[_values.FormId, _VARIANT_8152]
            | Annotated[_values.FormId, _VARIANT_8153]
            | Annotated[bytes, _VARIANT_8154]
            | Annotated[TargetPart8155, _VARIANT_8155]
            | Annotated[VatsAction8156, _VARIANT_8156]
            | Annotated[bytes, _VARIANT_8157]
            | Annotated[bytes, _VARIANT_8158]
            | Annotated[_values.FormId, _VARIANT_8159]
            | Annotated[_values.FormId, _VARIANT_8160]
            | Annotated[bytes, _VARIANT_8161]
            | Annotated[bytes, _VARIANT_8162]
            | Annotated[bytes, _VARIANT_8163]
            | Annotated[bytes, _VARIANT_8164]
            | Annotated[WeaponType8165, _VARIANT_8165]
            | Annotated[bytes, _VARIANT_8166]
            | Annotated[bytes, _VARIANT_8167]
            | Annotated[ProjectileType8168, _VARIANT_8168]
            | Annotated[DeliveryType8169, _VARIANT_8169]
            | Annotated[CastingType8170, _VARIANT_8170],
            _VARIANT_8149,
        ]
        | Annotated[_values.FormId, _VARIANT_8171]
        | Annotated[_values.FormId, _VARIANT_8172]
        | Annotated[_values.FormId, _VARIANT_8173]
        | Annotated[PlayerAction8174, _VARIANT_8174]
        | Annotated[CastingType8175, _VARIANT_8175]
        | Annotated[_values.FormId, _VARIANT_8176]
        | Annotated[_values.FormId, _VARIANT_8177]
        | Annotated[_values.FormId, _VARIANT_8178]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8179,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8180,
        ]
        | Annotated[_values.FormId, _VARIANT_8181]
        | Annotated[FurnitureAnim8182, _VARIANT_8182]
        | Annotated[FurnitureEntry8183, _VARIANT_8183]
        | Annotated[_values.FormId, _VARIANT_8184]
        | Annotated[WardState8185, _VARIANT_8185]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8186,
        ]
        | Annotated[_values.FormId, _VARIANT_8187]
        | Annotated[_values.FormId, _VARIANT_8188]
        | Annotated[_values.FormId, _VARIANT_8189]
    )
    """Value decoded from this schema node."""

    run_on: RunOn8190
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8192,
        ]
        | Annotated[_values.FormId, _VARIANT_8193]
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
        Annotated[float, _VARIANT_8047]
        | Annotated[_values.FormId, _VARIANT_8048]
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
    def field(self, name: Literal["unused_8050"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8052]
        | Annotated[bytes, _VARIANT_8053]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8054,
        ]
        | Annotated[float, _VARIANT_8055]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8056,
        ]
        | Annotated[Sex8057, _VARIANT_8057]
        | Annotated[ActorValue8058, _VARIANT_8058]
        | Annotated[CrimeType8059, _VARIANT_8059]
        | Annotated[Axis8060, _VARIANT_8060]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8061,
        ]
        | Annotated[MiscStat8062, _VARIANT_8062]
        | Annotated[Alignment8063, _VARIANT_8063]
        | Annotated[_values.FormId, _VARIANT_8064]
        | Annotated[FormType8065, _VARIANT_8065]
        | Annotated[CriticalStage8066, _VARIANT_8066]
        | Annotated[_values.FormId, _VARIANT_8067]
        | Annotated[_values.FormId, _VARIANT_8068]
        | Annotated[_values.FormId, _VARIANT_8069]
        | Annotated[_values.FormId, _VARIANT_8070]
        | Annotated[_values.FormId, _VARIANT_8071]
        | Annotated[_values.FormId, _VARIANT_8072]
        | Annotated[_values.FormId, _VARIANT_8073]
        | Annotated[_values.FormId, _VARIANT_8074]
        | Annotated[_values.FormId, _VARIANT_8075]
        | Annotated[_values.FormId, _VARIANT_8076]
        | Annotated[_values.FormId, _VARIANT_8077]
        | Annotated[_values.FormId, _VARIANT_8078]
        | Annotated[_values.FormId, _VARIANT_8079]
        | Annotated[_values.FormId, _VARIANT_8080]
        | Annotated[_values.FormId, _VARIANT_8081]
        | Annotated[_values.FormId, _VARIANT_8082]
        | Annotated[_values.FormId, _VARIANT_8083]
        | Annotated[_values.FormId, _VARIANT_8084]
        | Annotated[_values.FormId, _VARIANT_8085]
        | Annotated[_values.FormId, _VARIANT_8086]
        | Annotated[_values.FormId, _VARIANT_8087]
        | Annotated[_values.FormId, _VARIANT_8088]
        | Annotated[VatsValueFunction8089, _VARIANT_8089]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8090,
        ]
        | Annotated[_values.FormId, _VARIANT_8091]
        | Annotated[_values.FormId, _VARIANT_8092]
        | Annotated[_values.FormId, _VARIANT_8093]
        | Annotated[PlayerAction8094, _VARIANT_8094]
        | Annotated[CastingType8095, _VARIANT_8095]
        | Annotated[_values.FormId, _VARIANT_8096]
        | Annotated[_values.FormId, _VARIANT_8097]
        | Annotated[_values.FormId, _VARIANT_8098]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8099,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8100,
        ]
        | Annotated[_values.FormId, _VARIANT_8101]
        | Annotated[FurnitureAnim8102, _VARIANT_8102]
        | Annotated[FurnitureEntry8103, _VARIANT_8103]
        | Annotated[_values.FormId, _VARIANT_8104]
        | Annotated[WardState8105, _VARIANT_8105]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8106,
        ]
        | Annotated[_values.FormId, _VARIANT_8107]
        | Annotated[_values.FormId, _VARIANT_8108]
        | Annotated[_values.FormId, _VARIANT_8109]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8111]
        | Annotated[bytes, _VARIANT_8112]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8113,
        ]
        | Annotated[float, _VARIANT_8114]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8115,
        ]
        | Annotated[Sex8116, _VARIANT_8116]
        | Annotated[ActorValue8117, _VARIANT_8117]
        | Annotated[CrimeType8118, _VARIANT_8118]
        | Annotated[Axis8119, _VARIANT_8119]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8120,
        ]
        | Annotated[MiscStat8121, _VARIANT_8121]
        | Annotated[Alignment8122, _VARIANT_8122]
        | Annotated[_values.FormId, _VARIANT_8123]
        | Annotated[FormType8124, _VARIANT_8124]
        | Annotated[CriticalStage8125, _VARIANT_8125]
        | Annotated[_values.FormId, _VARIANT_8126]
        | Annotated[_values.FormId, _VARIANT_8127]
        | Annotated[_values.FormId, _VARIANT_8128]
        | Annotated[_values.FormId, _VARIANT_8129]
        | Annotated[_values.FormId, _VARIANT_8130]
        | Annotated[_values.FormId, _VARIANT_8131]
        | Annotated[_values.FormId, _VARIANT_8132]
        | Annotated[_values.FormId, _VARIANT_8133]
        | Annotated[_values.FormId, _VARIANT_8134]
        | Annotated[_values.FormId, _VARIANT_8135]
        | Annotated[_values.FormId, _VARIANT_8136]
        | Annotated[_values.FormId, _VARIANT_8137]
        | Annotated[_values.FormId, _VARIANT_8138]
        | Annotated[_values.FormId, _VARIANT_8139]
        | Annotated[_values.FormId, _VARIANT_8140]
        | Annotated[_values.FormId, _VARIANT_8141]
        | Annotated[_values.FormId, _VARIANT_8142]
        | Annotated[_values.FormId, _VARIANT_8143]
        | Annotated[_values.FormId, _VARIANT_8144]
        | Annotated[_values.FormId, _VARIANT_8145]
        | Annotated[_values.FormId, _VARIANT_8146]
        | Annotated[_values.FormId, _VARIANT_8147]
        | Annotated[VatsValueFunction8148, _VARIANT_8148]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8150]
            | Annotated[_values.FormId, _VARIANT_8151]
            | Annotated[_values.FormId, _VARIANT_8152]
            | Annotated[_values.FormId, _VARIANT_8153]
            | Annotated[bytes, _VARIANT_8154]
            | Annotated[TargetPart8155, _VARIANT_8155]
            | Annotated[VatsAction8156, _VARIANT_8156]
            | Annotated[bytes, _VARIANT_8157]
            | Annotated[bytes, _VARIANT_8158]
            | Annotated[_values.FormId, _VARIANT_8159]
            | Annotated[_values.FormId, _VARIANT_8160]
            | Annotated[bytes, _VARIANT_8161]
            | Annotated[bytes, _VARIANT_8162]
            | Annotated[bytes, _VARIANT_8163]
            | Annotated[bytes, _VARIANT_8164]
            | Annotated[WeaponType8165, _VARIANT_8165]
            | Annotated[bytes, _VARIANT_8166]
            | Annotated[bytes, _VARIANT_8167]
            | Annotated[ProjectileType8168, _VARIANT_8168]
            | Annotated[DeliveryType8169, _VARIANT_8169]
            | Annotated[CastingType8170, _VARIANT_8170],
            _VARIANT_8149,
        ]
        | Annotated[_values.FormId, _VARIANT_8171]
        | Annotated[_values.FormId, _VARIANT_8172]
        | Annotated[_values.FormId, _VARIANT_8173]
        | Annotated[PlayerAction8174, _VARIANT_8174]
        | Annotated[CastingType8175, _VARIANT_8175]
        | Annotated[_values.FormId, _VARIANT_8176]
        | Annotated[_values.FormId, _VARIANT_8177]
        | Annotated[_values.FormId, _VARIANT_8178]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8179,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8180,
        ]
        | Annotated[_values.FormId, _VARIANT_8181]
        | Annotated[FurnitureAnim8182, _VARIANT_8182]
        | Annotated[FurnitureEntry8183, _VARIANT_8183]
        | Annotated[_values.FormId, _VARIANT_8184]
        | Annotated[WardState8185, _VARIANT_8185]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8186,
        ]
        | Annotated[_values.FormId, _VARIANT_8187]
        | Annotated[_values.FormId, _VARIANT_8188]
        | Annotated[_values.FormId, _VARIANT_8189]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn8190]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8192,
        ]
        | Annotated[_values.FormId, _VARIANT_8193]
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


class Condition8041(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
        "itions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure8043] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure8043]]:
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


class StartConditions8039(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "conditions": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Conditions"
            ),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "SCEN/3:Phases/repeat/0:Phase/2:Start Conditions/0:Cond"
                "itions/repeat/0:Condition"
            ),
            child_kind="sequence",
        ),
    }

    conditions: tuple[Condition8041, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition8041, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_8209: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/2:Compar"
        "ison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_8210: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/2:Compar"
        "ison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_8214: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/0:Unknown"
    )
)


_VARIANT_8215: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/1:None"
    )
)


_VARIANT_8216: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/2:Integer"
    )
)


_VARIANT_8217: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/3:Float"
    )
)


_VARIANT_8218: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/4:Variable Name"
    )
)


class Sex8219(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8219: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/5:Sex"
    )
)


class ActorValue8220(_values.OpenIntEnum):
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


_VARIANT_8220: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/6:Actor Value"
    )
)


class CrimeType8221(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8221: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/7:Crime Type"
    )
)


class Axis8222(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8222: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/8:Axis"
    )
)


_VARIANT_8223: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat8224(_values.OpenIntEnum):
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


_VARIANT_8224: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/10:Misc Stat"
    )
)


class Alignment8225(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8225: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/11:Alignment"
    )
)


_VARIANT_8226: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/12:Equip Type"
    )
)


class FormType8227(_values.OpenIntEnum):
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


_VARIANT_8227: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/13:Form Type"
    )
)


class CriticalStage8228(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8228: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/14:Critical Stage"
    )
)


_VARIANT_8229: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/15:Object Reference"
    )
)


_VARIANT_8230: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/16:Inventory Object"
    )
)


_VARIANT_8231: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/17:Actor"
    )
)


_VARIANT_8232: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/18:Voice Type"
    )
)


_VARIANT_8233: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/19:Idle"
    )
)


_VARIANT_8234: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/20:Form List"
    )
)


_VARIANT_8235: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/21:Quest"
    )
)


_VARIANT_8236: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/22:Faction"
    )
)


_VARIANT_8237: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/23:Cell"
    )
)


_VARIANT_8238: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/24:Class"
    )
)


_VARIANT_8239: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/25:Race"
    )
)


_VARIANT_8240: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/26:Actor Base"
    )
)


_VARIANT_8241: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/27:Global"
    )
)


_VARIANT_8242: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/28:Weather"
    )
)


_VARIANT_8243: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/29:Package"
    )
)


_VARIANT_8244: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_8245: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/31:Perk"
    )
)


_VARIANT_8246: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/32:Owner"
    )
)


_VARIANT_8247: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/33:Furniture"
    )
)


_VARIANT_8248: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/34:Effect Item"
    )
)


_VARIANT_8249: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/35:Base Effect"
    )
)


_VARIANT_8250: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction8251(_values.OpenIntEnum):
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


_VARIANT_8251: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_8252: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_8253: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_8254: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/40:Region"
    )
)


_VARIANT_8255: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/41:Keyword"
    )
)


class PlayerAction8256(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8256: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/42:Player Action"
    )
)


class CastingType8257(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8257: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/43:Casting Type"
    )
)


_VARIANT_8258: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/44:Shout"
    )
)


_VARIANT_8259: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/45:Location"
    )
)


_VARIANT_8260: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_8261: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/47:Alias"
    )
)


_VARIANT_8262: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/48:Packdata ID"
    )
)


_VARIANT_8263: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/49:Association Type"
    )
)


class FurnitureAnim8264(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8264: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8265(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8265: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_8266: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/52:Scene"
    )
)


class WardState8267(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8267: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/53:Ward State"
    )
)


_VARIANT_8268: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/54:Event"
    )
)


_VARIANT_8269: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/55:Event Data"
    )
)


_VARIANT_8270: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/56:Knowable"
    )
)


_VARIANT_8271: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
        "ter #1/variants/57:Faction"
    )
)


_VARIANT_8273: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/0:Unknown"
    )
)


_VARIANT_8274: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/1:None"
    )
)


_VARIANT_8275: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/2:Integer"
    )
)


_VARIANT_8276: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/3:Float"
    )
)


_VARIANT_8277: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/4:Variable Name"
    )
)


class Sex8278(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8278: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/5:Sex"
    )
)


class ActorValue8279(_values.OpenIntEnum):
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


_VARIANT_8279: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/6:Actor Value"
    )
)


class CrimeType8280(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8280: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/7:Crime Type"
    )
)


class Axis8281(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8281: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/8:Axis"
    )
)


_VARIANT_8282: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/9:Quest Stage"
    )
)


class MiscStat8283(_values.OpenIntEnum):
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


_VARIANT_8283: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/10:Misc Stat"
    )
)


class Alignment8284(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8284: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/11:Alignment"
    )
)


_VARIANT_8285: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/12:Equip Type"
    )
)


class FormType8286(_values.OpenIntEnum):
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


_VARIANT_8286: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/13:Form Type"
    )
)


class CriticalStage8287(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8287: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/14:Critical Stage"
    )
)


_VARIANT_8288: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/15:Object Reference"
    )
)


_VARIANT_8289: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/16:Inventory Object"
    )
)


_VARIANT_8290: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/17:Actor"
    )
)


_VARIANT_8291: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/18:Voice Type"
    )
)


_VARIANT_8292: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/19:Idle"
    )
)


_VARIANT_8293: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/20:Form List"
    )
)


_VARIANT_8294: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/21:Quest"
    )
)


_VARIANT_8295: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/22:Faction"
    )
)


_VARIANT_8296: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/23:Cell"
    )
)


_VARIANT_8297: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/24:Class"
    )
)


_VARIANT_8298: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/25:Race"
    )
)


_VARIANT_8299: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/26:Actor Base"
    )
)


_VARIANT_8300: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/27:Global"
    )
)


_VARIANT_8301: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/28:Weather"
    )
)


_VARIANT_8302: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/29:Package"
    )
)


_VARIANT_8303: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_8304: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/31:Perk"
    )
)


_VARIANT_8305: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/32:Owner"
    )
)


_VARIANT_8306: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/33:Furniture"
    )
)


_VARIANT_8307: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/34:Effect Item"
    )
)


_VARIANT_8308: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/35:Base Effect"
    )
)


_VARIANT_8309: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction8310(_values.OpenIntEnum):
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


_VARIANT_8310: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_8312: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/0:Weapon"
    )
)


_VARIANT_8313: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/1:Weapon "
        "List"
    )
)


_VARIANT_8314: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/2:Target"
    )
)


_VARIANT_8315: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/3:Target "
        "List"
    )
)


_VARIANT_8316: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/4:Unknown"
    )
)


class TargetPart8317(_values.OpenIntEnum):
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


_VARIANT_8317: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/5:Target "
        "Part"
    )
)


class VatsAction8318(_values.OpenIntEnum):
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


_VARIANT_8318: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/6:VATS Ac"
        "tion"
    )
)


_VARIANT_8319: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/7:Unknown"
    )
)


_VARIANT_8320: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/8:Unknown"
    )
)


_VARIANT_8321: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/9:Critica"
        "l Effect"
    )
)


_VARIANT_8322: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/10:Critic"
        "al Effect List"
    )
)


_VARIANT_8323: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/11:Unknow"
        "n"
    )
)


_VARIANT_8324: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/12:Unknow"
        "n"
    )
)


_VARIANT_8325: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/13:Unknow"
        "n"
    )
)


_VARIANT_8326: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/14:Unknow"
        "n"
    )
)


class WeaponType8327(_values.OpenIntEnum):
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


_VARIANT_8327: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/15:Weapon"
        " Type"
    )
)


_VARIANT_8328: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/16:Unknow"
        "n"
    )
)


_VARIANT_8329: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/17:Unknow"
        "n"
    )
)


class ProjectileType8330(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_8330: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/18:Projec"
        "tile Type"
    )
)


class DeliveryType8331(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_8331: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/19:Delive"
        "ry Type"
    )
)


class CastingType8332(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_8332: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param/variants/20:Castin"
        "g Type"
    )
)


_VARIANT_8311: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_8333: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_8334: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/40:Region"
    )
)


_VARIANT_8335: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/41:Keyword"
    )
)


class PlayerAction8336(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8336: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/42:Player Action"
    )
)


class CastingType8337(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8337: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/43:Casting Type"
    )
)


_VARIANT_8338: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/44:Shout"
    )
)


_VARIANT_8339: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/45:Location"
    )
)


_VARIANT_8340: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_8341: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/47:Alias"
    )
)


_VARIANT_8342: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/48:Packdata ID"
    )
)


_VARIANT_8343: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/49:Association Type"
    )
)


class FurnitureAnim8344(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8344: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8345(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8345: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_8346: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/52:Scene"
    )
)


class WardState8347(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8347: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/53:Ward State"
    )
)


_VARIANT_8348: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/54:Event"
    )
)


_VARIANT_8349: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/55:Event Data"
    )
)


_VARIANT_8350: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/56:Knowable"
    )
)


_VARIANT_8351: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
        "ter #2/variants/57:Faction"
    )
)


class RunOn8352(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_8354: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/8:Refere"
        "nce/variants/0:Unused"
    )
)


_VARIANT_8355: _base.Variant = _base.Variant(
    path=(
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload/8:Refere"
        "nce/variants/1:Reference"
    )
)


class Structure8205(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/2:Compar"
                "ison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/3:Functi"
                "on"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_8212": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/5:Parame"
                "ter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/6:Parame"
                "ter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/8:Refere"
                "nce"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA/payload/9:Parame"
                "ter #3"
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
        Annotated[float, _VARIANT_8209]
        | Annotated[_values.FormId, _VARIANT_8210]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_8212: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_8214]
        | Annotated[bytes, _VARIANT_8215]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8216,
        ]
        | Annotated[float, _VARIANT_8217]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8218,
        ]
        | Annotated[Sex8219, _VARIANT_8219]
        | Annotated[ActorValue8220, _VARIANT_8220]
        | Annotated[CrimeType8221, _VARIANT_8221]
        | Annotated[Axis8222, _VARIANT_8222]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8223,
        ]
        | Annotated[MiscStat8224, _VARIANT_8224]
        | Annotated[Alignment8225, _VARIANT_8225]
        | Annotated[_values.FormId, _VARIANT_8226]
        | Annotated[FormType8227, _VARIANT_8227]
        | Annotated[CriticalStage8228, _VARIANT_8228]
        | Annotated[_values.FormId, _VARIANT_8229]
        | Annotated[_values.FormId, _VARIANT_8230]
        | Annotated[_values.FormId, _VARIANT_8231]
        | Annotated[_values.FormId, _VARIANT_8232]
        | Annotated[_values.FormId, _VARIANT_8233]
        | Annotated[_values.FormId, _VARIANT_8234]
        | Annotated[_values.FormId, _VARIANT_8235]
        | Annotated[_values.FormId, _VARIANT_8236]
        | Annotated[_values.FormId, _VARIANT_8237]
        | Annotated[_values.FormId, _VARIANT_8238]
        | Annotated[_values.FormId, _VARIANT_8239]
        | Annotated[_values.FormId, _VARIANT_8240]
        | Annotated[_values.FormId, _VARIANT_8241]
        | Annotated[_values.FormId, _VARIANT_8242]
        | Annotated[_values.FormId, _VARIANT_8243]
        | Annotated[_values.FormId, _VARIANT_8244]
        | Annotated[_values.FormId, _VARIANT_8245]
        | Annotated[_values.FormId, _VARIANT_8246]
        | Annotated[_values.FormId, _VARIANT_8247]
        | Annotated[_values.FormId, _VARIANT_8248]
        | Annotated[_values.FormId, _VARIANT_8249]
        | Annotated[_values.FormId, _VARIANT_8250]
        | Annotated[VatsValueFunction8251, _VARIANT_8251]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8252,
        ]
        | Annotated[_values.FormId, _VARIANT_8253]
        | Annotated[_values.FormId, _VARIANT_8254]
        | Annotated[_values.FormId, _VARIANT_8255]
        | Annotated[PlayerAction8256, _VARIANT_8256]
        | Annotated[CastingType8257, _VARIANT_8257]
        | Annotated[_values.FormId, _VARIANT_8258]
        | Annotated[_values.FormId, _VARIANT_8259]
        | Annotated[_values.FormId, _VARIANT_8260]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8261,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8262,
        ]
        | Annotated[_values.FormId, _VARIANT_8263]
        | Annotated[FurnitureAnim8264, _VARIANT_8264]
        | Annotated[FurnitureEntry8265, _VARIANT_8265]
        | Annotated[_values.FormId, _VARIANT_8266]
        | Annotated[WardState8267, _VARIANT_8267]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8268,
        ]
        | Annotated[_values.FormId, _VARIANT_8269]
        | Annotated[_values.FormId, _VARIANT_8270]
        | Annotated[_values.FormId, _VARIANT_8271]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_8273]
        | Annotated[bytes, _VARIANT_8274]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8275,
        ]
        | Annotated[float, _VARIANT_8276]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8277,
        ]
        | Annotated[Sex8278, _VARIANT_8278]
        | Annotated[ActorValue8279, _VARIANT_8279]
        | Annotated[CrimeType8280, _VARIANT_8280]
        | Annotated[Axis8281, _VARIANT_8281]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8282,
        ]
        | Annotated[MiscStat8283, _VARIANT_8283]
        | Annotated[Alignment8284, _VARIANT_8284]
        | Annotated[_values.FormId, _VARIANT_8285]
        | Annotated[FormType8286, _VARIANT_8286]
        | Annotated[CriticalStage8287, _VARIANT_8287]
        | Annotated[_values.FormId, _VARIANT_8288]
        | Annotated[_values.FormId, _VARIANT_8289]
        | Annotated[_values.FormId, _VARIANT_8290]
        | Annotated[_values.FormId, _VARIANT_8291]
        | Annotated[_values.FormId, _VARIANT_8292]
        | Annotated[_values.FormId, _VARIANT_8293]
        | Annotated[_values.FormId, _VARIANT_8294]
        | Annotated[_values.FormId, _VARIANT_8295]
        | Annotated[_values.FormId, _VARIANT_8296]
        | Annotated[_values.FormId, _VARIANT_8297]
        | Annotated[_values.FormId, _VARIANT_8298]
        | Annotated[_values.FormId, _VARIANT_8299]
        | Annotated[_values.FormId, _VARIANT_8300]
        | Annotated[_values.FormId, _VARIANT_8301]
        | Annotated[_values.FormId, _VARIANT_8302]
        | Annotated[_values.FormId, _VARIANT_8303]
        | Annotated[_values.FormId, _VARIANT_8304]
        | Annotated[_values.FormId, _VARIANT_8305]
        | Annotated[_values.FormId, _VARIANT_8306]
        | Annotated[_values.FormId, _VARIANT_8307]
        | Annotated[_values.FormId, _VARIANT_8308]
        | Annotated[_values.FormId, _VARIANT_8309]
        | Annotated[VatsValueFunction8310, _VARIANT_8310]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8312]
            | Annotated[_values.FormId, _VARIANT_8313]
            | Annotated[_values.FormId, _VARIANT_8314]
            | Annotated[_values.FormId, _VARIANT_8315]
            | Annotated[bytes, _VARIANT_8316]
            | Annotated[TargetPart8317, _VARIANT_8317]
            | Annotated[VatsAction8318, _VARIANT_8318]
            | Annotated[bytes, _VARIANT_8319]
            | Annotated[bytes, _VARIANT_8320]
            | Annotated[_values.FormId, _VARIANT_8321]
            | Annotated[_values.FormId, _VARIANT_8322]
            | Annotated[bytes, _VARIANT_8323]
            | Annotated[bytes, _VARIANT_8324]
            | Annotated[bytes, _VARIANT_8325]
            | Annotated[bytes, _VARIANT_8326]
            | Annotated[WeaponType8327, _VARIANT_8327]
            | Annotated[bytes, _VARIANT_8328]
            | Annotated[bytes, _VARIANT_8329]
            | Annotated[ProjectileType8330, _VARIANT_8330]
            | Annotated[DeliveryType8331, _VARIANT_8331]
            | Annotated[CastingType8332, _VARIANT_8332],
            _VARIANT_8311,
        ]
        | Annotated[_values.FormId, _VARIANT_8333]
        | Annotated[_values.FormId, _VARIANT_8334]
        | Annotated[_values.FormId, _VARIANT_8335]
        | Annotated[PlayerAction8336, _VARIANT_8336]
        | Annotated[CastingType8337, _VARIANT_8337]
        | Annotated[_values.FormId, _VARIANT_8338]
        | Annotated[_values.FormId, _VARIANT_8339]
        | Annotated[_values.FormId, _VARIANT_8340]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8341,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8342,
        ]
        | Annotated[_values.FormId, _VARIANT_8343]
        | Annotated[FurnitureAnim8344, _VARIANT_8344]
        | Annotated[FurnitureEntry8345, _VARIANT_8345]
        | Annotated[_values.FormId, _VARIANT_8346]
        | Annotated[WardState8347, _VARIANT_8347]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8348,
        ]
        | Annotated[_values.FormId, _VARIANT_8349]
        | Annotated[_values.FormId, _VARIANT_8350]
        | Annotated[_values.FormId, _VARIANT_8351]
    )
    """Value decoded from this schema node."""

    run_on: RunOn8352
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8354,
        ]
        | Annotated[_values.FormId, _VARIANT_8355]
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
        Annotated[float, _VARIANT_8209]
        | Annotated[_values.FormId, _VARIANT_8210]
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
    def field(self, name: Literal["unused_8212"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8214]
        | Annotated[bytes, _VARIANT_8215]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8216,
        ]
        | Annotated[float, _VARIANT_8217]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8218,
        ]
        | Annotated[Sex8219, _VARIANT_8219]
        | Annotated[ActorValue8220, _VARIANT_8220]
        | Annotated[CrimeType8221, _VARIANT_8221]
        | Annotated[Axis8222, _VARIANT_8222]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8223,
        ]
        | Annotated[MiscStat8224, _VARIANT_8224]
        | Annotated[Alignment8225, _VARIANT_8225]
        | Annotated[_values.FormId, _VARIANT_8226]
        | Annotated[FormType8227, _VARIANT_8227]
        | Annotated[CriticalStage8228, _VARIANT_8228]
        | Annotated[_values.FormId, _VARIANT_8229]
        | Annotated[_values.FormId, _VARIANT_8230]
        | Annotated[_values.FormId, _VARIANT_8231]
        | Annotated[_values.FormId, _VARIANT_8232]
        | Annotated[_values.FormId, _VARIANT_8233]
        | Annotated[_values.FormId, _VARIANT_8234]
        | Annotated[_values.FormId, _VARIANT_8235]
        | Annotated[_values.FormId, _VARIANT_8236]
        | Annotated[_values.FormId, _VARIANT_8237]
        | Annotated[_values.FormId, _VARIANT_8238]
        | Annotated[_values.FormId, _VARIANT_8239]
        | Annotated[_values.FormId, _VARIANT_8240]
        | Annotated[_values.FormId, _VARIANT_8241]
        | Annotated[_values.FormId, _VARIANT_8242]
        | Annotated[_values.FormId, _VARIANT_8243]
        | Annotated[_values.FormId, _VARIANT_8244]
        | Annotated[_values.FormId, _VARIANT_8245]
        | Annotated[_values.FormId, _VARIANT_8246]
        | Annotated[_values.FormId, _VARIANT_8247]
        | Annotated[_values.FormId, _VARIANT_8248]
        | Annotated[_values.FormId, _VARIANT_8249]
        | Annotated[_values.FormId, _VARIANT_8250]
        | Annotated[VatsValueFunction8251, _VARIANT_8251]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8252,
        ]
        | Annotated[_values.FormId, _VARIANT_8253]
        | Annotated[_values.FormId, _VARIANT_8254]
        | Annotated[_values.FormId, _VARIANT_8255]
        | Annotated[PlayerAction8256, _VARIANT_8256]
        | Annotated[CastingType8257, _VARIANT_8257]
        | Annotated[_values.FormId, _VARIANT_8258]
        | Annotated[_values.FormId, _VARIANT_8259]
        | Annotated[_values.FormId, _VARIANT_8260]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8261,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8262,
        ]
        | Annotated[_values.FormId, _VARIANT_8263]
        | Annotated[FurnitureAnim8264, _VARIANT_8264]
        | Annotated[FurnitureEntry8265, _VARIANT_8265]
        | Annotated[_values.FormId, _VARIANT_8266]
        | Annotated[WardState8267, _VARIANT_8267]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8268,
        ]
        | Annotated[_values.FormId, _VARIANT_8269]
        | Annotated[_values.FormId, _VARIANT_8270]
        | Annotated[_values.FormId, _VARIANT_8271]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8273]
        | Annotated[bytes, _VARIANT_8274]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8275,
        ]
        | Annotated[float, _VARIANT_8276]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8277,
        ]
        | Annotated[Sex8278, _VARIANT_8278]
        | Annotated[ActorValue8279, _VARIANT_8279]
        | Annotated[CrimeType8280, _VARIANT_8280]
        | Annotated[Axis8281, _VARIANT_8281]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8282,
        ]
        | Annotated[MiscStat8283, _VARIANT_8283]
        | Annotated[Alignment8284, _VARIANT_8284]
        | Annotated[_values.FormId, _VARIANT_8285]
        | Annotated[FormType8286, _VARIANT_8286]
        | Annotated[CriticalStage8287, _VARIANT_8287]
        | Annotated[_values.FormId, _VARIANT_8288]
        | Annotated[_values.FormId, _VARIANT_8289]
        | Annotated[_values.FormId, _VARIANT_8290]
        | Annotated[_values.FormId, _VARIANT_8291]
        | Annotated[_values.FormId, _VARIANT_8292]
        | Annotated[_values.FormId, _VARIANT_8293]
        | Annotated[_values.FormId, _VARIANT_8294]
        | Annotated[_values.FormId, _VARIANT_8295]
        | Annotated[_values.FormId, _VARIANT_8296]
        | Annotated[_values.FormId, _VARIANT_8297]
        | Annotated[_values.FormId, _VARIANT_8298]
        | Annotated[_values.FormId, _VARIANT_8299]
        | Annotated[_values.FormId, _VARIANT_8300]
        | Annotated[_values.FormId, _VARIANT_8301]
        | Annotated[_values.FormId, _VARIANT_8302]
        | Annotated[_values.FormId, _VARIANT_8303]
        | Annotated[_values.FormId, _VARIANT_8304]
        | Annotated[_values.FormId, _VARIANT_8305]
        | Annotated[_values.FormId, _VARIANT_8306]
        | Annotated[_values.FormId, _VARIANT_8307]
        | Annotated[_values.FormId, _VARIANT_8308]
        | Annotated[_values.FormId, _VARIANT_8309]
        | Annotated[VatsValueFunction8310, _VARIANT_8310]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8312]
            | Annotated[_values.FormId, _VARIANT_8313]
            | Annotated[_values.FormId, _VARIANT_8314]
            | Annotated[_values.FormId, _VARIANT_8315]
            | Annotated[bytes, _VARIANT_8316]
            | Annotated[TargetPart8317, _VARIANT_8317]
            | Annotated[VatsAction8318, _VARIANT_8318]
            | Annotated[bytes, _VARIANT_8319]
            | Annotated[bytes, _VARIANT_8320]
            | Annotated[_values.FormId, _VARIANT_8321]
            | Annotated[_values.FormId, _VARIANT_8322]
            | Annotated[bytes, _VARIANT_8323]
            | Annotated[bytes, _VARIANT_8324]
            | Annotated[bytes, _VARIANT_8325]
            | Annotated[bytes, _VARIANT_8326]
            | Annotated[WeaponType8327, _VARIANT_8327]
            | Annotated[bytes, _VARIANT_8328]
            | Annotated[bytes, _VARIANT_8329]
            | Annotated[ProjectileType8330, _VARIANT_8330]
            | Annotated[DeliveryType8331, _VARIANT_8331]
            | Annotated[CastingType8332, _VARIANT_8332],
            _VARIANT_8311,
        ]
        | Annotated[_values.FormId, _VARIANT_8333]
        | Annotated[_values.FormId, _VARIANT_8334]
        | Annotated[_values.FormId, _VARIANT_8335]
        | Annotated[PlayerAction8336, _VARIANT_8336]
        | Annotated[CastingType8337, _VARIANT_8337]
        | Annotated[_values.FormId, _VARIANT_8338]
        | Annotated[_values.FormId, _VARIANT_8339]
        | Annotated[_values.FormId, _VARIANT_8340]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8341,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8342,
        ]
        | Annotated[_values.FormId, _VARIANT_8343]
        | Annotated[FurnitureAnim8344, _VARIANT_8344]
        | Annotated[FurnitureEntry8345, _VARIANT_8345]
        | Annotated[_values.FormId, _VARIANT_8346]
        | Annotated[WardState8347, _VARIANT_8347]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8348,
        ]
        | Annotated[_values.FormId, _VARIANT_8349]
        | Annotated[_values.FormId, _VARIANT_8350]
        | Annotated[_values.FormId, _VARIANT_8351]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn8352]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8354,
        ]
        | Annotated[_values.FormId, _VARIANT_8355]
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


class Condition8203(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
        ":Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure8205] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure8205]]:
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


class CompletionConditions8201(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "conditions": _base.Binding(
            path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions"
            ),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions/0"
                ":Conditions/repeat/0:Condition"
            ),
            child_kind="sequence",
        ),
    }

    conditions: tuple[Condition8203, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition8203, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Unused8361(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/3:Phases/repeat/0:Phase/5:Unused"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/5:Unused/0:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8364": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/5:Unused/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8366": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/5:Unused/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8368": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/5:Unused/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8370": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/5:Unused/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8364: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8366: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8368: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8370: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8364"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8366"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8368"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8370"]
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


class Unused8374(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/3:Phases/repeat/0:Phase/7:Unused"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/7:Unused/0:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8377": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/7:Unused/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8379": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/7:Unused/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8381": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/7:Unused/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8383": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/7:Unused/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8377: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8379: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8381: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8383: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8377"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8379"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8381"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8383"]
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


class Phase8034(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/3:Phases/repeat/0:Phase"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "marker_phase_start": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/0:Marker Phase Start",
            kind="subrecord",
            name="Marker Phase Start",
        ),
        "name": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "start_conditions": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/2:Start Conditions",
            kind="sequence",
            name="Start Conditions",
        ),
        "marker": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/3:Marker",
            kind="subrecord",
            name="Marker",
        ),
        "completion_conditions": _base.Binding(
            path=("SCEN/3:Phases/repeat/0:Phase/4:Completion Conditions"),
            kind="sequence",
            name="Completion Conditions",
        ),
        "unused": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/5:Unused",
            kind="sequence",
            name="Unused",
        ),
        "marker_8372": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/6:Marker",
            kind="subrecord",
            name="Marker",
        ),
        "unused_8374": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/7:Unused",
            kind="sequence",
            name="Unused",
        ),
        "editor_width": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/8:Editor Width",
            kind="subrecord",
            name="Editor Width",
        ),
        "marker_phase_end": _base.Binding(
            path="SCEN/3:Phases/repeat/0:Phase/9:Marker Phase End",
            kind="subrecord",
            name="Marker Phase End",
        ),
    }

    marker_phase_start: Optional[bytes] = None
    """Value decoded from this schema node."""

    name: Optional[str] = None
    """Value decoded from this schema node."""

    start_conditions: Optional[StartConditions8039] = None
    """Value decoded from this schema node."""

    marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    completion_conditions: Optional[CompletionConditions8201] = None
    """Value decoded from this schema node."""

    unused: Optional[Unused8361] = None
    """Value decoded from this schema node."""

    marker_8372: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_8374: Optional[Unused8374] = None
    """Value decoded from this schema node."""

    editor_width: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    marker_phase_end: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["marker_phase_start"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["name"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["start_conditions"]
    ) -> _base.FieldRef[Optional[StartConditions8039]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["marker"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["completion_conditions"]
    ) -> _base.FieldRef[Optional[CompletionConditions8201]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[Optional[Unused8361]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["marker_8372"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_8374"]
    ) -> _base.FieldRef[Optional[Unused8374]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["editor_width"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["marker_phase_end"]
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


class NoPlayerActivationOptional8394(enum.IntFlag):
    """Named values from the pinned schema."""

    NO_PLAYER_ACTIVATION = 1
    OPTIONAL = 2


class DeathPauseUnsusedDeathEndCombatPauseCo45F816918396(enum.IntFlag):
    """Named values from the pinned schema."""

    DEATH_PAUSE_UNSUSED = 1
    DEATH_END = 2
    COMBAT_PAUSE = 4
    COMBAT_END = 8
    DIALOGUE_PAUSE = 16
    DIALOGUE_END = 32
    OBS_COM_PAUSE = 64
    OBS_COM_END = 128


class Actor8390(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/4:Actors/repeat/0:Actor"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "actor_id": _base.Binding(
            path="SCEN/4:Actors/repeat/0:Actor/0:Actor ID",
            kind="subrecord",
            name="Actor ID",
        ),
        "flags": _base.Binding(
            path="SCEN/4:Actors/repeat/0:Actor/1:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "behaviour_flags": _base.Binding(
            path="SCEN/4:Actors/repeat/0:Actor/2:Behaviour Flags",
            kind="subrecord",
            name="Behaviour Flags",
        ),
    }

    actor_id: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    flags: Optional[NoPlayerActivationOptional8394] = None
    """Value decoded from this schema node."""

    behaviour_flags: Optional[
        DeathPauseUnsusedDeathEndCombatPauseCo45F816918396
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["actor_id"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[NoPlayerActivationOptional8394]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["behaviour_flags"]
    ) -> _base.FieldRef[
        Optional[DeathPauseUnsusedDeathEndCombatPauseCo45F816918396]
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


class DialoguePackageTimer8400(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    DIALOGUE = 0
    PACKAGE = 1
    TIMER = 2


class Unknown1Unknown2Unknown3Unknown4Unkno14E3F71D8410(enum.IntFlag):
    """Named values from the pinned schema."""

    UNKNOWN_1 = 1
    UNKNOWN_2 = 2
    UNKNOWN_3 = 4
    UNKNOWN_4 = 8
    UNKNOWN_5 = 16
    UNKNOWN_6 = 32
    UNKNOWN_7 = 64
    UNKNOWN_8 = 128
    UNKNOWN_9 = 256
    UNKNOWN_10 = 512
    UNKNOWN_11 = 1024
    UNKNOWN_12 = 2048
    UNKNOWN_13 = 4096
    UNKNOWN_14 = 8192
    UNKNOWN_15 = 16384
    FACE_TARGET = 32768
    LOOPING = 65536
    HEADTRACK_PLAYER = 131072


class NeutralAngerDisgustFearSadHappySurprisePuzzled8426(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NEUTRAL = 0
    ANGER = 1
    DISGUST = 2
    FEAR = 3
    SAD = 4
    HAPPY = 5
    SURPRISE = 6
    PUZZLED = 7


class Dialogue8416(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/0:Dialogue"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "topic": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "0:Dialogue/0:Topic"
            ),
            kind="subrecord",
            name="Topic",
        ),
        "headtrack_actor_id": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "0:Dialogue/1:Headtrack Actor ID"
            ),
            kind="subrecord",
            name="Headtrack Actor ID",
        ),
        "looping_max": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "0:Dialogue/2:Looping - Max"
            ),
            kind="subrecord",
            name="Looping - Max",
        ),
        "looping_min": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "0:Dialogue/3:Looping - Min"
            ),
            kind="subrecord",
            name="Looping - Min",
        ),
        "emotion_type": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "0:Dialogue/4:Emotion Type"
            ),
            kind="subrecord",
            name="Emotion Type",
        ),
        "emotion_value": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "0:Dialogue/5:Emotion Value"
            ),
            kind="subrecord",
            name="Emotion Value",
        ),
    }

    topic: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    headtrack_actor_id: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    looping_max: Optional[float] = None
    """Value decoded from this schema node."""

    looping_min: Optional[float] = None
    """Value decoded from this schema node."""

    emotion_type: Optional[
        NeutralAngerDisgustFearSadHappySurprisePuzzled8426
    ] = None
    """Value decoded from this schema node."""

    emotion_value: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["headtrack_actor_id"]
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
    def field(
        self, name: Literal["looping_max"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["looping_min"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["emotion_type"]
    ) -> _base.FieldRef[
        Optional[NeutralAngerDisgustFearSadHappySurprisePuzzled8426]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["emotion_value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


_VARIANT_8416: _base.Variant = _base.Variant(
    path=("SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/0:Dialogue")
)


class Package8429(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/1:Package"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "packages": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "1:Package/0:Packages"
            ),
            kind="repeat",
            name="Packages",
            repeated_path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "1:Package/0:Packages/repeat/0:Package"
            ),
            child_kind="subrecord",
        ),
    }

    packages: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["packages"]
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


_VARIANT_8429: _base.Variant = _base.Variant(
    path=("SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/1:Package")
)


class Timer8433(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/2:Timer"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "duration_seconds": _base.Binding(
            path=(
                "SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/"
                "2:Timer/0:Duration (Seconds)"
            ),
            kind="subrecord",
            name="Duration (Seconds)",
        ),
    }

    duration_seconds: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["duration_seconds"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_8433: _base.Variant = _base.Variant(
    path=("SCEN/5:Actions/repeat/0:Action/8:Type Specific Action/2:Timer")
)


class Unused8436(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/5:Actions/repeat/0:Action/9:Unused"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/9:Unused/0:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8439": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/9:Unused/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8441": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/9:Unused/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8443": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/9:Unused/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8445": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/9:Unused/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8439: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8441: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8443: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8445: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8439"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8441"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8443"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8445"]
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


class Action8398(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/5:Actions/repeat/0:Action"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/0:Type",
            kind="subrecord",
            name="Type",
        ),
        "name": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "actor_id": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/2:Actor ID",
            kind="subrecord",
            name="Actor ID",
        ),
        "unknown": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "index": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/4:Index",
            kind="subrecord",
            name="Index",
        ),
        "flags": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/5:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "start_phase": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/6:Start Phase",
            kind="subrecord",
            name="Start Phase",
        ),
        "end_phase": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/7:End Phase",
            kind="subrecord",
            name="End Phase",
        ),
        "type_specific_action": _base.Binding(
            path=("SCEN/5:Actions/repeat/0:Action/8:Type Specific Action"),
            kind="selected_choice",
            name="Type Specific Action",
        ),
        "unused": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/9:Unused",
            kind="sequence",
            name="Unused",
        ),
        "marker": _base.Binding(
            path="SCEN/5:Actions/repeat/0:Action/10:Marker",
            kind="subrecord",
            name="Marker",
        ),
    }

    type: Optional[DialoguePackageTimer8400] = None
    """Value decoded from this schema node."""

    name: Optional[str] = None
    """Value decoded from this schema node."""

    actor_id: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    flags: Optional[Unknown1Unknown2Unknown3Unknown4Unkno14E3F71D8410] = None
    """Value decoded from this schema node."""

    start_phase: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    end_phase: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    type_specific_action: Optional[
        Annotated[Dialogue8416, _VARIANT_8416]
        | Annotated[Package8429, _VARIANT_8429]
        | Annotated[Timer8433, _VARIANT_8433]
    ] = None
    """Value decoded from this schema node."""

    unused: Optional[Unused8436] = None
    """Value decoded from this schema node."""

    marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["type"]
    ) -> _base.FieldRef[Optional[DialoguePackageTimer8400]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["name"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actor_id"]
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
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["index"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[Unknown1Unknown2Unknown3Unknown4Unkno14E3F71D8410]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["start_phase"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["end_phase"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["type_specific_action"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[Dialogue8416, _VARIANT_8416]
            | Annotated[Package8429, _VARIANT_8429]
            | Annotated[Timer8433, _VARIANT_8433]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[Optional[Unused8436]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["marker"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Unused8449(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/6:Unused"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="SCEN/6:Unused/0:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8452": _base.Binding(
            path="SCEN/6:Unused/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8454": _base.Binding(
            path="SCEN/6:Unused/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8456": _base.Binding(
            path="SCEN/6:Unused/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8458": _base.Binding(
            path="SCEN/6:Unused/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8452: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8454: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8456: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8458: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8452"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8454"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8456"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8458"]
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


class Unused8462(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/8:Unused"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="SCEN/8:Unused/0:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8465": _base.Binding(
            path="SCEN/8:Unused/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8467": _base.Binding(
            path="SCEN/8:Unused/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8469": _base.Binding(
            path="SCEN/8:Unused/3:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_8471": _base.Binding(
            path="SCEN/8:Unused/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8465: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8467: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8469: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_8471: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8465"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8467"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8469"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_8471"]
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


class Death8479(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SET_ALL_NORMAL = 0
    SET_ALL_END = 2
    DON_T_SET_ALL = 3


class Combat8480(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SET_ALL_NORMAL = 0
    SET_ALL_PAUSE = 1
    SET_ALL_END = 2
    DON_T_SET_ALL = 3


class Dialogue8481(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SET_ALL_NORMAL = 0
    SET_ALL_PAUSE = 1
    SET_ALL_END = 2
    DON_T_SET_ALL = 3


class ObserveCombat8482(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SET_ALL_NORMAL = 0
    SET_ALL_PAUSE = 1
    SET_ALL_END = 2
    DON_T_SET_ALL = 3


class Structure8478(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/11:Actor Behavior Settings/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "death": _base.Binding(
            path="SCEN/11:Actor Behavior Settings/payload/0:Death",
            kind="primitive",
            name="Death",
        ),
        "combat": _base.Binding(
            path="SCEN/11:Actor Behavior Settings/payload/1:Combat",
            kind="primitive",
            name="Combat",
        ),
        "dialogue": _base.Binding(
            path=("SCEN/11:Actor Behavior Settings/payload/2:Dialogue"),
            kind="primitive",
            name="Dialogue",
        ),
        "observe_combat": _base.Binding(
            path=("SCEN/11:Actor Behavior Settings/payload/3:Observe Combat"),
            kind="primitive",
            name="Observe Combat",
        ),
    }

    death: Death8479
    """Value decoded from this schema node."""

    combat: Combat8480
    """Value decoded from this schema node."""

    dialogue: Dialogue8481
    """Value decoded from this schema node."""

    observe_combat: ObserveCombat8482
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["death"]) -> _base.FieldRef[Death8479]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["combat"]) -> _base.FieldRef[Combat8480]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["dialogue"]) -> _base.FieldRef[Dialogue8481]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["observe_combat"]
    ) -> _base.FieldRef[ObserveCombat8482]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_8490: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_8491: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_8495: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_8496: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/1:None"
    )
)


_VARIANT_8497: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/2:Integer"
    )
)


_VARIANT_8498: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/3:Float"
    )
)


_VARIANT_8499: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/4:Variable Name"
    )
)


class Sex8500(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8500: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/5:Sex"
    )
)


class ActorValue8501(_values.OpenIntEnum):
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


_VARIANT_8501: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType8502(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8502: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/7:Crime Type"
    )
)


class Axis8503(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8503: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/8:Axis"
    )
)


_VARIANT_8504: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat8505(_values.OpenIntEnum):
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


_VARIANT_8505: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment8506(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8506: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_8507: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/12:Equip Type"
    )
)


class FormType8508(_values.OpenIntEnum):
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


_VARIANT_8508: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage8509(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8509: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_8510: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_8511: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_8512: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/17:Actor"
    )
)


_VARIANT_8513: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_8514: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/19:Idle"
    )
)


_VARIANT_8515: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/20:Form List"
    )
)


_VARIANT_8516: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/21:Quest"
    )
)


_VARIANT_8517: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/22:Faction"
    )
)


_VARIANT_8518: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/23:Cell"
    )
)


_VARIANT_8519: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/24:Class"
    )
)


_VARIANT_8520: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/25:Race"
    )
)


_VARIANT_8521: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_8522: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/27:Global"
    )
)


_VARIANT_8523: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/28:Weather"
    )
)


_VARIANT_8524: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/29:Package"
    )
)


_VARIANT_8525: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_8526: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/31:Perk"
    )
)


_VARIANT_8527: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/32:Owner"
    )
)


_VARIANT_8528: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_8529: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_8530: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_8531: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction8532(_values.OpenIntEnum):
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


_VARIANT_8532: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_8533: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_8534: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_8535: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/40:Region"
    )
)


_VARIANT_8536: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction8537(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8537: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/42:Player Action"
    )
)


class CastingType8538(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8538: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_8539: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/44:Shout"
    )
)


_VARIANT_8540: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/45:Location"
    )
)


_VARIANT_8541: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_8542: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/47:Alias"
    )
)


_VARIANT_8543: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_8544: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim8545(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8545: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8546(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8546: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_8547: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/52:Scene"
    )
)


class WardState8548(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8548: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_8549: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/54:Event"
    )
)


_VARIANT_8550: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_8551: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_8552: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/57:Faction"
    )
)


_VARIANT_8554: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_8555: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/1:None"
    )
)


_VARIANT_8556: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/2:Integer"
    )
)


_VARIANT_8557: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/3:Float"
    )
)


_VARIANT_8558: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/4:Variable Name"
    )
)


class Sex8559(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_8559: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/5:Sex"
    )
)


class ActorValue8560(_values.OpenIntEnum):
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


_VARIANT_8560: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType8561(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_8561: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/7:Crime Type"
    )
)


class Axis8562(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_8562: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/8:Axis"
    )
)


_VARIANT_8563: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat8564(_values.OpenIntEnum):
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


_VARIANT_8564: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment8565(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_8565: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_8566: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/12:Equip Type"
    )
)


class FormType8567(_values.OpenIntEnum):
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


_VARIANT_8567: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage8568(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_8568: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_8569: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_8570: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_8571: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/17:Actor"
    )
)


_VARIANT_8572: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_8573: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/19:Idle"
    )
)


_VARIANT_8574: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/20:Form List"
    )
)


_VARIANT_8575: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/21:Quest"
    )
)


_VARIANT_8576: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/22:Faction"
    )
)


_VARIANT_8577: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/23:Cell"
    )
)


_VARIANT_8578: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/24:Class"
    )
)


_VARIANT_8579: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/25:Race"
    )
)


_VARIANT_8580: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_8581: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/27:Global"
    )
)


_VARIANT_8582: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/28:Weather"
    )
)


_VARIANT_8583: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/29:Package"
    )
)


_VARIANT_8584: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_8585: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/31:Perk"
    )
)


_VARIANT_8586: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/32:Owner"
    )
)


_VARIANT_8587: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_8588: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_8589: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_8590: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction8591(_values.OpenIntEnum):
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


_VARIANT_8591: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_8593: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/0:"
        "Weapon"
    )
)


_VARIANT_8594: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/1:"
        "Weapon List"
    )
)


_VARIANT_8595: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/2:"
        "Target"
    )
)


_VARIANT_8596: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/3:"
        "Target List"
    )
)


_VARIANT_8597: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/4:"
        "Unknown"
    )
)


class TargetPart8598(_values.OpenIntEnum):
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


_VARIANT_8598: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/5:"
        "Target Part"
    )
)


class VatsAction8599(_values.OpenIntEnum):
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


_VARIANT_8599: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/6:"
        "VATS Action"
    )
)


_VARIANT_8600: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/7:"
        "Unknown"
    )
)


_VARIANT_8601: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/8:"
        "Unknown"
    )
)


_VARIANT_8602: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/9:"
        "Critical Effect"
    )
)


_VARIANT_8603: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/10"
        ":Critical Effect List"
    )
)


_VARIANT_8604: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/11"
        ":Unknown"
    )
)


_VARIANT_8605: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/12"
        ":Unknown"
    )
)


_VARIANT_8606: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/13"
        ":Unknown"
    )
)


_VARIANT_8607: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/14"
        ":Unknown"
    )
)


class WeaponType8608(_values.OpenIntEnum):
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


_VARIANT_8608: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/15"
        ":Weapon Type"
    )
)


_VARIANT_8609: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/16"
        ":Unknown"
    )
)


_VARIANT_8610: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/17"
        ":Unknown"
    )
)


class ProjectileType8611(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_8611: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/18"
        ":Projectile Type"
    )
)


class DeliveryType8612(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_8612: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/19"
        ":Delivery Type"
    )
)


class CastingType8613(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_8613: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/20"
        ":Casting Type"
    )
)


_VARIANT_8592: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_8614: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_8615: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/40:Region"
    )
)


_VARIANT_8616: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction8617(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_8617: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/42:Player Action"
    )
)


class CastingType8618(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_8618: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_8619: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/44:Shout"
    )
)


_VARIANT_8620: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/45:Location"
    )
)


_VARIANT_8621: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_8622: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/47:Alias"
    )
)


_VARIANT_8623: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_8624: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim8625(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_8625: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry8626(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_8626: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_8627: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/52:Scene"
    )
)


class WardState8628(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_8628: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_8629: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/54:Event"
    )
)


_VARIANT_8630: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_8631: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_8632: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/57:Faction"
    )
)


class RunOn8633(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_8635: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/0:Unused"
    )
)


_VARIANT_8636: _base.Variant = _base.Variant(
    path=(
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/1:Reference"
    )
)


class Structure8486(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/2"
                ":Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/3"
                ":Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_8493": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/5"
                ":Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/6"
                ":Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/8"
                ":Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "SCEN/12:Conditions/repeat/0:Condition/0:CTDA/payload/9"
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
        Annotated[float, _VARIANT_8490]
        | Annotated[_values.FormId, _VARIANT_8491]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_8493: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_8495]
        | Annotated[bytes, _VARIANT_8496]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8497,
        ]
        | Annotated[float, _VARIANT_8498]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8499,
        ]
        | Annotated[Sex8500, _VARIANT_8500]
        | Annotated[ActorValue8501, _VARIANT_8501]
        | Annotated[CrimeType8502, _VARIANT_8502]
        | Annotated[Axis8503, _VARIANT_8503]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8504,
        ]
        | Annotated[MiscStat8505, _VARIANT_8505]
        | Annotated[Alignment8506, _VARIANT_8506]
        | Annotated[_values.FormId, _VARIANT_8507]
        | Annotated[FormType8508, _VARIANT_8508]
        | Annotated[CriticalStage8509, _VARIANT_8509]
        | Annotated[_values.FormId, _VARIANT_8510]
        | Annotated[_values.FormId, _VARIANT_8511]
        | Annotated[_values.FormId, _VARIANT_8512]
        | Annotated[_values.FormId, _VARIANT_8513]
        | Annotated[_values.FormId, _VARIANT_8514]
        | Annotated[_values.FormId, _VARIANT_8515]
        | Annotated[_values.FormId, _VARIANT_8516]
        | Annotated[_values.FormId, _VARIANT_8517]
        | Annotated[_values.FormId, _VARIANT_8518]
        | Annotated[_values.FormId, _VARIANT_8519]
        | Annotated[_values.FormId, _VARIANT_8520]
        | Annotated[_values.FormId, _VARIANT_8521]
        | Annotated[_values.FormId, _VARIANT_8522]
        | Annotated[_values.FormId, _VARIANT_8523]
        | Annotated[_values.FormId, _VARIANT_8524]
        | Annotated[_values.FormId, _VARIANT_8525]
        | Annotated[_values.FormId, _VARIANT_8526]
        | Annotated[_values.FormId, _VARIANT_8527]
        | Annotated[_values.FormId, _VARIANT_8528]
        | Annotated[_values.FormId, _VARIANT_8529]
        | Annotated[_values.FormId, _VARIANT_8530]
        | Annotated[_values.FormId, _VARIANT_8531]
        | Annotated[VatsValueFunction8532, _VARIANT_8532]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8533,
        ]
        | Annotated[_values.FormId, _VARIANT_8534]
        | Annotated[_values.FormId, _VARIANT_8535]
        | Annotated[_values.FormId, _VARIANT_8536]
        | Annotated[PlayerAction8537, _VARIANT_8537]
        | Annotated[CastingType8538, _VARIANT_8538]
        | Annotated[_values.FormId, _VARIANT_8539]
        | Annotated[_values.FormId, _VARIANT_8540]
        | Annotated[_values.FormId, _VARIANT_8541]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8542,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8543,
        ]
        | Annotated[_values.FormId, _VARIANT_8544]
        | Annotated[FurnitureAnim8545, _VARIANT_8545]
        | Annotated[FurnitureEntry8546, _VARIANT_8546]
        | Annotated[_values.FormId, _VARIANT_8547]
        | Annotated[WardState8548, _VARIANT_8548]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8549,
        ]
        | Annotated[_values.FormId, _VARIANT_8550]
        | Annotated[_values.FormId, _VARIANT_8551]
        | Annotated[_values.FormId, _VARIANT_8552]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_8554]
        | Annotated[bytes, _VARIANT_8555]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8556,
        ]
        | Annotated[float, _VARIANT_8557]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8558,
        ]
        | Annotated[Sex8559, _VARIANT_8559]
        | Annotated[ActorValue8560, _VARIANT_8560]
        | Annotated[CrimeType8561, _VARIANT_8561]
        | Annotated[Axis8562, _VARIANT_8562]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8563,
        ]
        | Annotated[MiscStat8564, _VARIANT_8564]
        | Annotated[Alignment8565, _VARIANT_8565]
        | Annotated[_values.FormId, _VARIANT_8566]
        | Annotated[FormType8567, _VARIANT_8567]
        | Annotated[CriticalStage8568, _VARIANT_8568]
        | Annotated[_values.FormId, _VARIANT_8569]
        | Annotated[_values.FormId, _VARIANT_8570]
        | Annotated[_values.FormId, _VARIANT_8571]
        | Annotated[_values.FormId, _VARIANT_8572]
        | Annotated[_values.FormId, _VARIANT_8573]
        | Annotated[_values.FormId, _VARIANT_8574]
        | Annotated[_values.FormId, _VARIANT_8575]
        | Annotated[_values.FormId, _VARIANT_8576]
        | Annotated[_values.FormId, _VARIANT_8577]
        | Annotated[_values.FormId, _VARIANT_8578]
        | Annotated[_values.FormId, _VARIANT_8579]
        | Annotated[_values.FormId, _VARIANT_8580]
        | Annotated[_values.FormId, _VARIANT_8581]
        | Annotated[_values.FormId, _VARIANT_8582]
        | Annotated[_values.FormId, _VARIANT_8583]
        | Annotated[_values.FormId, _VARIANT_8584]
        | Annotated[_values.FormId, _VARIANT_8585]
        | Annotated[_values.FormId, _VARIANT_8586]
        | Annotated[_values.FormId, _VARIANT_8587]
        | Annotated[_values.FormId, _VARIANT_8588]
        | Annotated[_values.FormId, _VARIANT_8589]
        | Annotated[_values.FormId, _VARIANT_8590]
        | Annotated[VatsValueFunction8591, _VARIANT_8591]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8593]
            | Annotated[_values.FormId, _VARIANT_8594]
            | Annotated[_values.FormId, _VARIANT_8595]
            | Annotated[_values.FormId, _VARIANT_8596]
            | Annotated[bytes, _VARIANT_8597]
            | Annotated[TargetPart8598, _VARIANT_8598]
            | Annotated[VatsAction8599, _VARIANT_8599]
            | Annotated[bytes, _VARIANT_8600]
            | Annotated[bytes, _VARIANT_8601]
            | Annotated[_values.FormId, _VARIANT_8602]
            | Annotated[_values.FormId, _VARIANT_8603]
            | Annotated[bytes, _VARIANT_8604]
            | Annotated[bytes, _VARIANT_8605]
            | Annotated[bytes, _VARIANT_8606]
            | Annotated[bytes, _VARIANT_8607]
            | Annotated[WeaponType8608, _VARIANT_8608]
            | Annotated[bytes, _VARIANT_8609]
            | Annotated[bytes, _VARIANT_8610]
            | Annotated[ProjectileType8611, _VARIANT_8611]
            | Annotated[DeliveryType8612, _VARIANT_8612]
            | Annotated[CastingType8613, _VARIANT_8613],
            _VARIANT_8592,
        ]
        | Annotated[_values.FormId, _VARIANT_8614]
        | Annotated[_values.FormId, _VARIANT_8615]
        | Annotated[_values.FormId, _VARIANT_8616]
        | Annotated[PlayerAction8617, _VARIANT_8617]
        | Annotated[CastingType8618, _VARIANT_8618]
        | Annotated[_values.FormId, _VARIANT_8619]
        | Annotated[_values.FormId, _VARIANT_8620]
        | Annotated[_values.FormId, _VARIANT_8621]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8622,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8623,
        ]
        | Annotated[_values.FormId, _VARIANT_8624]
        | Annotated[FurnitureAnim8625, _VARIANT_8625]
        | Annotated[FurnitureEntry8626, _VARIANT_8626]
        | Annotated[_values.FormId, _VARIANT_8627]
        | Annotated[WardState8628, _VARIANT_8628]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8629,
        ]
        | Annotated[_values.FormId, _VARIANT_8630]
        | Annotated[_values.FormId, _VARIANT_8631]
        | Annotated[_values.FormId, _VARIANT_8632]
    )
    """Value decoded from this schema node."""

    run_on: RunOn8633
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8635,
        ]
        | Annotated[_values.FormId, _VARIANT_8636]
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
        Annotated[float, _VARIANT_8490]
        | Annotated[_values.FormId, _VARIANT_8491]
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
    def field(self, name: Literal["unused_8493"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8495]
        | Annotated[bytes, _VARIANT_8496]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8497,
        ]
        | Annotated[float, _VARIANT_8498]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8499,
        ]
        | Annotated[Sex8500, _VARIANT_8500]
        | Annotated[ActorValue8501, _VARIANT_8501]
        | Annotated[CrimeType8502, _VARIANT_8502]
        | Annotated[Axis8503, _VARIANT_8503]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8504,
        ]
        | Annotated[MiscStat8505, _VARIANT_8505]
        | Annotated[Alignment8506, _VARIANT_8506]
        | Annotated[_values.FormId, _VARIANT_8507]
        | Annotated[FormType8508, _VARIANT_8508]
        | Annotated[CriticalStage8509, _VARIANT_8509]
        | Annotated[_values.FormId, _VARIANT_8510]
        | Annotated[_values.FormId, _VARIANT_8511]
        | Annotated[_values.FormId, _VARIANT_8512]
        | Annotated[_values.FormId, _VARIANT_8513]
        | Annotated[_values.FormId, _VARIANT_8514]
        | Annotated[_values.FormId, _VARIANT_8515]
        | Annotated[_values.FormId, _VARIANT_8516]
        | Annotated[_values.FormId, _VARIANT_8517]
        | Annotated[_values.FormId, _VARIANT_8518]
        | Annotated[_values.FormId, _VARIANT_8519]
        | Annotated[_values.FormId, _VARIANT_8520]
        | Annotated[_values.FormId, _VARIANT_8521]
        | Annotated[_values.FormId, _VARIANT_8522]
        | Annotated[_values.FormId, _VARIANT_8523]
        | Annotated[_values.FormId, _VARIANT_8524]
        | Annotated[_values.FormId, _VARIANT_8525]
        | Annotated[_values.FormId, _VARIANT_8526]
        | Annotated[_values.FormId, _VARIANT_8527]
        | Annotated[_values.FormId, _VARIANT_8528]
        | Annotated[_values.FormId, _VARIANT_8529]
        | Annotated[_values.FormId, _VARIANT_8530]
        | Annotated[_values.FormId, _VARIANT_8531]
        | Annotated[VatsValueFunction8532, _VARIANT_8532]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8533,
        ]
        | Annotated[_values.FormId, _VARIANT_8534]
        | Annotated[_values.FormId, _VARIANT_8535]
        | Annotated[_values.FormId, _VARIANT_8536]
        | Annotated[PlayerAction8537, _VARIANT_8537]
        | Annotated[CastingType8538, _VARIANT_8538]
        | Annotated[_values.FormId, _VARIANT_8539]
        | Annotated[_values.FormId, _VARIANT_8540]
        | Annotated[_values.FormId, _VARIANT_8541]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8542,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8543,
        ]
        | Annotated[_values.FormId, _VARIANT_8544]
        | Annotated[FurnitureAnim8545, _VARIANT_8545]
        | Annotated[FurnitureEntry8546, _VARIANT_8546]
        | Annotated[_values.FormId, _VARIANT_8547]
        | Annotated[WardState8548, _VARIANT_8548]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8549,
        ]
        | Annotated[_values.FormId, _VARIANT_8550]
        | Annotated[_values.FormId, _VARIANT_8551]
        | Annotated[_values.FormId, _VARIANT_8552]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_8554]
        | Annotated[bytes, _VARIANT_8555]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8556,
        ]
        | Annotated[float, _VARIANT_8557]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8558,
        ]
        | Annotated[Sex8559, _VARIANT_8559]
        | Annotated[ActorValue8560, _VARIANT_8560]
        | Annotated[CrimeType8561, _VARIANT_8561]
        | Annotated[Axis8562, _VARIANT_8562]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8563,
        ]
        | Annotated[MiscStat8564, _VARIANT_8564]
        | Annotated[Alignment8565, _VARIANT_8565]
        | Annotated[_values.FormId, _VARIANT_8566]
        | Annotated[FormType8567, _VARIANT_8567]
        | Annotated[CriticalStage8568, _VARIANT_8568]
        | Annotated[_values.FormId, _VARIANT_8569]
        | Annotated[_values.FormId, _VARIANT_8570]
        | Annotated[_values.FormId, _VARIANT_8571]
        | Annotated[_values.FormId, _VARIANT_8572]
        | Annotated[_values.FormId, _VARIANT_8573]
        | Annotated[_values.FormId, _VARIANT_8574]
        | Annotated[_values.FormId, _VARIANT_8575]
        | Annotated[_values.FormId, _VARIANT_8576]
        | Annotated[_values.FormId, _VARIANT_8577]
        | Annotated[_values.FormId, _VARIANT_8578]
        | Annotated[_values.FormId, _VARIANT_8579]
        | Annotated[_values.FormId, _VARIANT_8580]
        | Annotated[_values.FormId, _VARIANT_8581]
        | Annotated[_values.FormId, _VARIANT_8582]
        | Annotated[_values.FormId, _VARIANT_8583]
        | Annotated[_values.FormId, _VARIANT_8584]
        | Annotated[_values.FormId, _VARIANT_8585]
        | Annotated[_values.FormId, _VARIANT_8586]
        | Annotated[_values.FormId, _VARIANT_8587]
        | Annotated[_values.FormId, _VARIANT_8588]
        | Annotated[_values.FormId, _VARIANT_8589]
        | Annotated[_values.FormId, _VARIANT_8590]
        | Annotated[VatsValueFunction8591, _VARIANT_8591]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_8593]
            | Annotated[_values.FormId, _VARIANT_8594]
            | Annotated[_values.FormId, _VARIANT_8595]
            | Annotated[_values.FormId, _VARIANT_8596]
            | Annotated[bytes, _VARIANT_8597]
            | Annotated[TargetPart8598, _VARIANT_8598]
            | Annotated[VatsAction8599, _VARIANT_8599]
            | Annotated[bytes, _VARIANT_8600]
            | Annotated[bytes, _VARIANT_8601]
            | Annotated[_values.FormId, _VARIANT_8602]
            | Annotated[_values.FormId, _VARIANT_8603]
            | Annotated[bytes, _VARIANT_8604]
            | Annotated[bytes, _VARIANT_8605]
            | Annotated[bytes, _VARIANT_8606]
            | Annotated[bytes, _VARIANT_8607]
            | Annotated[WeaponType8608, _VARIANT_8608]
            | Annotated[bytes, _VARIANT_8609]
            | Annotated[bytes, _VARIANT_8610]
            | Annotated[ProjectileType8611, _VARIANT_8611]
            | Annotated[DeliveryType8612, _VARIANT_8612]
            | Annotated[CastingType8613, _VARIANT_8613],
            _VARIANT_8592,
        ]
        | Annotated[_values.FormId, _VARIANT_8614]
        | Annotated[_values.FormId, _VARIANT_8615]
        | Annotated[_values.FormId, _VARIANT_8616]
        | Annotated[PlayerAction8617, _VARIANT_8617]
        | Annotated[CastingType8618, _VARIANT_8618]
        | Annotated[_values.FormId, _VARIANT_8619]
        | Annotated[_values.FormId, _VARIANT_8620]
        | Annotated[_values.FormId, _VARIANT_8621]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_8622,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8623,
        ]
        | Annotated[_values.FormId, _VARIANT_8624]
        | Annotated[FurnitureAnim8625, _VARIANT_8625]
        | Annotated[FurnitureEntry8626, _VARIANT_8626]
        | Annotated[_values.FormId, _VARIANT_8627]
        | Annotated[WardState8628, _VARIANT_8628]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8629,
        ]
        | Annotated[_values.FormId, _VARIANT_8630]
        | Annotated[_values.FormId, _VARIANT_8631]
        | Annotated[_values.FormId, _VARIANT_8632]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn8633]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_8635,
        ]
        | Annotated[_values.FormId, _VARIANT_8636]
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


class Condition8484(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN/12:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="SCEN/12:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("SCEN/12:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("SCEN/12:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure8486] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure8486]]:
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


class SceneRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SCEN"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SCEN"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SCEN/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="SCEN/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "flags": _base.Binding(
            path="SCEN/2:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "phases": _base.Binding(
            path="SCEN/3:Phases",
            kind="repeat",
            name="Phases",
            repeated_path="SCEN/3:Phases/repeat/0:Phase",
            child_kind="sequence",
        ),
        "actors": _base.Binding(
            path="SCEN/4:Actors",
            kind="repeat",
            name="Actors",
            repeated_path="SCEN/4:Actors/repeat/0:Actor",
            child_kind="sequence",
        ),
        "actions": _base.Binding(
            path="SCEN/5:Actions",
            kind="repeat",
            name="Actions",
            repeated_path="SCEN/5:Actions/repeat/0:Action",
            child_kind="sequence",
        ),
        "unused": _base.Binding(
            path="SCEN/6:Unused",
            kind="sequence",
            name="Unused",
        ),
        "marker": _base.Binding(
            path="SCEN/7:Marker",
            kind="subrecord",
            name="Marker",
        ),
        "unused_8462": _base.Binding(
            path="SCEN/8:Unused",
            kind="sequence",
            name="Unused",
        ),
        "quest": _base.Binding(
            path="SCEN/9:Quest",
            kind="subrecord",
            name="Quest",
        ),
        "last_action_index": _base.Binding(
            path="SCEN/10:Last Action Index",
            kind="subrecord",
            name="Last Action Index",
        ),
        "actor_behavior_settings": _base.Binding(
            path="SCEN/11:Actor Behavior Settings",
            kind="subrecord",
            name="Actor Behavior Settings",
        ),
        "conditions": _base.Binding(
            path="SCEN/12:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="SCEN/12:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure7968] = None
    """Value decoded from this schema node."""

    flags: Optional[BeginOnQuestStartStopQuestOnEndShowA0D148Fed8032] = None
    """Value decoded from this schema node."""

    phases: tuple[Phase8034, ...] = ()
    """Value decoded from this schema node."""

    actors: tuple[Actor8390, ...] = ()
    """Value decoded from this schema node."""

    actions: tuple[Action8398, ...] = ()
    """Value decoded from this schema node."""

    unused: Optional[Unused8449] = None
    """Value decoded from this schema node."""

    marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_8462: Optional[Unused8462] = None
    """Value decoded from this schema node."""

    quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    last_action_index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    actor_behavior_settings: Optional[Structure8478] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition8484, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure7968]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[
        Optional[BeginOnQuestStartStopQuestOnEndShowA0D148Fed8032]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["phases"]
    ) -> _base.FieldRef[tuple[Phase8034, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actors"]
    ) -> _base.FieldRef[tuple[Actor8390, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actions"]
    ) -> _base.FieldRef[tuple[Action8398, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused"]
    ) -> _base.FieldRef[Optional[Unused8449]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["marker"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_8462"]
    ) -> _base.FieldRef[Optional[Unused8462]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["quest"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["last_action_index"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["actor_behavior_settings"]
    ) -> _base.FieldRef[Optional[Structure8478]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition8484, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
