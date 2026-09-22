"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import logging
from pathlib import Path
from typing import ClassVar, Optional

from .. import _ffi, _ownership
from .._error import BethkitClosedError
from ..enums import Game
from .writable_group import WritableGroup as WritableGroup
from .writable_record import WritableRecord as WritableRecord

_HEDR_VERSION: dict[Game, float] = {
    Game.SKYRIM_SE: 1.7,
    Game.SKYRIM_VR: 1.7,
    Game.FALLOUT4: 0.95,
    Game.FALLOUT4_VR: 0.95,
    Game.SKYRIM_LE: 0.94,
    Game.FALLOUT3: 0.94,
    Game.FALLOUT_NV: 0.94,
    Game.OBLIVION: 0.8,
    Game.MORROWIND: 1.3,
    Game.FALLOUT76: 1.0,
    Game.STARFIELD: 1.0,
}


class PluginWriter:
    """Assembles and serialises a complete plugin file.

    Add top-level groups with :meth:`add_group`, then call
    :meth:`write_to_file` or :meth:`write_to_bytes` to produce the
    finished plugin.
    """

    log: ClassVar[logging.Logger] = logging.getLogger("PluginWriter")
    __ptr: int = 0

    def __init__(
        self, game: Game, hedr_version: Optional[float] = None
    ) -> None:
        """Creates an empty native owner with the requested configuration.

        Args:
            game (Game): Target game; determines the correct format.
            hedr_version (Optional[float]): HEDR version float written to
                the TES4 plugin header.  When ``None`` (the default), the
                canonical version for *game* is used (e.g. ``1.7`` for
                Skyrim SE, ``0.95`` for Fallout 4, ``0.94`` for Skyrim LE /
                Fallout 3 / Fallout NV).

        Raises:
            BethkitNativeError: If the native writer cannot be created.
        """

        if hedr_version is None:
            hedr_version = _HEDR_VERSION.get(game, 0.94)
        lib = _ffi.load_lib()
        ptr = lib.bethkit_plugin_writer_new(int(game), hedr_version)
        if not ptr:
            _ffi.raise_last_error(lib)
        self.__ptr = ptr

    def __check_open(self) -> int:
        """Return the native pointer, raising if the handle has been closed.

        Returns:
            int: Valid native pointer.

        Raises:
            BethkitClosedError: If the writer has been closed.
        """

        if not self.__ptr:
            raise BethkitClosedError("PluginWriter is closed")
        return self.__ptr

    def close(self) -> None:
        """Release the native writer handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_plugin_writer_free(pointer)

    def __enter__(self) -> PluginWriter:
        """Returns this open owner for use as a context manager.

        Returns:
            This instance, valid until the context exits or it is closed.

        Raises:
            BethkitClosedError: This owner is already closed or transferred.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Free the writer when exiting the context.

        Args:
            *_: Exception details supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    def add_group(self, group: WritableGroup) -> None:
        """Append a top-level group to the plugin, transferring ownership.

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
        writer_ptr = self.__check_open()
        grp_ptr = group._transfer_ptr()
        if lib.bethkit_plugin_writer_add_group(writer_ptr, grp_ptr) != 0:
            _ffi.raise_last_error(lib)

    def write_to_file(self, path: Path) -> None:
        """Serialise and write the plugin to *path* on disk.

        Args:
            path (Path): Destination file path.

        Raises:
            BethkitClosedError: If the writer has been closed.
            BethkitNativeError: If serialisation or the write fails.
        """

        lib = _ffi.load_lib()
        if (
            lib.bethkit_plugin_writer_write_to_file(
                self.__check_open(), _ffi.enc(path)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def add_master(self, name: str) -> None:
        """Appends a master dependency to the plugin header.

        Args:
            name: Master plugin filename, such as ``Skyrim.esm``.

        Raises:
            BethkitClosedError: The writer is closed.
            BethkitNativeError: The native writer rejected the dependency.
            ValueError: The filename contains a NUL character.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        if lib.bethkit_plugin_writer_add_master(pointer, _ffi.senc(name)) != 0:
            _ffi.raise_last_error(lib)

    def set_description(self, description: str) -> None:
        """Sets the plugin description in the TES4 header.

        Args:
            description: Description text to write.

        Raises:
            BethkitClosedError: The writer is closed.
            BethkitNativeError: The native writer rejected the description.
            ValueError: The description contains a NUL character.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        if (
            lib.bethkit_plugin_writer_set_description(
                pointer, _ffi.senc(description)
            )
            != 0
        ):
            _ffi.raise_last_error(lib)

    def set_localized(self, localized: bool) -> None:
        """Sets whether translatable fields contain external string IDs.

        This changes the header flag only. Callers must also supply matching
        string IDs and save the corresponding localization tables.

        Args:
            localized: Whether the plugin uses external string tables.

        Raises:
            BethkitClosedError: The writer is closed.
            BethkitNativeError: The native writer rejected the flag.
        """

        pointer = self.__check_open()
        lib = _ffi.load_lib()
        if lib.bethkit_plugin_writer_set_localized(pointer, localized) != 0:
            _ffi.raise_last_error(lib)

    def write_to_bytes(self) -> bytes:
        """Serialise the plugin and return it as a byte buffer.

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
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation of the writer.
        """

        return "<PluginWriter>"
