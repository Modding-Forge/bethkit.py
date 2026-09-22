"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import ClassVar, Literal, Optional, overload

from .. import _base


class Colors18300(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "VOLI/3:Colors"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "red": _base.Binding(
            path="VOLI/3:Colors/0:Red",
            kind="subrecord",
            name="Red",
        ),
        "green": _base.Binding(
            path="VOLI/3:Colors/1:Green",
            kind="subrecord",
            name="Green",
        ),
        "blue": _base.Binding(
            path="VOLI/3:Colors/2:Blue",
            kind="subrecord",
            name="Blue",
        ),
    }

    red: Optional[float] = None
    """Value decoded from this schema node."""

    green: Optional[float] = None
    """Value decoded from this schema node."""

    blue: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["red"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["green"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["blue"]) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class VolumetricLightingRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "VOLI"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "VOLI"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="VOLI/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "intensity": _base.Binding(
            path="VOLI/1:Intensity",
            kind="subrecord",
            name="Intensity",
        ),
        "custom_color_contribution": _base.Binding(
            path="VOLI/2:Custom Color - Contribution",
            kind="subrecord",
            name="Custom Color - Contribution",
        ),
        "colors": _base.Binding(
            path="VOLI/3:Colors",
            kind="sequence",
            name="Colors",
        ),
        "density_contribution": _base.Binding(
            path="VOLI/4:Density - Contribution",
            kind="subrecord",
            name="Density - Contribution",
        ),
        "density_size": _base.Binding(
            path="VOLI/5:Density - Size",
            kind="subrecord",
            name="Density - Size",
        ),
        "density_wind_speed": _base.Binding(
            path="VOLI/6:Density - Wind Speed",
            kind="subrecord",
            name="Density - Wind Speed",
        ),
        "density_falling_speed": _base.Binding(
            path="VOLI/7:Density - Falling Speed",
            kind="subrecord",
            name="Density - Falling Speed",
        ),
        "phase_function_contribution": _base.Binding(
            path="VOLI/8:Phase Function - Contribution",
            kind="subrecord",
            name="Phase Function - Contribution",
        ),
        "phase_function_scattering": _base.Binding(
            path="VOLI/9:Phase Function - Scattering",
            kind="subrecord",
            name="Phase Function - Scattering",
        ),
        "sampling_repartition_range_factor": _base.Binding(
            path="VOLI/10:Sampling Repartition - Range Factor",
            kind="subrecord",
            name="Sampling Repartition - Range Factor",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    intensity: Optional[float] = None
    """Value decoded from this schema node."""

    custom_color_contribution: Optional[float] = None
    """Value decoded from this schema node."""

    colors: Optional[Colors18300] = None
    """Value decoded from this schema node."""

    density_contribution: Optional[float] = None
    """Value decoded from this schema node."""

    density_size: Optional[float] = None
    """Value decoded from this schema node."""

    density_wind_speed: Optional[float] = None
    """Value decoded from this schema node."""

    density_falling_speed: Optional[float] = None
    """Value decoded from this schema node."""

    phase_function_contribution: Optional[float] = None
    """Value decoded from this schema node."""

    phase_function_scattering: Optional[float] = None
    """Value decoded from this schema node."""

    sampling_repartition_range_factor: Optional[float] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["intensity"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["custom_color_contribution"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["colors"]
    ) -> _base.FieldRef[Optional[Colors18300]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["density_contribution"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["density_size"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["density_wind_speed"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["density_falling_speed"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["phase_function_contribution"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["phase_function_scattering"]
    ) -> _base.FieldRef[Optional[float]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["sampling_repartition_range_factor"]
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
