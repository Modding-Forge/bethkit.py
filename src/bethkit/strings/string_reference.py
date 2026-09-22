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
    text: Optional[str]
    """Current text, or None when external tables were not supplied."""
    storage: Literal["inline", "external"]
    """Whether the source contains text bytes or an external string ID."""
    table_kind: Optional[StringFileKind] = None
    """External table selected by the authoritative schema."""
    string_id: Optional[int] = None
    """External table identifier; never part of the string's identity."""
    __source_token: Optional[uuid.UUID] = pydantic.PrivateAttr(default=None)

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
