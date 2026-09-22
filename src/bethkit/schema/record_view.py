"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, ClassVar, Optional

from .. import _ffi
from .._error import BethkitClosedError
from .._ownership import finalize
from ._adoption import adopt_native
from ._decode import _decode_field_value
from ._record_handle import RecordHandle
from .named_field import NamedField

if TYPE_CHECKING:
    from .semantic_context import SemanticContext


class RecordView:
    """Owned semantic snapshot of one plugin record."""

    log: ClassVar[logging.Logger] = logging.getLogger("RecordView")
    __pointer: int = 0
    __fields: Optional[tuple[NamedField, ...]]

    def __init__(self) -> None:
        """Rejects direct construction; use the documented native factories.

        Raises:
            TypeError: Native ownership can only originate from a factory.
        """

        raise TypeError("Use RecordView factory methods instead.")

    @classmethod
    def _from_native(cls, pointer: int) -> RecordView:
        """Adopts a non-null allocation returned by a trusted native factory.

        Args:
            pointer: Newly allocated native handle transferred to this wrapper.

        Returns:
            A wrapper owning the native allocation.

        Raises:
            ValueError: The pointer is null.
        """

        if not pointer:
            raise ValueError("A native factory returned a null handle.")
        instance = cls.__new__(cls)
        instance.__fields = None
        instance.__pointer = pointer
        return instance

    @classmethod
    def new(
        cls,
        context: SemanticContext,
        record: RecordHandle,
        *,
        localized: bool = False,
    ) -> RecordView:
        """Decodes a record into an independently owned generic view.

        Args:
            context: Open semantic runtime used for schema decoding.
            record: Source record whose owner remains open during this call.
            localized: Whether the source plugin uses external string tables.

        Returns:
            A view retaining its own native snapshot after source handles close.

        Raises:
            BethkitClosedError: The runtime or source record owner is closed.
            BethkitNativeError: The schema cannot decode the source record.
        """

        lib = _ffi.load_lib()
        pointer = lib.bethkit_record_view_new(
            context._native_pointer(),
            record._native_pointer(),
            localized,
        )
        if not pointer:
            _ffi.raise_last_error(lib)
        return adopt_native(
            pointer, cls._from_native, lib.bethkit_record_view_free
        )

    def __check_open(self) -> int:
        """Checks snapshot lifetime before borrowing its private pointer.

        Returns:
            The live pointer, still owned by this view.

        Raises:
            BethkitClosedError: The view has already been closed.
        """

        if not self.__pointer:
            raise BethkitClosedError("RecordView has already been closed.")
        return self.__pointer

    def fields(self) -> tuple[NamedField, ...]:
        """Returns cached fields with frozen attributes, not deep immutability.

        Returns:
            A tuple of NamedField values copied out of native memory. Nested
            lists remain mutable for compatibility; callers needing deeply
            immutable typed values should use generated record models instead.

        Raises:
            BethkitClosedError: The view has already been closed.
            UnicodeDecodeError: Native text is not valid UTF-8.
            ValueError: The native field kind is unsupported.
        """

        pointer = self.__check_open()
        if self.__fields is None:
            lib = _ffi.load_lib()
            result: list[NamedField] = []
            for index in range(lib.bethkit_record_view_field_count(pointer)):
                field_pointer = lib.bethkit_record_view_field_get(
                    pointer, index
                )
                if field_pointer:
                    field = field_pointer.contents
                    encoded_name: Optional[bytes] = field.name
                    result.append(
                        NamedField(
                            name=(
                                encoded_name.decode("utf-8")
                                if encoded_name
                                else ""
                            ),
                            value=_decode_field_value(field.value, lib),
                        )
                    )
            self.__fields = tuple(result)
        return self.__fields

    def field_count(self) -> int:
        """Returns the number of decoded top-level fields.

        Returns:
            The field count, including repeated top-level values.

        Raises:
            BethkitClosedError: The view has already been closed.
        """

        return int(
            _ffi.load_lib().bethkit_record_view_field_count(self.__check_open())
        )

    def close(self) -> None:
        """Releases the native view; repeated calls are safe no-ops."""

        if self.__pointer:
            lib = _ffi.load_lib()
            pointer = self.__pointer
            self.__pointer = 0
            self.__fields = None
            lib.bethkit_record_view_free(pointer)

    def __enter__(self) -> RecordView:
        """Returns this open view for scoped resource management.

        Returns:
            This view, closed automatically on context exit.

        Raises:
            BethkitClosedError: The view has already been closed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Closes this snapshot when leaving its context.

        Args:
            *_: Exception context supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Releases any remaining owned snapshot during finalization."""

        finalize(self.close, self.log)
