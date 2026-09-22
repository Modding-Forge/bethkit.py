"""
Copyright (c) Modding Forge
"""

# Regression tests for native owners and borrowed handle chains.

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from bethkit import (
    Archive,
    ArchiveEntry,
    BethkitClosedError,
    BethkitNativeError,
    Game,
    Group,
    Plugin,
    PluginCache,
    PluginWriter,
    Record,
    SubRecord,
    WritableGroup,
    WritableRecord,
)


class TestBorrowedLifetimes:
    """Covers explicit close, transfer, and nested borrowed wrappers."""

    def test_closed_plugin_invalidates_entire_chain(
        self, mock_lib: MagicMock
    ) -> None:
        """Rejects nested access before any native record call."""

        # given
        plugin = Plugin(0x100)
        group = Group(0x200, plugin)
        nested = Group(0x300, group)
        record = Record(0x400, nested)
        subrecord = SubRecord(0x500, record)

        # when
        plugin.close()

        # then
        with pytest.raises(BethkitClosedError):
            _ = nested.child_count
        with pytest.raises(BethkitClosedError):
            _ = record.form_id
        with pytest.raises(BethkitClosedError):
            subrecord.as_str()
        mock_lib.bethkit_group_child_count.assert_not_called()
        mock_lib.bethkit_record_form_id.assert_not_called()
        mock_lib.bethkit_subrecord_as_zstring.assert_not_called()

    def test_paused_iterator_rechecks_owner(self, mock_lib: MagicMock) -> None:
        """Does not dereference a record after its owning plugin closes."""

        # given
        plugin = Plugin(0x100)
        record = Record(0x200, plugin)
        mock_lib.bethkit_record_subrecord_count.return_value = 2
        mock_lib.bethkit_record_subrecord_get.return_value = 0x300
        iterator = iter(record)
        next(iterator)

        # when
        plugin.close()

        # then
        with pytest.raises(BethkitClosedError):
            next(iterator)
        mock_lib.bethkit_record_subrecord_get.assert_called_once()

    def test_closed_archive_invalidates_entries(
        self, mock_lib: MagicMock
    ) -> None:
        """Prevents archive entry use after its owner closes."""

        # given
        archive = Archive(0x100)
        entry = ArchiveEntry(0x200, archive)

        # when
        archive.close()

        # then
        with pytest.raises(BethkitClosedError):
            _ = entry.path
        with pytest.raises(BethkitClosedError):
            _ = entry.uncompressed_size
        mock_lib.bethkit_archive_entry_path.assert_not_called()
        mock_lib.bethkit_archive_entry_uncompressed_size.assert_not_called()

    def test_transfer_reparents_existing_borrows_to_cache(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps pre-transfer borrows valid until the receiving cache closes."""

        # given
        mock_lib.bethkit_plugin_cache_new.return_value = 0x400
        mock_lib.bethkit_plugin_cache_add.return_value = 0
        mock_lib.bethkit_record_form_id.return_value = 0x800
        plugin = Plugin(0x100)
        record = Record(0x300, Group(0x200, plugin))
        cache = PluginCache()

        # when
        cache.add("test.esp", plugin)
        plugin.close()

        # then
        assert record.form_id == 0x800
        with pytest.raises(BethkitClosedError):
            _ = plugin.kind
        mock_lib.bethkit_plugin_free.assert_not_called()
        cache.close()
        with pytest.raises(BethkitClosedError):
            _ = record.form_id
        mock_lib.bethkit_record_form_id.assert_called_once()

    def test_failed_cache_transfer_does_not_double_free(
        self, mock_lib: MagicMock
    ) -> None:
        """Honors native consumption on failure and invalidates old borrows."""

        # given
        mock_lib.bethkit_plugin_cache_new.return_value = 0x400
        mock_lib.bethkit_plugin_cache_add.return_value = -1
        mock_lib.bethkit_last_error.return_value = b"invalid plugin"
        plugin = Plugin(0x100)
        record = Record(0x300, plugin)

        # when
        with PluginCache() as cache:
            with pytest.raises(BethkitNativeError, match="invalid plugin"):
                cache.add("test.esp", plugin)
        plugin.close()

        # then
        with pytest.raises(BethkitClosedError):
            _ = record.form_id
        mock_lib.bethkit_plugin_free.assert_not_called()
        mock_lib.bethkit_plugin_cache_add.assert_called_once()

    def test_cache_validates_name_before_transfer(
        self, mock_lib: MagicMock
    ) -> None:
        """Leaves a plugin owned by its wrapper after rejected input."""

        # given
        mock_lib.bethkit_plugin_cache_new.return_value = 0x400
        plugin = Plugin(0x100)

        # when
        with PluginCache() as cache:
            with pytest.raises(ValueError):
                cache.add("bad\0name.esp", plugin)
        plugin.close()

        # then
        mock_lib.bethkit_plugin_free.assert_called_once_with(0x100)
        mock_lib.bethkit_plugin_cache_add.assert_not_called()

    def test_cache_result_checks_cache_owner(self, mock_lib: MagicMock) -> None:
        """Rejects resolved record access after the cache closes."""

        # given
        mock_lib.bethkit_plugin_cache_new.return_value = 0x400
        mock_lib.bethkit_plugin_cache_resolve.return_value = 0x300
        with PluginCache() as cache:
            record = cache.resolve("test.esp", 0x800)
        assert record is not None

        # when / then
        with pytest.raises(BethkitClosedError):
            _ = record.form_id
        mock_lib.bethkit_record_form_id.assert_not_called()


class TestWriterTransfers:
    """Ensures parent precondition failures never consume children."""

    def test_closed_group_preserves_record(self, mock_lib: MagicMock) -> None:
        """Retains a writable record if its receiving group is closed."""

        # given
        group = WritableGroup(0x200)
        record = WritableRecord(0x100)
        group.close()

        # when
        with pytest.raises(BethkitClosedError):
            group.add_record(record)
        record.close()

        # then
        mock_lib.bethkit_writable_record_free.assert_called_once_with(0x100)
        mock_lib.bethkit_writable_group_add_record.assert_not_called()

    def test_closed_writer_preserves_group(self, mock_lib: MagicMock) -> None:
        """Retains a writable group if its receiving writer is closed."""

        # given
        mock_lib.bethkit_plugin_writer_new.return_value = 0x300
        writer = PluginWriter(Game.SKYRIM_SE)
        group = WritableGroup(0x200)
        writer.close()

        # when
        with pytest.raises(BethkitClosedError):
            writer.add_group(group)
        group.close()

        # then
        mock_lib.bethkit_writable_group_free.assert_called_once_with(0x200)
        mock_lib.bethkit_plugin_writer_add_group.assert_not_called()

    def test_self_add_preserves_group(self, mock_lib: MagicMock) -> None:
        """Rejects self-containment before ownership transfer."""

        # given
        group = WritableGroup(0x200)

        # when
        with pytest.raises(ValueError, match="itself"):
            group.add_group(group)
        group.close()

        # then
        mock_lib.bethkit_writable_group_free.assert_called_once_with(0x200)
        mock_lib.bethkit_writable_group_add_group.assert_not_called()
