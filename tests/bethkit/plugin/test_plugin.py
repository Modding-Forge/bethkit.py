"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
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
    SubRecord,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestSubRecord:
    """Tests ``bethkit.plugin.plugin.SubRecord``."""

    def test_as_u8_calls_native_and_returns_int(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_u8() delegates to bethkit_subrecord_as_u8."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u8.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord(0xBEEF, Record(0xDEAD, object()))

        # when
        result = sub.as_u8()

        # then
        assert isinstance(result, int)
        mock_lib.bethkit_subrecord_as_u8.assert_called_once()

    def test_as_u16_calls_native_and_returns_int(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_u16() delegates to bethkit_subrecord_as_u16."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u16.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord(0xBEEF, Record(0xDEAD, object()))

        # when
        result = sub.as_u16()

        # then
        assert isinstance(result, int)
        mock_lib.bethkit_subrecord_as_u16.assert_called_once()

    def test_as_u32_calls_native_and_returns_int(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_u32() delegates to bethkit_subrecord_as_u32."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u32.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord(0xBEEF, Record(0xDEAD, object()))

        # when
        result = sub.as_u32()

        # then
        assert isinstance(result, int)
        mock_lib.bethkit_subrecord_as_u32.assert_called_once()

    def test_as_f32_calls_native_and_returns_float(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_f32() delegates to bethkit_subrecord_as_f32."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_f32.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord(0xBEEF, Record(0xDEAD, object()))

        # when
        result = sub.as_f32()

        # then
        assert isinstance(result, float)
        mock_lib.bethkit_subrecord_as_f32.assert_called_once()

    def test_as_str_decodes_utf8_and_frees_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_str() decodes the native string and frees the pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        fake_ptr: int = 0xCCCC
        mock_lib.bethkit_subrecord_as_zstring.return_value = fake_ptr
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        mocker.patch("ctypes.string_at", return_value=b"TestValue")
        sub = SubRecord(0xBEEF, Record(0xDEAD, object()))

        # when
        result = sub.as_str()

        # then
        assert result == "TestValue"
        mock_lib.bethkit_zstring_free.assert_called_once_with(fake_ptr)

    def test_as_str_raises_on_null_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_str() raises BethkitNativeError when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_zstring.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"type mismatch"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord(0xBEEF, Record(0xDEAD, object()))

        # when / then
        with pytest.raises(BethkitNativeError):
            sub.as_str()

    def test_as_u8_raises_on_native_error(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that as_u8() raises BethkitNativeError when FFI returns nonzero."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_subrecord_as_u8.return_value = 1
        mock_lib.bethkit_last_error.return_value = b"size mismatch"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sub = SubRecord(0xBEEF, Record(0xDEAD, object()))

        # when / then
        with pytest.raises(BethkitNativeError):
            sub.as_u8()


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

    def test_from_bytes_raises_on_null_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that from_bytes() raises BethkitNativeError when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"parse error"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with pytest.raises(BethkitNativeError):
            Plugin.from_bytes(b"\x00" * 32, Game.SKYRIM_SE)

    def test_context_manager_frees_handle(
        self, mocker: MockerFixture
    ) -> None:
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

    def test_kind_returns_plugin_kind_full(
        self, mocker: MockerFixture
    ) -> None:
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

    def test_no_masters_returns_empty_list(
        self, mocker: MockerFixture
    ) -> None:
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
        """
        Integration: parse a minimal plugin built from raw bytes.

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


class TestRecord:
    """Tests ``bethkit.plugin.plugin.Record``."""

    def test_editor_id_returns_none_when_absent(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that editor_id returns None when FFI returns a null pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_editor_id.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sentinel_parent = object()
        record = Record(0xDEAD, sentinel_parent)

        # when
        result = record.editor_id

        # then
        assert result is None

    def test_editor_id_decodes_bytes(self, mocker: MockerFixture) -> None:
        """Tests that editor_id decodes the FFI string and frees the pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        fake_ptr = 0xBEEF
        mock_lib.bethkit_record_editor_id.return_value = fake_ptr
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        mocker.patch("ctypes.string_at", return_value=b"TestNPC")
        record = Record(0xDEAD, object())

        # when
        result = record.editor_id

        # then
        assert result == "TestNPC"
        mock_lib.bethkit_record_editor_id_free.assert_called_once_with(
            fake_ptr
        )

    def test_form_id_delegates_to_native(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that form_id returns the value from bethkit_record_form_id."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_form_id.return_value = 0x000D62
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record(0xDEAD, object())

        # when
        result = record.form_id

        # then
        assert result == 0x000D62

    def test_signature_returns_four_bytes(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that signature copies four bytes from the native buffer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()

        def fake_sig(ptr: int, buf: ctypes.Array[ctypes.c_uint8]) -> int:
            for i, b in enumerate(b"NPC_"):
                buf[i] = b
            return 0

        mock_lib.bethkit_record_signature.side_effect = fake_sig
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record(0xDEAD, object())

        # when
        sig = record.signature

        # then
        assert sig == b"NPC_"

    def test_find_subrecord_returns_none_when_absent(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_subrecord() returns None when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_subrecord_find.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record(0xDEAD, object())

        # when
        result = record.find_subrecord(b"EDID")

        # then
        assert result is None

    def test_find_subrecord_returns_subrecord(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that find_subrecord() wraps a non-null FFI pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_subrecord_find.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record(0xDEAD, object())

        # when
        result = record.find_subrecord(b"EDID")

        # then
        assert isinstance(result, SubRecord)

    def test_find_subrecord_validates_signature_length(self) -> None:
        """Tests that find_subrecord() raises ValueError for wrong sig length."""

        # given
        record = Record(0xDEAD, object())

        # when / then
        with pytest.raises(ValueError):
            record.find_subrecord(b"ED")

    def test_flags_delegates_to_native(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that flags reads from bethkit_record_flags."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_flags.return_value = 0x00000020
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record(0xDEAD, object())

        # when
        result = record.flags

        # then
        assert result == 0x00000020

    def test_form_version_delegates_to_native(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that form_version reads from bethkit_record_form_version."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_record_form_version.return_value = 44
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        record = Record(0xDEAD, object())

        # when
        result = record.form_version

        # then
        assert result == 44


class TestGroup:
    """Tests ``bethkit.plugin.plugin.Group``."""

    def test_child_count_delegates_to_native(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that child_count reads from bethkit_group_child_count."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_count.return_value = 3
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sentinel_parent = Plugin.__new__(Plugin)
        group = Group(0xDEAD, sentinel_parent)

        # when
        count = group.child_count

        # then
        assert count == 3

    def test_child_as_record_returns_none_for_group_child(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that child_as_record() returns None when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_as_record.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = Group(0xDEAD, Plugin.__new__(Plugin))

        # when
        result = group.child_as_record(0)

        # then
        assert result is None

    def test_child_as_record_wraps_valid_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that child_as_record() wraps a non-null FFI pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_as_record.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = Group(0xDEAD, Plugin.__new__(Plugin))

        # when
        result = group.child_as_record(0)

        # then
        assert isinstance(result, Record)

    def test_iter_yields_records_and_groups(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that iterating a Group yields mixed Record and Group children."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_count.return_value = 2
        mock_lib.bethkit_group_child_is_record.side_effect = [True, False]
        mock_lib.bethkit_group_child_as_record.return_value = 0xAAAA
        mock_lib.bethkit_group_child_as_group.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = Group(0xDEAD, Plugin.__new__(Plugin))

        # when
        children = list(group)

        # then
        assert len(children) == 2
        assert isinstance(children[0], Record)
        assert isinstance(children[1], Group)

