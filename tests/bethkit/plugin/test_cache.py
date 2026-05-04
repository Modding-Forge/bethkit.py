"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitOwnershipError,
    CacheHit,
    Game,
    GlobalFormId,
    Plugin,
    PluginCache,
    Record,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestPluginCache:
    """Tests ``bethkit.plugin.cache.PluginCache``."""

    def test_constructor_calls_cache_new(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __init__ calls bethkit_plugin_cache_new."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        cache = PluginCache()

        # then
        mock_lib.bethkit_plugin_cache_new.assert_called_once()
        cache.close()

    def test_context_manager_frees_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls bethkit_plugin_cache_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginCache():
            pass

        # then
        mock_lib.bethkit_plugin_cache_free.assert_called_once_with(0xCAFE)

    def test_close_is_idempotent(self, mocker: MockerFixture) -> None:
        """Tests that calling close() twice does not double-free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        cache = PluginCache()

        # when
        cache.close()
        cache.close()

        # then
        mock_lib.bethkit_plugin_cache_free.assert_called_once()

    def test_record_count_raises_after_close(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that record_count raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        cache = PluginCache()
        cache.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            _ = cache.record_count

    def test_add_transfers_plugin_ownership(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add() transfers Plugin ownership; plugin becomes invalid."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mock_lib.bethkit_plugin_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_cache_add.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        plugin = Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE)

        # when
        with PluginCache() as cache:
            cache.add("mod.esp", plugin)

        # then — plugin handle was zeroed out by _transfer_ptr()
        with pytest.raises(BethkitClosedError):
            _ = plugin.kind

    def test_add_raises_type_error_for_non_plugin(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add() raises TypeError when given a non-Plugin object."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with PluginCache() as cache:
            with pytest.raises(TypeError):
                cache.add("mod.esp", object())  # type: ignore[arg-type]

    def test_add_raises_ownership_error_for_transferred_plugin(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add() raises BethkitOwnershipError for an already-added plugin."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mock_lib.bethkit_plugin_from_bytes.return_value = 0xDEAD
        mock_lib.bethkit_plugin_cache_add.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        plugin = Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE)

        # when — first add transfers ownership
        with PluginCache() as cache:
            cache.add("mod.esp", plugin)

            # then — second add must fail (handle is 0)
            with pytest.raises((BethkitOwnershipError, BethkitClosedError)):
                cache.add("mod2.esp", plugin)

    def test_resolve_returns_none_for_unknown_form_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that resolve() returns None when FFI returns a null pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mock_lib.bethkit_plugin_cache_resolve.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginCache() as cache:
            result = cache.resolve("unknown.esp", 0x000001)

        # then
        assert result is None

    def test_resolve_returns_record_for_known_form_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that resolve() wraps the returned pointer in a Record."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mock_lib.bethkit_plugin_cache_resolve.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginCache() as cache:
            result = cache.resolve("Skyrim.esm", 0x12E49)

        # then
        assert isinstance(result, Record)

    def test_find_by_editor_id_returns_none_for_unknown(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_by_editor_id() returns None when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mock_lib.bethkit_plugin_cache_find_by_editor_id.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginCache() as cache:
            result = cache.find_by_editor_id("NonExistentNPC")

        # then
        assert result is None

    def test_find_by_editor_id_returns_cache_hit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_by_editor_id() returns a CacheHit with a Record."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_cache_new.return_value = 0xCAFE
        mock_lib.bethkit_plugin_cache_find_by_editor_id.return_value = 0xBEEF

        # configure the out-parameter GlobalFormId struct
        out_struct = mocker.MagicMock()
        out_struct.plugin_name = b"Skyrim.esm"
        out_struct.object_id = 0x12E49
        mocker.patch(
            "bethkit.plugin.cache.BethkitGlobalFormId",
            return_value=out_struct,
        )
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginCache() as cache:
            hit = cache.find_by_editor_id("ArmorIron")

        # then
        assert isinstance(hit, CacheHit)
        assert isinstance(hit.global_form_id, GlobalFormId)
        assert hit.global_form_id.plugin_name == "Skyrim.esm"


class TestCacheHit:
    """Tests ``bethkit.plugin.cache.CacheHit``."""

    def test_fields_are_accessible(self) -> None:
        """Tests that CacheHit exposes record and global_form_id fields."""

        # given
        gfid = GlobalFormId(plugin_name="Skyrim.esm", object_id=0x12E49)
        sentinel_record = Record(0xDEAD, object())

        # when
        hit = CacheHit(record=sentinel_record, global_form_id=gfid)

        # then
        assert hit.record is sentinel_record
        assert hit.global_form_id == gfid
