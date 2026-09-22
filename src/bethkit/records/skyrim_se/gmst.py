"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values

_VARIANT_4178: _base.Variant = _base.Variant(
    path="GMST/1:Value/payload/variants/0:Name"
)


_VARIANT_4179: _base.Variant = _base.Variant(
    path="GMST/1:Value/payload/variants/1:Int"
)


_VARIANT_4180: _base.Variant = _base.Variant(
    path="GMST/1:Value/payload/variants/2:Float"
)


class Bool4181(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


_VARIANT_4181: _base.Variant = _base.Variant(
    path="GMST/1:Value/payload/variants/3:Bool"
)


class GameSettingRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "GMST"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "GMST"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="GMST/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "value": _base.Binding(
            path="GMST/1:Value",
            kind="subrecord",
            name="Value",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    value: Optional[
        Annotated[str | _values.UInt32, _VARIANT_4178]
        | Annotated[
            Annotated[
                int, pydantic.Field(strict=True, ge=-2147483648, le=2147483647)
            ],
            _VARIANT_4179,
        ]
        | Annotated[float, _VARIANT_4180]
        | Annotated[Bool4181, _VARIANT_4181]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["value"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[str | _values.UInt32, _VARIANT_4178]
            | Annotated[
                Annotated[
                    int,
                    pydantic.Field(strict=True, ge=-2147483648, le=2147483647),
                ],
                _VARIANT_4179,
            ]
            | Annotated[float, _VARIANT_4180]
            | Annotated[Bool4181, _VARIANT_4181]
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
