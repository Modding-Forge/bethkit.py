"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import math
import struct
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitNativeError,
    BethkitOwnershipError,
    Game,
    Plugin,
    PluginKind,
    PluginWriter,
    WritableGroup,
    WritableRecord,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestPluginWriter:
    """Tests ``bethkit.plugin.writer.PluginWriter``."""

    def test_header_setters_delegate_to_native(
        self, mock_lib: MagicMock
    ) -> None:
        """Passes master, description, and localization metadata explicitly."""

        # given
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_plugin_writer_add_master.return_value = 0
        mock_lib.bethkit_plugin_writer_set_description.return_value = 0
        mock_lib.bethkit_plugin_writer_set_localized.return_value = 0

        # when
        with PluginWriter(Game.SKYRIM_SE) as writer:
            writer.add_master("Skyrim.esm")
            writer.set_description("A test plugin")
            writer.set_localized(True)

        # then
        mock_lib.bethkit_plugin_writer_add_master.assert_called_once_with(
            0xCCCC, b"Skyrim.esm"
        )
        mock_lib.bethkit_plugin_writer_set_description.assert_called_once_with(
            0xCCCC, b"A test plugin"
        )
        mock_lib.bethkit_plugin_writer_set_localized.assert_called_once_with(
            0xCCCC, True
        )

    def test_header_setters_reject_closed_writer(
        self, mock_lib: MagicMock
    ) -> None:
        """Does not mutate native state after the writer closes."""

        # given
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        writer = PluginWriter(Game.SKYRIM_SE)
        writer.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            writer.add_master("Skyrim.esm")
        with pytest.raises(BethkitClosedError):
            writer.set_description("A test plugin")
        with pytest.raises(BethkitClosedError):
            writer.set_localized(True)
        mock_lib.bethkit_plugin_writer_add_master.assert_not_called()
        mock_lib.bethkit_plugin_writer_set_description.assert_not_called()
        mock_lib.bethkit_plugin_writer_set_localized.assert_not_called()

    @pytest.mark.integration
    def test_header_setters_round_trip(self) -> None:
        """Reads all configured header metadata through the native parser."""

        # given
        with PluginWriter(Game.SKYRIM_SE) as writer:
            writer.add_master("Skyrim.esm")
            writer.set_description("Localization fixture")
            writer.set_localized(True)

            # when
            data = writer.write_to_bytes()

        # then
        with Plugin.from_bytes(data, Game.SKYRIM_SE) as plugin:
            assert plugin.masters == ["Skyrim.esm"]
            assert plugin.description == "Localization fixture"
            assert plugin.is_localized

    def test_constructor_calls_writer_new(self, mocker: MockerFixture) -> None:
        """Tests that __init__ calls bethkit_plugin_writer_new with game int."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        writer = PluginWriter(Game.SKYRIM_SE)

        # then
        call_args = mock_lib.bethkit_plugin_writer_new.call_args
        assert call_args is not None
        game_arg, _hedr_arg = call_args.args
        assert game_arg == int(Game.SKYRIM_SE)
        writer.close()

    def test_constructor_raises_on_null_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that __init__ raises BethkitNativeError when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"writer error"
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when / then
        with pytest.raises(BethkitNativeError):
            PluginWriter(Game.SKYRIM_SE)

    def test_context_manager_frees_on_exit(self, mocker: MockerFixture) -> None:
        """Tests that __exit__ calls bethkit_plugin_writer_free."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginWriter(Game.SKYRIM_SE):
            pass

        # then
        mock_lib.bethkit_plugin_writer_free.assert_called_once_with(0xCCCC)

    def test_add_group_transfers_group_ownership(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_group() takes ownership of the WritableGroup."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mock_lib.bethkit_plugin_writer_add_group.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        group = WritableGroup.new(b"NPC_")

        # when
        with PluginWriter(Game.SKYRIM_SE) as writer:
            writer.add_group(group)

        # then — group must be invalidated
        with pytest.raises(BethkitOwnershipError):
            group._transfer_ptr()

    def test_close_prevents_add_group(self, mocker: MockerFixture) -> None:
        """Tests that add_group() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        writer = PluginWriter(Game.SKYRIM_SE)
        writer.close()
        group = WritableGroup.new(b"NPC_")

        # when / then
        with pytest.raises(BethkitClosedError):
            writer.add_group(group)
        group.close()

    def test_write_to_file_calls_native(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Tests that file output delegates to the native writer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mock_lib.bethkit_plugin_writer_write_to_file.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginWriter(Game.SKYRIM_SE) as writer:
            writer.write_to_file(tmp_path / "out.esp")

        # then
        mock_lib.bethkit_plugin_writer_write_to_file.assert_called_once()

    def test_write_to_file_raises_after_close(
        self, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        """Rejects file serialization after closing the writer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        writer = PluginWriter(Game.SKYRIM_SE)
        writer.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            writer.write_to_file(tmp_path / "out.esp")

    def test_write_to_bytes_returns_bytes(self, mocker: MockerFixture) -> None:
        """Tests that write_to_bytes() returns a bytes object."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        fake_ptr: int = 0xDDDD
        mock_lib.bethkit_plugin_writer_write_to_bytes.return_value = fake_ptr
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        mocker.patch("ctypes.string_at", return_value=b"\x54\x45\x53\x34")

        # when
        with PluginWriter(Game.SKYRIM_SE) as writer:
            result = writer.write_to_bytes()

        # then
        assert isinstance(result, bytes)
        mock_lib.bethkit_bytes_free.assert_called_once()

    def test_write_to_bytes_raises_after_close(
        self, mocker: MockerFixture
    ) -> None:
        """Rejects byte serialization after closing the writer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        writer = PluginWriter(Game.SKYRIM_SE)
        writer.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            writer.write_to_bytes()

    def test_default_hedr_version_skyrim_se(
        self, mocker: MockerFixture
    ) -> None:
        """Defaults to HEDR version 1.7 for Skyrim SE."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginWriter(Game.SKYRIM_SE):
            pass

        # then
        _game, hedr = mock_lib.bethkit_plugin_writer_new.call_args.args
        assert math.isclose(hedr, 1.7, abs_tol=1e-4)

    def test_default_hedr_version_fallout4(self, mocker: MockerFixture) -> None:
        """Defaults to HEDR version 0.95 for Fallout 4."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginWriter(Game.FALLOUT4):
            pass

        # then
        _game, hedr = mock_lib.bethkit_plugin_writer_new.call_args.args
        assert math.isclose(hedr, 0.95, abs_tol=1e-4)

    def test_explicit_hedr_version_is_forwarded(
        self, mocker: MockerFixture
    ) -> None:
        """Preserves an explicit HEDR version instead of the game default."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_plugin_writer_new.return_value = 0xCCCC
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        with PluginWriter(Game.SKYRIM_SE, hedr_version=1.71):
            pass

        # then
        _game, hedr = mock_lib.bethkit_plugin_writer_new.call_args.args
        assert math.isclose(hedr, 1.71, abs_tol=1e-4)

    @pytest.mark.integration
    def test_round_trip_produces_correct_hedr_version(self) -> None:
        """Integration: PluginWriter serialises the correct HEDR version.

        Writes an empty SSE plugin via PluginWriter, then reads the
        raw HEDR float from the serialised bytes to confirm it equals 1.7
        and not 44.0 (the former incorrect default).

        Requires the real bethkit_ffi library.
        """

        # given
        with PluginWriter(Game.SKYRIM_SE) as writer:
            data = writer.write_to_bytes()

        # when — HEDR subrecord starts at byte 32 inside the TES4 record.
        # Layout: TES4(4) + data_size(4) + flags(4) + form_id(4) +
        #         vc(4) + form_version(2) + unknown(2) = 24 B header,
        #         then first subrecord: "HEDR"(4) + size(2) = 6 B, then data.
        hedr_value: float = struct.unpack_from("<f", data, 30)[0]

        # then
        assert math.isclose(hedr_value, 1.7, abs_tol=0.01)

    @pytest.mark.integration
    def test_round_trip_write_then_parse(self) -> None:
        """Integration: a plugin written by PluginWriter can be parsed back.

        Writes a minimal SSE plugin with one NPC_ group containing one
        record, then re-parses the bytes and verifies the structure.

        Requires the real bethkit_ffi library.
        """

        # given — build a minimal plugin in-memory
        with WritableRecord.new(b"NPC_", form_id=0x000D62) as rec:
            rec.add_subrecord(b"EDID", b"TestNPC\x00")
            with WritableGroup.new(b"NPC_") as grp:
                grp.add_record(rec)
                with PluginWriter(Game.SKYRIM_SE) as writer:
                    writer.add_group(grp)
                    data = writer.write_to_bytes()

        # when
        with Plugin.from_bytes(data, Game.SKYRIM_SE) as plugin:
            kind = plugin.kind
            group_count = plugin.group_count

        # then
        assert kind == PluginKind.FULL
        assert group_count == 1
