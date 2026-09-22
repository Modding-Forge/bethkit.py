# bethkit.py

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)](https://www.python.org) [![PyPI](https://img.shields.io/pypi/v/bethkit?logo=pypi&logoColor=white)](https://pypi.org/project/bethkit/)

Python bindings for [bethkit](https://github.com/Modding-Forge/bethkit), a Rust library for reading and writing Bethesda plugin and archive files. Python provides typed views and editing workflows; Bethkit remains responsible for binary formats, schema interpretation, and lossless writing.

Python 2.0 uses Bethkit 0.5.0, pinned together with its release artifacts in [native-source.json](native-source.json). Older native binaries, including Bethkit 0.4.0, do not provide all required functions. See [BUILDING.md](BUILDING.md) for source builds and release gates.

## Features

- **Plugin reading** - open `.esp`/`.esm`/`.esl` files by path or from in-memory bytes; iterate groups and records; look up records by FormID or EditorID; inspect sub-records
- **Plugin writing** - build new plugins from scratch with `PluginWriter`, `WritableGroup`, and `WritableRecord`
- **BSA / BA2 archives** - open and extract entries from BSA (TES4/SSE) and BA2 (GNRL/DX10) archives; write new archives with `BsaWriter`, `Ba2GnrlWriter`, and `Ba2Dx10Writer`
- **String tables** - read, edit, and write `.STRINGS`/`.DLSTRINGS`/`.ILSTRINGS` localisation files; apply translation sets with `LocalizationSet`
- **Typed records** - schema-generated, immutable models for all 134 Skyrim SE record definitions, with nested Quest stages, dialogue responses, and perk effects; models load only when requested.
- **Semantic editing** - edit typed fields through structural addresses, validate records, and patch existing plugins while preserving untouched record bytes.
- **Localization** - enumerate inline and external text by position, isolate changes to shared string IDs, and save a plugin together with its tables as a new output bundle.
- **Load-order utilities** - `LoadOrder`, `GlobalFormId`, and `PluginCache` for winning-override lookups and EditorID search across multiple plugins

## Requirements

| Requirement  | Version |
| ------------ | ------- |
| Python       | ≥ 3.10  |
| pydantic     | ≥ 2.5.3, < 3 |

Release wheels bundle the matching native library with the Skyrim SE schema only. Access the embedded package through `SchemaCatalog.embedded()` and `catalog.package(Game.SKYRIM_SE)`, or open an explicit `.bkschema` file as in the examples below. Local development requires the pinned native build. Generated types also check the exact schema payload hash; an ABI-compatible library alone does not make a different schema compatible.

Schema definitions originate in [xEdit](https://github.com/TES5Edit/TES5Edit) and are exported and published by [Modding-Forge/xDump](https://github.com/Modding-Forge/xDump). See [SCHEMA.md](SCHEMA.md) for coverage, provenance, generation, and current limitations.

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

### Reading and editing a typed quest

```python
from pathlib import Path

from bethkit import Game, Plugin, PluginPatcher, SchemaPackage, SemanticContext
from bethkit.records.skyrim_se import QuestRecord

with SchemaPackage.open(Path("skyrim_se.bkschema")) as package:
    with SemanticContext(package) as context:
        with Plugin.open(Path("MyMod.esp"), Game.SKYRIM_SE) as plugin:
            record = plugin.find_record(0x800)
            if record is None:
                raise LookupError("Quest 0x800 was not found")
            quest = QuestRecord.from_record(
                record, context, localized=plugin.is_localized
            )
            for stage in quest.stages:
                for entry in stage.log_entries:
                    print(entry.log_entry)
            with context.edit(record, localized=plugin.is_localized) as editor:
                editor.set(quest.field("editor_id"), "MyRenamedQuest")
                with editor.finish() as replacement:
                    with PluginPatcher(plugin) as patcher:
                        patcher.replace_record(record.form_id, replacement)
                        patcher.write_to_file(Path("MyMod-edited.esp"))
```

The generated view is read-only and remains usable after its source handles close. Edits use the native editor, including schema validation and callbacks. Structural changes require fresh addresses from `editor.snapshot()`; ordinary scalar or text-length changes retain their positions. The generic `RecordView` and `SemanticContext.snapshot()` remain available for inspectors and unknown fields.

### Editing localized text safely

```python
from pathlib import Path

from bethkit import (
    Game, LocalizationEditor, LocalizationSet, Plugin,
    SchemaPackage, SemanticContext,
)

source = Path("MyLocalizedMod.esp")
with SchemaPackage.open(Path("skyrim_se.bkschema")) as package:
    with SemanticContext(package) as context:
        with Plugin.open(source, Game.SKYRIM_SE) as plugin:
            with LocalizationSet.open(source, "english") as tables:
                with LocalizationEditor(plugin, context, tables) as editor:
                    for string in editor.iter_strings():
                        if string.text == "Old text":
                            editor.replace(string, "New text")
                    editor.save_bundle(
                        Path("edited-bundle"), source.name, language="english"
                    )
```

For an inline-string plugin, omit `tables`. A string's identity contains its plugin and structural position, never its text or external table ID. Replacing one external string allocates a fresh ID so other users of a shared ID are unchanged. Saving creates a new directory containing the plugin, its `Strings/` files, and a checksum manifest; it never overwrites an installed Data directory.

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

Unit tests mock the native boundary. A release-quality check must also set `BETHKIT_LIB` and `BETHKIT_SCHEMA` and run `pytest --require-native`; an explicitly configured but incompatible library is an error, not a skipped test. See [BUILDING.md](BUILDING.md) for the pinned workflow and [SCHEMA.md](SCHEMA.md) for deterministic model generation.

## Related projects

- [bethkit](https://github.com/Modding-Forge/bethkit) - the underlying Rust library; `bethkit.py` wraps its C ABI

## License

Apache-2.0 - see [LICENSE](LICENSE).
