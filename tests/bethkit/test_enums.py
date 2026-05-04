"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

from bethkit import (
    Ba2Version,
    BsaVersion,
    FieldValueKind,
    Game,
    PluginKind,
    StringFileKind,
)


class TestGame:
    """Tests ``bethkit.enums.Game``."""

    def test_is_int_enum(self) -> None:
        """Tests that Game members are ints."""

        assert isinstance(Game.SKYRIM_SE, int)

    def test_skyrim_se_distinct_from_skyrim(self) -> None:
        """Tests that SKYRIM_SE (64-bit) and SKYRIM (32-bit) differ."""

        assert Game.SKYRIM_SE != Game.SKYRIM

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

    def test_sse_is_3(self) -> None:
        """Tests that BsaVersion.SSE has integer value 3."""

        assert BsaVersion.SSE == 3

    def test_tes4_is_1(self) -> None:
        """Tests that BsaVersion.TES4 has integer value 1."""

        assert BsaVersion.TES4 == 1

    def test_sse_greater_than_tes4(self) -> None:
        """Tests that SSE version selector is larger than TES4."""

        assert BsaVersion.SSE > BsaVersion.TES4


class TestBa2Version:
    """Tests ``bethkit.enums.Ba2Version``."""

    def test_v1_is_int(self) -> None:
        """Tests that Ba2Version.V1 is an integer."""

        assert isinstance(Ba2Version.V1, int)

    def test_v7_differs_from_v1(self) -> None:
        """Tests that V7 and V1 have different values."""

        assert Ba2Version.V7 != Ba2Version.V1


class TestStringFileKind:
    """Tests ``bethkit.enums.StringFileKind``."""

    def test_strings_is_int(self) -> None:
        """Tests that StringFileKind.STRINGS is an int."""

        assert isinstance(StringFileKind.STRINGS, int)

    def test_all_kinds_are_distinct(self) -> None:
        """Tests that all StringFileKind members have distinct values."""

        kinds = [
            StringFileKind.STRINGS,
            StringFileKind.DL_STRINGS,
            StringFileKind.IL_STRINGS,
        ]
        assert len(set(kinds)) == len(kinds)


class TestFieldValueKind:
    """Tests ``bethkit.enums.FieldValueKind``."""

    def test_is_int_enum(self) -> None:
        """Tests that FieldValueKind members are ints."""

        assert isinstance(FieldValueKind.INT, int)

    def test_int_is_zero(self) -> None:
        """Tests that FieldValueKind.INT has integer value 0."""

        assert FieldValueKind.INT == 0

    def test_float_is_one(self) -> None:
        """Tests that FieldValueKind.FLOAT has integer value 1."""

        assert FieldValueKind.FLOAT == 1

    def test_missing_is_eleven(self) -> None:
        """Tests that FieldValueKind.MISSING has integer value 11."""

        assert FieldValueKind.MISSING == 11

    def test_roundtrip_from_int(self) -> None:
        """Tests that FieldValueKind can be constructed from its integer value."""

        # given
        value: int = FieldValueKind.STR.value

        # when
        reconstructed = FieldValueKind(value)

        # then
        assert reconstructed == FieldValueKind.STR

    def test_all_members_distinct(self) -> None:
        """Tests that all FieldValueKind members have distinct integer values."""

        values = [fvk.value for fvk in FieldValueKind]
        assert len(set(values)) == len(values)
