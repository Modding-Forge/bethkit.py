"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import ClassVar, Optional, Protocol, TypeVar, cast

import pydantic

from .._error import RecordDecodeError, SchemaMismatchError
from . import _materialize, _wire
from ._struct_model import StructModel

_Model = TypeVar("_Model", bound="RecordModel")


class RecordModel(StructModel, frozen=True):
    """Base of schema-pinned, lazily materialized record snapshots."""

    signature: ClassVar[str] = ""
    schema_sha256: ClassVar[str] = ""
    _snapshot: Optional[_wire.RecordSnapshot] = pydantic.PrivateAttr(
        default=None
    )

    @classmethod
    def from_snapshot(
        cls: type[_Model], snapshot: _wire.RecordSnapshot
    ) -> _Model:
        """Materializes this record type from one native-owned snapshot.

        Args:
            snapshot: Complete native semantic snapshot of one record.

        Returns:
            A typed view independent of the source plugin's lifetime.

        Raises:
            SchemaMismatchError: Signature or exact schema identity differs.
            RecordDecodeError: Native values do not match the generated model.
        """

        if snapshot.record_signature != cls.signature:
            raise SchemaMismatchError(
                f"Expected {cls.signature}, "
                f"received {snapshot.record_signature}."
            )
        if snapshot.projection != "full":
            raise RecordDecodeError(
                "Typed models require a full record snapshot."
            )
        if snapshot.schema_payload_sha256 != cls.schema_sha256:
            raise SchemaMismatchError(
                "Generated models and loaded schema differ."
            )
        try:
            model = cast(
                _Model, _materialize.grammar_model(cls, snapshot.fields)
            )
        except (ValueError, TypeError, KeyError) as exc:
            raise RecordDecodeError(
                f"Cannot decode {cls.signature}: {exc}"
            ) from exc
        _materialize.set_private(model, "_snapshot", snapshot)
        return model

    @classmethod
    def from_record(
        cls: type[_Model],
        record: _RecordHandle,
        context: _SnapshotContext,
        *,
        localized: bool = False,
    ) -> _Model:
        """Decodes only the requested record through its native context.

        Args:
            record: Borrowed source record whose plugin is still open.
            context: Semantic runtime using the matching schema package.
            localized: Whether the source plugin uses external string tables.

        Returns:
            An independently owned immutable model.

        Raises:
            SchemaMismatchError: The generated and loaded schemas differ.
            RecordDecodeError: Values cannot be represented by this model.
            BethkitClosedError: The record owner or context has been closed.
            BethkitNativeError: The native runtime cannot decode the record.
        """

        return cls.from_snapshot(context.snapshot(record, localized=localized))


class _RecordHandle(Protocol):
    """A private lifetime-checked borrowed record contract."""

    def _native_pointer(self) -> int:
        """Checks the complete owner chain and returns a borrowed pointer."""

        ...


class _SnapshotContext(Protocol):
    """Native snapshot service without a runtime import cycle."""

    def snapshot(
        self,
        record: _RecordHandle,
        *,
        localized: bool = False,
    ) -> _wire.RecordSnapshot:
        """Copies one record into a validated, independently owned snapshot."""

        ...
