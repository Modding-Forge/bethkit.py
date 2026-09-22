"""
Copyright (c) Modding Forge
"""

# Validates and includes the native library without modifying the source tree.

from __future__ import annotations

import ast
import ctypes
import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

from hatchling.builders.config import BuilderConfig
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


def _dll_name() -> str:
    """Returns the shared-library filename for the current platform."""

    if sys.platform == "win32":
        return "bethkit_ffi.dll"
    if sys.platform == "darwin":
        return "libbethkit_ffi.dylib"
    return "libbethkit_ffi.so"


def _wheel_tag() -> str:
    """Returns a wheel platform tag without claiming a manylinux ABI."""

    machine = platform.machine().lower()
    if sys.platform == "win32":
        architecture = (
            "win_amd64" if machine in ("amd64", "x86_64") else "win32"
        )
        return f"py3-none-{architecture}"
    if sys.platform == "darwin":
        version = platform.mac_ver()[0].replace(".", "_")
        architecture = "arm64" if machine == "arm64" else "x86_64"
        return f"py3-none-macosx_{version}_{architecture}"
    architecture = "x86_64" if machine in ("x86_64", "amd64") else machine
    return f"py3-none-linux_{architecture}"


def _required_symbols(root: Path) -> set[str]:
    """Reads required exports without importing the binding declarations.

    Args:
        root: Python project directory containing the binding source.

    Returns:
        The complete set of native function names used by the bindings.
    """

    declarations = root / "src" / "bethkit" / "_ffi"
    return {
        node.attr
        for path in declarations.rglob("*.py")
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8")))
        if isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id in {"lib", "loaded"}
        and node.attr.startswith("bethkit_")
    }


def _validate_embedded_schema(library: ctypes.CDLL) -> None:
    """Verifies that the bundled runtime includes the promised Skyrim SE schema.

    Args:
        library: Loaded library whose required exports have been verified.

    Raises:
        RuntimeError: The embedded catalog or Skyrim SE package is unavailable.
    """

    library.bethkit_schema_catalog_embedded.restype = ctypes.c_void_p
    library.bethkit_schema_catalog_embedded.argtypes = []
    library.bethkit_schema_catalog_package.restype = ctypes.c_void_p
    library.bethkit_schema_catalog_package.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int32,
    ]
    library.bethkit_schema_catalog_free.restype = None
    library.bethkit_schema_catalog_free.argtypes = [ctypes.c_void_p]
    library.bethkit_schema_package_free.restype = None
    library.bethkit_schema_package_free.argtypes = [ctypes.c_void_p]

    catalog: Optional[int] = library.bethkit_schema_catalog_embedded()
    if not catalog:
        raise RuntimeError(
            "Native library lacks a valid embedded schema catalog. "
            "Rebuild with the schema-skyrim-se feature before creating a wheel."
        )
    try:
        # Skyrim Special Edition is game 1 in the stable C ABI.
        package: Optional[int] = library.bethkit_schema_catalog_package(
            catalog, 1
        )
        if not package:
            raise RuntimeError(
                "Native library lacks the embedded Skyrim SE schema package. "
                "Rebuild with schema-skyrim-se before wheel creation."
            )
        library.bethkit_schema_package_free(package)
    finally:
        library.bethkit_schema_catalog_free(catalog)


def _validate_library(path: Path, root: Path) -> None:
    """Rejects missing, incompatible, or incomplete native libraries.

    Args:
        path: Absolute path to the native library that will be bundled.
        root: Python project directory containing the binding declarations.

    Raises:
        RuntimeError: Loading fails or required ABI, exports, or schemas differ.
    """

    if not path.is_file():
        raise RuntimeError(
            f"Native library not found: {path}. "
            "Build the pinned native revision or set BETHKIT_LIB to a "
            "compatible library before building a wheel."
        )
    try:
        library = ctypes.CDLL(str(path))
        version_function = library.bethkit_abi_version
        version_function.restype = ctypes.c_uint32
        version_function.argtypes = []
        version = int(version_function())
        if version != 2:
            raise RuntimeError(f"Expected Bethkit ABI 2, got {version}: {path}")
        missing = sorted(
            name
            for name in _required_symbols(root)
            if getattr(library, name, None) is None
        )
        if missing:
            raise RuntimeError(
                f"Native library lacks required exports: {', '.join(missing)}. "
                "Use the revision pinned in native-source.json."
            )
        _validate_embedded_schema(library)
    except (OSError, AttributeError) as error:
        raise RuntimeError(
            f"Cannot load a compatible native library: {path}"
        ) from error


def _validate_file_lengths(root: Path) -> None:
    """Blocks every build variant when the source violates its line policy.

    Args:
        root: Project or extracted source-distribution directory.

    Raises:
        RuntimeError: The checker is missing, cannot run, or rejects the source.
    """

    checker = root / "scripts" / "check_file_lengths.py"
    if not checker.is_file():
        raise RuntimeError(
            f"Required file-length checker is missing: {checker}"
        )
    try:
        result = subprocess.run(
            [sys.executable, str(checker), "--root", str(root)],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
    except OSError as error:
        raise RuntimeError(
            "Cannot execute the file-length policy check."
        ) from error
    if result.returncode:
        details = "\n".join(
            value.strip() for value in (result.stdout, result.stderr) if value
        )
        raise RuntimeError(f"File-length policy blocks this build:\n{details}")


class CustomBuildHook(BuildHookInterface[BuilderConfig]):
    """Bundles validated native libraries into non-editable platform wheels."""

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        """Adds the native artifact without copying or deleting package files.

        Args:
            version: Build variant supplied by Hatch.
            build_data: Hatch's extensible build metadata dictionary.

        Raises:
            RuntimeError: Source length policy or native compatibility fails.
        """

        root = Path(self.root).resolve()
        _validate_file_lengths(root)
        if self.target_name == "sdist":
            # Source-only builds must retain the same gate without Git metadata.
            includes = build_data.setdefault("force_include", {})
            for relative in (
                "scripts/hatch_build.py",
                "scripts/check_file_lengths.py",
                "scripts/_file_length_text.py",
                "scripts/_file_length_archive.py",
                "file-length-policy.json",
            ):
                includes[str(root / relative)] = relative
            return
        if self.target_name != "wheel" or version == "editable":
            return
        configured = os.environ.get("BETHKIT_LIB")
        library = (
            Path(configured)
            if configured
            else root.parent / "bethkit" / "target" / "release" / _dll_name()
        ).resolve()
        _validate_library(library, root)
        # Hatch defines this extensible dictionary with Any-valued entries.
        build_data.setdefault("force_include", {})[str(library)] = (
            f"bethkit/{_dll_name()}"
        )
        build_data["force_include"][str(root / "native-source.json")] = (
            "bethkit/native-source.json"
        )
        build_data["pure_python"] = False
        build_data["tag"] = _wheel_tag()
