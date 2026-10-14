"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Literal

import pydantic


class PluginEncodingDecision(pydantic.BaseModel, frozen=True):
    """Retained native codec decision and the evidence used to select it."""

    encoding: str
    """Concrete codec used for inline translatable reading and writing."""
    source: Literal["cpoverride", "detector", "ascii", "no_inline_text"]
    """Evidence used to select the codec; ASCII cannot identify its origin."""
    sample_bytes: int = pydantic.Field(ge=0, le=65536)
    """Number of bytes inspected, including separators between strings."""
    sample_strings: int = pydantic.Field(ge=0)
    """Number of complete schema-localizable strings in the sample."""
    scanned_records: int = pydantic.Field(ge=0, le=512)
    """Number of source records structurally inspected."""
    skipped_records: int = pydantic.Field(ge=0, le=512)
    """Records omitted because of size or structural/schema decoding errors."""
