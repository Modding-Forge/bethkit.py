"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags9381(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LOCAL = 0
    INHERITED = 1
    REMOVED = 2
    INHERITED_AND_REMOVED = 3


class Type9385(_values.OpenIntEnum):
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


class Flags9386(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    EDITED = 1
    REMOVED = 3


_VARIANT_9388: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/0:Unused"
    )
)


class ObjectV29390(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9390: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/0:Object v2"
    )
)


class ObjectV19394(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/1:Object Unio"
                "n/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9394: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n/variants/1:Object v1"
    )
)


_VARIANT_9389: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/1:Object Unio"
        "n"
    )
)


_VARIANT_9398: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/2:String"
    )
)


_VARIANT_9399: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/3:Int32"
    )
)


_VARIANT_9400: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/4:Float"
    )
)


class Bool9401(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_9401: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/5:Bool"
    )
)


class ObjectV29404(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unused": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/0:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "alias": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/0:Object v2/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "form_id": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9404: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/0:Object v2"
    )
)


class ObjectV19408(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "form_id": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/0:FormID"
            ),
            kind="primitive",
            name="FormID",
        ),
        "alias": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
                "ject/element/variants/1:Object v1/1:Alias"
            ),
            kind="primitive",
            name="Alias",
        ),
        "unused": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
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


_VARIANT_9408: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject/element/variants/1:Object v1"
    )
)


_VARIANT_9402: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/6:Array of Ob"
        "ject"
    )
)


_VARIANT_9412: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/7:Array of St"
        "ring"
    )
)


_VARIANT_9414: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/8:Array of In"
        "t32"
    )
)


_VARIANT_9416: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/9:Array of Fl"
        "oat"
    )
)


class Element9419(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_9418: _base.Variant = _base.Variant(
    path=(
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element/3:Value/variants/10:Array of B"
        "ool"
    )
)


class Property9383(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
        "nt/2:Properties/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "property_name": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/0:propertyName"
            ),
            kind="primitive",
            name="propertyName",
        ),
        "type": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/1:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "flags": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/2:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "value": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties/element/3:Value"
            ),
            kind="union",
            name="Value",
        ),
    }

    property_name: str
    """Value decoded from this schema node."""

    type: Type9385
    """Value decoded from this schema node."""

    flags: Flags9386
    """Value decoded from this schema node."""

    value: (
        Annotated[bytes, _VARIANT_9388]
        | Annotated[
            Annotated[ObjectV29390, _VARIANT_9390]
            | Annotated[ObjectV19394, _VARIANT_9394],
            _VARIANT_9389,
        ]
        | Annotated[str, _VARIANT_9398]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9399,
        ]
        | Annotated[float, _VARIANT_9400]
        | Annotated[Bool9401, _VARIANT_9401]
        | Annotated[
            tuple[
                Annotated[ObjectV29404, _VARIANT_9404]
                | Annotated[ObjectV19408, _VARIANT_9408],
                ...,
            ],
            _VARIANT_9402,
        ]
        | Annotated[tuple[str, ...], _VARIANT_9412]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_9414,
        ]
        | Annotated[tuple[float, ...], _VARIANT_9416]
        | Annotated[tuple[Element9419, ...], _VARIANT_9418]
    )
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["property_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["type"]) -> _base.FieldRef[Type9385]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9386]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_9388]
        | Annotated[
            Annotated[ObjectV29390, _VARIANT_9390]
            | Annotated[ObjectV19394, _VARIANT_9394],
            _VARIANT_9389,
        ]
        | Annotated[str, _VARIANT_9398]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9399,
        ]
        | Annotated[float, _VARIANT_9400]
        | Annotated[Bool9401, _VARIANT_9401]
        | Annotated[
            tuple[
                Annotated[ObjectV29404, _VARIANT_9404]
                | Annotated[ObjectV19408, _VARIANT_9408],
                ...,
            ],
            _VARIANT_9402,
        ]
        | Annotated[tuple[str, ...], _VARIANT_9412]
        | Annotated[
            tuple[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                ...,
            ],
            _VARIANT_9414,
        ]
        | Annotated[tuple[float, ...], _VARIANT_9416]
        | Annotated[tuple[Element9419, ...], _VARIANT_9418]
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


class Script9379(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/2:Scripts/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "script_name": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/0:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "flags": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "properties": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/2:Scripts/eleme"
                "nt/2:Properties"
            ),
            kind="array",
            name="Properties",
        ),
    }

    script_name: str
    """Value decoded from this schema node."""

    flags: Flags9381
    """Value decoded from this schema node."""

    properties: tuple[Property9383, ...]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["script_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9381]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["properties"]
    ) -> _base.FieldRef[tuple[Property9383, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags9422(enum.IntFlag):
    """Named values from the pinned schema."""

    ON_BEGIN = 1
    ON_END = 2


class Fragment9425(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
        "nts/3:Fragments/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/0:Unknown"
            ),
            kind="primitive",
            name="Unknown",
        ),
        "script_name": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/3:Fragments/element/1:ScriptName"
            ),
            kind="primitive",
            name="ScriptName",
        ),
        "fragment_name": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
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


class ScriptFragments9420(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/1:Virtual Machine Adapter/payload/3:Script Fragments"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "extra_bind_data_version": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/0:Extra bind data version"
            ),
            kind="primitive",
            name="Extra bind data version",
        ),
        "flags": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/1:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "file_name": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
                "nts/2:FileName"
            ),
            kind="primitive",
            name="FileName",
        ),
        "fragments": _base.Binding(
            path=(
                "INFO/1:Virtual Machine Adapter/payload/3:Script Fragme"
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

    flags: Flags9422
    """Value decoded from this schema node."""

    file_name: str
    """Value decoded from this schema node."""

    fragments: tuple[Fragment9425, ...]
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
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9422]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["file_name"]) -> _base.FieldRef[str]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["fragments"]
    ) -> _base.FieldRef[tuple[Fragment9425, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure9375(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INFO/1:Virtual Machine Adapter/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="INFO/1:Virtual Machine Adapter/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "object_format": _base.Binding(
            path=("INFO/1:Virtual Machine Adapter/payload/1:Object Format"),
            kind="primitive",
            name="Object Format",
        ),
        "scripts": _base.Binding(
            path="INFO/1:Virtual Machine Adapter/payload/2:Scripts",
            kind="array",
            name="Scripts",
        ),
        "script_fragments": _base.Binding(
            path=("INFO/1:Virtual Machine Adapter/payload/3:Script Fragments"),
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

    scripts: tuple[Script9379, ...]
    """Value decoded from this schema node."""

    script_fragments: Optional[ScriptFragments9420] = None
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
    ) -> _base.FieldRef[tuple[Script9379, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_fragments"]
    ) -> _base.FieldRef[Optional[ScriptFragments9420]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Flags9433(enum.IntFlag):
    """Named values from the pinned schema."""

    GOODBYE = 1
    RANDOM = 2
    SAY_ONCE = 4
    REQUIRES_PLAYER_ACTIVATION = 8
    INFO_REFUSAL = 16
    RANDOM_END = 32
    INVISIBLE_CONTINUE = 64
    WALK_AWAY = 128
    WALK_AWAY_INVISIBLE_IN_MENU = 256
    FORCE_SUBTITLE = 512
    CAN_MOVE_WHILE_GREETING = 1024
    NO_LIP_FILE = 2048
    REQUIRES_POST_PROCESSING = 4096
    AUDIO_OUTPUT_OVERRIDE = 8192
    SPENDS_FAVOR_POINTS = 16384
    UNKNOWN_16 = 32768


class Structure9432(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INFO/3:Response flags/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="INFO/3:Response flags/payload/0:Flags",
            kind="primitive",
            name="Flags",
        ),
        "reset_hours": _base.Binding(
            path="INFO/3:Response flags/payload/1:Reset Hours",
            kind="primitive",
            name="Reset Hours",
        ),
    }

    flags: Flags9433
    """Value decoded from this schema node."""

    reset_hours: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9433]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reset_hours"]
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


class NoneSmallMediumLarge9440(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class EmotionType9450(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NEUTRAL = 0
    ANGER = 1
    DISGUST = 2
    FEAR = 3
    SAD = 4
    HAPPY = 5
    SURPRISE = 6
    PUZZLED = 7


class Flags9456(enum.IntFlag):
    """Named values from the pinned schema."""

    USE_EMOTION_ANIMATION = 1


class Structure9449(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/9:Responses/repeat/0:Response/0:Response Data/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "emotion_type": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/0:Emotion Type"
            ),
            kind="primitive",
            name="Emotion Type",
        ),
        "emotion_value": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/1:Emotion Value"
            ),
            kind="primitive",
            name="Emotion Value",
        ),
        "unused": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/2:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "response_number": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/3:Response number"
            ),
            kind="primitive",
            name="Response number",
        ),
        "unused_9454": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "sound": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/5:Sound"
            ),
            kind="primitive",
            name="Sound",
        ),
        "flags": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/6:Flags"
            ),
            kind="primitive",
            name="Flags",
        ),
        "unused_9457": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/0:Response Data/pay"
                "load/7:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
    }

    emotion_type: EmotionType9450
    """Value decoded from this schema node."""

    emotion_value: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    unused: bytes
    """Value decoded from this schema node."""

    response_number: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unused_9454: bytes
    """Value decoded from this schema node."""

    sound: _values.FormId
    """Value decoded from this schema node."""

    flags: Flags9456
    """Value decoded from this schema node."""

    unused_9457: bytes
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["emotion_type"]
    ) -> _base.FieldRef[EmotionType9450]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["emotion_value"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["response_number"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9454"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["sound"]) -> _base.FieldRef[_values.FormId]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9456]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unused_9457"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Response9447(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INFO/9:Responses/repeat/0:Response"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "response_data": _base.Binding(
            path=("INFO/9:Responses/repeat/0:Response/0:Response Data"),
            kind="subrecord",
            name="Response Data",
        ),
        "response_text": _base.Binding(
            path=("INFO/9:Responses/repeat/0:Response/1:Response Text"),
            kind="subrecord",
            name="Response Text",
        ),
        "script_notes": _base.Binding(
            path="INFO/9:Responses/repeat/0:Response/2:Script Notes",
            kind="subrecord",
            name="Script Notes",
        ),
        "edits": _base.Binding(
            path="INFO/9:Responses/repeat/0:Response/3:Edits",
            kind="subrecord",
            name="Edits",
        ),
        "idle_animations_speaker": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/4:Idle Animations: Speaker"
            ),
            kind="subrecord",
            name="Idle Animations: Speaker",
        ),
        "idle_animations_listener": _base.Binding(
            path=(
                "INFO/9:Responses/repeat/0:Response/5:Idle Animations: Listener"
            ),
            kind="subrecord",
            name="Idle Animations: Listener",
        ),
    }

    response_data: Optional[Structure9449] = None
    """Value decoded from this schema node."""

    response_text: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    script_notes: Optional[str] = None
    """Value decoded from this schema node."""

    edits: Optional[str] = None
    """Value decoded from this schema node."""

    idle_animations_speaker: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    idle_animations_listener: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["response_data"]
    ) -> _base.FieldRef[Optional[Structure9449]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["response_text"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["script_notes"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["edits"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["idle_animations_speaker"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["idle_animations_listener"]
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


_VARIANT_9475: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/0:Comparison Value - Float"
    )
)


_VARIANT_9476: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/2"
        ":Comparison Value/variants/1:Comparison Value - Global"
    )
)


_VARIANT_9480: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/0:Unknown"
    )
)


_VARIANT_9481: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/1:None"
    )
)


_VARIANT_9482: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/2:Integer"
    )
)


_VARIANT_9483: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/3:Float"
    )
)


_VARIANT_9484: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/4:Variable Name"
    )
)


class Sex9485(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_9485: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/5:Sex"
    )
)


class ActorValue9486(_values.OpenIntEnum):
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


_VARIANT_9486: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/6:Actor Value"
    )
)


class CrimeType9487(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_9487: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/7:Crime Type"
    )
)


class Axis9488(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_9488: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/8:Axis"
    )
)


_VARIANT_9489: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/9:Quest Stage (unused)"
    )
)


class MiscStat9490(_values.OpenIntEnum):
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


_VARIANT_9490: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/10:Misc Stat"
    )
)


class Alignment9491(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_9491: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/11:Alignment"
    )
)


_VARIANT_9492: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/12:Equip Type"
    )
)


class FormType9493(_values.OpenIntEnum):
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


_VARIANT_9493: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/13:Form Type"
    )
)


class CriticalStage9494(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_9494: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/14:Critical Stage"
    )
)


_VARIANT_9495: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/15:Object Reference"
    )
)


_VARIANT_9496: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/16:Inventory Object"
    )
)


_VARIANT_9497: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/17:Actor"
    )
)


_VARIANT_9498: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/18:Voice Type"
    )
)


_VARIANT_9499: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/19:Idle"
    )
)


_VARIANT_9500: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/20:Form List"
    )
)


_VARIANT_9501: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/21:Quest"
    )
)


_VARIANT_9502: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/22:Faction"
    )
)


_VARIANT_9503: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/23:Cell"
    )
)


_VARIANT_9504: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/24:Class"
    )
)


_VARIANT_9505: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/25:Race"
    )
)


_VARIANT_9506: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/26:Actor Base"
    )
)


_VARIANT_9507: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/27:Global"
    )
)


_VARIANT_9508: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/28:Weather"
    )
)


_VARIANT_9509: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/29:Package"
    )
)


_VARIANT_9510: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/30:Encounter Zone"
    )
)


_VARIANT_9511: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/31:Perk"
    )
)


_VARIANT_9512: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/32:Owner"
    )
)


_VARIANT_9513: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/33:Furniture"
    )
)


_VARIANT_9514: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/34:Effect Item"
    )
)


_VARIANT_9515: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/35:Base Effect"
    )
)


_VARIANT_9516: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/36:Worldspace"
    )
)


class VatsValueFunction9517(_values.OpenIntEnum):
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


_VARIANT_9517: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/37:VATS Value Function"
    )
)


_VARIANT_9518: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/38:VATS Value Param (INVALID)"
    )
)


_VARIANT_9519: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/39:Referenceable Object"
    )
)


_VARIANT_9520: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/40:Region"
    )
)


_VARIANT_9521: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/41:Keyword"
    )
)


class PlayerAction9522(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_9522: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/42:Player Action"
    )
)


class CastingType9523(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_9523: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/43:Casting Type"
    )
)


_VARIANT_9524: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/44:Shout"
    )
)


_VARIANT_9525: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/45:Location"
    )
)


_VARIANT_9526: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/46:Location Ref Type"
    )
)


_VARIANT_9527: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/47:Alias"
    )
)


_VARIANT_9528: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/48:Packdata ID"
    )
)


_VARIANT_9529: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/49:Association Type"
    )
)


class FurnitureAnim9530(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_9530: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/50:Furniture Anim"
    )
)


class FurnitureEntry9531(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_9531: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/51:Furniture Entry"
    )
)


_VARIANT_9532: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/52:Scene"
    )
)


class WardState9533(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_9533: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/53:Ward State"
    )
)


_VARIANT_9534: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/54:Event"
    )
)


_VARIANT_9535: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/55:Event Data"
    )
)


_VARIANT_9536: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/56:Knowable"
    )
)


_VARIANT_9537: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
        ":Parameter #1/variants/57:Faction"
    )
)


_VARIANT_9539: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/0:Unknown"
    )
)


_VARIANT_9540: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/1:None"
    )
)


_VARIANT_9541: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/2:Integer"
    )
)


_VARIANT_9542: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/3:Float"
    )
)


_VARIANT_9543: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/4:Variable Name"
    )
)


class Sex9544(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MALE = 0
    FEMALE = 1


_VARIANT_9544: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/5:Sex"
    )
)


class ActorValue9545(_values.OpenIntEnum):
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


_VARIANT_9545: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/6:Actor Value"
    )
)


class CrimeType9546(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = -1
    STEAL = 0
    PICKPOCKET = 1
    TRESPASS = 2
    ATTACK = 3
    MURDER = 4
    ESCAPE_JAIL = 5
    WEREWOLF_TRANSFORMATION = 6


_VARIANT_9546: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/7:Crime Type"
    )
)


class Axis9547(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    X = 88
    Y = 89
    Z = 90


_VARIANT_9547: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/8:Axis"
    )
)


_VARIANT_9548: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/9:Quest Stage"
    )
)


class MiscStat9549(_values.OpenIntEnum):
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


_VARIANT_9549: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/10:Misc Stat"
    )
)


class Alignment9550(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    GOOD = 0
    NEUTRAL = 1
    EVIL = 2
    VERY_GOOD = 3
    VERY_EVIL = 4


_VARIANT_9550: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/11:Alignment"
    )
)


_VARIANT_9551: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/12:Equip Type"
    )
)


class FormType9552(_values.OpenIntEnum):
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


_VARIANT_9552: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/13:Form Type"
    )
)


class CriticalStage9553(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    GOO_START = 1
    GOO_END = 2
    DISINTEGRATE_START = 3
    DISINTEGRATE_END = 4


_VARIANT_9553: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/14:Critical Stage"
    )
)


_VARIANT_9554: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/15:Object Reference"
    )
)


_VARIANT_9555: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/16:Inventory Object"
    )
)


_VARIANT_9556: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/17:Actor"
    )
)


_VARIANT_9557: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/18:Voice Type"
    )
)


_VARIANT_9558: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/19:Idle"
    )
)


_VARIANT_9559: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/20:Form List"
    )
)


_VARIANT_9560: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/21:Quest"
    )
)


_VARIANT_9561: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/22:Faction"
    )
)


_VARIANT_9562: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/23:Cell"
    )
)


_VARIANT_9563: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/24:Class"
    )
)


_VARIANT_9564: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/25:Race"
    )
)


_VARIANT_9565: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/26:Actor Base"
    )
)


_VARIANT_9566: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/27:Global"
    )
)


_VARIANT_9567: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/28:Weather"
    )
)


_VARIANT_9568: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/29:Package"
    )
)


_VARIANT_9569: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/30:Encounter Zone"
    )
)


_VARIANT_9570: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/31:Perk"
    )
)


_VARIANT_9571: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/32:Owner"
    )
)


_VARIANT_9572: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/33:Furniture"
    )
)


_VARIANT_9573: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/34:Effect Item"
    )
)


_VARIANT_9574: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/35:Base Effect"
    )
)


_VARIANT_9575: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/36:Worldspace"
    )
)


class VatsValueFunction9576(_values.OpenIntEnum):
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


_VARIANT_9576: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/37:VATS Value Function"
    )
)


_VARIANT_9578: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/0:"
        "Weapon"
    )
)


_VARIANT_9579: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/1:"
        "Weapon List"
    )
)


_VARIANT_9580: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/2:"
        "Target"
    )
)


_VARIANT_9581: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/3:"
        "Target List"
    )
)


_VARIANT_9582: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/4:"
        "Unknown"
    )
)


class TargetPart9583(_values.OpenIntEnum):
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


_VARIANT_9583: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/5:"
        "Target Part"
    )
)


class VatsAction9584(_values.OpenIntEnum):
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


_VARIANT_9584: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/6:"
        "VATS Action"
    )
)


_VARIANT_9585: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/7:"
        "Unknown"
    )
)


_VARIANT_9586: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/8:"
        "Unknown"
    )
)


_VARIANT_9587: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/9:"
        "Critical Effect"
    )
)


_VARIANT_9588: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/10"
        ":Critical Effect List"
    )
)


_VARIANT_9589: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/11"
        ":Unknown"
    )
)


_VARIANT_9590: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/12"
        ":Unknown"
    )
)


_VARIANT_9591: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/13"
        ":Unknown"
    )
)


_VARIANT_9592: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/14"
        ":Unknown"
    )
)


class WeaponType9593(_values.OpenIntEnum):
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


_VARIANT_9593: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/15"
        ":Weapon Type"
    )
)


_VARIANT_9594: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/16"
        ":Unknown"
    )
)


_VARIANT_9595: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/17"
        ":Unknown"
    )
)


class ProjectileType9596(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    MISSILE = 0
    LOBBER = 1
    BEAM = 2
    FLAME = 3
    CONE = 4
    BARRIER = 5
    ARROW = 6


_VARIANT_9596: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/18"
        ":Projectile Type"
    )
)


class DeliveryType9597(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SELF = 0
    TOUCH = 1
    AIMED = 2
    TARGET_ACTOR = 3
    TARGET_LOCATION = 4


_VARIANT_9597: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/19"
        ":Delivery Type"
    )
)


class CastingType9598(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    CONSTANT_EFFECT = 0
    FIRE_AND_FORGET = 1
    CONCENTRATION = 2
    SCROLL = 3


_VARIANT_9598: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param/variants/20"
        ":Casting Type"
    )
)


_VARIANT_9577: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/38:VATS Value Param"
    )
)


_VARIANT_9599: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/39:Referenceable Object"
    )
)


_VARIANT_9600: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/40:Region"
    )
)


_VARIANT_9601: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/41:Keyword"
    )
)


class PlayerAction9602(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NORMAL_USAGE = 0
    POWER_ATTACK = 1
    BASH = 2
    LOCKPICK_SUCCESS = 3
    LOCKPICK_BROKEN = 4


_VARIANT_9602: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/42:Player Action"
    )
)


class CastingType9603(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    LEFT = 0
    RIGHT = 1
    VOICE = 2
    INSTANT = 3


_VARIANT_9603: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/43:Casting Type"
    )
)


_VARIANT_9604: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/44:Shout"
    )
)


_VARIANT_9605: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/45:Location"
    )
)


_VARIANT_9606: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/46:Location Ref Type"
    )
)


_VARIANT_9607: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/47:Alias"
    )
)


_VARIANT_9608: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/48:Packdata ID"
    )
)


_VARIANT_9609: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/49:Association Type"
    )
)


class FurnitureAnim9610(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SIT = 1
    LAY = 2
    LEAN = 4


_VARIANT_9610: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/50:Furniture Anim"
    )
)


class FurnitureEntry9611(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FRONT = 65536
    BEHIND = 131072
    RIGHT = 262144
    LEFT = 524288
    UP = 1048576


_VARIANT_9611: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/51:Furniture Entry"
    )
)


_VARIANT_9612: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/52:Scene"
    )
)


class WardState9613(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    NONE = 0
    ABSORB = 1
    BREAK = 2


_VARIANT_9613: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/53:Ward State"
    )
)


_VARIANT_9614: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/54:Event"
    )
)


_VARIANT_9615: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/55:Event Data"
    )
)


_VARIANT_9616: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/56:Knowable"
    )
)


_VARIANT_9617: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
        ":Parameter #2/variants/57:Faction"
    )
)


class RunOn9618(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    SUBJECT = 0
    TARGET = 1
    REFERENCE = 2
    COMBAT_TARGET = 3
    LINKED_REFERENCE = 4
    QUEST_ALIAS = 5
    PACKAGE_DATA = 6
    EVENT_DATA = 7


_VARIANT_9620: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/0:Unused"
    )
)


_VARIANT_9621: _base.Variant = _base.Variant(
    path=(
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/8"
        ":Reference/variants/1:Reference"
    )
)


class Structure9471(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "type": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/0:Type"
            ),
            kind="primitive",
            name="Type",
        ),
        "unused": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/1:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "comparison_value": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/2"
                ":Comparison Value"
            ),
            kind="union",
            name="Comparison Value",
        ),
        "function": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/3"
                ":Function"
            ),
            kind="primitive",
            name="Function",
        ),
        "unused_9478": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/4:Unused"
            ),
            kind="primitive",
            name="Unused",
        ),
        "parameter_1": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/5"
                ":Parameter #1"
            ),
            kind="union",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/6"
                ":Parameter #2"
            ),
            kind="union",
            name="Parameter #2",
        ),
        "run_on": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/7:Run On"
            ),
            kind="primitive",
            name="Run On",
        ),
        "reference": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/8"
                ":Reference"
            ),
            kind="union",
            name="Reference",
        ),
        "parameter_3": _base.Binding(
            path=(
                "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload/9"
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
        Annotated[float, _VARIANT_9475]
        | Annotated[_values.FormId, _VARIANT_9476]
    )
    """Value decoded from this schema node."""

    function: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    unused_9478: bytes
    """Value decoded from this schema node."""

    parameter_1: (
        Annotated[bytes, _VARIANT_9480]
        | Annotated[bytes, _VARIANT_9481]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9482,
        ]
        | Annotated[float, _VARIANT_9483]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9484,
        ]
        | Annotated[Sex9485, _VARIANT_9485]
        | Annotated[ActorValue9486, _VARIANT_9486]
        | Annotated[CrimeType9487, _VARIANT_9487]
        | Annotated[Axis9488, _VARIANT_9488]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9489,
        ]
        | Annotated[MiscStat9490, _VARIANT_9490]
        | Annotated[Alignment9491, _VARIANT_9491]
        | Annotated[_values.FormId, _VARIANT_9492]
        | Annotated[FormType9493, _VARIANT_9493]
        | Annotated[CriticalStage9494, _VARIANT_9494]
        | Annotated[_values.FormId, _VARIANT_9495]
        | Annotated[_values.FormId, _VARIANT_9496]
        | Annotated[_values.FormId, _VARIANT_9497]
        | Annotated[_values.FormId, _VARIANT_9498]
        | Annotated[_values.FormId, _VARIANT_9499]
        | Annotated[_values.FormId, _VARIANT_9500]
        | Annotated[_values.FormId, _VARIANT_9501]
        | Annotated[_values.FormId, _VARIANT_9502]
        | Annotated[_values.FormId, _VARIANT_9503]
        | Annotated[_values.FormId, _VARIANT_9504]
        | Annotated[_values.FormId, _VARIANT_9505]
        | Annotated[_values.FormId, _VARIANT_9506]
        | Annotated[_values.FormId, _VARIANT_9507]
        | Annotated[_values.FormId, _VARIANT_9508]
        | Annotated[_values.FormId, _VARIANT_9509]
        | Annotated[_values.FormId, _VARIANT_9510]
        | Annotated[_values.FormId, _VARIANT_9511]
        | Annotated[_values.FormId, _VARIANT_9512]
        | Annotated[_values.FormId, _VARIANT_9513]
        | Annotated[_values.FormId, _VARIANT_9514]
        | Annotated[_values.FormId, _VARIANT_9515]
        | Annotated[_values.FormId, _VARIANT_9516]
        | Annotated[VatsValueFunction9517, _VARIANT_9517]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9518,
        ]
        | Annotated[_values.FormId, _VARIANT_9519]
        | Annotated[_values.FormId, _VARIANT_9520]
        | Annotated[_values.FormId, _VARIANT_9521]
        | Annotated[PlayerAction9522, _VARIANT_9522]
        | Annotated[CastingType9523, _VARIANT_9523]
        | Annotated[_values.FormId, _VARIANT_9524]
        | Annotated[_values.FormId, _VARIANT_9525]
        | Annotated[_values.FormId, _VARIANT_9526]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9527,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9528,
        ]
        | Annotated[_values.FormId, _VARIANT_9529]
        | Annotated[FurnitureAnim9530, _VARIANT_9530]
        | Annotated[FurnitureEntry9531, _VARIANT_9531]
        | Annotated[_values.FormId, _VARIANT_9532]
        | Annotated[WardState9533, _VARIANT_9533]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9534,
        ]
        | Annotated[_values.FormId, _VARIANT_9535]
        | Annotated[_values.FormId, _VARIANT_9536]
        | Annotated[_values.FormId, _VARIANT_9537]
    )
    """Value decoded from this schema node."""

    parameter_2: (
        Annotated[bytes, _VARIANT_9539]
        | Annotated[bytes, _VARIANT_9540]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9541,
        ]
        | Annotated[float, _VARIANT_9542]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9543,
        ]
        | Annotated[Sex9544, _VARIANT_9544]
        | Annotated[ActorValue9545, _VARIANT_9545]
        | Annotated[CrimeType9546, _VARIANT_9546]
        | Annotated[Axis9547, _VARIANT_9547]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9548,
        ]
        | Annotated[MiscStat9549, _VARIANT_9549]
        | Annotated[Alignment9550, _VARIANT_9550]
        | Annotated[_values.FormId, _VARIANT_9551]
        | Annotated[FormType9552, _VARIANT_9552]
        | Annotated[CriticalStage9553, _VARIANT_9553]
        | Annotated[_values.FormId, _VARIANT_9554]
        | Annotated[_values.FormId, _VARIANT_9555]
        | Annotated[_values.FormId, _VARIANT_9556]
        | Annotated[_values.FormId, _VARIANT_9557]
        | Annotated[_values.FormId, _VARIANT_9558]
        | Annotated[_values.FormId, _VARIANT_9559]
        | Annotated[_values.FormId, _VARIANT_9560]
        | Annotated[_values.FormId, _VARIANT_9561]
        | Annotated[_values.FormId, _VARIANT_9562]
        | Annotated[_values.FormId, _VARIANT_9563]
        | Annotated[_values.FormId, _VARIANT_9564]
        | Annotated[_values.FormId, _VARIANT_9565]
        | Annotated[_values.FormId, _VARIANT_9566]
        | Annotated[_values.FormId, _VARIANT_9567]
        | Annotated[_values.FormId, _VARIANT_9568]
        | Annotated[_values.FormId, _VARIANT_9569]
        | Annotated[_values.FormId, _VARIANT_9570]
        | Annotated[_values.FormId, _VARIANT_9571]
        | Annotated[_values.FormId, _VARIANT_9572]
        | Annotated[_values.FormId, _VARIANT_9573]
        | Annotated[_values.FormId, _VARIANT_9574]
        | Annotated[_values.FormId, _VARIANT_9575]
        | Annotated[VatsValueFunction9576, _VARIANT_9576]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_9578]
            | Annotated[_values.FormId, _VARIANT_9579]
            | Annotated[_values.FormId, _VARIANT_9580]
            | Annotated[_values.FormId, _VARIANT_9581]
            | Annotated[bytes, _VARIANT_9582]
            | Annotated[TargetPart9583, _VARIANT_9583]
            | Annotated[VatsAction9584, _VARIANT_9584]
            | Annotated[bytes, _VARIANT_9585]
            | Annotated[bytes, _VARIANT_9586]
            | Annotated[_values.FormId, _VARIANT_9587]
            | Annotated[_values.FormId, _VARIANT_9588]
            | Annotated[bytes, _VARIANT_9589]
            | Annotated[bytes, _VARIANT_9590]
            | Annotated[bytes, _VARIANT_9591]
            | Annotated[bytes, _VARIANT_9592]
            | Annotated[WeaponType9593, _VARIANT_9593]
            | Annotated[bytes, _VARIANT_9594]
            | Annotated[bytes, _VARIANT_9595]
            | Annotated[ProjectileType9596, _VARIANT_9596]
            | Annotated[DeliveryType9597, _VARIANT_9597]
            | Annotated[CastingType9598, _VARIANT_9598],
            _VARIANT_9577,
        ]
        | Annotated[_values.FormId, _VARIANT_9599]
        | Annotated[_values.FormId, _VARIANT_9600]
        | Annotated[_values.FormId, _VARIANT_9601]
        | Annotated[PlayerAction9602, _VARIANT_9602]
        | Annotated[CastingType9603, _VARIANT_9603]
        | Annotated[_values.FormId, _VARIANT_9604]
        | Annotated[_values.FormId, _VARIANT_9605]
        | Annotated[_values.FormId, _VARIANT_9606]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9607,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9608,
        ]
        | Annotated[_values.FormId, _VARIANT_9609]
        | Annotated[FurnitureAnim9610, _VARIANT_9610]
        | Annotated[FurnitureEntry9611, _VARIANT_9611]
        | Annotated[_values.FormId, _VARIANT_9612]
        | Annotated[WardState9613, _VARIANT_9613]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9614,
        ]
        | Annotated[_values.FormId, _VARIANT_9615]
        | Annotated[_values.FormId, _VARIANT_9616]
        | Annotated[_values.FormId, _VARIANT_9617]
    )
    """Value decoded from this schema node."""

    run_on: RunOn9618
    """Value decoded from this schema node."""

    reference: (
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9620,
        ]
        | Annotated[_values.FormId, _VARIANT_9621]
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
        Annotated[float, _VARIANT_9475]
        | Annotated[_values.FormId, _VARIANT_9476]
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
    def field(self, name: Literal["unused_9478"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_1"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_9480]
        | Annotated[bytes, _VARIANT_9481]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9482,
        ]
        | Annotated[float, _VARIANT_9483]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9484,
        ]
        | Annotated[Sex9485, _VARIANT_9485]
        | Annotated[ActorValue9486, _VARIANT_9486]
        | Annotated[CrimeType9487, _VARIANT_9487]
        | Annotated[Axis9488, _VARIANT_9488]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9489,
        ]
        | Annotated[MiscStat9490, _VARIANT_9490]
        | Annotated[Alignment9491, _VARIANT_9491]
        | Annotated[_values.FormId, _VARIANT_9492]
        | Annotated[FormType9493, _VARIANT_9493]
        | Annotated[CriticalStage9494, _VARIANT_9494]
        | Annotated[_values.FormId, _VARIANT_9495]
        | Annotated[_values.FormId, _VARIANT_9496]
        | Annotated[_values.FormId, _VARIANT_9497]
        | Annotated[_values.FormId, _VARIANT_9498]
        | Annotated[_values.FormId, _VARIANT_9499]
        | Annotated[_values.FormId, _VARIANT_9500]
        | Annotated[_values.FormId, _VARIANT_9501]
        | Annotated[_values.FormId, _VARIANT_9502]
        | Annotated[_values.FormId, _VARIANT_9503]
        | Annotated[_values.FormId, _VARIANT_9504]
        | Annotated[_values.FormId, _VARIANT_9505]
        | Annotated[_values.FormId, _VARIANT_9506]
        | Annotated[_values.FormId, _VARIANT_9507]
        | Annotated[_values.FormId, _VARIANT_9508]
        | Annotated[_values.FormId, _VARIANT_9509]
        | Annotated[_values.FormId, _VARIANT_9510]
        | Annotated[_values.FormId, _VARIANT_9511]
        | Annotated[_values.FormId, _VARIANT_9512]
        | Annotated[_values.FormId, _VARIANT_9513]
        | Annotated[_values.FormId, _VARIANT_9514]
        | Annotated[_values.FormId, _VARIANT_9515]
        | Annotated[_values.FormId, _VARIANT_9516]
        | Annotated[VatsValueFunction9517, _VARIANT_9517]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9518,
        ]
        | Annotated[_values.FormId, _VARIANT_9519]
        | Annotated[_values.FormId, _VARIANT_9520]
        | Annotated[_values.FormId, _VARIANT_9521]
        | Annotated[PlayerAction9522, _VARIANT_9522]
        | Annotated[CastingType9523, _VARIANT_9523]
        | Annotated[_values.FormId, _VARIANT_9524]
        | Annotated[_values.FormId, _VARIANT_9525]
        | Annotated[_values.FormId, _VARIANT_9526]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9527,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9528,
        ]
        | Annotated[_values.FormId, _VARIANT_9529]
        | Annotated[FurnitureAnim9530, _VARIANT_9530]
        | Annotated[FurnitureEntry9531, _VARIANT_9531]
        | Annotated[_values.FormId, _VARIANT_9532]
        | Annotated[WardState9533, _VARIANT_9533]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9534,
        ]
        | Annotated[_values.FormId, _VARIANT_9535]
        | Annotated[_values.FormId, _VARIANT_9536]
        | Annotated[_values.FormId, _VARIANT_9537]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["parameter_2"]
    ) -> _base.FieldRef[
        Annotated[bytes, _VARIANT_9539]
        | Annotated[bytes, _VARIANT_9540]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9541,
        ]
        | Annotated[float, _VARIANT_9542]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9543,
        ]
        | Annotated[Sex9544, _VARIANT_9544]
        | Annotated[ActorValue9545, _VARIANT_9545]
        | Annotated[CrimeType9546, _VARIANT_9546]
        | Annotated[Axis9547, _VARIANT_9547]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9548,
        ]
        | Annotated[MiscStat9549, _VARIANT_9549]
        | Annotated[Alignment9550, _VARIANT_9550]
        | Annotated[_values.FormId, _VARIANT_9551]
        | Annotated[FormType9552, _VARIANT_9552]
        | Annotated[CriticalStage9553, _VARIANT_9553]
        | Annotated[_values.FormId, _VARIANT_9554]
        | Annotated[_values.FormId, _VARIANT_9555]
        | Annotated[_values.FormId, _VARIANT_9556]
        | Annotated[_values.FormId, _VARIANT_9557]
        | Annotated[_values.FormId, _VARIANT_9558]
        | Annotated[_values.FormId, _VARIANT_9559]
        | Annotated[_values.FormId, _VARIANT_9560]
        | Annotated[_values.FormId, _VARIANT_9561]
        | Annotated[_values.FormId, _VARIANT_9562]
        | Annotated[_values.FormId, _VARIANT_9563]
        | Annotated[_values.FormId, _VARIANT_9564]
        | Annotated[_values.FormId, _VARIANT_9565]
        | Annotated[_values.FormId, _VARIANT_9566]
        | Annotated[_values.FormId, _VARIANT_9567]
        | Annotated[_values.FormId, _VARIANT_9568]
        | Annotated[_values.FormId, _VARIANT_9569]
        | Annotated[_values.FormId, _VARIANT_9570]
        | Annotated[_values.FormId, _VARIANT_9571]
        | Annotated[_values.FormId, _VARIANT_9572]
        | Annotated[_values.FormId, _VARIANT_9573]
        | Annotated[_values.FormId, _VARIANT_9574]
        | Annotated[_values.FormId, _VARIANT_9575]
        | Annotated[VatsValueFunction9576, _VARIANT_9576]
        | Annotated[
            Annotated[_values.FormId, _VARIANT_9578]
            | Annotated[_values.FormId, _VARIANT_9579]
            | Annotated[_values.FormId, _VARIANT_9580]
            | Annotated[_values.FormId, _VARIANT_9581]
            | Annotated[bytes, _VARIANT_9582]
            | Annotated[TargetPart9583, _VARIANT_9583]
            | Annotated[VatsAction9584, _VARIANT_9584]
            | Annotated[bytes, _VARIANT_9585]
            | Annotated[bytes, _VARIANT_9586]
            | Annotated[_values.FormId, _VARIANT_9587]
            | Annotated[_values.FormId, _VARIANT_9588]
            | Annotated[bytes, _VARIANT_9589]
            | Annotated[bytes, _VARIANT_9590]
            | Annotated[bytes, _VARIANT_9591]
            | Annotated[bytes, _VARIANT_9592]
            | Annotated[WeaponType9593, _VARIANT_9593]
            | Annotated[bytes, _VARIANT_9594]
            | Annotated[bytes, _VARIANT_9595]
            | Annotated[ProjectileType9596, _VARIANT_9596]
            | Annotated[DeliveryType9597, _VARIANT_9597]
            | Annotated[CastingType9598, _VARIANT_9598],
            _VARIANT_9577,
        ]
        | Annotated[_values.FormId, _VARIANT_9599]
        | Annotated[_values.FormId, _VARIANT_9600]
        | Annotated[_values.FormId, _VARIANT_9601]
        | Annotated[PlayerAction9602, _VARIANT_9602]
        | Annotated[CastingType9603, _VARIANT_9603]
        | Annotated[_values.FormId, _VARIANT_9604]
        | Annotated[_values.FormId, _VARIANT_9605]
        | Annotated[_values.FormId, _VARIANT_9606]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_9607,
        ]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9608,
        ]
        | Annotated[_values.FormId, _VARIANT_9609]
        | Annotated[FurnitureAnim9610, _VARIANT_9610]
        | Annotated[FurnitureEntry9611, _VARIANT_9611]
        | Annotated[_values.FormId, _VARIANT_9612]
        | Annotated[WardState9613, _VARIANT_9613]
        | Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9614,
        ]
        | Annotated[_values.FormId, _VARIANT_9615]
        | Annotated[_values.FormId, _VARIANT_9616]
        | Annotated[_values.FormId, _VARIANT_9617]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["run_on"]) -> _base.FieldRef[RunOn9618]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reference"]
    ) -> _base.FieldRef[
        Annotated[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)],
            _VARIANT_9620,
        ]
        | Annotated[_values.FormId, _VARIANT_9621]
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


class Condition9469(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INFO/10:Conditions/repeat/0:Condition"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "ctda": _base.Binding(
            path="INFO/10:Conditions/repeat/0:Condition/0:CTDA",
            kind="subrecord",
            name="CTDA",
        ),
        "parameter_1": _base.Binding(
            path=("INFO/10:Conditions/repeat/0:Condition/1:Parameter #1"),
            kind="subrecord",
            name="Parameter #1",
        ),
        "parameter_2": _base.Binding(
            path=("INFO/10:Conditions/repeat/0:Condition/2:Parameter #2"),
            kind="subrecord",
            name="Parameter #2",
        ),
    }

    ctda: Optional[Structure9471] = None
    """Value decoded from this schema node."""

    parameter_1: Optional[str] = None
    """Value decoded from this schema node."""

    parameter_2: Optional[str] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["ctda"]
    ) -> _base.FieldRef[Optional[Structure9471]]:
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


class Unknown9628(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INFO/11:Unknown/repeat/0:Unknown"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="INFO/11:Unknown/repeat/0:Unknown/0:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_9631": _base.Binding(
            path="INFO/11:Unknown/repeat/0:Unknown/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "marker": _base.Binding(
            path="INFO/11:Unknown/repeat/0:Unknown/2:Marker",
            kind="subrecord",
            name="Marker",
        ),
    }

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_9631: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    marker: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_9631"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
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


class InfoRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "INFO"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "INFO"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="INFO/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "virtual_machine_adapter": _base.Binding(
            path="INFO/1:Virtual Machine Adapter",
            kind="subrecord",
            name="Virtual Machine Adapter",
        ),
        "unknown": _base.Binding(
            path="INFO/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "response_flags": _base.Binding(
            path="INFO/3:Response flags",
            kind="subrecord",
            name="Response flags",
        ),
        "topic": _base.Binding(
            path="INFO/4:Topic",
            kind="subrecord",
            name="Topic",
        ),
        "previous_info": _base.Binding(
            path="INFO/5:Previous INFO",
            kind="subrecord",
            name="Previous INFO",
        ),
        "favor_level": _base.Binding(
            path="INFO/6:Favor Level",
            kind="subrecord",
            name="Favor Level",
        ),
        "link_to": _base.Binding(
            path="INFO/7:Link To",
            kind="repeat",
            name="Link To",
            repeated_path="INFO/7:Link To/repeat/0:Response",
            child_kind="subrecord",
        ),
        "response_data": _base.Binding(
            path="INFO/8:Response Data",
            kind="subrecord",
            name="Response Data",
        ),
        "responses": _base.Binding(
            path="INFO/9:Responses",
            kind="repeat",
            name="Responses",
            repeated_path="INFO/9:Responses/repeat/0:Response",
            child_kind="sequence",
        ),
        "conditions": _base.Binding(
            path="INFO/10:Conditions",
            kind="repeat",
            name="Conditions",
            repeated_path="INFO/10:Conditions/repeat/0:Condition",
            child_kind="sequence",
        ),
        "unknown_9627": _base.Binding(
            path="INFO/11:Unknown",
            kind="repeat",
            name="Unknown",
            repeated_path="INFO/11:Unknown/repeat/0:Unknown",
            child_kind="sequence",
        ),
        "prompt": _base.Binding(
            path="INFO/12:Prompt",
            kind="subrecord",
            name="Prompt",
        ),
        "speaker": _base.Binding(
            path="INFO/13:Speaker",
            kind="subrecord",
            name="Speaker",
        ),
        "walk_away_topic": _base.Binding(
            path="INFO/14:Walk Away Topic",
            kind="subrecord",
            name="Walk Away Topic",
        ),
        "audio_output_override": _base.Binding(
            path="INFO/15:Audio Output Override",
            kind="subrecord",
            name="Audio Output Override",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    virtual_machine_adapter: Optional[Structure9375] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    response_flags: Optional[Structure9432] = None
    """Value decoded from this schema node."""

    topic: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    previous_info: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    favor_level: Optional[NoneSmallMediumLarge9440] = None
    """Value decoded from this schema node."""

    link_to: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    response_data: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    responses: tuple[Response9447, ...] = ()
    """Value decoded from this schema node."""

    conditions: tuple[Condition9469, ...] = ()
    """Value decoded from this schema node."""

    unknown_9627: tuple[Unknown9628, ...] = ()
    """Value decoded from this schema node."""

    prompt: Optional[str | _values.UInt32] = None
    """Value decoded from this schema node."""

    speaker: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    walk_away_topic: Optional[_values.FormId] = None
    """Value decoded from this schema node."""

    audio_output_override: Optional[_values.FormId] = None
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
    ) -> _base.FieldRef[Optional[Structure9375]]:
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
        self, name: Literal["response_flags"]
    ) -> _base.FieldRef[Optional[Structure9432]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["topic"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["previous_info"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["favor_level"]
    ) -> _base.FieldRef[Optional[NoneSmallMediumLarge9440]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["link_to"]
    ) -> _base.FieldRef[tuple[_values.FormId, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["response_data"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["responses"]
    ) -> _base.FieldRef[tuple[Response9447, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["conditions"]
    ) -> _base.FieldRef[tuple[Condition9469, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_9627"]
    ) -> _base.FieldRef[tuple[Unknown9628, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["prompt"]
    ) -> _base.FieldRef[Optional[str | _values.UInt32]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["speaker"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["walk_away_topic"]
    ) -> _base.FieldRef[Optional[_values.FormId]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["audio_output_override"]
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
