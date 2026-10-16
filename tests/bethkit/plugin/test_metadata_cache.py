"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from bethkit import BethkitClosedError, BethkitNativeError, Game, Plugin


class TestMetadataCache:
    """Checks immutable metadata reuse without bypassing owner validation."""

    def test_cache_is_private_and_owner_scoped(
        self, mock_lib: MagicMock
    ) -> None:
        """Caches once per plugin and never exposes a mutable cached list.

        Args:
            mock_lib: Mock native functions, never a real library.
        """

        # given
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 123
        mock_lib.bethkit_plugin_master_count.return_value = 2
        mock_lib.bethkit_plugin_master_get.side_effect = [
            b"Skyrim.esm",
            b"Update.esm",
            b"Other.esm",
            b"Second.esm",
        ]
        with (
            Plugin.from_bytes(b"data", Game.SKYRIM_SE) as first,
            Plugin.from_bytes(b"data", Game.SKYRIM_SE) as second,
        ):
            # when
            names = first.masters
            names.clear()
            assert first.masters == ["Skyrim.esm", "Update.esm"]
            assert first.master_at(1) == "Update.esm"
            assert first.master_count == 2
            assert second.masters == ["Other.esm", "Second.esm"]

        # then
        assert mock_lib.bethkit_plugin_master_get.call_count == 4
        assert mock_lib.bethkit_plugin_master_count.call_count == 2
        with pytest.raises(BethkitClosedError):
            _ = first.masters
        with pytest.raises(BethkitClosedError):
            _ = first.master_count
        with pytest.raises(BethkitClosedError):
            first.master_at(0)

    def test_failed_read_is_not_cached(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Retains original FFI errors and retries incomplete metadata loads.

        Args:
            mock_lib: Mock native functions.
            mocker: Patches the immediate native error conversion.
        """

        # given
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 123
        mock_lib.bethkit_plugin_master_count.return_value = 1
        mock_lib.bethkit_plugin_master_get.side_effect = [None, b"Skyrim.esm"]
        mocker.patch(
            "bethkit._ffi.raise_last_error",
            side_effect=BethkitNativeError("missing master"),
        )
        with Plugin.from_bytes(b"data", Game.SKYRIM_SE) as plugin:
            # when / then
            with pytest.raises(BethkitNativeError, match="missing master"):
                _ = plugin.masters
            assert plugin.masters == ["Skyrim.esm"]
            assert mock_lib.bethkit_plugin_master_get.call_count == 2

    def test_cached_owner_still_uses_ffi_for_invalid_index(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Preserves native bounds errors rather than Python negative indexing.

        Args:
            mock_lib: Mock native functions.
            mocker: Patches native error conversion.
        """

        mock_lib.bethkit_plugin_open_from_bytes.return_value = 123
        mock_lib.bethkit_plugin_master_count.return_value = 0
        mock_lib.bethkit_plugin_master_get.return_value = None
        mocker.patch(
            "bethkit._ffi.raise_last_error",
            side_effect=BethkitNativeError("out of range"),
        )
        with Plugin.from_bytes(b"data", Game.SKYRIM_SE) as plugin:
            assert plugin.masters == []
            for index in (-1, 0):
                with pytest.raises(BethkitNativeError, match="out of range"):
                    plugin.master_at(index)
