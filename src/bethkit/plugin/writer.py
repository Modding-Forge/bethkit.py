"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
from pathlib import Path

from .. import _ffi
from .._error import BethkitClosedError, BethkitOwnershipError
from ..enums import Game


def _sig_buf(sig: bytes | str) -> ctypes.Array[ctypes.c_uint8]:
    """
    Convert a 4-byte signature to a ctypes ``c_uint8`` array.

    Args:
        sig (bytes | str): Four-byte ASCII signature.

    Returns:
        ctypes.Array: A ``c_uint8[4]`` array containing the signature.

    Raises:
        ValueError: If *sig* is not exactly 4 bytes.
    """

    if isinstance(sig, str):
        sig = sig.encode("ascii")
    if len(sig) != 4:
        raise ValueError("signature must be exactly 4 bytes")
    return (ctypes.c_uint8 * 4)(*sig)


class WritableRecord:
    """
    A plugin record under construction.

    Create via :meth:`new`, add sub-records with :meth:`add_subrecord`,
    then hand the record off to a :class:`WritableGroup` with
    :meth:`WritableGroup.add_record`.  Ownership transfers on that call
    and this wrapper becomes invalid.

    Use as a context manager to free the handle if the record is never
    added to a group::

        with WritableRecord.new(b"NPC_") as rec:
            rec.add_subrecord(b"EDID", b"MyNPC\x00")
            group.add_record(rec)
    """

    __ptr: int

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI new call.
        """

        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the record has been closed or transferred.
        """

        if not self.__ptr:
            raise BethkitClosedError("WritableRecord is closed or transferred")
        return self.__ptr

    def _transfer_ptr(self) -> int:
        """
        Transfer ownership to the caller.

        Returns:
            int: The raw native pointer.

        Raises:
            BethkitOwnershipError: If the record has already been transferred
                or closed.
        """

        if not self.__ptr:
            raise BethkitOwnershipError(
                "WritableRecord has already been transferred or closed"
            )
        ptr = self.__ptr
        self.__ptr = 0
        return ptr

    @classmethod
    def new(
        cls,
        signature: bytes | str,
        flags: int = 0,
        form_id: int = 0,
        form_version: int = 44,
    ) -> WritableRecord:
        """
        Create a new writable record with the given header fields.

        Args:
            signature (bytes | str): Four-byte record type signature.
            flags (int): Record header flags bitmask. Defaults to ``0``.
            form_id (int): Raw FormID. Defaults to ``0``.
            form_version (int): Form version. Defaults to ``44``.

        Returns:
            WritableRecord: A new, empty record.

        Raises:
            BethkitNativeError: If the native record cannot be created.
            ValueError: If *signature* is not exactly 4 bytes.
        """

        lib = _ffi.load_lib()
        buf = _sig_buf(signature)
        ptr = lib.bethkit_writable_record_new(
            buf, flags, form_id, form_version
        )
        if not ptr:
            _ffi.raise_last_error(lib)
        return cls(ptr)

    def close(self) -> None:
        """
        Release the native record handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_writable_record_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> WritableRecord:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the record when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def add_subrecord(
        self, signature: bytes | str, data: bytes
    ) -> None:
        """
        Append a sub-record to this record.

        Args:
            signature (bytes | str): Four-byte sub-record type signature.
            data (bytes): Raw sub-record payload.

        Raises:
            BethkitClosedError: If the record has been closed or transferred.
            BethkitNativeError: If the native call fails.
            ValueError: If *signature* is not exactly 4 bytes.
        """

        lib = _ffi.load_lib()
        sig_buf = _sig_buf(signature)
        data_buf = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
        if (
            lib.bethkit_writable_record_add_subrecord(
                self.__check_open(), sig_buf, data_buf, len(data)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with native pointer.
        """

        if not self.__ptr:
            return "<WritableRecord transferred>"
        return f"<WritableRecord ptr=0x{self.__ptr:016X}>"


class WritableGroup:
    """
    A plugin group under construction.

    Add records with :meth:`add_record` and sub-groups with
    :meth:`add_group`, then hand the group off to a
    :class:`PluginWriter` with :meth:`PluginWriter.add_group`.
    Ownership transfers on that call.
    """

    __ptr: int

    def __init__(self, ptr: int) -> None:
        """
        Args:
            ptr (int): Native handle returned by the FFI new call.
        """

        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the group has been closed or transferred.
        """

        if not self.__ptr:
            raise BethkitClosedError("WritableGroup is closed or transferred")
        return self.__ptr

    def _transfer_ptr(self) -> int:
        """
        Transfer ownership to the caller.

        Returns:
            int: The raw native pointer.

        Raises:
            BethkitOwnershipError: If the group has already been transferred
                or closed.
        """

        if not self.__ptr:
            raise BethkitOwnershipError(
                "WritableGroup has already been transferred or closed"
            )
        ptr = self.__ptr
        self.__ptr = 0
        return ptr

    @classmethod
    def new(
        cls, label: bytes | str, group_type: int = 0
    ) -> WritableGroup:
        """
        Create a new writable group.

        Args:
            label (bytes | str): Four-byte group label (top-level
                groups use a record-type signature).
            group_type (int): Numeric group type. Defaults to ``0``
                (top-level).

        Returns:
            WritableGroup: A new, empty group.

        Raises:
            BethkitNativeError: If the native group cannot be created.
            ValueError: If *label* is not exactly 4 bytes.
        """

        lib = _ffi.load_lib()
        buf = _sig_buf(label)
        ptr = lib.bethkit_writable_group_new(buf, group_type)
        if not ptr:
            _ffi.raise_last_error(lib)
        return cls(ptr)

    def close(self) -> None:
        """
        Release the native group handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_writable_group_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> WritableGroup:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the group when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def add_record(self, record: WritableRecord) -> None:
        """
        Append a record to this group, transferring ownership.

        After this call *record* is invalid.

        Args:
            record (WritableRecord): The record to add.

        Raises:
            BethkitClosedError: If this group has been closed or transferred.
            BethkitOwnershipError: If *record* has already been transferred
                or closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        rec_ptr = record._transfer_ptr()
        if lib.bethkit_writable_group_add_record(
            self.__check_open(), rec_ptr
        ) != 0:
            _ffi.raise_last_error(lib)

    def add_group(self, child: WritableGroup) -> None:
        """
        Append a sub-group to this group, transferring ownership.

        After this call *child* is invalid.

        Args:
            child (WritableGroup): The sub-group to add.

        Raises:
            BethkitClosedError: If this group has been closed or transferred.
            BethkitOwnershipError: If *child* has already been transferred
                or closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        child_ptr = child._transfer_ptr()
        if lib.bethkit_writable_group_add_group(
            self.__check_open(), child_ptr
        ) != 0:
            _ffi.raise_last_error(lib)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with native pointer.
        """

        if not self.__ptr:
            return "<WritableGroup transferred>"
        return f"<WritableGroup ptr=0x{self.__ptr:016X}>"


class PluginWriter:
    """
    Assembles and serialises a complete plugin file.

    Add top-level groups with :meth:`add_group`, then call
    :meth:`write_to_file` or :meth:`write_to_bytes` to produce the
    finished plugin.
    """

    __ptr: int

    def __init__(self, game: Game, form_version: int = 44) -> None:
        """
        Args:
            game (Game): Target game; determines the correct format.
            form_version (int): Default form version written to record
                headers. Defaults to ``44`` (Skyrim SE).

        Raises:
            BethkitNativeError: If the native writer cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_plugin_writer_new(int(game), form_version)
        if not ptr:
            _ffi.raise_last_error(lib)
        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the writer has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("PluginWriter is closed")
        return self.__ptr

    def close(self) -> None:
        """
        Release the native writer handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_plugin_writer_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> PluginWriter:
        """Return *self* for use as a context manager."""

        return self

    def __exit__(self, *_: object) -> None:
        """Free the writer when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def add_group(self, group: WritableGroup) -> None:
        """
        Append a top-level group to the plugin, transferring ownership.

        After this call *group* is invalid.

        Args:
            group (WritableGroup): The group to add.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitOwnershipError: If *group* has already been transferred
                or closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        grp_ptr = group._transfer_ptr()
        if lib.bethkit_plugin_writer_add_group(
            self.__check_open(), grp_ptr
        ) != 0:
            _ffi.raise_last_error(lib)

    def write_to_file(self, path: Path) -> None:
        """
        Serialise and write the plugin to *path* on disk.

        Args:
            path (Path): Destination file path.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If serialisation or the write fails.
        """

        lib = _ffi.load_lib()
        if lib.bethkit_plugin_writer_write_to_file(
            self.__check_open(), _ffi.enc(path)
        ) != 0:
            _ffi.raise_last_error(lib)

    def write_to_bytes(self) -> bytes:
        """
        Serialise the plugin and return it as a byte buffer.

        Returns:
            bytes: Complete serialised plugin data.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If serialisation fails.
        """

        lib = _ffi.load_lib()
        out_len = ctypes.c_size_t(0)
        ptr = lib.bethkit_plugin_writer_write_to_bytes(
            self.__check_open(), ctypes.byref(out_len)
        )
        if not ptr:
            _ffi.raise_last_error(lib)
        try:
            return bytes(ctypes.string_at(ptr, out_len.value))
        finally:
            lib.bethkit_bytes_free(ptr, out_len.value)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation of the writer.
        """

        return "<PluginWriter>"
