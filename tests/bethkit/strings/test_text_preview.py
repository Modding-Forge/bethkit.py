"""
Copyright (c) Modding Forge
"""

import pytest

from bethkit.strings._text_preview import TextPreview


class TestTextPreview:
    """Prefer Windows-1252 without claiming certainty or dropping bytes."""

    @pytest.mark.parametrize(
        ("source", "expected"),
        [(b"Gh\xfbra", "Ghûra"), (b"R\xfbkd\xfbg", "Rûkdûg")],
    )
    def test_ambiguous_orc_names(self, source: bytes, expected: str) -> None:
        """Choose the requested Western interpretation, not a competing guess.

        Args:
            source: Exact original name bytes.
            expected: Requested Windows-1252 spelling.
        """

        preview = TextPreview.from_bytes(source)
        assert preview.text == expected
        assert preview.encoding == "windows-1252"
        assert not preview.escaped_bytes
        assert preview.text.encode("cp1252") == source

    def test_undefined_bytes_are_visible_not_replaced(self) -> None:
        """Use explicit escapes rather than replacement glyphs."""

        source = b"Original\x81\xff"
        preview = TextPreview.from_bytes(source)
        assert preview.text == "Original\\x81ÿ"
        assert preview.escaped_bytes
        assert "\ufffd" not in preview.text
        assert source == b"Original\x81\xff"

    def test_authoritative_utf8_is_not_overridden(self) -> None:
        """Keep an explicit codec even when its text body is damaged."""

        preview = TextPreview.from_bytes(b"Broken\xff", encoding="utf-8")
        assert preview.text == "Broken\\xff"
        assert preview.encoding == "utf-8"
        assert preview.escaped_bytes

    def test_unavailable_codec_only_shows_raw_escapes(self) -> None:
        """Do not substitute another codec for an unavailable explicit codec."""

        preview = TextPreview.from_bytes(b"Raw\xff", encoding="unknown-codec")
        assert preview.text == "Raw\\xff"
        assert preview.encoding == "unknown-codec"
        assert preview.escaped_bytes
