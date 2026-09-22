"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, cast

from .. import _ffi
from ..enums import PluginKind


class PluginMetadata(ABC):
    """Provides header metadata for an open plugin owner."""

    @abstractmethod
    def _native_pointer(self) -> int:
        """Returns the owning plugin's live pointer.

        Returns:
            The validated native plugin pointer.

        Raises:
            BethkitClosedError: The owning plugin is no longer open.
        """

        ...

    @property
    def kind(self) -> PluginKind:
        """Plugin type as declared in the file header.

        Returns:
            PluginKind: ``FULL``, ``LIGHT``, or ``OVERLAY``.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return PluginKind(
            _ffi.load_lib().bethkit_plugin_kind(self._native_pointer())
        )

    @property
    def is_localized(self) -> bool:
        """Whether the plugin uses external string localisation files.

        Returns:
            bool: ``True`` if the plugin sets the localised flag.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return bool(
            _ffi.load_lib().bethkit_plugin_is_localized(self._native_pointer())
        )

    @property
    def description(self) -> Optional[str]:
        """Plugin description from the SNAM sub-record, if present.

        Returns:
            Optional[str]: Description string, or ``None`` if absent.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        lib = _ffi.load_lib()
        raw: Optional[bytes] = lib.bethkit_plugin_description(
            self._native_pointer()
        )
        return raw.decode("utf-8") if raw else None

    @property
    def master_count(self) -> int:
        """Number of master plugin dependencies declared in the header.

        Returns:
            int: Master count.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return _ffi.load_lib().bethkit_plugin_master_count(
            self._native_pointer()
        )

    def master_at(self, index: int) -> str:
        """Return the master plugin name at the given index.

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
            self._native_pointer(), index
        )
        if raw is None:
            _ffi.raise_last_error(lib)
        return cast(bytes, raw).decode("utf-8")

    @property
    def masters(self) -> list[str]:
        """All master plugin names in load order.

        Returns:
            list[str]: Ordered list of master file names.

        Raises:
            BethkitClosedError: If the plugin has been closed.
        """

        return [self.master_at(i) for i in range(self.master_count)]
