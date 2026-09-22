"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    Ba2GnrlWriter,
    Ba2Version,
    BethkitClosedError,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestBa2GnrlWriter:
    """Tests ``bethkit.archive.archive.Ba2GnrlWriter``."""

    def test_constructor_calls_native(self, mocker: MockerFixture) -> None:
        """Wraps a newly created native BA2 writer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_ba2_gnrl_writer_new.return_value = 0xDDDD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        writer: Ba2GnrlWriter = Ba2GnrlWriter(Ba2Version.V1)

        # then
        assert isinstance(writer, Ba2GnrlWriter)
        writer.close()

    def test_context_manager_frees_on_exit(self, mocker: MockerFixture) -> None:
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

    def test_closed_writer_raises_on_add(self, mocker: MockerFixture) -> None:
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
            writer.add("sound/fx/boom.wav", b"\xff" * 8)

        # then
        mock_lib.bethkit_ba2_gnrl_writer_add.assert_called_once()

    def test_write_to_calls_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Delegates writing to the native BA2 writer."""

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
