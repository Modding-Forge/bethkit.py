"""
Copyright (c) Modding Forge

Hatch build hook that bundles the native ``bethkit_ffi`` shared library into
the platform wheel.

During ``uv build`` / ``hatch build``:

1. The platform-appropriate shared library is located in the sibling
   ``bethkit/target/release/`` directory (produced by
   ``cargo build --release -p bethkit-ffi``).
   The ``BETHKIT_LIB`` environment variable can override the search path.
2. The library is copied into ``src/bethkit/`` so it lands next to the Python
   modules inside the wheel.  It is removed again in ``finalize()`` to keep
   the source tree clean.  If ``BETHKIT_LIB`` already points into
   ``src/bethkit/`` (as the CI workflow does), the copy is skipped.
3. The wheel tag is set to the current platform so pip installs only the
   compatible wheel.

If the library cannot be found (e.g. pure-sdist build), the hook exits
gracefully and the wheel is built without a native library.
"""

from __future__ import annotations

import os
import platform
import shutil
import sys
from pathlib import Path
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


def _dll_name() -> str:
    """Return the platform-appropriate shared library filename."""
    if sys.platform == "win32":
        return "bethkit_ffi.dll"
    if sys.platform == "darwin":
        return "libbethkit_ffi.dylib"
    return "libbethkit_ffi.so"


def _wheel_tag() -> str:
    """Return a PEP 425 platform tag string for the current machine."""
    if sys.platform == "win32":
        machine = platform.machine().lower()
        arch = "win_amd64" if machine in ("amd64", "x86_64") else "win32"
        return f"py3-none-{arch}"
    if sys.platform == "darwin":
        mac_ver = platform.mac_ver()[0].replace(".", "_")
        machine = platform.machine().lower()
        arch = "arm64" if machine == "arm64" else "x86_64"
        return f"py3-none-macosx_{mac_ver}_{arch}"
    machine = platform.machine().lower()
    arch = "x86_64" if machine in ("x86_64", "amd64") else machine
    return f"py3-none-linux_{arch}"


class CustomBuildHook(BuildHookInterface):
    """Hatch build hook: bundles the native library and regenerates stubs."""

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        """Copy the shared library into the package and set the platform tag.

        Args:
            version: Package version string passed by Hatch.
            build_data: Mutable build metadata dict.
        """
        root = Path(self.root).resolve()
        rust_root = root.parent / "bethkit"

        dll_name = _dll_name()

        # Allow explicit override via environment variable.
        env_lib = os.environ.get("BETHKIT_LIB")
        if env_lib:
            dll_src = Path(env_lib)
        else:
            dll_src = rust_root / "target" / "release" / dll_name

        self._copied_dll: Path | None = None

        if dll_src.exists():
            dest = root / "src" / "bethkit" / dll_name
            # Only copy when source and destination differ (e.g. BETHKIT_LIB
            # already points into src/bethkit/ as the CI workflow does).
            if dll_src.resolve() != dest.resolve():
                shutil.copy2(dll_src, dest)
                self._copied_dll = dest
            # Always register as an artifact so hatchling includes it even
            # when the file is gitignored.
            build_data.setdefault("artifacts", []).append(str(dest))
            build_data["pure-python"] = False
            build_data["tag"] = _wheel_tag()
            print(f"Bundling {dll_src.name} → {dest}", flush=True)
        else:
            print(
                f"Shared library not found at {dll_src} — "
                "wheel will not contain a native library.",
                flush=True,
            )

    def finalize(
        self,
        version: str,
        build_data: dict[str, Any],
        artifact_path: str,
    ) -> None:
        """Remove the temporary DLL copy from the source tree.

        Args:
            version: Package version string passed by Hatch.
            build_data: Build metadata dict.
            artifact_path: Path to the built wheel or sdist.
        """
        if self._copied_dll and self._copied_dll.exists():
            self._copied_dll.unlink()
            print(f"Cleaned up temporary {self._copied_dll.name}", flush=True)
