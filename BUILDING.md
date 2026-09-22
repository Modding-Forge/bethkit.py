# Building and validating bethkit.py

The Python API requires the native source revision recorded in [native-source.json](native-source.json). ABI version 2 alone is insufficient: older native releases, including v0.4.0, do not export all functions required by Python 2.0. The wheel build checks both the ABI version and every function declared by the Python bindings.

## Local development

Install a stable Rust toolchain, Python 3.10 or newer, and uv. Check out the pinned commit of [Modding-Forge/bethkit](https://github.com/Modding-Forge/bethkit). Windows native builds also require the Visual Studio C++ build tools and Windows SDK.

The runtime uses Pydantic 2.5.3 or newer within the 2.x series. The typed JSON boundary needs `JsonValue`, introduced in [Pydantic 2.5](https://docs.pydantic.dev/latest/changelog/#v250-2023-11-13); the earlier `pydantic>=2.0` lower bound does not cover this API.

Obtain the Skyrim SE schema using the native repository's `scripts/Get-SkyrimSeSchema.ps1`; it verifies the xDump release asset against the checked-in SHA-256 pin. Set `BETHKIT_SKYRIM_SE_SCHEMA` to the resulting absolute path, then build the native shared library with `cargo build --locked --release -p bethkit-ffi --features schema-skyrim-se`. This embeds only the Skyrim SE package, available through `SchemaCatalog.embedded().package(Game.SKYRIM_SE)`. Set `BETHKIT_LIB` to the absolute path of that library (`bethkit_ffi.dll` on Windows or `libbethkit_ffi.so` on Linux) and `BETHKIT_SCHEMA` to the schema path for the integration tests.

```sh
uv sync --extra dev
uv run ruff check src/ tests/ scripts/
uv run ruff format --check src/ tests/ scripts/
uv run pyright src/ tests/ scripts/
uv run pytest tests/ --require-native
uv run python scripts/generate_records.py --schema "$BETHKIT_SCHEMA" --output src/bethkit/records/skyrim_se --check
uv build --wheel
```

The commands above use shell-style environment expansion. In PowerShell, use `$env:BETHKIT_SCHEMA` instead of `$BETHKIT_SCHEMA`.

Unit tests can run independently with `uv run pytest tests/ -m "not integration"`. CI and release validation must use `--require-native`: missing libraries, incompatible ABI versions, and absent exports are failures, not skipped integration tests. Distribution wheels require a compatible native library with embedded Skyrim SE schemas. Editable development installs such as `uv sync --extra dev`, and source distributions, do not validate or bundle native libraries; this allows environment setup and mocked unit tests before the native build. The build hook includes the selected library directly in distribution wheels and never overwrites or deletes an existing copy in `src/bethkit/`.

## CI and publication

All maintained text files have a hard limit of 400 lines. A generated file may exceed that limit only when its exact path, explicit maximum, and justification are approved in `file-length-policy.json`; there are no directory-wide or automatic exceptions. Run `python scripts/check_file_lengths.py` to check the working tree before building. CI and tagged releases check the committed snapshot before installing dependencies or preparing native artifacts.

The same gate runs inside Hatch before every wheel, editable install, and source-distribution build. Source archives include the checker, its helpers, and the policy so builds without Git metadata remain subject to the limit. Editable installs still need no native library, but they cannot bypass source-quality checks.

Install the local commit and push guards once per clone using `python scripts/install_git_hooks.py`, or `uv run python scripts/install_git_hooks.py` after dependency setup. The installer records that Python executable in the local `bethkit.policyPython` setting and enables `.githooks` through `core.hooksPath`. It refuses to replace another hook manager or active default hooks. Re-run it with a working Python 3.10+ interpreter if that interpreter is later moved or removed. On POSIX systems it also makes the hook launchers executable; preserve their executable Git file mode when committing them.

The commit guard checks the staged index, not unrelated working-tree edits. The push guard checks every outgoing commit and each updated destination tip, including tags. Deletions do not introduce code and are skipped. New branches and tags use freshly advertised destination refs, not cached remote-tracking refs, to identify history already on the server. This requires network access; if an advertised commit is unavailable locally, fetch that destination's heads and tags before retrying. Repositories first pushed to a new destination must satisfy the policy throughout their outgoing history. Existing files over the limit remain failures until they are split or an individual generated-file exception is explicitly approved; installing hooks does not grant exemptions. Local Git hooks can be bypassed deliberately, so CI remains the shared enforcement boundary.

The GitHub `master` branch requires the `File length policy` check from GitHub Actions, including for administrators. Force pushes and branch deletion are disabled. Changes without a successful required check must be validated on a branch or pull request before entering `master`; changing this repository does not itself configure protection for another fork.

Regular CI builds exactly the pinned native commit from source on Windows and Linux, obtains the checksum-pinned schema, runs native integration, verifies generated Python models, and builds platform wheels. A commit that exists only locally must be pushed to the native repository before remote CI can check it out; updating the pin does not upload or publish anything.

Python 2.0 pins the published Bethkit v0.5.0 release and its Windows and Linux archive checksums. A `release: null` entry explicitly means the required native API has not yet been assigned a published release. Python publication is blocked in that state. There is no fallback to the latest native release and no invented future tag.

Before publishing Python, publish and verify the intended native revision. Then replace the null release entry with its actual tag and both platform asset entries, each containing the exact `filename` and full ZIP `sha256`. Keep `revision` aligned with the source used for those artifacts. The release workflow downloads only these immutable selections, verifies ZIP and schema checksums, and requires real native integration before building wheels. Linux wheels are repaired and inspected with auditwheel; their tags are not inferred from a string scan.

After validating and committing the release pin, push master and the matching Python version tag. The tag-triggered workflow builds both platform wheels, publishes them to PyPI through OIDC, and attaches them to a GitHub release.
