"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict

from .. import _ffi
from .._error import BethkitClosedError
from .._ffi import BethkitFieldValue
from ..enums import FieldValueKind


class TypedFormId(BaseModel, frozen=True):
    """
    A FormID together with the set of record-type signatures it may
    reference.
    """

    raw: int
    """Raw 32-bit FormID."""

    allowed_sigs: tuple[bytes, ...]
    """Permitted target record-type signatures."""


class EnumVal(BaseModel, frozen=True):
    """
    A decoded enumeration field value.
    """

    value: int
    """Underlying integer value."""

    name: Optional[str]
    """Human-readable name, or ``None`` if unknown."""


class FlagsVal(BaseModel, frozen=True):
    """
    A decoded bit-flags field value.
    """

    raw_value: int
    """Full raw flags integer."""

    active_names: tuple[str, ...]
    """Names of all currently set bits."""


FieldValue = (
    int
    | float
    | str
    | bytes
    | TypedFormId
    | EnumVal
    | FlagsVal
    | list[Any]  # struct fields: list[NamedField]; array fields: list[FieldValue]
    | None
)
"""
Union of all possible decoded field value types.

Simple types (``int``, ``float``, ``str``, ``bytes``, ``None``) are
returned as-is.  Complex types use :class:`TypedFormId`,
:class:`EnumVal`, or :class:`FlagsVal`.  Struct fields produce
``list[NamedField]``; array fields produce ``list[FieldValue]``.
"""


class NamedField(BaseModel):
    """
    A single named field inside a struct or record view.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    """Schema-defined field name."""

    value: FieldValue
    """Decoded value for this field."""


NamedField.model_rebuild()


def _decode_field_value(raw: BethkitFieldValue, lib: ctypes.CDLL) -> FieldValue:
    """
    Decode a ctypes ``BethkitFieldValue`` into a Python :data:`FieldValue`.

    Args:
        raw: The ctypes ``BethkitFieldValue`` struct instance.
        lib (ctypes.CDLL): Loaded bethkit native library handle.

    Returns:
        FieldValue: The decoded Python value.
    """

    kind = FieldValueKind(raw.kind)
    p = raw.payload

    if kind == FieldValueKind.INT:
        return p.int_val

    if kind == FieldValueKind.FLOAT:
        return p.float_val

    if kind == FieldValueKind.STR:
        s: Optional[bytes] = p.str_val
        return s.decode("utf-8") if s else ""

    if kind == FieldValueKind.FORM_ID:
        return p.form_id

    if kind == FieldValueKind.FORM_ID_TYPED:
        fid = p.form_id_typed
        sigs: tuple[bytes, ...] = ()
        if fid.allowed_sigs and fid.allowed_count:
            raw_ptr = ctypes.cast(
                fid.allowed_sigs, ctypes.POINTER(ctypes.c_uint8 * 4)
            )
            sigs = tuple(
                bytes(raw_ptr[i]) for i in range(fid.allowed_count)
            )
        return TypedFormId(raw=fid.raw, allowed_sigs=sigs)

    if kind == FieldValueKind.BYTES:
        sl = p.bytes
        if not sl.ptr:
            return b""
        return bytes(ctypes.string_at(sl.ptr, sl.len))

    if kind == FieldValueKind.ENUM:
        ev = p.enum_val
        name_raw: Optional[bytes] = ev.name
        return EnumVal(
            value=ev.value,
            name=name_raw.decode("utf-8") if name_raw else None,
        )

    if kind == FieldValueKind.FLAGS:
        fv = p.flags_val
        names: tuple[str, ...] = ()
        if fv.active_names and fv.active_count:
            names = tuple(
                fv.active_names[i].decode("utf-8")
                for i in range(fv.active_count)
                if fv.active_names[i]
            )
        return FlagsVal(raw_value=fv.raw_value, active_names=names)

    if kind == FieldValueKind.STRUCT:
        entries_ptr = p.struct_entries
        if not entries_ptr:
            return []
        return _decode_entries(entries_ptr, lib)

    if kind == FieldValueKind.ARRAY:
        values_ptr = p.array_values
        if not values_ptr:
            return []
        return _decode_values(values_ptr, lib)

    if kind == FieldValueKind.LOCALIZED_ID:
        return p.localized_id

    return None


def _decode_entries(
    entries_ptr: int, lib: ctypes.CDLL
) -> list[NamedField]:
    """
    Convert a native ``BethkitFieldEntries*`` to a list of
    :class:`NamedField`.

    Args:
        entries_ptr (int): Native pointer to the field-entries object.
        lib (ctypes.CDLL): Loaded bethkit native library handle.

    Returns:
        list[NamedField]: Decoded list of named fields.
    """

    n = lib.bethkit_field_entries_len(entries_ptr)
    result: list[NamedField] = []
    for i in range(n):
        nf_ptr = lib.bethkit_field_entries_get(entries_ptr, i)
        if not nf_ptr:
            continue
        nf = nf_ptr.contents
        name_raw: Optional[bytes] = nf.name
        name = name_raw.decode("utf-8") if name_raw else ""
        value = _decode_field_value(nf.value, lib)
        result.append(NamedField(name=name, value=value))
    return result


def _decode_values(
    values_ptr: int, lib: ctypes.CDLL
) -> list[FieldValue]:
    """
    Convert a native ``BethkitFieldValues*`` to a list of
    :data:`FieldValue`.

    Args:
        values_ptr (int): Native pointer to the field-values object.
        lib (ctypes.CDLL): Loaded bethkit native library handle.

    Returns:
        list[FieldValue]: Decoded list of field values.
    """

    n = lib.bethkit_field_values_len(values_ptr)
    result: list[FieldValue] = []
    for i in range(n):
        fv_ptr = lib.bethkit_field_values_get(values_ptr, i)
        if not fv_ptr:
            continue
        result.append(_decode_field_value(fv_ptr.contents, lib))
    return result


class SchemaRegistry:
    """
    A registry that maps record signatures to their field schemas.

    Obtain a pre-built registry for a specific game with the class
    methods (e.g. :meth:`sse`), then use :meth:`has` to check whether a
    given record type is known.

    This is a **borrowed** handle: the native memory is owned by the
    library and must not be freed.
    """

    _ptr: int

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI factory call.
        """

        self._ptr = ptr

    @classmethod
    def sse(cls) -> SchemaRegistry:
        """
        Load the built-in Skyrim Special Edition schema registry.

        Returns:
            SchemaRegistry: The SSE registry (borrowed, never freed).

        Raises:
            BethkitNativeError: If the registry cannot be loaded.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_schema_registry_sse()
        if not ptr:
            _ffi.raise_last_error(lib)
        return cls(ptr)

    def has(self, sig: bytes | str) -> bool:
        """
        Check whether the registry contains a schema for *sig*.

        Args:
            sig (bytes | str): Four-byte record-type signature to look up.

        Returns:
            bool: ``True`` if the signature is known.

        Raises:
            ValueError: If *sig* is not exactly 4 bytes.
        """

        if isinstance(sig, str):
            sig = sig.encode("ascii")
        if len(sig) != 4:
            raise ValueError("sig must be exactly 4 bytes")
        buf = (ctypes.c_uint8 * 4)(*sig)
        return bool(
            _ffi.load_lib().bethkit_schema_registry_has(self._ptr, buf)
        )

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation of the registry.
        """

        return "<SchemaRegistry>"


class RecordView:
    """
    A decoded, schema-aware view of a plugin record.

    Create a view with :meth:`new`, specifying the record and its type
    signature.  Use :meth:`fields` to retrieve all decoded fields.

    Use as a context manager to guarantee the native handle is freed::

        with RecordView.new(record, b"NPC_") as view:
            for field in view.fields():
                print(field.name, field.value)
    """

    __ptr: int
    _fields_cache: Optional[list[NamedField]]

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI new call.
        """

        self.__ptr = ptr
        self._fields_cache = None

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle is already closed.

        Returns:
            int: Non-zero native pointer.

        Raises:
            BethkitClosedError: If :meth:`close` has already been called.
        """

        if not self.__ptr:
            raise BethkitClosedError("RecordView has already been closed.")
        return self.__ptr

    @classmethod
    def new(
        cls,
        record: object,
        sig: bytes | str,
        *,
        localized: bool = False,
    ) -> RecordView:
        """
        Create a schema-decoded view of *record*.

        Args:
            record: An open :class:`~bethkit.Record` instance.
            sig (bytes | str): Four-byte record-type signature used to
                select the correct schema.
            localized (bool): Whether to interpret string fields as
                localisation IDs rather than inline strings. Defaults
                to ``False``.

        Returns:
            RecordView: The decoded view.

        Raises:
            BethkitNativeError: If decoding fails.
            BethkitClosedError: If *record* has already been closed.
            ValueError: If *sig* is not exactly 4 bytes.
        """

        if isinstance(sig, str):
            sig = sig.encode("ascii")
        if len(sig) != 4:
            raise ValueError("sig must be exactly 4 bytes")
        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * 4)(*sig)
        rec_ptr: int = getattr(record, "_ptr", 0)
        if not rec_ptr:
            raise BethkitClosedError(
                "Record is closed or has no native pointer."
            )
        ptr = lib.bethkit_record_view_new(rec_ptr, buf, localized)
        if not ptr:
            _ffi.raise_last_error(lib)
        return cls(ptr)

    def close(self) -> None:
        """
        Release the native view handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_record_view_free(self.__ptr)
            self.__ptr = 0
            self._fields_cache = None

    def __enter__(self) -> RecordView:
        """
        Return *self* for use as a context manager.

        Returns:
            RecordView: This instance.
        """

        return self

    def __exit__(self, *_: object) -> None:
        """Free the view when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def field_count(self) -> int:
        """
        Return the number of decoded top-level fields in this view.

        Returns:
            int: Field count.

        Raises:
            BethkitClosedError: If this view has already been closed.
        """

        return _ffi.load_lib().bethkit_record_view_field_count(
            self.__check_open()
        )

    def fields(self) -> list[NamedField]:
        """
        Return all top-level decoded fields, cached after the first call.

        Returns:
            list[NamedField]: Ordered list of named fields.

        Raises:
            BethkitClosedError: If this view has already been closed.
        """

        ptr = self.__check_open()
        if self._fields_cache is None:
            lib = _ffi.load_lib()
            n = lib.bethkit_record_view_field_count(ptr)
            result: list[NamedField] = []
            for i in range(n):
                nf_ptr = lib.bethkit_record_view_field_get(ptr, i)
                if not nf_ptr:
                    continue
                nf = nf_ptr.contents
                name_raw: Optional[bytes] = nf.name
                name = name_raw.decode("utf-8") if name_raw else ""
                value = _decode_field_value(nf.value, lib)
                result.append(NamedField(name=name, value=value))
            self._fields_cache = result
        return self._fields_cache

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with field count.
        """

        if not self.__ptr:
            return "<RecordView closed>"
        return f"<RecordView fields={self.field_count()}>"
