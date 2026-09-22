# Typed Skyrim SE records

The generated Python models derive from the Skyrim Special Edition schema published by [Modding-Forge/xDump](https://github.com/Modding-Forge/xDump). Its record definitions and semantic metadata originate in [xEdit](https://github.com/TES5Edit/TES5Edit). Bethkit interprets that schema; the Python generator does not independently reverse-engineer the file format or duplicate xEdit's grammar rules.

## Pinned input

| Property | Value |
| --- | --- |
| Game | Skyrim Special Edition |
| xDump release | `v0.1.0` |
| Schema package | `skyrim_se.bkschema` |
| Package SHA-256 | `8066dd6c64fe61583bafe0f8e57c6d78bbaf4d84d41a427fe98d383e976ee092` |
| Payload SHA-256 | `66998fb3c765fbe4b29059c6d68722d1b53a1951b0ab300ff530ca19104104c7` |
| Upstream xEdit version | `4.1.5f` |
| Upstream xEdit commit | `f5c00f3fa3ee39511185515802647246c807f759` |
| Generated record definitions | 134 |

The complete schema provenance is available through `SchemaPackage.manifest()`. Each generated record class embeds the exact payload hash and rejects mismatched snapshots with `SchemaMismatchError`. Other games remain available through the generic native APIs when a suitable schema is supplied, but this package does not claim generated Python models for those games.

## What coverage means

All 134 definitions in the pinned package have generated Python modules with concrete field annotations, nested immutable Pydantic models, named enums and flags, typed FormIDs, and typed field-reference overloads. Unsupported generator nodes fail generation instead of silently becoming `Any`. Unknown enumeration values are retained. A generated module and successful type checking do not prove that every possible game record has been decoded or edited successfully.

The package imports record modules lazily. Opening a plugin does not materialize those models. `QuestRecord.from_record(...)`, for example, materializes only the requested record. Large individual records can still be expensive; lazy loading is currently at record granularity, not at every payload-array element.

Native regression tests cover ownership, exact repeat scopes, nested struct and array editing, stale-address rejection, and lossless patching. Python integration tests exercise `QUST` stages and log entries, `INFO` responses, `PERK` effect alternatives, edits followed by reopening, and preservation of untouched compressed records. Localization tests cover inline edits, all three external table formats, shared-ID isolation, and consistent bundle output.

The final local Skyrim.esm sample decoded and materialized 223 records across 116 signatures without a failure. It walked 869,687 records to find those samples; the walk is not a claim that all those records were semantically validated. A separately selected small WRLD record also materialized successfully. Both sampled BPTD records with empty NAM5 model-info payloads were edited without changes, reopened, and retained all 19 subrecords byte-for-byte. This is a bounded compatibility sample, not full-corpus certification.

NAVI and large WRLD snapshots remain performance work: these can require substantial time and memory, so they were excluded from the final bounded sample. Sixteen generated definitions were not encountered by its group traversal, including the TES4 header, which is outside that traversal. Tests requiring installed game data supplement, rather than replace, the distributable synthetic integration suite.

## Editing boundaries

Generated record models are immutable views, not a second writer. Use `RecordEditor.set(view.field("name"), value)` for a typed field, or the addressed generic API for a semantic value tree. Repetition membership comes from the native grammar, including an Entry occurrence inside its containing Stage; Python does not infer membership from a subrecord signature or a global occurrence counter.

Addresses include the schema identity, record identity, source subrecord, repeat scopes, and nested value steps. Their structural guard excludes text, scalar values, byte offsets, and text lengths. Changing a string does not change its positional identity. Changing arrays, selected alternatives, or repeated grammar structure can invalidate addresses; obtain a fresh snapshot before further edits.

Individual fields and supported array elements can be replaced, inserted, or removed. Creating a complete multi-subrecord Stage, Alias, Response, or Effect group in one operation is not yet exposed as a transactional high-level API. Unsupported or ambiguous insertions fail rather than guessing boundaries. Unknown source subrecords remain in the lossless native record; use the generic snapshot or raw inspector to inspect them.

`LocalizationEditor` operates on schema-declared translatable text, not every string-shaped field; editor IDs are not translation targets. Persistent string identity excludes text, table IDs, and the transient structural guard. Live editing also checks that references originate from the correct plugin instance. Supply `name=` when opening in-memory plugins if identities must distinguish multiple files persistently.

String enumeration uses a native strings-only snapshot: unrelated binary payloads and numeric arrays are not copied into Python JSON models. This projection retains original field addresses and the complete record's structural guard. It cannot be used to construct a complete typed record model. Native schema decoding still operates on the requested record; this is not lazy decoding of individual native array elements.

## Regeneration

Build the native source revision specified in [native-source.json](native-source.json), obtain the pinned schema, and set `BETHKIT_LIB` to that library. The generator asks Bethkit for its versioned schema graph and generates static source from that graph.

```sh
python scripts/generate_records.py --schema /path/to/skyrim_se.bkschema --output src/bethkit/records/skyrim_se
python scripts/generate_records.py --schema /path/to/skyrim_se.bkschema --output src/bethkit/records/skyrim_se --check
```

Ruff must be installed with the development dependencies; use `--ruff /path/to/ruff` when it is not on PATH. Formatting and import cleanup are part of deterministic generation. Commit the generated modules together with the generator and schema pin. Review schema changes as public Python API changes, then rerun strict type checking and native integration tests before releasing.
