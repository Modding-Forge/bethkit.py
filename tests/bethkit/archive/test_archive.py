"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    Archive,
    ArchiveEntry,
    BethkitClosedError,
    BethkitNativeError,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestArchive:
    """Tests ``bethkit.archive.archive.Archive``."""

    def test_missing_path_ignores_stale_error(
        self, mock_lib: MagicMock
    ) -> None:
        """Distinguishes missing content from a prior unrelated error."""

        # given
        mock_lib.bethkit_archive_extract_status.return_value = 1
        mock_lib.bethkit_last_error.return_value = b"an earlier failure"

        # when / then
        with Archive._from_native(0x100) as archive:
            assert archive.extract("missing.txt") is None
        mock_lib.bethkit_last_error.assert_not_called()
        mock_lib.bethkit_bytes_free.assert_not_called()

    def test_extraction_failure_is_not_absence(
        self, mock_lib: MagicMock
    ) -> None:
        """Surfaces decompression errors instead of treating them as missing."""

        # given
        mock_lib.bethkit_archive_extract_status.return_value = -1
        mock_lib.bethkit_last_error.return_value = b"corrupt compressed data"

        # when / then
        with Archive._from_native(0x100) as archive:
            with pytest.raises(BethkitNativeError, match="corrupt"):
                archive.extract("damaged.txt")
        mock_lib.bethkit_bytes_free.assert_not_called()

    def test_open_returns_archive_instance(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that Archive.open() wraps a non-null FFI pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        fake_path = tmp_path / "test.bsa"

        # when
        archive = Archive.open(fake_path)

        # then
        assert isinstance(archive, Archive)
        archive.close()

    def test_open_raises_on_null_ptr(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Raises a native error when opening an archive returns null."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"file not found"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with pytest.raises(BethkitNativeError):
            Archive.open(tmp_path / "missing.bsa")

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that __exit__ calls bethkit_archive_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Archive.open(tmp_path / "test.bsa"):
            pass

        # then
        mock_lib.bethkit_archive_free.assert_called_once_with(0xDEAD)

    def test_close_is_idempotent(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that close() called twice does not double-free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        archive = Archive.open(tmp_path / "test.bsa")

        # when
        archive.close()
        archive.close()

        # then
        mock_lib.bethkit_archive_free.assert_called_once()

    def test_extract_returns_none_for_missing_file(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that extract() returns None when FFI returns null slice."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_extract_status.return_value = 1
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Archive.open(tmp_path / "test.bsa") as archive:
            result = archive.extract("textures/missing.dds")

        # then
        assert result is None

    def test_extract_required_raises_for_missing_file(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Raises a not-found error when required content is absent."""

        from bethkit import BethkitNotFoundError

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_extract_status.return_value = 1
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with Archive.open(tmp_path / "test.bsa") as archive:
            with pytest.raises(BethkitNotFoundError):
                archive.extract_required("textures/missing.dds")

    def test_closed_archive_raises_on_extract(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that extract() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        archive = Archive.open(tmp_path / "test.bsa")
        archive.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            archive.extract("meshes/foo.nif")

    def test_file_count_delegates_to_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that file_count reads from bethkit_archive_file_count."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_file_count.return_value = 42
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Archive.open(tmp_path / "test.bsa") as archive:
            count = archive.file_count

        # then
        assert count == 42

    def test_format_name_decodes_bytes(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that format_name decodes the FFI byte string."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_format_name.return_value = b"BSA"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Archive.open(tmp_path / "test.bsa") as archive:
            fmt = archive.format_name

        # then
        assert fmt == "BSA"

    def test_extract_to_file_calls_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that file extraction delegates to the native writer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_extract_to_file.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Archive.open(tmp_path / "test.bsa") as archive:
            archive.extract_to_file("meshes/foo.nif", tmp_path / "foo.nif")

        # then
        mock_lib.bethkit_archive_extract_to_file.assert_called_once()

    def test_extract_to_file_raises_after_close(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Rejects extraction after closing the archive."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        archive = Archive.open(tmp_path / "test.bsa")
        archive.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            archive.extract_to_file("meshes/foo.nif", tmp_path / "foo.nif")

    def test_entry_iteration_yields_archive_entries(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that iterating an Archive yields ArchiveEntry objects."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_file_count.return_value = 1
        mock_lib.bethkit_archive_entry_get.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Archive.open(tmp_path / "test.bsa") as archive:
            entries: list[ArchiveEntry] = list(archive.entries())

        # then
        assert len(entries) == 1
        assert isinstance(entries[0], ArchiveEntry)
