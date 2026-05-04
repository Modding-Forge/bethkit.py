"""
Copyright (c) Modding Forge

Internal FFI package — loads the native library and declares ctypes types.

Not part of the public API; import from ``bethkit`` directly.
"""
from __future__ import annotations

from ._loader import (
    copy_and_free_str,
    enc,
    last_error,
    load_lib,
    raise_last_error,
    senc,
)
from ._types import (
    BethkitEnumVal,
    BethkitFieldValue,
    BethkitFieldValuePayload,
    BethkitFlagsVal,
    BethkitGlobalFormId,
    BethkitNamedField,
    BethkitSlice,
    BethkitTypedFormId,
)

__all__ = [
    "copy_and_free_str",
    "enc",
    "last_error",
    "load_lib",
    "raise_last_error",
    "senc",
    "BethkitEnumVal",
    "BethkitFieldValue",
    "BethkitFieldValuePayload",
    "BethkitFlagsVal",
    "BethkitGlobalFormId",
    "BethkitNamedField",
    "BethkitSlice",
    "BethkitTypedFormId",
]
