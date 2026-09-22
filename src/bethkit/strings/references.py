"""
Copyright (c) Modding Forge
"""

# Position-based references to inline and externally localized strings.

from __future__ import annotations

from collections.abc import Iterator
from typing import Optional

from .. import _error
from ..enums import StringFileKind
from ..plugin import plugin as plugin_module
from ..records import _wire
from ..schema import schema
from ..strings import strings
from .string_identity import StringIdentity as StringIdentity
from .string_reference import StringReference as StringReference

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

    for field in snapshot.fields:
        for value in _iter_scalars(field.value):
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
                    text=value.value,
                    storage="inline",
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
                            f"String ID {value.value} is absent "
                            f"from {kind.name}."
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
) -> Iterator[StringReference]:
    """Lazily enumerates schema-declared strings in a plugin.

    Args:
        plugin: Open source plugin; named inputs allow persistent identities.
        context: Semantic runtime matching the plugin's schema.
        tables: Optional tables resolving external IDs into text.

    Yields:
        Inline and external text using the same position-based reference API.

    Raises:
        BethkitClosedError: A native owner closes during iteration.
        RecordDecodeError: A record cannot be decoded by the schema runtime.
        StringTableError: Supplied tables are incomplete or invalid.
    """

    localized = plugin.is_localized
    for record in _iter_records(plugin):
        snapshot = context.strings_snapshot(record, localized=localized)
        yield from _from_snapshot(snapshot, plugin, tables)
