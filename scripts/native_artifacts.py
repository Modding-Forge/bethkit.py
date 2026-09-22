"""
Copyright (c) Modding Forge
"""

# Validates pinned native inputs and prepares reproducible CI artifacts.

from __future__ import annotations

import argparse
import hashlib
import io
import os
import urllib.request
import zipfile
from pathlib import Path
from typing import Literal, Optional

import pydantic


class ReleaseAsset(pydantic.BaseModel):
    """An explicitly selected and checksum-pinned native release archive."""

    model_config = pydantic.ConfigDict(frozen=True, extra="forbid")
    filename: str = pydantic.Field(pattern=r"^[A-Za-z0-9_.-]+\.zip$")
    """Exact GitHub release asset filename."""
    sha256: str = pydantic.Field(pattern=r"^[a-f0-9]{64}$")
    """Expected SHA-256 of the complete downloaded archive."""


class NativeRelease(pydantic.BaseModel):
    """A published native release explicitly approved for Python packaging."""

    model_config = pydantic.ConfigDict(frozen=True, extra="forbid")
    tag: str = pydantic.Field(pattern=r"^v[0-9][A-Za-z0-9_.-]*$")
    """Exact release tag, never a mutable latest alias."""
    assets: dict[Literal["windows-x64", "linux-x64"], ReleaseAsset]
    """Checksums for every supported platform."""


class NativeSource(pydantic.BaseModel):
    """Native source revision and optional published-release contract."""

    model_config = pydantic.ConfigDict(frozen=True, extra="forbid")
    format_version: Literal[1]
    """Manifest format understood by this script."""
    repository: Literal["Modding-Forge/bethkit"]
    """Upstream native repository to check out and download from."""
    revision: str = pydantic.Field(pattern=r"^[a-f0-9]{40}$")
    """Immutable source commit required by this Python revision."""
    schema_sha256: str = pydantic.Field(pattern=r"^[a-f0-9]{64}$")
    """Expected file checksum of the Skyrim SE schema."""
    release: Optional[NativeRelease]
    """Published release, or null while the required API is unreleased."""


def load_source(path: Path) -> NativeSource:
    """Loads and validates the native contract.

    Args:
        path: Path to native-source.json.

    Returns:
        Validated source and release pins.

    Raises:
        OSError: The manifest cannot be read.
        pydantic.ValidationError: The manifest is invalid.
    """

    return NativeSource.model_validate_json(path.read_text(encoding="utf-8"))


def require_release(source: NativeSource) -> NativeRelease:
    """Rejects publication until a real native release has been pinned.

    Args:
        source: Validated native source contract.

    Returns:
        The configured published release.

    Raises:
        RuntimeError: No release is configured or a platform pin is missing.
    """

    release = source.release
    if release is None:
        raise RuntimeError(
            "Python publication is blocked: the required native API is "
            "unreleased. Publish the pinned Bethkit revision, then set an "
            "explicit release tag and platform ZIP SHA-256 values in "
            "native-source.json. No latest-release fallback is allowed."
        )
    if set(release.assets) != {"windows-x64", "linux-x64"}:
        raise RuntimeError(
            "The native release must pin both platform archives."
        )
    return release


def configure_environment(
    library: Path, schema: Path, source: NativeSource
) -> None:
    """Exports explicit native paths after checking library and schema presence.

    Args:
        library: Existing platform shared library.
        schema: Existing Skyrim SE schema.
        source: Expected schema and source pins.

    Raises:
        RuntimeError: An artifact is missing or the schema checksum differs.
    """

    library = library.resolve()
    schema = schema.resolve()
    if not library.is_file() or not schema.is_file():
        raise RuntimeError("Both the native library and schema must exist.")
    if hashlib.sha256(schema.read_bytes()).hexdigest() != source.schema_sha256:
        raise RuntimeError("Skyrim SE schema checksum does not match the pin.")
    values = f"BETHKIT_LIB={library}\nBETHKIT_SCHEMA={schema}\n"
    environment_file = os.environ.get("GITHUB_ENV")
    if environment_file:
        with Path(environment_file).open("a", encoding="utf-8") as stream:
            stream.write(values)
    else:
        print(values, end="")


def fetch_release(
    source: NativeSource, platform_name: str, destination: Path
) -> None:
    """Downloads and extracts the exact checksum-pinned release.

    Args:
        source: Native source and release contract.
        platform_name: Supported wheel platform.
        destination: Directory receiving the DLL/shared object and schema.

    Raises:
        RuntimeError: The release, platform, or checksum is invalid.
        OSError: Downloading or writing fails.
        KeyError: Required root-level ZIP members are absent.
        zipfile.BadZipFile: The verified artifact is not a ZIP archive.
    """

    release = require_release(source)
    if platform_name not in ("windows-x64", "linux-x64"):
        raise RuntimeError(f"Unsupported native platform: {platform_name}")
    asset = release.assets[platform_name]
    url = (
        f"https://github.com/{source.repository}/releases/download/"
        f"{release.tag}/{asset.filename}"
    )
    request = urllib.request.Request(
        url, headers={"User-Agent": "bethkit-python-ci"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        payload: bytes = response.read()
    if hashlib.sha256(payload).hexdigest() != asset.sha256:
        raise RuntimeError(
            f"Native archive checksum mismatch: {asset.filename}"
        )
    library_name = (
        "bethkit_ffi.dll"
        if platform_name == "windows-x64"
        else "libbethkit_ffi.so"
    )
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        library_bytes = archive.read(library_name)
        schema_bytes = archive.read("skyrim_se.bkschema")
    if hashlib.sha256(schema_bytes).hexdigest() != source.schema_sha256:
        raise RuntimeError("Release schema checksum does not match the pin.")
    destination.mkdir(parents=True, exist_ok=True)
    library = destination / library_name
    schema = destination / "skyrim_se.bkschema"
    library.write_bytes(library_bytes)
    schema.write_bytes(schema_bytes)
    configure_environment(library, schema, source)


def main() -> None:
    """Runs the requested native-input validation or preparation step."""

    parser = argparse.ArgumentParser(
        description="Prepare and validate pinned Bethkit native build inputs."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "native-source.json",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    describe = commands.add_parser("describe")
    describe.add_argument("--require-release", action="store_true")
    fetch = commands.add_parser("fetch-release")
    fetch.add_argument("--platform", required=True)
    fetch.add_argument("--destination", type=Path, required=True)
    configure = commands.add_parser("configure")
    configure.add_argument("--library", type=Path, required=True)
    configure.add_argument("--schema", type=Path, required=True)
    arguments = parser.parse_args()
    source = load_source(arguments.manifest)
    if arguments.command == "describe":
        if arguments.require_release:
            require_release(source)
        values = f"repository={source.repository}\nrevision={source.revision}\n"
        output_file = os.environ.get("GITHUB_OUTPUT")
        if output_file:
            with Path(output_file).open("a", encoding="utf-8") as stream:
                stream.write(values)
        else:
            print(values, end="")
    elif arguments.command == "fetch-release":
        fetch_release(source, arguments.platform, arguments.destination)
    else:
        configure_environment(arguments.library, arguments.schema, source)


if __name__ == "__main__":
    main()
