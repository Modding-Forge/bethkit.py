"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BsaVersion,
    BsaWriter,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestBsaWriter:
    """Tests ``bethkit.archive.archive.BsaWriter``."""

    def test_constructor_calls_native(self, mocker: MockerFixture) -> None:
        """Wraps a newly created native BSA writer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_bsa_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        writer: BsaWriter = BsaWriter(BsaVersion.SSE)

        # then
        assert isinstance(writer, BsaWriter)
        writer.close()

    def test_context_manager_frees_on_exit(self, mocker: MockerFixture) -> None:
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

    def test_closed_writer_raises_on_add(self, mocker: MockerFixture) -> None:
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
        """Delegates compression settings to the native writer."""

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
        """Tests that name embedding delegates to the native writer."""

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
            writer.add("meshes/foo.nif", b"\xde\xad\xbe\xef")

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
