"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base, _values


class FalseTrue7952(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    FALSE = 0
    TRUE = 1


class EquipTypeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "EQUP"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "EQUP"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="EQUP/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "slot_parents": _base.Binding(
            path="EQUP/1:Slot Parents",
            kind="subrecord",
            name="Slot Parents",
        ),
        "use_all_parents": _base.Binding(
            path="EQUP/2:Use All Parents",
            kind="subrecord",
            name="Use All Parents",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    slot_parents: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    use_all_parents: Optional[FalseTrue7952] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["slot_parents"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["use_all_parents"]
    ) -> _base.FieldRef[Optional[FalseTrue7952]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
