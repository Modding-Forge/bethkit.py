"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

import enum
from typing import ClassVar, Literal, Optional, overload

from .. import _base


class AllowDefaultDialogFemale6594(enum.IntFlag):
    """Named values from the pinned schema."""

    ALLOW_DEFAULT_DIALOG = 1
    FEMALE = 2


class VoiceTypeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "VTYP"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "VTYP"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="VTYP/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "flags": _base.Binding(
            path="VTYP/1:Flags",
            kind="subrecord",
            name="Flags",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    flags: Optional[AllowDefaultDialogFemale6594] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["flags"]
    ) -> _base.FieldRef[Optional[AllowDefaultDialogFemale6594]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
