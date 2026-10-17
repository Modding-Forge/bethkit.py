# bethkit.py

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)](https://www.python.org) [![PyPI](https://img.shields.io/pypi/v/bethkit?logo=pypi&logoColor=white)](https://pypi.org/project/bethkit/)

Python bindings for [bethkit](https://github.com/Modding-Forge/bethkit), a Rust library for reading and writing Bethesda plugin and archive files. Python provides typed views and editing workflows; Bethkit remains responsible for binary formats, schema interpretation, and lossless writing.

Published Python 2.4.1 uses Bethkit 0.9.0. This development branch pins a newer native source commit for in-memory string-table parsing; that API is not in the published wheels yet. Source-build inputs and release checksums are controlled by [native-source.json](native-source.json). See [BUILDING.md](BUILDING.md) for source builds and release gates.

`LocalizationEditor.save_bundle(output_dir, plugin_name, exist_ok=True)` allows an existing output directory. It replaces generated plugin, table and manifest files while preserving unrelated files. The default rejects existing directories. New bundles are published by one directory rename; merging into an existing directory is atomic per file, not transactional across the whole bundle. A failed merge can leave some files updated; retry the save to complete it. The manifest describes the current save, not other files already in the directory.

See [PERFORMANCE.md](PERFORMANCE.md) for measured real-corpus results, streaming batches, the explicit mixed heuristic, extraction-only traversal, and correctness boundaries. Updating an installed package alone does not opt an application's existing schema context into automatic detection.

## Features

For automatic plugin-specific inline decoding, create `SemanticContext.for_plugin(package, plugin, cpoverride=optional_path)`. An explicitly supplied `Path` to a `.cpoverride` file always wins; an unreadable or unsupported override fails without guessing. Without it, native Bethkit detects one codec from a bounded sample of schema-localizable strings and retains that choice for reading and localization editing. Inspect `context.encoding_decision` for the selected codec, decision source, and sample counts. The context must be reused only with its source plugin. This API requires Bethkit 0.8.0 or newer.

The preservation option `SemanticContext.for_plugin(package, plugin, preserve_undecodable=True)` keeps suspicious or weakly evidenced inline text as raw bytes instead of inventing decoded text. Such a `StringReference` has `text=None`, `raw_bytes`, and a `decoding_warning`, with a separately labeled `best_effort_text` preview. Ambiguous previews prefer Windows-1252 and log that unconfirmed choice; undefined bytes are shown as hex escapes. Explicit override codecs remain authoritative for previews too. Preserve these fields when caching, do not automatically translate previews, and select an explicit field codec before editing unresolved text. The conservative warning classifier can flag valid legacy strings; it is not proof of corruption. Typed record models still require resolved text.

Separately, `plugin.iter_strings(context, preserve_opaque_nontext=True, on_diagnostic=observer)` attempts full record validation but retains failed schema-proven nontext records as untouched opaque source, emitting typed diagnostics and warnings. Text-bearing failures and unknown schemas remain strict. The default remains strict, and this option cannot be combined with `validate_nontext=False`. An unchanged `PluginPatcher` output and unrelated record edits retain opaque source bytes; the option does not repair or permit semantic edits to an undecodable record. Both preservation options require Bethkit 0.9.0 or newer.

Encoding detector and codec copyright/permission notices are bundled under `bethkit/licenses/` in platform wheels. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) identifies the audited components; Bethkit's own license remains Apache-2.0.

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

### Reading string tables from archive data

`StringTable.from_bytes(data, kind)` parses the complete serialized file directly in memory. `StringTable.from_stream(stream, kind)` reads a blocking binary stream from its current position to EOF without seeking or closing it. Both methods support STRINGS, DLSTRINGS and ILSTRINGS; specify the format explicitly because these files have no reliable format signature. Entries retain raw bytes; `get_str()` explicitly decodes UTF-8. No temporary files are created, and the parsed table owns its data independently of the input.

```python
from io import BytesIO

from bethkit import StringFileKind, StringTable

# data is the complete decompressed file returned by the BSA reader.
with StringTable.from_bytes(data, StringFileKind.STRINGS) as table:
    text = table.get_str(17)

with BytesIO(data) as stream:
    with StringTable.from_stream(stream, StringFileKind.STRINGS) as table:
        raw = table.get(17)
```

These factories require a native build exporting `bethkit_string_table_from_bytes`; the published native 0.9.0 does not provide that symbol. Existing APIs remain available with older libraries; the new factories raise a clear error instead of creating a temporary-file fallback.

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

Bethkit normally uses each schema field's declared encoding for inline text. For a plugin known to use UTF-8 throughout its translatable inline fields, `SemanticContext(package, inline_encoding="utf-8")` remains an explicit override. For plugins mixing UTF-8 and legacy text, use `SemanticContext(package, inline_decoding="prefer_utf8")`. This opt-in mode checks each translatable inline string separately, falling back to the schema codec when its bytes are not valid UTF-8. `StringReference.encoding` and `encoding_source` report the selected codec and whether it came from the schema or the heuristic. Valid UTF-8 bytes can also be valid legacy bytes, so automatic selection cannot resolve every ambiguous string. For such a field, `LocalizationEditor.select_inline_encoding(reference, "cp1252")` re-decodes it without changing bytes; `replace(reference, text, inline_encoding="cp1252")` selects the codec for an atomic edit. Technical fields and external string tables are unaffected. Mixed decoding requires Bethkit 0.7.0 or newer.

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
uv run ruff check src/ tests/ scripts/
uv run ruff format --check src/ tests/ scripts/
uv run pyright src/ tests/ scripts/
```

Unit tests mock the native boundary. A release-quality check must also set `BETHKIT_LIB` and `BETHKIT_SCHEMA` and run `pytest --require-native`; an explicitly configured but incompatible library is an error, not a skipped test. See [BUILDING.md](BUILDING.md) for the pinned workflow and [SCHEMA.md](SCHEMA.md) for deterministic model generation.

Contributions follow the [Python style conventions](STYLE.md). Maintained files are limited to 400 lines, enforced by local commit/push hooks, CI, and the build backend; individual generated-file exceptions are recorded explicitly in `file-length-policy.json`. Install the local guards with `uv run python scripts/install_git_hooks.py` after setting up the development environment.

## Related projects

- [bethkit](https://github.com/Modding-Forge/bethkit) - the underlying Rust library; `bethkit.py` wraps its C ABI

## License

Apache-2.0 - see [LICENSE](LICENSE).
