"""Minimal-change writing of an existing plugin.

Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
from pathlib import Path

from bethkit import _error, _ffi
from bethkit.plugin import plugin as plugin_module
from bethkit.plugin import writer


class PluginPatcher:
    """Copies unchanged records and rewrites only explicit replacements.

    The native patcher takes an independent snapshot of its input. Closing
    the original plugin does not invalidate the patcher. Replacements are
    copied, so callers keep ownership of their writable records.
    """

    __pointer: int

    def __init__(self, plugin: plugin_module.Plugin) -> None:
        """Creates a patcher for an existing plugin.

        Args:
            plugin: Open plugin supplying the original file contents.

        Raises:
            BethkitClosedError: The input plugin is closed or transferred.
            BethkitNativeError: The native snapshot could not be created.
        """

        self.__pointer = 0
        pointer = plugin._native_pointer()
        lib = _ffi.load_lib()
        result = lib.bethkit_plugin_patcher_new(pointer)
        if not result:
            _ffi.raise_last_error(lib)
        self.__pointer = result

    def __check_open(self) -> int:
        """Returns the owned pointer while the patcher remains open.

        Returns:
            The live native patcher pointer.

        Raises:
            BethkitClosedError: The patcher is closed.
        """

        if not self.__pointer:
            raise _error.BethkitClosedError("PluginPatcher is closed.")
        return self.__pointer

    def close(self) -> None:
        """Releases the patcher; repeated calls are harmless."""

        if self.__pointer:
            _ffi.load_lib().bethkit_plugin_patcher_free(self.__pointer)
            self.__pointer = 0

    def replace_record(
        self, form_id: int, record: writer.WritableRecord
    ) -> None:
        """Replaces one existing record without consuming its Python owner.

        Args:
            form_id: Raw FormID identifying the existing source record.
            record: Complete replacement produced by a record editor.

        Raises:
            BethkitClosedError: The patcher or replacement record is closed.
            BethkitNativeError: The replacement is invalid or not found.
            ValueError: The FormID is outside the unsigned 32-bit range.
        """

        pointer = self.__check_open()
        if not 0 <= form_id <= 0xFFFFFFFF:
            raise ValueError("form_id must be an unsigned 32-bit integer.")
        record_pointer = record._native_pointer()
        lib = _ffi.load_lib()
        if (
            lib.bethkit_plugin_patcher_replace_record(
                pointer, form_id, record_pointer
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def write_to_bytes(self) -> bytes:
        """Serializes the original file with the requested replacements.

        Returns:
            Complete plugin bytes, preserving unchanged record payloads.

        Raises:
            BethkitClosedError: The patcher is closed.
            BethkitNativeError: The plugin cannot be serialized.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        result = ctypes.POINTER(ctypes.c_uint8)()
        length = ctypes.c_size_t()
        if (
            lib.bethkit_plugin_patcher_write_to_bytes(
                pointer, ctypes.byref(result), ctypes.byref(length)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        try:
            return bytes(ctypes.string_at(result, length.value))
        finally:
            lib.bethkit_bytes_free(result, length.value)

    def write_to_file(self, path: Path) -> None:
        """Writes the patched plugin to a destination path.

        Args:
            path: Destination plugin file.

        Raises:
            BethkitClosedError: The patcher is closed.
            BethkitNativeError: Serialization or file writing failed.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        if (
            lib.bethkit_plugin_patcher_write_to_file(pointer, _ffi.enc(path))
            != 0
        ):
            _ffi.raise_last_error(lib)

    def __enter__(self) -> PluginPatcher:
        """Returns the open patcher for a context-managed operation.

        Returns:
            This patcher instance.

        Raises:
            BethkitClosedError: The patcher is already closed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Releases the patcher when leaving a context."""

        self.close()

    def __del__(self) -> None:
        """Performs best-effort cleanup of an abandoned patcher."""

        try:
            self.close()
        except Exception:
            pass
