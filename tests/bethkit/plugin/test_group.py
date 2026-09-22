"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

from bethkit import (
    Group,
    Plugin,
    Record,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


class TestGroup:
    """Tests ``bethkit.plugin.plugin.Group``."""

    def test_child_count_delegates_to_native(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that child_count reads from bethkit_group_child_count."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_count.return_value = 3
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        sentinel_parent = Plugin._from_native(0xCAFE)
        group = Group._from_native(0xDEAD, sentinel_parent)

        # when
        count = group.child_count

        # then
        assert count == 3

    def test_child_as_record_returns_none_for_group_child(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that child_as_record() returns None when FFI returns 0."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_as_record.return_value = 0
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = Group._from_native(0xDEAD, Plugin._from_native(0xCAFE))

        # when
        result = group.child_as_record(0)

        # then
        assert result is None

    def test_child_as_record_wraps_valid_ptr(
        self, mocker: MockerFixture
    ) -> None:
        """Tests that child_as_record() wraps a non-null FFI pointer."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_as_record.return_value = 0xBEEF
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = Group._from_native(0xDEAD, Plugin._from_native(0xCAFE))

        # when
        result = group.child_as_record(0)

        # then
        assert isinstance(result, Record)

    def test_iter_yields_records_and_groups(
        self, mocker: MockerFixture
    ) -> None:
        """Yields both records and nested groups during iteration."""

        # given
        mock_lib: MagicMock = mocker.MagicMock()
        mock_lib.bethkit_group_child_count.return_value = 2
        mock_lib.bethkit_group_child_is_record.side_effect = [True, False]
        mock_lib.bethkit_group_child_as_record.return_value = 0xAAAA
        mock_lib.bethkit_group_child_as_group.return_value = 0xBBBB
        mocker.patch("bethkit._ffi.load_lib", return_value=mock_lib)
        group = Group._from_native(0xDEAD, Plugin._from_native(0xCAFE))

        # when
        children = list(group)

        # then
        assert len(children) == 2
        assert isinstance(children[0], Record)
        assert isinstance(children[1], Group)
