"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import BethkitClosedError, GlobalFormId, LoadOrder, PluginKind

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestGlobalFormId:
    """Tests ``bethkit.load_order.GlobalFormId``."""

    def test_str_contains_plugin_name_and_object_id(self) -> None:
        """Tests that __str__ formats as 'PluginName:0xOBJECTID'."""

        # given
        gfid = GlobalFormId(plugin_name="Skyrim.esm", object_id=0x12E49)

        # when
        result = str(gfid)

        # then
        assert "Skyrim.esm" in result
        assert "12E49" in result.upper()

    def test_str_pads_object_id_to_six_hex_digits(self) -> None:
        """Tests that the object ID is zero-padded to 6 hex digits."""

        # given
        gfid = GlobalFormId(plugin_name="A.esp", object_id=0x1)

        # when
        result = str(gfid)

        # then
        assert "000001" in result

    def test_equality_is_field_based(self) -> None:
        """Tests that two GlobalFormIds with same fields are equal."""

        # given
        a = GlobalFormId(plugin_name="Mod.esp", object_id=42)
        b = GlobalFormId(plugin_name="Mod.esp", object_id=42)

        # then
        assert a == b

    def test_frozen_model_is_hashable(self) -> None:
        """Tests that GlobalFormId can be used as a dict key."""

        # given
        gfid = GlobalFormId(plugin_name="Mod.esp", object_id=1)

        # when
        mapping = {gfid: "value"}

        # then
        assert mapping[gfid] == "value"

    def test_frozen_model_rejects_assignment(self) -> None:
        """Tests that assigning to fields on a frozen model raises."""

        # given
        gfid = GlobalFormId(plugin_name="A.esp", object_id=1)

        # when / then
        with pytest.raises(Exception):
            gfid.plugin_name = "B.esp"  # type: ignore[misc]


class TestLoadOrder:
    """Tests ``bethkit.load_order.LoadOrder``."""

    def test_constructor_creates_handle(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that LoadOrder() calls bethkit_load_order_new."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        lo = LoadOrder()

        # then
        mock_lib.bethkit_load_order_new.assert_called_once()
        lo.close()

    def test_close_frees_handle(self, mocker: MockerFixture) -> None:
        """Tests that close() calls bethkit_load_order_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        lo = LoadOrder()

        # when
        lo.close()

        # then
        mock_lib.bethkit_load_order_free.assert_called_once_with(0xABCD)

    def test_close_is_idempotent(self, mocker: MockerFixture) -> None:
        """Tests that calling close() twice does not call free twice."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        lo = LoadOrder()

        # when
        lo.close()
        lo.close()

        # then
        mock_lib.bethkit_load_order_free.assert_called_once()

    def test_context_manager_closes_on_exit(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __exit__ calls close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LoadOrder():
            pass

        # then
        mock_lib.bethkit_load_order_free.assert_called_once()

    def test_push_calls_native_function(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that push() delegates to bethkit_load_order_push."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mock_lib.bethkit_load_order_push.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LoadOrder() as lo:
            lo.push("Skyrim.esm", PluginKind.FULL)

        # then
        mock_lib.bethkit_load_order_push.assert_called_once()

    def test_closed_handle_raises_on_push(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that push() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        lo = LoadOrder()
        lo.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            lo.push("Skyrim.esm", PluginKind.FULL)

    def test_len_delegates_to_native(self, mocker: MockerFixture) -> None:
        """Tests that __len__() delegates to bethkit_load_order_len."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mock_lib.bethkit_load_order_len.return_value = 3
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LoadOrder() as lo:
            count = len(lo)

        # then
        assert count == 3

    def test_len_raises_after_close(self, mocker: MockerFixture) -> None:
        """Tests that __len__() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        lo = LoadOrder()
        lo.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            _ = len(lo)

    def test_resolve_returns_global_form_id(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that resolve() wraps the native result in a GlobalFormId."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mock_lib.bethkit_load_order_resolve.return_value = 0

        out_struct: MagicMock = mocker.MagicMock()
        out_struct.plugin_name = b"Skyrim.esm"
        out_struct.object_id = 0x12E49
        mocker.patch(
            "bethkit.load_order.BethkitGlobalFormId", return_value=out_struct
        )
        mocker.patch("bethkit.load_order.ctypes.byref", return_value=out_struct)
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with LoadOrder() as lo:
            gfid = lo.resolve(0x0012E49, "Skyrim.esm")

        # then
        assert gfid.plugin_name == "Skyrim.esm"
        assert gfid.object_id == 0x12E49

    def test_repr_shows_closed_when_closed(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __repr__() returns '<LoadOrder closed>' after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_load_order_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        lo = LoadOrder()
        lo.close()

        # when
        result = repr(lo)

        # then
        assert result == "<LoadOrder closed>"
