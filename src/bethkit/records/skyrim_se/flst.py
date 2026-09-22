"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class FormIdListRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FLST"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "FLST"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="FLST/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "form_ids": _base.Binding(
            path="FLST/1:FormIDs",
            kind="repeat",
            name="FormIDs",
            repeated_path="FLST/1:FormIDs/repeat/0:FormID",
            child_kind="subrecord",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    form_ids: tuple[_values.FormId, ...] = ()
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["form_ids"]
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
