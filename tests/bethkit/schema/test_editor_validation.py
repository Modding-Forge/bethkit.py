"""
Copyright (c) Modding Forge
"""

# Python boundary validation prevents silent ctypes integer truncation.

from unittest.mock import MagicMock

import pytest

from bethkit import RecordEditor


class TestEditorValidation:
    """Rejects values that cannot cross the fixed-width native boundary."""

    @pytest.mark.parametrize("value", [-(1 << 63) - 1, 1 << 64])
    def test_integer_overflow(self, mock_lib: MagicMock, value: int) -> None:
        """Rejects integer overflow before any native setter call.

        Args:
            mock_lib: Patched native functions.
            value: Out-of-range signed or unsigned integer.
        """

        with RecordEditor(505) as editor:
            with pytest.raises(ValueError, match="64-bit"):
                editor.set("test", value)
        mock_lib.bethkit_record_editor_set_i64.assert_not_called()
        mock_lib.bethkit_record_editor_set_u64.assert_not_called()

    @pytest.mark.parametrize("value", [-1, 1 << 32, True])
    def test_form_id_overflow(self, mock_lib: MagicMock, value: int) -> None:
        """Rejects invalid FormIDs without wrapping them to another record.

        Args:
            mock_lib: Patched native functions.
            value: Out-of-range or boolean record identity.
        """

        with RecordEditor(505) as editor:
            with pytest.raises(ValueError, match="32-bit"):
                editor.set_form_id("test", value)
        mock_lib.bethkit_record_editor_set_form_id.assert_not_called()

    def test_negative_occurrence(self, mock_lib: MagicMock) -> None:
        """Rejects negative positions instead of converting to huge indexes.

        Args:
            mock_lib: Patched native functions.
        """

        with RecordEditor(505) as editor:
            with pytest.raises(ValueError, match="nonnegative"):
                editor.set("test", 1, occurrence=-1)
            with pytest.raises(ValueError, match="nonnegative"):
                editor.set_form_id("test", 1, occurrence=-1)
            with pytest.raises(ValueError, match="nonnegative"):
                editor.remove("test", occurrence=-1)
        mock_lib.bethkit_record_editor_remove.assert_not_called()
