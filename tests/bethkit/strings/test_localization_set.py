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
    LocalizationSet,
    StringFileKind,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestLocalizationSet:
    """Tests ``bethkit.strings.strings.LocalizationSet``."""

    def test_new_creates_set(self, mocker: MockerFixture) -> None:
        """Creates a native localization set through the FFI."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        loc = LocalizationSet.new()

        # then
        assert isinstance(loc, LocalizationSet)
        loc.close()

    def test_context_manager_frees_on_exit(self, mocker: MockerFixture) -> None:
        """Tests that __exit__ calls bethkit_localization_set_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LocalizationSet.new():
            pass

        # then
        mock_lib.bethkit_localization_set_free.assert_called_once_with(0xBBBB)

    def test_close_is_idempotent(self, mocker: MockerFixture) -> None:
        """Tests that close() called twice does not double-free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        loc = LocalizationSet.new()

        # when
        loc.close()
        loc.close()

        # then
        mock_lib.bethkit_localization_set_free.assert_called_once()

    def test_closed_set_raises_on_get(self, mocker: MockerFixture) -> None:
        """Tests that get() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        loc = LocalizationSet.new()
        loc.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            loc.get(StringFileKind.STRINGS, 1)

    def test_get_returns_none_for_missing_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get() returns None when FFI returns a null pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mock_lib.bethkit_localization_set_get.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LocalizationSet.new() as loc:
            result = loc.get(StringFileKind.STRINGS, 9999)

        # then
        assert result is None

    def test_get_returns_bytes_for_found_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get() returns raw bytes for a found string ID."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mock_lib.bethkit_localization_set_get.return_value = 0xCCCC
        payload = b"Iron Dagger\x00"
        mocker.patch("ctypes.string_at", return_value=payload)
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LocalizationSet.new() as loc:
            result = loc.get(StringFileKind.STRINGS, 1)

        # then
        assert result == payload

    def test_get_str_strips_null_and_decodes(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get_str() strips trailing null and decodes as UTF-8."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mock_lib.bethkit_localization_set_get.return_value = 0xCCCC
        mocker.patch("ctypes.string_at", return_value=b"Wooden Sword\x00")
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LocalizationSet.new() as loc:
            result = loc.get_str(StringFileKind.STRINGS, 1)

        # then
        assert result == "Wooden Sword"

    def test_set_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that set() delegates to bethkit_localization_set_set."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mock_lib.bethkit_localization_set_set.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LocalizationSet.new() as loc:
            loc.set(StringFileKind.STRINGS, 1, b"Steel Sword\x00")

        # then
        mock_lib.bethkit_localization_set_set.assert_called_once()

    def test_write_calls_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that write() delegates to bethkit_localization_set_write."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mock_lib.bethkit_localization_set_write.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LocalizationSet.new() as loc:
            loc.write(tmp_path / "Skyrim.esp", "english")

        # then
        mock_lib.bethkit_localization_set_write.assert_called_once()
