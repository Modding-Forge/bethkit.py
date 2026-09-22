"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import codecs
from pathlib import Path

import pytest

from scripts import check_file_lengths
from tests import file_length_support as support


class TestEncodedTextFiles:
    """Prevents alternate text encodings from bypassing the physical limit."""

    @pytest.mark.parametrize(
        ("encoding", "marker"),
        [
            ("utf-16-le", codecs.BOM_UTF16_LE),
            ("utf-16-be", codecs.BOM_UTF16_BE),
            ("utf-32-le", codecs.BOM_UTF32_LE),
            ("utf-32-be", codecs.BOM_UTF32_BE),
        ],
    )
    def test_unicode_bom_files_are_counted(
        self, tmp_path: Path, encoding: str, marker: bytes
    ) -> None:
        """Treats marked Unicode as text even for an unfamiliar extension.

        Args:
            tmp_path: Isolated source archive fixture.
            encoding: Explicit byte order for the Unicode fixture.
            marker: Matching Unicode byte-order marker.
        """

        # given
        support.write_policy(tmp_path)
        path = tmp_path / "fixture.custom"
        path.write_bytes(marker + ("text\n" * 400).encode(encoding))

        # when
        at_bound = check_file_lengths.check_file_lengths(tmp_path)
        path.write_bytes(marker + ("text\n" * 401).encode(encoding))
        over_bound = check_file_lengths.check_file_lengths(tmp_path)

        # then
        assert at_bound == []
        assert any("fixture.custom" in error for error in over_bound)

    @pytest.mark.parametrize(
        "content", [codecs.BOM_UTF16_LE + b"x", codecs.BOM_UTF32_BE + b"x"]
    )
    def test_malformed_unicode_is_rejected(
        self, tmp_path: Path, content: bytes
    ) -> None:
        """Reports malformed marked text instead of excluding it as binary.

        Args:
            tmp_path: Isolated source archive fixture.
            content: Marked Unicode with an incomplete final code unit.
        """

        support.write_policy(tmp_path)
        (tmp_path / "fixture.custom").write_bytes(content)
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert any("fixture.custom" in error for error in errors)

    @pytest.mark.parametrize(
        "suffix", [".py", ".json", ".md", ".toml", ".yml", ".sh", ".ps1"]
    )
    def test_nul_does_not_exempt_known_source(
        self, tmp_path: Path, suffix: str
    ) -> None:
        """Rejects binary-looking content placed in a known text source file.

        Args:
            tmp_path: Isolated source archive fixture.
            suffix: Known text format that must not become a binary exemption.
        """

        support.write_policy(tmp_path)
        filename = f"fixture{suffix}"
        (tmp_path / filename).write_bytes(b"\0text\n" * 401)
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert any(filename in error for error in errors)

    @pytest.mark.parametrize("suffix", [".dll", ".png"])
    def test_nul_binary_artifacts_are_excluded(
        self, tmp_path: Path, suffix: str
    ) -> None:
        """Does not count opaque executable and image payloads as text lines.

        Args:
            tmp_path: Isolated source archive fixture.
            suffix: Binary artifact format.
        """

        support.write_policy(tmp_path)
        (tmp_path / f"fixture{suffix}").write_bytes(b"\0binary\n" * 401)
        assert check_file_lengths.check_file_lengths(tmp_path) == []

    @pytest.mark.parametrize(
        "suffix", [".dll", ".png", ".so", ".zip", ".whl", ".bkschema"]
    )
    @pytest.mark.parametrize("encoding", ["utf-8", "utf-16", "utf-32"])
    def test_binary_extension_does_not_exempt_text(
        self, tmp_path: Path, suffix: str, encoding: str
    ) -> None:
        """Counts text by content even when its filename suggests binary data.

        Args:
            tmp_path: Isolated source archive fixture.
            suffix: Binary-looking extension that must not exempt text.
            encoding: Plain or BOM-marked Unicode encoding for the source.
        """

        support.write_policy(tmp_path)
        filename = f"fixture{suffix}"
        (tmp_path / filename).write_bytes(("text\n" * 401).encode(encoding))
        errors = check_file_lengths.check_file_lengths(tmp_path)
        assert any(filename in error and "401" in error for error in errors)

    def test_unknown_control_byte_payload_is_binary(
        self, tmp_path: Path
    ) -> None:
        """Recognizes opaque payloads without relying on a known extension.

        Args:
            tmp_path: Isolated source archive fixture.
        """

        support.write_policy(tmp_path)
        (tmp_path / "payload.custom").write_bytes(b"\x01binary\n" * 401)
        assert check_file_lengths.check_file_lengths(tmp_path) == []
