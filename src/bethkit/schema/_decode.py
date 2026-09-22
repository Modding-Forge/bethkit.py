"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
from typing import Optional

from .._ffi import BethkitFieldValue
from ..enums import FieldValueKind
from .enum_val import EnumVal
from .field_value import FieldValue
from .flags_val import FlagsVal
from .named_field import NamedField
from .typed_form_id import TypedFormId


def _decode_field_value(raw: BethkitFieldValue, lib: ctypes.CDLL) -> FieldValue:
    """Copies one native tagged field value into compatibility models.

    Args:
        raw: Native field whose backing view remains open during decoding.
        lib: Loaded library supplying borrowed struct and array accessors.

    Returns:
        A copied Python value; nested lists intentionally remain mutable.

    Raises:
        ValueError: The native field kind is unsupported.
        UnicodeDecodeError: Native text is not valid UTF-8.
    """

    kind = FieldValueKind(raw.kind)
    payload = raw.payload
    if kind == FieldValueKind.INT:
        return int(payload.int_val)
    if kind == FieldValueKind.UINT:
        return int(payload.uint_val)
    if kind == FieldValueKind.FLOAT:
        return float(payload.float_val)
    if kind == FieldValueKind.STR:
        encoded: Optional[bytes] = payload.str_val
        return encoded.decode("utf-8") if encoded else ""
    if kind == FieldValueKind.FORM_ID:
        return int(payload.form_id)
    if kind == FieldValueKind.FORM_ID_TYPED:
        form_id = payload.form_id_typed
        signatures: tuple[bytes, ...] = ()
        if form_id.allowed_sigs and form_id.allowed_count:
            pointer = ctypes.cast(
                form_id.allowed_sigs,
                ctypes.POINTER(ctypes.c_uint8 * 4),
            )
            signatures = tuple(
                bytes(pointer[index]) for index in range(form_id.allowed_count)
            )
        return TypedFormId(raw=form_id.raw, allowed_sigs=signatures)
    if kind == FieldValueKind.BYTES:
        value = payload.bytes
        return (
            bytes(ctypes.string_at(value.ptr, value.len)) if value.ptr else b""
        )
    if kind == FieldValueKind.ENUM:
        value = payload.enum_val
        encoded_name: Optional[bytes] = value.name
        return EnumVal(
            value=value.value,
            name=encoded_name.decode("utf-8") if encoded_name else None,
        )
    if kind == FieldValueKind.FLAGS:
        value = payload.flags_val
        names: tuple[str, ...] = ()
        if value.active_names and value.active_count:
            names = tuple(
                value.active_names[index].decode("utf-8")
                for index in range(value.active_count)
                if value.active_names[index]
            )
        return FlagsVal(raw_value=value.raw_value, active_names=names)
    if kind == FieldValueKind.STRUCT:
        return _decode_entries(payload.struct_entries, lib)
    if kind == FieldValueKind.ARRAY:
        return _decode_values(payload.array_values, lib)
    return None


def _decode_entries(pointer: int, lib: ctypes.CDLL) -> list[NamedField]:
    """Copies fields from a borrowed native struct list.

    Args:
        pointer: Borrowed struct-entry list, or zero for an empty list.
        lib: Loaded library exposing native field accessors.

    Returns:
        Named fields copied into a mutable compatibility list.

    Raises:
        ValueError: A nested native field kind is unsupported.
        UnicodeDecodeError: Native text is not valid UTF-8.
    """

    if not pointer:
        return []
    result: list[NamedField] = []
    for index in range(lib.bethkit_field_entries_len(pointer)):
        field_pointer = lib.bethkit_field_entries_get(pointer, index)
        if field_pointer:
            field = field_pointer.contents
            encoded_name: Optional[bytes] = field.name
            result.append(
                NamedField(
                    name=encoded_name.decode("utf-8") if encoded_name else "",
                    value=_decode_field_value(field.value, lib),
                )
            )
    return result


def _decode_values(pointer: int, lib: ctypes.CDLL) -> list[FieldValue]:
    """Copies values from a borrowed native array list.

    Args:
        pointer: Borrowed array-value list, or zero for an empty list.
        lib: Loaded library exposing native array accessors.

    Returns:
        Values copied into a mutable compatibility list.

    Raises:
        ValueError: A nested native field kind is unsupported.
        UnicodeDecodeError: Native text is not valid UTF-8.
    """

    if not pointer:
        return []
    result: list[FieldValue] = []
    for index in range(lib.bethkit_field_values_len(pointer)):
        value_pointer = lib.bethkit_field_values_get(pointer, index)
        if value_pointer:
            result.append(_decode_field_value(value_pointer.contents, lib))
    return result
