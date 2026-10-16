"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import uuid
from typing import Literal, Optional

import pydantic

from ..enums import StringFileKind
from ..records import _wire
from .string_identity import StringIdentity


class StringReference(pydantic.BaseModel, frozen=True):
    """Immutable text snapshot with a native structural edit address."""

    identity: StringIdentity
    """Position-based identity that never incorporates the current text."""
    address: _wire.FieldAddress
    """Exact native address, including a stale-structure guard."""
    schema_path: Optional[str] = None
    """Exact selected string leaf path for scoped codec edits."""
    text: Optional[str]
    """Decoded text; None for unresolved tables or preserved raw bodies."""
    storage: Literal["inline", "external"]
    """Whether the source contains text bytes or an external string ID."""
    encoding: Optional[str] = None
    """Decoded inline codec; absent for external or preserved raw text."""
    encoding_source: Optional[Literal["schema", "heuristic", "forced"]] = None
    """How the inline codec was selected; never part of identity."""
    raw_bytes: Optional[bytes] = None
    """Original undecoded body, excluding prefixes and terminators."""
    decoding_warning: Optional[str] = None
    """Why this inline body has no guessed text; source stays unchanged."""
    best_effort_text: Optional[str] = None
    """Unconfirmed display preview, never authoritative replacement text."""
    best_effort_encoding: Optional[str] = None
    """Codec chosen for the preview; raw bytes remain the source of truth."""
    preview_escaped_bytes: bool = False
    """Whether undefined preview bytes are shown as explicit hex escapes."""
    table_kind: Optional[StringFileKind] = None
    """External table selected by the authoritative schema."""
    string_id: Optional[int] = None
    """External table identifier; never part of the string's identity."""
    __source_token: Optional[uuid.UUID] = pydantic.PrivateAttr(default=None)

    @pydantic.field_serializer("raw_bytes", when_used="json")
    def __serialize_raw(self, value: Optional[bytes]) -> Optional[str]:
        """Encode arbitrary raw bytes as lossless JSON hex.

        Args:
            value: Optional original byte body.

        Returns:
            Hex text, or None when the field was decoded.
        """

        return None if value is None else value.hex()

    @pydantic.field_validator("raw_bytes", mode="before")
    @classmethod
    def __parse_raw(
        cls, value: object, info: pydantic.ValidationInfo
    ) -> object:
        """Restore JSON hex without changing normal Python byte inputs.

        Args:
            value: External raw value.
            info: Whether validation reads JSON or Python data.

        Returns:
            Original bytes for JSON hex, otherwise the unmodified value.

        Raises:
            ValueError: JSON raw data is not valid hex.
        """

        return (
            bytes.fromhex(value)
            if info.mode == "json" and isinstance(value, str)
            else value
        )

    @property
    def _source_token(self) -> Optional[uuid.UUID]:
        """Private live-instance provenance, separate from persistent identity.

        Returns:
            The source instance token, or None for an unbound value.
        """

        return self.__source_token

    def _bind_source(self, token: uuid.UUID) -> None:
        """Binds fresh snapshot metadata to its source instance exactly once.

        Args:
            token: Private identity supplied by the source plugin.

        Raises:
            ValueError: This reference already belongs to a source instance.
        """

        if self.__source_token is not None:
            raise ValueError(
                "A string reference is already bound to its source."
            )
        # Provenance is initialized once after validation, never from user data.
        object.__setattr__(self, "_StringReference__source_token", token)
