"""Coordinated, copy-on-write plugin and localization editing.

Copyright (c) Modding Forge
"""

from __future__ import annotations

import hashlib
import os
import re
import tempfile
from collections.abc import Iterator
from pathlib import Path
from typing import Literal, Optional

import pydantic

from bethkit import _error
from bethkit.enums import StringFileKind
from bethkit.plugin import patcher
from bethkit.plugin import plugin as plugin_module
from bethkit.schema import schema
from bethkit.strings import references, strings

_EXTENSIONS: dict[StringFileKind, str] = {
    StringFileKind.STRINGS: "STRINGS",
    StringFileKind.DL_STRINGS: "DLSTRINGS",
    StringFileKind.IL_STRINGS: "ILSTRINGS",
}


class _BundleFile(pydantic.BaseModel, frozen=True):
    """Checksum of one complete output artifact."""

    path: str
    """Bundle-relative file path."""
    size: int
    """Encoded byte length."""
    sha256: str
    """Checksum of the exact saved bytes."""


class _BundleManifest(pydantic.BaseModel, frozen=True):
    """Describes a jointly published plugin and its string tables."""

    format_version: Literal[1]
    """Version of this bundle manifest."""
    plugin: str
    """Plugin filename inside the bundle."""
    language: str
    """Language used for the external string filenames."""
    schema_payload_sha256: Optional[str]
    """Schema identity when at least one record was edited."""
    files: tuple[_BundleFile, ...]
    """Encoded output files and their integrity hashes."""


def _validate_filename(name: str, language: str) -> None:
    """Rejects output names that could escape or confuse the bundle layout.

    Args:
        name: Destination plugin basename.
        language: String table language component.

    Raises:
        ValueError: Either component is not a safe filename component.
    """

    if (
        not name
        or any(character in '<>:"/\\|?*\0' for character in name)
        or name != name.strip()
        or name.endswith(".")
        or Path(name).suffix.lower() not in {".esp", ".esm", ".esl"}
    ):
        raise ValueError(
            "plugin_name must be a plain ESP, ESM, or ESL filename."
        )
    if re.fullmatch(r"[A-Za-z0-9_-]+", language) is None:
        raise ValueError("language must contain letters, digits, '_' or '-'.")


class LocalizationEditor:
    """Edits text by position and publishes a consistent output bundle.

    The source plugin and semantic context remain caller-owned and must stay
    open until serialization. Supplied string tables are cloned immediately.
    External edits allocate fresh IDs, so other fields sharing the old ID
    remain unchanged. No original plugin or table is overwritten.
    """

    __plugin: plugin_module.Plugin
    __context: schema.SemanticContext
    __tables: Optional[strings.LocalizationSet]
    __patcher: Optional[patcher.PluginPatcher]
    __editors: dict[int, schema.RecordEditor]
    __changed: set[int]
    __localized: bool
    __closed: bool
    __finalized: bool
    __plugin_bytes: Optional[bytes]
    __table_bytes: dict[StringFileKind, bytes]
    __schema_hash: Optional[str]

    def __init__(
        self,
        plugin: plugin_module.Plugin,
        context: schema.SemanticContext,
        tables: Optional[strings.LocalizationSet] = None,
    ) -> None:
        """Starts an isolated text-editing session.

        Args:
            plugin: Source plugin, kept alive but never consumed or modified.
            context: Matching semantic runtime, borrowed for record editing.
            tables: Required original tables for a localized source plugin.

        Raises:
            BethkitClosedError: A required input handle is closed.
            BethkitNativeError: The source snapshot or table clone failed.
            StringTableError: A localized plugin has no supplied tables.
        """

        self.__closed = False
        self.__finalized = False
        self.__tables = None
        self.__patcher = None
        self.__editors = {}
        self.__changed = set()
        self.__plugin_bytes = None
        self.__table_bytes = {}
        self.__schema_hash = None
        self.__plugin = plugin
        self.__context = context
        self.__localized = plugin.is_localized
        context._native_pointer()
        if self.__localized and tables is None:
            raise _error.StringTableError(
                "Localized editing requires the original string tables."
            )
        if tables is not None:
            self.__tables = tables.clone()
        self.__patcher = patcher.PluginPatcher(plugin)

    def __check_open(self, *, editing: bool = False) -> None:
        """Checks session state before exposing owned resources.

        Args:
            editing: Whether mutable editors are required by the operation.

        Raises:
            BethkitClosedError: The session closed or was finalized for saving.
        """

        if self.__closed:
            raise _error.BethkitClosedError("LocalizationEditor is closed.")
        if editing and self.__finalized:
            raise _error.BethkitClosedError(
                "LocalizationEditor was finalized; only saving is available."
            )

    def iter_strings(self) -> Iterator[references.StringReference]:
        """Yields current text with updated addresses for edited records.

        Yields:
            Position-based text references from the session's current state.

        Raises:
            BethkitClosedError: The session or a borrowed input is closed.
            RecordDecodeError: The schema cannot decode a source record.
            StringTableError: An external string cannot be resolved.
        """

        self.__check_open(editing=True)
        for record in references._iter_records(self.__plugin):
            self.__check_open(editing=True)
            editor = self.__editors.get(record.form_id)
            snapshot = (
                editor.strings_snapshot()
                if editor is not None
                else self.__context.strings_snapshot(
                    record, localized=self.__localized
                )
            )
            yield from references._from_snapshot(
                snapshot, self.__plugin, self.__tables
            )

    def __editor_for(
        self, reference: references.StringReference
    ) -> schema.RecordEditor:
        """Finds or creates the editor for a provenance-checked reference.

        Args:
            reference: A reference originating from this source plugin.

        Returns:
            The cached editor for the reference's containing record.

        Raises:
            StringTableError: The reference is foreign or its record is absent.
            BethkitNativeError: The native editor could not be created.
        """

        if reference._source_token != self.__plugin._reference_identity():
            raise _error.StringTableError(
                "The string reference belongs to a different plugin instance."
            )
        form_id = reference.address.form_id
        editor = self.__editors.get(form_id)
        if editor is None:
            record = self.__plugin.find_record(form_id)
            if record is None:
                raise _error.StringTableError(
                    f"The source record 0x{form_id:08X} no longer exists."
                )
            editor = self.__context.edit(record, localized=self.__localized)
            self.__editors[form_id] = editor
        return editor

    def replace(self, reference: references.StringReference, text: str) -> None:
        """Replaces exactly one string without changing other shared-ID users.

        Args:
            reference: Current positional reference from this source plugin.
            text: Replacement Unicode text.

        Raises:
            BethkitClosedError: The session or a required input is closed.
            StringTableError: The reference or external tables are invalid.
            UnsupportedEditError: The address is stale or the edit is unsafe.
            ValueError: Text contains a NUL character.
        """

        self.__check_open(editing=True)
        if "\0" in text:
            raise ValueError(
                "String replacements cannot contain NUL characters."
            )
        editor = self.__editor_for(reference)
        snapshot = editor.strings_snapshot()
        current = next(
            (
                item
                for item in references._from_snapshot(
                    snapshot, self.__plugin, self.__tables
                )
                if item.identity == reference.identity
            ),
            None,
        )
        if current is None or current.address != reference.address:
            raise _error.UnsupportedEditError(
                "The string address is stale; enumerate strings again."
            )
        self.__schema_hash = current.address.schema_payload_sha256
        if current.text == text:
            return
        if current.storage == "inline":
            editor._set_json(current.address, {"kind": "string", "value": text})
            self.__changed.add(current.address.form_id)
            return
        tables = self.__tables
        kind = current.table_kind
        if tables is None or kind is None:
            raise _error.StringTableError("External string tables are missing.")
        try:
            new_id = tables.insert_new(kind, text.encode("utf-8"))
        except _error.BethkitNativeError as exc:
            raise _error.StringTableError(str(exc)) from exc
        try:
            editor._set_json(current.address, {"kind": "uint", "value": new_id})
        except Exception as edit_error:
            try:
                tables.remove(kind, new_id)
            except _error.BethkitNativeError as rollback_error:
                self.close()
                raise _error.StringTableError(
                    f"String edit and rollback failed: {rollback_error}"
                ) from edit_error
            raise
        self.__changed.add(current.address.form_id)

    def __finalize(self) -> bytes:
        """Finalizes validated records once and caches the serialized outputs.

        Returns:
            The encoded plugin, available for retrying a failed disk write.

        Raises:
            BethkitClosedError: The session is closed.
            BethkitNativeError: Record finalization or serialization failed.
        """

        self.__check_open()
        if self.__plugin_bytes is not None:
            return self.__plugin_bytes
        native_patcher = self.__patcher
        if native_patcher is None:
            raise _error.BethkitClosedError("No patcher is available.")
        self.__finalized = True
        try:
            for form_id, editor in self.__editors.items():
                if form_id in self.__changed:
                    with editor.finish() as record:
                        native_patcher.replace_record(form_id, record)
            if self.__localized and self.__tables is not None:
                self.__table_bytes = {
                    kind: self.__tables.table_to_bytes(kind)
                    for kind in _EXTENSIONS
                }
            self.__plugin_bytes = native_patcher.write_to_bytes()
            return self.__plugin_bytes
        except Exception:
            self.close()
            raise

    def save_bundle(
        self,
        output_dir: Path,
        plugin_name: str,
        *,
        language: str = "english",
    ) -> Path:
        """Publishes a new directory containing the plugin and all its tables.

        All files are staged in a sibling directory and exposed together by
        one directory rename. Existing output directories are rejected. This
        does not overwrite installed game files or claim transactional updates
        of multiple files in an existing Data directory. Saving finalizes the
        session; a failed disk write can be retried with the cached outputs.

        Args:
            output_dir: New output directory whose parent already exists.
            plugin_name: Plain plugin filename within that directory.
            language: Language suffix for the external string tables.

        Returns:
            Absolute path of the newly published bundle directory.

        Raises:
            BethkitClosedError: The session is closed.
            BethkitNativeError: Plugin or table serialization failed.
            FileExistsError: The output directory already exists.
            OSError: Staging, writing, or final publication failed.
            ValueError: A filename or language component is invalid.
        """

        self.__check_open()
        _validate_filename(plugin_name, language)
        destination = output_dir.absolute()
        if destination.exists():
            raise FileExistsError(destination)
        plugin_bytes = self.__finalize()
        payloads = {plugin_name: plugin_bytes}
        stem = Path(plugin_name).stem
        for kind, data in self.__table_bytes.items():
            payloads[f"Strings/{stem}_{language}.{_EXTENSIONS[kind]}"] = data
        manifest = _BundleManifest(
            format_version=1,
            plugin=plugin_name,
            language=language,
            schema_payload_sha256=self.__schema_hash,
            files=tuple(
                _BundleFile(
                    path=name,
                    size=len(data),
                    sha256=hashlib.sha256(data).hexdigest(),
                )
                for name, data in sorted(payloads.items())
            ),
        )
        payloads["manifest.json"] = manifest.model_dump_json(
            indent=4, by_alias=True, exclude_defaults=True
        ).encode("utf-8")
        with tempfile.TemporaryDirectory(
            prefix=f".{destination.name}-", dir=destination.parent
        ) as temporary:
            staging = Path(temporary)
            for name, data in payloads.items():
                file_path = staging / name
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with file_path.open("xb") as output:
                    output.write(data)
                    output.flush()
                    os.fsync(output.fileno())
            if destination.exists():
                raise FileExistsError(destination)
            staging.rename(destination)
        return destination

    def close(self) -> None:
        """Discards private edits and releases only session-owned resources."""

        if self.__closed:
            return
        self.__closed = True
        for editor in self.__editors.values():
            editor.close()
        if self.__patcher is not None:
            self.__patcher.close()
        if self.__tables is not None:
            self.__tables.close()

    def __enter__(self) -> LocalizationEditor:
        """Returns this open session for context-managed cleanup.

        Returns:
            This session instance.

        Raises:
            BethkitClosedError: The session has already closed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Discards native working state when leaving the context."""

        self.close()

    def __del__(self) -> None:
        """Performs best-effort cleanup of an abandoned session."""

        try:
            self.close()
        except Exception:
            pass
