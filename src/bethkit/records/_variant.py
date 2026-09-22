"""
Copyright (c) Modding Forge
"""

from __future__ import annotations


class Variant(str):
    """Immutable annotation token, not a Pydantic value or schema provider."""

    def __new__(cls, *, path: str) -> Variant:
        """Creates a hashable native-path token without validation hooks.

        Args:
            path: Exact native schema path identifying one union alternative.

        Returns:
            Immutable metadata that Pydantic leaves out of value validation.
        """

        return super().__new__(cls, path)

    @property
    def path(self) -> str:
        """Returns the schema identity represented by this metadata token."""

        return str(self)
