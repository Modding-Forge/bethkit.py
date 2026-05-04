"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

from bethkit import Ba2Version, BsaVersion, Game, PluginKind, StringFileKind


class TestGame:
    """Tests ``bethkit.enums.Game``."""

    def test_is_int_enum(self) -> None:
        """Tests that Game members are ints."""

        assert isinstance(Game.SKYRIM_SE, int)

    def test_skyrim_se_distinct_from_skyrim_le(self) -> None:
        """Tests that SKYRIM_SE and SKYRIM_LE have different integer values."""

        assert Game.SKYRIM_SE != Game.SKYRIM_LE

    def test_roundtrip_from_int(self) -> None:
        """Tests that Game can be constructed from its integer value."""

        # given
        value: int = Game.SKYRIM_SE.value

        # when
        reconstructed = Game(value)

        # then
        assert reconstructed == Game.SKYRIM_SE


class TestPluginKind:
    """Tests ``bethkit.enums.PluginKind``."""

    def test_full_is_zero(self) -> None:
        """Tests that PluginKind.FULL has integer value 0."""

        assert PluginKind.FULL == 0

    def test_light_differs_from_full(self) -> None:
        """Tests that LIGHT and FULL are different values."""

        assert PluginKind.LIGHT != PluginKind.FULL

    def test_overlay_differs_from_light(self) -> None:
        """Tests that OVERLAY and LIGHT are different values."""

        assert PluginKind.OVERLAY != PluginKind.LIGHT


class TestBsaVersion:
    """Tests ``bethkit.enums.BsaVersion``."""

    def test_sse_is_104(self) -> None:
        """Tests that BsaVersion.SSE equals 104."""

        assert BsaVersion.SSE == 104

    def test_tes4_is_103(self) -> None:
        """Tests that BsaVersion.TES4 equals 103."""

        assert BsaVersion.TES4 == 103

    def test_sse_greater_than_tes4(self) -> None:
        """Tests that SSE version number is larger than TES4."""

        assert BsaVersion.SSE > BsaVersion.TES4


class TestBa2Version:
    """Tests ``bethkit.enums.Ba2Version``."""

    def test_gnrl_is_int(self) -> None:
        """Tests that Ba2Version.GNRL is an integer."""

        assert isinstance(Ba2Version.GNRL, int)

    def test_dx10_differs_from_gnrl(self) -> None:
        """Tests that DX10 and GNRL are different values."""

        assert Ba2Version.DX10 != Ba2Version.GNRL


class TestStringFileKind:
    """Tests ``bethkit.enums.StringFileKind``."""

    def test_strings_is_int(self) -> None:
        """Tests that StringFileKind.STRINGS is an int."""

        assert isinstance(StringFileKind.STRINGS, int)

    def test_all_kinds_are_distinct(self) -> None:
        """Tests that STRINGS, DLSTRINGS and ILSTRINGS have distinct values."""

        kinds = [
            StringFileKind.STRINGS,
            StringFileKind.DLSTRINGS,
            StringFileKind.ILSTRINGS,
        ]
        assert len(set(kinds)) == len(kinds)
