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
    BethkitNativeError,
    LocalizationSet,
    StringFileKind,
    StringTable,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestStringTable:
    """Tests ``bethkit.strings.strings.StringTable``."""

    def test_new_creates_table(self, mocker: MockerFixture) -> None:
        """Tests that StringTable.new() calls bethkit_string_table_new."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        table = StringTable.new(StringFileKind.STRINGS)

        # then
        assert isinstance(table, StringTable)
        table.close()

    def test_new_raises_on_null_ptr(self, mocker: MockerFixture) -> None:
        """Tests that new() raises BethkitNativeError when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"failed"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with pytest.raises(BethkitNativeError):
            StringTable.new(StringFileKind.STRINGS)

    def test_open_returns_table(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that StringTable.open() wraps a non-null FFI pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_open.return_value = 0xAAAA
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        table = StringTable.open(tmp_path / "test.strings")

        # then
        assert isinstance(table, StringTable)
        table.close()

    def test_open_raises_on_null_ptr(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that open() raises BethkitNativeError when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_open.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"file not found"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with pytest.raises(BethkitNativeError):
            StringTable.open(tmp_path / "missing.strings")

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls bethkit_string_table_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS):
            pass

        # then
        mock_lib.bethkit_string_table_free.assert_called_once_with(0xAAAA)

    def test_close_is_idempotent(self, mocker: MockerFixture) -> None:
        """Tests that close() called twice does not double-free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        table = StringTable.new(StringFileKind.STRINGS)

        # when
        table.close()
        table.close()

        # then
        mock_lib.bethkit_string_table_free.assert_called_once()

    def test_get_returns_none_for_missing_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get() returns None when FFI returns a null pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_get.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            result = table.get(9999)

        # then
        assert result is None

    def test_get_returns_bytes_for_known_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get() returns raw bytes when FFI returns a valid pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        fake_ptr = 0xBEEF
        payload = b"Hello World\x00"
        mock_lib.bethkit_string_table_get.return_value = fake_ptr
        mocker.patch(
            "ctypes.string_at", return_value=payload
        )
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            result = table.get(1)

        # then
        assert result == payload

    def test_get_str_strips_null_and_decodes(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get_str() strips trailing null and decodes as UTF-8."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_get.return_value = 0xBEEF
        mocker.patch(
            "ctypes.string_at", return_value=b"Iron Sword\x00"
        )
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            result = table.get_str(1)

        # then
        assert result == "Iron Sword"

    def test_get_str_returns_none_for_missing_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get_str() returns None for an absent string ID."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_get.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            result = table.get_str(9999)

        # then
        assert result is None

    def test_closed_table_raises_on_get(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that get() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        table = StringTable.new(StringFileKind.STRINGS)
        table.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            table.get(1)

    def test_insert_calls_native(self, mocker: MockerFixture) -> None:
        """Tests that insert() calls bethkit_string_table_insert."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_insert.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            table.insert(1, b"Iron Sword\x00")

        # then
        mock_lib.bethkit_string_table_insert.assert_called_once()

    def test_remove_returns_true_when_found(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that remove() returns True when the FFI reports the entry existed."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_remove.return_value = 1
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            result = table.remove(1)

        # then
        assert result is True

    def test_remove_returns_false_when_absent(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that remove() returns False when the FFI reports the entry was absent."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_remove.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            result = table.remove(9999)

        # then
        assert result is False

    def test_kind_returns_string_file_kind(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that kind delegates to bethkit_string_table_kind."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_kind.return_value = int(
            StringFileKind.DL_STRINGS
        )
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.DL_STRINGS) as table:
            kind = table.kind

        # then
        assert kind == StringFileKind.DL_STRINGS

    def test_len_delegates_to_native(self, mocker: MockerFixture) -> None:
        """Tests that __len__() delegates to bethkit_string_table_len."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_len.return_value = 7
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            count = len(table)

        # then
        assert count == 7

    def test_insert_new_returns_assigned_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that insert_new() returns the ID assigned by the native call."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_insert_new.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            assigned_id = table.insert_new(b"Dragon\x00")

        # then
        assert isinstance(assigned_id, int)
        mock_lib.bethkit_string_table_insert_new.assert_called_once()

    def test_write_to_file_calls_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that write_to_file() delegates to
        bethkit_string_table_write_to_file."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mock_lib.bethkit_string_table_write_to_file.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with StringTable.new(StringFileKind.STRINGS) as table:
            table.write_to_file(tmp_path / "Skyrim_english.strings")

        # then
        mock_lib.bethkit_string_table_write_to_file.assert_called_once()

    def test_write_to_file_raises_after_close(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that write_to_file() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_string_table_new.return_value = 0xAAAA
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        table = StringTable.new(StringFileKind.STRINGS)
        table.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            table.write_to_file(tmp_path / "out.strings")


class TestLocalizationSet:
    """Tests ``bethkit.strings.strings.LocalizationSet``."""

    def test_new_creates_set(self, mocker: MockerFixture) -> None:
        """Tests that LocalizationSet.new() calls bethkit_localization_set_new."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        loc = LocalizationSet.new()

        # then
        assert isinstance(loc, LocalizationSet)
        loc.close()

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls bethkit_localization_set_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_localization_set_new.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LocalizationSet.new():
            pass

        # then
        mock_lib.bethkit_localization_set_free.assert_called_once_with(
            0xBBBB
        )

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

    def test_closed_set_raises_on_get(
        self, mocker: MockerFixture
    ) -> None:
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
