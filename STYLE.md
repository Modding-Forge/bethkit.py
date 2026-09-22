# Python style conventions

This project follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) with the explicit workspace conventions below. Ruff checks Google docstring rules as well as imports, naming, annotations, modern Python syntax, and formatting. Strict Pyright covers source, tests, and maintenance scripts. Automated checks complement review of documented behavior, native ownership, and API design; passing a linter is not proof that every contract is correct.

## Project-specific conventions

- Target Python 3.10 or newer and fully annotate public APIs, class state, and non-obvious local values. Use `Optional[T]` for optional values and built-in generic containers elsewhere.
- Keep imports relative inside the library. Direct imports of types are allowed where they keep annotations and Pydantic models readable. Native declarations remain private; public APIs do not expose pointers or native handles.
- Use frozen Pydantic models for immutable values and snapshots. A frozen container does not by itself make nested mutable values deeply immutable; documentation must distinguish these cases.
- Every Python file starts with the exact three-line copyright docstring. Every function, method, and class has a docstring, including generated overloads. Follow each docstring with one blank line before code. Describe parameters, return values, meaningful exceptions, ownership, and lifetime constraints where applicable.
- Use the pinned Ruff formatter with an 80-character target, which remains within the workspace's 90-character maximum. Markdown paragraphs have no forced line breaks.
- Give each public class a focused module. Small, closely related private data-contract types may remain together. Preserve top-level public imports when moving implementation files.
- Every maintained text file has a hard cap of 400 physical lines, including blanks and comments. The only longer files are individually named generated modules with a fixed maximum and reason in `file-length-policy.json`. Never add a handwritten-file waiver to avoid a logical split.

The exact copyright header conflicts with Ruff rules D200, D212, and D415. The required blank line after docstrings conflicts with D202, and documented overloads conflict with D418. These five exceptions are listed with reasons in `pyproject.toml`; other Google-convention docstring rules remain enabled. Outside the required header, use clear summary sentences ending in punctuation. `UP045` is disabled because the workspace requires `Optional[T]`.

## Native resource safety

Create native-backed objects through their documented creation methods. Private factories adopt successful native allocations and are not a public constructor interface. Borrowed records keep their owner alive and validate its open state on each native access. Explicit `close()` and context managers provide deterministic cleanup; finalizers provide best-effort cleanup and log failures without raising during interpreter shutdown.

Copy thread-local native error text immediately after failure. Owned output buffers must be released with their matching native destructor even when decoding fails. Clear owned handles before freeing them so repeated cleanup cannot free the same allocation twice. Never transfer a child before validating the receiving owner's state.

## Validation

Run the checks documented in [BUILDING.md](BUILDING.md), including real-library integration and deterministic model generation before shipping. Unit tests use mocked native boundaries; integration tests require the pinned ABI and schema. The local Git hooks check staged or outgoing snapshots, while the protected `master` branch requires the GitHub Actions `File length policy` check. Local hooks are not a security boundary: intentionally changing Git configuration can bypass them, but does not bypass branch protection or the build hook.
