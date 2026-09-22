"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes

from .. import _ffi
from .._error import UnsupportedEditError
from ..records import _base, _wire


def set_legacy(
    pointer: int, path: object, value: object, occurrence: int
) -> None:
    """Validates and sets a scalar through the compatibility path API.

    Args:
        pointer: Live editor whose lifetime was checked by its owner.
        path: Schema path, which may have several occurrences in a record.
        value: Scalar replacement within the native type's numeric range.
        occurrence: Zero-based occurrence across that schema path.

    Raises:
        TypeError: The path or value has an unsupported Python type.
        ValueError: The integer value or occurrence is out of range.
        BethkitNativeError: The native schema rejected the replacement.
    """

    if not isinstance(path, str):
        raise TypeError("Use a generated FieldRef or a schema path string.")
    if occurrence < 0:
        raise ValueError("An occurrence must be nonnegative.")
    if isinstance(value, bool) or not isinstance(
        value, (int, float, str, bytes)
    ):
        raise TypeError(
            "A legacy edit requires an integer, float, string, or bytes."
        )
    if isinstance(value, int) and not -(1 << 63) <= value < (1 << 64):
        raise ValueError("An integer must fit a native 64-bit value.")
    lib = _ffi.load_lib()

    encoded_path = _ffi.senc(path)
    if isinstance(value, bytes):
        data = (ctypes.c_uint8 * len(value)).from_buffer_copy(value)
        result = lib.bethkit_record_editor_set_bytes(
            pointer,
            encoded_path,
            occurrence,
            data,
            len(value),
        )
    elif isinstance(value, str):
        result = lib.bethkit_record_editor_set_string(
            pointer,
            encoded_path,
            occurrence,
            _ffi.senc(value),
        )
    elif isinstance(value, float):
        result = lib.bethkit_record_editor_set_f64(
            pointer,
            encoded_path,
            occurrence,
            value,
        )
    elif value < 0:
        result = lib.bethkit_record_editor_set_i64(
            pointer,
            encoded_path,
            occurrence,
            value,
        )
    else:
        result = lib.bethkit_record_editor_set_u64(
            pointer,
            encoded_path,
            occurrence,
            value,
        )
    if result != 0:
        _ffi.raise_last_error(lib)


def set_form_id(pointer: int, path: str, value: int, occurrence: int) -> None:
    """Validates and sets a legacy FormID occurrence.

    Args:
        pointer: Live editor whose lifetime was checked by its owner.
        path: Schema path to a FormID field.
        value: File-local unsigned 32-bit record identity.
        occurrence: Zero-based occurrence of the path.

    Raises:
        ValueError: The FormID or occurrence is out of range.
        BethkitNativeError: The native schema rejected the replacement.
    """

    if isinstance(value, bool) or not 0 <= value <= 0xFFFFFFFF:
        raise ValueError("A FormID must fit an unsigned 32-bit integer.")
    if occurrence < 0:
        raise ValueError("An occurrence must be nonnegative.")
    lib = _ffi.load_lib()
    result = lib.bethkit_record_editor_set_form_id(
        pointer,
        _ffi.senc(path),
        occurrence,
        value,
    )
    if result != 0:
        _ffi.raise_last_error(lib)


def remove(
    pointer: int,
    path: str | _wire.FieldAddress | _base.FieldReference,
    occurrence: int,
) -> None:
    """Removes one legacy occurrence or one precisely addressed value.

    Args:
        pointer: Live editor whose lifetime was checked by its owner.
        path: Schema path, generated field reference, or structural address.
        occurrence: Legacy path occurrence; must be zero for exact addresses.

    Raises:
        ValueError: The occurrence is negative or conflicts with an address.
        UnsupportedEditError: The address or removal violates the schema.
        BethkitNativeError: A legacy path operation failed native validation.
    """

    if occurrence < 0:
        raise ValueError("An occurrence must be nonnegative.")
    lib = _ffi.load_lib()
    if isinstance(path, _base.FieldReference):
        if path.address is None:
            raise UnsupportedEditError(
                "Select an individual field within the group."
            )
        path = path.address
    if isinstance(path, _wire.FieldAddress):
        if occurrence:
            raise ValueError(
                "An addressed field already identifies its occurrence."
            )
        result = lib.bethkit_record_editor_remove_at_json(
            pointer,
            _ffi.senc(path.model_dump_json()),
        )
        if result != 0:
            raise UnsupportedEditError(_ffi.last_error(lib))
        return
    result = lib.bethkit_record_editor_remove(
        pointer,
        _ffi.senc(path),
        occurrence,
    )
    if result != 0:
        _ffi.raise_last_error(lib)
