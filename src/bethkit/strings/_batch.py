"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from collections.abc import Callable, Iterator
from typing import Optional

import pydantic

from .. import _ffi
from .._error import RecordDecodeError
from ..plugin.plugin import Plugin
from ..records import _wire
from ..schema.semantic_context import SemanticContext
from .string_scan_diagnostic import StringScanDiagnostic


class _StringBatch(pydantic.BaseModel, frozen=True):
    """Validated scalar-only projection from one bounded native batch."""

    values: tuple[_wire.WireScalar, ...]
    """Ordered translatable leaves with full structural editing addresses."""
    done: bool
    """Whether the cursor reached the end of the plugin."""
    diagnostics: tuple[StringScanDiagnostic, ...] = ()
    """Explicit opaque nontext failures, never fabricated decoded values."""


def available() -> bool:
    """Reports whether the loaded native library supports batched traversal.

    Returns:
        True only when all three cursor lifecycle functions are present.
    """

    lib = _ffi.load_lib()
    return all(
        hasattr(lib, name)
        for name in (
            "bethkit_string_cursor_new",
            "bethkit_string_cursor_next_json",
            "bethkit_string_cursor_free",
        )
    )


def iter_values(
    plugin: Plugin,
    context: SemanticContext,
    *,
    validate_nontext: bool = True,
    preserve_opaque_nontext: bool = False,
    on_diagnostic: Optional[Callable[[StringScanDiagnostic], None]] = None,
) -> Iterator[_wire.WireScalar]:
    """Borrows both owners and releases the cursor on exhaustion or close.

    Args:
        plugin: Source plugin, never transferred to the cursor.
        context: Matching decoding runtime, borrowed for iteration.
        validate_nontext: Decode even schema-proven text-free records.
        preserve_opaque_nontext: Retain failed nontext records as opaque source.
        on_diagnostic: Optional observer of each retained record's failure.

    Yields:
        Independently owned scalar values validated from native JSON.

    Raises:
        BethkitClosedError: Either source owner closes, even within a batch.
        RecordDecodeError: Cursor creation or a record decode fails.
        ValueError: Opaque retention is combined with nontext skipping.
        pydantic.ValidationError: Native batch JSON violates its contract.
    """

    lib = _ffi.load_lib()
    if preserve_opaque_nontext:
        if not validate_nontext:
            raise ValueError("Opaque retention requires full validation.")
        if not hasattr(lib, "bethkit_string_cursor_new_preserving_nontext"):
            raise RecordDecodeError("Native library lacks opaque retention.")
        pointer = lib.bethkit_string_cursor_new_preserving_nontext(
            context._native_pointer(), plugin._native_pointer()
        )
    else:
        pointer = lib.bethkit_string_cursor_new(
            context._native_pointer(),
            plugin._native_pointer(),
            validate_nontext,
        )
    if not pointer:
        raise RecordDecodeError(_ffi.last_error(lib))
    try:
        while True:
            context._native_pointer()
            plugin._native_pointer()
            result = lib.bethkit_string_cursor_next_json(pointer, 128)
            if not result:
                raise RecordDecodeError(_ffi.last_error(lib))
            text = _ffi.copy_and_free_str(result, lib.bethkit_string_free, lib)
            batch = _StringBatch.model_validate_json(text)
            for diagnostic in batch.diagnostics:
                logging.getLogger("StringScan").warning(
                    f"Preserving opaque {diagnostic.record_signature} "
                    f"in {plugin.source_name!r}, "
                    f"{diagnostic.form_id:08X}: {diagnostic.message}"
                )
                if on_diagnostic is not None:
                    on_diagnostic(diagnostic)
            for value in batch.values:
                # Buffered values must not conceal a closed source owner.
                context._native_pointer()
                plugin._native_pointer()
                yield value
            if batch.done:
                return
    finally:
        lib.bethkit_string_cursor_free(pointer)
