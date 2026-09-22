"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base


class Structure8796(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MOVT/2:Default Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "left_walk": _base.Binding(
            path="MOVT/2:Default Data/payload/0:Left Walk",
            kind="primitive",
            name="Left Walk",
        ),
        "left_run": _base.Binding(
            path="MOVT/2:Default Data/payload/1:Left Run",
            kind="primitive",
            name="Left Run",
        ),
        "right_walk": _base.Binding(
            path="MOVT/2:Default Data/payload/2:Right Walk",
            kind="primitive",
            name="Right Walk",
        ),
        "right_run": _base.Binding(
            path="MOVT/2:Default Data/payload/3:Right Run",
            kind="primitive",
            name="Right Run",
        ),
        "forward_walk": _base.Binding(
            path="MOVT/2:Default Data/payload/4:Forward Walk",
            kind="primitive",
            name="Forward Walk",
        ),
        "forward_run": _base.Binding(
            path="MOVT/2:Default Data/payload/5:Forward Run",
            kind="primitive",
            name="Forward Run",
        ),
        "back_walk": _base.Binding(
            path="MOVT/2:Default Data/payload/6:Back Walk",
            kind="primitive",
            name="Back Walk",
        ),
        "back_run": _base.Binding(
            path="MOVT/2:Default Data/payload/7:Back Run",
            kind="primitive",
            name="Back Run",
        ),
        "rotate_in_place_walk": _base.Binding(
            path=("MOVT/2:Default Data/payload/8:Rotate in Place Walk"),
            kind="primitive",
            name="Rotate in Place Walk",
        ),
        "rotate_in_place_run": _base.Binding(
            path="MOVT/2:Default Data/payload/9:Rotate in Place Run",
            kind="primitive",
            name="Rotate in Place Run",
        ),
        "rotate_while_moving_run": _base.Binding(
            path=("MOVT/2:Default Data/payload/10:Rotate while Moving Run"),
            kind="primitive",
            name="Rotate while Moving Run",
        ),
    }

    left_walk: float
    """Value decoded from this schema node."""

    left_run: float
    """Value decoded from this schema node."""

    right_walk: float
    """Value decoded from this schema node."""

    right_run: float
    """Value decoded from this schema node."""

    forward_walk: float
    """Value decoded from this schema node."""

    forward_run: float
    """Value decoded from this schema node."""

    back_walk: float
    """Value decoded from this schema node."""

    back_run: float
    """Value decoded from this schema node."""

    rotate_in_place_walk: float
    """Value decoded from this schema node."""

    rotate_in_place_run: float
    """Value decoded from this schema node."""

    rotate_while_moving_run: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["left_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["left_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["right_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["right_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["forward_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["forward_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["back_walk"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["back_run"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotate_in_place_walk"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotate_in_place_run"]
    ) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rotate_while_moving_run"]
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


class Structure8809(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MOVT/3:Anim Change Thresholds/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "directional": _base.Binding(
            path=("MOVT/3:Anim Change Thresholds/payload/0:Directional"),
            kind="primitive",
            name="Directional",
        ),
        "movement_speed": _base.Binding(
            path=("MOVT/3:Anim Change Thresholds/payload/1:Movement Speed"),
            kind="primitive",
            name="Movement Speed",
        ),
        "rotation_speed": _base.Binding(
            path=("MOVT/3:Anim Change Thresholds/payload/2:Rotation Speed"),
            kind="primitive",
            name="Rotation Speed",
        ),
    }

    directional: float
    """Value decoded from this schema node."""

    movement_speed: float
    """Value decoded from this schema node."""

    rotation_speed: float
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["directional"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["movement_speed"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["rotation_speed"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class MovementTypeRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "MOVT"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "MOVT"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="MOVT/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "name": _base.Binding(
            path="MOVT/1:Name",
            kind="subrecord",
            name="Name",
        ),
        "default_data": _base.Binding(
            path="MOVT/2:Default Data",
            kind="subrecord",
            name="Default Data",
        ),
        "anim_change_thresholds": _base.Binding(
            path="MOVT/3:Anim Change Thresholds",
            kind="subrecord",
            name="Anim Change Thresholds",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    name: Optional[str] = None
    """Value decoded from this schema node."""

    default_data: Optional[Structure8796] = None
    """Value decoded from this schema node."""

    anim_change_thresholds: Optional[Structure8809] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["name"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["default_data"]
    ) -> _base.FieldRef[Optional[Structure8796]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["anim_change_thresholds"]
    ) -> _base.FieldRef[Optional[Structure8809]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
