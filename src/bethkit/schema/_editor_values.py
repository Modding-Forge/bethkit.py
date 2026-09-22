"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import json

import pydantic

from .. import _ffi
from .._error import RecordDecodeError, UnsupportedEditError
from ..records import _base, _encoding, _values, _wire

InsertValue = (
    _wire.WireValue
    | int
    | float
    | str
    | bytes
    | _base.StructModel
    | _values.FormId
)
"""Accepted payloads for an optional subrecord insertion."""


def snapshot(
    pointer: int, *, strings_only: bool = False
) -> _wire.RecordSnapshot:
    """Copies a semantic snapshot out of a live editor.

    Args:
        pointer: Editor pointer checked by its Python owner.
        strings_only: Omit values that are not translatable text.

    Returns:
        An independent snapshot with current structural addresses.

    Raises:
        RecordDecodeError: The native decoder rejected the record.
        pydantic.ValidationError: Native JSON violates the snapshot model.
    """

    lib = _ffi.load_lib()
    function = (
        lib.bethkit_record_editor_strings_snapshot_json
        if strings_only
        else lib.bethkit_record_editor_snapshot_json
    )
    result = function(pointer)
    if not result:
        raise RecordDecodeError(_ffi.last_error(lib))
    text = _ffi.copy_and_free_str(result, lib.bethkit_string_free, lib)
    return _wire.RecordSnapshot.model_validate_json(text)


def insert(pointer: int, path: str, value: InsertValue) -> None:
    """Encodes an insertion without interpreting the native record grammar.

    Args:
        pointer: Editor pointer checked by its Python owner.
        path: Exact schema path to the optional subrecord.
        value: Scalar or structured replacement payload.

    Raises:
        UnsupportedEditError: The value or insertion is unsupported.
        TypeError: The replacement contains an unsupported Python value.
        ValueError: A floating-point value cannot be represented in JSON.
    """

    encoded = (
        value.model_dump(mode="json", exclude_none=True)
        if isinstance(
            value, (_wire.WireScalar, _wire.WireStruct, _wire.WireArray)
        )
        else _encoding._encode(value)
    )
    lib = _ffi.load_lib()
    result = lib.bethkit_record_editor_insert_json(
        pointer,
        _ffi.senc(path),
        _ffi.senc(json.dumps(encoded, allow_nan=False)),
    )
    if result != 0:
        raise UnsupportedEditError(_ffi.last_error(lib))


def set_json(
    pointer: int,
    address: _wire.FieldAddress,
    value: dict[str, pydantic.JsonValue],
) -> None:
    """Delegates an exact-address replacement to native validation.

    Args:
        pointer: Editor pointer checked by its Python owner.
        address: Stable location with a current topology guard.
        value: Tagged JSON-compatible replacement payload.

    Raises:
        UnsupportedEditError: The address is stale or replacement is invalid.
        ValueError: A floating-point value cannot be represented in JSON.
    """

    lib = _ffi.load_lib()
    result = lib.bethkit_record_editor_set_at_json(
        pointer,
        _ffi.senc(address.model_dump_json()),
        _ffi.senc(json.dumps(value, allow_nan=False)),
    )
    if result != 0:
        raise UnsupportedEditError(_ffi.last_error(lib))


def insert_at(
    pointer: int, address: _wire.FieldAddress, value: _wire.WireValue
) -> None:
    """Delegates insertion before one exact sibling to native validation.

    Args:
        pointer: Editor pointer checked by its Python owner.
        address: Current insertion anchor and repetition scope.
        value: Tagged value of the schema-declared sibling type.

    Raises:
        UnsupportedEditError: The insertion or repetition scope is invalid.
    """

    lib = _ffi.load_lib()
    result = lib.bethkit_record_editor_insert_at_json(
        pointer,
        _ffi.senc(address.model_dump_json()),
        _ffi.senc(value.model_dump_json()),
    )
    if result != 0:
        raise UnsupportedEditError(_ffi.last_error(lib))
