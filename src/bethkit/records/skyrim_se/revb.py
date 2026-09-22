"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base


class Structure9109(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REVB/1:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "decay_time_ms": _base.Binding(
            path="REVB/1:Data/payload/0:Decay Time (ms)",
            kind="primitive",
            name="Decay Time (ms)",
        ),
        "hf_reference_hz": _base.Binding(
            path="REVB/1:Data/payload/1:HF Reference (Hz)",
            kind="primitive",
            name="HF Reference (Hz)",
        ),
        "room_filter": _base.Binding(
            path="REVB/1:Data/payload/2:Room Filter",
            kind="primitive",
            name="Room Filter",
        ),
        "room_hf_filter": _base.Binding(
            path="REVB/1:Data/payload/3:Room HF Filter",
            kind="primitive",
            name="Room HF Filter",
        ),
        "reflections": _base.Binding(
            path="REVB/1:Data/payload/4:Reflections",
            kind="primitive",
            name="Reflections",
        ),
        "reverb_amp": _base.Binding(
            path="REVB/1:Data/payload/5:Reverb Amp",
            kind="primitive",
            name="Reverb Amp",
        ),
        "decay_hf_ratio": _base.Binding(
            path="REVB/1:Data/payload/6:Decay HF Ratio",
            kind="primitive",
            name="Decay HF Ratio",
        ),
        "reflect_delay_ms_scaled": _base.Binding(
            path="REVB/1:Data/payload/7:Reflect Delay (ms), scaled",
            kind="primitive",
            name="Reflect Delay (ms), scaled",
        ),
        "reverb_delay_ms": _base.Binding(
            path="REVB/1:Data/payload/8:Reverb Delay (ms)",
            kind="primitive",
            name="Reverb Delay (ms)",
        ),
        "diffusion": _base.Binding(
            path="REVB/1:Data/payload/9:Diffusion %",
            kind="primitive",
            name="Diffusion %",
        ),
        "density": _base.Binding(
            path="REVB/1:Data/payload/10:Density %",
            kind="primitive",
            name="Density %",
        ),
        "unknown": _base.Binding(
            path="REVB/1:Data/payload/11:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    decay_time_ms: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    hf_reference_hz: Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    """Value decoded from this schema node."""

    room_filter: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    room_hf_filter: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    reflections: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    reverb_amp: Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    """Value decoded from this schema node."""

    decay_hf_ratio: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    reflect_delay_ms_scaled: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=255)
    ]
    """Value decoded from this schema node."""

    reverb_delay_ms: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    diffusion: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    density: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    unknown: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["decay_time_ms"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["hf_reference_hz"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=65535)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["room_filter"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["room_hf_filter"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reflections"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reverb_amp"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=-128, le=127)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["decay_hf_ratio"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reflect_delay_ms_scaled"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reverb_delay_ms"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["diffusion"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["density"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
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


class ReverbParametersRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "REVB"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "REVB"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="REVB/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "data": _base.Binding(
            path="REVB/1:Data",
            kind="subrecord",
            name="Data",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    data: Optional[Structure9109] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["data"]
    ) -> _base.FieldRef[Optional[Structure9109]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
