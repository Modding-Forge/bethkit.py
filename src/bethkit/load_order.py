"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
from typing import Optional

from pydantic import BaseModel

from . import _ffi
from ._error import BethkitClosedError
from ._ffi import BethkitGlobalFormId
from .enums import PluginKind


class GlobalFormId(BaseModel, frozen=True):
    """
    A globally unique FormID consisting of a plugin name and a 24-bit
    object ID.
    """

    plugin_name: str
    """Name of the owning plugin (e.g. ``"Skyrim.esm"``)."""

    object_id: int
    """24-bit object identifier within *plugin_name*."""

    def __str__(self) -> str:
        """
        Returns:
            str: Human-readable ``"PluginName:0xOBJECTID"`` representation.
        """

        return f"{self.plugin_name}:0x{self.object_id:06X}"


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

    __ptr: int

    def __init__(self) -> None:
        """
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
        Return the native pointer, raising if the handle is already closed.

        Returns:
            int: Non-zero native pointer.

        Raises:
            BethkitClosedError: If :meth:`close` has already been called.
        """

        if not self.__ptr:
            raise BethkitClosedError(
                "LoadOrder has already been closed."
            )
        return self.__ptr

    def close(self) -> None:
        """
        Release the native load-order handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_load_order_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> LoadOrder:
        """
        Return *self* for use as a context manager.

        Returns:
            LoadOrder: This instance.
        """

        return self

    def __exit__(self, *_: object) -> None:
        """Close the load order when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def push(self, name: str, kind: PluginKind) -> None:
        """
        Append a plugin to the end of the load order.

        Args:
            name (str): Plugin file name (e.g. ``"Skyrim.esm"``).
            kind (PluginKind): Whether the plugin is a full, light, or
                overlay plugin.

        Raises:
            BethkitClosedError: If this load order has already been closed.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        ptr = self.__check_open()
        if lib.bethkit_load_order_push(
            ptr, _ffi.senc(name), int(kind)
        ) != 0:
            _ffi.raise_last_error(lib)

    def __len__(self) -> int:
        """
        Returns:
            int: Number of plugins currently in the load order.

        Raises:
            BethkitClosedError: If this load order has already been closed.
        """

        return _ffi.load_lib().bethkit_load_order_len(self.__check_open())

    def resolve(self, form_id: int, source_plugin: str) -> GlobalFormId:
        """
        Resolve a local FormID to a globally unique :class:`GlobalFormId`.

        Args:
            form_id (int): The raw 32-bit FormID as stored in a plugin
                record.
            source_plugin (str): Name of the plugin that contains the
                FormID.

        Returns:
            GlobalFormId: The resolved global FormID.

        Raises:
            BethkitClosedError: If this load order has already been closed.
            BethkitNativeError: If *form_id* or *source_plugin* cannot be
                resolved.
        """

        lib = _ffi.load_lib()
        ptr = self.__check_open()
        out = BethkitGlobalFormId()
        if (
            lib.bethkit_load_order_resolve(
                ptr,
                form_id,
                _ffi.senc(source_plugin),
                ctypes.byref(out),
            )
            != 0
        ):
            _ffi.raise_last_error(lib)
        plugin_name_raw: Optional[bytes] = out.plugin_name
        plugin_name = plugin_name_raw.decode("utf-8") if plugin_name_raw else ""
        return GlobalFormId(plugin_name=plugin_name, object_id=out.object_id)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with plugin count.
        """

        if not self.__ptr:
            return "<LoadOrder closed>"
        return f"<LoadOrder len={len(self)}>"
