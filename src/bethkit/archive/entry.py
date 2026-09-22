"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from .. import _ffi, _ownership


class ArchiveEntry(_ownership.BorrowedHandle):
    """A single file entry inside an open archive.

    Instances borrow their data from the parent :class:`Archive` and
    become invalid once the archive is closed or freed.
    """

    def __init__(self) -> None:
        """Rejects direct construction of borrowed native views.

        Raises:
            TypeError: Always; retrieve this view from its owning object.
        """

        raise TypeError("ArchiveEntry must be obtained from its owning object.")

    @classmethod
    def _from_native(
        cls, pointer: int, owner: _ownership.BorrowOwner
    ) -> ArchiveEntry:
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
            raise ValueError("Cannot borrow a null ArchiveEntry pointer.")
        result = cls.__new__(cls)
        _ownership.BorrowedHandle.__init__(result, pointer, owner)
        return result

    @property
    def path(self) -> str:
        """Virtual path of the entry as stored in the archive.

        Returns:
            str: Path string, or an empty string when unavailable.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        lib = _ffi.load_lib()
        ptr = lib.bethkit_archive_entry_path(self._native_pointer())
        if not ptr:
            return ""
        return _ffi.copy_and_free_str(
            ptr, lib.bethkit_archive_entry_path_free, lib
        )

    @property
    def uncompressed_size(self) -> int:
        """Uncompressed size of the entry data in bytes.

        Returns:
            int: Byte count of the decompressed content.

        Raises:
            BethkitClosedError: The native owner is closed or transferred.
        """

        return _ffi.load_lib().bethkit_archive_entry_uncompressed_size(
            self._native_pointer()
        )

    def __repr__(self) -> str:
        """Returns a concise diagnostic representation.

        Returns:
            str: Developer-friendly representation showing the entry path.

        Raises:
            BethkitClosedError: The native owner is closed.
        """

        return f"<ArchiveEntry {self.path!r}>"
