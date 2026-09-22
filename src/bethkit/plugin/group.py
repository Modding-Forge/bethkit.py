"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Optional

from .. import _ffi, _ownership
from .._error import BethkitNativeError
from .record import Record


class Group(_ownership.BorrowedHandle):
    """A top-level group inside a plugin, containing records or sub-groups.

    Groups are the primary organisational unit in Bethesda plugin files.
    They may contain :class:`Record` children or nested :class:`Group`
    children.

    Access after the native owner closes raises ``BethkitClosedError``.
    """

    def __init__(self) -> None:
        """Rejects direct construction of borrowed native views.

        Raises:
            TypeError: Always; retrieve this view from its owning object.
        """

        raise TypeError("Group must be obtained from its owning object.")

    @classmethod
    def _from_native(cls, pointer: int, owner: _ownership.BorrowOwner) -> Group:
        """Wraps a borrowed pointer without taking ownership.

        Args:
            pointer: Nonzero native pointer borrowed from the owner.
            owner: Object that keeps the native allocation alive.

        Returns:
            A borrowed view that validates its owner's lifetime.

        Raises:
            ValueError: The supplied native pointer is null.
        """

        if not pointer:
            raise ValueError("Cannot borrow a null Group pointer.")
        result = cls.__new__(cls)
        _ownership.BorrowedHandle.__init__(result, pointer, owner)
        return result

    @property
    def group_type(self) -> int:
        """Numeric group type code as defined in the plugin format.

        Returns:
            int: Group type (e.g. ``0`` for top-level groups).

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
            BethkitNativeError: If the native call fails.
        """

        lib = _ffi.load_lib()
        t = lib.bethkit_group_type(self._native_pointer())
        if t < 0:
            _ffi.raise_last_error(lib)
        return t

    @property
    def child_count(self) -> int:
        """Total number of direct children (records and sub-groups).

        Returns:
            int: Child count.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        return _ffi.load_lib().bethkit_group_child_count(self._native_pointer())

    def child_is_record(self, index: int) -> bool:
        """Return whether the child at *index* is a record (vs. a group).

        Args:
            index (int): Zero-based child index.

        Returns:
            bool: ``True`` if the child is a :class:`Record`.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        return bool(
            _ffi.load_lib().bethkit_group_child_is_record(
                self._native_pointer(), index
            )
        )

    def child_as_record(self, index: int) -> Optional[Record]:
        """Return the child at *index* as a :class:`Record`.

        Args:
            index (int): Zero-based child index.

        Returns:
            Optional[Record]: The child record, or ``None`` if the child is
            a group or the index is out of range.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_group_child_as_record(self._native_pointer(), index)
        if not ptr:
            return None
        return Record._from_native(ptr, self)

    def child_as_group(self, index: int) -> Optional[Group]:
        """Return the child at *index* as a :class:`Group`.

        Args:
            index (int): Zero-based child index.

        Returns:
            Optional[Group]: The child group, or ``None`` if the child is
            a record or the index is out of range.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_group_child_as_group(self._native_pointer(), index)
        if not ptr:
            return None
        return Group._from_native(ptr, self)

    def __iter__(self) -> Iterator[Record | Group]:
        """Iterate over all direct children of this group.

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
                    yield Record._from_native(ptr, self)
            else:
                ptr = lib.bethkit_group_child_as_group(
                    self._native_pointer(), i
                )
                if ptr:
                    yield Group._from_native(ptr, self)

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation showing type and count.

        Raises:
            BethkitClosedError: The native owner is closed.
        """

        try:
            return f"<Group type={self.group_type} children={self.child_count}>"
        except BethkitNativeError:
            return "<Group ?>"
