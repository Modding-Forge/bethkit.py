"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import logging
from typing import TYPE_CHECKING, ClassVar, Optional

from . import _ffi, _ownership
from ._error import BethkitClosedError
from ._ffi import BethkitGlobalFormId
from .enums import PluginKind
from .global_form_id import GlobalFormId as GlobalFormId

if TYPE_CHECKING:
    from .plugin.plugin import Plugin


class LoadOrder:
    """
    An ordered list of plugins that mirrors the active load order.

    Use :meth:`push` to register plugins in load order, then call
    :meth:`resolve` to translate a local FormID into a
    :class:`GlobalFormId`.

    Use as a context manager to guarantee that the native handle is
    freed::

        with LoadOrder() as lo:
            lo.push("Skyrim.esm", PluginKind.FULL)
            gfid = lo.resolve(0x00012E49, "Skyrim.esm")
    """

    log: ClassVar[logging.Logger] = logging.getLogger("LoadOrder")
    __ptr: int = 0

    def __init__(self) -> None:
        """Creates an empty native load order owned by this instance.

        Raises:
            BethkitNativeError: If the native load-order object cannot be
                created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_load_order_new()
        if not ptr:
            _ffi.raise_last_error(lib)
        self.__ptr = ptr

    def __check_open(self) -> int:
        """
        Returns the native pointer, raising if the handle is already closed.

        Returns:
            int: Non-zero native pointer.

        Raises:
            BethkitClosedError: If :meth:`close` has already been called.
        """

        if not self.__ptr:
            raise BethkitClosedError("LoadOrder has already been closed.")
        return self.__ptr

    def close(self) -> None:
        """
        Releases the native load-order handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_load_order_free(pointer)

    def __enter__(self) -> LoadOrder:
        """
        Returns *self* for use as a context manager.

        Returns:
            LoadOrder: This instance.

        Raises:
            BethkitClosedError: This load order is closed.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Closes the load order when exiting the context.

        Args:
            *_: Exception information supplied by the context manager.
        """

        self.close()

    def __del__(self) -> None:
        """Frees the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    def push(self, name: str, kind: PluginKind) -> None:
        """
        Appends a plugin to the end of the load order.

        Args:
            name (str): Plugin file name (e.g. ``"Skyrim.esm"``).
            kind (PluginKind): Whether the plugin is a full, light, or
                overlay plugin.

        Raises:
            BethkitClosedError: If this load order has already been closed.
            BethkitNativeError: If the native call fails.
            ValueError: The plugin name contains a NUL character.
            UnicodeEncodeError: The plugin name contains an unpaired surrogate.
        """

        lib = _ffi.load_lib()
        ptr = self.__check_open()
        if lib.bethkit_load_order_push(ptr, _ffi.senc(name), int(kind)) != 0:
            _ffi.raise_last_error(lib)

    def __len__(self) -> int:
        """Returns the number of registered plugins.

        Returns:
            int: Number of plugins currently in the load order.

        Raises:
            BethkitClosedError: If this load order has already been closed.
        """

        return _ffi.load_lib().bethkit_load_order_len(self.__check_open())

    def resolve(
        self,
        form_id: int,
        source_plugin: str,
        plugin: Optional[Plugin] = None,
    ) -> GlobalFormId:
        """
        Resolves a local FormID to a globally unique :class:`GlobalFormId`.

        Args:
            form_id (int): The raw 32-bit FormID as stored in a plugin
                record.
            source_plugin (str): Name of the plugin that contains the
                FormID.
            plugin: Open source plugin whose master list determines local
                FormID ownership. Omit only for a source with no masters.

        Returns:
            GlobalFormId: The resolved global FormID.

        Raises:
            BethkitClosedError: This load order or the source plugin is closed.
            BethkitNativeError: If *form_id* or *source_plugin* cannot be
                resolved.
            UnicodeDecodeError: The native plugin name is not UTF-8.
            UnicodeEncodeError: The source name contains an unpaired surrogate.
            ValueError: The FormID is outside the unsigned 32-bit range or the
                source name contains a NUL character.
        """

        lib = _ffi.load_lib()
        ptr = self.__check_open()
        if not 0 <= form_id <= 0xFFFFFFFF:
            raise ValueError("form_id must be an unsigned 32-bit integer.")
        out = BethkitGlobalFormId()
        if plugin is None:
            status = lib.bethkit_load_order_resolve(
                ptr,
                form_id,
                _ffi.senc(source_plugin),
                ctypes.byref(out),
            )
        else:
            status = lib.bethkit_load_order_resolve_with_plugin(
                ptr,
                form_id,
                _ffi.senc(source_plugin),
                plugin._native_pointer(),
                ctypes.byref(out),
            )
        if status != 0:
            _ffi.raise_last_error(lib)
        plugin_name_raw: Optional[bytes] = out.plugin_name
        plugin_name = plugin_name_raw.decode("utf-8") if plugin_name_raw else ""
        return GlobalFormId(plugin_name=plugin_name, object_id=out.object_id)

    def __repr__(self) -> str:
        """Returns the plugin count or closed state for debugging.

        Returns:
            str: Developer-friendly representation with plugin count.
        """

        if not self.__ptr:
            return "<LoadOrder closed>"
        return f"<LoadOrder len={len(self)}>"
