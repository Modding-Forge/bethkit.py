"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import uuid
from collections.abc import Iterator
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from .. import _ffi, _ownership
from .._error import BethkitClosedError, BethkitNativeError
from ..enums import Game, PluginKind

if TYPE_CHECKING:
    from ..schema import SemanticContext
    from ..strings import LocalizationSet, StringReference


class SubRecord(_ownership.BorrowedHandle):
    """
    A single sub-record field inside a :class:`Record`.

    Sub-records are borrowed from the parent ``Record`` and become
    invalid once the record is closed or freed.
    """

    def __init__(self, ptr: int, parent: Record) -> None:
        """
        Args:
            ptr (int): Native pointer to the underlying sub-record object.
            parent (Record): Owning record that keeps native memory alive.
        """

        super().__init__(ptr, parent)

    @property
    def signature(self) -> bytes:
        """
        Four-byte ASCII signature identifying the sub-record type.

        Returns:
            bytes: Four-byte signature (e.g. ``b"EDID"``).

        Raises:
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * 4)()
        if lib.bethkit_subrecord_signature(self._native_pointer(), buf) != 0:
            _ffi.raise_last_error(lib)
        return bytes(buf)

    @property
    def raw_bytes(self) -> bytes:  # type: ignore[return]
        """
        Raw byte content of the sub-record as stored in the plugin.

        Returns:
            bytes: Sub-record data, or ``b""`` if empty.
        """

        lib = _ffi.load_lib()
        sl = lib.bethkit_subrecord_bytes(self._native_pointer())
        if not sl.ptr:
            return b""
        return bytes(ctypes.string_at(sl.ptr, sl.len))

    def as_u8(self) -> int:
        """
        Interpret the sub-record data as an unsigned 8-bit integer.

        Returns:
            int: Decoded value.

        Raises:
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_uint8()
        if (
            lib.bethkit_subrecord_as_u8(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_u16(self) -> int:
        """
        Interpret the sub-record data as an unsigned 16-bit integer.

        Returns:
            int: Decoded value.

        Raises:
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_uint16()
        if (
            lib.bethkit_subrecord_as_u16(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_u32(self) -> int:
        """
        Interpret the sub-record data as an unsigned 32-bit integer.

        Returns:
            int: Decoded value.

        Raises:
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_uint32()
        if (
            lib.bethkit_subrecord_as_u32(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_f32(self) -> float:
        """
        Interpret the sub-record data as a 32-bit float.

        Returns:
            float: Decoded value.

        Raises:
            BethkitNativeError: If the data length does not match.
        """

        lib = _ffi.load_lib()
        out = ctypes.c_float()
        if (
            lib.bethkit_subrecord_as_f32(
                self._native_pointer(), ctypes.byref(out)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        return out.value

    def as_str(self) -> str:
        """
        Interpret the sub-record data as a null-terminated UTF-8 string.

        Returns:
            str: Decoded string.

        Raises:
            BethkitNativeError: If the data is not a valid null-terminated
                string.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_subrecord_as_zstring(self._native_pointer())
        if not ptr:
            _ffi.raise_last_error(lib)
        try:
            return ctypes.string_at(ptr).decode("utf-8")
        finally:
            lib.bethkit_zstring_free(ptr)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation showing the signature.
        """

        try:
            sig = self.signature.decode("ascii", errors="replace")
        except BethkitNativeError:
            sig = "?"
        return f"<SubRecord {sig!r}>"


class Record(_ownership.BorrowedHandle):
    """
    A single plugin record containing sub-records.

    Records are owned by their parent :class:`Group` or
    :class:`PluginCache` and must not outlive it.

    Access after the native owner closes raises ``BethkitClosedError``.
    """

    def __init__(self, ptr: int, parent: _ownership.BorrowOwner) -> None:
        """
        Args:
            ptr (int): Native pointer to the underlying record object.
            parent (object): Owner that keeps native memory alive.
        """

        super().__init__(ptr, parent)

    @property
    def signature(self) -> bytes:
        """
        Four-byte ASCII record type signature.

        Returns:
            bytes: Four-byte signature (e.g. ``b"NPC_"``).

        Raises:
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * 4)()
        if lib.bethkit_record_signature(self._native_pointer(), buf) != 0:
            _ffi.raise_last_error(lib)
        return bytes(buf)

    @property
    def form_id(self) -> int:
        """
        Raw 32-bit FormID of the record as stored in the plugin.

        Returns:
            int: FormID value.
        """

        return _ffi.load_lib().bethkit_record_form_id(self._native_pointer())

    @property
    def flags(self) -> int:
        """
        Record header flags bitmask.

        Returns:
            int: Flags value.
        """

        return _ffi.load_lib().bethkit_record_flags(self._native_pointer())

    @property
    def form_version(self) -> int:
        """
        Form version stored in the record header.

        Returns:
            int: Form version number.
        """

        return _ffi.load_lib().bethkit_record_form_version(
            self._native_pointer()
        )

    @property
    def editor_id(self) -> Optional[str]:
        """
        Editor ID string (EDID sub-record), if present.

        Returns:
            Optional[str]: The editor ID, or ``None`` if absent.
        """

        lib = _ffi.load_lib()
        ptr = ctypes.c_void_p()
        status = lib.bethkit_record_editor_id_status(
            self._native_pointer(), ctypes.byref(ptr)
        )
        if status == 1:
            return None
        if status != 0:
            _ffi.raise_last_error(lib)
        try:
            return ctypes.string_at(ptr).decode("utf-8")
        finally:
            lib.bethkit_record_editor_id_free(ptr)

    def subrecord_count(self) -> int:
        """
        Return the number of sub-records in this record.

        Returns:
            int: Sub-record count.

        Raises:
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        n = lib.bethkit_record_subrecord_count(self._native_pointer())
        if n < 0:
            _ffi.raise_last_error(lib)
        return n

    def subrecord_at(self, index: int) -> SubRecord:
        """
        Return the sub-record at the given index.

        Args:
            index (int): Zero-based sub-record index.

        Returns:
            SubRecord: Borrowed sub-record.

        Raises:
            BethkitNativeError: If *index* is out of range.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_record_subrecord_get(self._native_pointer(), index)
        if not ptr:
            _ffi.raise_last_error(lib)
        return SubRecord(ptr, self)

    def find_subrecord(self, sig: bytes | str) -> Optional[SubRecord]:
        """
        Find the first sub-record matching the given 4-byte signature.

        Args:
            sig (bytes | str): Four-byte signature to search for.

        Returns:
            Optional[SubRecord]: The first matching sub-record, or ``None``.

        Raises:
            ValueError: If *sig* is not exactly 4 bytes.
        """

        if isinstance(sig, str):
            sig = sig.encode("ascii")
        if len(sig) != 4:
            raise ValueError("sig must be exactly 4 bytes")
        lib = _ffi.load_lib()
        buf = (ctypes.c_uint8 * 4)(*sig)
        ptr = lib.bethkit_record_subrecord_find(self._native_pointer(), buf)
        if not ptr:
            return None
        return SubRecord(ptr, self)

    def __iter__(self) -> Iterator[SubRecord]:
        """
        Iterate over all sub-records in this record.

        Yields:
            SubRecord: Each sub-record in order.
        """

        for i in range(self.subrecord_count()):
            yield self.subrecord_at(i)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with signature and FormID.
        """

        try:
            sig = self.signature.decode("ascii", errors="replace")
            fid = self.form_id
        except BethkitNativeError:
            return "<Record ?>"
        return f"<Record {sig!r} FormID=0x{fid:08X}>"


class Group(_ownership.BorrowedHandle):
    """
    A top-level group inside a plugin, containing records or sub-groups.

    Groups are the primary organisational unit in Bethesda plugin files.
    They may contain :class:`Record` children or nested :class:`Group`
    children.

    Access after the native owner closes raises ``BethkitClosedError``.
    """

    def __init__(self, ptr: int, parent: Plugin | Group) -> None:
        """
        Args:
            ptr (int): Native pointer to the underlying group object.
            parent (Plugin | Group): Owner that keeps native memory alive.
        """

        super().__init__(ptr, parent)

    @property
    def group_type(self) -> int:
        """
        Numeric group type code as defined in the plugin format.

        Returns:
            int: Group type (e.g. ``0`` for top-level groups).

        Raises:
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        t = lib.bethkit_group_type(self._native_pointer())
        if t < 0:
            _ffi.raise_last_error(lib)
        return t

    @property
    def child_count(self) -> int:
        """
        Total number of direct children (records and sub-groups).

        Returns:
            int: Child count.
        """

        return _ffi.load_lib().bethkit_group_child_count(self._native_pointer())

    def child_is_record(self, index: int) -> bool:
        """
        Return whether the child at *index* is a record (vs. a group).

        Args:
            index (int): Zero-based child index.

        Returns:
            bool: ``True`` if the child is a :class:`Record`.
        """

        return bool(
            _ffi.load_lib().bethkit_group_child_is_record(
                self._native_pointer(), index
            )
        )

    def child_as_record(self, index: int) -> Optional[Record]:
        """
        Return the child at *index* as a :class:`Record`.

        Args:
            index (int): Zero-based child index.

        Returns:
            Optional[Record]: The child record, or ``None`` if the child is
            a group or the index is out of range.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_group_child_as_record(self._native_pointer(), index)
        if not ptr:
            return None
        return Record(ptr, self)

    def child_as_group(self, index: int) -> Optional[Group]:
        """
        Return the child at *index* as a :class:`Group`.

        Args:
            index (int): Zero-based child index.

        Returns:
            Optional[Group]: The child group, or ``None`` if the child is
            a record or the index is out of range.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_group_child_as_group(self._native_pointer(), index)
        if not ptr:
            return None
        return Group(ptr, self)

    def __iter__(self) -> Iterator[Record | Group]:
        """
        Iterate over all direct children of this group.

        Yields:
            Record | Group: Each child in order.

        Raises:
            BethkitClosedError: If the owner closes during iteration.
        """

        lib = _ffi.load_lib()
        for i in range(self.child_count):
            if lib.bethkit_group_child_is_record(self._native_pointer(), i):
                ptr = lib.bethkit_group_child_as_record(
                    self._native_pointer(), i
                )
                if ptr:
                    yield Record(ptr, self)
            else:
                ptr = lib.bethkit_group_child_as_group(
                    self._native_pointer(), i
                )
                if ptr:
                    yield Group(ptr, self)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation showing type and count.
        """

        try:
            return f"<Group type={self.group_type} children={self.child_count}>"
        except BethkitNativeError:
            return "<Group ?>"


class Plugin:
    """
    An open Bethesda plugin file (ESP, ESM, or ESL).

    Use as a context manager to guarantee that the native handle is freed
    even on error::

        with Plugin.open(Path("Skyrim.esm"), Game.SKYRIM_SE) as p:
            for group in p:
                for child in group:
                    if isinstance(child, Record):
                        print(child.editor_id)
    """

    __ptr: int
    __borrow_owner: Optional[_ownership.BorrowOwner]
    __source_name: Optional[str]
    __reference_token: uuid.UUID

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI open call.
        """

        self.__ptr = ptr
        self.__borrow_owner = None
        self.__source_name = None
        self.__reference_token = uuid.uuid4()

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
        """
        Return the native pointer, raising if the handle has been closed.

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
        """
        Open a plugin file from disk.

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
        result = cls(ptr)
        result.__source_name = path.name
        return result

    @classmethod
    def from_bytes(
        cls, data: bytes, game: Game, *, name: Optional[str] = None
    ) -> Plugin:
        """
        Parse a plugin from an in-memory byte buffer.

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
        result = cls(ptr)
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
        """
        Release the native plugin handle.

        Safe to call multiple times; subsequent calls are no-ops.

        Borrowed records, groups, and subrecords raise ``BethkitClosedError``
        after the native owner closes. Transferred plugins remain owned by
        their receiving cache.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_plugin_free(self.__ptr)
            self.__ptr = 0

    def _transfer_ptr(self) -> int:
        """
        Transfer ownership of the native handle to the caller.

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
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Close the plugin when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    @property
    def kind(self) -> PluginKind:
        """
        Plugin type as declared in the file header.

        Returns:
            PluginKind: ``FULL``, ``LIGHT``, or ``OVERLAY``.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return PluginKind(
            _ffi.load_lib().bethkit_plugin_kind(self.__check_open())
        )

    @property
    def is_localized(self) -> bool:
        """
        Whether the plugin uses external string localisation files.

        Returns:
            bool: ``True`` if the plugin sets the localised flag.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return bool(
            _ffi.load_lib().bethkit_plugin_is_localized(self.__check_open())
        )

    @property
    def description(self) -> Optional[str]:
        """
        Plugin description from the SNAM sub-record, if present.

        Returns:
            Optional[str]: Description string, or ``None`` if absent.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        lib = _ffi.load_lib()
        raw: Optional[bytes] = lib.bethkit_plugin_description(
            self.__check_open()
        )
        return raw.decode("utf-8") if raw else None

    @property
    def master_count(self) -> int:
        """
        Number of master plugin dependencies declared in the header.

        Returns:
            int: Master count.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return _ffi.load_lib().bethkit_plugin_master_count(self.__check_open())

    def master_at(self, index: int) -> str:
        """
        Return the master plugin name at the given index.

        Args:
            index (int): Zero-based master index.

        Returns:
            str: Master file name (e.g. ``"Skyrim.esm"``).

        Raises:
            BethkitClosedError: If the plugin has been closed.
            BethkitNativeError: If *index* is out of range.
        """

        lib = _ffi.load_lib()
        raw: Optional[bytes] = lib.bethkit_plugin_master_get(
            self.__check_open(), index
        )
        if raw is None:
            _ffi.raise_last_error(lib)
        return raw.decode("utf-8")  # type: ignore[union-attr]

    @property
    def masters(self) -> list[str]:
        """
        All master plugin names in load order.

        Returns:
            list[str]: Ordered list of master file names.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return [self.master_at(i) for i in range(self.master_count)]

    @property
    def group_count(self) -> int:
        """
        Number of top-level groups in the plugin.

        Returns:
            int: Group count.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return _ffi.load_lib().bethkit_plugin_group_count(self.__check_open())

    def group_at(self, index: int) -> Group:
        """
        Return the top-level group at the given index.

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
        return Group(ptr, self)

    @property
    def groups(self) -> Iterator[Group]:
        """
        Iterate over all top-level groups.

        Yields:
            Group: Each top-level group in order.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        for i in range(self.group_count):
            yield self.group_at(i)

    def __iter__(self) -> Iterator[Group]:
        """
        Iterate over all top-level groups (alias for :attr:`groups`).

        Yields:
            Group: Each top-level group in order.
        """

        return self.groups

    def find_record(self, form_id: int) -> Optional[Record]:
        """
        Search for a record by its raw 32-bit FormID.

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
        return Record(ptr, self)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with kind and group count.
        """

        if not self.__ptr:
            return "<Plugin closed>"
        try:
            return f"<Plugin kind={self.kind.name} groups={self.group_count}>"
        except BethkitNativeError:
            return "<Plugin ?>"
