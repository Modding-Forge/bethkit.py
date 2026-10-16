"""
Copyright (c) Modding Forge
"""

import pydantic


class StringScanDiagnostic(pydantic.BaseModel, frozen=True):
    """Nontext record retained as opaque source after a decode failure."""

    record_signature: str = pydantic.Field(min_length=4, max_length=4)
    """Schema-proven nontranslatable record type."""
    form_id: int = pydantic.Field(ge=0, le=0xFFFFFFFF)
    """Exact source record identity, not a synthetic replacement."""
    source_size: int = pydantic.Field(ge=0, le=0xFFFFFFFF)
    """Original on-disk payload size, including compressed representation."""
    message: str
    """Original decoding failure; opaque retention is not a repair."""
