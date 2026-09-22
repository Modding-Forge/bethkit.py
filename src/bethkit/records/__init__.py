"""Lazy, schema-generated record views and structural editing primitives.

Copyright (c) Modding Forge
"""

from bethkit.records._base import FieldRef, RecordModel, StructModel
from bethkit.records._values import FormId, OpenIntEnum
from bethkit.records._wire import FieldAddress, RecordSnapshot

__all__ = [
    "FieldAddress",
    "FieldRef",
    "FormId",
    "OpenIntEnum",
    "RecordModel",
    "RecordSnapshot",
    "StructModel",
]
