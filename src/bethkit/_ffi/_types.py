"""ctypes Structure and Union definitions mirroring bethkit.h."""
from __future__ import annotations

import ctypes


class BethkitSlice(ctypes.Structure):
    """A non-owning view of a byte slice passed across the FFI boundary."""

    _fields_ = [
        ("ptr", ctypes.POINTER(ctypes.c_uint8)),
        ("len", ctypes.c_size_t),
    ]


class BethkitGlobalFormId(ctypes.Structure):
    """A globally unique FormID (plugin name + 24-bit object ID)."""

    _fields_ = [
        # Borrowed from the owning LoadOrder / PluginCache.
        ("plugin_name", ctypes.c_char_p),
        ("object_id", ctypes.c_uint32),
    ]


class BethkitTypedFormId(ctypes.Structure):
    """A FormID together with the record signatures it is allowed to reference."""

    _fields_ = [
        ("raw", ctypes.c_uint32),
        # Pointer to a static array of 4-byte signatures; ctypes inserts the
        # necessary 4-byte padding before this field automatically.
        ("allowed_sigs", ctypes.c_void_p),
        ("allowed_count", ctypes.c_size_t),
    ]


class BethkitEnumVal(ctypes.Structure):
    """An enumeration field value with its raw integer and optional name."""

    _fields_ = [
        ("value", ctypes.c_int64),
        # Points to static memory; never free.
        ("name", ctypes.c_char_p),
    ]


class BethkitFlagsVal(ctypes.Structure):
    """A flags field value with the raw integer and the names of active bits."""

    _fields_ = [
        ("raw_value", ctypes.c_uint64),
        # Heap-allocated array of static string pointers; freed with the view.
        ("active_names", ctypes.POINTER(ctypes.c_char_p)),
        ("active_count", ctypes.c_size_t),
    ]


class BethkitFieldValuePayload(ctypes.Union):
    """The payload union inside BethkitFieldValue."""

    _fields_ = [
        ("int_val", ctypes.c_int64),
        ("float_val", ctypes.c_double),
        # Borrowed from the owning view; never free.
        ("str_val", ctypes.c_char_p),
        ("form_id", ctypes.c_uint32),
        ("form_id_typed", BethkitTypedFormId),
        ("bytes", BethkitSlice),
        ("enum_val", BethkitEnumVal),
        ("flags_val", BethkitFlagsVal),
        # Owned; freed with bethkit_field_entries_free (or via view free).
        ("struct_entries", ctypes.c_void_p),
        # Owned; freed with bethkit_field_values_free (or via view free).
        ("array_values", ctypes.c_void_p),
        ("localized_id", ctypes.c_uint32),
        ("_pad", ctypes.c_uint64),
    ]


class BethkitFieldValue(ctypes.Structure):
    """A decoded field value stored as a tagged union."""

    _fields_ = [
        ("kind", ctypes.c_int32),
        ("payload", BethkitFieldValuePayload),
    ]


class BethkitNamedField(ctypes.Structure):
    """A named field snapshot inside a BethkitRecordView or BethkitFieldEntries."""

    _fields_ = [
        # Points to static memory; never free.
        ("name", ctypes.c_char_p),
        ("value", BethkitFieldValue),
    ]
