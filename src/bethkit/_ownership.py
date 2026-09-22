"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import Protocol

from . import _error


class BorrowOwner(Protocol):
    """Defines the private lifetime check required by borrowed handles."""

    def _check_borrowed(self) -> None:
        """Checks whether memory owned by this object remains available.

        Raises:
            BethkitClosedError: If the native owner has been closed.
        """

        ...


class BorrowedHandle:
    """Keeps an owner alive and validates it before native pointer access."""

    __pointer: int
    __owner: BorrowOwner

    def __init__(self, pointer: int, owner: BorrowOwner) -> None:
        """Stores a borrowed pointer and its lifetime owner.

        Args:
            pointer: Native pointer borrowed from the owner.
            owner: Object responsible for keeping the native memory alive.
        """

        self.__pointer = pointer
        self.__owner = owner

    def _check_borrowed(self) -> None:
        """Checks the complete owner chain before accessing native memory.

        Raises:
            BethkitClosedError: If this pointer or an owner is unavailable.
        """

        self.__owner._check_borrowed()
        if not self.__pointer:
            raise _error.BethkitClosedError("Borrowed handle is unavailable.")

    def _native_pointer(self) -> int:
        """Returns a borrowed pointer after validating its lifetime.

        Returns:
            A native pointer valid while the owner remains open.

        Raises:
            BethkitClosedError: If this pointer or an owner is unavailable.
        """

        self._check_borrowed()
        return self.__pointer
