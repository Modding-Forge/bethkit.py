"""
Copyright (c) Modding Forge
"""

# Generated from the pinned xEdit/Bethkit schema. Do not edit.

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, overload

import pydantic

from .. import _base, _values


class Structure16623(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TES4/0:Header/payload"
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "version": _base.Binding(
            path="TES4/0:Header/payload/0:Version",
            kind="primitive",
            name="Version",
        ),
        "number_of_records": _base.Binding(
            path="TES4/0:Header/payload/1:Number of Records",
            kind="primitive",
            name="Number of Records",
        ),
        "next_object_id": _base.Binding(
            path="TES4/0:Header/payload/2:Next Object ID",
            kind="primitive",
            name="Next Object ID",
        ),
    }

    version: float
    """Value decoded from this schema node."""

    number_of_records: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    next_object_id: Annotated[
        int, pydantic.Field(strict=True, ge=0, le=4294967295)
    ]
    """Value decoded from this schema node."""

    @overload
    def field(self, name: Literal["version"]) -> _base.FieldRef[float]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["number_of_records"]
    ) -> _base.FieldRef[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["next_object_id"]
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


class MasterFile16636(_base.StructModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TES4/5:Master Files/repeat/0:Master File"
    _grammar: ClassVar[bool] = True
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "file_name": _base.Binding(
            path=("TES4/5:Master Files/repeat/0:Master File/0:FileName"),
            kind="subrecord",
            name="FileName",
        ),
        "unknown": _base.Binding(
            path=("TES4/5:Master Files/repeat/0:Master File/1:Unknown"),
            kind="subrecord",
            name="Unknown",
        ),
    }

    file_name: Optional[str] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["file_name"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: str) -> _base.FieldReference:
        """Returns a dynamically selected reference."""

        ...

    def field(self, name: str) -> _base.FieldReference:
        """Returns the snapshot field reference."""

        return super().field(name)


class MainFileHeaderRecord(_base.RecordModel, frozen=True):
    """Schema-generated immutable structural view."""

    _schema_path: ClassVar[str] = "TES4"
    _grammar: ClassVar[bool] = True
    signature: ClassVar[str] = "TES4"
    schema_sha256: ClassVar[str] = (
        "66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7"
    )
    _bindings: ClassVar[dict[str, _base.Binding]] = {
        "header": _base.Binding(
            path="TES4/0:Header",
            kind="subrecord",
            name="Header",
        ),
        "unknown": _base.Binding(
            path="TES4/1:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "unknown_16629": _base.Binding(
            path="TES4/2:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "author": _base.Binding(
            path="TES4/3:Author",
            kind="subrecord",
            name="Author",
        ),
        "description": _base.Binding(
            path="TES4/4:Description",
            kind="subrecord",
            name="Description",
        ),
        "master_files": _base.Binding(
            path="TES4/5:Master Files",
            kind="repeat",
            name="Master Files",
            repeated_path="TES4/5:Master Files/repeat/0:Master File",
            child_kind="sequence",
        ),
        "overridden_forms": _base.Binding(
            path="TES4/6:Overridden Forms",
            kind="subrecord",
            name="Overridden Forms",
        ),
        "screenshot": _base.Binding(
            path="TES4/7:Screenshot",
            kind="subrecord",
            name="Screenshot",
        ),
        "unknown_16646": _base.Binding(
            path="TES4/8:Unknown",
            kind="subrecord",
            name="Unknown",
        ),
        "interior_cell_count": _base.Binding(
            path="TES4/9:Interior Cell Count",
            kind="subrecord",
            name="Interior Cell Count",
        ),
    }

    header: Optional[Structure16623] = None
    """Value decoded from this schema node."""

    unknown: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_16629: Optional[bytes] = None
    """Value decoded from this schema node."""

    author: Optional[str] = None
    """Value decoded from this schema node."""

    description: Optional[str] = None
    """Value decoded from this schema node."""

    master_files: tuple[MasterFile16636, ...] = ()
    """Value decoded from this schema node."""

    overridden_forms: Optional[tuple[_values.FormId, ...]] = None
    """Value decoded from this schema node."""

    screenshot: Optional[bytes] = None
    """Value decoded from this schema node."""

    unknown_16646: Optional[bytes] = None
    """Value decoded from this schema node."""

    interior_cell_count: Optional[
        Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
    ] = None
    """Value decoded from this schema node."""

    @overload
    def field(
        self, name: Literal["header"]
    ) -> _base.FieldRef[Optional[Structure16623]]:
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
        self, name: Literal["unknown_16629"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(self, name: Literal["author"]) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["description"]
    ) -> _base.FieldRef[Optional[str]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["master_files"]
    ) -> _base.FieldRef[tuple[MasterFile16636, ...]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["overridden_forms"]
    ) -> _base.FieldRef[Optional[tuple[_values.FormId, ...]]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["screenshot"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["unknown_16646"]
    ) -> _base.FieldRef[Optional[bytes]]:
        """Returns the typed field reference."""

        ...

    @overload
    def field(
        self, name: Literal["interior_cell_count"]
    ) -> _base.FieldRef[
        Optional[
            Annotated[int, pydantic.Field(strict=True, ge=0, le=4294967295)]
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
