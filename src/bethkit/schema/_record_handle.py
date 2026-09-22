"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Protocol


class RecordHandle(Protocol):
    """A lifetime-checked borrowed native record."""

    def _native_pointer(self) -> int:
        """Checks the owner chain before returning a borrowed pointer.

        Returns:
            The pointer while the complete owner chain remains open.

        Raises:
            BethkitClosedError: The record or an owning handle is closed.
        """

        ...
