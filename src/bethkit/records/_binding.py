"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Optional

import pydantic


class Binding(pydantic.BaseModel, frozen=True):
    """Generated connection between a Python attribute and a grammar node."""

    path: str
    """Authoritative schema path."""
    kind: str
    """Schema grammar or payload node kind."""
    name: str = ""
    """Original field label, which may itself contain path separators."""
    repeated_path: Optional[str] = None
    """Native repetition scope path for repeated children."""
    child_kind: Optional[str] = None
    """Repeated child's grammar kind."""
