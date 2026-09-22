"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import logging
import uuid
from collections.abc import Iterator
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Optional

from .. import _ffi, _ownership
from .._error import BethkitClosedError, BethkitNativeError
from ..enums import Game

if TYPE_CHECKING:
    from ..schema import SemanticContext
    from ..strings import LocalizationSet, StringReference


from ._metadata import PluginMetadata
from .group import Group as Group
from .record import Record as Record
from .subrecord import SubRecord as SubRecord


class Plugin(PluginMetadata):
    """An open Bethesda plugin file (ESP, ESM, or ESL).

    Use as a context manager to guarantee that the native handle is freed
    even on error::

        with Plugin.open(Path("Skyrim.esm"), Game.SKYRIM_SE) as p:
            for group in p:
                for child in group:
                    if isinstance(child, Record):
                        print(child.editor_id)
    """

    log: ClassVar[logging.Logger] = logging.getLogger("Plugin")
    __ptr: int = 0
    __borrow_owner: Optional[_ownership.BorrowOwner]
    __source_name: Optional[str]
    __reference_token: uuid.UUID

    def __init__(self) -> None:
        """Rejects direct construction of an owned native handle.

        Raises:
            TypeError: Always; use this class's public creation methods.
        """

        raise TypeError("Use Plugin's public creation methods.")

    @classmethod
    def _from_native(cls, pointer: int) -> Plugin:
        """Adopts a native allocation returned by a successful FFI call.

        Args:
            pointer: Nonzero native pointer whose ownership is transferred.

        Returns:
            A wrapper responsible for freeing the allocation exactly once.

        Raises:
            ValueError: The supplied native pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot adopt a null Plugin pointer.")
        result = cls.__new__(cls)
        result.__borrow_owner = None
        result.__source_name = None
        result.__reference_token = uuid.uuid4()
        result.__ptr = pointer
        return result

    @property
    def source_name(self) -> Optional[str]:
        """Returns the filename identity, when provided by the caller.

        Returns:
            The opened filename or the name supplied to ``from_bytes``.
        """

        return self.__source_name

    def _reference_identity(self) -> uuid.UUID:
        """Returns a session-local token for rejecting foreign references.

        Returns:
            This plugin wrapper's opaque identity, never a native handle.
        """

        return self.__reference_token

    def _check_borrowed(self) -> None:
        """Checks the plugin's current native memory owner.

        Raises:
            BethkitClosedError: If the plugin or its receiving cache closed.
        """

        if self.__borrow_owner is not None:
            self.__borrow_owner._check_borrowed()
        else:
            self.__check_open()

    def _native_pointer(self) -> int:
        """Returns this plugin's owned pointer for private FFI operations.

        Returns:
            The pointer owned by this open plugin wrapper.

        Raises:
            BethkitClosedError: If the plugin has closed or transferred.
        """

        return self.__check_open()

    def _set_borrow_owner(self, owner: _ownership.BorrowOwner) -> None:
        """Keeps the receiving cache alive after successful ownership transfer.

        Args:
            owner: Cache that now owns the plugin's native memory.
        """

        self.__borrow_owner = owner

    def __check_open(self) -> int:
        """Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the plugin has been closed or transferred.
        """

        if not self.__ptr:
            raise BethkitClosedError("Plugin is closed")
        return self.__ptr

    @classmethod
    def open(cls, path: Path, game: Game) -> Plugin:
        """Open a plugin file from disk.

        Args:
            path (Path): Filesystem path to the ``.esp``, ``.esm``, or
                ``.esl`` file.
            game (Game): Target game; selects the correct format variant.

        Returns:
            Plugin: A new ``Plugin`` wrapping the open file.

        Raises:
            BethkitNativeError: If the file cannot be opened or parsed.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_plugin_open(_ffi.enc(path), int(game))
        if not ptr:
            _ffi.raise_last_error(lib)
        result = _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_plugin_free
        )
        result.__source_name = path.name
        return result

    @classmethod
    def from_bytes(
        cls, data: bytes, game: Game, *, name: Optional[str] = None
    ) -> Plugin:
        """Parse a plugin from an in-memory byte buffer.

        Args:
            data (bytes): Raw plugin file contents.
            game (Game): Target game; selects the correct format variant.
            name: Optional filename identity for persistent string references.

        Returns:
            Plugin: A new ``Plugin`` parsed from *data*.

        Raises:
            BethkitNativeError: If parsing fails.
        """

        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
        ptr = lib.bethkit_plugin_open_from_bytes(buf, len(data), int(game))
        if not ptr:
            _ffi.raise_last_error(lib)
        result = _ownership.adopt_native(
            ptr, cls._from_native, lib.bethkit_plugin_free
        )
        result.__source_name = name
        return result

    def iter_strings(
        self,
        context: SemanticContext,
        tables: Optional[LocalizationSet] = None,
    ) -> Iterator[StringReference]:
        """Lazily enumerates schema-declared, positionally identified text.

        Args:
            context: Semantic runtime matching this plugin's game schema.
            tables: Optional tables for resolving externally stored text.

        Returns:
            An iterator decoding only the current record's string fields.

        Raises:
            BethkitClosedError: A native owner closes during iteration.
            RecordDecodeError: A source record cannot be decoded.
            StringTableError: A supplied table cannot resolve a string ID.
        """

        from ..strings import references

        return references.iter_strings(self, context, tables)

    def close(self) -> None:
        """Release the native plugin handle.

        Safe to call multiple times; subsequent calls are no-ops.

        Borrowed records, groups, and subrecords raise ``BethkitClosedError``
        after the native owner closes. Transferred plugins remain owned by
        their receiving cache.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_plugin_free(pointer)

    def _transfer_ptr(self) -> int:
        """Transfer ownership of the native handle to the caller.

        After this call the wrapper is closed (``__ptr`` is set to ``0``).
        Called by :class:`PluginCache` when it takes ownership of the plugin.

        Returns:
            int: The raw native pointer.

        Raises:
            BethkitClosedError: If the plugin has already been closed or
                transferred.
        """

        ptr = self.__check_open()
        self.__ptr = 0
        return ptr

    def __enter__(self) -> Plugin:
        """Returns this open owner for use as a context manager.

        Returns:
            This instance, valid until the context exits or it is closed.

        Raises:
            BethkitClosedError: This owner is already closed or transferred.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Close the plugin when exiting the context.

        Args:
            *_: Exception details supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    @property
    def group_count(self) -> int:
        """Number of top-level groups in the plugin.

        Returns:
            int: Group count.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return _ffi.load_lib().bethkit_plugin_group_count(self.__check_open())

    def group_at(self, index: int) -> Group:
        """Return the top-level group at the given index.

        Args:
            index (int): Zero-based group index.

        Returns:
            Group: Borrowed group object.

        Raises:
            BethkitClosedError: If the plugin has been closed.
            BethkitNativeError: If *index* is out of range.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_plugin_group_get(self.__check_open(), index)
        if not ptr:
            _ffi.raise_last_error(lib)
        return Group._from_native(ptr, self)

    @property
    def groups(self) -> Iterator[Group]:
        """Iterate over all top-level groups.

        Yields:
            Group: Each top-level group in order.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        for i in range(self.group_count):
            yield self.group_at(i)

    def __iter__(self) -> Iterator[Group]:
        """Iterate over all top-level groups (alias for :attr:`groups`).

        Returns:
            An iterator over each top-level group in order.

        Raises:
            BethkitClosedError: The plugin closes during iteration.
            BethkitNativeError: A group cannot be read during iteration.
        """

        return self.groups

    def find_record(self, form_id: int) -> Optional[Record]:
        """Search for a record by its raw 32-bit FormID.

        Args:
            form_id (int): The raw FormID to look up.

        Returns:
            Optional[Record]: The matching record, or ``None`` if not found.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_plugin_find_record(self.__check_open(), form_id)
        if not ptr:
            return None
        return Record._from_native(ptr, self)

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation with kind and group count.
        """

        if not self.__ptr:
            return "<Plugin closed>"
        try:
            return f"<Plugin kind={self.kind.name} groups={self.group_count}>"
        except BethkitNativeError:
            return "<Plugin ?>"
