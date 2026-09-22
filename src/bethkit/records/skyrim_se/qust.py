"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags12577(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type12581(_values.OpenIntEnum):
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


class Flags12582(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_12584: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV212586(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12586: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV112590(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12590: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_12585: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_12594: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_12595: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_12596: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool12597(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_12597: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV212600(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12600: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV112604(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_12604: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_12598: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_12608: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_12610: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_12612: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element12615(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_12614: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property12579(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type12581
    """Value decoded from this schema node."""

    flags: Flags12582
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_12584]
        | Annotated[
            Annotated[ObjectV212586, _VARIANT_12586]
            | Annotated[ObjectV112590, _VARIANT_12590],
            _VARIANT_12585,
        ]
        | Annotated[str, _VARIANT_12594]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12595,
        ]
        | Annotated[float, _VARIANT_12596]
        | Annotated[Bool12597, _VARIANT_12597]
        | Annotated[
            tuple[
                Annotated[ObjectV212600, _VARIANT_12600]
                | Annotated[ObjectV112604, _VARIANT_12604],
                ...,
            ],
            _VARIANT_12598,
        ]
        | Annotated[tuple[str, ...], _VARIANT_12608]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_12610,
        ]
        | Annotated[tuple[float, ...], _VARIANT_12612]
        | Annotated[tuple[Element12615, ...], _VARIANT_12614]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12581]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12582]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12584]
        | Annotated[
            Annotated[ObjectV212586, _VARIANT_12586]
            | Annotated[ObjectV112590, _VARIANT_12590],
            _VARIANT_12585,
        ]
        | Annotated[str, _VARIANT_12594]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12595,
        ]
        | Annotated[float, _VARIANT_12596]
        | Annotated[Bool12597, _VARIANT_12597]
        | Annotated[
            tuple[
                Annotated[ObjectV212600, _VARIANT_12600]
                | Annotated[ObjectV112604, _VARIANT_12604],
                ...,
            ],
            _VARIANT_12598,
        ]
        | Annotated[tuple[str, ...], _VARIANT_12608]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_12610,
        ]
        | Annotated[tuple[float, ...], _VARIANT_12612]
        | Annotated[tuple[Element12615, ...], _VARIANT_12614]
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


class Script12575(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags12577
    """Value decoded from this schema node."""

    properties: tuple[Property12579, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12577]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property12579, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Fragment12621(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
        "nts/3:Fragments/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "quest_stage": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/0:Quest Stage"
            ),
            kind="primitive",
            name="Quest Stage",
        ),
        "unknown": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/1:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "quest_stage_index": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/2:Quest Stage Index"
            ),
            kind="primitive",
            name="Quest Stage Index",
        ),
        "unknown_12625": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/3:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "script_name": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/4:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "fragment_name": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/5:FragmentName"
            ),
            kind="primitive",
            name="FragmentName",
        ),
    }

    quest_stage: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unknown: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    quest_stage_index: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    unknown_12625: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    script_name: str
    """Value decoded from this schema node."""

    fragment_name: str
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["quest_stage"]
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
        self, name: Literal["quest_stage_index"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_12625"]
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


class ScriptFragments12616(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/3:Script Fragments"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "extra_bind_data_version": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/0:Extra bind data version"
            ),
            kind="primitive",
            name="Extra bind data version",
        ),
        "fragment_count": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/1:FragmentCount"
            ),
            kind="primitive",
            name="FragmentCount",
        ),
        "file_name": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:FileName"
            ),
            kind="primitive",
            name="FileName",
        ),
        "fragments": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/3:Script Fragme"
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

    fragment_count: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    file_name: str
    """Value decoded from this schema node."""

    fragments: tuple[Fragment12621, ...]
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
    def field(
        self, name: Literal["fragment_count"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
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
    ) -> _base.FieldRef[tuple[Fragment12621, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class ObjectV212631(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/0:Object Union/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/0:Object Union/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/0:Object Union/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/0:Object Union/variants/0:Object v2/2:FormID"
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


_VARIANT_12631: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/0:Object Union/variants/0:Object v2"
    )
)


class ObjectV112635(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/0:Object Union/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/0:Object Union/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/0:Object Union/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/0:Object Union/variants/1:Object v1/2:Unused"
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


_VARIANT_12635: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/0:Object Union/variants/1:Object v1"
    )
)


class Flags12644(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type12648(_values.OpenIntEnum):
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


class Flags12649(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_12651: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/0:Unused"
    )
)


class ObjectV212653(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/1:Object Union/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/1:Object Union/variants/0:Object v2/0:Unuse"
                "d"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/1:Object Union/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/1:Object Union/variants/0:Object v2/2:FormI"
                "D"
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


_VARIANT_12653: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/1:Object Union/variants/0:Object v2"
    )
)


class ObjectV112657(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/1:Object Union/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/1:Object Union/variants/1:Object v1/0:FormI"
                "D"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/1:Object Union/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/1:Object Union/variants/1:Object v1/2:Unuse"
                "d"
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


_VARIANT_12657: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/1:Object Union/variants/1:Object v1"
    )
)


_VARIANT_12652: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/1:Object Union"
    )
)


_VARIANT_12661: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/2:String"
    )
)


_VARIANT_12662: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/3:Int32"
    )
)


_VARIANT_12663: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/4:Float"
    )
)


class Bool12664(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_12664: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/5:Bool"
    )
)


class ObjectV212667(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/6:Array of Object/element/variants/0:Object"
        " v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/6:Array of Object/element/variants/0:Object"
                " v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/6:Array of Object/element/variants/0:Object"
                " v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/6:Array of Object/element/variants/0:Object"
                " v2/2:FormID"
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


_VARIANT_12667: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/6:Array of Object/element/variants/0:Object"
        " v2"
    )
)


class ObjectV112671(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/6:Array of Object/element/variants/1:Object"
        " v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/6:Array of Object/element/variants/1:Object"
                " v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/6:Array of Object/element/variants/1:Object"
                " v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e/variants/6:Array of Object/element/variants/1:Object"
                " v1/2:Unused"
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


_VARIANT_12671: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/6:Array of Object/element/variants/1:Object"
        " v1"
    )
)


_VARIANT_12665: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/6:Array of Object"
    )
)


_VARIANT_12675: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/7:Array of String"
    )
)


_VARIANT_12677: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/8:Array of Int32"
    )
)


_VARIANT_12679: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/9:Array of Float"
    )
)


class Element12682(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_12681: _base.Variant = _base.Variant(
    path=(
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
        "e/variants/10:Array of Bool"
    )
)


class Property12646(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/0:prop"
                "ertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/2:Flag"
                "s"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties/element/3:Valu"
                "e"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type12648
    """Value decoded from this schema node."""

    flags: Flags12649
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_12651]
        | Annotated[
            Annotated[ObjectV212653, _VARIANT_12653]
            | Annotated[ObjectV112657, _VARIANT_12657],
            _VARIANT_12652,
        ]
        | Annotated[str, _VARIANT_12661]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12662,
        ]
        | Annotated[float, _VARIANT_12663]
        | Annotated[Bool12664, _VARIANT_12664]
        | Annotated[
            tuple[
                Annotated[ObjectV212667, _VARIANT_12667]
                | Annotated[ObjectV112671, _VARIANT_12671],
                ...,
            ],
            _VARIANT_12665,
        ]
        | Annotated[tuple[str, ...], _VARIANT_12675]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_12677,
        ]
        | Annotated[tuple[float, ...], _VARIANT_12679]
        | Annotated[tuple[Element12682, ...], _VARIANT_12681]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12648]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12649]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12651]
        | Annotated[
            Annotated[ObjectV212653, _VARIANT_12653]
            | Annotated[ObjectV112657, _VARIANT_12657],
            _VARIANT_12652,
        ]
        | Annotated[str, _VARIANT_12661]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12662,
        ]
        | Annotated[float, _VARIANT_12663]
        | Annotated[Bool12664, _VARIANT_12664]
        | Annotated[
            tuple[
                Annotated[ObjectV212667, _VARIANT_12667]
                | Annotated[ObjectV112671, _VARIANT_12671],
                ...,
            ],
            _VARIANT_12665,
        ]
        | Annotated[tuple[str, ...], _VARIANT_12675]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_12677,
        ]
        | Annotated[tuple[float, ...], _VARIANT_12679]
        | Annotated[tuple[Element12682, ...], _VARIANT_12681]
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


class Script12642(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
        "nt/3:Alias Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts/element/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags12644
    """Value decoded from this schema node."""

    properties: tuple[Property12646, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12644]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property12646, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Alias12629(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/1:Virtual Machine Adapter/payload/4:Aliases/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "object_union": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/0:Object Union"
            ),
            kind="union",
            name="Object Union",
        ),
        "version": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/1:Version"
            ),
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/2:Object Format"
            ),
            kind="primitive",
            name="Object Format",
        ),
        "alias_scripts": _base.Binding(
            path=(
                "QUST/1:Virtual Machine Adapter/payload/4:Aliases/eleme"
                "nt/3:Alias Scripts"
            ),
            kind="array",
            name="Alias Scripts",
        ),
    }

    object_union: (
        Annotated[ObjectV212631, _VARIANT_12631]
        | Annotated[ObjectV112635, _VARIANT_12635]
    )
    """Value decoded from this schema node."""

    version: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    object_format: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    alias_scripts: tuple[Script12642, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["object_union"]
    ) -> _base.FieldRef[
        Annotated[ObjectV212631, _VARIANT_12631]
        | Annotated[ObjectV112635, _VARIANT_12635]
    ]:
        """Returns the typed field reference."""

        ...

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
        self, name: Literal["alias_scripts"]
    ) -> _base.FieldRef[tuple[Script12642, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure12571(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="QUST/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("QUST/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="QUST/1:Virtual Machine Adapter/payload/2:Scripts",
            kind="array",
            name="Scripts",
        ),
        "script_fragments": _base.Binding(
            path=("QUST/1:Virtual Machine Adapter/payload/3:Script Fragments"),
            kind="struct",
            name="Script Fragments",
        ),
        "aliases": _base.Binding(
            path="QUST/1:Virtual Machine Adapter/payload/4:Aliases",
            kind="array",
            name="Aliases",
        ),
    }

    version: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    object_format: Annotated[
        int, pydantic.Field(strict=True, ge=-32768, le=32767)
    ]
    """Value decoded from this schema node."""

    scripts: tuple[Script12575, ...]
    """Value decoded from this schema node."""

    script_fragments: Optional[ScriptFragments12616] = None
    """Value decoded from this schema node."""

    aliases: Optional[tuple[Alias12629, ...]] = None
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
    ) -> _base.FieldRef[tuple[Script12575, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_fragments"]
    ) -> _base.FieldRef[Optional[ScriptFragments12616]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["aliases"]
    ) -> _base.FieldRef[Optional[tuple[Alias12629, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags12687(enum.IntFlag):
    """Named values from the pinned schema."""

    START_GAME_ENABLED = 1
    COMPLETED = 2
    ADD_IDLE_TOPIC_TO_HELLO = 4
    ALLOW_REPEATED_STAGES = 8
    STARTS_ENABLED = 16
    DISPLAYED_IN_HUD = 32
    FAILED = 64
    STAGE_WAIT = 128
    RUN_ONCE = 256
    EXCLUDE_FROM_DIALOGUE_EXPORT = 512
    WARN_ON_ALIAS_FILL_FAILURE = 1024
    ACTIVE = 2048
    REPEATS_CONDITIONS = 4096
    KEEP_INSTANCE = 8192
    WANT_DORMANT = 16384
    HAS_DIALOGUE_DATA = 32768


class Type12691(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    MAIN_QUEST = 1
    MAGES_GUILD = 2
    THIEVES_GUILD = 3
    DARK_BROTHERHOOD = 4
    COMPANION_QUESTS = 5
    MISCELLANEOUS = 6
    DAEDRIC = 7
    SIDE_QUEST = 8
    CIVIL_WAR = 9
    DLC01_VAMPIRE = 10
    DLC02_DRAGONBORN = 11


class Structure12686(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/3:General/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="QUST/3:General/payload/0:Flags",
            kind="primitive",
            name="Flags",
        ),
        "priority": _base.Binding(
            path="QUST/3:General/payload/1:Priority",
            kind="primitive",
            name="Priority",
        ),
        "form_version": _base.Binding(
            path="QUST/3:General/payload/2:Form Version",
            kind="primitive",
            name="Form Version",
        ),
        "unknown": _base.Binding(
            path="QUST/3:General/payload/3:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "type": _base.Binding(
            path="QUST/3:General/payload/4:Type",
            kind="primitive",
            name="Type",
        ),
    }

    flags: Flags12687
    """Value decoded from this schema node."""

    priority: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    form_version: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    type: Type12691
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags12687]:
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
    def field(
        self, name: Literal["form_version"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type12691]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_12707: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/2:Comparison Value/variants/"
        "0:Comparison Value - Float"
    )
)


_VARIANT_12708: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/2:Comparison Value/variants/"
        "1:Comparison Value - Global"
    )
)


_VARIANT_12712: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/0:Un"
        "known"
    )
)


_VARIANT_12713: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/1:No"
        "ne"
    )
)


_VARIANT_12714: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/2:In"
        "teger"
    )
)


_VARIANT_12715: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/3:Fl"
        "oat"
    )
)


_VARIANT_12716: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/4:Va"
        "riable Name"
    )
)


class Sex12717(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12717: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/5:Se"
        "x"
    )
)


class ActorValue12718(_values.OpenIntEnum):
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


_VARIANT_12718: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/6:Ac"
        "tor Value"
    )
)


class CrimeType12719(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12719: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/7:Cr"
        "ime Type"
    )
)


class Axis12720(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12720: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/8:Ax"
        "is"
    )
)


_VARIANT_12721: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/9:Qu"
        "est Stage (unused)"
    )
)


class MiscStat12722(_values.OpenIntEnum):
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


_VARIANT_12722: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/10:M"
        "isc Stat"
    )
)


class Alignment12723(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12723: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/11:A"
        "lignment"
    )
)


_VARIANT_12724: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/12:E"
        "quip Type"
    )
)


class FormType12725(_values.OpenIntEnum):
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


_VARIANT_12725: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/13:F"
        "orm Type"
    )
)


class CriticalStage12726(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12726: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/14:C"
        "ritical Stage"
    )
)


_VARIANT_12727: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/15:O"
        "bject Reference"
    )
)


_VARIANT_12728: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/16:I"
        "nventory Object"
    )
)


_VARIANT_12729: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/17:A"
        "ctor"
    )
)


_VARIANT_12730: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/18:V"
        "oice Type"
    )
)


_VARIANT_12731: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/19:I"
        "dle"
    )
)


_VARIANT_12732: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/20:F"
        "orm List"
    )
)


_VARIANT_12733: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/21:Q"
        "uest"
    )
)


_VARIANT_12734: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/22:F"
        "action"
    )
)


_VARIANT_12735: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/23:C"
        "ell"
    )
)


_VARIANT_12736: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/24:C"
        "lass"
    )
)


_VARIANT_12737: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/25:R"
        "ace"
    )
)


_VARIANT_12738: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/26:A"
        "ctor Base"
    )
)


_VARIANT_12739: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/27:G"
        "lobal"
    )
)


_VARIANT_12740: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/28:W"
        "eather"
    )
)


_VARIANT_12741: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/29:P"
        "ackage"
    )
)


_VARIANT_12742: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/30:E"
        "ncounter Zone"
    )
)


_VARIANT_12743: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/31:P"
        "erk"
    )
)


_VARIANT_12744: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/32:O"
        "wner"
    )
)


_VARIANT_12745: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/33:F"
        "urniture"
    )
)


_VARIANT_12746: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/34:E"
        "ffect Item"
    )
)


_VARIANT_12747: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/35:B"
        "ase Effect"
    )
)


_VARIANT_12748: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/36:W"
        "orldspace"
    )
)


class VatsValueFunction12749(_values.OpenIntEnum):
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


_VARIANT_12749: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/37:V"
        "ATS Value Function"
    )
)


_VARIANT_12750: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/38:V"
        "ATS Value Param (INVALID)"
    )
)


_VARIANT_12751: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/39:R"
        "eferenceable Object"
    )
)


_VARIANT_12752: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/40:R"
        "egion"
    )
)


_VARIANT_12753: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/41:K"
        "eyword"
    )
)


class PlayerAction12754(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12754: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/42:P"
        "layer Action"
    )
)


class CastingType12755(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12755: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/43:C"
        "asting Type"
    )
)


_VARIANT_12756: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/44:S"
        "hout"
    )
)


_VARIANT_12757: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/45:L"
        "ocation"
    )
)


_VARIANT_12758: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/46:L"
        "ocation Ref Type"
    )
)


_VARIANT_12759: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/47:A"
        "lias"
    )
)


_VARIANT_12760: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/48:P"
        "ackdata ID"
    )
)


_VARIANT_12761: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/49:A"
        "ssociation Type"
    )
)


class FurnitureAnim12762(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_12762: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/50:F"
        "urniture Anim"
    )
)


class FurnitureEntry12763(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_12763: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/51:F"
        "urniture Entry"
    )
)


_VARIANT_12764: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/52:S"
        "cene"
    )
)


class WardState12765(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_12765: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/53:W"
        "ard State"
    )
)


_VARIANT_12766: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/54:E"
        "vent"
    )
)


_VARIANT_12767: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/55:E"
        "vent Data"
    )
)


_VARIANT_12768: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/56:K"
        "nowable"
    )
)


_VARIANT_12769: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/5:Parameter #1/variants/57:F"
        "action"
    )
)


_VARIANT_12771: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/0:Un"
        "known"
    )
)


_VARIANT_12772: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/1:No"
        "ne"
    )
)


_VARIANT_12773: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/2:In"
        "teger"
    )
)


_VARIANT_12774: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/3:Fl"
        "oat"
    )
)


_VARIANT_12775: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/4:Va"
        "riable Name"
    )
)


class Sex12776(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12776: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/5:Se"
        "x"
    )
)


class ActorValue12777(_values.OpenIntEnum):
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


_VARIANT_12777: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/6:Ac"
        "tor Value"
    )
)


class CrimeType12778(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12778: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/7:Cr"
        "ime Type"
    )
)


class Axis12779(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12779: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/8:Ax"
        "is"
    )
)


_VARIANT_12780: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/9:Qu"
        "est Stage"
    )
)


class MiscStat12781(_values.OpenIntEnum):
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


_VARIANT_12781: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/10:M"
        "isc Stat"
    )
)


class Alignment12782(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12782: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/11:A"
        "lignment"
    )
)


_VARIANT_12783: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/12:E"
        "quip Type"
    )
)


class FormType12784(_values.OpenIntEnum):
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


_VARIANT_12784: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/13:F"
        "orm Type"
    )
)


class CriticalStage12785(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12785: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/14:C"
        "ritical Stage"
    )
)


_VARIANT_12786: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/15:O"
        "bject Reference"
    )
)


_VARIANT_12787: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/16:I"
        "nventory Object"
    )
)


_VARIANT_12788: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/17:A"
        "ctor"
    )
)


_VARIANT_12789: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/18:V"
        "oice Type"
    )
)


_VARIANT_12790: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/19:I"
        "dle"
    )
)


_VARIANT_12791: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/20:F"
        "orm List"
    )
)


_VARIANT_12792: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/21:Q"
        "uest"
    )
)


_VARIANT_12793: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/22:F"
        "action"
    )
)


_VARIANT_12794: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/23:C"
        "ell"
    )
)


_VARIANT_12795: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/24:C"
        "lass"
    )
)


_VARIANT_12796: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/25:R"
        "ace"
    )
)


_VARIANT_12797: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/26:A"
        "ctor Base"
    )
)


_VARIANT_12798: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/27:G"
        "lobal"
    )
)


_VARIANT_12799: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/28:W"
        "eather"
    )
)


_VARIANT_12800: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/29:P"
        "ackage"
    )
)


_VARIANT_12801: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/30:E"
        "ncounter Zone"
    )
)


_VARIANT_12802: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/31:P"
        "erk"
    )
)


_VARIANT_12803: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/32:O"
        "wner"
    )
)


_VARIANT_12804: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/33:F"
        "urniture"
    )
)


_VARIANT_12805: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/34:E"
        "ffect Item"
    )
)


_VARIANT_12806: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/35:B"
        "ase Effect"
    )
)


_VARIANT_12807: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/36:W"
        "orldspace"
    )
)


class VatsValueFunction12808(_values.OpenIntEnum):
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


_VARIANT_12808: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/37:V"
        "ATS Value Function"
    )
)


_VARIANT_12810: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/0:Weapon"
    )
)


_VARIANT_12811: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/1:Weapon List"
    )
)


_VARIANT_12812: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/2:Target"
    )
)


_VARIANT_12813: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/3:Target List"
    )
)


_VARIANT_12814: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/4:Unknown"
    )
)


class TargetPart12815(_values.OpenIntEnum):
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


_VARIANT_12815: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/5:Target Part"
    )
)


class VatsAction12816(_values.OpenIntEnum):
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


_VARIANT_12816: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/6:VATS Action"
    )
)


_VARIANT_12817: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/7:Unknown"
    )
)


_VARIANT_12818: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/8:Unknown"
    )
)


_VARIANT_12819: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/9:Critical Effect"
    )
)


_VARIANT_12820: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/10:Critical Effect List"
    )
)


_VARIANT_12821: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/11:Unknown"
    )
)


_VARIANT_12822: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/12:Unknown"
    )
)


_VARIANT_12823: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/13:Unknown"
    )
)


_VARIANT_12824: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/14:Unknown"
    )
)


class WeaponType12825(_values.OpenIntEnum):
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


_VARIANT_12825: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_12826: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/16:Unknown"
    )
)


_VARIANT_12827: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/17:Unknown"
    )
)


class ProjectileType12828(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_12828: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/18:Projectile Type"
    )
)


class DeliveryType12829(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_12829: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/19:Delivery Type"
    )
)


class CastingType12830(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_12830: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param/variants/20:Casting Type"
    )
)


_VARIANT_12809: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/38:V"
        "ATS Value Param"
    )
)


_VARIANT_12831: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/39:R"
        "eferenceable Object"
    )
)


_VARIANT_12832: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/40:R"
        "egion"
    )
)


_VARIANT_12833: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/41:K"
        "eyword"
    )
)


class PlayerAction12834(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12834: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/42:P"
        "layer Action"
    )
)


class CastingType12835(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12835: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/43:C"
        "asting Type"
    )
)


_VARIANT_12836: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/44:S"
        "hout"
    )
)


_VARIANT_12837: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/45:L"
        "ocation"
    )
)


_VARIANT_12838: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/46:L"
        "ocation Ref Type"
    )
)


_VARIANT_12839: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/47:A"
        "lias"
    )
)


_VARIANT_12840: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/48:P"
        "ackdata ID"
    )
)


_VARIANT_12841: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/49:A"
        "ssociation Type"
    )
)


class FurnitureAnim12842(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_12842: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/50:F"
        "urniture Anim"
    )
)


class FurnitureEntry12843(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_12843: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/51:F"
        "urniture Entry"
    )
)


_VARIANT_12844: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/52:S"
        "cene"
    )
)


class WardState12845(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_12845: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/53:W"
        "ard State"
    )
)


_VARIANT_12846: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/54:E"
        "vent"
    )
)


_VARIANT_12847: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/55:E"
        "vent Data"
    )
)


_VARIANT_12848: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/56:K"
        "nowable"
    )
)


_VARIANT_12849: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/6:Parameter #2/variants/57:F"
        "action"
    )
)


class RunOn12850(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_12852: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/8:Reference/variants/0:Unuse"
        "d"
    )
)


_VARIANT_12853: _base.Variant = _base.Variant(
    path=(
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload/8:Reference/variants/1:Refer"
        "ence"
    )
)


class Structure12703(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
        ":Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_12710": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA/payload/9:Parameter #3"
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
        Annotated[float, _VARIANT_12707]
        | Annotated[_values.FormId, _VARIANT_12708]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_12710: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_12712]
        | Annotated[bytes, _VARIANT_12713]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12714,
        ]
        | Annotated[float, _VARIANT_12715]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12716,
        ]
        | Annotated[Sex12717, _VARIANT_12717]
        | Annotated[ActorValue12718, _VARIANT_12718]
        | Annotated[CrimeType12719, _VARIANT_12719]
        | Annotated[Axis12720, _VARIANT_12720]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12721,
        ]
        | Annotated[MiscStat12722, _VARIANT_12722]
        | Annotated[Alignment12723, _VARIANT_12723]
        | Annotated[_values.FormId, _VARIANT_12724]
        | Annotated[FormType12725, _VARIANT_12725]
        | Annotated[CriticalStage12726, _VARIANT_12726]
        | Annotated[_values.FormId, _VARIANT_12727]
        | Annotated[_values.FormId, _VARIANT_12728]
        | Annotated[_values.FormId, _VARIANT_12729]
        | Annotated[_values.FormId, _VARIANT_12730]
        | Annotated[_values.FormId, _VARIANT_12731]
        | Annotated[_values.FormId, _VARIANT_12732]
        | Annotated[_values.FormId, _VARIANT_12733]
        | Annotated[_values.FormId, _VARIANT_12734]
        | Annotated[_values.FormId, _VARIANT_12735]
        | Annotated[_values.FormId, _VARIANT_12736]
        | Annotated[_values.FormId, _VARIANT_12737]
        | Annotated[_values.FormId, _VARIANT_12738]
        | Annotated[_values.FormId, _VARIANT_12739]
        | Annotated[_values.FormId, _VARIANT_12740]
        | Annotated[_values.FormId, _VARIANT_12741]
        | Annotated[_values.FormId, _VARIANT_12742]
        | Annotated[_values.FormId, _VARIANT_12743]
        | Annotated[_values.FormId, _VARIANT_12744]
        | Annotated[_values.FormId, _VARIANT_12745]
        | Annotated[_values.FormId, _VARIANT_12746]
        | Annotated[_values.FormId, _VARIANT_12747]
        | Annotated[_values.FormId, _VARIANT_12748]
        | Annotated[VatsValueFunction12749, _VARIANT_12749]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12750,
        ]
        | Annotated[_values.FormId, _VARIANT_12751]
        | Annotated[_values.FormId, _VARIANT_12752]
        | Annotated[_values.FormId, _VARIANT_12753]
        | Annotated[PlayerAction12754, _VARIANT_12754]
        | Annotated[CastingType12755, _VARIANT_12755]
        | Annotated[_values.FormId, _VARIANT_12756]
        | Annotated[_values.FormId, _VARIANT_12757]
        | Annotated[_values.FormId, _VARIANT_12758]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12759,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12760,
        ]
        | Annotated[_values.FormId, _VARIANT_12761]
        | Annotated[FurnitureAnim12762, _VARIANT_12762]
        | Annotated[FurnitureEntry12763, _VARIANT_12763]
        | Annotated[_values.FormId, _VARIANT_12764]
        | Annotated[WardState12765, _VARIANT_12765]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12766,
        ]
        | Annotated[_values.FormId, _VARIANT_12767]
        | Annotated[_values.FormId, _VARIANT_12768]
        | Annotated[_values.FormId, _VARIANT_12769]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_12771]
        | Annotated[bytes, _VARIANT_12772]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12773,
        ]
        | Annotated[float, _VARIANT_12774]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12775,
        ]
        | Annotated[Sex12776, _VARIANT_12776]
        | Annotated[ActorValue12777, _VARIANT_12777]
        | Annotated[CrimeType12778, _VARIANT_12778]
        | Annotated[Axis12779, _VARIANT_12779]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12780,
        ]
        | Annotated[MiscStat12781, _VARIANT_12781]
        | Annotated[Alignment12782, _VARIANT_12782]
        | Annotated[_values.FormId, _VARIANT_12783]
        | Annotated[FormType12784, _VARIANT_12784]
        | Annotated[CriticalStage12785, _VARIANT_12785]
        | Annotated[_values.FormId, _VARIANT_12786]
        | Annotated[_values.FormId, _VARIANT_12787]
        | Annotated[_values.FormId, _VARIANT_12788]
        | Annotated[_values.FormId, _VARIANT_12789]
        | Annotated[_values.FormId, _VARIANT_12790]
        | Annotated[_values.FormId, _VARIANT_12791]
        | Annotated[_values.FormId, _VARIANT_12792]
        | Annotated[_values.FormId, _VARIANT_12793]
        | Annotated[_values.FormId, _VARIANT_12794]
        | Annotated[_values.FormId, _VARIANT_12795]
        | Annotated[_values.FormId, _VARIANT_12796]
        | Annotated[_values.FormId, _VARIANT_12797]
        | Annotated[_values.FormId, _VARIANT_12798]
        | Annotated[_values.FormId, _VARIANT_12799]
        | Annotated[_values.FormId, _VARIANT_12800]
        | Annotated[_values.FormId, _VARIANT_12801]
        | Annotated[_values.FormId, _VARIANT_12802]
        | Annotated[_values.FormId, _VARIANT_12803]
        | Annotated[_values.FormId, _VARIANT_12804]
        | Annotated[_values.FormId, _VARIANT_12805]
        | Annotated[_values.FormId, _VARIANT_12806]
        | Annotated[_values.FormId, _VARIANT_12807]
        | Annotated[VatsValueFunction12808, _VARIANT_12808]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12810]
            | Annotated[_values.FormId, _VARIANT_12811]
            | Annotated[_values.FormId, _VARIANT_12812]
            | Annotated[_values.FormId, _VARIANT_12813]
            | Annotated[bytes, _VARIANT_12814]
            | Annotated[TargetPart12815, _VARIANT_12815]
            | Annotated[VatsAction12816, _VARIANT_12816]
            | Annotated[bytes, _VARIANT_12817]
            | Annotated[bytes, _VARIANT_12818]
            | Annotated[_values.FormId, _VARIANT_12819]
            | Annotated[_values.FormId, _VARIANT_12820]
            | Annotated[bytes, _VARIANT_12821]
            | Annotated[bytes, _VARIANT_12822]
            | Annotated[bytes, _VARIANT_12823]
            | Annotated[bytes, _VARIANT_12824]
            | Annotated[WeaponType12825, _VARIANT_12825]
            | Annotated[bytes, _VARIANT_12826]
            | Annotated[bytes, _VARIANT_12827]
            | Annotated[ProjectileType12828, _VARIANT_12828]
            | Annotated[DeliveryType12829, _VARIANT_12829]
            | Annotated[CastingType12830, _VARIANT_12830],
            _VARIANT_12809,
        ]
        | Annotated[_values.FormId, _VARIANT_12831]
        | Annotated[_values.FormId, _VARIANT_12832]
        | Annotated[_values.FormId, _VARIANT_12833]
        | Annotated[PlayerAction12834, _VARIANT_12834]
        | Annotated[CastingType12835, _VARIANT_12835]
        | Annotated[_values.FormId, _VARIANT_12836]
        | Annotated[_values.FormId, _VARIANT_12837]
        | Annotated[_values.FormId, _VARIANT_12838]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12839,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12840,
        ]
        | Annotated[_values.FormId, _VARIANT_12841]
        | Annotated[FurnitureAnim12842, _VARIANT_12842]
        | Annotated[FurnitureEntry12843, _VARIANT_12843]
        | Annotated[_values.FormId, _VARIANT_12844]
        | Annotated[WardState12845, _VARIANT_12845]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12846,
        ]
        | Annotated[_values.FormId, _VARIANT_12847]
        | Annotated[_values.FormId, _VARIANT_12848]
        | Annotated[_values.FormId, _VARIANT_12849]
    )
    """Value decoded from this schema node."""

    run_on: RunOn12850
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12852,
        ]
        | Annotated[_values.FormId, _VARIANT_12853]
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
        Annotated[float, _VARIANT_12707]
        | Annotated[_values.FormId, _VARIANT_12708]
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
    def field(self, name: Literal["unused_12710"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12712]
        | Annotated[bytes, _VARIANT_12713]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12714,
        ]
        | Annotated[float, _VARIANT_12715]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12716,
        ]
        | Annotated[Sex12717, _VARIANT_12717]
        | Annotated[ActorValue12718, _VARIANT_12718]
        | Annotated[CrimeType12719, _VARIANT_12719]
        | Annotated[Axis12720, _VARIANT_12720]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12721,
        ]
        | Annotated[MiscStat12722, _VARIANT_12722]
        | Annotated[Alignment12723, _VARIANT_12723]
        | Annotated[_values.FormId, _VARIANT_12724]
        | Annotated[FormType12725, _VARIANT_12725]
        | Annotated[CriticalStage12726, _VARIANT_12726]
        | Annotated[_values.FormId, _VARIANT_12727]
        | Annotated[_values.FormId, _VARIANT_12728]
        | Annotated[_values.FormId, _VARIANT_12729]
        | Annotated[_values.FormId, _VARIANT_12730]
        | Annotated[_values.FormId, _VARIANT_12731]
        | Annotated[_values.FormId, _VARIANT_12732]
        | Annotated[_values.FormId, _VARIANT_12733]
        | Annotated[_values.FormId, _VARIANT_12734]
        | Annotated[_values.FormId, _VARIANT_12735]
        | Annotated[_values.FormId, _VARIANT_12736]
        | Annotated[_values.FormId, _VARIANT_12737]
        | Annotated[_values.FormId, _VARIANT_12738]
        | Annotated[_values.FormId, _VARIANT_12739]
        | Annotated[_values.FormId, _VARIANT_12740]
        | Annotated[_values.FormId, _VARIANT_12741]
        | Annotated[_values.FormId, _VARIANT_12742]
        | Annotated[_values.FormId, _VARIANT_12743]
        | Annotated[_values.FormId, _VARIANT_12744]
        | Annotated[_values.FormId, _VARIANT_12745]
        | Annotated[_values.FormId, _VARIANT_12746]
        | Annotated[_values.FormId, _VARIANT_12747]
        | Annotated[_values.FormId, _VARIANT_12748]
        | Annotated[VatsValueFunction12749, _VARIANT_12749]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12750,
        ]
        | Annotated[_values.FormId, _VARIANT_12751]
        | Annotated[_values.FormId, _VARIANT_12752]
        | Annotated[_values.FormId, _VARIANT_12753]
        | Annotated[PlayerAction12754, _VARIANT_12754]
        | Annotated[CastingType12755, _VARIANT_12755]
        | Annotated[_values.FormId, _VARIANT_12756]
        | Annotated[_values.FormId, _VARIANT_12757]
        | Annotated[_values.FormId, _VARIANT_12758]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12759,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12760,
        ]
        | Annotated[_values.FormId, _VARIANT_12761]
        | Annotated[FurnitureAnim12762, _VARIANT_12762]
        | Annotated[FurnitureEntry12763, _VARIANT_12763]
        | Annotated[_values.FormId, _VARIANT_12764]
        | Annotated[WardState12765, _VARIANT_12765]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12766,
        ]
        | Annotated[_values.FormId, _VARIANT_12767]
        | Annotated[_values.FormId, _VARIANT_12768]
        | Annotated[_values.FormId, _VARIANT_12769]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12771]
        | Annotated[bytes, _VARIANT_12772]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12773,
        ]
        | Annotated[float, _VARIANT_12774]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12775,
        ]
        | Annotated[Sex12776, _VARIANT_12776]
        | Annotated[ActorValue12777, _VARIANT_12777]
        | Annotated[CrimeType12778, _VARIANT_12778]
        | Annotated[Axis12779, _VARIANT_12779]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12780,
        ]
        | Annotated[MiscStat12781, _VARIANT_12781]
        | Annotated[Alignment12782, _VARIANT_12782]
        | Annotated[_values.FormId, _VARIANT_12783]
        | Annotated[FormType12784, _VARIANT_12784]
        | Annotated[CriticalStage12785, _VARIANT_12785]
        | Annotated[_values.FormId, _VARIANT_12786]
        | Annotated[_values.FormId, _VARIANT_12787]
        | Annotated[_values.FormId, _VARIANT_12788]
        | Annotated[_values.FormId, _VARIANT_12789]
        | Annotated[_values.FormId, _VARIANT_12790]
        | Annotated[_values.FormId, _VARIANT_12791]
        | Annotated[_values.FormId, _VARIANT_12792]
        | Annotated[_values.FormId, _VARIANT_12793]
        | Annotated[_values.FormId, _VARIANT_12794]
        | Annotated[_values.FormId, _VARIANT_12795]
        | Annotated[_values.FormId, _VARIANT_12796]
        | Annotated[_values.FormId, _VARIANT_12797]
        | Annotated[_values.FormId, _VARIANT_12798]
        | Annotated[_values.FormId, _VARIANT_12799]
        | Annotated[_values.FormId, _VARIANT_12800]
        | Annotated[_values.FormId, _VARIANT_12801]
        | Annotated[_values.FormId, _VARIANT_12802]
        | Annotated[_values.FormId, _VARIANT_12803]
        | Annotated[_values.FormId, _VARIANT_12804]
        | Annotated[_values.FormId, _VARIANT_12805]
        | Annotated[_values.FormId, _VARIANT_12806]
        | Annotated[_values.FormId, _VARIANT_12807]
        | Annotated[VatsValueFunction12808, _VARIANT_12808]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12810]
            | Annotated[_values.FormId, _VARIANT_12811]
            | Annotated[_values.FormId, _VARIANT_12812]
            | Annotated[_values.FormId, _VARIANT_12813]
            | Annotated[bytes, _VARIANT_12814]
            | Annotated[TargetPart12815, _VARIANT_12815]
            | Annotated[VatsAction12816, _VARIANT_12816]
            | Annotated[bytes, _VARIANT_12817]
            | Annotated[bytes, _VARIANT_12818]
            | Annotated[_values.FormId, _VARIANT_12819]
            | Annotated[_values.FormId, _VARIANT_12820]
            | Annotated[bytes, _VARIANT_12821]
            | Annotated[bytes, _VARIANT_12822]
            | Annotated[bytes, _VARIANT_12823]
            | Annotated[bytes, _VARIANT_12824]
            | Annotated[WeaponType12825, _VARIANT_12825]
            | Annotated[bytes, _VARIANT_12826]
            | Annotated[bytes, _VARIANT_12827]
            | Annotated[ProjectileType12828, _VARIANT_12828]
            | Annotated[DeliveryType12829, _VARIANT_12829]
            | Annotated[CastingType12830, _VARIANT_12830],
            _VARIANT_12809,
        ]
        | Annotated[_values.FormId, _VARIANT_12831]
        | Annotated[_values.FormId, _VARIANT_12832]
        | Annotated[_values.FormId, _VARIANT_12833]
        | Annotated[PlayerAction12834, _VARIANT_12834]
        | Annotated[CastingType12835, _VARIANT_12835]
        | Annotated[_values.FormId, _VARIANT_12836]
        | Annotated[_values.FormId, _VARIANT_12837]
        | Annotated[_values.FormId, _VARIANT_12838]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12839,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12840,
        ]
        | Annotated[_values.FormId, _VARIANT_12841]
        | Annotated[FurnitureAnim12842, _VARIANT_12842]
        | Annotated[FurnitureEntry12843, _VARIANT_12843]
        | Annotated[_values.FormId, _VARIANT_12844]
        | Annotated[WardState12845, _VARIANT_12845]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12846,
        ]
        | Annotated[_values.FormId, _VARIANT_12847]
        | Annotated[_values.FormId, _VARIANT_12848]
        | Annotated[_values.FormId, _VARIANT_12849]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn12850]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12852,
        ]
        | Annotated[_values.FormId, _VARIANT_12853]
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


class Condition12701(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure12703] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure12703]]:
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


class QuestDialogueConditions12699(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/7:Quest Dialogue Conditions"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "conditions": _base.Binding(
            path="QUST/7:Quest Dialogue Conditions/0:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "QUST/7:Quest Dialogue Conditions/0:Conditions/repeat/0"
                ":Condition"
            ),
            child_kind="sequence",
        ),
    }

    conditions: tuple[Condition12701, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition12701, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


_VARIANT_12868: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_12869: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
        "Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_12873: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_12874: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/1:None"
    )
)


_VARIANT_12875: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/2:Integer"
    )
)


_VARIANT_12876: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/3:Float"
    )
)


_VARIANT_12877: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/4:Variable Name"
    )
)


class Sex12878(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12878: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/5:Sex"
    )
)


class ActorValue12879(_values.OpenIntEnum):
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


_VARIANT_12879: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType12880(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12880: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/7:Crime Type"
    )
)


class Axis12881(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12881: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/8:Axis"
    )
)


_VARIANT_12882: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat12883(_values.OpenIntEnum):
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


_VARIANT_12883: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment12884(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12884: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_12885: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/12:Equip Type"
    )
)


class FormType12886(_values.OpenIntEnum):
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


_VARIANT_12886: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage12887(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12887: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_12888: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_12889: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_12890: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/17:Actor"
    )
)


_VARIANT_12891: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_12892: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/19:Idle"
    )
)


_VARIANT_12893: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/20:Form List"
    )
)


_VARIANT_12894: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/21:Quest"
    )
)


_VARIANT_12895: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/22:Faction"
    )
)


_VARIANT_12896: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/23:Cell"
    )
)


_VARIANT_12897: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/24:Class"
    )
)


_VARIANT_12898: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/25:Race"
    )
)


_VARIANT_12899: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_12900: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/27:Global"
    )
)


_VARIANT_12901: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/28:Weather"
    )
)


_VARIANT_12902: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/29:Package"
    )
)


_VARIANT_12903: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_12904: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/31:Perk"
    )
)


_VARIANT_12905: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/32:Owner"
    )
)


_VARIANT_12906: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_12907: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_12908: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_12909: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction12910(_values.OpenIntEnum):
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


_VARIANT_12910: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_12911: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_12912: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_12913: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/40:Region"
    )
)


_VARIANT_12914: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction12915(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12915: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/42:Player Action"
    )
)


class CastingType12916(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12916: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_12917: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/44:Shout"
    )
)


_VARIANT_12918: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/45:Location"
    )
)


_VARIANT_12919: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_12920: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/47:Alias"
    )
)


_VARIANT_12921: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_12922: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim12923(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_12923: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry12924(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_12924: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_12925: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/52:Scene"
    )
)


class WardState12926(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_12926: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_12927: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/54:Event"
    )
)


_VARIANT_12928: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_12929: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_12930: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
        "Parameter #1/variants/57:Faction"
    )
)


_VARIANT_12932: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_12933: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/1:None"
    )
)


_VARIANT_12934: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/2:Integer"
    )
)


_VARIANT_12935: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/3:Float"
    )
)


_VARIANT_12936: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/4:Variable Name"
    )
)


class Sex12937(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_12937: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/5:Sex"
    )
)


class ActorValue12938(_values.OpenIntEnum):
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


_VARIANT_12938: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType12939(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_12939: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/7:Crime Type"
    )
)


class Axis12940(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_12940: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/8:Axis"
    )
)


_VARIANT_12941: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat12942(_values.OpenIntEnum):
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


_VARIANT_12942: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment12943(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_12943: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_12944: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/12:Equip Type"
    )
)


class FormType12945(_values.OpenIntEnum):
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


_VARIANT_12945: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage12946(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_12946: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_12947: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_12948: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_12949: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/17:Actor"
    )
)


_VARIANT_12950: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_12951: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/19:Idle"
    )
)


_VARIANT_12952: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/20:Form List"
    )
)


_VARIANT_12953: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/21:Quest"
    )
)


_VARIANT_12954: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/22:Faction"
    )
)


_VARIANT_12955: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/23:Cell"
    )
)


_VARIANT_12956: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/24:Class"
    )
)


_VARIANT_12957: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/25:Race"
    )
)


_VARIANT_12958: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_12959: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/27:Global"
    )
)


_VARIANT_12960: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/28:Weather"
    )
)


_VARIANT_12961: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/29:Package"
    )
)


_VARIANT_12962: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_12963: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/31:Perk"
    )
)


_VARIANT_12964: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/32:Owner"
    )
)


_VARIANT_12965: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_12966: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_12967: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_12968: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction12969(_values.OpenIntEnum):
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


_VARIANT_12969: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_12971: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/0:W"
        "eapon"
    )
)


_VARIANT_12972: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/1:W"
        "eapon List"
    )
)


_VARIANT_12973: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/2:T"
        "arget"
    )
)


_VARIANT_12974: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/3:T"
        "arget List"
    )
)


_VARIANT_12975: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/4:U"
        "nknown"
    )
)


class TargetPart12976(_values.OpenIntEnum):
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


_VARIANT_12976: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/5:T"
        "arget Part"
    )
)


class VatsAction12977(_values.OpenIntEnum):
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


_VARIANT_12977: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/6:V"
        "ATS Action"
    )
)


_VARIANT_12978: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/7:U"
        "nknown"
    )
)


_VARIANT_12979: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/8:U"
        "nknown"
    )
)


_VARIANT_12980: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/9:C"
        "ritical Effect"
    )
)


_VARIANT_12981: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/10:"
        "Critical Effect List"
    )
)


_VARIANT_12982: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/11:"
        "Unknown"
    )
)


_VARIANT_12983: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/12:"
        "Unknown"
    )
)


_VARIANT_12984: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/13:"
        "Unknown"
    )
)


_VARIANT_12985: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/14:"
        "Unknown"
    )
)


class WeaponType12986(_values.OpenIntEnum):
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


_VARIANT_12986: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/15:"
        "Weapon Type"
    )
)


_VARIANT_12987: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/16:"
        "Unknown"
    )
)


_VARIANT_12988: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/17:"
        "Unknown"
    )
)


class ProjectileType12989(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_12989: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/18:"
        "Projectile Type"
    )
)


class DeliveryType12990(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_12990: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/19:"
        "Delivery Type"
    )
)


class CastingType12991(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_12991: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param/variants/20:"
        "Casting Type"
    )
)


_VARIANT_12970: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_12992: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_12993: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/40:Region"
    )
)


_VARIANT_12994: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction12995(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_12995: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/42:Player Action"
    )
)


class CastingType12996(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_12996: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_12997: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/44:Shout"
    )
)


_VARIANT_12998: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/45:Location"
    )
)


_VARIANT_12999: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_13000: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/47:Alias"
    )
)


_VARIANT_13001: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_13002: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim13003(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13003: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry13004(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13004: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_13005: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/52:Scene"
    )
)


class WardState13006(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13006: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_13007: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/54:Event"
    )
)


_VARIANT_13008: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_13009: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_13010: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
        "Parameter #2/variants/57:Faction"
    )
)


class RunOn13011(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_13013: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/0:Unused"
    )
)


_VARIANT_13014: _base.Variant = _base.Variant(
    path=(
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
        "Reference/variants/1:Reference"
    )
)


class Structure12864(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=("QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/2:"
                "Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_12871": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/5:"
                "Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/6:"
                "Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/8:"
                "Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "QUST/9:Conditions/repeat/0:Condition/0:CTDA/payload/9:"
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
        Annotated[float, _VARIANT_12868]
        | Annotated[_values.FormId, _VARIANT_12869]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_12871: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_12873]
        | Annotated[bytes, _VARIANT_12874]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12875,
        ]
        | Annotated[float, _VARIANT_12876]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12877,
        ]
        | Annotated[Sex12878, _VARIANT_12878]
        | Annotated[ActorValue12879, _VARIANT_12879]
        | Annotated[CrimeType12880, _VARIANT_12880]
        | Annotated[Axis12881, _VARIANT_12881]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12882,
        ]
        | Annotated[MiscStat12883, _VARIANT_12883]
        | Annotated[Alignment12884, _VARIANT_12884]
        | Annotated[_values.FormId, _VARIANT_12885]
        | Annotated[FormType12886, _VARIANT_12886]
        | Annotated[CriticalStage12887, _VARIANT_12887]
        | Annotated[_values.FormId, _VARIANT_12888]
        | Annotated[_values.FormId, _VARIANT_12889]
        | Annotated[_values.FormId, _VARIANT_12890]
        | Annotated[_values.FormId, _VARIANT_12891]
        | Annotated[_values.FormId, _VARIANT_12892]
        | Annotated[_values.FormId, _VARIANT_12893]
        | Annotated[_values.FormId, _VARIANT_12894]
        | Annotated[_values.FormId, _VARIANT_12895]
        | Annotated[_values.FormId, _VARIANT_12896]
        | Annotated[_values.FormId, _VARIANT_12897]
        | Annotated[_values.FormId, _VARIANT_12898]
        | Annotated[_values.FormId, _VARIANT_12899]
        | Annotated[_values.FormId, _VARIANT_12900]
        | Annotated[_values.FormId, _VARIANT_12901]
        | Annotated[_values.FormId, _VARIANT_12902]
        | Annotated[_values.FormId, _VARIANT_12903]
        | Annotated[_values.FormId, _VARIANT_12904]
        | Annotated[_values.FormId, _VARIANT_12905]
        | Annotated[_values.FormId, _VARIANT_12906]
        | Annotated[_values.FormId, _VARIANT_12907]
        | Annotated[_values.FormId, _VARIANT_12908]
        | Annotated[_values.FormId, _VARIANT_12909]
        | Annotated[VatsValueFunction12910, _VARIANT_12910]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12911,
        ]
        | Annotated[_values.FormId, _VARIANT_12912]
        | Annotated[_values.FormId, _VARIANT_12913]
        | Annotated[_values.FormId, _VARIANT_12914]
        | Annotated[PlayerAction12915, _VARIANT_12915]
        | Annotated[CastingType12916, _VARIANT_12916]
        | Annotated[_values.FormId, _VARIANT_12917]
        | Annotated[_values.FormId, _VARIANT_12918]
        | Annotated[_values.FormId, _VARIANT_12919]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12920,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12921,
        ]
        | Annotated[_values.FormId, _VARIANT_12922]
        | Annotated[FurnitureAnim12923, _VARIANT_12923]
        | Annotated[FurnitureEntry12924, _VARIANT_12924]
        | Annotated[_values.FormId, _VARIANT_12925]
        | Annotated[WardState12926, _VARIANT_12926]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12927,
        ]
        | Annotated[_values.FormId, _VARIANT_12928]
        | Annotated[_values.FormId, _VARIANT_12929]
        | Annotated[_values.FormId, _VARIANT_12930]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_12932]
        | Annotated[bytes, _VARIANT_12933]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12934,
        ]
        | Annotated[float, _VARIANT_12935]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12936,
        ]
        | Annotated[Sex12937, _VARIANT_12937]
        | Annotated[ActorValue12938, _VARIANT_12938]
        | Annotated[CrimeType12939, _VARIANT_12939]
        | Annotated[Axis12940, _VARIANT_12940]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12941,
        ]
        | Annotated[MiscStat12942, _VARIANT_12942]
        | Annotated[Alignment12943, _VARIANT_12943]
        | Annotated[_values.FormId, _VARIANT_12944]
        | Annotated[FormType12945, _VARIANT_12945]
        | Annotated[CriticalStage12946, _VARIANT_12946]
        | Annotated[_values.FormId, _VARIANT_12947]
        | Annotated[_values.FormId, _VARIANT_12948]
        | Annotated[_values.FormId, _VARIANT_12949]
        | Annotated[_values.FormId, _VARIANT_12950]
        | Annotated[_values.FormId, _VARIANT_12951]
        | Annotated[_values.FormId, _VARIANT_12952]
        | Annotated[_values.FormId, _VARIANT_12953]
        | Annotated[_values.FormId, _VARIANT_12954]
        | Annotated[_values.FormId, _VARIANT_12955]
        | Annotated[_values.FormId, _VARIANT_12956]
        | Annotated[_values.FormId, _VARIANT_12957]
        | Annotated[_values.FormId, _VARIANT_12958]
        | Annotated[_values.FormId, _VARIANT_12959]
        | Annotated[_values.FormId, _VARIANT_12960]
        | Annotated[_values.FormId, _VARIANT_12961]
        | Annotated[_values.FormId, _VARIANT_12962]
        | Annotated[_values.FormId, _VARIANT_12963]
        | Annotated[_values.FormId, _VARIANT_12964]
        | Annotated[_values.FormId, _VARIANT_12965]
        | Annotated[_values.FormId, _VARIANT_12966]
        | Annotated[_values.FormId, _VARIANT_12967]
        | Annotated[_values.FormId, _VARIANT_12968]
        | Annotated[VatsValueFunction12969, _VARIANT_12969]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12971]
            | Annotated[_values.FormId, _VARIANT_12972]
            | Annotated[_values.FormId, _VARIANT_12973]
            | Annotated[_values.FormId, _VARIANT_12974]
            | Annotated[bytes, _VARIANT_12975]
            | Annotated[TargetPart12976, _VARIANT_12976]
            | Annotated[VatsAction12977, _VARIANT_12977]
            | Annotated[bytes, _VARIANT_12978]
            | Annotated[bytes, _VARIANT_12979]
            | Annotated[_values.FormId, _VARIANT_12980]
            | Annotated[_values.FormId, _VARIANT_12981]
            | Annotated[bytes, _VARIANT_12982]
            | Annotated[bytes, _VARIANT_12983]
            | Annotated[bytes, _VARIANT_12984]
            | Annotated[bytes, _VARIANT_12985]
            | Annotated[WeaponType12986, _VARIANT_12986]
            | Annotated[bytes, _VARIANT_12987]
            | Annotated[bytes, _VARIANT_12988]
            | Annotated[ProjectileType12989, _VARIANT_12989]
            | Annotated[DeliveryType12990, _VARIANT_12990]
            | Annotated[CastingType12991, _VARIANT_12991],
            _VARIANT_12970,
        ]
        | Annotated[_values.FormId, _VARIANT_12992]
        | Annotated[_values.FormId, _VARIANT_12993]
        | Annotated[_values.FormId, _VARIANT_12994]
        | Annotated[PlayerAction12995, _VARIANT_12995]
        | Annotated[CastingType12996, _VARIANT_12996]
        | Annotated[_values.FormId, _VARIANT_12997]
        | Annotated[_values.FormId, _VARIANT_12998]
        | Annotated[_values.FormId, _VARIANT_12999]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13000,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13001,
        ]
        | Annotated[_values.FormId, _VARIANT_13002]
        | Annotated[FurnitureAnim13003, _VARIANT_13003]
        | Annotated[FurnitureEntry13004, _VARIANT_13004]
        | Annotated[_values.FormId, _VARIANT_13005]
        | Annotated[WardState13006, _VARIANT_13006]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13007,
        ]
        | Annotated[_values.FormId, _VARIANT_13008]
        | Annotated[_values.FormId, _VARIANT_13009]
        | Annotated[_values.FormId, _VARIANT_13010]
    )
    """Value decoded from this schema node."""

    run_on: RunOn13011
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13013,
        ]
        | Annotated[_values.FormId, _VARIANT_13014]
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
        Annotated[float, _VARIANT_12868]
        | Annotated[_values.FormId, _VARIANT_12869]
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
    def field(self, name: Literal["unused_12871"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12873]
        | Annotated[bytes, _VARIANT_12874]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12875,
        ]
        | Annotated[float, _VARIANT_12876]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12877,
        ]
        | Annotated[Sex12878, _VARIANT_12878]
        | Annotated[ActorValue12879, _VARIANT_12879]
        | Annotated[CrimeType12880, _VARIANT_12880]
        | Annotated[Axis12881, _VARIANT_12881]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12882,
        ]
        | Annotated[MiscStat12883, _VARIANT_12883]
        | Annotated[Alignment12884, _VARIANT_12884]
        | Annotated[_values.FormId, _VARIANT_12885]
        | Annotated[FormType12886, _VARIANT_12886]
        | Annotated[CriticalStage12887, _VARIANT_12887]
        | Annotated[_values.FormId, _VARIANT_12888]
        | Annotated[_values.FormId, _VARIANT_12889]
        | Annotated[_values.FormId, _VARIANT_12890]
        | Annotated[_values.FormId, _VARIANT_12891]
        | Annotated[_values.FormId, _VARIANT_12892]
        | Annotated[_values.FormId, _VARIANT_12893]
        | Annotated[_values.FormId, _VARIANT_12894]
        | Annotated[_values.FormId, _VARIANT_12895]
        | Annotated[_values.FormId, _VARIANT_12896]
        | Annotated[_values.FormId, _VARIANT_12897]
        | Annotated[_values.FormId, _VARIANT_12898]
        | Annotated[_values.FormId, _VARIANT_12899]
        | Annotated[_values.FormId, _VARIANT_12900]
        | Annotated[_values.FormId, _VARIANT_12901]
        | Annotated[_values.FormId, _VARIANT_12902]
        | Annotated[_values.FormId, _VARIANT_12903]
        | Annotated[_values.FormId, _VARIANT_12904]
        | Annotated[_values.FormId, _VARIANT_12905]
        | Annotated[_values.FormId, _VARIANT_12906]
        | Annotated[_values.FormId, _VARIANT_12907]
        | Annotated[_values.FormId, _VARIANT_12908]
        | Annotated[_values.FormId, _VARIANT_12909]
        | Annotated[VatsValueFunction12910, _VARIANT_12910]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12911,
        ]
        | Annotated[_values.FormId, _VARIANT_12912]
        | Annotated[_values.FormId, _VARIANT_12913]
        | Annotated[_values.FormId, _VARIANT_12914]
        | Annotated[PlayerAction12915, _VARIANT_12915]
        | Annotated[CastingType12916, _VARIANT_12916]
        | Annotated[_values.FormId, _VARIANT_12917]
        | Annotated[_values.FormId, _VARIANT_12918]
        | Annotated[_values.FormId, _VARIANT_12919]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12920,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12921,
        ]
        | Annotated[_values.FormId, _VARIANT_12922]
        | Annotated[FurnitureAnim12923, _VARIANT_12923]
        | Annotated[FurnitureEntry12924, _VARIANT_12924]
        | Annotated[_values.FormId, _VARIANT_12925]
        | Annotated[WardState12926, _VARIANT_12926]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12927,
        ]
        | Annotated[_values.FormId, _VARIANT_12928]
        | Annotated[_values.FormId, _VARIANT_12929]
        | Annotated[_values.FormId, _VARIANT_12930]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_12932]
        | Annotated[bytes, _VARIANT_12933]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12934,
        ]
        | Annotated[float, _VARIANT_12935]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_12936,
        ]
        | Annotated[Sex12937, _VARIANT_12937]
        | Annotated[ActorValue12938, _VARIANT_12938]
        | Annotated[CrimeType12939, _VARIANT_12939]
        | Annotated[Axis12940, _VARIANT_12940]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_12941,
        ]
        | Annotated[MiscStat12942, _VARIANT_12942]
        | Annotated[Alignment12943, _VARIANT_12943]
        | Annotated[_values.FormId, _VARIANT_12944]
        | Annotated[FormType12945, _VARIANT_12945]
        | Annotated[CriticalStage12946, _VARIANT_12946]
        | Annotated[_values.FormId, _VARIANT_12947]
        | Annotated[_values.FormId, _VARIANT_12948]
        | Annotated[_values.FormId, _VARIANT_12949]
        | Annotated[_values.FormId, _VARIANT_12950]
        | Annotated[_values.FormId, _VARIANT_12951]
        | Annotated[_values.FormId, _VARIANT_12952]
        | Annotated[_values.FormId, _VARIANT_12953]
        | Annotated[_values.FormId, _VARIANT_12954]
        | Annotated[_values.FormId, _VARIANT_12955]
        | Annotated[_values.FormId, _VARIANT_12956]
        | Annotated[_values.FormId, _VARIANT_12957]
        | Annotated[_values.FormId, _VARIANT_12958]
        | Annotated[_values.FormId, _VARIANT_12959]
        | Annotated[_values.FormId, _VARIANT_12960]
        | Annotated[_values.FormId, _VARIANT_12961]
        | Annotated[_values.FormId, _VARIANT_12962]
        | Annotated[_values.FormId, _VARIANT_12963]
        | Annotated[_values.FormId, _VARIANT_12964]
        | Annotated[_values.FormId, _VARIANT_12965]
        | Annotated[_values.FormId, _VARIANT_12966]
        | Annotated[_values.FormId, _VARIANT_12967]
        | Annotated[_values.FormId, _VARIANT_12968]
        | Annotated[VatsValueFunction12969, _VARIANT_12969]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_12971]
            | Annotated[_values.FormId, _VARIANT_12972]
            | Annotated[_values.FormId, _VARIANT_12973]
            | Annotated[_values.FormId, _VARIANT_12974]
            | Annotated[bytes, _VARIANT_12975]
            | Annotated[TargetPart12976, _VARIANT_12976]
            | Annotated[VatsAction12977, _VARIANT_12977]
            | Annotated[bytes, _VARIANT_12978]
            | Annotated[bytes, _VARIANT_12979]
            | Annotated[_values.FormId, _VARIANT_12980]
            | Annotated[_values.FormId, _VARIANT_12981]
            | Annotated[bytes, _VARIANT_12982]
            | Annotated[bytes, _VARIANT_12983]
            | Annotated[bytes, _VARIANT_12984]
            | Annotated[bytes, _VARIANT_12985]
            | Annotated[WeaponType12986, _VARIANT_12986]
            | Annotated[bytes, _VARIANT_12987]
            | Annotated[bytes, _VARIANT_12988]
            | Annotated[ProjectileType12989, _VARIANT_12989]
            | Annotated[DeliveryType12990, _VARIANT_12990]
            | Annotated[CastingType12991, _VARIANT_12991],
            _VARIANT_12970,
        ]
        | Annotated[_values.FormId, _VARIANT_12992]
        | Annotated[_values.FormId, _VARIANT_12993]
        | Annotated[_values.FormId, _VARIANT_12994]
        | Annotated[PlayerAction12995, _VARIANT_12995]
        | Annotated[CastingType12996, _VARIANT_12996]
        | Annotated[_values.FormId, _VARIANT_12997]
        | Annotated[_values.FormId, _VARIANT_12998]
        | Annotated[_values.FormId, _VARIANT_12999]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13000,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13001,
        ]
        | Annotated[_values.FormId, _VARIANT_13002]
        | Annotated[FurnitureAnim13003, _VARIANT_13003]
        | Annotated[FurnitureEntry13004, _VARIANT_13004]
        | Annotated[_values.FormId, _VARIANT_13005]
        | Annotated[WardState13006, _VARIANT_13006]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13007,
        ]
        | Annotated[_values.FormId, _VARIANT_13008]
        | Annotated[_values.FormId, _VARIANT_13009]
        | Annotated[_values.FormId, _VARIANT_13010]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn13011]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13013,
        ]
        | Annotated[_values.FormId, _VARIANT_13014]
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


class Condition12862(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/9:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="QUST/9:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("QUST/9:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("QUST/9:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure12864] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure12864]]:
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


class Flags13025(enum.IntFlag):
    """Named values from the pinned schema."""

    UNKNOWN_1 = 1
    START_UP_STAGE = 2
    SHUT_DOWN_STAGE = 4
    KEEP_INSTANCE_DATA_FROM_HERE_ON = 8


class Structure13023(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/10:Stages/repeat/0:Stage/0:Stage Index/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "stage_index": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/0:Stage Index/payload/0:"
                "Stage Index"
            ),
            kind="primitive",
            name="Stage Index",
        ),
        "flags": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/0:Stage Index/payload/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "unknown": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/0:Stage Index/payload/2:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
    }

    stage_index: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    flags: Flags13025
    """Value decoded from this schema node."""

    unknown: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["stage_index"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags13025]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
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


class CompleteQuestFailQuest13030(enum.IntFlag):
    """Named values from the pinned schema."""

    COMPLETE_QUEST = 1
    FAIL_QUEST = 2


_VARIANT_13038: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/2:Comparison Value/variants/0:Comparison Value - Flo"
        "at"
    )
)


_VARIANT_13039: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/2:Comparison Value/variants/1:Comparison Value - Glo"
        "bal"
    )
)


_VARIANT_13043: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_13044: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/1:None"
    )
)


_VARIANT_13045: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/2:Integer"
    )
)


_VARIANT_13046: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/3:Float"
    )
)


_VARIANT_13047: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/4:Variable Name"
    )
)


class Sex13048(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13048: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/5:Sex"
    )
)


class ActorValue13049(_values.OpenIntEnum):
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


_VARIANT_13049: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType13050(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13050: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/7:Crime Type"
    )
)


class Axis13051(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13051: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/8:Axis"
    )
)


_VARIANT_13052: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat13053(_values.OpenIntEnum):
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


_VARIANT_13053: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment13054(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13054: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_13055: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/12:Equip Type"
    )
)


class FormType13056(_values.OpenIntEnum):
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


_VARIANT_13056: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage13057(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13057: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_13058: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_13059: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_13060: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/17:Actor"
    )
)


_VARIANT_13061: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_13062: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/19:Idle"
    )
)


_VARIANT_13063: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/20:Form List"
    )
)


_VARIANT_13064: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/21:Quest"
    )
)


_VARIANT_13065: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/22:Faction"
    )
)


_VARIANT_13066: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/23:Cell"
    )
)


_VARIANT_13067: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/24:Class"
    )
)


_VARIANT_13068: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/25:Race"
    )
)


_VARIANT_13069: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_13070: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/27:Global"
    )
)


_VARIANT_13071: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/28:Weather"
    )
)


_VARIANT_13072: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/29:Package"
    )
)


_VARIANT_13073: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_13074: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/31:Perk"
    )
)


_VARIANT_13075: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/32:Owner"
    )
)


_VARIANT_13076: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_13077: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_13078: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_13079: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction13080(_values.OpenIntEnum):
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


_VARIANT_13080: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_13081: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/38:VATS Value Param (INVALID"
        ")"
    )
)


_VARIANT_13082: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_13083: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/40:Region"
    )
)


_VARIANT_13084: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction13085(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13085: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/42:Player Action"
    )
)


class CastingType13086(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13086: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_13087: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/44:Shout"
    )
)


_VARIANT_13088: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/45:Location"
    )
)


_VARIANT_13089: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_13090: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/47:Alias"
    )
)


_VARIANT_13091: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_13092: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim13093(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13093: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry13094(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13094: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_13095: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/52:Scene"
    )
)


class WardState13096(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13096: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_13097: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/54:Event"
    )
)


_VARIANT_13098: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_13099: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_13100: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/5:Parameter #1/variants/57:Faction"
    )
)


_VARIANT_13102: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_13103: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/1:None"
    )
)


_VARIANT_13104: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/2:Integer"
    )
)


_VARIANT_13105: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/3:Float"
    )
)


_VARIANT_13106: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/4:Variable Name"
    )
)


class Sex13107(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13107: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/5:Sex"
    )
)


class ActorValue13108(_values.OpenIntEnum):
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


_VARIANT_13108: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType13109(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13109: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/7:Crime Type"
    )
)


class Axis13110(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13110: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/8:Axis"
    )
)


_VARIANT_13111: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat13112(_values.OpenIntEnum):
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


_VARIANT_13112: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment13113(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13113: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_13114: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/12:Equip Type"
    )
)


class FormType13115(_values.OpenIntEnum):
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


_VARIANT_13115: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage13116(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13116: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_13117: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_13118: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_13119: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/17:Actor"
    )
)


_VARIANT_13120: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_13121: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/19:Idle"
    )
)


_VARIANT_13122: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/20:Form List"
    )
)


_VARIANT_13123: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/21:Quest"
    )
)


_VARIANT_13124: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/22:Faction"
    )
)


_VARIANT_13125: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/23:Cell"
    )
)


_VARIANT_13126: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/24:Class"
    )
)


_VARIANT_13127: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/25:Race"
    )
)


_VARIANT_13128: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_13129: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/27:Global"
    )
)


_VARIANT_13130: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/28:Weather"
    )
)


_VARIANT_13131: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/29:Package"
    )
)


_VARIANT_13132: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_13133: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/31:Perk"
    )
)


_VARIANT_13134: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/32:Owner"
    )
)


_VARIANT_13135: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_13136: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_13137: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_13138: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction13139(_values.OpenIntEnum):
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


_VARIANT_13139: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_13141: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/0:Weapon"
    )
)


_VARIANT_13142: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/1:Weapon List"
    )
)


_VARIANT_13143: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/2:Target"
    )
)


_VARIANT_13144: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/3:Target List"
    )
)


_VARIANT_13145: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/4:Unknown"
    )
)


class TargetPart13146(_values.OpenIntEnum):
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


_VARIANT_13146: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/5:Target Part"
    )
)


class VatsAction13147(_values.OpenIntEnum):
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


_VARIANT_13147: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/6:VATS Action"
    )
)


_VARIANT_13148: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/7:Unknown"
    )
)


_VARIANT_13149: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/8:Unknown"
    )
)


_VARIANT_13150: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/9:Critical Effect"
    )
)


_VARIANT_13151: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/10:Critical Effect List"
    )
)


_VARIANT_13152: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/11:Unknown"
    )
)


_VARIANT_13153: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/12:Unknown"
    )
)


_VARIANT_13154: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/13:Unknown"
    )
)


_VARIANT_13155: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/14:Unknown"
    )
)


class WeaponType13156(_values.OpenIntEnum):
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


_VARIANT_13156: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/15:Weapon Type"
    )
)


_VARIANT_13157: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/16:Unknown"
    )
)


_VARIANT_13158: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/17:Unknown"
    )
)


class ProjectileType13159(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_13159: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/18:Projectile Type"
    )
)


class DeliveryType13160(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_13160: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/19:Delivery Type"
    )
)


class CastingType13161(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_13161: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param/variants"
        "/20:Casting Type"
    )
)


_VARIANT_13140: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_13162: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_13163: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/40:Region"
    )
)


_VARIANT_13164: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction13165(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13165: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/42:Player Action"
    )
)


class CastingType13166(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13166: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_13167: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/44:Shout"
    )
)


_VARIANT_13168: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/45:Location"
    )
)


_VARIANT_13169: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_13170: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/47:Alias"
    )
)


_VARIANT_13171: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_13172: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim13173(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13173: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry13174(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13174: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_13175: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/52:Scene"
    )
)


class WardState13176(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13176: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_13177: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/54:Event"
    )
)


_VARIANT_13178: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_13179: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_13180: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/6:Parameter #2/variants/57:Faction"
    )
)


class RunOn13181(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_13183: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/8:Reference/variants/0:Unused"
    )
)


_VARIANT_13184: _base.Variant = _base.Variant(
    path=(
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d/8:Reference/variants/1:Reference"
    )
)


class Structure13034(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
        "d"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_13041": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA/payloa"
                "d/9:Parameter #3"
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
        Annotated[float, _VARIANT_13038]
        | Annotated[_values.FormId, _VARIANT_13039]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_13041: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_13043]
        | Annotated[bytes, _VARIANT_13044]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13045,
        ]
        | Annotated[float, _VARIANT_13046]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13047,
        ]
        | Annotated[Sex13048, _VARIANT_13048]
        | Annotated[ActorValue13049, _VARIANT_13049]
        | Annotated[CrimeType13050, _VARIANT_13050]
        | Annotated[Axis13051, _VARIANT_13051]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13052,
        ]
        | Annotated[MiscStat13053, _VARIANT_13053]
        | Annotated[Alignment13054, _VARIANT_13054]
        | Annotated[_values.FormId, _VARIANT_13055]
        | Annotated[FormType13056, _VARIANT_13056]
        | Annotated[CriticalStage13057, _VARIANT_13057]
        | Annotated[_values.FormId, _VARIANT_13058]
        | Annotated[_values.FormId, _VARIANT_13059]
        | Annotated[_values.FormId, _VARIANT_13060]
        | Annotated[_values.FormId, _VARIANT_13061]
        | Annotated[_values.FormId, _VARIANT_13062]
        | Annotated[_values.FormId, _VARIANT_13063]
        | Annotated[_values.FormId, _VARIANT_13064]
        | Annotated[_values.FormId, _VARIANT_13065]
        | Annotated[_values.FormId, _VARIANT_13066]
        | Annotated[_values.FormId, _VARIANT_13067]
        | Annotated[_values.FormId, _VARIANT_13068]
        | Annotated[_values.FormId, _VARIANT_13069]
        | Annotated[_values.FormId, _VARIANT_13070]
        | Annotated[_values.FormId, _VARIANT_13071]
        | Annotated[_values.FormId, _VARIANT_13072]
        | Annotated[_values.FormId, _VARIANT_13073]
        | Annotated[_values.FormId, _VARIANT_13074]
        | Annotated[_values.FormId, _VARIANT_13075]
        | Annotated[_values.FormId, _VARIANT_13076]
        | Annotated[_values.FormId, _VARIANT_13077]
        | Annotated[_values.FormId, _VARIANT_13078]
        | Annotated[_values.FormId, _VARIANT_13079]
        | Annotated[VatsValueFunction13080, _VARIANT_13080]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13081,
        ]
        | Annotated[_values.FormId, _VARIANT_13082]
        | Annotated[_values.FormId, _VARIANT_13083]
        | Annotated[_values.FormId, _VARIANT_13084]
        | Annotated[PlayerAction13085, _VARIANT_13085]
        | Annotated[CastingType13086, _VARIANT_13086]
        | Annotated[_values.FormId, _VARIANT_13087]
        | Annotated[_values.FormId, _VARIANT_13088]
        | Annotated[_values.FormId, _VARIANT_13089]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13090,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13091,
        ]
        | Annotated[_values.FormId, _VARIANT_13092]
        | Annotated[FurnitureAnim13093, _VARIANT_13093]
        | Annotated[FurnitureEntry13094, _VARIANT_13094]
        | Annotated[_values.FormId, _VARIANT_13095]
        | Annotated[WardState13096, _VARIANT_13096]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13097,
        ]
        | Annotated[_values.FormId, _VARIANT_13098]
        | Annotated[_values.FormId, _VARIANT_13099]
        | Annotated[_values.FormId, _VARIANT_13100]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_13102]
        | Annotated[bytes, _VARIANT_13103]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13104,
        ]
        | Annotated[float, _VARIANT_13105]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13106,
        ]
        | Annotated[Sex13107, _VARIANT_13107]
        | Annotated[ActorValue13108, _VARIANT_13108]
        | Annotated[CrimeType13109, _VARIANT_13109]
        | Annotated[Axis13110, _VARIANT_13110]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13111,
        ]
        | Annotated[MiscStat13112, _VARIANT_13112]
        | Annotated[Alignment13113, _VARIANT_13113]
        | Annotated[_values.FormId, _VARIANT_13114]
        | Annotated[FormType13115, _VARIANT_13115]
        | Annotated[CriticalStage13116, _VARIANT_13116]
        | Annotated[_values.FormId, _VARIANT_13117]
        | Annotated[_values.FormId, _VARIANT_13118]
        | Annotated[_values.FormId, _VARIANT_13119]
        | Annotated[_values.FormId, _VARIANT_13120]
        | Annotated[_values.FormId, _VARIANT_13121]
        | Annotated[_values.FormId, _VARIANT_13122]
        | Annotated[_values.FormId, _VARIANT_13123]
        | Annotated[_values.FormId, _VARIANT_13124]
        | Annotated[_values.FormId, _VARIANT_13125]
        | Annotated[_values.FormId, _VARIANT_13126]
        | Annotated[_values.FormId, _VARIANT_13127]
        | Annotated[_values.FormId, _VARIANT_13128]
        | Annotated[_values.FormId, _VARIANT_13129]
        | Annotated[_values.FormId, _VARIANT_13130]
        | Annotated[_values.FormId, _VARIANT_13131]
        | Annotated[_values.FormId, _VARIANT_13132]
        | Annotated[_values.FormId, _VARIANT_13133]
        | Annotated[_values.FormId, _VARIANT_13134]
        | Annotated[_values.FormId, _VARIANT_13135]
        | Annotated[_values.FormId, _VARIANT_13136]
        | Annotated[_values.FormId, _VARIANT_13137]
        | Annotated[_values.FormId, _VARIANT_13138]
        | Annotated[VatsValueFunction13139, _VARIANT_13139]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13141]
            | Annotated[_values.FormId, _VARIANT_13142]
            | Annotated[_values.FormId, _VARIANT_13143]
            | Annotated[_values.FormId, _VARIANT_13144]
            | Annotated[bytes, _VARIANT_13145]
            | Annotated[TargetPart13146, _VARIANT_13146]
            | Annotated[VatsAction13147, _VARIANT_13147]
            | Annotated[bytes, _VARIANT_13148]
            | Annotated[bytes, _VARIANT_13149]
            | Annotated[_values.FormId, _VARIANT_13150]
            | Annotated[_values.FormId, _VARIANT_13151]
            | Annotated[bytes, _VARIANT_13152]
            | Annotated[bytes, _VARIANT_13153]
            | Annotated[bytes, _VARIANT_13154]
            | Annotated[bytes, _VARIANT_13155]
            | Annotated[WeaponType13156, _VARIANT_13156]
            | Annotated[bytes, _VARIANT_13157]
            | Annotated[bytes, _VARIANT_13158]
            | Annotated[ProjectileType13159, _VARIANT_13159]
            | Annotated[DeliveryType13160, _VARIANT_13160]
            | Annotated[CastingType13161, _VARIANT_13161],
            _VARIANT_13140,
        ]
        | Annotated[_values.FormId, _VARIANT_13162]
        | Annotated[_values.FormId, _VARIANT_13163]
        | Annotated[_values.FormId, _VARIANT_13164]
        | Annotated[PlayerAction13165, _VARIANT_13165]
        | Annotated[CastingType13166, _VARIANT_13166]
        | Annotated[_values.FormId, _VARIANT_13167]
        | Annotated[_values.FormId, _VARIANT_13168]
        | Annotated[_values.FormId, _VARIANT_13169]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13170,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13171,
        ]
        | Annotated[_values.FormId, _VARIANT_13172]
        | Annotated[FurnitureAnim13173, _VARIANT_13173]
        | Annotated[FurnitureEntry13174, _VARIANT_13174]
        | Annotated[_values.FormId, _VARIANT_13175]
        | Annotated[WardState13176, _VARIANT_13176]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13177,
        ]
        | Annotated[_values.FormId, _VARIANT_13178]
        | Annotated[_values.FormId, _VARIANT_13179]
        | Annotated[_values.FormId, _VARIANT_13180]
    )
    """Value decoded from this schema node."""

    run_on: RunOn13181
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13183,
        ]
        | Annotated[_values.FormId, _VARIANT_13184]
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
        Annotated[float, _VARIANT_13038]
        | Annotated[_values.FormId, _VARIANT_13039]
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
    def field(self, name: Literal["unused_13041"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13043]
        | Annotated[bytes, _VARIANT_13044]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13045,
        ]
        | Annotated[float, _VARIANT_13046]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13047,
        ]
        | Annotated[Sex13048, _VARIANT_13048]
        | Annotated[ActorValue13049, _VARIANT_13049]
        | Annotated[CrimeType13050, _VARIANT_13050]
        | Annotated[Axis13051, _VARIANT_13051]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13052,
        ]
        | Annotated[MiscStat13053, _VARIANT_13053]
        | Annotated[Alignment13054, _VARIANT_13054]
        | Annotated[_values.FormId, _VARIANT_13055]
        | Annotated[FormType13056, _VARIANT_13056]
        | Annotated[CriticalStage13057, _VARIANT_13057]
        | Annotated[_values.FormId, _VARIANT_13058]
        | Annotated[_values.FormId, _VARIANT_13059]
        | Annotated[_values.FormId, _VARIANT_13060]
        | Annotated[_values.FormId, _VARIANT_13061]
        | Annotated[_values.FormId, _VARIANT_13062]
        | Annotated[_values.FormId, _VARIANT_13063]
        | Annotated[_values.FormId, _VARIANT_13064]
        | Annotated[_values.FormId, _VARIANT_13065]
        | Annotated[_values.FormId, _VARIANT_13066]
        | Annotated[_values.FormId, _VARIANT_13067]
        | Annotated[_values.FormId, _VARIANT_13068]
        | Annotated[_values.FormId, _VARIANT_13069]
        | Annotated[_values.FormId, _VARIANT_13070]
        | Annotated[_values.FormId, _VARIANT_13071]
        | Annotated[_values.FormId, _VARIANT_13072]
        | Annotated[_values.FormId, _VARIANT_13073]
        | Annotated[_values.FormId, _VARIANT_13074]
        | Annotated[_values.FormId, _VARIANT_13075]
        | Annotated[_values.FormId, _VARIANT_13076]
        | Annotated[_values.FormId, _VARIANT_13077]
        | Annotated[_values.FormId, _VARIANT_13078]
        | Annotated[_values.FormId, _VARIANT_13079]
        | Annotated[VatsValueFunction13080, _VARIANT_13080]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13081,
        ]
        | Annotated[_values.FormId, _VARIANT_13082]
        | Annotated[_values.FormId, _VARIANT_13083]
        | Annotated[_values.FormId, _VARIANT_13084]
        | Annotated[PlayerAction13085, _VARIANT_13085]
        | Annotated[CastingType13086, _VARIANT_13086]
        | Annotated[_values.FormId, _VARIANT_13087]
        | Annotated[_values.FormId, _VARIANT_13088]
        | Annotated[_values.FormId, _VARIANT_13089]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13090,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13091,
        ]
        | Annotated[_values.FormId, _VARIANT_13092]
        | Annotated[FurnitureAnim13093, _VARIANT_13093]
        | Annotated[FurnitureEntry13094, _VARIANT_13094]
        | Annotated[_values.FormId, _VARIANT_13095]
        | Annotated[WardState13096, _VARIANT_13096]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13097,
        ]
        | Annotated[_values.FormId, _VARIANT_13098]
        | Annotated[_values.FormId, _VARIANT_13099]
        | Annotated[_values.FormId, _VARIANT_13100]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13102]
        | Annotated[bytes, _VARIANT_13103]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13104,
        ]
        | Annotated[float, _VARIANT_13105]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13106,
        ]
        | Annotated[Sex13107, _VARIANT_13107]
        | Annotated[ActorValue13108, _VARIANT_13108]
        | Annotated[CrimeType13109, _VARIANT_13109]
        | Annotated[Axis13110, _VARIANT_13110]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13111,
        ]
        | Annotated[MiscStat13112, _VARIANT_13112]
        | Annotated[Alignment13113, _VARIANT_13113]
        | Annotated[_values.FormId, _VARIANT_13114]
        | Annotated[FormType13115, _VARIANT_13115]
        | Annotated[CriticalStage13116, _VARIANT_13116]
        | Annotated[_values.FormId, _VARIANT_13117]
        | Annotated[_values.FormId, _VARIANT_13118]
        | Annotated[_values.FormId, _VARIANT_13119]
        | Annotated[_values.FormId, _VARIANT_13120]
        | Annotated[_values.FormId, _VARIANT_13121]
        | Annotated[_values.FormId, _VARIANT_13122]
        | Annotated[_values.FormId, _VARIANT_13123]
        | Annotated[_values.FormId, _VARIANT_13124]
        | Annotated[_values.FormId, _VARIANT_13125]
        | Annotated[_values.FormId, _VARIANT_13126]
        | Annotated[_values.FormId, _VARIANT_13127]
        | Annotated[_values.FormId, _VARIANT_13128]
        | Annotated[_values.FormId, _VARIANT_13129]
        | Annotated[_values.FormId, _VARIANT_13130]
        | Annotated[_values.FormId, _VARIANT_13131]
        | Annotated[_values.FormId, _VARIANT_13132]
        | Annotated[_values.FormId, _VARIANT_13133]
        | Annotated[_values.FormId, _VARIANT_13134]
        | Annotated[_values.FormId, _VARIANT_13135]
        | Annotated[_values.FormId, _VARIANT_13136]
        | Annotated[_values.FormId, _VARIANT_13137]
        | Annotated[_values.FormId, _VARIANT_13138]
        | Annotated[VatsValueFunction13139, _VARIANT_13139]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13141]
            | Annotated[_values.FormId, _VARIANT_13142]
            | Annotated[_values.FormId, _VARIANT_13143]
            | Annotated[_values.FormId, _VARIANT_13144]
            | Annotated[bytes, _VARIANT_13145]
            | Annotated[TargetPart13146, _VARIANT_13146]
            | Annotated[VatsAction13147, _VARIANT_13147]
            | Annotated[bytes, _VARIANT_13148]
            | Annotated[bytes, _VARIANT_13149]
            | Annotated[_values.FormId, _VARIANT_13150]
            | Annotated[_values.FormId, _VARIANT_13151]
            | Annotated[bytes, _VARIANT_13152]
            | Annotated[bytes, _VARIANT_13153]
            | Annotated[bytes, _VARIANT_13154]
            | Annotated[bytes, _VARIANT_13155]
            | Annotated[WeaponType13156, _VARIANT_13156]
            | Annotated[bytes, _VARIANT_13157]
            | Annotated[bytes, _VARIANT_13158]
            | Annotated[ProjectileType13159, _VARIANT_13159]
            | Annotated[DeliveryType13160, _VARIANT_13160]
            | Annotated[CastingType13161, _VARIANT_13161],
            _VARIANT_13140,
        ]
        | Annotated[_values.FormId, _VARIANT_13162]
        | Annotated[_values.FormId, _VARIANT_13163]
        | Annotated[_values.FormId, _VARIANT_13164]
        | Annotated[PlayerAction13165, _VARIANT_13165]
        | Annotated[CastingType13166, _VARIANT_13166]
        | Annotated[_values.FormId, _VARIANT_13167]
        | Annotated[_values.FormId, _VARIANT_13168]
        | Annotated[_values.FormId, _VARIANT_13169]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13170,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13171,
        ]
        | Annotated[_values.FormId, _VARIANT_13172]
        | Annotated[FurnitureAnim13173, _VARIANT_13173]
        | Annotated[FurnitureEntry13174, _VARIANT_13174]
        | Annotated[_values.FormId, _VARIANT_13175]
        | Annotated[WardState13176, _VARIANT_13176]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13177,
        ]
        | Annotated[_values.FormId, _VARIANT_13178]
        | Annotated[_values.FormId, _VARIANT_13179]
        | Annotated[_values.FormId, _VARIANT_13180]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn13181]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13183,
        ]
        | Annotated[_values.FormId, _VARIANT_13184]
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


class Condition13032(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
        "og Entry/1:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/1:Parameter #"
                "1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition/2:Parameter #"
                "2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure13034] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure13034]]:
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


class LogEntry13028(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:Log Entry"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "stage_flags": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/0:Stage Flags"
            ),
            kind="subrecord",
            name="Stage Flags",
        ),
        "conditions": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions"
            ),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/1:Conditions/repeat/0:Condition"
            ),
            child_kind="sequence",
        ),
        "log_entry": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/2:Log Entry"
            ),
            kind="subrecord",
            name="Log Entry",
        ),
        "next_quest": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/3:Next Quest"
            ),
            kind="subrecord",
            name="Next Quest",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/4:Unused"
            ),
            kind="subrecord",
            name="Unused",
        ),
        "unused_13196": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/5:Unused"
            ),
            kind="subrecord",
            name="Unused",
        ),
        "unused_13198": _base.Binding(
            path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:L"
                "og Entry/6:Unused"
            ),
            kind="subrecord",
            name="Unused",
        ),
    }

    stage_flags: Optional[CompleteQuestFailQuest13030] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition13032, ...] = ()
    """Value decoded from this schema node."""

    log_entry: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    next_quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unused: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_13196: Optional[bytes] = None
    """Value decoded from this schema node."""

    unused_13198: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["stage_flags"]
    ) -> _base.FieldRef[Optional[CompleteQuestFailQuest13030]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition13032, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["log_entry"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["next_quest"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_13196"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unused_13198"]
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


class Stage13021(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/10:Stages/repeat/0:Stage"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "stage_index": _base.Binding(
            path="QUST/10:Stages/repeat/0:Stage/0:Stage Index",
            kind="subrecord",
            name="Stage Index",
        ),
        "log_entries": _base.Binding(
            path="QUST/10:Stages/repeat/0:Stage/1:Log Entries",
            kind="repeat",
            name="Log Entries",
            repeated_path=(
                "QUST/10:Stages/repeat/0:Stage/1:Log Entries/repeat/0:Log Entry"
            ),
            child_kind="sequence",
        ),
    }

    stage_index: Optional[Structure13023] = None
    """Value decoded from this schema node."""

    log_entries: tuple[LogEntry13028, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["stage_index"]
    ) -> _base.FieldRef[Optional[Structure13023]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["log_entries"]
    ) -> _base.FieldRef[tuple[LogEntry13028, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class OredWithPrevious13205(enum.IntFlag):
    """Named values from the pinned schema."""

    ORED_WITH_PREVIOUS = 1


class Flags13213(enum.IntFlag):
    """Named values from the pinned schema."""

    COMPASS_MARKER_IGNORES_LOCKS = 1


class Structure13211(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/0:Target/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alias": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/0:Target/payload/0:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "flags": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/0:Target/payload/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/0:Target/payload/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    alias: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    flags: Flags13213
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags13213]:
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


_VARIANT_13222: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/2:Comparison Value/variants/0:Comparison Value - Fl"
        "oat"
    )
)


_VARIANT_13223: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/2:Comparison Value/variants/1:Comparison Value - Gl"
        "obal"
    )
)


_VARIANT_13227: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_13228: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/1:None"
    )
)


_VARIANT_13229: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/2:Integer"
    )
)


_VARIANT_13230: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/3:Float"
    )
)


_VARIANT_13231: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/4:Variable Name"
    )
)


class Sex13232(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13232: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/5:Sex"
    )
)


class ActorValue13233(_values.OpenIntEnum):
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


_VARIANT_13233: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType13234(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13234: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/7:Crime Type"
    )
)


class Axis13235(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13235: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/8:Axis"
    )
)


_VARIANT_13236: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat13237(_values.OpenIntEnum):
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


_VARIANT_13237: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment13238(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13238: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_13239: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/12:Equip Type"
    )
)


class FormType13240(_values.OpenIntEnum):
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


_VARIANT_13240: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage13241(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13241: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_13242: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_13243: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_13244: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/17:Actor"
    )
)


_VARIANT_13245: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_13246: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/19:Idle"
    )
)


_VARIANT_13247: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/20:Form List"
    )
)


_VARIANT_13248: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/21:Quest"
    )
)


_VARIANT_13249: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/22:Faction"
    )
)


_VARIANT_13250: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/23:Cell"
    )
)


_VARIANT_13251: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/24:Class"
    )
)


_VARIANT_13252: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/25:Race"
    )
)


_VARIANT_13253: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_13254: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/27:Global"
    )
)


_VARIANT_13255: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/28:Weather"
    )
)


_VARIANT_13256: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/29:Package"
    )
)


_VARIANT_13257: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_13258: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/31:Perk"
    )
)


_VARIANT_13259: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/32:Owner"
    )
)


_VARIANT_13260: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_13261: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_13262: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_13263: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction13264(_values.OpenIntEnum):
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


_VARIANT_13264: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_13265: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/38:VATS Value Param (INVALI"
        "D)"
    )
)


_VARIANT_13266: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_13267: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/40:Region"
    )
)


_VARIANT_13268: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction13269(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13269: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/42:Player Action"
    )
)


class CastingType13270(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13270: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_13271: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/44:Shout"
    )
)


_VARIANT_13272: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/45:Location"
    )
)


_VARIANT_13273: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_13274: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/47:Alias"
    )
)


_VARIANT_13275: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_13276: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim13277(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13277: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry13278(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13278: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_13279: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/52:Scene"
    )
)


class WardState13280(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13280: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_13281: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/54:Event"
    )
)


_VARIANT_13282: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_13283: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_13284: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/5:Parameter #1/variants/57:Faction"
    )
)


_VARIANT_13286: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_13287: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/1:None"
    )
)


_VARIANT_13288: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/2:Integer"
    )
)


_VARIANT_13289: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/3:Float"
    )
)


_VARIANT_13290: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/4:Variable Name"
    )
)


class Sex13291(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13291: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/5:Sex"
    )
)


class ActorValue13292(_values.OpenIntEnum):
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


_VARIANT_13292: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType13293(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13293: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/7:Crime Type"
    )
)


class Axis13294(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13294: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/8:Axis"
    )
)


_VARIANT_13295: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat13296(_values.OpenIntEnum):
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


_VARIANT_13296: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment13297(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13297: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_13298: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/12:Equip Type"
    )
)


class FormType13299(_values.OpenIntEnum):
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


_VARIANT_13299: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage13300(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13300: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_13301: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_13302: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_13303: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/17:Actor"
    )
)


_VARIANT_13304: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_13305: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/19:Idle"
    )
)


_VARIANT_13306: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/20:Form List"
    )
)


_VARIANT_13307: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/21:Quest"
    )
)


_VARIANT_13308: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/22:Faction"
    )
)


_VARIANT_13309: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/23:Cell"
    )
)


_VARIANT_13310: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/24:Class"
    )
)


_VARIANT_13311: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/25:Race"
    )
)


_VARIANT_13312: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_13313: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/27:Global"
    )
)


_VARIANT_13314: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/28:Weather"
    )
)


_VARIANT_13315: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/29:Package"
    )
)


_VARIANT_13316: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_13317: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/31:Perk"
    )
)


_VARIANT_13318: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/32:Owner"
    )
)


_VARIANT_13319: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_13320: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_13321: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_13322: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction13323(_values.OpenIntEnum):
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


_VARIANT_13323: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_13325: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/0:Weapon"
    )
)


_VARIANT_13326: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/1:Weapon List"
    )
)


_VARIANT_13327: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/2:Target"
    )
)


_VARIANT_13328: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/3:Target List"
    )
)


_VARIANT_13329: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/4:Unknown"
    )
)


class TargetPart13330(_values.OpenIntEnum):
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


_VARIANT_13330: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/5:Target Part"
    )
)


class VatsAction13331(_values.OpenIntEnum):
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


_VARIANT_13331: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/6:VATS Action"
    )
)


_VARIANT_13332: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/7:Unknown"
    )
)


_VARIANT_13333: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/8:Unknown"
    )
)


_VARIANT_13334: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/9:Critical Effect"
    )
)


_VARIANT_13335: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/10:Critical Effect List"
    )
)


_VARIANT_13336: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/11:Unknown"
    )
)


_VARIANT_13337: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/12:Unknown"
    )
)


_VARIANT_13338: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/13:Unknown"
    )
)


_VARIANT_13339: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/14:Unknown"
    )
)


class WeaponType13340(_values.OpenIntEnum):
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


_VARIANT_13340: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/15:Weapon Type"
    )
)


_VARIANT_13341: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/16:Unknown"
    )
)


_VARIANT_13342: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/17:Unknown"
    )
)


class ProjectileType13343(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_13343: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/18:Projectile Type"
    )
)


class DeliveryType13344(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_13344: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/19:Delivery Type"
    )
)


class CastingType13345(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_13345: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param/variant"
        "s/20:Casting Type"
    )
)


_VARIANT_13324: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_13346: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_13347: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/40:Region"
    )
)


_VARIANT_13348: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction13349(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13349: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/42:Player Action"
    )
)


class CastingType13350(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13350: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_13351: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/44:Shout"
    )
)


_VARIANT_13352: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/45:Location"
    )
)


_VARIANT_13353: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_13354: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/47:Alias"
    )
)


_VARIANT_13355: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_13356: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim13357(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13357: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry13358(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13358: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_13359: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/52:Scene"
    )
)


class WardState13360(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13360: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_13361: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/54:Event"
    )
)


_VARIANT_13362: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_13363: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_13364: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/6:Parameter #2/variants/57:Faction"
    )
)


class RunOn13365(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_13367: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/8:Reference/variants/0:Unused"
    )
)


_VARIANT_13368: _base.Variant = _base.Variant(
    path=(
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad/8:Reference/variants/1:Reference"
    )
)


class Structure13218(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
        "ad"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_13225": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA/paylo"
                "ad/9:Parameter #3"
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
        Annotated[float, _VARIANT_13222]
        | Annotated[_values.FormId, _VARIANT_13223]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_13225: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_13227]
        | Annotated[bytes, _VARIANT_13228]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13229,
        ]
        | Annotated[float, _VARIANT_13230]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13231,
        ]
        | Annotated[Sex13232, _VARIANT_13232]
        | Annotated[ActorValue13233, _VARIANT_13233]
        | Annotated[CrimeType13234, _VARIANT_13234]
        | Annotated[Axis13235, _VARIANT_13235]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13236,
        ]
        | Annotated[MiscStat13237, _VARIANT_13237]
        | Annotated[Alignment13238, _VARIANT_13238]
        | Annotated[_values.FormId, _VARIANT_13239]
        | Annotated[FormType13240, _VARIANT_13240]
        | Annotated[CriticalStage13241, _VARIANT_13241]
        | Annotated[_values.FormId, _VARIANT_13242]
        | Annotated[_values.FormId, _VARIANT_13243]
        | Annotated[_values.FormId, _VARIANT_13244]
        | Annotated[_values.FormId, _VARIANT_13245]
        | Annotated[_values.FormId, _VARIANT_13246]
        | Annotated[_values.FormId, _VARIANT_13247]
        | Annotated[_values.FormId, _VARIANT_13248]
        | Annotated[_values.FormId, _VARIANT_13249]
        | Annotated[_values.FormId, _VARIANT_13250]
        | Annotated[_values.FormId, _VARIANT_13251]
        | Annotated[_values.FormId, _VARIANT_13252]
        | Annotated[_values.FormId, _VARIANT_13253]
        | Annotated[_values.FormId, _VARIANT_13254]
        | Annotated[_values.FormId, _VARIANT_13255]
        | Annotated[_values.FormId, _VARIANT_13256]
        | Annotated[_values.FormId, _VARIANT_13257]
        | Annotated[_values.FormId, _VARIANT_13258]
        | Annotated[_values.FormId, _VARIANT_13259]
        | Annotated[_values.FormId, _VARIANT_13260]
        | Annotated[_values.FormId, _VARIANT_13261]
        | Annotated[_values.FormId, _VARIANT_13262]
        | Annotated[_values.FormId, _VARIANT_13263]
        | Annotated[VatsValueFunction13264, _VARIANT_13264]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13265,
        ]
        | Annotated[_values.FormId, _VARIANT_13266]
        | Annotated[_values.FormId, _VARIANT_13267]
        | Annotated[_values.FormId, _VARIANT_13268]
        | Annotated[PlayerAction13269, _VARIANT_13269]
        | Annotated[CastingType13270, _VARIANT_13270]
        | Annotated[_values.FormId, _VARIANT_13271]
        | Annotated[_values.FormId, _VARIANT_13272]
        | Annotated[_values.FormId, _VARIANT_13273]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13274,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13275,
        ]
        | Annotated[_values.FormId, _VARIANT_13276]
        | Annotated[FurnitureAnim13277, _VARIANT_13277]
        | Annotated[FurnitureEntry13278, _VARIANT_13278]
        | Annotated[_values.FormId, _VARIANT_13279]
        | Annotated[WardState13280, _VARIANT_13280]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13281,
        ]
        | Annotated[_values.FormId, _VARIANT_13282]
        | Annotated[_values.FormId, _VARIANT_13283]
        | Annotated[_values.FormId, _VARIANT_13284]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_13286]
        | Annotated[bytes, _VARIANT_13287]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13288,
        ]
        | Annotated[float, _VARIANT_13289]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13290,
        ]
        | Annotated[Sex13291, _VARIANT_13291]
        | Annotated[ActorValue13292, _VARIANT_13292]
        | Annotated[CrimeType13293, _VARIANT_13293]
        | Annotated[Axis13294, _VARIANT_13294]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13295,
        ]
        | Annotated[MiscStat13296, _VARIANT_13296]
        | Annotated[Alignment13297, _VARIANT_13297]
        | Annotated[_values.FormId, _VARIANT_13298]
        | Annotated[FormType13299, _VARIANT_13299]
        | Annotated[CriticalStage13300, _VARIANT_13300]
        | Annotated[_values.FormId, _VARIANT_13301]
        | Annotated[_values.FormId, _VARIANT_13302]
        | Annotated[_values.FormId, _VARIANT_13303]
        | Annotated[_values.FormId, _VARIANT_13304]
        | Annotated[_values.FormId, _VARIANT_13305]
        | Annotated[_values.FormId, _VARIANT_13306]
        | Annotated[_values.FormId, _VARIANT_13307]
        | Annotated[_values.FormId, _VARIANT_13308]
        | Annotated[_values.FormId, _VARIANT_13309]
        | Annotated[_values.FormId, _VARIANT_13310]
        | Annotated[_values.FormId, _VARIANT_13311]
        | Annotated[_values.FormId, _VARIANT_13312]
        | Annotated[_values.FormId, _VARIANT_13313]
        | Annotated[_values.FormId, _VARIANT_13314]
        | Annotated[_values.FormId, _VARIANT_13315]
        | Annotated[_values.FormId, _VARIANT_13316]
        | Annotated[_values.FormId, _VARIANT_13317]
        | Annotated[_values.FormId, _VARIANT_13318]
        | Annotated[_values.FormId, _VARIANT_13319]
        | Annotated[_values.FormId, _VARIANT_13320]
        | Annotated[_values.FormId, _VARIANT_13321]
        | Annotated[_values.FormId, _VARIANT_13322]
        | Annotated[VatsValueFunction13323, _VARIANT_13323]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13325]
            | Annotated[_values.FormId, _VARIANT_13326]
            | Annotated[_values.FormId, _VARIANT_13327]
            | Annotated[_values.FormId, _VARIANT_13328]
            | Annotated[bytes, _VARIANT_13329]
            | Annotated[TargetPart13330, _VARIANT_13330]
            | Annotated[VatsAction13331, _VARIANT_13331]
            | Annotated[bytes, _VARIANT_13332]
            | Annotated[bytes, _VARIANT_13333]
            | Annotated[_values.FormId, _VARIANT_13334]
            | Annotated[_values.FormId, _VARIANT_13335]
            | Annotated[bytes, _VARIANT_13336]
            | Annotated[bytes, _VARIANT_13337]
            | Annotated[bytes, _VARIANT_13338]
            | Annotated[bytes, _VARIANT_13339]
            | Annotated[WeaponType13340, _VARIANT_13340]
            | Annotated[bytes, _VARIANT_13341]
            | Annotated[bytes, _VARIANT_13342]
            | Annotated[ProjectileType13343, _VARIANT_13343]
            | Annotated[DeliveryType13344, _VARIANT_13344]
            | Annotated[CastingType13345, _VARIANT_13345],
            _VARIANT_13324,
        ]
        | Annotated[_values.FormId, _VARIANT_13346]
        | Annotated[_values.FormId, _VARIANT_13347]
        | Annotated[_values.FormId, _VARIANT_13348]
        | Annotated[PlayerAction13349, _VARIANT_13349]
        | Annotated[CastingType13350, _VARIANT_13350]
        | Annotated[_values.FormId, _VARIANT_13351]
        | Annotated[_values.FormId, _VARIANT_13352]
        | Annotated[_values.FormId, _VARIANT_13353]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13354,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13355,
        ]
        | Annotated[_values.FormId, _VARIANT_13356]
        | Annotated[FurnitureAnim13357, _VARIANT_13357]
        | Annotated[FurnitureEntry13358, _VARIANT_13358]
        | Annotated[_values.FormId, _VARIANT_13359]
        | Annotated[WardState13360, _VARIANT_13360]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13361,
        ]
        | Annotated[_values.FormId, _VARIANT_13362]
        | Annotated[_values.FormId, _VARIANT_13363]
        | Annotated[_values.FormId, _VARIANT_13364]
    )
    """Value decoded from this schema node."""

    run_on: RunOn13365
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13367,
        ]
        | Annotated[_values.FormId, _VARIANT_13368]
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
        Annotated[float, _VARIANT_13222]
        | Annotated[_values.FormId, _VARIANT_13223]
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
    def field(self, name: Literal["unused_13225"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13227]
        | Annotated[bytes, _VARIANT_13228]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13229,
        ]
        | Annotated[float, _VARIANT_13230]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13231,
        ]
        | Annotated[Sex13232, _VARIANT_13232]
        | Annotated[ActorValue13233, _VARIANT_13233]
        | Annotated[CrimeType13234, _VARIANT_13234]
        | Annotated[Axis13235, _VARIANT_13235]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13236,
        ]
        | Annotated[MiscStat13237, _VARIANT_13237]
        | Annotated[Alignment13238, _VARIANT_13238]
        | Annotated[_values.FormId, _VARIANT_13239]
        | Annotated[FormType13240, _VARIANT_13240]
        | Annotated[CriticalStage13241, _VARIANT_13241]
        | Annotated[_values.FormId, _VARIANT_13242]
        | Annotated[_values.FormId, _VARIANT_13243]
        | Annotated[_values.FormId, _VARIANT_13244]
        | Annotated[_values.FormId, _VARIANT_13245]
        | Annotated[_values.FormId, _VARIANT_13246]
        | Annotated[_values.FormId, _VARIANT_13247]
        | Annotated[_values.FormId, _VARIANT_13248]
        | Annotated[_values.FormId, _VARIANT_13249]
        | Annotated[_values.FormId, _VARIANT_13250]
        | Annotated[_values.FormId, _VARIANT_13251]
        | Annotated[_values.FormId, _VARIANT_13252]
        | Annotated[_values.FormId, _VARIANT_13253]
        | Annotated[_values.FormId, _VARIANT_13254]
        | Annotated[_values.FormId, _VARIANT_13255]
        | Annotated[_values.FormId, _VARIANT_13256]
        | Annotated[_values.FormId, _VARIANT_13257]
        | Annotated[_values.FormId, _VARIANT_13258]
        | Annotated[_values.FormId, _VARIANT_13259]
        | Annotated[_values.FormId, _VARIANT_13260]
        | Annotated[_values.FormId, _VARIANT_13261]
        | Annotated[_values.FormId, _VARIANT_13262]
        | Annotated[_values.FormId, _VARIANT_13263]
        | Annotated[VatsValueFunction13264, _VARIANT_13264]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13265,
        ]
        | Annotated[_values.FormId, _VARIANT_13266]
        | Annotated[_values.FormId, _VARIANT_13267]
        | Annotated[_values.FormId, _VARIANT_13268]
        | Annotated[PlayerAction13269, _VARIANT_13269]
        | Annotated[CastingType13270, _VARIANT_13270]
        | Annotated[_values.FormId, _VARIANT_13271]
        | Annotated[_values.FormId, _VARIANT_13272]
        | Annotated[_values.FormId, _VARIANT_13273]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13274,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13275,
        ]
        | Annotated[_values.FormId, _VARIANT_13276]
        | Annotated[FurnitureAnim13277, _VARIANT_13277]
        | Annotated[FurnitureEntry13278, _VARIANT_13278]
        | Annotated[_values.FormId, _VARIANT_13279]
        | Annotated[WardState13280, _VARIANT_13280]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13281,
        ]
        | Annotated[_values.FormId, _VARIANT_13282]
        | Annotated[_values.FormId, _VARIANT_13283]
        | Annotated[_values.FormId, _VARIANT_13284]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13286]
        | Annotated[bytes, _VARIANT_13287]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13288,
        ]
        | Annotated[float, _VARIANT_13289]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13290,
        ]
        | Annotated[Sex13291, _VARIANT_13291]
        | Annotated[ActorValue13292, _VARIANT_13292]
        | Annotated[CrimeType13293, _VARIANT_13293]
        | Annotated[Axis13294, _VARIANT_13294]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13295,
        ]
        | Annotated[MiscStat13296, _VARIANT_13296]
        | Annotated[Alignment13297, _VARIANT_13297]
        | Annotated[_values.FormId, _VARIANT_13298]
        | Annotated[FormType13299, _VARIANT_13299]
        | Annotated[CriticalStage13300, _VARIANT_13300]
        | Annotated[_values.FormId, _VARIANT_13301]
        | Annotated[_values.FormId, _VARIANT_13302]
        | Annotated[_values.FormId, _VARIANT_13303]
        | Annotated[_values.FormId, _VARIANT_13304]
        | Annotated[_values.FormId, _VARIANT_13305]
        | Annotated[_values.FormId, _VARIANT_13306]
        | Annotated[_values.FormId, _VARIANT_13307]
        | Annotated[_values.FormId, _VARIANT_13308]
        | Annotated[_values.FormId, _VARIANT_13309]
        | Annotated[_values.FormId, _VARIANT_13310]
        | Annotated[_values.FormId, _VARIANT_13311]
        | Annotated[_values.FormId, _VARIANT_13312]
        | Annotated[_values.FormId, _VARIANT_13313]
        | Annotated[_values.FormId, _VARIANT_13314]
        | Annotated[_values.FormId, _VARIANT_13315]
        | Annotated[_values.FormId, _VARIANT_13316]
        | Annotated[_values.FormId, _VARIANT_13317]
        | Annotated[_values.FormId, _VARIANT_13318]
        | Annotated[_values.FormId, _VARIANT_13319]
        | Annotated[_values.FormId, _VARIANT_13320]
        | Annotated[_values.FormId, _VARIANT_13321]
        | Annotated[_values.FormId, _VARIANT_13322]
        | Annotated[VatsValueFunction13323, _VARIANT_13323]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13325]
            | Annotated[_values.FormId, _VARIANT_13326]
            | Annotated[_values.FormId, _VARIANT_13327]
            | Annotated[_values.FormId, _VARIANT_13328]
            | Annotated[bytes, _VARIANT_13329]
            | Annotated[TargetPart13330, _VARIANT_13330]
            | Annotated[VatsAction13331, _VARIANT_13331]
            | Annotated[bytes, _VARIANT_13332]
            | Annotated[bytes, _VARIANT_13333]
            | Annotated[_values.FormId, _VARIANT_13334]
            | Annotated[_values.FormId, _VARIANT_13335]
            | Annotated[bytes, _VARIANT_13336]
            | Annotated[bytes, _VARIANT_13337]
            | Annotated[bytes, _VARIANT_13338]
            | Annotated[bytes, _VARIANT_13339]
            | Annotated[WeaponType13340, _VARIANT_13340]
            | Annotated[bytes, _VARIANT_13341]
            | Annotated[bytes, _VARIANT_13342]
            | Annotated[ProjectileType13343, _VARIANT_13343]
            | Annotated[DeliveryType13344, _VARIANT_13344]
            | Annotated[CastingType13345, _VARIANT_13345],
            _VARIANT_13324,
        ]
        | Annotated[_values.FormId, _VARIANT_13346]
        | Annotated[_values.FormId, _VARIANT_13347]
        | Annotated[_values.FormId, _VARIANT_13348]
        | Annotated[PlayerAction13349, _VARIANT_13349]
        | Annotated[CastingType13350, _VARIANT_13350]
        | Annotated[_values.FormId, _VARIANT_13351]
        | Annotated[_values.FormId, _VARIANT_13352]
        | Annotated[_values.FormId, _VARIANT_13353]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13354,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13355,
        ]
        | Annotated[_values.FormId, _VARIANT_13356]
        | Annotated[FurnitureAnim13357, _VARIANT_13357]
        | Annotated[FurnitureEntry13358, _VARIANT_13358]
        | Annotated[_values.FormId, _VARIANT_13359]
        | Annotated[WardState13360, _VARIANT_13360]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13361,
        ]
        | Annotated[_values.FormId, _VARIANT_13362]
        | Annotated[_values.FormId, _VARIANT_13363]
        | Annotated[_values.FormId, _VARIANT_13364]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn13365]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13367,
        ]
        | Annotated[_values.FormId, _VARIANT_13368]
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


class Condition13216(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
        "/0:Target/1:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/1:Parameter "
                "#1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition/2:Parameter "
                "#2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure13218] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure13218]]:
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


class Target13209(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat/0:Target"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "target": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/0:Target"
            ),
            kind="subrecord",
            name="Target",
        ),
        "conditions": _base.Binding(
            path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions"
            ),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target/1:Conditions/repeat/0:Condition"
            ),
            child_kind="sequence",
        ),
    }

    target: Optional[Structure13211] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition13216, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["target"]
    ) -> _base.FieldRef[Optional[Structure13211]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition13216, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Objective13201(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/11:Objectives/repeat/0:Objective"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "objective_index": _base.Binding(
            path=("QUST/11:Objectives/repeat/0:Objective/0:Objective Index"),
            kind="subrecord",
            name="Objective Index",
        ),
        "flags": _base.Binding(
            path="QUST/11:Objectives/repeat/0:Objective/1:Flags",
            kind="subrecord",
            name="Flags",
        ),
        "display_text": _base.Binding(
            path=("QUST/11:Objectives/repeat/0:Objective/2:Display Text"),
            kind="subrecord",
            name="Display Text",
        ),
        "targets": _base.Binding(
            path="QUST/11:Objectives/repeat/0:Objective/3:Targets",
            kind="repeat",
            name="Targets",
            repeated_path=(
                "QUST/11:Objectives/repeat/0:Objective/3:Targets/repeat"
                "/0:Target"
            ),
            child_kind="sequence",
        ),
    }

    objective_index: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ] = None
    """Value decoded from this schema node."""

    flags: Optional[OredWithPrevious13205] = None
    """Value decoded from this schema node."""

    display_text: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    targets: tuple[Target13209, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["objective_index"]
    ) -> _base.FieldRef[
        Optional[Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[OredWithPrevious13205]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["display_text"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["targets"]
    ) -> _base.FieldRef[tuple[Target13209, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags13385(enum.IntFlag):
    """Named values from the pinned schema."""

    RESERVES_LOCATION_REFERENCE = 1
    OPTIONAL = 2
    QUEST_OBJECT = 4
    ALLOW_REUSE_IN_QUEST = 8
    ALLOW_DEAD = 16
    MATCHING_REF_IN_LOADED_AREA = 32
    ESSENTIAL = 64
    ALLOW_DISABLED = 128
    STORES_TEXT = 256
    ALLOW_RESERVED = 512
    PROTECTED = 1024
    FORCED_BY_ALIASES = 2048
    ALLOW_DESTROYED = 4096
    MATCHING_REF_CLOSEST = 8192
    USES_STORED_TEXT = 16384
    INITIALLY_DISABLED = 32768


class AdditionalFlags13386(enum.IntFlag):
    """Named values from the pinned schema."""

    ALLOW_CLEARED = 1
    CLEAR_NAMES_WHEN_REMOVED = 2


class Structure13384(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/2:Alias Flags/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/2:Alias Flags/p"
                "ayload/0:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "additional_flags": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/2:Alias Flags/p"
                "ayload/1:Additional Flags"
            ),
            kind="primitive",
            name="Additional Flags",
        ),
    }

    flags: Flags13385
    """Value decoded from this schema node."""

    additional_flags: Optional[AdditionalFlags13386] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags13385]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["additional_flags"]
    ) -> _base.FieldRef[Optional[AdditionalFlags13386]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LocationAliasReference13395(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/7:Location Alias Reference"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/7:Location Alia"
                "s Reference/0:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
        "keyword": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/7:Location Alia"
                "s Reference/1:Keyword"
            ),
            kind="subrecord",
            name="Keyword",
        ),
        "ref_type": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/7:Location Alia"
                "s Reference/2:Ref Type"
            ),
            kind="subrecord",
            name="Ref Type",
        ),
    }

    alias: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    keyword: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ref_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alias"]
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
        self, name: Literal["keyword"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ref_type"]
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


class ExternalAliasReference13402(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/8:External Alias Reference"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "quest": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/8:External Alia"
                "s Reference/0:Quest"
            ),
            kind="subrecord",
            name="Quest",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/8:External Alia"
                "s Reference/1:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
    }

    quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["quest"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
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


class Create13413(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    AT = 0
    IN = 32768


class Structure13411(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Refere"
        "nce to Object/1:Alias/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Refere"
                "nce to Object/1:Alias/payload/0:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "create": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Refere"
                "nce to Object/1:Alias/payload/1:Create"
            ),
            kind="primitive",
            name="Create",
        ),
    }

    alias: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    create: Create13413
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["create"]) -> _base.FieldRef[Create13413]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class EasyMediumHardVeryHardNone13415(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EASY = 0
    MEDIUM = 1
    HARD = 2
    VERY_HARD = 3
    NONE = 4


class CreateReferenceToObject13407(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Reference to Object"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "object": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Refere"
                "nce to Object/0:Object"
            ),
            kind="subrecord",
            name="Object",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Refere"
                "nce to Object/1:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
        "level": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Refere"
                "nce to Object/2:Level"
            ),
            kind="subrecord",
            name="Level",
        ),
    }

    object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias: Optional[Structure13411] = None
    """Value decoded from this schema node."""

    level: Optional[EasyMediumHardVeryHardNone13415] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["object"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[Optional[Structure13411]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["level"]
    ) -> _base.FieldRef[Optional[EasyMediumHardVeryHardNone13415]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LinkedRefChild13420(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LINKED_REF_CHILD = 0


class FindMatchingReferenceNearAlias13416(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/10:Find Matchin"
        "g Reference Near Alias"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/10:Find Matchin"
                "g Reference Near Alias/0:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
        "type": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/10:Find Matchin"
                "g Reference Near Alias/1:Type"
            ),
            kind="subrecord",
            name="Type",
        ),
    }

    alias: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    type: Optional[LinkedRefChild13420] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alias"]
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
        self, name: Literal["type"]
    ) -> _base.FieldRef[Optional[LinkedRefChild13420]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FindMatchingReferenceFromEvent13421(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/11:Find Matchin"
        "g Reference From Event"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "from_event": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/11:Find Matchin"
                "g Reference From Event/0:From Event"
            ),
            kind="subrecord",
            name="From Event",
        ),
        "event_data": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/11:Find Matchin"
                "g Reference From Event/1:Event Data"
            ),
            kind="subrecord",
            name="Event Data",
        ),
    }

    from_event: Optional[str] = None
    """Value decoded from this schema node."""

    event_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["from_event"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["event_data"]
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


_VARIANT_13433: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/2:Comparison Value/va"
        "riants/0:Comparison Value - Float"
    )
)


_VARIANT_13434: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/2:Comparison Value/va"
        "riants/1:Comparison Value - Global"
    )
)


_VARIANT_13438: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/0:Unknown"
    )
)


_VARIANT_13439: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/1:None"
    )
)


_VARIANT_13440: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/2:Integer"
    )
)


_VARIANT_13441: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/3:Float"
    )
)


_VARIANT_13442: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/4:Variable Name"
    )
)


class Sex13443(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13443: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/5:Sex"
    )
)


class ActorValue13444(_values.OpenIntEnum):
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


_VARIANT_13444: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/6:Actor Value"
    )
)


class CrimeType13445(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13445: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/7:Crime Type"
    )
)


class Axis13446(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13446: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/8:Axis"
    )
)


_VARIANT_13447: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/9:Quest Stage (unused)"
    )
)


class MiscStat13448(_values.OpenIntEnum):
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


_VARIANT_13448: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/10:Misc Stat"
    )
)


class Alignment13449(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13449: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/11:Alignment"
    )
)


_VARIANT_13450: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/12:Equip Type"
    )
)


class FormType13451(_values.OpenIntEnum):
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


_VARIANT_13451: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/13:Form Type"
    )
)


class CriticalStage13452(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13452: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/14:Critical Stage"
    )
)


_VARIANT_13453: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/15:Object Reference"
    )
)


_VARIANT_13454: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/16:Inventory Object"
    )
)


_VARIANT_13455: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/17:Actor"
    )
)


_VARIANT_13456: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/18:Voice Type"
    )
)


_VARIANT_13457: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/19:Idle"
    )
)


_VARIANT_13458: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/20:Form List"
    )
)


_VARIANT_13459: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/21:Quest"
    )
)


_VARIANT_13460: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/22:Faction"
    )
)


_VARIANT_13461: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/23:Cell"
    )
)


_VARIANT_13462: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/24:Class"
    )
)


_VARIANT_13463: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/25:Race"
    )
)


_VARIANT_13464: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/26:Actor Base"
    )
)


_VARIANT_13465: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/27:Global"
    )
)


_VARIANT_13466: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/28:Weather"
    )
)


_VARIANT_13467: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/29:Package"
    )
)


_VARIANT_13468: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/30:Encounter Zone"
    )
)


_VARIANT_13469: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/31:Perk"
    )
)


_VARIANT_13470: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/32:Owner"
    )
)


_VARIANT_13471: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/33:Furniture"
    )
)


_VARIANT_13472: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/34:Effect Item"
    )
)


_VARIANT_13473: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/35:Base Effect"
    )
)


_VARIANT_13474: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/36:Worldspace"
    )
)


class VatsValueFunction13475(_values.OpenIntEnum):
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


_VARIANT_13475: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/37:VATS Value Function"
    )
)


_VARIANT_13476: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_13477: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/39:Referenceable Object"
    )
)


_VARIANT_13478: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/40:Region"
    )
)


_VARIANT_13479: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/41:Keyword"
    )
)


class PlayerAction13480(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13480: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/42:Player Action"
    )
)


class CastingType13481(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13481: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/43:Casting Type"
    )
)


_VARIANT_13482: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/44:Shout"
    )
)


_VARIANT_13483: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/45:Location"
    )
)


_VARIANT_13484: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/46:Location Ref Type"
    )
)


_VARIANT_13485: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/47:Alias"
    )
)


_VARIANT_13486: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/48:Packdata ID"
    )
)


_VARIANT_13487: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/49:Association Type"
    )
)


class FurnitureAnim13488(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13488: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/50:Furniture Anim"
    )
)


class FurnitureEntry13489(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13489: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/51:Furniture Entry"
    )
)


_VARIANT_13490: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/52:Scene"
    )
)


class WardState13491(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13491: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/53:Ward State"
    )
)


_VARIANT_13492: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/54:Event"
    )
)


_VARIANT_13493: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/55:Event Data"
    )
)


_VARIANT_13494: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/56:Knowable"
    )
)


_VARIANT_13495: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/57:Faction"
    )
)


_VARIANT_13497: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/0:Unknown"
    )
)


_VARIANT_13498: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/1:None"
    )
)


_VARIANT_13499: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/2:Integer"
    )
)


_VARIANT_13500: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/3:Float"
    )
)


_VARIANT_13501: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/4:Variable Name"
    )
)


class Sex13502(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13502: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/5:Sex"
    )
)


class ActorValue13503(_values.OpenIntEnum):
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


_VARIANT_13503: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/6:Actor Value"
    )
)


class CrimeType13504(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13504: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/7:Crime Type"
    )
)


class Axis13505(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13505: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/8:Axis"
    )
)


_VARIANT_13506: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/9:Quest Stage"
    )
)


class MiscStat13507(_values.OpenIntEnum):
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


_VARIANT_13507: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/10:Misc Stat"
    )
)


class Alignment13508(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13508: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/11:Alignment"
    )
)


_VARIANT_13509: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/12:Equip Type"
    )
)


class FormType13510(_values.OpenIntEnum):
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


_VARIANT_13510: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/13:Form Type"
    )
)


class CriticalStage13511(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13511: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/14:Critical Stage"
    )
)


_VARIANT_13512: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/15:Object Reference"
    )
)


_VARIANT_13513: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/16:Inventory Object"
    )
)


_VARIANT_13514: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/17:Actor"
    )
)


_VARIANT_13515: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/18:Voice Type"
    )
)


_VARIANT_13516: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/19:Idle"
    )
)


_VARIANT_13517: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/20:Form List"
    )
)


_VARIANT_13518: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/21:Quest"
    )
)


_VARIANT_13519: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/22:Faction"
    )
)


_VARIANT_13520: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/23:Cell"
    )
)


_VARIANT_13521: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/24:Class"
    )
)


_VARIANT_13522: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/25:Race"
    )
)


_VARIANT_13523: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/26:Actor Base"
    )
)


_VARIANT_13524: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/27:Global"
    )
)


_VARIANT_13525: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/28:Weather"
    )
)


_VARIANT_13526: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/29:Package"
    )
)


_VARIANT_13527: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/30:Encounter Zone"
    )
)


_VARIANT_13528: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/31:Perk"
    )
)


_VARIANT_13529: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/32:Owner"
    )
)


_VARIANT_13530: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/33:Furniture"
    )
)


_VARIANT_13531: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/34:Effect Item"
    )
)


_VARIANT_13532: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/35:Base Effect"
    )
)


_VARIANT_13533: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/36:Worldspace"
    )
)


class VatsValueFunction13534(_values.OpenIntEnum):
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


_VARIANT_13534: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/37:VATS Value Function"
    )
)


_VARIANT_13536: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/0:Weapon"
    )
)


_VARIANT_13537: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/1:Weapon List"
    )
)


_VARIANT_13538: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/2:Target"
    )
)


_VARIANT_13539: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/3:Target List"
    )
)


_VARIANT_13540: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/4:Unknown"
    )
)


class TargetPart13541(_values.OpenIntEnum):
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


_VARIANT_13541: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/5:Target Part"
    )
)


class VatsAction13542(_values.OpenIntEnum):
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


_VARIANT_13542: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/6:VATS Action"
    )
)


_VARIANT_13543: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/7:Unknown"
    )
)


_VARIANT_13544: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/8:Unknown"
    )
)


_VARIANT_13545: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/9:Critical Effect"
    )
)


_VARIANT_13546: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/10:Critical Effect Lis"
        "t"
    )
)


_VARIANT_13547: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/11:Unknown"
    )
)


_VARIANT_13548: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/12:Unknown"
    )
)


_VARIANT_13549: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/13:Unknown"
    )
)


_VARIANT_13550: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/14:Unknown"
    )
)


class WeaponType13551(_values.OpenIntEnum):
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


_VARIANT_13551: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_13552: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/16:Unknown"
    )
)


_VARIANT_13553: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/17:Unknown"
    )
)


class ProjectileType13554(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_13554: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/18:Projectile Type"
    )
)


class DeliveryType13555(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_13555: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/19:Delivery Type"
    )
)


class CastingType13556(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_13556: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/20:Casting Type"
    )
)


_VARIANT_13535: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param"
    )
)


_VARIANT_13557: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/39:Referenceable Object"
    )
)


_VARIANT_13558: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/40:Region"
    )
)


_VARIANT_13559: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/41:Keyword"
    )
)


class PlayerAction13560(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13560: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/42:Player Action"
    )
)


class CastingType13561(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13561: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/43:Casting Type"
    )
)


_VARIANT_13562: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/44:Shout"
    )
)


_VARIANT_13563: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/45:Location"
    )
)


_VARIANT_13564: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/46:Location Ref Type"
    )
)


_VARIANT_13565: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/47:Alias"
    )
)


_VARIANT_13566: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/48:Packdata ID"
    )
)


_VARIANT_13567: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/49:Association Type"
    )
)


class FurnitureAnim13568(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13568: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/50:Furniture Anim"
    )
)


class FurnitureEntry13569(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13569: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/51:Furniture Entry"
    )
)


_VARIANT_13570: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/52:Scene"
    )
)


class WardState13571(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13571: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/53:Ward State"
    )
)


_VARIANT_13572: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/54:Event"
    )
)


_VARIANT_13573: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/55:Event Data"
    )
)


_VARIANT_13574: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/56:Knowable"
    )
)


_VARIANT_13575: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/57:Faction"
    )
)


class RunOn13576(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_13578: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/8:Reference/variants/"
        "0:Unused"
    )
)


_VARIANT_13579: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/8:Reference/variants/"
        "1:Reference"
    )
)


class Structure13429(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_13436": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/9:Parameter #3"
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
        Annotated[float, _VARIANT_13433]
        | Annotated[_values.FormId, _VARIANT_13434]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_13436: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_13438]
        | Annotated[bytes, _VARIANT_13439]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13440,
        ]
        | Annotated[float, _VARIANT_13441]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13442,
        ]
        | Annotated[Sex13443, _VARIANT_13443]
        | Annotated[ActorValue13444, _VARIANT_13444]
        | Annotated[CrimeType13445, _VARIANT_13445]
        | Annotated[Axis13446, _VARIANT_13446]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13447,
        ]
        | Annotated[MiscStat13448, _VARIANT_13448]
        | Annotated[Alignment13449, _VARIANT_13449]
        | Annotated[_values.FormId, _VARIANT_13450]
        | Annotated[FormType13451, _VARIANT_13451]
        | Annotated[CriticalStage13452, _VARIANT_13452]
        | Annotated[_values.FormId, _VARIANT_13453]
        | Annotated[_values.FormId, _VARIANT_13454]
        | Annotated[_values.FormId, _VARIANT_13455]
        | Annotated[_values.FormId, _VARIANT_13456]
        | Annotated[_values.FormId, _VARIANT_13457]
        | Annotated[_values.FormId, _VARIANT_13458]
        | Annotated[_values.FormId, _VARIANT_13459]
        | Annotated[_values.FormId, _VARIANT_13460]
        | Annotated[_values.FormId, _VARIANT_13461]
        | Annotated[_values.FormId, _VARIANT_13462]
        | Annotated[_values.FormId, _VARIANT_13463]
        | Annotated[_values.FormId, _VARIANT_13464]
        | Annotated[_values.FormId, _VARIANT_13465]
        | Annotated[_values.FormId, _VARIANT_13466]
        | Annotated[_values.FormId, _VARIANT_13467]
        | Annotated[_values.FormId, _VARIANT_13468]
        | Annotated[_values.FormId, _VARIANT_13469]
        | Annotated[_values.FormId, _VARIANT_13470]
        | Annotated[_values.FormId, _VARIANT_13471]
        | Annotated[_values.FormId, _VARIANT_13472]
        | Annotated[_values.FormId, _VARIANT_13473]
        | Annotated[_values.FormId, _VARIANT_13474]
        | Annotated[VatsValueFunction13475, _VARIANT_13475]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13476,
        ]
        | Annotated[_values.FormId, _VARIANT_13477]
        | Annotated[_values.FormId, _VARIANT_13478]
        | Annotated[_values.FormId, _VARIANT_13479]
        | Annotated[PlayerAction13480, _VARIANT_13480]
        | Annotated[CastingType13481, _VARIANT_13481]
        | Annotated[_values.FormId, _VARIANT_13482]
        | Annotated[_values.FormId, _VARIANT_13483]
        | Annotated[_values.FormId, _VARIANT_13484]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13485,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13486,
        ]
        | Annotated[_values.FormId, _VARIANT_13487]
        | Annotated[FurnitureAnim13488, _VARIANT_13488]
        | Annotated[FurnitureEntry13489, _VARIANT_13489]
        | Annotated[_values.FormId, _VARIANT_13490]
        | Annotated[WardState13491, _VARIANT_13491]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13492,
        ]
        | Annotated[_values.FormId, _VARIANT_13493]
        | Annotated[_values.FormId, _VARIANT_13494]
        | Annotated[_values.FormId, _VARIANT_13495]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_13497]
        | Annotated[bytes, _VARIANT_13498]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13499,
        ]
        | Annotated[float, _VARIANT_13500]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13501,
        ]
        | Annotated[Sex13502, _VARIANT_13502]
        | Annotated[ActorValue13503, _VARIANT_13503]
        | Annotated[CrimeType13504, _VARIANT_13504]
        | Annotated[Axis13505, _VARIANT_13505]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13506,
        ]
        | Annotated[MiscStat13507, _VARIANT_13507]
        | Annotated[Alignment13508, _VARIANT_13508]
        | Annotated[_values.FormId, _VARIANT_13509]
        | Annotated[FormType13510, _VARIANT_13510]
        | Annotated[CriticalStage13511, _VARIANT_13511]
        | Annotated[_values.FormId, _VARIANT_13512]
        | Annotated[_values.FormId, _VARIANT_13513]
        | Annotated[_values.FormId, _VARIANT_13514]
        | Annotated[_values.FormId, _VARIANT_13515]
        | Annotated[_values.FormId, _VARIANT_13516]
        | Annotated[_values.FormId, _VARIANT_13517]
        | Annotated[_values.FormId, _VARIANT_13518]
        | Annotated[_values.FormId, _VARIANT_13519]
        | Annotated[_values.FormId, _VARIANT_13520]
        | Annotated[_values.FormId, _VARIANT_13521]
        | Annotated[_values.FormId, _VARIANT_13522]
        | Annotated[_values.FormId, _VARIANT_13523]
        | Annotated[_values.FormId, _VARIANT_13524]
        | Annotated[_values.FormId, _VARIANT_13525]
        | Annotated[_values.FormId, _VARIANT_13526]
        | Annotated[_values.FormId, _VARIANT_13527]
        | Annotated[_values.FormId, _VARIANT_13528]
        | Annotated[_values.FormId, _VARIANT_13529]
        | Annotated[_values.FormId, _VARIANT_13530]
        | Annotated[_values.FormId, _VARIANT_13531]
        | Annotated[_values.FormId, _VARIANT_13532]
        | Annotated[_values.FormId, _VARIANT_13533]
        | Annotated[VatsValueFunction13534, _VARIANT_13534]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13536]
            | Annotated[_values.FormId, _VARIANT_13537]
            | Annotated[_values.FormId, _VARIANT_13538]
            | Annotated[_values.FormId, _VARIANT_13539]
            | Annotated[bytes, _VARIANT_13540]
            | Annotated[TargetPart13541, _VARIANT_13541]
            | Annotated[VatsAction13542, _VARIANT_13542]
            | Annotated[bytes, _VARIANT_13543]
            | Annotated[bytes, _VARIANT_13544]
            | Annotated[_values.FormId, _VARIANT_13545]
            | Annotated[_values.FormId, _VARIANT_13546]
            | Annotated[bytes, _VARIANT_13547]
            | Annotated[bytes, _VARIANT_13548]
            | Annotated[bytes, _VARIANT_13549]
            | Annotated[bytes, _VARIANT_13550]
            | Annotated[WeaponType13551, _VARIANT_13551]
            | Annotated[bytes, _VARIANT_13552]
            | Annotated[bytes, _VARIANT_13553]
            | Annotated[ProjectileType13554, _VARIANT_13554]
            | Annotated[DeliveryType13555, _VARIANT_13555]
            | Annotated[CastingType13556, _VARIANT_13556],
            _VARIANT_13535,
        ]
        | Annotated[_values.FormId, _VARIANT_13557]
        | Annotated[_values.FormId, _VARIANT_13558]
        | Annotated[_values.FormId, _VARIANT_13559]
        | Annotated[PlayerAction13560, _VARIANT_13560]
        | Annotated[CastingType13561, _VARIANT_13561]
        | Annotated[_values.FormId, _VARIANT_13562]
        | Annotated[_values.FormId, _VARIANT_13563]
        | Annotated[_values.FormId, _VARIANT_13564]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13565,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13566,
        ]
        | Annotated[_values.FormId, _VARIANT_13567]
        | Annotated[FurnitureAnim13568, _VARIANT_13568]
        | Annotated[FurnitureEntry13569, _VARIANT_13569]
        | Annotated[_values.FormId, _VARIANT_13570]
        | Annotated[WardState13571, _VARIANT_13571]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13572,
        ]
        | Annotated[_values.FormId, _VARIANT_13573]
        | Annotated[_values.FormId, _VARIANT_13574]
        | Annotated[_values.FormId, _VARIANT_13575]
    )
    """Value decoded from this schema node."""

    run_on: RunOn13576
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13578,
        ]
        | Annotated[_values.FormId, _VARIANT_13579]
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
        Annotated[float, _VARIANT_13433]
        | Annotated[_values.FormId, _VARIANT_13434]
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
    def field(self, name: Literal["unused_13436"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13438]
        | Annotated[bytes, _VARIANT_13439]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13440,
        ]
        | Annotated[float, _VARIANT_13441]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13442,
        ]
        | Annotated[Sex13443, _VARIANT_13443]
        | Annotated[ActorValue13444, _VARIANT_13444]
        | Annotated[CrimeType13445, _VARIANT_13445]
        | Annotated[Axis13446, _VARIANT_13446]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13447,
        ]
        | Annotated[MiscStat13448, _VARIANT_13448]
        | Annotated[Alignment13449, _VARIANT_13449]
        | Annotated[_values.FormId, _VARIANT_13450]
        | Annotated[FormType13451, _VARIANT_13451]
        | Annotated[CriticalStage13452, _VARIANT_13452]
        | Annotated[_values.FormId, _VARIANT_13453]
        | Annotated[_values.FormId, _VARIANT_13454]
        | Annotated[_values.FormId, _VARIANT_13455]
        | Annotated[_values.FormId, _VARIANT_13456]
        | Annotated[_values.FormId, _VARIANT_13457]
        | Annotated[_values.FormId, _VARIANT_13458]
        | Annotated[_values.FormId, _VARIANT_13459]
        | Annotated[_values.FormId, _VARIANT_13460]
        | Annotated[_values.FormId, _VARIANT_13461]
        | Annotated[_values.FormId, _VARIANT_13462]
        | Annotated[_values.FormId, _VARIANT_13463]
        | Annotated[_values.FormId, _VARIANT_13464]
        | Annotated[_values.FormId, _VARIANT_13465]
        | Annotated[_values.FormId, _VARIANT_13466]
        | Annotated[_values.FormId, _VARIANT_13467]
        | Annotated[_values.FormId, _VARIANT_13468]
        | Annotated[_values.FormId, _VARIANT_13469]
        | Annotated[_values.FormId, _VARIANT_13470]
        | Annotated[_values.FormId, _VARIANT_13471]
        | Annotated[_values.FormId, _VARIANT_13472]
        | Annotated[_values.FormId, _VARIANT_13473]
        | Annotated[_values.FormId, _VARIANT_13474]
        | Annotated[VatsValueFunction13475, _VARIANT_13475]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13476,
        ]
        | Annotated[_values.FormId, _VARIANT_13477]
        | Annotated[_values.FormId, _VARIANT_13478]
        | Annotated[_values.FormId, _VARIANT_13479]
        | Annotated[PlayerAction13480, _VARIANT_13480]
        | Annotated[CastingType13481, _VARIANT_13481]
        | Annotated[_values.FormId, _VARIANT_13482]
        | Annotated[_values.FormId, _VARIANT_13483]
        | Annotated[_values.FormId, _VARIANT_13484]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13485,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13486,
        ]
        | Annotated[_values.FormId, _VARIANT_13487]
        | Annotated[FurnitureAnim13488, _VARIANT_13488]
        | Annotated[FurnitureEntry13489, _VARIANT_13489]
        | Annotated[_values.FormId, _VARIANT_13490]
        | Annotated[WardState13491, _VARIANT_13491]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13492,
        ]
        | Annotated[_values.FormId, _VARIANT_13493]
        | Annotated[_values.FormId, _VARIANT_13494]
        | Annotated[_values.FormId, _VARIANT_13495]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13497]
        | Annotated[bytes, _VARIANT_13498]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13499,
        ]
        | Annotated[float, _VARIANT_13500]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13501,
        ]
        | Annotated[Sex13502, _VARIANT_13502]
        | Annotated[ActorValue13503, _VARIANT_13503]
        | Annotated[CrimeType13504, _VARIANT_13504]
        | Annotated[Axis13505, _VARIANT_13505]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13506,
        ]
        | Annotated[MiscStat13507, _VARIANT_13507]
        | Annotated[Alignment13508, _VARIANT_13508]
        | Annotated[_values.FormId, _VARIANT_13509]
        | Annotated[FormType13510, _VARIANT_13510]
        | Annotated[CriticalStage13511, _VARIANT_13511]
        | Annotated[_values.FormId, _VARIANT_13512]
        | Annotated[_values.FormId, _VARIANT_13513]
        | Annotated[_values.FormId, _VARIANT_13514]
        | Annotated[_values.FormId, _VARIANT_13515]
        | Annotated[_values.FormId, _VARIANT_13516]
        | Annotated[_values.FormId, _VARIANT_13517]
        | Annotated[_values.FormId, _VARIANT_13518]
        | Annotated[_values.FormId, _VARIANT_13519]
        | Annotated[_values.FormId, _VARIANT_13520]
        | Annotated[_values.FormId, _VARIANT_13521]
        | Annotated[_values.FormId, _VARIANT_13522]
        | Annotated[_values.FormId, _VARIANT_13523]
        | Annotated[_values.FormId, _VARIANT_13524]
        | Annotated[_values.FormId, _VARIANT_13525]
        | Annotated[_values.FormId, _VARIANT_13526]
        | Annotated[_values.FormId, _VARIANT_13527]
        | Annotated[_values.FormId, _VARIANT_13528]
        | Annotated[_values.FormId, _VARIANT_13529]
        | Annotated[_values.FormId, _VARIANT_13530]
        | Annotated[_values.FormId, _VARIANT_13531]
        | Annotated[_values.FormId, _VARIANT_13532]
        | Annotated[_values.FormId, _VARIANT_13533]
        | Annotated[VatsValueFunction13534, _VARIANT_13534]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13536]
            | Annotated[_values.FormId, _VARIANT_13537]
            | Annotated[_values.FormId, _VARIANT_13538]
            | Annotated[_values.FormId, _VARIANT_13539]
            | Annotated[bytes, _VARIANT_13540]
            | Annotated[TargetPart13541, _VARIANT_13541]
            | Annotated[VatsAction13542, _VARIANT_13542]
            | Annotated[bytes, _VARIANT_13543]
            | Annotated[bytes, _VARIANT_13544]
            | Annotated[_values.FormId, _VARIANT_13545]
            | Annotated[_values.FormId, _VARIANT_13546]
            | Annotated[bytes, _VARIANT_13547]
            | Annotated[bytes, _VARIANT_13548]
            | Annotated[bytes, _VARIANT_13549]
            | Annotated[bytes, _VARIANT_13550]
            | Annotated[WeaponType13551, _VARIANT_13551]
            | Annotated[bytes, _VARIANT_13552]
            | Annotated[bytes, _VARIANT_13553]
            | Annotated[ProjectileType13554, _VARIANT_13554]
            | Annotated[DeliveryType13555, _VARIANT_13555]
            | Annotated[CastingType13556, _VARIANT_13556],
            _VARIANT_13535,
        ]
        | Annotated[_values.FormId, _VARIANT_13557]
        | Annotated[_values.FormId, _VARIANT_13558]
        | Annotated[_values.FormId, _VARIANT_13559]
        | Annotated[PlayerAction13560, _VARIANT_13560]
        | Annotated[CastingType13561, _VARIANT_13561]
        | Annotated[_values.FormId, _VARIANT_13562]
        | Annotated[_values.FormId, _VARIANT_13563]
        | Annotated[_values.FormId, _VARIANT_13564]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13565,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13566,
        ]
        | Annotated[_values.FormId, _VARIANT_13567]
        | Annotated[FurnitureAnim13568, _VARIANT_13568]
        | Annotated[FurnitureEntry13569, _VARIANT_13569]
        | Annotated[_values.FormId, _VARIANT_13570]
        | Annotated[WardState13571, _VARIANT_13571]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13572,
        ]
        | Annotated[_values.FormId, _VARIANT_13573]
        | Annotated[_values.FormId, _VARIANT_13574]
        | Annotated[_values.FormId, _VARIANT_13575]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn13576]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13578,
        ]
        | Annotated[_values.FormId, _VARIANT_13579]
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


class Condition13427(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
        "epeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure13429] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure13429]]:
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


class Structure13595(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
        "/0:Item/0:Item/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
                "/0:Item/0:Item/payload/0:Item"
            ),
            kind="primitive",
            name="Item",
        ),
        "count": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
                "/0:Item/0:Item/payload/1:Count"
            ),
            kind="primitive",
            name="Count",
        ),
    }

    item: _values.FormId
    """Value decoded from this schema node."""

    count: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["item"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
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


_VARIANT_13602: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
        "red Rank/variants/0:Unused"
    )
)


_VARIANT_13603: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
        "red Rank/variants/1:Global Variable"
    )
)


_VARIANT_13604: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
        "red Rank/variants/2:Required Rank"
    )
)


class Structure13599(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data/payload/0:Owner"
            ),
            kind="primitive",
            name="Owner",
        ),
        "global_variable_required_rank": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
                "red Rank"
            ),
            kind="union",
            name="Global Variable / Required Rank",
        ),
        "item_condition": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data/payload/2:Item Condition"
            ),
            kind="primitive",
            name="Item Condition",
        ),
    }

    owner: _values.FormId
    """Value decoded from this schema node."""

    global_variable_required_rank: (
        Annotated[bytes, _VARIANT_13602]
        | Annotated[_values.FormId, _VARIANT_13603]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13604,
        ]
    )
    """Value decoded from this schema node."""

    item_condition: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["owner"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["global_variable_required_rank"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13602]
        | Annotated[_values.FormId, _VARIANT_13603]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13604,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["item_condition"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Item13593(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat/0:Item"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
                "/0:Item/0:Item"
            ),
            kind="subrecord",
            name="Item",
        ),
        "extra_data": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data"
            ),
            kind="subrecord",
            name="Extra Data",
        ),
    }

    item: Optional[Structure13595] = None
    """Value decoded from this schema node."""

    extra_data: Optional[Structure13599] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["item"]
    ) -> _base.FieldRef[Optional[Structure13595]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["extra_data"]
    ) -> _base.FieldRef[Optional[Structure13599]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Alias13378(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/13:Aliases/repeat/0:Alias/0:Alias"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "reference_alias_id": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/0:Reference Alias ID"
            ),
            kind="subrecord",
            name="Reference Alias ID",
        ),
        "alias_name": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/1:Alias Name"),
            kind="subrecord",
            name="Alias Name",
        ),
        "alias_flags": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/2:Alias Flags"),
            kind="subrecord",
            name="Alias Flags",
        ),
        "force_into_alias_when_filled": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/3:Force Into Al"
                "ias When Filled"
            ),
            kind="subrecord",
            name="Force Into Alias When Filled",
        ),
        "specific_location": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/4:Specific Location"),
            kind="subrecord",
            name="Specific Location",
        ),
        "forced_reference": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/5:Forced Reference"),
            kind="subrecord",
            name="Forced Reference",
        ),
        "unique_actor": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/6:Unique Actor"),
            kind="subrecord",
            name="Unique Actor",
        ),
        "location_alias_reference": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/7:Location Alia"
                "s Reference"
            ),
            kind="sequence",
            name="Location Alias Reference",
        ),
        "external_alias_reference": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/8:External Alia"
                "s Reference"
            ),
            kind="sequence",
            name="External Alias Reference",
        ),
        "create_reference_to_object": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/9:Create Refere"
                "nce to Object"
            ),
            kind="sequence",
            name="Create Reference to Object",
        ),
        "find_matching_reference_near_alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/10:Find Matchin"
                "g Reference Near Alias"
            ),
            kind="sequence",
            name="Find Matching Reference Near Alias",
        ),
        "find_matching_reference_from_event": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/11:Find Matchin"
                "g Reference From Event"
            ),
            kind="sequence",
            name="Find Matching Reference From Event",
        ),
        "conditions": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions"),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/12:Conditions/r"
                "epeat/0:Condition"
            ),
            child_kind="sequence",
        ),
        "keyword_count": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/13:Keyword Count"),
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/14:Keywords"),
            kind="subrecord",
            name="Keywords",
        ),
        "count": _base.Binding(
            path="QUST/13:Aliases/repeat/0:Alias/0:Alias/15:Count",
            kind="subrecord",
            name="Count",
        ),
        "items": _base.Binding(
            path="QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items",
            kind="repeat",
            name="Items",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/16:Items/repeat/0:Item"
            ),
            child_kind="sequence",
        ),
        "spectator_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/17:Spectator ov"
                "erride package list"
            ),
            kind="subrecord",
            name="Spectator override package list",
        ),
        "observe_dead_body_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/18:Observe dead"
                " body override package list"
            ),
            kind="subrecord",
            name="Observe dead body override package list",
        ),
        "guard_warn_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/19:Guard warn o"
                "verride package list"
            ),
            kind="subrecord",
            name="Guard warn override package list",
        ),
        "combat_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/20:Combat overr"
                "ide package list"
            ),
            kind="subrecord",
            name="Combat override package list",
        ),
        "display_name": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/21:Display Name"),
            kind="subrecord",
            name="Display Name",
        ),
        "alias_spells": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/22:Alias Spells"),
            kind="repeat",
            name="Alias Spells",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/22:Alias Spells"
                "/repeat/0:Spell"
            ),
            child_kind="subrecord",
        ),
        "alias_factions": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/23:Alias Factions"),
            kind="repeat",
            name="Alias Factions",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/23:Alias Factio"
                "ns/repeat/0:Faction"
            ),
            child_kind="subrecord",
        ),
        "alias_package_data": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/24:Alias Package Data"
            ),
            kind="repeat",
            name="Alias Package Data",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/0:Alias/24:Alias Packag"
                "e Data/repeat/0:Package"
            ),
            child_kind="subrecord",
        ),
        "voice_types": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/25:Voice Types"),
            kind="subrecord",
            name="Voice Types",
        ),
        "alias_end": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/0:Alias/26:Alias End"),
            kind="subrecord",
            name="Alias End",
        ),
    }

    reference_alias_id: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    alias_name: Optional[str] = None
    """Value decoded from this schema node."""

    alias_flags: Optional[Structure13384] = None
    """Value decoded from this schema node."""

    force_into_alias_when_filled: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    specific_location: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    forced_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unique_actor: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    location_alias_reference: Optional[LocationAliasReference13395] = None
    """Value decoded from this schema node."""

    external_alias_reference: Optional[ExternalAliasReference13402] = None
    """Value decoded from this schema node."""

    create_reference_to_object: Optional[CreateReferenceToObject13407] = None
    """Value decoded from this schema node."""

    find_matching_reference_near_alias: Optional[
        FindMatchingReferenceNearAlias13416
    ] = None
    """Value decoded from this schema node."""

    find_matching_reference_from_event: Optional[
        FindMatchingReferenceFromEvent13421
    ] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition13427, ...] = ()
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    items: tuple[Item13593, ...] = ()
    """Value decoded from this schema node."""

    spectator_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    observe_dead_body_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    guard_warn_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    combat_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    display_name: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias_spells: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    alias_factions: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    alias_package_data: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    voice_types: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias_end: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["reference_alias_id"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_flags"]
    ) -> _base.FieldRef[Optional[Structure13384]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["force_into_alias_when_filled"]
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
        self, name: Literal["specific_location"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["forced_reference"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unique_actor"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location_alias_reference"]
    ) -> _base.FieldRef[Optional[LocationAliasReference13395]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["external_alias_reference"]
    ) -> _base.FieldRef[Optional[ExternalAliasReference13402]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["create_reference_to_object"]
    ) -> _base.FieldRef[Optional[CreateReferenceToObject13407]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["find_matching_reference_near_alias"]
    ) -> _base.FieldRef[Optional[FindMatchingReferenceNearAlias13416]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["find_matching_reference_from_event"]
    ) -> _base.FieldRef[Optional[FindMatchingReferenceFromEvent13421]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition13427, ...]]:
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
        self, name: Literal["count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["items"]
    ) -> _base.FieldRef[tuple[Item13593, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["spectator_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["observe_dead_body_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["guard_warn_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["combat_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["display_name"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_spells"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_factions"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_package_data"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["voice_types"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_end"]
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


_VARIANT_13378: _base.Variant = _base.Variant(
    path="QUST/13:Aliases/repeat/0:Alias/0:Alias"
)


class Flags13636(enum.IntFlag):
    """Named values from the pinned schema."""

    RESERVES_LOCATION_REFERENCE = 1
    OPTIONAL = 2
    QUEST_OBJECT = 4
    ALLOW_REUSE_IN_QUEST = 8
    ALLOW_DEAD = 16
    MATCHING_REF_IN_LOADED_AREA = 32
    ESSENTIAL = 64
    ALLOW_DISABLED = 128
    STORES_TEXT = 256
    ALLOW_RESERVED = 512
    PROTECTED = 1024
    FORCED_BY_ALIASES = 2048
    ALLOW_DESTROYED = 4096
    MATCHING_REF_CLOSEST = 8192
    USES_STORED_TEXT = 16384
    INITIALLY_DISABLED = 32768


class AdditionalFlags13637(enum.IntFlag):
    """Named values from the pinned schema."""

    ALLOW_CLEARED = 1
    CLEAR_NAMES_WHEN_REMOVED = 2


class Structure13635(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/2:Alias Flags/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/2:Alias Flags/p"
                "ayload/0:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "additional_flags": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/2:Alias Flags/p"
                "ayload/1:Additional Flags"
            ),
            kind="primitive",
            name="Additional Flags",
        ),
    }

    flags: Flags13636
    """Value decoded from this schema node."""

    additional_flags: Optional[AdditionalFlags13637] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags13636]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["additional_flags"]
    ) -> _base.FieldRef[Optional[AdditionalFlags13637]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LocationAliasReference13646(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/7:Location Alias Reference"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/7:Location Alia"
                "s Reference/0:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
        "keyword": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/7:Location Alia"
                "s Reference/1:Keyword"
            ),
            kind="subrecord",
            name="Keyword",
        ),
        "ref_type": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/7:Location Alia"
                "s Reference/2:Ref Type"
            ),
            kind="subrecord",
            name="Ref Type",
        ),
    }

    alias: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    keyword: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    ref_type: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alias"]
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
        self, name: Literal["keyword"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["ref_type"]
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


class ExternalAliasReference13653(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/8:External Alias Reference"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "quest": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/8:External Alia"
                "s Reference/0:Quest"
            ),
            kind="subrecord",
            name="Quest",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/8:External Alia"
                "s Reference/1:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
    }

    quest: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["quest"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
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


class Create13664(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    AT = 0
    IN = 32768


class Structure13662(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Refere"
        "nce to Object/1:Alias/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Refere"
                "nce to Object/1:Alias/payload/0:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "create": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Refere"
                "nce to Object/1:Alias/payload/1:Create"
            ),
            kind="primitive",
            name="Create",
        ),
    }

    alias: Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    """Value decoded from this schema node."""

    create: Create13664
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-32768, le=32767)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["create"]) -> _base.FieldRef[Create13664]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class EasyMediumHardVeryHardNone13666(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EASY = 0
    MEDIUM = 1
    HARD = 2
    VERY_HARD = 3
    NONE = 4


class CreateReferenceToObject13658(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Reference to Object"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "object": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Refere"
                "nce to Object/0:Object"
            ),
            kind="subrecord",
            name="Object",
        ),
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Refere"
                "nce to Object/1:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
        "level": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Refere"
                "nce to Object/2:Level"
            ),
            kind="subrecord",
            name="Level",
        ),
    }

    object: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias: Optional[Structure13662] = None
    """Value decoded from this schema node."""

    level: Optional[EasyMediumHardVeryHardNone13666] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["object"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias"]
    ) -> _base.FieldRef[Optional[Structure13662]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["level"]
    ) -> _base.FieldRef[Optional[EasyMediumHardVeryHardNone13666]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class LinkedRefChild13671(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LINKED_REF_CHILD = 0


class FindMatchingReferenceNearAlias13667(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/10:Find Matchin"
        "g Reference Near Alias"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/10:Find Matchin"
                "g Reference Near Alias/0:Alias"
            ),
            kind="subrecord",
            name="Alias",
        ),
        "type": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/10:Find Matchin"
                "g Reference Near Alias/1:Type"
            ),
            kind="subrecord",
            name="Type",
        ),
    }

    alias: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    type: Optional[LinkedRefChild13671] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["alias"]
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
        self, name: Literal["type"]
    ) -> _base.FieldRef[Optional[LinkedRefChild13671]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class FindMatchingReferenceFromEvent13672(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/11:Find Matchin"
        "g Reference From Event"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "from_event": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/11:Find Matchin"
                "g Reference From Event/0:From Event"
            ),
            kind="subrecord",
            name="From Event",
        ),
        "event_data": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/11:Find Matchin"
                "g Reference From Event/1:Event Data"
            ),
            kind="subrecord",
            name="Event Data",
        ),
    }

    from_event: Optional[str] = None
    """Value decoded from this schema node."""

    event_data: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["from_event"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["event_data"]
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


_VARIANT_13684: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/2:Comparison Value/va"
        "riants/0:Comparison Value - Float"
    )
)


_VARIANT_13685: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/2:Comparison Value/va"
        "riants/1:Comparison Value - Global"
    )
)


_VARIANT_13689: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/0:Unknown"
    )
)


_VARIANT_13690: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/1:None"
    )
)


_VARIANT_13691: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/2:Integer"
    )
)


_VARIANT_13692: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/3:Float"
    )
)


_VARIANT_13693: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/4:Variable Name"
    )
)


class Sex13694(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13694: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/5:Sex"
    )
)


class ActorValue13695(_values.OpenIntEnum):
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


_VARIANT_13695: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/6:Actor Value"
    )
)


class CrimeType13696(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13696: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/7:Crime Type"
    )
)


class Axis13697(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13697: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/8:Axis"
    )
)


_VARIANT_13698: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/9:Quest Stage (unused)"
    )
)


class MiscStat13699(_values.OpenIntEnum):
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


_VARIANT_13699: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/10:Misc Stat"
    )
)


class Alignment13700(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13700: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/11:Alignment"
    )
)


_VARIANT_13701: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/12:Equip Type"
    )
)


class FormType13702(_values.OpenIntEnum):
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


_VARIANT_13702: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/13:Form Type"
    )
)


class CriticalStage13703(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13703: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/14:Critical Stage"
    )
)


_VARIANT_13704: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/15:Object Reference"
    )
)


_VARIANT_13705: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/16:Inventory Object"
    )
)


_VARIANT_13706: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/17:Actor"
    )
)


_VARIANT_13707: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/18:Voice Type"
    )
)


_VARIANT_13708: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/19:Idle"
    )
)


_VARIANT_13709: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/20:Form List"
    )
)


_VARIANT_13710: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/21:Quest"
    )
)


_VARIANT_13711: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/22:Faction"
    )
)


_VARIANT_13712: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/23:Cell"
    )
)


_VARIANT_13713: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/24:Class"
    )
)


_VARIANT_13714: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/25:Race"
    )
)


_VARIANT_13715: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/26:Actor Base"
    )
)


_VARIANT_13716: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/27:Global"
    )
)


_VARIANT_13717: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/28:Weather"
    )
)


_VARIANT_13718: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/29:Package"
    )
)


_VARIANT_13719: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/30:Encounter Zone"
    )
)


_VARIANT_13720: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/31:Perk"
    )
)


_VARIANT_13721: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/32:Owner"
    )
)


_VARIANT_13722: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/33:Furniture"
    )
)


_VARIANT_13723: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/34:Effect Item"
    )
)


_VARIANT_13724: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/35:Base Effect"
    )
)


_VARIANT_13725: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/36:Worldspace"
    )
)


class VatsValueFunction13726(_values.OpenIntEnum):
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


_VARIANT_13726: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/37:VATS Value Function"
    )
)


_VARIANT_13727: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_13728: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/39:Referenceable Object"
    )
)


_VARIANT_13729: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/40:Region"
    )
)


_VARIANT_13730: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/41:Keyword"
    )
)


class PlayerAction13731(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13731: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/42:Player Action"
    )
)


class CastingType13732(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13732: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/43:Casting Type"
    )
)


_VARIANT_13733: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/44:Shout"
    )
)


_VARIANT_13734: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/45:Location"
    )
)


_VARIANT_13735: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/46:Location Ref Type"
    )
)


_VARIANT_13736: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/47:Alias"
    )
)


_VARIANT_13737: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/48:Packdata ID"
    )
)


_VARIANT_13738: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/49:Association Type"
    )
)


class FurnitureAnim13739(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13739: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/50:Furniture Anim"
    )
)


class FurnitureEntry13740(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13740: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/51:Furniture Entry"
    )
)


_VARIANT_13741: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/52:Scene"
    )
)


class WardState13742(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13742: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/53:Ward State"
    )
)


_VARIANT_13743: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/54:Event"
    )
)


_VARIANT_13744: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/55:Event Data"
    )
)


_VARIANT_13745: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/56:Knowable"
    )
)


_VARIANT_13746: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/5:Parameter #1/varian"
        "ts/57:Faction"
    )
)


_VARIANT_13748: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/0:Unknown"
    )
)


_VARIANT_13749: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/1:None"
    )
)


_VARIANT_13750: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/2:Integer"
    )
)


_VARIANT_13751: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/3:Float"
    )
)


_VARIANT_13752: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/4:Variable Name"
    )
)


class Sex13753(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13753: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/5:Sex"
    )
)


class ActorValue13754(_values.OpenIntEnum):
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


_VARIANT_13754: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/6:Actor Value"
    )
)


class CrimeType13755(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13755: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/7:Crime Type"
    )
)


class Axis13756(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13756: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/8:Axis"
    )
)


_VARIANT_13757: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/9:Quest Stage"
    )
)


class MiscStat13758(_values.OpenIntEnum):
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


_VARIANT_13758: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/10:Misc Stat"
    )
)


class Alignment13759(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13759: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/11:Alignment"
    )
)


_VARIANT_13760: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/12:Equip Type"
    )
)


class FormType13761(_values.OpenIntEnum):
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


_VARIANT_13761: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/13:Form Type"
    )
)


class CriticalStage13762(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13762: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/14:Critical Stage"
    )
)


_VARIANT_13763: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/15:Object Reference"
    )
)


_VARIANT_13764: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/16:Inventory Object"
    )
)


_VARIANT_13765: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/17:Actor"
    )
)


_VARIANT_13766: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/18:Voice Type"
    )
)


_VARIANT_13767: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/19:Idle"
    )
)


_VARIANT_13768: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/20:Form List"
    )
)


_VARIANT_13769: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/21:Quest"
    )
)


_VARIANT_13770: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/22:Faction"
    )
)


_VARIANT_13771: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/23:Cell"
    )
)


_VARIANT_13772: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/24:Class"
    )
)


_VARIANT_13773: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/25:Race"
    )
)


_VARIANT_13774: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/26:Actor Base"
    )
)


_VARIANT_13775: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/27:Global"
    )
)


_VARIANT_13776: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/28:Weather"
    )
)


_VARIANT_13777: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/29:Package"
    )
)


_VARIANT_13778: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/30:Encounter Zone"
    )
)


_VARIANT_13779: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/31:Perk"
    )
)


_VARIANT_13780: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/32:Owner"
    )
)


_VARIANT_13781: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/33:Furniture"
    )
)


_VARIANT_13782: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/34:Effect Item"
    )
)


_VARIANT_13783: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/35:Base Effect"
    )
)


_VARIANT_13784: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/36:Worldspace"
    )
)


class VatsValueFunction13785(_values.OpenIntEnum):
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


_VARIANT_13785: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/37:VATS Value Function"
    )
)


_VARIANT_13787: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/0:Weapon"
    )
)


_VARIANT_13788: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/1:Weapon List"
    )
)


_VARIANT_13789: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/2:Target"
    )
)


_VARIANT_13790: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/3:Target List"
    )
)


_VARIANT_13791: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/4:Unknown"
    )
)


class TargetPart13792(_values.OpenIntEnum):
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


_VARIANT_13792: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/5:Target Part"
    )
)


class VatsAction13793(_values.OpenIntEnum):
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


_VARIANT_13793: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/6:VATS Action"
    )
)


_VARIANT_13794: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/7:Unknown"
    )
)


_VARIANT_13795: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/8:Unknown"
    )
)


_VARIANT_13796: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/9:Critical Effect"
    )
)


_VARIANT_13797: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/10:Critical Effect Lis"
        "t"
    )
)


_VARIANT_13798: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/11:Unknown"
    )
)


_VARIANT_13799: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/12:Unknown"
    )
)


_VARIANT_13800: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/13:Unknown"
    )
)


_VARIANT_13801: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/14:Unknown"
    )
)


class WeaponType13802(_values.OpenIntEnum):
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


_VARIANT_13802: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_13803: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/16:Unknown"
    )
)


_VARIANT_13804: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/17:Unknown"
    )
)


class ProjectileType13805(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_13805: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/18:Projectile Type"
    )
)


class DeliveryType13806(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_13806: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/19:Delivery Type"
    )
)


class CastingType13807(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_13807: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param/variants/20:Casting Type"
    )
)


_VARIANT_13786: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/38:VATS Value Param"
    )
)


_VARIANT_13808: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/39:Referenceable Object"
    )
)


_VARIANT_13809: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/40:Region"
    )
)


_VARIANT_13810: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/41:Keyword"
    )
)


class PlayerAction13811(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13811: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/42:Player Action"
    )
)


class CastingType13812(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13812: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/43:Casting Type"
    )
)


_VARIANT_13813: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/44:Shout"
    )
)


_VARIANT_13814: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/45:Location"
    )
)


_VARIANT_13815: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/46:Location Ref Type"
    )
)


_VARIANT_13816: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/47:Alias"
    )
)


_VARIANT_13817: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/48:Packdata ID"
    )
)


_VARIANT_13818: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/49:Association Type"
    )
)


class FurnitureAnim13819(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13819: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/50:Furniture Anim"
    )
)


class FurnitureEntry13820(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13820: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/51:Furniture Entry"
    )
)


_VARIANT_13821: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/52:Scene"
    )
)


class WardState13822(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13822: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/53:Ward State"
    )
)


_VARIANT_13823: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/54:Event"
    )
)


_VARIANT_13824: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/55:Event Data"
    )
)


_VARIANT_13825: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/56:Knowable"
    )
)


_VARIANT_13826: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/6:Parameter #2/varian"
        "ts/57:Faction"
    )
)


class RunOn13827(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_13829: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/8:Reference/variants/"
        "0:Unused"
    )
)


_VARIANT_13830: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload/8:Reference/variants/"
        "1:Reference"
    )
)


class Structure13680(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_13687": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA/payload/9:Parameter #3"
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
        Annotated[float, _VARIANT_13684]
        | Annotated[_values.FormId, _VARIANT_13685]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_13687: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_13689]
        | Annotated[bytes, _VARIANT_13690]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13691,
        ]
        | Annotated[float, _VARIANT_13692]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13693,
        ]
        | Annotated[Sex13694, _VARIANT_13694]
        | Annotated[ActorValue13695, _VARIANT_13695]
        | Annotated[CrimeType13696, _VARIANT_13696]
        | Annotated[Axis13697, _VARIANT_13697]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13698,
        ]
        | Annotated[MiscStat13699, _VARIANT_13699]
        | Annotated[Alignment13700, _VARIANT_13700]
        | Annotated[_values.FormId, _VARIANT_13701]
        | Annotated[FormType13702, _VARIANT_13702]
        | Annotated[CriticalStage13703, _VARIANT_13703]
        | Annotated[_values.FormId, _VARIANT_13704]
        | Annotated[_values.FormId, _VARIANT_13705]
        | Annotated[_values.FormId, _VARIANT_13706]
        | Annotated[_values.FormId, _VARIANT_13707]
        | Annotated[_values.FormId, _VARIANT_13708]
        | Annotated[_values.FormId, _VARIANT_13709]
        | Annotated[_values.FormId, _VARIANT_13710]
        | Annotated[_values.FormId, _VARIANT_13711]
        | Annotated[_values.FormId, _VARIANT_13712]
        | Annotated[_values.FormId, _VARIANT_13713]
        | Annotated[_values.FormId, _VARIANT_13714]
        | Annotated[_values.FormId, _VARIANT_13715]
        | Annotated[_values.FormId, _VARIANT_13716]
        | Annotated[_values.FormId, _VARIANT_13717]
        | Annotated[_values.FormId, _VARIANT_13718]
        | Annotated[_values.FormId, _VARIANT_13719]
        | Annotated[_values.FormId, _VARIANT_13720]
        | Annotated[_values.FormId, _VARIANT_13721]
        | Annotated[_values.FormId, _VARIANT_13722]
        | Annotated[_values.FormId, _VARIANT_13723]
        | Annotated[_values.FormId, _VARIANT_13724]
        | Annotated[_values.FormId, _VARIANT_13725]
        | Annotated[VatsValueFunction13726, _VARIANT_13726]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13727,
        ]
        | Annotated[_values.FormId, _VARIANT_13728]
        | Annotated[_values.FormId, _VARIANT_13729]
        | Annotated[_values.FormId, _VARIANT_13730]
        | Annotated[PlayerAction13731, _VARIANT_13731]
        | Annotated[CastingType13732, _VARIANT_13732]
        | Annotated[_values.FormId, _VARIANT_13733]
        | Annotated[_values.FormId, _VARIANT_13734]
        | Annotated[_values.FormId, _VARIANT_13735]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13736,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13737,
        ]
        | Annotated[_values.FormId, _VARIANT_13738]
        | Annotated[FurnitureAnim13739, _VARIANT_13739]
        | Annotated[FurnitureEntry13740, _VARIANT_13740]
        | Annotated[_values.FormId, _VARIANT_13741]
        | Annotated[WardState13742, _VARIANT_13742]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13743,
        ]
        | Annotated[_values.FormId, _VARIANT_13744]
        | Annotated[_values.FormId, _VARIANT_13745]
        | Annotated[_values.FormId, _VARIANT_13746]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_13748]
        | Annotated[bytes, _VARIANT_13749]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13750,
        ]
        | Annotated[float, _VARIANT_13751]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13752,
        ]
        | Annotated[Sex13753, _VARIANT_13753]
        | Annotated[ActorValue13754, _VARIANT_13754]
        | Annotated[CrimeType13755, _VARIANT_13755]
        | Annotated[Axis13756, _VARIANT_13756]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13757,
        ]
        | Annotated[MiscStat13758, _VARIANT_13758]
        | Annotated[Alignment13759, _VARIANT_13759]
        | Annotated[_values.FormId, _VARIANT_13760]
        | Annotated[FormType13761, _VARIANT_13761]
        | Annotated[CriticalStage13762, _VARIANT_13762]
        | Annotated[_values.FormId, _VARIANT_13763]
        | Annotated[_values.FormId, _VARIANT_13764]
        | Annotated[_values.FormId, _VARIANT_13765]
        | Annotated[_values.FormId, _VARIANT_13766]
        | Annotated[_values.FormId, _VARIANT_13767]
        | Annotated[_values.FormId, _VARIANT_13768]
        | Annotated[_values.FormId, _VARIANT_13769]
        | Annotated[_values.FormId, _VARIANT_13770]
        | Annotated[_values.FormId, _VARIANT_13771]
        | Annotated[_values.FormId, _VARIANT_13772]
        | Annotated[_values.FormId, _VARIANT_13773]
        | Annotated[_values.FormId, _VARIANT_13774]
        | Annotated[_values.FormId, _VARIANT_13775]
        | Annotated[_values.FormId, _VARIANT_13776]
        | Annotated[_values.FormId, _VARIANT_13777]
        | Annotated[_values.FormId, _VARIANT_13778]
        | Annotated[_values.FormId, _VARIANT_13779]
        | Annotated[_values.FormId, _VARIANT_13780]
        | Annotated[_values.FormId, _VARIANT_13781]
        | Annotated[_values.FormId, _VARIANT_13782]
        | Annotated[_values.FormId, _VARIANT_13783]
        | Annotated[_values.FormId, _VARIANT_13784]
        | Annotated[VatsValueFunction13785, _VARIANT_13785]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13787]
            | Annotated[_values.FormId, _VARIANT_13788]
            | Annotated[_values.FormId, _VARIANT_13789]
            | Annotated[_values.FormId, _VARIANT_13790]
            | Annotated[bytes, _VARIANT_13791]
            | Annotated[TargetPart13792, _VARIANT_13792]
            | Annotated[VatsAction13793, _VARIANT_13793]
            | Annotated[bytes, _VARIANT_13794]
            | Annotated[bytes, _VARIANT_13795]
            | Annotated[_values.FormId, _VARIANT_13796]
            | Annotated[_values.FormId, _VARIANT_13797]
            | Annotated[bytes, _VARIANT_13798]
            | Annotated[bytes, _VARIANT_13799]
            | Annotated[bytes, _VARIANT_13800]
            | Annotated[bytes, _VARIANT_13801]
            | Annotated[WeaponType13802, _VARIANT_13802]
            | Annotated[bytes, _VARIANT_13803]
            | Annotated[bytes, _VARIANT_13804]
            | Annotated[ProjectileType13805, _VARIANT_13805]
            | Annotated[DeliveryType13806, _VARIANT_13806]
            | Annotated[CastingType13807, _VARIANT_13807],
            _VARIANT_13786,
        ]
        | Annotated[_values.FormId, _VARIANT_13808]
        | Annotated[_values.FormId, _VARIANT_13809]
        | Annotated[_values.FormId, _VARIANT_13810]
        | Annotated[PlayerAction13811, _VARIANT_13811]
        | Annotated[CastingType13812, _VARIANT_13812]
        | Annotated[_values.FormId, _VARIANT_13813]
        | Annotated[_values.FormId, _VARIANT_13814]
        | Annotated[_values.FormId, _VARIANT_13815]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13816,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13817,
        ]
        | Annotated[_values.FormId, _VARIANT_13818]
        | Annotated[FurnitureAnim13819, _VARIANT_13819]
        | Annotated[FurnitureEntry13820, _VARIANT_13820]
        | Annotated[_values.FormId, _VARIANT_13821]
        | Annotated[WardState13822, _VARIANT_13822]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13823,
        ]
        | Annotated[_values.FormId, _VARIANT_13824]
        | Annotated[_values.FormId, _VARIANT_13825]
        | Annotated[_values.FormId, _VARIANT_13826]
    )
    """Value decoded from this schema node."""

    run_on: RunOn13827
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13829,
        ]
        | Annotated[_values.FormId, _VARIANT_13830]
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
        Annotated[float, _VARIANT_13684]
        | Annotated[_values.FormId, _VARIANT_13685]
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
    def field(self, name: Literal["unused_13687"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13689]
        | Annotated[bytes, _VARIANT_13690]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13691,
        ]
        | Annotated[float, _VARIANT_13692]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13693,
        ]
        | Annotated[Sex13694, _VARIANT_13694]
        | Annotated[ActorValue13695, _VARIANT_13695]
        | Annotated[CrimeType13696, _VARIANT_13696]
        | Annotated[Axis13697, _VARIANT_13697]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13698,
        ]
        | Annotated[MiscStat13699, _VARIANT_13699]
        | Annotated[Alignment13700, _VARIANT_13700]
        | Annotated[_values.FormId, _VARIANT_13701]
        | Annotated[FormType13702, _VARIANT_13702]
        | Annotated[CriticalStage13703, _VARIANT_13703]
        | Annotated[_values.FormId, _VARIANT_13704]
        | Annotated[_values.FormId, _VARIANT_13705]
        | Annotated[_values.FormId, _VARIANT_13706]
        | Annotated[_values.FormId, _VARIANT_13707]
        | Annotated[_values.FormId, _VARIANT_13708]
        | Annotated[_values.FormId, _VARIANT_13709]
        | Annotated[_values.FormId, _VARIANT_13710]
        | Annotated[_values.FormId, _VARIANT_13711]
        | Annotated[_values.FormId, _VARIANT_13712]
        | Annotated[_values.FormId, _VARIANT_13713]
        | Annotated[_values.FormId, _VARIANT_13714]
        | Annotated[_values.FormId, _VARIANT_13715]
        | Annotated[_values.FormId, _VARIANT_13716]
        | Annotated[_values.FormId, _VARIANT_13717]
        | Annotated[_values.FormId, _VARIANT_13718]
        | Annotated[_values.FormId, _VARIANT_13719]
        | Annotated[_values.FormId, _VARIANT_13720]
        | Annotated[_values.FormId, _VARIANT_13721]
        | Annotated[_values.FormId, _VARIANT_13722]
        | Annotated[_values.FormId, _VARIANT_13723]
        | Annotated[_values.FormId, _VARIANT_13724]
        | Annotated[_values.FormId, _VARIANT_13725]
        | Annotated[VatsValueFunction13726, _VARIANT_13726]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13727,
        ]
        | Annotated[_values.FormId, _VARIANT_13728]
        | Annotated[_values.FormId, _VARIANT_13729]
        | Annotated[_values.FormId, _VARIANT_13730]
        | Annotated[PlayerAction13731, _VARIANT_13731]
        | Annotated[CastingType13732, _VARIANT_13732]
        | Annotated[_values.FormId, _VARIANT_13733]
        | Annotated[_values.FormId, _VARIANT_13734]
        | Annotated[_values.FormId, _VARIANT_13735]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13736,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13737,
        ]
        | Annotated[_values.FormId, _VARIANT_13738]
        | Annotated[FurnitureAnim13739, _VARIANT_13739]
        | Annotated[FurnitureEntry13740, _VARIANT_13740]
        | Annotated[_values.FormId, _VARIANT_13741]
        | Annotated[WardState13742, _VARIANT_13742]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13743,
        ]
        | Annotated[_values.FormId, _VARIANT_13744]
        | Annotated[_values.FormId, _VARIANT_13745]
        | Annotated[_values.FormId, _VARIANT_13746]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13748]
        | Annotated[bytes, _VARIANT_13749]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13750,
        ]
        | Annotated[float, _VARIANT_13751]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13752,
        ]
        | Annotated[Sex13753, _VARIANT_13753]
        | Annotated[ActorValue13754, _VARIANT_13754]
        | Annotated[CrimeType13755, _VARIANT_13755]
        | Annotated[Axis13756, _VARIANT_13756]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13757,
        ]
        | Annotated[MiscStat13758, _VARIANT_13758]
        | Annotated[Alignment13759, _VARIANT_13759]
        | Annotated[_values.FormId, _VARIANT_13760]
        | Annotated[FormType13761, _VARIANT_13761]
        | Annotated[CriticalStage13762, _VARIANT_13762]
        | Annotated[_values.FormId, _VARIANT_13763]
        | Annotated[_values.FormId, _VARIANT_13764]
        | Annotated[_values.FormId, _VARIANT_13765]
        | Annotated[_values.FormId, _VARIANT_13766]
        | Annotated[_values.FormId, _VARIANT_13767]
        | Annotated[_values.FormId, _VARIANT_13768]
        | Annotated[_values.FormId, _VARIANT_13769]
        | Annotated[_values.FormId, _VARIANT_13770]
        | Annotated[_values.FormId, _VARIANT_13771]
        | Annotated[_values.FormId, _VARIANT_13772]
        | Annotated[_values.FormId, _VARIANT_13773]
        | Annotated[_values.FormId, _VARIANT_13774]
        | Annotated[_values.FormId, _VARIANT_13775]
        | Annotated[_values.FormId, _VARIANT_13776]
        | Annotated[_values.FormId, _VARIANT_13777]
        | Annotated[_values.FormId, _VARIANT_13778]
        | Annotated[_values.FormId, _VARIANT_13779]
        | Annotated[_values.FormId, _VARIANT_13780]
        | Annotated[_values.FormId, _VARIANT_13781]
        | Annotated[_values.FormId, _VARIANT_13782]
        | Annotated[_values.FormId, _VARIANT_13783]
        | Annotated[_values.FormId, _VARIANT_13784]
        | Annotated[VatsValueFunction13785, _VARIANT_13785]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13787]
            | Annotated[_values.FormId, _VARIANT_13788]
            | Annotated[_values.FormId, _VARIANT_13789]
            | Annotated[_values.FormId, _VARIANT_13790]
            | Annotated[bytes, _VARIANT_13791]
            | Annotated[TargetPart13792, _VARIANT_13792]
            | Annotated[VatsAction13793, _VARIANT_13793]
            | Annotated[bytes, _VARIANT_13794]
            | Annotated[bytes, _VARIANT_13795]
            | Annotated[_values.FormId, _VARIANT_13796]
            | Annotated[_values.FormId, _VARIANT_13797]
            | Annotated[bytes, _VARIANT_13798]
            | Annotated[bytes, _VARIANT_13799]
            | Annotated[bytes, _VARIANT_13800]
            | Annotated[bytes, _VARIANT_13801]
            | Annotated[WeaponType13802, _VARIANT_13802]
            | Annotated[bytes, _VARIANT_13803]
            | Annotated[bytes, _VARIANT_13804]
            | Annotated[ProjectileType13805, _VARIANT_13805]
            | Annotated[DeliveryType13806, _VARIANT_13806]
            | Annotated[CastingType13807, _VARIANT_13807],
            _VARIANT_13786,
        ]
        | Annotated[_values.FormId, _VARIANT_13808]
        | Annotated[_values.FormId, _VARIANT_13809]
        | Annotated[_values.FormId, _VARIANT_13810]
        | Annotated[PlayerAction13811, _VARIANT_13811]
        | Annotated[CastingType13812, _VARIANT_13812]
        | Annotated[_values.FormId, _VARIANT_13813]
        | Annotated[_values.FormId, _VARIANT_13814]
        | Annotated[_values.FormId, _VARIANT_13815]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13816,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13817,
        ]
        | Annotated[_values.FormId, _VARIANT_13818]
        | Annotated[FurnitureAnim13819, _VARIANT_13819]
        | Annotated[FurnitureEntry13820, _VARIANT_13820]
        | Annotated[_values.FormId, _VARIANT_13821]
        | Annotated[WardState13822, _VARIANT_13822]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13823,
        ]
        | Annotated[_values.FormId, _VARIANT_13824]
        | Annotated[_values.FormId, _VARIANT_13825]
        | Annotated[_values.FormId, _VARIANT_13826]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn13827]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13829,
        ]
        | Annotated[_values.FormId, _VARIANT_13830]
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


class Condition13678(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
        "epeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure13680] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure13680]]:
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


class Structure13846(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
        "/0:Item/0:Item/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
                "/0:Item/0:Item/payload/0:Item"
            ),
            kind="primitive",
            name="Item",
        ),
        "count": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
                "/0:Item/0:Item/payload/1:Count"
            ),
            kind="primitive",
            name="Count",
        ),
    }

    item: _values.FormId
    """Value decoded from this schema node."""

    count: Annotated[
        int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["item"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
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


_VARIANT_13853: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
        "red Rank/variants/0:Unused"
    )
)


_VARIANT_13854: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
        "red Rank/variants/1:Global Variable"
    )
)


_VARIANT_13855: _base.Variant = _base.Variant(
    path=(
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
        "red Rank/variants/2:Required Rank"
    )
)


class Structure13850(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
        "/0:Item/1:Extra Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "owner": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data/payload/0:Owner"
            ),
            kind="primitive",
            name="Owner",
        ),
        "global_variable_required_rank": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data/payload/1:Global Variable / Requi"
                "red Rank"
            ),
            kind="union",
            name="Global Variable / Required Rank",
        ),
        "item_condition": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data/payload/2:Item Condition"
            ),
            kind="primitive",
            name="Item Condition",
        ),
    }

    owner: _values.FormId
    """Value decoded from this schema node."""

    global_variable_required_rank: (
        Annotated[bytes, _VARIANT_13853]
        | Annotated[_values.FormId, _VARIANT_13854]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13855,
        ]
    )
    """Value decoded from this schema node."""

    item_condition: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["owner"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["global_variable_required_rank"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13853]
        | Annotated[_values.FormId, _VARIANT_13854]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13855,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["item_condition"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Item13844(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat/0:Item"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "item": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
                "/0:Item/0:Item"
            ),
            kind="subrecord",
            name="Item",
        ),
        "extra_data": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat"
                "/0:Item/1:Extra Data"
            ),
            kind="subrecord",
            name="Extra Data",
        ),
    }

    item: Optional[Structure13846] = None
    """Value decoded from this schema node."""

    extra_data: Optional[Structure13850] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["item"]
    ) -> _base.FieldRef[Optional[Structure13846]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["extra_data"]
    ) -> _base.FieldRef[Optional[Structure13850]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Alias13629(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/13:Aliases/repeat/0:Alias/1:Alias"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "location_alias_id": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/0:Location Alias ID"),
            kind="subrecord",
            name="Location Alias ID",
        ),
        "alias_name": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/1:Alias Name"),
            kind="subrecord",
            name="Alias Name",
        ),
        "alias_flags": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/2:Alias Flags"),
            kind="subrecord",
            name="Alias Flags",
        ),
        "force_into_alias_when_filled": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/3:Force Into Al"
                "ias When Filled"
            ),
            kind="subrecord",
            name="Force Into Alias When Filled",
        ),
        "specific_location": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/4:Specific Location"),
            kind="subrecord",
            name="Specific Location",
        ),
        "forced_reference": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/5:Forced Reference"),
            kind="subrecord",
            name="Forced Reference",
        ),
        "unique_actor": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/6:Unique Actor"),
            kind="subrecord",
            name="Unique Actor",
        ),
        "location_alias_reference": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/7:Location Alia"
                "s Reference"
            ),
            kind="sequence",
            name="Location Alias Reference",
        ),
        "external_alias_reference": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/8:External Alia"
                "s Reference"
            ),
            kind="sequence",
            name="External Alias Reference",
        ),
        "create_reference_to_object": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/9:Create Refere"
                "nce to Object"
            ),
            kind="sequence",
            name="Create Reference to Object",
        ),
        "find_matching_reference_near_alias": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/10:Find Matchin"
                "g Reference Near Alias"
            ),
            kind="sequence",
            name="Find Matching Reference Near Alias",
        ),
        "find_matching_reference_from_event": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/11:Find Matchin"
                "g Reference From Event"
            ),
            kind="sequence",
            name="Find Matching Reference From Event",
        ),
        "conditions": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions"),
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/12:Conditions/r"
                "epeat/0:Condition"
            ),
            child_kind="sequence",
        ),
        "keyword_count": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/13:Keyword Count"),
            kind="subrecord",
            name="Keyword Count",
        ),
        "keywords": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/14:Keywords"),
            kind="subrecord",
            name="Keywords",
        ),
        "count": _base.Binding(
            path="QUST/13:Aliases/repeat/0:Alias/1:Alias/15:Count",
            kind="subrecord",
            name="Count",
        ),
        "items": _base.Binding(
            path="QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items",
            kind="repeat",
            name="Items",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/16:Items/repeat/0:Item"
            ),
            child_kind="sequence",
        ),
        "spectator_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/17:Spectator ov"
                "erride package list"
            ),
            kind="subrecord",
            name="Spectator override package list",
        ),
        "observe_dead_body_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/18:Observe dead"
                " body override package list"
            ),
            kind="subrecord",
            name="Observe dead body override package list",
        ),
        "guard_warn_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/19:Guard warn o"
                "verride package list"
            ),
            kind="subrecord",
            name="Guard warn override package list",
        ),
        "combat_override_package_list": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/20:Combat overr"
                "ide package list"
            ),
            kind="subrecord",
            name="Combat override package list",
        ),
        "display_name": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/21:Display Name"),
            kind="subrecord",
            name="Display Name",
        ),
        "alias_spells": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/22:Alias Spells"),
            kind="repeat",
            name="Alias Spells",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/22:Alias Spells"
                "/repeat/0:Spell"
            ),
            child_kind="subrecord",
        ),
        "alias_factions": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/23:Alias Factions"),
            kind="repeat",
            name="Alias Factions",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/23:Alias Factio"
                "ns/repeat/0:Faction"
            ),
            child_kind="subrecord",
        ),
        "alias_package_data": _base.Binding(
            path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/24:Alias Package Data"
            ),
            kind="repeat",
            name="Alias Package Data",
            repeated_path=(
                "QUST/13:Aliases/repeat/0:Alias/1:Alias/24:Alias Packag"
                "e Data/repeat/0:Package"
            ),
            child_kind="subrecord",
        ),
        "voice_types": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/25:Voice Types"),
            kind="subrecord",
            name="Voice Types",
        ),
        "alias_end": _base.Binding(
            path=("QUST/13:Aliases/repeat/0:Alias/1:Alias/26:Alias End"),
            kind="subrecord",
            name="Alias End",
        ),
    }

    location_alias_id: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    alias_name: Optional[str] = None
    """Value decoded from this schema node."""

    alias_flags: Optional[Structure13635] = None
    """Value decoded from this schema node."""

    force_into_alias_when_filled: Optional[
        Annotated[
            int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
        ]
    ] = None
    """Value decoded from this schema node."""

    specific_location: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    forced_reference: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    unique_actor: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    location_alias_reference: Optional[LocationAliasReference13646] = None
    """Value decoded from this schema node."""

    external_alias_reference: Optional[ExternalAliasReference13653] = None
    """Value decoded from this schema node."""

    create_reference_to_object: Optional[CreateReferenceToObject13658] = None
    """Value decoded from this schema node."""

    find_matching_reference_near_alias: Optional[
        FindMatchingReferenceNearAlias13667
    ] = None
    """Value decoded from this schema node."""

    find_matching_reference_from_event: Optional[
        FindMatchingReferenceFromEvent13672
    ] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition13678, ...] = ()
    """Value decoded from this schema node."""

    keyword_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    keywords: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    items: tuple[Item13844, ...] = ()
    """Value decoded from this schema node."""

    spectator_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    observe_dead_body_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    guard_warn_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    combat_override_package_list: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    display_name: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias_spells: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    alias_factions: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    alias_package_data: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    voice_types: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    alias_end: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["location_alias_id"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_flags"]
    ) -> _base.FieldRef[Optional[Structure13635]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["force_into_alias_when_filled"]
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
        self, name: Literal["specific_location"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["forced_reference"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unique_actor"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["location_alias_reference"]
    ) -> _base.FieldRef[Optional[LocationAliasReference13646]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["external_alias_reference"]
    ) -> _base.FieldRef[Optional[ExternalAliasReference13653]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["create_reference_to_object"]
    ) -> _base.FieldRef[Optional[CreateReferenceToObject13658]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["find_matching_reference_near_alias"]
    ) -> _base.FieldRef[Optional[FindMatchingReferenceNearAlias13667]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["find_matching_reference_from_event"]
    ) -> _base.FieldRef[Optional[FindMatchingReferenceFromEvent13672]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition13678, ...]]:
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
        self, name: Literal["count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["items"]
    ) -> _base.FieldRef[tuple[Item13844, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["spectator_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["observe_dead_body_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["guard_warn_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["combat_override_package_list"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["display_name"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_spells"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_factions"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_package_data"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["voice_types"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["alias_end"]
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


_VARIANT_13629: _base.Variant = _base.Variant(
    path="QUST/13:Aliases/repeat/0:Alias/1:Alias"
)


class Flags13887(enum.IntFlag):
    """Named values from the pinned schema."""

    COMPASS_MARKER_IGNORES_LOCKS = 1


class Structure13885(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/15:Targets/repeat/0:Target/0:Target/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "target": _base.Binding(
            path=("QUST/15:Targets/repeat/0:Target/0:Target/payload/0:Target"),
            kind="primitive",
            name="Target",
        ),
        "flags": _base.Binding(
            path=("QUST/15:Targets/repeat/0:Target/0:Target/payload/1:Flags"),
            kind="primitive",
            name="Flags",
        ),
        "unknown": _base.Binding(
            path=("QUST/15:Targets/repeat/0:Target/0:Target/payload/2:Unknown"),
            kind="primitive",
            name="Unknown",
        ),
    }

    target: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags13887
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["target"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags13887]:
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


_VARIANT_13896: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/2:Comparison Value/variants/0"
        ":Comparison Value - Float"
    )
)


_VARIANT_13897: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/2:Comparison Value/variants/1"
        ":Comparison Value - Global"
    )
)


_VARIANT_13901: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/0:Unk"
        "nown"
    )
)


_VARIANT_13902: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/1:Non"
        "e"
    )
)


_VARIANT_13903: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/2:Int"
        "eger"
    )
)


_VARIANT_13904: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/3:Flo"
        "at"
    )
)


_VARIANT_13905: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/4:Var"
        "iable Name"
    )
)


class Sex13906(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13906: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/5:Sex"
    )
)


class ActorValue13907(_values.OpenIntEnum):
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


_VARIANT_13907: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/6:Act"
        "or Value"
    )
)


class CrimeType13908(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13908: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/7:Cri"
        "me Type"
    )
)


class Axis13909(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13909: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/8:Axi"
        "s"
    )
)


_VARIANT_13910: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/9:Que"
        "st Stage (unused)"
    )
)


class MiscStat13911(_values.OpenIntEnum):
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


_VARIANT_13911: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/10:Mi"
        "sc Stat"
    )
)


class Alignment13912(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13912: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/11:Al"
        "ignment"
    )
)


_VARIANT_13913: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/12:Eq"
        "uip Type"
    )
)


class FormType13914(_values.OpenIntEnum):
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


_VARIANT_13914: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/13:Fo"
        "rm Type"
    )
)


class CriticalStage13915(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13915: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/14:Cr"
        "itical Stage"
    )
)


_VARIANT_13916: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/15:Ob"
        "ject Reference"
    )
)


_VARIANT_13917: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/16:In"
        "ventory Object"
    )
)


_VARIANT_13918: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/17:Ac"
        "tor"
    )
)


_VARIANT_13919: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/18:Vo"
        "ice Type"
    )
)


_VARIANT_13920: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/19:Id"
        "le"
    )
)


_VARIANT_13921: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/20:Fo"
        "rm List"
    )
)


_VARIANT_13922: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/21:Qu"
        "est"
    )
)


_VARIANT_13923: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/22:Fa"
        "ction"
    )
)


_VARIANT_13924: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/23:Ce"
        "ll"
    )
)


_VARIANT_13925: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/24:Cl"
        "ass"
    )
)


_VARIANT_13926: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/25:Ra"
        "ce"
    )
)


_VARIANT_13927: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/26:Ac"
        "tor Base"
    )
)


_VARIANT_13928: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/27:Gl"
        "obal"
    )
)


_VARIANT_13929: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/28:We"
        "ather"
    )
)


_VARIANT_13930: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/29:Pa"
        "ckage"
    )
)


_VARIANT_13931: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/30:En"
        "counter Zone"
    )
)


_VARIANT_13932: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/31:Pe"
        "rk"
    )
)


_VARIANT_13933: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/32:Ow"
        "ner"
    )
)


_VARIANT_13934: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/33:Fu"
        "rniture"
    )
)


_VARIANT_13935: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/34:Ef"
        "fect Item"
    )
)


_VARIANT_13936: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/35:Ba"
        "se Effect"
    )
)


_VARIANT_13937: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/36:Wo"
        "rldspace"
    )
)


class VatsValueFunction13938(_values.OpenIntEnum):
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


_VARIANT_13938: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/37:VA"
        "TS Value Function"
    )
)


_VARIANT_13939: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/38:VA"
        "TS Value Param (INVALID)"
    )
)


_VARIANT_13940: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/39:Re"
        "ferenceable Object"
    )
)


_VARIANT_13941: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/40:Re"
        "gion"
    )
)


_VARIANT_13942: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/41:Ke"
        "yword"
    )
)


class PlayerAction13943(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_13943: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/42:Pl"
        "ayer Action"
    )
)


class CastingType13944(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_13944: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/43:Ca"
        "sting Type"
    )
)


_VARIANT_13945: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/44:Sh"
        "out"
    )
)


_VARIANT_13946: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/45:Lo"
        "cation"
    )
)


_VARIANT_13947: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/46:Lo"
        "cation Ref Type"
    )
)


_VARIANT_13948: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/47:Al"
        "ias"
    )
)


_VARIANT_13949: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/48:Pa"
        "ckdata ID"
    )
)


_VARIANT_13950: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/49:As"
        "sociation Type"
    )
)


class FurnitureAnim13951(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_13951: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/50:Fu"
        "rniture Anim"
    )
)


class FurnitureEntry13952(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_13952: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/51:Fu"
        "rniture Entry"
    )
)


_VARIANT_13953: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/52:Sc"
        "ene"
    )
)


class WardState13954(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_13954: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/53:Wa"
        "rd State"
    )
)


_VARIANT_13955: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/54:Ev"
        "ent"
    )
)


_VARIANT_13956: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/55:Ev"
        "ent Data"
    )
)


_VARIANT_13957: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/56:Kn"
        "owable"
    )
)


_VARIANT_13958: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/5:Parameter #1/variants/57:Fa"
        "ction"
    )
)


_VARIANT_13960: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/0:Unk"
        "nown"
    )
)


_VARIANT_13961: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/1:Non"
        "e"
    )
)


_VARIANT_13962: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/2:Int"
        "eger"
    )
)


_VARIANT_13963: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/3:Flo"
        "at"
    )
)


_VARIANT_13964: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/4:Var"
        "iable Name"
    )
)


class Sex13965(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_13965: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/5:Sex"
    )
)


class ActorValue13966(_values.OpenIntEnum):
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


_VARIANT_13966: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/6:Act"
        "or Value"
    )
)


class CrimeType13967(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_13967: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/7:Cri"
        "me Type"
    )
)


class Axis13968(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_13968: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/8:Axi"
        "s"
    )
)


_VARIANT_13969: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/9:Que"
        "st Stage"
    )
)


class MiscStat13970(_values.OpenIntEnum):
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


_VARIANT_13970: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/10:Mi"
        "sc Stat"
    )
)


class Alignment13971(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_13971: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/11:Al"
        "ignment"
    )
)


_VARIANT_13972: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/12:Eq"
        "uip Type"
    )
)


class FormType13973(_values.OpenIntEnum):
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


_VARIANT_13973: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/13:Fo"
        "rm Type"
    )
)


class CriticalStage13974(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_13974: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/14:Cr"
        "itical Stage"
    )
)


_VARIANT_13975: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/15:Ob"
        "ject Reference"
    )
)


_VARIANT_13976: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/16:In"
        "ventory Object"
    )
)


_VARIANT_13977: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/17:Ac"
        "tor"
    )
)


_VARIANT_13978: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/18:Vo"
        "ice Type"
    )
)


_VARIANT_13979: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/19:Id"
        "le"
    )
)


_VARIANT_13980: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/20:Fo"
        "rm List"
    )
)


_VARIANT_13981: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/21:Qu"
        "est"
    )
)


_VARIANT_13982: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/22:Fa"
        "ction"
    )
)


_VARIANT_13983: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/23:Ce"
        "ll"
    )
)


_VARIANT_13984: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/24:Cl"
        "ass"
    )
)


_VARIANT_13985: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/25:Ra"
        "ce"
    )
)


_VARIANT_13986: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/26:Ac"
        "tor Base"
    )
)


_VARIANT_13987: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/27:Gl"
        "obal"
    )
)


_VARIANT_13988: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/28:We"
        "ather"
    )
)


_VARIANT_13989: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/29:Pa"
        "ckage"
    )
)


_VARIANT_13990: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/30:En"
        "counter Zone"
    )
)


_VARIANT_13991: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/31:Pe"
        "rk"
    )
)


_VARIANT_13992: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/32:Ow"
        "ner"
    )
)


_VARIANT_13993: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/33:Fu"
        "rniture"
    )
)


_VARIANT_13994: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/34:Ef"
        "fect Item"
    )
)


_VARIANT_13995: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/35:Ba"
        "se Effect"
    )
)


_VARIANT_13996: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/36:Wo"
        "rldspace"
    )
)


class VatsValueFunction13997(_values.OpenIntEnum):
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


_VARIANT_13997: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/37:VA"
        "TS Value Function"
    )
)


_VARIANT_13999: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/0:Weapon"
    )
)


_VARIANT_14000: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/1:Weapon List"
    )
)


_VARIANT_14001: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/2:Target"
    )
)


_VARIANT_14002: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/3:Target List"
    )
)


_VARIANT_14003: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/4:Unknown"
    )
)


class TargetPart14004(_values.OpenIntEnum):
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


_VARIANT_14004: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/5:Target Part"
    )
)


class VatsAction14005(_values.OpenIntEnum):
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


_VARIANT_14005: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/6:VATS Action"
    )
)


_VARIANT_14006: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/7:Unknown"
    )
)


_VARIANT_14007: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/8:Unknown"
    )
)


_VARIANT_14008: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/9:Critical Effect"
    )
)


_VARIANT_14009: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/10:Critical Effect List"
    )
)


_VARIANT_14010: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/11:Unknown"
    )
)


_VARIANT_14011: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/12:Unknown"
    )
)


_VARIANT_14012: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/13:Unknown"
    )
)


_VARIANT_14013: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/14:Unknown"
    )
)


class WeaponType14014(_values.OpenIntEnum):
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


_VARIANT_14014: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/15:Weapon Type"
    )
)


_VARIANT_14015: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/16:Unknown"
    )
)


_VARIANT_14016: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/17:Unknown"
    )
)


class ProjectileType14017(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_14017: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/18:Projectile Type"
    )
)


class DeliveryType14018(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_14018: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/19:Delivery Type"
    )
)


class CastingType14019(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_14019: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param/variants/20:Casting Type"
    )
)


_VARIANT_13998: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/38:VA"
        "TS Value Param"
    )
)


_VARIANT_14020: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/39:Re"
        "ferenceable Object"
    )
)


_VARIANT_14021: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/40:Re"
        "gion"
    )
)


_VARIANT_14022: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/41:Ke"
        "yword"
    )
)


class PlayerAction14023(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_14023: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/42:Pl"
        "ayer Action"
    )
)


class CastingType14024(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_14024: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/43:Ca"
        "sting Type"
    )
)


_VARIANT_14025: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/44:Sh"
        "out"
    )
)


_VARIANT_14026: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/45:Lo"
        "cation"
    )
)


_VARIANT_14027: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/46:Lo"
        "cation Ref Type"
    )
)


_VARIANT_14028: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/47:Al"
        "ias"
    )
)


_VARIANT_14029: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/48:Pa"
        "ckdata ID"
    )
)


_VARIANT_14030: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/49:As"
        "sociation Type"
    )
)


class FurnitureAnim14031(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_14031: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/50:Fu"
        "rniture Anim"
    )
)


class FurnitureEntry14032(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_14032: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/51:Fu"
        "rniture Entry"
    )
)


_VARIANT_14033: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/52:Sc"
        "ene"
    )
)


class WardState14034(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_14034: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/53:Wa"
        "rd State"
    )
)


_VARIANT_14035: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/54:Ev"
        "ent"
    )
)


_VARIANT_14036: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/55:Ev"
        "ent Data"
    )
)


_VARIANT_14037: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/56:Kn"
        "owable"
    )
)


_VARIANT_14038: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/6:Parameter #2/variants/57:Fa"
        "ction"
    )
)


class RunOn14039(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_14041: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/8:Reference/variants/0:Unused"
    )
)


_VARIANT_14042: _base.Variant = _base.Variant(
    path=(
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload/8:Reference/variants/1:Refere"
        "nce"
    )
)


class Structure13892(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
        "Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/2:Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/3:Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_13899": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/5:Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/6:Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA/payload/8:Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
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
        Annotated[float, _VARIANT_13896]
        | Annotated[_values.FormId, _VARIANT_13897]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_13899: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_13901]
        | Annotated[bytes, _VARIANT_13902]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13903,
        ]
        | Annotated[float, _VARIANT_13904]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13905,
        ]
        | Annotated[Sex13906, _VARIANT_13906]
        | Annotated[ActorValue13907, _VARIANT_13907]
        | Annotated[CrimeType13908, _VARIANT_13908]
        | Annotated[Axis13909, _VARIANT_13909]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13910,
        ]
        | Annotated[MiscStat13911, _VARIANT_13911]
        | Annotated[Alignment13912, _VARIANT_13912]
        | Annotated[_values.FormId, _VARIANT_13913]
        | Annotated[FormType13914, _VARIANT_13914]
        | Annotated[CriticalStage13915, _VARIANT_13915]
        | Annotated[_values.FormId, _VARIANT_13916]
        | Annotated[_values.FormId, _VARIANT_13917]
        | Annotated[_values.FormId, _VARIANT_13918]
        | Annotated[_values.FormId, _VARIANT_13919]
        | Annotated[_values.FormId, _VARIANT_13920]
        | Annotated[_values.FormId, _VARIANT_13921]
        | Annotated[_values.FormId, _VARIANT_13922]
        | Annotated[_values.FormId, _VARIANT_13923]
        | Annotated[_values.FormId, _VARIANT_13924]
        | Annotated[_values.FormId, _VARIANT_13925]
        | Annotated[_values.FormId, _VARIANT_13926]
        | Annotated[_values.FormId, _VARIANT_13927]
        | Annotated[_values.FormId, _VARIANT_13928]
        | Annotated[_values.FormId, _VARIANT_13929]
        | Annotated[_values.FormId, _VARIANT_13930]
        | Annotated[_values.FormId, _VARIANT_13931]
        | Annotated[_values.FormId, _VARIANT_13932]
        | Annotated[_values.FormId, _VARIANT_13933]
        | Annotated[_values.FormId, _VARIANT_13934]
        | Annotated[_values.FormId, _VARIANT_13935]
        | Annotated[_values.FormId, _VARIANT_13936]
        | Annotated[_values.FormId, _VARIANT_13937]
        | Annotated[VatsValueFunction13938, _VARIANT_13938]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13939,
        ]
        | Annotated[_values.FormId, _VARIANT_13940]
        | Annotated[_values.FormId, _VARIANT_13941]
        | Annotated[_values.FormId, _VARIANT_13942]
        | Annotated[PlayerAction13943, _VARIANT_13943]
        | Annotated[CastingType13944, _VARIANT_13944]
        | Annotated[_values.FormId, _VARIANT_13945]
        | Annotated[_values.FormId, _VARIANT_13946]
        | Annotated[_values.FormId, _VARIANT_13947]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13948,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13949,
        ]
        | Annotated[_values.FormId, _VARIANT_13950]
        | Annotated[FurnitureAnim13951, _VARIANT_13951]
        | Annotated[FurnitureEntry13952, _VARIANT_13952]
        | Annotated[_values.FormId, _VARIANT_13953]
        | Annotated[WardState13954, _VARIANT_13954]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13955,
        ]
        | Annotated[_values.FormId, _VARIANT_13956]
        | Annotated[_values.FormId, _VARIANT_13957]
        | Annotated[_values.FormId, _VARIANT_13958]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_13960]
        | Annotated[bytes, _VARIANT_13961]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13962,
        ]
        | Annotated[float, _VARIANT_13963]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13964,
        ]
        | Annotated[Sex13965, _VARIANT_13965]
        | Annotated[ActorValue13966, _VARIANT_13966]
        | Annotated[CrimeType13967, _VARIANT_13967]
        | Annotated[Axis13968, _VARIANT_13968]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13969,
        ]
        | Annotated[MiscStat13970, _VARIANT_13970]
        | Annotated[Alignment13971, _VARIANT_13971]
        | Annotated[_values.FormId, _VARIANT_13972]
        | Annotated[FormType13973, _VARIANT_13973]
        | Annotated[CriticalStage13974, _VARIANT_13974]
        | Annotated[_values.FormId, _VARIANT_13975]
        | Annotated[_values.FormId, _VARIANT_13976]
        | Annotated[_values.FormId, _VARIANT_13977]
        | Annotated[_values.FormId, _VARIANT_13978]
        | Annotated[_values.FormId, _VARIANT_13979]
        | Annotated[_values.FormId, _VARIANT_13980]
        | Annotated[_values.FormId, _VARIANT_13981]
        | Annotated[_values.FormId, _VARIANT_13982]
        | Annotated[_values.FormId, _VARIANT_13983]
        | Annotated[_values.FormId, _VARIANT_13984]
        | Annotated[_values.FormId, _VARIANT_13985]
        | Annotated[_values.FormId, _VARIANT_13986]
        | Annotated[_values.FormId, _VARIANT_13987]
        | Annotated[_values.FormId, _VARIANT_13988]
        | Annotated[_values.FormId, _VARIANT_13989]
        | Annotated[_values.FormId, _VARIANT_13990]
        | Annotated[_values.FormId, _VARIANT_13991]
        | Annotated[_values.FormId, _VARIANT_13992]
        | Annotated[_values.FormId, _VARIANT_13993]
        | Annotated[_values.FormId, _VARIANT_13994]
        | Annotated[_values.FormId, _VARIANT_13995]
        | Annotated[_values.FormId, _VARIANT_13996]
        | Annotated[VatsValueFunction13997, _VARIANT_13997]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13999]
            | Annotated[_values.FormId, _VARIANT_14000]
            | Annotated[_values.FormId, _VARIANT_14001]
            | Annotated[_values.FormId, _VARIANT_14002]
            | Annotated[bytes, _VARIANT_14003]
            | Annotated[TargetPart14004, _VARIANT_14004]
            | Annotated[VatsAction14005, _VARIANT_14005]
            | Annotated[bytes, _VARIANT_14006]
            | Annotated[bytes, _VARIANT_14007]
            | Annotated[_values.FormId, _VARIANT_14008]
            | Annotated[_values.FormId, _VARIANT_14009]
            | Annotated[bytes, _VARIANT_14010]
            | Annotated[bytes, _VARIANT_14011]
            | Annotated[bytes, _VARIANT_14012]
            | Annotated[bytes, _VARIANT_14013]
            | Annotated[WeaponType14014, _VARIANT_14014]
            | Annotated[bytes, _VARIANT_14015]
            | Annotated[bytes, _VARIANT_14016]
            | Annotated[ProjectileType14017, _VARIANT_14017]
            | Annotated[DeliveryType14018, _VARIANT_14018]
            | Annotated[CastingType14019, _VARIANT_14019],
            _VARIANT_13998,
        ]
        | Annotated[_values.FormId, _VARIANT_14020]
        | Annotated[_values.FormId, _VARIANT_14021]
        | Annotated[_values.FormId, _VARIANT_14022]
        | Annotated[PlayerAction14023, _VARIANT_14023]
        | Annotated[CastingType14024, _VARIANT_14024]
        | Annotated[_values.FormId, _VARIANT_14025]
        | Annotated[_values.FormId, _VARIANT_14026]
        | Annotated[_values.FormId, _VARIANT_14027]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_14028,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_14029,
        ]
        | Annotated[_values.FormId, _VARIANT_14030]
        | Annotated[FurnitureAnim14031, _VARIANT_14031]
        | Annotated[FurnitureEntry14032, _VARIANT_14032]
        | Annotated[_values.FormId, _VARIANT_14033]
        | Annotated[WardState14034, _VARIANT_14034]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_14035,
        ]
        | Annotated[_values.FormId, _VARIANT_14036]
        | Annotated[_values.FormId, _VARIANT_14037]
        | Annotated[_values.FormId, _VARIANT_14038]
    )
    """Value decoded from this schema node."""

    run_on: RunOn14039
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_14041,
        ]
        | Annotated[_values.FormId, _VARIANT_14042]
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
        Annotated[float, _VARIANT_13896]
        | Annotated[_values.FormId, _VARIANT_13897]
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
    def field(self, name: Literal["unused_13899"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13901]
        | Annotated[bytes, _VARIANT_13902]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13903,
        ]
        | Annotated[float, _VARIANT_13904]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13905,
        ]
        | Annotated[Sex13906, _VARIANT_13906]
        | Annotated[ActorValue13907, _VARIANT_13907]
        | Annotated[CrimeType13908, _VARIANT_13908]
        | Annotated[Axis13909, _VARIANT_13909]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13910,
        ]
        | Annotated[MiscStat13911, _VARIANT_13911]
        | Annotated[Alignment13912, _VARIANT_13912]
        | Annotated[_values.FormId, _VARIANT_13913]
        | Annotated[FormType13914, _VARIANT_13914]
        | Annotated[CriticalStage13915, _VARIANT_13915]
        | Annotated[_values.FormId, _VARIANT_13916]
        | Annotated[_values.FormId, _VARIANT_13917]
        | Annotated[_values.FormId, _VARIANT_13918]
        | Annotated[_values.FormId, _VARIANT_13919]
        | Annotated[_values.FormId, _VARIANT_13920]
        | Annotated[_values.FormId, _VARIANT_13921]
        | Annotated[_values.FormId, _VARIANT_13922]
        | Annotated[_values.FormId, _VARIANT_13923]
        | Annotated[_values.FormId, _VARIANT_13924]
        | Annotated[_values.FormId, _VARIANT_13925]
        | Annotated[_values.FormId, _VARIANT_13926]
        | Annotated[_values.FormId, _VARIANT_13927]
        | Annotated[_values.FormId, _VARIANT_13928]
        | Annotated[_values.FormId, _VARIANT_13929]
        | Annotated[_values.FormId, _VARIANT_13930]
        | Annotated[_values.FormId, _VARIANT_13931]
        | Annotated[_values.FormId, _VARIANT_13932]
        | Annotated[_values.FormId, _VARIANT_13933]
        | Annotated[_values.FormId, _VARIANT_13934]
        | Annotated[_values.FormId, _VARIANT_13935]
        | Annotated[_values.FormId, _VARIANT_13936]
        | Annotated[_values.FormId, _VARIANT_13937]
        | Annotated[VatsValueFunction13938, _VARIANT_13938]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13939,
        ]
        | Annotated[_values.FormId, _VARIANT_13940]
        | Annotated[_values.FormId, _VARIANT_13941]
        | Annotated[_values.FormId, _VARIANT_13942]
        | Annotated[PlayerAction13943, _VARIANT_13943]
        | Annotated[CastingType13944, _VARIANT_13944]
        | Annotated[_values.FormId, _VARIANT_13945]
        | Annotated[_values.FormId, _VARIANT_13946]
        | Annotated[_values.FormId, _VARIANT_13947]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13948,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13949,
        ]
        | Annotated[_values.FormId, _VARIANT_13950]
        | Annotated[FurnitureAnim13951, _VARIANT_13951]
        | Annotated[FurnitureEntry13952, _VARIANT_13952]
        | Annotated[_values.FormId, _VARIANT_13953]
        | Annotated[WardState13954, _VARIANT_13954]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13955,
        ]
        | Annotated[_values.FormId, _VARIANT_13956]
        | Annotated[_values.FormId, _VARIANT_13957]
        | Annotated[_values.FormId, _VARIANT_13958]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_13960]
        | Annotated[bytes, _VARIANT_13961]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13962,
        ]
        | Annotated[float, _VARIANT_13963]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_13964,
        ]
        | Annotated[Sex13965, _VARIANT_13965]
        | Annotated[ActorValue13966, _VARIANT_13966]
        | Annotated[CrimeType13967, _VARIANT_13967]
        | Annotated[Axis13968, _VARIANT_13968]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_13969,
        ]
        | Annotated[MiscStat13970, _VARIANT_13970]
        | Annotated[Alignment13971, _VARIANT_13971]
        | Annotated[_values.FormId, _VARIANT_13972]
        | Annotated[FormType13973, _VARIANT_13973]
        | Annotated[CriticalStage13974, _VARIANT_13974]
        | Annotated[_values.FormId, _VARIANT_13975]
        | Annotated[_values.FormId, _VARIANT_13976]
        | Annotated[_values.FormId, _VARIANT_13977]
        | Annotated[_values.FormId, _VARIANT_13978]
        | Annotated[_values.FormId, _VARIANT_13979]
        | Annotated[_values.FormId, _VARIANT_13980]
        | Annotated[_values.FormId, _VARIANT_13981]
        | Annotated[_values.FormId, _VARIANT_13982]
        | Annotated[_values.FormId, _VARIANT_13983]
        | Annotated[_values.FormId, _VARIANT_13984]
        | Annotated[_values.FormId, _VARIANT_13985]
        | Annotated[_values.FormId, _VARIANT_13986]
        | Annotated[_values.FormId, _VARIANT_13987]
        | Annotated[_values.FormId, _VARIANT_13988]
        | Annotated[_values.FormId, _VARIANT_13989]
        | Annotated[_values.FormId, _VARIANT_13990]
        | Annotated[_values.FormId, _VARIANT_13991]
        | Annotated[_values.FormId, _VARIANT_13992]
        | Annotated[_values.FormId, _VARIANT_13993]
        | Annotated[_values.FormId, _VARIANT_13994]
        | Annotated[_values.FormId, _VARIANT_13995]
        | Annotated[_values.FormId, _VARIANT_13996]
        | Annotated[VatsValueFunction13997, _VARIANT_13997]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_13999]
            | Annotated[_values.FormId, _VARIANT_14000]
            | Annotated[_values.FormId, _VARIANT_14001]
            | Annotated[_values.FormId, _VARIANT_14002]
            | Annotated[bytes, _VARIANT_14003]
            | Annotated[TargetPart14004, _VARIANT_14004]
            | Annotated[VatsAction14005, _VARIANT_14005]
            | Annotated[bytes, _VARIANT_14006]
            | Annotated[bytes, _VARIANT_14007]
            | Annotated[_values.FormId, _VARIANT_14008]
            | Annotated[_values.FormId, _VARIANT_14009]
            | Annotated[bytes, _VARIANT_14010]
            | Annotated[bytes, _VARIANT_14011]
            | Annotated[bytes, _VARIANT_14012]
            | Annotated[bytes, _VARIANT_14013]
            | Annotated[WeaponType14014, _VARIANT_14014]
            | Annotated[bytes, _VARIANT_14015]
            | Annotated[bytes, _VARIANT_14016]
            | Annotated[ProjectileType14017, _VARIANT_14017]
            | Annotated[DeliveryType14018, _VARIANT_14018]
            | Annotated[CastingType14019, _VARIANT_14019],
            _VARIANT_13998,
        ]
        | Annotated[_values.FormId, _VARIANT_14020]
        | Annotated[_values.FormId, _VARIANT_14021]
        | Annotated[_values.FormId, _VARIANT_14022]
        | Annotated[PlayerAction14023, _VARIANT_14023]
        | Annotated[CastingType14024, _VARIANT_14024]
        | Annotated[_values.FormId, _VARIANT_14025]
        | Annotated[_values.FormId, _VARIANT_14026]
        | Annotated[_values.FormId, _VARIANT_14027]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_14028,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_14029,
        ]
        | Annotated[_values.FormId, _VARIANT_14030]
        | Annotated[FurnitureAnim14031, _VARIANT_14031]
        | Annotated[FurnitureEntry14032, _VARIANT_14032]
        | Annotated[_values.FormId, _VARIANT_14033]
        | Annotated[WardState14034, _VARIANT_14034]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_14035,
        ]
        | Annotated[_values.FormId, _VARIANT_14036]
        | Annotated[_values.FormId, _VARIANT_14037]
        | Annotated[_values.FormId, _VARIANT_14038]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn14039]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_14041,
        ]
        | Annotated[_values.FormId, _VARIANT_14042]
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


class Condition13890(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:Condition"
    )
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/0:CTDA"
            ),
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/1:Parameter #1"
            ),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition/2:Parameter #2"
            ),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure13892] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure13892]]:
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


class Target13883(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST/15:Targets/repeat/0:Target"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "target": _base.Binding(
            path="QUST/15:Targets/repeat/0:Target/0:Target",
            kind="subrecord",
            name="Target",
        ),
        "conditions": _base.Binding(
            path="QUST/15:Targets/repeat/0:Target/1:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path=(
                "QUST/15:Targets/repeat/0:Target/1:Conditions/repeat/0:"
                "Condition"
            ),
            child_kind="sequence",
        ),
    }

    target: Optional[Structure13885] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition13890, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["target"]
    ) -> _base.FieldRef[Optional[Structure13885]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition13890, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class QuestRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "QUST"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "QUST"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="QUST/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="QUST/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "name": _base.Binding(
            path="QUST/2:Name",
            kind="subrecord",
            name="Name",
        ),
        "general": _base.Binding(
            path="QUST/3:General",
            kind="subrecord",
            name="General",
        ),
        "event": _base.Binding(
            path="QUST/4:Event",
            kind="subrecord",
            name="Event",
        ),
        "text_display_globals": _base.Binding(
            path="QUST/5:Text Display Globals",
            kind="repeat",
            name="Text Display Globals",
            repeated_path="QUST/5:Text Display Globals/repeat/0:Global",
            child_kind="subrecord",
        ),
        "object_window_filter": _base.Binding(
            path="QUST/6:Object Window Filter",
            kind="subrecord",
            name="Object Window Filter",
        ),
        "quest_dialogue_conditions": _base.Binding(
            path="QUST/7:Quest Dialogue Conditions",
            kind="sequence",
            name="Quest Dialogue Conditions",
        ),
        "marker": _base.Binding(
            path="QUST/8:Marker",
            kind="subrecord",
            name="Marker",
        ),
        "conditions": _base.Binding(
            path="QUST/9:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="QUST/9:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "stages": _base.Binding(
            path="QUST/10:Stages",
            kind="repeat",
            name="Stages",
            repeated_path="QUST/10:Stages/repeat/0:Stage",
            child_kind="sequence",
        ),
        "objectives": _base.Binding(
            path="QUST/11:Objectives",
            kind="repeat",
            name="Objectives",
            repeated_path="QUST/11:Objectives/repeat/0:Objective",
            child_kind="sequence",
        ),
        "next_alias_id": _base.Binding(
            path="QUST/12:Next Alias ID",
            kind="subrecord",
            name="Next Alias ID",
        ),
        "aliases": _base.Binding(
            path="QUST/13:Aliases",
            kind="repeat",
            name="Aliases",
            repeated_path="QUST/13:Aliases/repeat/0:Alias",
            child_kind="choice",
        ),
        "description": _base.Binding(
            path="QUST/14:Description",
            kind="subrecord",
            name="Description",
        ),
        "targets": _base.Binding(
            path="QUST/15:Targets",
            kind="repeat",
            name="Targets",
            repeated_path="QUST/15:Targets/repeat/0:Target",
            child_kind="sequence",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure12571] = None
    """Value decoded from this schema node."""

    name: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    general: Optional[Structure12686] = None
    """Value decoded from this schema node."""

    event: Optional[str] = None
    """Value decoded from this schema node."""

    text_display_globals: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    object_window_filter: Optional[str] = None
    """Value decoded from this schema node."""

    quest_dialogue_conditions: Optional[QuestDialogueConditions12699] = None
    """Value decoded from this schema node."""

    marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    conditions: tuple[Condition12862, ...] = ()
    """Value decoded from this schema node."""

    stages: tuple[Stage13021, ...] = ()
    """Value decoded from this schema node."""

    objectives: tuple[Objective13201, ...] = ()
    """Value decoded from this schema node."""

    next_alias_id: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    aliases: tuple[
        Annotated[Alias13378, _VARIANT_13378]
        | Annotated[Alias13629, _VARIANT_13629],
        ...,
    ] = ()
    """Value decoded from this schema node."""

    description: Optional[str] = None
    """Value decoded from this schema node."""

    targets: tuple[Target13883, ...] = ()
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
    ) -> _base.FieldRef[Optional[Structure12571]]:
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
        self, name: Literal["general"]
    ) -> _base.FieldRef[Optional[Structure12686]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["event"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["text_display_globals"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["object_window_filter"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["quest_dialogue_conditions"]
    ) -> _base.FieldRef[Optional[QuestDialogueConditions12699]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["marker"]) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition12862, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["stages"]
    ) -> _base.FieldRef[tuple[Stage13021, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["objectives"]
    ) -> _base.FieldRef[tuple[Objective13201, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["next_alias_id"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["aliases"]
    ) -> _base.FieldRef[
        tuple[
            Annotated[Alias13378, _VARIANT_13378]
            | Annotated[Alias13629, _VARIANT_13629],
            ...,
        ]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["targets"]
    ) -> _base.FieldRef[tuple[Target13883, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
