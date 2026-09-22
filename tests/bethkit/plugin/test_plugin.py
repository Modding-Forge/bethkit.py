"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitNativeError,
    Game,
    Group,
    Plugin,
    PluginKind,
    Record,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestPlugin:
    """Tests ``bethkit.plugin.plugin.Plugin``."""

    def test_from_bytes_returns_plugin_instance(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that from_bytes() creates a Plugin from a non-null FFI ptr."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEADBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        plugin = Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE)

        # then
        assert isinstance(plugin, Plugin)
        plugin.close()

    def test_from_bytes_raises_on_null_ptr(self, mocker: MockerFixture) -> None:
        """Raises a native error when parsing returns a null pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"parse error"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with pytest.raises(BethkitNativeError):
            Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE)

    def test_context_manager_frees_handle(self, mocker: MockerFixture) -> None:
        """Tests that __exit__ calls bethkit_plugin_free exactly once."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE):
            pass

        # then
        mock_lib.bethkit_plugin_free.assert_called_once_with(0xDEAD)

    def test_close_is_idempotent(self, mocker: MockerFixture) -> None:
        """Tests that close() called twice does not double-free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        plugin = Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE)

        # when
        plugin.close()
        plugin.close()

        # then
        mock_lib.bethkit_plugin_free.assert_called_once()

    def test_kind_returns_plugin_kind_full(self, mocker: MockerFixture) -> None:
        """Tests that kind returns PluginKind.FULL when native returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_kind.return_value = int(PluginKind.FULL)
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE) as plugin:
            kind = plugin.kind

        # then
        assert kind == PluginKind.FULL

    def test_kind_raises_after_close(self, mocker: MockerFixture) -> None:
        """Tests that accessing kind after close() raises BethkitClosedError."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        plugin = Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE)
        plugin.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            _ = plugin.kind

    def test_masters_returns_list_of_strings(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that masters property decodes and returns all master names."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_master_count.return_value = 2
        mock_lib.bethkit_plugin_master_get.side_effect = [
            b"Skyrim.esm",
            b"Update.esm",
        ]
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE) as plugin:
            masters = plugin.masters

        # then
        assert masters == ["Skyrim.esm", "Update.esm"]

    def test_no_masters_returns_empty_list(self, mocker: MockerFixture) -> None:
        """Tests that masters returns [] when master_count is 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_master_count.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE) as plugin:
            masters = plugin.masters

        # then
        assert masters == []

    def test_group_count_returns_native_value(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that group_count delegates to bethkit_plugin_group_count."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_group_count.return_value = 5
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE) as plugin:
            count = plugin.group_count

        # then
        assert count == 5

    def test_iteration_yields_groups(self, mocker: MockerFixture) -> None:
        """Tests that iterating a Plugin yields Group objects."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_group_count.return_value = 1
        mock_lib.bethkit_plugin_group_get.return_value = 0xBEEF
        mock_lib.bethkit_group_type.return_value = 0
        mock_lib.bethkit_group_child_count.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE) as plugin:
            groups = list(plugin)

        # then
        assert len(groups) == 1
        assert isinstance(groups[0], Group)

    def test_find_record_returns_none_when_not_found(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_record() returns None when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_find_record.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE) as plugin:
            result = plugin.find_record(0x99999999)

        # then
        assert result is None

    def test_find_record_returns_record_when_found(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_record() wraps a non-null FFI pointer as a Record."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_find_record.return_value = 0xAAAA
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE) as plugin:
            result = plugin.find_record(0x000D62)

        # then
        assert isinstance(result, Record)

    @pytest.mark.integration
    def test_minimal_plugin_bytes_parse(self) -> None:
        """Integration: parse a minimal plugin built from raw bytes.

        Requires the real bethkit_ffi library to be available.
        """

        from conftest import build_minimal_plugin

        # given
        data = build_minimal_plugin(hedr_version=1.7)

        # when
        with Plugin.from_bytes(data, Game.SKYRIM_SE) as plugin:
            kind = plugin.kind
            n_groups = plugin.group_count

        # then
        assert kind == PluginKind.FULL
        assert n_groups == 1
