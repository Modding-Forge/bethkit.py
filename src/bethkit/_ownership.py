"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from typing import Protocol, TypeVar

from . import _error

_T = TypeVar("_T")


def adopt_native(
    pointer: int, factory: Callable[[int], _T], free: Callable[[int], None]
) -> _T:
    """Transfers a native allocation or releases it if wrapper creation fails.

    Args:
        pointer: Non-null allocation returned by a successful native call.
        factory: Wrapper factory that takes ownership only on success.
        free: Matching native destructor.

    Returns:
        The Python owner of the allocation.

    Raises:
        BaseException: Wrapper creation failed after native allocation.
    """

    try:
        return factory(pointer)
    except BaseException:
        free(pointer)
        raise


def finalize(callback: Callable[[], None], logger: logging.Logger) -> None:
    """Releases a native resource without raising from a destructor.

    Args:
        callback: Idempotent cleanup operation for the owned native resource.
        logger: Logger receiving diagnostic details if cleanup fails.
    """

    try:
        callback()
    except Exception as error:
        # Destructors must not interrupt interpreter cleanup.
        try:
            logger.warning(f"Native cleanup failed: {error!r}", exc_info=True)
        except Exception:
            # Broken handlers must not make a destructor raise during shutdown.
            pass


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
