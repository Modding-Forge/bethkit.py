"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel


class Diagnostic(BaseModel, frozen=True):
    """Immutable semantic validation diagnostic."""

    severity: Literal["information", "warning", "error"]
    """Severity assigned by semantic validation."""
    code: str
    """Stable diagnostic category."""
    message: str
    """Human-readable description of the issue."""
    record_signature: bytes
    """Four-byte signature of the affected record."""
    form_id: int
    """File-local identity of the affected record."""
    schema_path: Optional[str] = None
    """Affected schema node, when known."""
    byte_start: Optional[int] = None
    """First affected payload byte, when known."""
    byte_end: Optional[int] = None
    """Exclusive end of the affected payload range."""
