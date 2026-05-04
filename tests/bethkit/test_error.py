"""
Copyright (c) Modding Forge
"""
from __future__ import annotations

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitError,
    BethkitLibraryNotFoundError,
    BethkitNativeError,
    BethkitNotFoundError,
    BethkitOwnershipError,
)


class TestBethkitError:
    """Tests ``bethkit._error`` exception hierarchy."""

    def test_is_base_exception(self) -> None:
        """Tests that BethkitError is a subclass of Exception."""

        assert issubclass(BethkitError, Exception)

    def test_library_not_found_inherits_base(self) -> None:
        """Tests that BethkitLibraryNotFoundError inherits BethkitError."""

        assert issubclass(BethkitLibraryNotFoundError, BethkitError)

    def test_native_error_inherits_base(self) -> None:
        """Tests that BethkitNativeError inherits BethkitError."""

        assert issubclass(BethkitNativeError, BethkitError)

    def test_native_error_carries_message(self) -> None:
        """Tests that BethkitNativeError stores its message."""

        # given / when
        err = BethkitNativeError("native call failed")

        # then
        assert err.message == "native call failed"
        assert "native call failed" in str(err)

    def test_not_found_inherits_native(self) -> None:
        """Tests that BethkitNotFoundError is a BethkitNativeError."""

        assert issubclass(BethkitNotFoundError, BethkitNativeError)

    def test_not_found_can_be_caught_as_native(self) -> None:
        """Tests that BethkitNotFoundError is caught by except BethkitNativeError."""

        # given / when / then
        with pytest.raises(BethkitNativeError):
            raise BethkitNotFoundError("record not found")

    def test_closed_error_inherits_base(self) -> None:
        """Tests that BethkitClosedError inherits BethkitError."""

        assert issubclass(BethkitClosedError, BethkitError)

    def test_ownership_error_inherits_base(self) -> None:
        """Tests that BethkitOwnershipError inherits BethkitError."""

        assert issubclass(BethkitOwnershipError, BethkitError)

    def test_all_errors_caught_by_base(self) -> None:
        """Tests that every error class can be caught as BethkitError."""

        # given
        errors = [
            BethkitLibraryNotFoundError("lib not found"),
            BethkitNativeError("native error"),
            BethkitNotFoundError("not found"),
            BethkitClosedError("handle closed"),
            BethkitOwnershipError("ownership transferred"),
        ]

        # when / then
        for exc in errors:
            with pytest.raises(BethkitError):
                raise exc
