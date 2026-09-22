"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bethkit import _ownership

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestFinalization:
    """Verifies best-effort cleanup and diagnostics during destruction."""

    def test_success_is_quiet(self, mocker: MockerFixture) -> None:
        """Runs cleanup once without producing a warning.

        Args:
            mocker: Mock factory keeping native resources out of unit tests.
        """

        callback = mocker.Mock()
        logger = mocker.Mock()
        _ownership.finalize(callback, logger)
        callback.assert_called_once_with()
        logger.warning.assert_not_called()

    def test_failure_logs_original_exception(
        self, mocker: MockerFixture
    ) -> None:
        """Retains the original cleanup error in the diagnostic message.

        Args:
            mocker: Mock factory keeping native resources out of unit tests.
        """

        callback = mocker.Mock(side_effect=RuntimeError("cleanup failed"))
        logger = mocker.Mock()
        _ownership.finalize(callback, logger)
        logger.warning.assert_called_once_with(
            "Native cleanup failed: RuntimeError('cleanup failed')",
            exc_info=True,
        )

    def test_logging_failure_is_contained(self, mocker: MockerFixture) -> None:
        """Prevents a broken logging handler from escaping the finalizer.

        Args:
            mocker: Mock factory keeping native resources out of unit tests.
        """

        callback = mocker.Mock(side_effect=RuntimeError("cleanup failed"))
        logger = mocker.Mock()
        logger.warning.side_effect = OSError("logging unavailable")
        _ownership.finalize(callback, logger)
        callback.assert_called_once_with()
        logger.warning.assert_called_once()
