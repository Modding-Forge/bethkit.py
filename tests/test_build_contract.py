"""
Copyright (c) Modding Forge
"""

# Regression tests for fail-closed native packaging and publication gates.

from __future__ import annotations

import ctypes
from pathlib import Path
from typing import TYPE_CHECKING, Any
from unittest.mock import MagicMock

import pytest

from scripts import hatch_build, native_artifacts

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def _source() -> native_artifacts.NativeSource:
    """Returns an unreleased but immutable native source contract."""

    return native_artifacts.NativeSource(
        format_version=1,
        repository="Modding-Forge/bethkit",
        revision="1" * 40,
        schema_sha256="2" * 64,
        release=None,
    )


def _native_library(
    tmp_path: Path, mocker: MockerFixture
) -> tuple[Path, MagicMock]:
    """Mocks a compatible library without loading native code in unit tests.

    Args:
        tmp_path: Temporary directory for the artifact placeholder.
        mocker: Fixture providing restored ctypes and symbol-discovery patches.

    Returns:
        The artifact path and its configurable native-library mock.
    """

    path = tmp_path / "native.dll"
    path.write_bytes(b"fixture")
    native = MagicMock()
    native.bethkit_abi_version.return_value = 2
    native.bethkit_schema_catalog_embedded.return_value = 0x1000
    native.bethkit_schema_catalog_package.return_value = 0x2000
    mocker.patch.object(hatch_build.ctypes, "CDLL", return_value=native)
    mocker.patch.object(hatch_build, "_required_symbols", return_value=set())
    return path, native


class TestNativeReleaseContract:
    """Ensures unreleased and mismatched native inputs cannot be published."""

    def test_unreleased_pin_blocks_publication(self) -> None:
        """Rejects an explicit null release without guessing a newer tag."""

        with pytest.raises(
            RuntimeError, match="required native API is unreleased"
        ):
            native_artifacts.require_release(_source())

    def test_schema_hash_mismatch_blocks_environment(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Never exports artifact paths after a checksum failure."""

        library = tmp_path / "library.dll"
        schema = tmp_path / "schema.bkschema"
        environment = tmp_path / "environment"
        library.write_bytes(b"library")
        schema.write_bytes(b"unexpected schema")
        mocker.patch.dict("os.environ", {"GITHUB_ENV": str(environment)})
        with pytest.raises(RuntimeError, match="checksum"):
            native_artifacts.configure_environment(library, schema, _source())
        assert not environment.exists()


class TestNativeBuildHook:
    """Checks native compatibility and source-preserving wheel inclusion."""

    def test_missing_library_rejects_wheel(self, tmp_path: Path) -> None:
        """Does not silently produce a wheel without its runtime dependency."""

        with pytest.raises(RuntimeError, match="Native library not found"):
            hatch_build._validate_library(tmp_path / "missing.dll", tmp_path)

    def test_old_abi_is_rejected(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Rejects ABI 1 before checking or declaring newer function exports."""

        library = tmp_path / "old.dll"
        library.write_bytes(b"fixture")
        native = MagicMock()
        native.bethkit_abi_version.return_value = 1
        mocker.patch.object(hatch_build.ctypes, "CDLL", return_value=native)
        with pytest.raises(RuntimeError, match="Expected Bethkit ABI 2"):
            hatch_build._validate_library(library, tmp_path)

    def test_missing_export_is_rejected(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Rejects old ABI-2 builds lacking newly required functionality."""

        library = tmp_path / "old.dll"
        library.write_bytes(b"fixture")
        native = MagicMock()
        native.bethkit_abi_version.return_value = 2
        del native.bethkit_required_export
        mocker.patch.object(hatch_build.ctypes, "CDLL", return_value=native)
        mocker.patch.object(
            hatch_build,
            "_required_symbols",
            return_value={"bethkit_required_export"},
        )
        with pytest.raises(RuntimeError, match="lacks required exports"):
            hatch_build._validate_library(library, tmp_path)

    def test_wheel_inclusion_does_not_modify_source_files(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Includes the selected library without replacing package files."""

        library = tmp_path / "native" / hatch_build._dll_name()
        library.parent.mkdir()
        library.write_bytes(b"new library")
        package_library = tmp_path / "src" / "bethkit" / library.name
        package_library.parent.mkdir(parents=True)
        package_library.write_bytes(b"existing library")
        mocker.patch.dict("os.environ", {"BETHKIT_LIB": str(library)})
        validate = mocker.patch.object(hatch_build, "_validate_library")
        mocker.patch.object(hatch_build, "_validate_file_lengths")
        hook = hatch_build.CustomBuildHook(
            str(tmp_path), {}, MagicMock(), MagicMock(), str(tmp_path), "wheel"
        )
        build_data: dict[str, Any] = {}
        hook.initialize("standard", build_data)
        validate.assert_called_once_with(library, tmp_path)
        assert package_library.read_bytes() == b"existing library"
        assert library.read_bytes() == b"new library"
        assert build_data["pure_python"] is False
        assert build_data["force_include"][str(library)] == (
            f"bethkit/{library.name}"
        )

    def test_missing_embedded_catalog_rejects_wheel(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Rejects featureless builds despite matching ABI and exports."""

        # given
        path, native = _native_library(tmp_path, mocker)
        native.bethkit_schema_catalog_embedded.return_value = None

        # when
        with pytest.raises(RuntimeError, match="embedded schema catalog"):
            hatch_build._validate_library(path, tmp_path)

        # then
        native.bethkit_schema_catalog_package.assert_not_called()
        native.bethkit_schema_package_free.assert_not_called()
        native.bethkit_schema_catalog_free.assert_not_called()

    def test_missing_skyrim_package_frees_catalog_and_rejects_wheel(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Rejects other-game-only catalogs and releases their owned handle."""

        # given
        path, native = _native_library(tmp_path, mocker)
        native.bethkit_schema_catalog_package.return_value = None

        # when
        with pytest.raises(
            RuntimeError, match="embedded Skyrim SE schema package"
        ):
            hatch_build._validate_library(path, tmp_path)

        # then
        native.bethkit_schema_catalog_package.assert_called_once_with(0x1000, 1)
        native.bethkit_schema_package_free.assert_not_called()
        native.bethkit_schema_catalog_free.assert_called_once_with(0x1000)

    def test_embedded_schema_validation_declares_and_frees_owned_handles(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Preserves pointer widths and frees both handles after success."""

        # given
        path, native = _native_library(tmp_path, mocker)

        # when
        hatch_build._validate_library(path, tmp_path)

        # then
        assert native.bethkit_schema_catalog_embedded.restype is ctypes.c_void_p
        assert native.bethkit_schema_catalog_embedded.argtypes == []
        assert native.bethkit_schema_catalog_package.restype is ctypes.c_void_p
        assert native.bethkit_schema_catalog_package.argtypes == [
            ctypes.c_void_p,
            ctypes.c_int32,
        ]
        for function in (
            native.bethkit_schema_package_free,
            native.bethkit_schema_catalog_free,
        ):
            assert function.restype is None
            assert function.argtypes == [ctypes.c_void_p]
        native.bethkit_schema_catalog_package.assert_called_once_with(0x1000, 1)
        native.bethkit_schema_package_free.assert_called_once_with(0x2000)
        native.bethkit_schema_catalog_free.assert_called_once_with(0x1000)

    def test_editable_install_needs_no_native_library(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Allows developer setup before the native checkout has been built."""

        # given
        validate = mocker.patch.object(hatch_build, "_validate_library")
        mocker.patch.object(hatch_build, "_validate_file_lengths")
        hook = hatch_build.CustomBuildHook(
            str(tmp_path), {}, MagicMock(), MagicMock(), str(tmp_path), "wheel"
        )
        build_data: dict[str, Any] = {}

        # when
        hook.initialize("editable", build_data)

        # then
        validate.assert_not_called()
        assert build_data == {}

    def test_sdist_needs_no_native_library(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """Allows source distributions without claiming native wheel support."""

        validate = mocker.patch.object(hatch_build, "_validate_library")
        mocker.patch.object(hatch_build, "_validate_file_lengths")
        hook = hatch_build.CustomBuildHook(
            str(tmp_path), {}, MagicMock(), MagicMock(), str(tmp_path), "sdist"
        )
        hook.initialize("standard", {})
        validate.assert_not_called()
