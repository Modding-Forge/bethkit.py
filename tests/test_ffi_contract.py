"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from bethkit._ffi import _loader
from scripts import hatch_build

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestDeclarationInventory:
    """Keeps split declarations and the native packaging contract aligned."""

    def test_all_symbols_have_explicit_types(
        self, mocker: MockerFixture
    ) -> None:
        """Checks argument and return declarations across every ABI domain.

        Args:
            mocker: Factory for a native-library stand-in.
        """

        # given
        root = Path(__file__).resolve().parents[1]
        symbols = hatch_build._required_symbols(root)
        library = mocker.Mock()

        # when
        _loader._declare(library)

        # then
        assert {
            "bethkit_abi_version",
            "bethkit_archive_open",
            "bethkit_plugin_open",
            "bethkit_schema_package_graph_json",
            "bethkit_record_editor_set_at_json",
            "bethkit_localization_set_clone",
            "bethkit_load_order_new",
        } <= symbols
        for symbol in symbols:
            function = getattr(library, symbol)
            assert "restype" in vars(function), symbol
            assert isinstance(function.argtypes, list), symbol
        assert library.bethkit_string_free.restype is None
        assert library.bethkit_last_error.restype is ctypes.c_char_p
        assert (
            library.bethkit_schema_package_graph_json.restype is ctypes.c_void_p
        )

    def test_nested_declarations_are_discovered(self, tmp_path: Path) -> None:
        """Finds declarations even when a later refactor adds a subpackage.

        Args:
            tmp_path: Disposable project root.
        """

        path = tmp_path / "src" / "bethkit" / "_ffi" / "domain" / "types.py"
        path.parent.mkdir(parents=True)
        path.write_text("lib.bethkit_nested.restype = None\n", encoding="utf-8")
        assert hatch_build._required_symbols(tmp_path) == {"bethkit_nested"}


class TestNativeTextEncoding:
    """Rejects malformed C strings before they can be truncated natively."""

    @pytest.mark.parametrize("value", ["bad\0name", "bad\ud800name"])
    def test_strings_reject_invalid_input(self, value: str) -> None:
        """Rejects embedded NULs and unpaired surrogates.

        Args:
            value: Malformed native text argument.
        """

        with pytest.raises((ValueError, UnicodeEncodeError)):
            _loader.senc(value)

    def test_paths_reject_nul(self) -> None:
        """Does not silently shorten a filesystem path at a NUL byte."""

        with pytest.raises(ValueError, match="NUL"):
            _loader.enc(Path("bad\0name.esp"))
