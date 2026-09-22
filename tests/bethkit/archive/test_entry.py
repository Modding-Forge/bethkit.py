"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

from bethkit import (
    Archive,
    ArchiveEntry,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestArchiveEntry:
    """Tests ``bethkit.archive.archive.ArchiveEntry``."""

    def test_path_returns_empty_string_on_null(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that ArchiveEntry.path returns '' when FFI returns null."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_entry_path.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # given — construct entry manually with a fake ptr
        with Archive.open(tmp_path / "x.bsa") as archive:
            entry = ArchiveEntry._from_native(0xBEEF, archive)
            result = entry.path

        # then
        assert result == ""

    def test_uncompressed_size_delegates_to_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that uncompressed size comes from the native entry."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_entry_uncompressed_size.return_value = 1024
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        with Archive.open(tmp_path / "x.bsa") as archive:
            entry = ArchiveEntry._from_native(0xBEEF, archive)

            # when
            size = entry.uncompressed_size

        # then
        assert size == 1024
