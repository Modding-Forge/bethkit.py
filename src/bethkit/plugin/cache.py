"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ctypes
import logging
from typing import ClassVar, Optional

from .. import _ffi, _ownership
from .._error import BethkitClosedError, BethkitOwnershipError
from .._ffi import BethkitGlobalFormId
from ..load_order import GlobalFormId
from . import plugin as plugin_module
from .cache_hit import CacheHit as CacheHit


def _require_plugin(value: object) -> plugin_module.Plugin:
    """Validates a plugin at the ownership-transfer boundary.

    Args:
        value: User-provided plugin argument.

    Returns:
        The validated plugin wrapper.

    Raises:
        TypeError: The argument is not a plugin wrapper.
    """

    if not isinstance(value, plugin_module.Plugin):
        raise TypeError(
            f"plugin must be a Plugin instance, got {type(value).__name__!r}"
        )
    return value


class PluginCache:
    """An in-memory cache that indexes records across multiple loaded plugins.

    Add plugins with :meth:`add`, then use :meth:`resolve` or
    :meth:`find_by_editor_id` to look up records across all loaded
    plugins.

    Use as a context manager to guarantee that the native handle is
    freed::

        with PluginCache() as cache:
            cache.add("Skyrim.esm", plugin)
            rec = cache.resolve("Skyrim.esm", 0x12E49)
    """

    log: ClassVar[logging.Logger] = logging.getLogger("PluginCache")
    __ptr: int = 0

    def __init__(self) -> None:
        """Creates an empty native plugin cache.

        Raises:
            BethkitNativeError: If the native cache object cannot be created.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_plugin_cache_new()
        if not ptr:
            _ffi.raise_last_error(lib)
        self.__ptr = ptr

    def __check_open(self) -> int:
        """Return the native pointer, raising if the handle is already closed.

        Returns:
            int: Non-zero native pointer.

        Raises:
            BethkitClosedError: If :meth:`close` has already been called.
        """

        if not self.__ptr:
            raise BethkitClosedError("PluginCache has already been closed.")
        return self.__ptr

    def close(self) -> None:
        """Release the native cache handle.

        Safe to call multiple times; subsequent calls are no-ops.
        """

        if self.__ptr:
            pointer = self.__ptr
            self.__ptr = 0
            _ffi.load_lib().bethkit_plugin_cache_free(pointer)

    def _check_borrowed(self) -> None:
        """Checks whether the cache still owns its borrowed records.

        Raises:
            BethkitClosedError: If the cache has already been closed.
        """

        self.__check_open()

    def __enter__(self) -> PluginCache:
        """Return *self* for use as a context manager.

        Returns:
            PluginCache: This instance.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        self.__check_open()
        return self

    def __exit__(self, *_: object) -> None:
        """Free the cache when exiting the context.

        Args:
            *_: Exception details supplied by the context manager protocol.
        """

        self.close()

    def __del__(self) -> None:
        """Free the native handle on garbage collection."""

        _ownership.finalize(self.close, self.log)

    def add(self, name: str, plugin: plugin_module.Plugin) -> None:
        """Transfer a :class:`~bethkit.Plugin` into the cache.

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

        plugin = _require_plugin(plugin)
        ptr = self.__check_open()
        lib = _ffi.load_lib()
        encoded_name = _ffi.senc(name)
        plugin_ptr: int = plugin._transfer_ptr()
        if not plugin_ptr:
            raise BethkitOwnershipError(
                "Plugin handle has already been transferred or closed."
            )
        if lib.bethkit_plugin_cache_add(ptr, encoded_name, plugin_ptr) != 0:
            _ffi.raise_last_error(lib)
        plugin._set_borrow_owner(self)

    def __len__(self) -> int:
        """Return the number of plugins currently held in the cache.

        Returns:
            int: Number of plugins.

        Raises:
            BethkitClosedError: If this cache has already been closed.
        """

        return _ffi.load_lib().bethkit_plugin_cache_len(self.__check_open())

    @property
    def record_count(self) -> int:
        """Total number of records indexed across all cached plugins.

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
    ) -> Optional[plugin_module.Record]:
        """Look up a record by its global FormID components.

        Args:
            plugin_name (str): Name of the owning plugin.
            object_id (int): 24-bit object ID within that plugin.

        Returns:
            Optional[Record]: The matching :class:`~bethkit.Record`, or
            ``None`` if not found.

        Raises:
            BethkitClosedError: If this cache has already been closed.
        """

        lib = _ffi.load_lib()
        ptr_val = lib.bethkit_plugin_cache_resolve(
            self.__check_open(), _ffi.senc(plugin_name), object_id
        )
        if not ptr_val:
            return None
        return plugin_module.Record._from_native(ptr_val, self)

    def find_by_editor_id(self, edid: str) -> Optional[CacheHit]:
        """Search for a record by its EDID (editor ID) string.

        Args:
            edid (str): The editor ID to search for (e.g. ``"ArmorIron"``).

        Returns:
            Optional[CacheHit]: A :class:`CacheHit` containing the matched
            record and its :class:`~bethkit.GlobalFormId`, or ``None`` if
            not found.

        Raises:
            BethkitClosedError: If this cache has already been closed.
        """

        lib = _ffi.load_lib()
        out = BethkitGlobalFormId()
        ptr_val = lib.bethkit_plugin_cache_find_by_editor_id(
            self.__check_open(), _ffi.senc(edid), ctypes.byref(out)
        )
        if not ptr_val:
            return None
        plugin_name_raw: Optional[bytes] = out.plugin_name
        plugin_name = plugin_name_raw.decode("utf-8") if plugin_name_raw else ""
        gfid = GlobalFormId(plugin_name=plugin_name, object_id=out.object_id)
        return CacheHit(
            record=plugin_module.Record._from_native(ptr_val, self),
            global_form_id=gfid,
        )

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation with plugin and record
            counts.
        """

        if not self.__ptr:
            return "<PluginCache closed>"
        return f"<PluginCache plugins={len(self)} records={self.record_count}>"
