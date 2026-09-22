"""
Copyright (c) Modding Forge

Generated from the pinned xEdit/Bethkit schema. Do not edit.
"""

from __future__ import annotations

import enum
from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Flags9039(enum.IntFlag):
    """Named values from the pinned schema."""

    ATTENUATES_WITH_DISTANCE = 1
    ALLOWS_RUMBLE = 2


class Structure9038(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SOPM/1:Data/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "flags": _base.Binding(
            path="SOPM/1:Data/payload/0:Flags",
            kind="primitive",
            name="Flags",
        ),
        "unknown": _base.Binding(
            path="SOPM/1:Data/payload/1:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "reverb_send": _base.Binding(
            path="SOPM/1:Data/payload/2:Reverb Send %",
            kind="primitive",
            name="Reverb Send %",
        ),
    }

    flags: Flags9039
    """Value decoded from this schema node."""

    unknown: bytes
    """Value decoded from this schema node."""

    reverb_send: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["flags"]) -> _base.FieldRef[Flags9039]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["reverb_send"]
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


class UsesHrtfDefinedSpeakerOutput9045(_values.OpenIntEnum):
    """Named values from the pinned schema."""

    USES_HRTF = 0
    DEFINED_SPEAKER_OUTPUT = 1


class Structure9053(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = (
        "SOPM/6:Output Values/payload/0:Channels/element"
    )
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "l_value": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/0:L"),
            kind="primitive",
            name="L",
        ),
        "r": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/1:R"),
            kind="primitive",
            name="R",
        ),
        "c": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/2:C"),
            kind="primitive",
            name="C",
        ),
        "lfe": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/3:LFE"),
            kind="primitive",
            name="LFE",
        ),
        "rl": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/4:RL"),
            kind="primitive",
            name="RL",
        ),
        "rr": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/5:RR"),
            kind="primitive",
            name="RR",
        ),
        "bl": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/6:BL"),
            kind="primitive",
            name="BL",
        ),
        "br": _base.Binding(
            path=("SOPM/6:Output Values/payload/0:Channels/element/7:BR"),
            kind="primitive",
            name="BR",
        ),
    }

    l_value: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    r: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    c: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    lfe: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    rl: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    rr: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    bl: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    br: Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["l_value"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["r"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["c"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["lfe"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rl"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["rr"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["bl"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=255)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["br"]
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


class Structure9051(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SOPM/6:Output Values/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "channels": _base.Binding(
            path="SOPM/6:Output Values/payload/0:Channels",
            kind="array",
            name="Channels",
        ),
    }

    channels: tuple[Structure9053, ...]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["channels"]
    ) -> _base.FieldRef[tuple[Structure9053, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class Structure9063(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SOPM/7:Attenuation Values/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "unknown": _base.Binding(
            path="SOPM/7:Attenuation Values/payload/0:Unknown",
            kind="primitive",
            name="Unknown",
        ),
        "min_distance": _base.Binding(
            path="SOPM/7:Attenuation Values/payload/1:Min Distance",
            kind="primitive",
            name="Min Distance",
        ),
        "max_distance": _base.Binding(
            path="SOPM/7:Attenuation Values/payload/2:Max Distance",
            kind="primitive",
            name="Max Distance",
        ),
        "curve": _base.Binding(
            path="SOPM/7:Attenuation Values/payload/3:Curve",
            kind="array",
            name="Curve",
        ),
        "unknown_9069": _base.Binding(
            path="SOPM/7:Attenuation Values/payload/4:Unknown",
            kind="primitive",
            name="Unknown",
        ),
    }

    unknown: bytes
    """Value decoded from this schema node."""

    min_distance: float
    """Value decoded from this schema node."""

    max_distance: float
    """Value decoded from this schema node."""

    curve: tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    """Value decoded from this schema node."""

    unknown_9069: bytes
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["unknown"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["min_distance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["max_distance"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["curve"]
    ) -> _base.FieldRef[
        tuple[Annotated[int, pydantic.Field(strict=True, ge=0, le=255)], ...]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["unknown_9069"]) -> _base.FieldRef[bytes]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class SoundOutputModelRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "SOPM"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "SOPM"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="SOPM/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "data": _base.Binding(
            path="SOPM/1:Data",
            kind="subrecord",
            name="Data",
        ),
        "unknown": _base.Binding(
            path="SOPM/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "type": _base.Binding(
            path="SOPM/3:Type",
            kind="subrecord",
            name="Type",
        ),
        "unknown_9046": _base.Binding(
            path="SOPM/4:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_9048": _base.Binding(
            path="SOPM/5:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "output_values": _base.Binding(
            path="SOPM/6:Output Values",
            kind="subrecord",
            name="Output Values",
        ),
        "attenuation_values": _base.Binding(
            path="SOPM/7:Attenuation Values",
            kind="subrecord",
            name="Attenuation Values",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    data: Optional[Structure9038] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    type: Optional[UsesHrtfDefinedSpeakerOutput9045] = None
    """Value decoded from this schema node."""

    unknown_9046: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_9048: Optional[bytes] = None
    """Value decoded from this schema node."""

    output_values: Optional[Structure9051] = None
    """Value decoded from this schema node."""

    attenuation_values: Optional[Structure9063] = None
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
    ) -> _base.FieldRef[Optional[Structure9038]]:
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
        self, name: Literal["type"]
    ) -> _base.FieldRef[Optional[UsesHrtfDefinedSpeakerOutput9045]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_9046"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_9048"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["output_values"]
    ) -> _base.FieldRef[Optional[Structure9051]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["attenuation_values"]
    ) -> _base.FieldRef[Optional[Structure9063]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
