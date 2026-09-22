"""
Copyright (c) Modding Forge
"""

from collections.abc import Callable
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from bethkit import BethkitClosedError, BethkitNativeError, RecordEditor


class TestEditorOwnership:
    """Checks that finishing an editor has an explicit ownership boundary."""

    def test_successful_finish_consumes_editor(
        self, mock_lib: MagicMock
    ) -> None:
        """Rejects every subsequent native operation after successful finish.

        Args:
            mock_lib: Patched native functions.
        """

        # given
        mock_lib.bethkit_record_editor_finish.return_value = 606
        editor = RecordEditor._from_native(505)

        # when
        writable = editor.finish()
        editor.close()
        operations: tuple[Callable[[], object], ...] = (
            editor.snapshot,
            editor.strings_snapshot,
            editor.finish,
            lambda: editor.set("TEST.FULL", "changed"),
            lambda: editor.insert("TEST.FULL", "changed"),
            lambda: editor.set_form_id("TEST.DATA", 1),
            lambda: editor.remove("TEST.FULL"),
        )
        for operation in operations:
            with pytest.raises(BethkitClosedError):
                operation()
        writable.close()

        # then
        mock_lib.bethkit_record_editor_free.assert_called_once_with(505)
        mock_lib.bethkit_record_editor_finish.assert_called_once_with(505)
        mock_lib.bethkit_writable_record_free.assert_called_once_with(606)

    def test_editor_cleanup_failure_releases_finished_record(
        self, mock_lib: MagicMock
    ) -> None:
        """Releases the result even if freeing its consumed editor raises.

        Args:
            mock_lib: Patched native functions.
        """

        mock_lib.bethkit_record_editor_finish.return_value = 606
        mock_lib.bethkit_record_editor_free.side_effect = RuntimeError(
            "cleanup"
        )
        editor = RecordEditor._from_native(505)
        with pytest.raises(RuntimeError, match="cleanup"):
            editor.finish()
        editor.close()
        mock_lib.bethkit_record_editor_free.assert_called_once_with(505)
        mock_lib.bethkit_writable_record_free.assert_called_once_with(606)
        mock_lib.bethkit_record_editor_set_string.assert_not_called()
        mock_lib.bethkit_record_editor_insert_json.assert_not_called()
        mock_lib.bethkit_record_editor_remove.assert_not_called()

    def test_native_finish_failure_retains_editor(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps pending edits owned and accessible when native finish fails.

        Args:
            mock_lib: Patched native functions.
        """

        # given
        mock_lib.bethkit_record_editor_finish.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"cannot encode record"
        mock_lib.bethkit_record_editor_set_string.return_value = 0

        # when
        with RecordEditor._from_native(505) as editor:
            with pytest.raises(BethkitNativeError, match="cannot encode"):
                editor.finish()
            mock_lib.bethkit_record_editor_free.assert_not_called()
            editor.set("TEST.FULL", "fixed")

        # then
        mock_lib.bethkit_record_editor_set_string.assert_called_once_with(
            505, b"TEST.FULL", 0, b"fixed"
        )
        mock_lib.bethkit_record_editor_free.assert_called_once_with(505)
        mock_lib.bethkit_writable_record_free.assert_not_called()

    def test_failed_result_adoption_releases_finished_record(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Releases the finished record if creating its Python owner fails.

        Args:
            mock_lib: Patched native functions.
            mocker: Mock manager replacing only writable record adoption.
        """

        # given
        mock_lib.bethkit_record_editor_finish.return_value = 606
        mocker.patch(
            "bethkit.plugin.writer.WritableRecord._from_native",
            side_effect=MemoryError("adoption"),
        )
        editor = RecordEditor._from_native(505)

        # when
        with pytest.raises(MemoryError, match="adoption"):
            editor.finish()
        editor.close()
        with pytest.raises(BethkitClosedError):
            editor.finish()

        # then
        mock_lib.bethkit_record_editor_free.assert_called_once_with(505)
        mock_lib.bethkit_writable_record_free.assert_called_once_with(606)
