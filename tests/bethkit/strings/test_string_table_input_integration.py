"""
Copyright (c) Modding Forge
"""

from io import BytesIO
from pathlib import Path

import pytest

from bethkit import BethkitNativeError, StringFileKind, StringTable


@pytest.mark.integration
class TestNativeStringTableInput:
    """Parses complete serialized tables without filesystem extraction."""

    @pytest.mark.parametrize("kind", list(StringFileKind))
    def test_bytes_and_stream_match_file_parser(
        self, tmp_path: Path, kind: StringFileKind
    ) -> None:
        """Matches file parsing and retains entries after the source closes."""

        # given
        extension = {
            StringFileKind.STRINGS: "strings",
            StringFileKind.DL_STRINGS: "dlstrings",
            StringFileKind.IL_STRINGS: "ilstrings",
        }[kind]
        path = tmp_path / f"test.{extension}"
        expected = {17: "Grüße".encode(), 29: b"\xff\xfe", 42: b""}
        with StringTable.new(kind) as original:
            for entry_id, raw in expected.items():
                original.insert(entry_id, raw)
            original.write_to_file(path)
        serialized = path.read_bytes()

        # when
        stream = BytesIO(b"prefix" + serialized)
        stream.seek(6)
        with (
            StringTable.open(path) as disk,
            StringTable.from_bytes(serialized, kind) as memory,
            StringTable.from_stream(stream, kind) as streamed,
        ):
            assert not stream.closed
            stream.close()

            # then
            for table in (disk, memory, streamed):
                assert table.kind == kind
                assert len(table) == len(expected)
                for entry_id, raw in expected.items():
                    assert table.get(entry_id) == raw
                assert table.get_str(17) == "Grüße"
                assert table.get(999) is None
            memory.insert(17, b"changed")
            assert streamed.get(17) == expected[17]
            assert disk.get(17) == expected[17]

    @pytest.mark.parametrize("kind", list(StringFileKind))
    @pytest.mark.parametrize("payload", [b"", b"\0" * 7, b"\xff" * 8])
    def test_malformed_input_is_rejected(
        self, kind: StringFileKind, payload: bytes
    ) -> None:
        """Rejects malformed serialized data rather than inventing entries."""

        with pytest.raises(BethkitNativeError):
            StringTable.from_bytes(payload, kind)

    @pytest.mark.parametrize("kind", list(StringFileKind))
    def test_serialized_empty_table_is_valid(
        self, kind: StringFileKind
    ) -> None:
        """Distinguishes a complete empty table header from missing data."""

        with StringTable.from_bytes(bytes(8), kind) as table:
            assert table.kind == kind
            assert len(table) == 0
