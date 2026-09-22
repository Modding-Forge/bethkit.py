"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure7171(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FSTS/1:Count/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "walk_forward_sets": _base.Binding(
            path="FSTS/1:Count/payload/0:Walk Forward Sets",
            kind="primitive",
            name="Walk Forward Sets",
        ),
        "run_forward_sets": _base.Binding(
            path="FSTS/1:Count/payload/1:Run Forward Sets",
            kind="primitive",
            name="Run Forward Sets",
        ),
        "walk_forward_alternate_sets": _base.Binding(
            path=("FSTS/1:Count/payload/2:Walk Forward Alternate Sets"),
            kind="primitive",
            name="Walk Forward Alternate Sets",
        ),
        "run_forward_alternate_sets": _base.Binding(
            path="FSTS/1:Count/payload/3:Run Forward Alternate Sets",
            kind="primitive",
            name="Run Forward Alternate Sets",
        ),
        "walk_forward_alternate_2_sets": _base.Binding(
            path=("FSTS/1:Count/payload/4:Walk Forward Alternate 2 Sets"),
            kind="primitive",
            name="Walk Forward Alternate 2 Sets",
        ),
    }

    walk_forward_sets: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    run_forward_sets: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    walk_forward_alternate_sets: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    run_forward_alternate_sets: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    walk_forward_alternate_2_sets: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["walk_forward_sets"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["run_forward_sets"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["walk_forward_alternate_sets"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["run_forward_alternate_sets"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["walk_forward_alternate_2_sets"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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


class FootstepSetRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "FSTS"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "FSTS"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "editor_id": _base.Binding(
            path="FSTS/0:Editor ID",
            kind="subrecord",
            name="Editor ID",
        ),
        "count": _base.Binding(
            path="FSTS/1:Count",
            kind="subrecord",
            name="Count",
        ),
        "footstep_sets": _base.Binding(
            path="FSTS/2:Footstep Sets",
            kind="subrecord",
            name="Footstep Sets",
        ),
    }

    editor_id: Optional[str] = None
    """Value decoded from this schema node."""

    count: Optional[Structure7171] = None
    """Value decoded from this schema node."""

    footstep_sets: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["editor_id"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["count"]
    ) -> _base.FieldRef[Optional[Structure7171]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["footstep_sets"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)
