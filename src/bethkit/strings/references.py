"""
Copyright (c) Modding Forge
"""

# Position-based references to inline and externally localized strings.

from __future__ import annotations

import logging
from collections.abc import Callable, Iterator
from typing import Optional

from .. import _error
from ..enums import StringFileKind
from ..plugin import plugin as plugin_module
from ..records import _wire
from ..schema import schema
from ..strings import strings
from . import _batch
from ._text_preview import TextPreview
from .string_identity import StringIdentity as StringIdentity
from .string_reference import StringReference as StringReference
from .string_scan_diagnostic import StringScanDiagnostic

_TABLE_KINDS: dict[str, StringFileKind] = {
    "strings": StringFileKind.STRINGS,
    "dl_strings": StringFileKind.DL_STRINGS,
    "il_strings": StringFileKind.IL_STRINGS,
}


def _iter_records(
    plugin: plugin_module.Plugin,
) -> Iterator[plugin_module.Record]:
    """Walks groups without materializing typed records.

    Args:
        plugin: Open source plugin.

    Yields:
        Each borrowed record in source order.

    Raises:
        BethkitClosedError: The plugin closes during iteration.
    """

    stack: list[Iterator[plugin_module.Record | plugin_module.Group]] = [
        iter(plugin)
    ]
    while stack:
        child = next(stack[-1], None)
        if child is None:
            stack.pop()
        elif isinstance(child, plugin_module.Group):
            stack.append(iter(child))
        else:
            yield child


def _iter_scalars(value: _wire.WireValue) -> Iterator[_wire.WireScalar]:
    """Traverses a snapshot's existing value tree.

    Args:
        value: Native semantic value tree.

    Yields:
        Each scalar in source order, without guessing repetition membership.
    """

    if isinstance(value, _wire.WireScalar):
        yield value
    elif isinstance(value, _wire.WireStruct):
        for field in value.fields:
            yield from _iter_scalars(field.value)
    else:
        for item in value.items:
            yield from _iter_scalars(item)


def _from_snapshot(
    snapshot: _wire.RecordSnapshot,
    plugin: plugin_module.Plugin,
    tables: Optional[strings.LocalizationSet],
) -> Iterator[StringReference]:
    """Creates translatable references from a fully decoded record snapshot.

    Args:
        snapshot: Native immutable semantic snapshot.
        plugin: Source supplying stable filename and session provenance.
        tables: Optional tables resolving external strings.

    Yields:
        Addressed translatable strings, excluding editor IDs and other text.

    Raises:
        BethkitClosedError: The plugin or supplied tables are closed.
        StringTableError: A translatable value or supplied table is invalid.
    """

    values = (
        value
        for field in snapshot.fields
        for value in _iter_scalars(field.value)
    )
    yield from _from_scalars(values, plugin, tables)


def _from_scalars(
    values: Iterator[_wire.WireScalar],
    plugin: plugin_module.Plugin,
    tables: Optional[strings.LocalizationSet],
) -> Iterator[StringReference]:
    """Builds references from either record snapshots or native batches.

    Args:
        values: Ordered, validated native scalar values.
        plugin: Live source supplying identity and provenance.
        tables: Optional external localization tables.

    Yields:
        Positionally identified strings with unchanged edit addresses.

    Raises:
        StringTableError: A translatable value or table lookup is invalid.
        BethkitClosedError: A supplied source or table is closed.
    """

    for value in values:
        if not value.translatable or value.kind == "absent":
            continue
        address = value.address
        identity = StringIdentity(
            plugin_name=plugin.source_name,
            record_signature=address.record_signature,
            form_id=address.form_id,
            subrecord_index=address.subrecord_index,
            subrecord_path=address.subrecord_path,
            repeat_scopes=address.repeat_scopes,
            value_steps=address.value_steps,
        )
        if value.kind == "string" and isinstance(value.value, str):
            reference = StringReference(
                identity=identity,
                address=address,
                schema_path=value.schema_path,
                text=value.value,
                storage="inline",
                encoding=value.inline_encoding,
                encoding_source=value.encoding_source,
            )
        elif (
            value.kind == "bytes"
            and isinstance(value.value, tuple)
            and value.decoding_warning is not None
        ):
            raw_bytes = bytes(value.value)
            preview = TextPreview.from_bytes(
                raw_bytes, encoding=value.preview_encoding or "windows-1252"
            )
            reference = StringReference(
                identity=identity,
                address=address,
                schema_path=value.schema_path,
                text=None,
                storage="inline",
                raw_bytes=raw_bytes,
                decoding_warning=value.decoding_warning,
                best_effort_text=preview.text,
                best_effort_encoding=preview.encoding,
                preview_escaped_bytes=preview.escaped_bytes,
            )
            logging.getLogger("StringScan").warning(
                f"Undecoded text in {plugin.source_name!r}, "
                f"{identity.form_id:08X} "
                f"{identity.subrecord_path}: best-effort codec "
                f"{preview.encoding!r} selected (not confirmed); "
                f"escaped_bytes={preview.escaped_bytes}; "
                f"{value.decoding_warning}"
            )
        elif value.kind == "uint" and isinstance(value.value, int):
            if value.string_table is None:
                raise _error.StringTableError(
                    f"No string table is declared for {address}."
                )
            kind = _TABLE_KINDS[value.string_table]
            text: Optional[str] = None
            if tables is not None:
                try:
                    text = tables.get_str(kind, value.value)
                except (
                    UnicodeDecodeError,
                    _error.BethkitNativeError,
                ) as exc:
                    raise _error.StringTableError(str(exc)) from exc
                if text is None:
                    raise _error.StringTableError(
                        f"String ID {value.value} is absent from {kind.name}."
                    )
            reference = StringReference(
                identity=identity,
                address=address,
                text=text,
                storage="external",
                table_kind=kind,
                string_id=value.value,
            )
        else:
            raise _error.StringTableError(
                f"Invalid translatable {value.kind!r} value at {address}."
            )
        reference._bind_source(plugin._reference_identity())
        yield reference


def iter_strings(
    plugin: plugin_module.Plugin,
    context: schema.SemanticContext,
    tables: Optional[strings.LocalizationSet] = None,
    *,
    validate_nontext: bool = True,
    preserve_opaque_nontext: bool = False,
    on_diagnostic: Optional[Callable[[StringScanDiagnostic], None]] = None,
) -> Iterator[StringReference]:
    """Lazily enumerates schema-declared strings in a plugin.

    Args:
        plugin: Open source plugin; named inputs allow persistent identities.
        context: Semantic runtime matching the plugin's schema.
        tables: Optional tables resolving external IDs into text.
        validate_nontext: Retain full decoding of records without strings.
            False opts into schema-proven text-free skipping on newer libraries.
        preserve_opaque_nontext: Explicitly preserve undecodable nontext records
            without repairing them. Each failure is logged and reported.
        on_diagnostic: Optional observer for retained opaque record diagnostics.

    Yields:
        Inline and external text using the same position-based reference API.

    Raises:
        BethkitClosedError: A native owner closes during iteration.
        RecordDecodeError: A record cannot be decoded by the schema runtime.
        ValueError: Opaque preservation is combined with nontext skipping.
        StringTableError: Supplied tables are incomplete or invalid.
    """

    context._check_plugin(plugin)
    if _batch.available():
        yield from _from_scalars(
            _batch.iter_values(
                plugin,
                context,
                validate_nontext=validate_nontext,
                preserve_opaque_nontext=preserve_opaque_nontext,
                on_diagnostic=on_diagnostic,
            ),
            plugin,
            tables,
        )
        return
    if preserve_opaque_nontext:
        raise _error.RecordDecodeError("Native library lacks opaque retention.")
    localized = plugin.is_localized
    for record in _iter_records(plugin):
        snapshot = context.strings_snapshot(record, localized=localized)
        yield from _from_snapshot(snapshot, plugin, tables)
