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
    Ba2GnrlWriter,
    Ba2Version,
    BethkitClosedError,
    BethkitNativeError,
    BsaVersion,
    BsaWriter,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestArchive:
    """Tests ``bethkit.archive.archive.Archive``."""

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
        """Tests that Archive.open() raises BethkitNativeError when FFI returns 0."""

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
        mock_lib.bethkit_archive_extract.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Archive.open(tmp_path / "test.bsa") as archive:
            result = archive.extract("textures/missing.dds")

        # then
        assert result is None

    def test_extract_required_raises_for_missing_file(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that extract_required() raises BethkitNotFoundError for absent files."""

        from bethkit import BethkitNotFoundError

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_extract.return_value = 0
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
        """Tests that extract_to_file() delegates to
        bethkit_archive_extract_to_file."""

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
        """Tests that extract_to_file() raises BethkitClosedError after close()."""

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
            entry = ArchiveEntry(0xBEEF, archive)
            result = entry.path

        # then
        assert result == ""

    def test_uncompressed_size_delegates_to_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that uncompressed_size reads from
        bethkit_archive_entry_uncompressed_size."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_archive_open.return_value = 0xDEAD
        mock_lib.bethkit_archive_entry_uncompressed_size.return_value = 1024
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        with Archive.open(tmp_path / "x.bsa") as archive:
            entry = ArchiveEntry(0xBEEF, archive)

            # when
            size = entry.uncompressed_size

        # then
        assert size == 1024


class TestBsaWriter:
    """Tests ``bethkit.archive.archive.BsaWriter``."""

    def test_constructor_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that BsaWriter() calls bethkit_bsa_writer_new and wraps the ptr."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        writer: BsaWriter = BsaWriter(BsaVersion.SSE)

        # then
        assert isinstance(writer, BsaWriter)
        writer.close()

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls bethkit_bsa_writer_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with BsaWriter(BsaVersion.SSE):
            pass

        # then
        mock_lib.bethkit_bsa_writer_free.assert_called_once_with(0xCCCC)

    def test_close_is_idempotent(self, mocker: MockerFixture) -> None:
        """Tests that close() twice does not double-free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        writer: BsaWriter = BsaWriter(BsaVersion.SSE)

        # when
        writer.close()
        writer.close()

        # then
        mock_lib.bethkit_bsa_writer_free.assert_called_once()

    def test_closed_writer_raises_on_add(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        writer: BsaWriter = BsaWriter(BsaVersion.SSE)
        writer.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            writer.add("meshes/foo.nif", b"\x00" * 16)

    def test_set_compress_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that set_compress() delegates to bethkit_bsa_writer_set_compress."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_bsa_writer_set_compress.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with BsaWriter(BsaVersion.SSE) as writer:
            writer.set_compress(True)

        # then
        mock_lib.bethkit_bsa_writer_set_compress.assert_called_once()

    def test_set_embed_names_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that set_embed_names() delegates to
        bethkit_bsa_writer_set_embed_names."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_bsa_writer_set_embed_names.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with BsaWriter(BsaVersion.SSE) as writer:
            writer.set_embed_names(True)

        # then
        mock_lib.bethkit_bsa_writer_set_embed_names.assert_called_once()

    def test_add_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that add() delegates to bethkit_bsa_writer_add."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_bsa_writer_add.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with BsaWriter(BsaVersion.SSE) as writer:
            writer.add("meshes/foo.nif", b"\xDE\xAD\xBE\xEF")

        # then
        mock_lib.bethkit_bsa_writer_add.assert_called_once()

    def test_write_to_calls_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that write_to() delegates to bethkit_bsa_writer_write_to."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_bsa_writer_write_to.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with BsaWriter(BsaVersion.SSE) as writer:
            writer.write_to(tmp_path / "out.bsa")

        # then
        mock_lib.bethkit_bsa_writer_write_to.assert_called_once()


class TestBa2GnrlWriter:
    """Tests ``bethkit.archive.archive.Ba2GnrlWriter``."""

    def test_constructor_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that Ba2GnrlWriter() calls bethkit_ba2_gnrl_writer_new and wraps ptr."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_ba2_gnrl_writer_new.return_value = 0xDDDD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        writer: Ba2GnrlWriter = Ba2GnrlWriter(Ba2Version.V1)

        # then
        assert isinstance(writer, Ba2GnrlWriter)
        writer.close()

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls bethkit_ba2_gnrl_writer_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_ba2_gnrl_writer_new.return_value = 0xDDDD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Ba2GnrlWriter(Ba2Version.V1):
            pass

        # then
        mock_lib.bethkit_ba2_gnrl_writer_free.assert_called_once_with(0xDDDD)

    def test_closed_writer_raises_on_add(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_ba2_gnrl_writer_new.return_value = 0xDDDD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        writer: Ba2GnrlWriter = Ba2GnrlWriter(Ba2Version.V1)
        writer.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            writer.add("meshes/foo.nif", b"\x00" * 16)

    def test_add_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that add() delegates to bethkit_ba2_gnrl_writer_add."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_ba2_gnrl_writer_new.return_value = 0xDDDD
        mock_lib.bethkit_ba2_gnrl_writer_add.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Ba2GnrlWriter(Ba2Version.V1) as writer:
            writer.add("sound/fx/boom.wav", b"\xFF" * 8)

        # then
        mock_lib.bethkit_ba2_gnrl_writer_add.assert_called_once()

    def test_write_to_calls_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that write_to() delegates to bethkit_ba2_gnrl_writer_write_to."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_ba2_gnrl_writer_new.return_value = 0xDDDD
        mock_lib.bethkit_ba2_gnrl_writer_write_to.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Ba2GnrlWriter(Ba2Version.V1) as writer:
            writer.write_to(tmp_path / "out.ba2")

        # then
        mock_lib.bethkit_ba2_gnrl_writer_write_to.assert_called_once()
