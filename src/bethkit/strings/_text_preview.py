"""
Copyright (c) Modding Forge
"""

import pydantic


class TextPreview(pydantic.BaseModel, frozen=True):
    """Unconfirmed Windows-1252 display choice, separate from original bytes."""

    text: str
    """Display text with visible hex escapes for undecodable bytes."""
    encoding: str = "windows-1252"
    """Preferred best-effort codec for ambiguous byte text."""
    escaped_bytes: bool
    """Whether undefined bytes needed explicit hex escapes in the preview."""

    @classmethod
    def from_bytes(
        cls, data: bytes, *, encoding: str = "windows-1252"
    ) -> "TextPreview":
        """Build a reversible or visibly escaped preview without changing input.

        Args:
            data: Original undecoded text body.
            encoding: Explicit authoritative codec or the preferred fallback.

        Returns:
            An unconfirmed preview with an explicit codec and escape indicator.
        """

        try:
            return cls(
                text=data.decode(encoding),
                encoding=encoding,
                escaped_bytes=False,
            )
        except UnicodeDecodeError:
            return cls(
                text=data.decode(encoding, errors="backslashreplace"),
                encoding=encoding,
                escaped_bytes=True,
            )
        except LookupError:
            return cls(
                text=data.decode("ascii", errors="backslashreplace"),
                encoding=encoding,
                escaped_bytes=True,
            )
