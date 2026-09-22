# Building and validating bethkit.py

The Python API requires the native source revision recorded in [native-source.json](native-source.json). ABI version 2 alone is insufficient: older native releases, including v0.4.0, do not export all functions required by this development version. The wheel build checks both the ABI version and every function declared by the Python bindings.

## Local development

Install a stable Rust toolchain, Python 3.10 or newer, and uv. Check out the pinned commit of [Modding-Forge/bethkit](https://github.com/Modding-Forge/bethkit). Windows native builds also require the Visual Studio C++ build tools and Windows SDK.

The runtime uses Pydantic 2.5.3 or newer within the 2.x series. The typed JSON boundary needs `JsonValue`, introduced in [Pydantic 2.5](https://docs.pydantic.dev/latest/changelog/#v250-2023-11-13); the earlier `pydantic>=2.0` lower bound does not cover this API.

Obtain the Skyrim SE schema using the native repository's `scripts/Get-SkyrimSeSchema.ps1`; it verifies the xDump release asset against the checked-in SHA-256 pin. Set `BETHKIT_SKYRIM_SE_SCHEMA` to the resulting absolute path, then build the native shared library with `cargo build --locked --release -p bethkit-ffi --features schema-skyrim-se`. This embeds only the Skyrim SE package, available through `SchemaCatalog.embedded().package(Game.SKYRIM_SE)`. Set `BETHKIT_LIB` to the absolute path of that library (`bethkit_ffi.dll` on Windows or `libbethkit_ffi.so` on Linux) and `BETHKIT_SCHEMA` to the schema path for the integration tests.

```sh
uv sync --extra dev
uv run ruff check src/ tests/ scripts/
uv run ruff format --check src/ tests/ scripts/
uv run pyright src/ tests/
uv run pytest tests/ --require-native
uv run python scripts/generate_records.py --schema "$BETHKIT_SCHEMA" --output src/bethkit/records/skyrim_se --check
uv build --wheel
```

The commands above use shell-style environment expansion. In PowerShell, use `$env:BETHKIT_SCHEMA` instead of `$BETHKIT_SCHEMA`.

Unit tests can run independently with `uv run pytest tests/ -m "not integration"`. CI and release validation must use `--require-native`: missing libraries, incompatible ABI versions, and absent exports are failures, not skipped integration tests. Distribution wheels require a compatible native library with embedded Skyrim SE schemas. Editable development installs such as `uv sync --extra dev`, and source distributions, do not validate or bundle native libraries; this allows environment setup and mocked unit tests before the native build. The build hook includes the selected library directly in distribution wheels and never overwrites or deletes an existing copy in `src/bethkit/`.

## CI and publication

Regular CI builds exactly the pinned native commit from source on Windows and Linux, obtains the checksum-pinned schema, runs native integration, verifies generated Python models, and builds platform wheels. A commit that exists only locally must be pushed to the native repository before remote CI can check it out; updating the pin does not upload or publish anything.

`release: null` explicitly means the required native API has not yet been assigned a published release. Python publication is blocked in that state. There is no fallback to the latest native release and no invented future tag.

Before publishing Python, publish and verify the intended native revision. Then replace the null release entry with its actual tag and both platform asset entries, each containing the exact `filename` and full ZIP `sha256`. Keep `revision` aligned with the source used for those artifacts. The release workflow downloads only these immutable selections, verifies ZIP and schema checksums, and requires real native integration before building wheels. Linux wheels are repaired and inspected with auditwheel; their tags are not inferred from a string scan.

Existing tag-triggered PyPI and GitHub publishing jobs remain unchanged. This preparation does not create a release, push a commit, or push a tag.
