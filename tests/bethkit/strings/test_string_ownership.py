"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import gc
from collections.abc import Callable
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    LocalizationSet,
    StringFileKind,
    StringTable,
)
from bethkit.strings import strings

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestStringOwnership:
    """Guards private handle adoption and lifetime-safe public operations."""

    def test_clone_releases_new_allocation_if_wrapper_creation_fails(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Frees only the new clone while preserving its original owner."""

        # given
        mock_lib.bethkit_localization_set_clone.return_value = 0x200
        with LocalizationSet._from_native(0x100) as original:
            mocker.patch.object(
                LocalizationSet,
                "_from_native",
                side_effect=MemoryError("wrapper failed"),
            )

            # when / then
            with pytest.raises(MemoryError, match="wrapper failed"):
                original.clone()
            mock_lib.bethkit_localization_set_free.assert_called_once_with(
                0x200
            )

        assert mock_lib.bethkit_localization_set_free.call_count == 2

    @pytest.mark.parametrize("constructor", [StringTable, LocalizationSet])
    def test_public_constructor_rejects_pointer_adoption(
        self, constructor: Callable[..., object], mock_lib: MagicMock
    ) -> None:
        """Rejects raw pointer integers without attempting native cleanup."""

        # when / then
        with pytest.raises(TypeError):
            constructor(0x100)
        with pytest.raises(TypeError, match="Use"):
            constructor()
        gc.collect()
        mock_lib.bethkit_string_table_free.assert_not_called()
        mock_lib.bethkit_localization_set_free.assert_not_called()

    @pytest.mark.parametrize("constructor", [StringTable, LocalizationSet])
    def test_private_factory_rejects_null(
        self, constructor: type[StringTable] | type[LocalizationSet]
    ) -> None:
        """Rejects a null owner before constructing a live wrapper."""

        with pytest.raises(ValueError, match="null"):
            constructor._from_native(0)

    def test_legacy_module_keeps_identical_public_classes(self) -> None:
        """Preserves existing class import identities after decomposition."""

        assert strings.StringTable is StringTable
        assert strings.LocalizationSet is LocalizationSet

    def test_closed_owners_reject_context_entry(
        self, mock_lib: MagicMock
    ) -> None:
        """Rejects entering an already closed table or localization set."""

        # given
        table = StringTable._from_native(0x100)
        localization = LocalizationSet._from_native(0x200)
        table.close()
        localization.close()

        # when / then
        with pytest.raises(BethkitClosedError):
            table.__enter__()
        with pytest.raises(BethkitClosedError):
            localization.__enter__()

    def test_invalid_text_reports_decode_error(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Leaves invalid UTF-8 visible as the documented builtin error."""

        # given
        mock_lib.bethkit_string_table_get.return_value = 0x300
        mock_lib.bethkit_localization_set_get.return_value = 0x300
        mocker.patch("ctypes.string_at", return_value=b"\xff\0")

        # when / then
        with StringTable._from_native(0x100) as table:
            with pytest.raises(UnicodeDecodeError):
                table.get_str(17)
        with LocalizationSet._from_native(0x200) as localization:
            with pytest.raises(UnicodeDecodeError):
                localization.get_str(StringFileKind.STRINGS, 17)
