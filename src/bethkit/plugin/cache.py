"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import ctypes
from typing import Optional

from pydantic import BaseModel, ConfigDict

from .. import _ffi
from .._error import BethkitClosedError, BethkitOwnershipError
from .._ffi import BethkitGlobalFormId
from ..load_order import GlobalFormId


class CacheHit(BaseModel):
    """
    Result of a successful :meth:`PluginCache.find_by_editor_id` lookup.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    record: object
    """The matched record (borrowed, valid while the cache is open)."""

    global_form_id: GlobalFormId
    """The resolved global FormID of the matched record."""


class PluginCache:
    """
    An in-memory cache that indexes records across multiple loaded plugins.

    Add plugins with :meth:`add`, then use :meth:`resolve` or
    :meth:`find_by_editor_id` to look up records across all loaded
    plugins.

    Use as a context manager to guarantee that the native handle is
    freed::

        with PluginCache() as cache:
            cache.add("Skyrim.esm", plugin)
            rec = cache.resolve("Skyrim.esm", 0x12E49)
    """

    __ptr: int

    def __init__(self) -> None:
        """
        Raises:
            BethkitNativeError: If the native cache object cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_plugin_cache_new()
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
            raise BethkitClosedError("PluginCache has already been closed.")
        return self.__ptr

    def close(self) -> None:
        """
        Release the native cache handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            _ffi.load_lib().bethkit_plugin_cache_free(self.__ptr)
            self.__ptr = 0

    def __enter__(self) -> PluginCache:
        """
        Return *self* for use as a context manager.

        Returns:
            PluginCache: This instance.
        """

        return self

    def __exit__(self, *_: object) -> None:
        """Free the cache when exiting the context."""

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        try:
            self.close()
        except Exception:
            pass

    def add(self, name: str, plugin: object) -> None:
        """
        Transfer a :class:`~bethkit.Plugin` into the cache.

        Ownership of the native plugin handle is transferred to the cache;
        the :class:`~bethkit.Plugin` wrapper becomes invalid after this call.

        Args:
            name (str): Plugin file name used as the lookup key
                (e.g. ``"Skyrim.esm"``).
            plugin: The plugin to add.  Must be a valid, open
                :class:`~bethkit.Plugin` instance.

        Raises:
            BethkitClosedError: If this cache or the plugin is already closed.
            BethkitOwnershipError: If the plugin handle has already been
                transferred to another container.
            BethkitNativeError: If the native call fails.
            TypeError: If *plugin* is not a ``Plugin`` instance.
        """

        from .plugin import Plugin

        if not isinstance(plugin, Plugin):
            raise TypeError(
                f"plugin must be a Plugin instance, got {type(plugin).__name__!r}"
            )
        ptr = self.__check_open()
        lib = _ffi.load_lib()
        plugin_ptr: int = plugin._transfer_ptr()
        if not plugin_ptr:
            raise BethkitOwnershipError(
                "Plugin handle has already been transferred or closed."
            )
        if lib.bethkit_plugin_cache_add(
            ptr, _ffi.senc(name), plugin_ptr
        ) != 0:
            _ffi.raise_last_error(lib)

    def __len__(self) -> int:
        """
        Returns:
            int: Number of plugins currently held in the cache.

        Raises:
            BethkitClosedError: If this cache has already been closed.
        """

        return _ffi.load_lib().bethkit_plugin_cache_len(self.__check_open())

    @property
    def record_count(self) -> int:
        """
        Total number of records indexed across all cached plugins.

        Returns:
            int: Aggregate record count.

        Raises:
            BethkitClosedError: If this cache has already been closed.
        """

        return _ffi.load_lib().bethkit_plugin_cache_record_count(
            self.__check_open()
        )

    def resolve(
        self, plugin_name: str, object_id: int
    ) -> Optional[object]:
        """
        Look up a record by its global FormID components.

        Args:
            plugin_name (str): Name of the owning plugin.
            object_id (int): 24-bit object ID within that plugin.

        Returns:
            Optional[Record]: The matching :class:`~bethkit.Record`, or
            ``None`` if not found.

        Raises:
            BethkitClosedError: If this cache has already been closed.
        """

        from .plugin import Record

        lib = _ffi.load_lib()
        ptr_val = lib.bethkit_plugin_cache_resolve(
            self.__check_open(), _ffi.senc(plugin_name), object_id
        )
        if not ptr_val:
            return None
        return Record(ptr_val, self)

    def find_by_editor_id(self, edid: str) -> Optional[CacheHit]:
        """
        Search for a record by its EDID (editor ID) string.

        Args:
            edid (str): The editor ID to search for (e.g. ``"ArmorIron"``).

        Returns:
            Optional[CacheHit]: A :class:`CacheHit` containing the matched
            record and its :class:`~bethkit.GlobalFormId`, or ``None`` if
            not found.

        Raises:
            BethkitClosedError: If this cache has already been closed.
        """

        from .plugin import Record

        lib = _ffi.load_lib()
        out = BethkitGlobalFormId()
        ptr_val = lib.bethkit_plugin_cache_find_by_editor_id(
            self.__check_open(), _ffi.senc(edid), ctypes.byref(out)
        )
        if not ptr_val:
            return None
        plugin_name_raw: Optional[bytes] = out.plugin_name
        plugin_name = (
            plugin_name_raw.decode("utf-8") if plugin_name_raw else ""
        )
        gfid = GlobalFormId(plugin_name=plugin_name, object_id=out.object_id)
        return CacheHit(record=Record(ptr_val, self), global_form_id=gfid)

    def __repr__(self) -> str:
        """
        Returns:
            str: Developer-friendly representation with plugin and record
            counts.
        """

        if not self.__ptr:
            return "<PluginCache closed>"
        return (
            f"<PluginCache plugins={len(self)} records={self.record_count}>"
        )


