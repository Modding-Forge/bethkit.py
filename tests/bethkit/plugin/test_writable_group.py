"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import (
    BethkitClosedError,
    BethkitOwnershipError,
    WritableGroup,
    WritableRecord,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestWritableGroup:
    """Tests ``bethkit.plugin.writer.WritableGroup``."""

    def test_new_creates_group(self, mocker: MockerFixture) -> None:
        """Tests that WritableGroup.new() calls the FFI and wraps the ptr."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        # when
        group = WritableGroup.new(b"NPC_")

        # then
        assert isinstance(group, WritableGroup)
        group.close()

    def test_add_record_transfers_ownership(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that add_record() takes ownership of the WritableRecord."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mock_lib.bethkit_writable_group_add_record.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        rec = WritableRecord.new(b"NPC_")

        # when
        with WritableGroup.new(b"NPC_") as group:
            group.add_record(rec)

        # then — second _transfer_ptr must fail (already zeroed)
        with pytest.raises(BethkitOwnershipError):
            rec._transfer_ptr()

    def test_add_record_raises_after_close(self, mocker: MockerFixture) -> None:
        """Tests that add_record() raises BethkitClosedError after close()."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mock_lib.bethkit_writable_record_new.return_value = 0xABCD
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)

        group = WritableGroup.new(b"NPC_")
        group.close()
        rec = WritableRecord.new(b"NPC_")

        # when / then
        with pytest.raises(BethkitClosedError):
            group.add_record(rec)
        rec.close()

    def test_transfer_ptr_invalidates_group(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that _transfer_ptr() zeroes the group handle."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_writable_group_new.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = WritableGroup.new(b"NPC_")

        # when
        ptr = group._transfer_ptr()

        # then
        assert ptr == 0xBEEF
        with pytest.raises(BethkitOwnershipError):
            group._transfer_ptr()
