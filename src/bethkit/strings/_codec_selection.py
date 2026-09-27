"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import codecs
from typing import Literal, Optional

from .. import _error
from ..plugin import plugin as plugin_module
from ..schema import _editor_values, schema
from . import references, strings


def encoding_id(encoding: str) -> int:
    """Resolves one supported concrete inline codec to its native code.

    Args:
        encoding: Python codec name or alias.

    Returns:
        Native identifier for UTF-8 or Windows-1252.

    Raises:
        LookupError: The codec name is unknown.
        ValueError: The codec is not supported by native inline editing.
    """

    name = codecs.lookup(encoding).name
    result = {"utf-8": 1, "cp1252": 2}.get(name)
    if result is None:
        raise ValueError(f"Unsupported inline encoding: {encoding!r}.")
    return result


def set_value(
    editor: schema.RecordEditor,
    reference: references.StringReference,
    kind: Literal["string", "uint"],
    value: str | int,
) -> None:
    """Sets an inline value or external table ID at a checked address.

    Args:
        editor: Native editor for the reference's record.
        reference: Current addressed string.
        kind: Native scalar kind for the replacement.
        value: Replacement text or string-table identifier.

    Raises:
        UnsupportedEditError: The address or replacement is invalid.
    """

    _editor_values.set_json(
        editor._borrow_pointer(),
        reference.address,
        {"kind": kind, "value": value},
    )


def replace(
    editor: schema.RecordEditor,
    reference: references.StringReference,
    text: str,
    encoding: str,
) -> None:
    """Replaces a scoped string using a concrete codec atomically.

    Args:
        editor: Native editor for the reference's record.
        reference: Current addressed inline string.
        text: Replacement Unicode text.
        encoding: Concrete codec name selected by the caller.

    Raises:
        LookupError: The codec name is unknown.
        UnsupportedEditError: The native edit or address is invalid.
        ValueError: The codec is unsupported for inline editing.
    """

    if reference.schema_path is None:
        raise _error.UnsupportedEditError(
            "This reference has no schema string path."
        )
    _editor_values.set_inline_string_at(
        editor._borrow_pointer(),
        reference.address,
        reference.schema_path,
        encoding_id(encoding),
        text,
    )


def select(
    editor: schema.RecordEditor,
    plugin: plugin_module.Plugin,
    tables: Optional[strings.LocalizationSet],
    reference: references.StringReference,
    encoding: str,
) -> references.StringReference:
    """Re-decodes one editor-local string without changing its bytes.

    Args:
        editor: Native editor for the reference's record.
        plugin: Source plugin owning the reference.
        tables: Optional external string tables.
        reference: Current addressed inline string.
        encoding: Concrete codec name selected by the caller.

    Returns:
        Fresh reference with corrected text and codec provenance.

    Raises:
        UnsupportedEditError: The field address or codec is invalid.
        LookupError: The codec name is unknown.
        ValueError: The codec is unsupported for inline editing.
    """

    if reference.storage != "inline" or reference.schema_path is None:
        raise _error.UnsupportedEditError(
            "The reference does not identify an inline schema string."
        )
    code = encoding_id(encoding)
    current = next(
        (
            item
            for item in references._from_snapshot(
                editor.strings_snapshot(), plugin, tables
            )
            if item.identity == reference.identity
        ),
        None,
    )
    if current is None or current.address != reference.address:
        raise _error.UnsupportedEditError(
            "The string address is stale; enumerate strings again."
        )
    _editor_values.select_inline_encoding_at(
        editor._borrow_pointer(), current.address, reference.schema_path, code
    )
    selected = next(
        (
            item
            for item in references._from_snapshot(
                editor.strings_snapshot(), plugin, tables
            )
            if item.identity == reference.identity
        ),
        None,
    )
    if selected is None:
        raise _error.UnsupportedEditError(
            "The selected string disappeared from the editor."
        )
    return selected
