"""
Copyright (c) Modding Forge
"""

# Lazy, schema-generated record views and structural editing primitives.

from ..records._base import FieldRef, RecordModel, StructModel
from ..records._values import FormId, OpenIntEnum
from ..records._wire import FieldAddress, RecordSnapshot

__all__ = [
    "FieldAddress",
    "FieldRef",
    "FormId",
    "OpenIntEnum",
    "RecordModel",
    "RecordSnapshot",
    "StructModel",
]
