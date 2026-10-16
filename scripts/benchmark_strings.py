"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Optional

from bethkit import Game, Plugin, SchemaCatalog, SemanticContext
from bethkit.strings import StringReference
from bethkit.strings.references import _from_snapshot, _iter_records


def reference_strings(
    plugin: Plugin, context: SemanticContext
) -> Iterator[StringReference]:
    """Runs the pre-batching projection as an independent correctness oracle.

    Args:
        plugin: Open input plugin.
        context: Runtime used by both implementations.

    Yields:
        Unmodified references from complete record projections.

    Raises:
        BethkitNativeError: A native record cannot be decoded.
    """

    for record in _iter_records(plugin):
        snapshot = context.strings_snapshot(
            record, localized=plugin.is_localized
        )
        yield from _from_snapshot(snapshot, plugin, None)


def benchmark(
    paths: list[Path],
    output: Path,
    *,
    legacy: bool,
    detect_only: bool,
    strings_only: bool,
    mixed: bool,
) -> None:
    """Measures real files and records ordered content/address fingerprints.

    No cache is evicted: the first and subsequent runs are process-cold and
    process-warm, not claims about a cold operating-system page cache.
    Each result is flushed immediately so failed inputs remain inspectable.

    Args:
        paths: Ordered real plugin paths; sources are never modified.
        output: JSON-lines report, created exclusively to avoid overwrites.
        legacy: Use the original per-record snapshot path.
        detect_only: Omit complete enumeration for large detection corpora.
        strings_only: Skip schema-proven text-free record types.
        mixed: Use the explicit per-string UTF-8/legacy heuristic.

    Raises:
        OSError: The report cannot be created or an input cannot be read.
        BethkitNativeError: The embedded schema cannot be loaded.
    """

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        with SchemaCatalog.embedded() as catalog:
            with catalog.package(Game.SKYRIM_SE) as package:
                for path in paths:
                    started = time.perf_counter()
                    count = 0
                    digest = hashlib.sha256()
                    failure: Optional[str] = None
                    decision: dict[str, object] = {}
                    opened = started
                    detected = started
                    try:
                        with Plugin.open(path, Game.SKYRIM_SE) as plugin:
                            opened = time.perf_counter()
                            with SemanticContext.for_plugin(
                                package, plugin, mixed=mixed
                            ) as context:
                                detected = time.perf_counter()
                                metadata = context.encoding_decision
                                if metadata is not None:
                                    decision = metadata.model_dump()
                                if not detect_only:
                                    references = (
                                        reference_strings(plugin, context)
                                        if legacy
                                        else plugin.iter_strings(
                                            context,
                                            validate_nontext=not strings_only,
                                        )
                                    )
                                    for reference in references:
                                        digest.update(
                                            reference.model_dump_json().encode()
                                        )
                                        digest.update(b"\n")
                                        count += 1
                    except Exception as error:
                        # Record failures, never silently omit a corpus member.
                        failure = f"{type(error).__name__}: {error}"
                    finished = time.perf_counter()
                    result: dict[str, object] = {
                        "path": str(path.resolve()),
                        "size": path.stat().st_size,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "legacy": legacy,
                        "strings_only": strings_only,
                        "mixed": mixed,
                        "open_seconds": opened - started,
                        "detect_seconds": detected - opened,
                        "enumerate_seconds": finished - detected,
                        "count": count,
                        "references_sha256": digest.hexdigest(),
                        "decision": decision,
                        "failure": failure,
                    }
                    encoded = json.dumps(result, ensure_ascii=True)
                    stream.write(encoded + "\n")
                    stream.flush()
                    print(encoded, flush=True)


def main() -> None:
    """Measures explicit files or every existing plugin in a real load order.

    Raises:
        OSError: Input paths or the report are inaccessible.
        ValueError: Load-order names would escape the supplied Data directory.
    """

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", type=Path, nargs="*")
    parser.add_argument("--data", type=Path)
    parser.add_argument("--plugins", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--legacy", action="store_true")
    parser.add_argument("--detect-only", action="store_true")
    parser.add_argument("--strings-only", action="store_true")
    parser.add_argument("--mixed", action="store_true")
    arguments = parser.parse_args()
    paths: list[Path] = arguments.paths
    if arguments.plugins is not None:
        if arguments.data is None:
            parser.error("--plugins requires --data")
        data: Path = arguments.data.resolve()
        for line in arguments.plugins.read_text(
            encoding="utf-8-sig"
        ).splitlines():
            if not line.startswith("*"):
                continue
            name = line[1:]
            if Path(name).name != name:
                raise ValueError(f"Invalid plugin basename: {name!r}")
            path = data / name
            if path.is_file() and path not in paths:
                paths.append(path)
            elif not path.is_file():
                print(f"Missing active plugin: {path}", flush=True)
    if not paths:
        parser.error("No existing input plugins were selected")
    benchmark(
        paths,
        arguments.output,
        legacy=arguments.legacy,
        detect_only=arguments.detect_only,
        strings_only=arguments.strings_only,
        mixed=arguments.mixed,
    )


if __name__ == "__main__":
    main()
