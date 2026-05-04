# bethkit.py

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)](https://www.python.org) [![PyPI](https://img.shields.io/pypi/v/bethkit?logo=pypi&logoColor=white)](https://pypi.org/project/bethkit/)

Python bindings for [bethkit](https://github.com/Modding-Forge/bethkit) - a fast Rust library for reading and writing Bethesda game plugin and archive files. `bethkit.py` wraps the `bethkit_ffi` C ABI via `ctypes`; no compiler or build tools required.

## Features

- **Plugin reading** - open `.esp`/`.esm`/`.esl` files by path or from in-memory bytes; iterate groups and records; look up records by FormID or EditorID; inspect sub-records
- **Plugin writing** - build new plugins from scratch with `PluginWriter`, `WritableGroup`, and `WritableRecord`
- **BSA / BA2 archives** - open and extract entries from BSA (TES4/SSE) and BA2 (GNRL/DX10) archives; write new archives with `BsaWriter`, `Ba2GnrlWriter`, and `Ba2Dx10Writer`
- **String tables** - read, edit, and write `.STRINGS`/`.DLSTRINGS`/`.ILSTRINGS` localisation files; apply translation sets with `LocalizationSet`
- **Schema** - decode sub-records into typed `FieldValue` variants (integers, floats, FormIDs, enums with resolved names, flags, structs, arrays) via `RecordView` and `SchemaRegistry`
- **Load-order utilities** - `LoadOrder`, `GlobalFormId`, and `PluginCache` for winning-override lookups and EditorID search across multiple plugins

## Requirements

| Requirement  | Version  |
| ------------ | -------- |
| Python       | ≥ 3.10  |
| pydantic     | ≥ 2.0   |
| bethkit\_ffi | matching |

Place `bethkit_ffi.dll` (Windows), `libbethkit_ffi.so` (Linux), or `libbethkit_ffi.dylib` (macOS) next to the package, or set the `BETHKIT_LIB` environment variable to the full path of the library.

## Installation

```sh
uv add bethkit
```

or

```sh
pip install bethkit
```

## Quick Start

### Reading a plugin

```python
from pathlib import Path
from bethkit import Plugin, Game

with Plugin.open(Path("Ordinator - Perks of Skyrim.esp"), Game.SKYRIM_SE) as plugin:
    print("Masters:", plugin.masters)
    print("Kind:", plugin.kind)

    for group in plugin:
        for child in group:
            if hasattr(child, "form_id"):
                print(f"  0x{child.form_id:08X}  {child.editor_id}")
```

### Building a plugin from scratch

```python
from pathlib import Path
from bethkit import Game, PluginWriter, WritableGroup, WritableRecord

with PluginWriter(Game.SKYRIM_SE) as writer:
    with WritableGroup.new(b"NPC_") as group:
        rec = WritableRecord.new(b"NPC_", form_id=0x000D62)
        rec.add_subrecord(b"EDID", b"MyNPC\x00")
        group.add_record(rec)
        writer.add_group(group)
    writer.write_to_file(Path("MyMod.esp"))
```

### Extracting from an archive

```python
from pathlib import Path
from bethkit import Archive

with Archive.open(Path("Skyrim - Meshes.bsa")) as arc:
    data = arc.extract("meshes/actors/character/character assets/skeleton.nif")
    if data:
        Path("skeleton.nif").write_bytes(data)
```

### Load-order and FormID resolution

```python
from pathlib import Path
from bethkit import Game, Plugin, PluginCache, PluginKind, LoadOrder

lo = LoadOrder()
lo.push("Skyrim.esm", PluginKind.FULL)
lo.push("MyMod.esp", PluginKind.FULL)

cache = PluginCache()
cache.add("Skyrim.esm", Plugin.open(Path("Skyrim.esm"), Game.SKYRIM_SE))

hit = cache.find_by_editor_id("ArmorIronCuirass")
if hit:
    print(hit.global_form_id)   # Skyrim.esm:0x012E49
    print(hit.record.editor_id)
```

## Development

```sh
git clone https://github.com/Modding-Forge/bethkit.py
cd bethkit.py
uv sync --extra dev
uv run pytest
```

Linting and type-checking:

```sh
uv tool run ruff check src/ tests/
uv tool run pyright src/ tests/
```

## Related projects

- [bethkit](https://github.com/Modding-Forge/bethkit) - the underlying Rust library; `bethkit.py` wraps its C ABI
- [SSE-Auto-Translator](https://github.com/Modding-Forge/SSE-Auto-Translator) - uses `bethkit.py` to patch localised strings

## License

Apache-2.0 - see [LICENSE](LICENSE).
