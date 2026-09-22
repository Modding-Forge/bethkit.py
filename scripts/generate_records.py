"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from bethkit import _ffi
from bethkit.records import _schema

if __package__:
    from ._record_generator import RecordGenerator
else:
    from _record_generator import RecordGenerator


def generate(graph: _schema.SchemaGraph) -> dict[str, str]:
    """Compiles a complete game package without any dynamic type fallback.

    Args:
        graph: Validated, versioned native schema graph.

    Returns:
        Relative module filenames and deterministic source code.

    Raises:
        ValueError: A node cannot retain its full type information.
    """

    if graph.manifest.get("game") != "skyrim_se":
        raise ValueError(
            "This generator currently targets the Skyrim SE package."
        )
    if not graph.records:
        raise ValueError("The schema must contain at least one record.")
    files: dict[str, str] = {}
    exports: dict[str, str] = {}
    for record in sorted(graph.records, key=lambda r: r.signature):
        signature = bytes(record.signature).decode("ascii")
        if not re.fullmatch(r"[A-Z0-9_]{4}", signature):
            raise ValueError(f"Invalid record signature: {signature!r}")
        module = signature.lower().rstrip("_")
        if not module or module + ".py" in files:
            raise ValueError(f"Duplicate or empty record module: {module!r}")
        generator = RecordGenerator(record, graph.payload_sha256)
        name, source = generator.render()
        files[module + ".py"] = source
        if name in exports:
            raise ValueError(f"Duplicate public record class {name}")
        exports[name] = module
    init = [
        '"""',
        "Copyright (c) Modding Forge",
        '"""',
        "",
        "# Lazily loaded Skyrim SE record models generated from xEdit.",
        "",
        "from __future__ import annotations",
        "",
        "import importlib",
        "from typing import TYPE_CHECKING",
        "",
        "if TYPE_CHECKING:",
    ]
    for name, module in sorted(exports.items()):
        init.append(f"    from .{module} import {name} as {name}")
    init.extend(["", "_EXPORTS: dict[str, str] = {"])
    for name, module in sorted(exports.items()):
        init.append(f"    {name!r}: {module!r},")
    init.extend(
        [
            "}",
            "",
            "__all__ = " + repr(sorted(exports)),
            "",
            "",
            "def __getattr__(name: str) -> object:",
            '    """Loads only the requested record module.',
            "",
            "    Args:",
            "        name: Record class exported by this game package.",
            "",
            "    Returns:",
            "        The requested generated class.",
            "",
            "    Raises:",
            "        AttributeError: The class is not part of this schema.",
            '    """',
            "",
            "    if name not in _EXPORTS:",
            "        raise AttributeError(name)",
            "    module = importlib.import_module("
            'f"{__name__}.{_EXPORTS[name]}")',
            "    value: object = getattr(module, name)",
            "    globals()[name] = value",
            "    return value",
            "",
        ]
    )
    files["__init__.py"] = "\n".join(init)
    return files


def normalized_files(files: dict[str, str], ruff: Path) -> dict[str, str]:
    """Formats deterministic generated code using the project's Ruff rules.

    Args:
        files: Unformatted generated sources indexed by relative filename.
        ruff: Installed Ruff executable used both for generation and checks.

    Returns:
        Sources with unused imports removed and stable formatting applied.

    Raises:
        subprocess.CalledProcessError: Formatting or lint validation fails.
        OSError: Temporary source files or the Ruff executable are inaccessible.
    """

    config = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with tempfile.TemporaryDirectory(prefix="bethkit_models_") as directory:
        staging = Path(directory)
        for filename, source in files.items():
            (staging / filename).write_text(
                source, encoding="utf-8", newline="\n"
            )
        subprocess.run(
            [
                str(ruff),
                "check",
                "--config",
                str(config),
                "--select",
                "F401,I",
                "--fix",
                str(staging),
            ],
            check=True,
        )
        subprocess.run(
            [str(ruff), "format", "--config", str(config), str(staging)],
            check=True,
        )
        subprocess.run(
            [str(ruff), "check", "--config", str(config), str(staging)],
            check=True,
        )
        return {
            filename: (staging / filename).read_text("utf-8")
            for filename in files
        }


def verify_files(files: dict[str, str], output: Path) -> None:
    """Checks exact generated contents and rejects obsolete Python modules.

    Args:
        files: Expected relative filenames mapped to normalized source code.
        output: Checked-in game package directory to verify.

    Raises:
        SystemExit: A generated module differs, is missing, or is unexpected.
        OSError: Existing generated sources cannot be read.
    """

    actual = {
        path.relative_to(output).as_posix() for path in output.rglob("*.py")
    }
    unexpected = sorted(actual - files.keys())
    if unexpected:
        raise SystemExit(
            f"Unexpected generated models: {', '.join(unexpected)}"
        )
    for filename, source in sorted(files.items()):
        destination = output / filename
        if (
            not destination.is_file()
            or destination.read_text("utf-8") != source
        ):
            raise SystemExit(f"Generated model differs: {destination}")


def main() -> None:
    """Loads one native schema and regenerates or verifies its Python models.

    Raises:
        SystemExit: Arguments, dependencies, or generated files fail validation.
        BethkitNativeError: The native schema cannot be opened or exported.
        ValueError: Exported schema data is invalid or unsupported.
        OSError: Input or output files cannot be accessed.
        subprocess.CalledProcessError: Generated sources fail Ruff validation.
    """

    parser = argparse.ArgumentParser(
        description="Generate typed record views from a pinned native schema."
    )
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--ruff", type=Path, default=shutil.which("ruff"))
    arguments = parser.parse_args()
    schema_path: Path = arguments.schema
    output: Path = arguments.output
    lib = _ffi.load_lib()
    package = lib.bethkit_schema_package_open(_ffi.enc(schema_path))
    if not package:
        _ffi.raise_last_error(lib)
    try:
        pointer = lib.bethkit_schema_package_graph_json(package)
        if not pointer:
            _ffi.raise_last_error(lib)
        text = _ffi.copy_and_free_str(pointer, lib.bethkit_string_free, lib)
    finally:
        lib.bethkit_schema_package_free(package)
    graph = _schema.SchemaGraph.model_validate_json(text)
    if arguments.ruff is None:
        raise SystemExit(
            "Install the development Ruff dependency or pass --ruff."
        )
    files = normalized_files(generate(graph), Path(arguments.ruff))
    if arguments.check:
        verify_files(files, output)
    else:
        output.mkdir(parents=True, exist_ok=True)
        for filename, source in files.items():
            destination = output / filename
            destination.write_text(source, encoding="utf-8", newline="\n")
    digest = hashlib.sha256(schema_path.read_bytes()).hexdigest()
    print(
        f"{len(graph.records)} records; schema file SHA-256 {digest}; "
        f"payload {graph.payload_sha256}"
    )


if __name__ == "__main__":
    main()
