"""
Copyright (c) Modding Forge
"""

# Checks positional text editing and coordinated output publication.

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from bethkit import Game, Plugin, StringFileKind, _error
from bethkit.schema import SemanticContext
from bethkit.strings import (
    LocalizationSet,
    references,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


from ._fixtures import snapshot as _snapshot


class TestStringReferences:
    """Covers identity, schema annotations, and lazy text enumeration."""

    def test_bound_provenance_cannot_be_reassigned(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps an existing reference tied to its original plugin instance."""

        # given
        with Plugin._from_native(0x100) as plugin:
            reference = next(
                references._from_snapshot(_snapshot(), plugin, None)
            )

            # when / then
            with pytest.raises(ValueError, match="already bound"):
                reference._bind_source(plugin._reference_identity())

    def test_equal_text_has_different_position_identity(
        self, mock_lib: MagicMock
    ) -> None:
        """Does not identify repeated quest strings by their text content."""

        # given
        with Plugin._from_native(0x100) as plugin:
            # when
            result = list(references._from_snapshot(_snapshot(), plugin, None))

        # then
        assert result[0].text == result[1].text
        assert result[0].identity != result[1].identity
        assert result[0].address.repeat_scopes[0].occurrence == 0
        assert result[1].address.repeat_scopes[0].occurrence == 1

    def test_identity_survives_text_change_and_reload(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps filename plus structural position stable across instances."""

        # given
        mock_lib.bethkit_plugin_open_from_bytes.return_value = 0x100
        original = _snapshot()
        first = original.fields[0]
        changed = original.model_copy(
            update={
                "fields": (
                    first.model_copy(
                        update={
                            "value": first.value.model_copy(
                                update={"value": "A longer changed text"}
                            )
                        }
                    ),
                )
            }
        )
        with Plugin.from_bytes(b"", Game.SKYRIM_SE, name="quest.esp") as source:
            before = next(references._from_snapshot(original, source, None))
        with Plugin.from_bytes(b"", Game.SKYRIM_SE, name="quest.esp") as reload:
            # when
            after = next(references._from_snapshot(changed, reload, None))

        # then
        assert before.identity == after.identity
        assert before.text != after.text
        assert before._source_token != after._source_token

    def test_external_reference_without_tables_is_unresolved(
        self, mock_lib: MagicMock
    ) -> None:
        """Retains identity and storage metadata without inventing text."""

        # given
        with Plugin._from_native(0x100) as plugin:
            # when
            result = next(
                references._from_snapshot(
                    _snapshot(localized=True), plugin, None
                )
            )

        # then
        assert result.text is None
        assert result.storage == "external"
        assert result.string_id == 17
        assert result.table_kind == StringFileKind.DL_STRINGS

    def test_supplied_tables_must_resolve_referenced_ids(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Raises on incomplete tables instead of silently dropping strings."""

        # given
        tables = mocker.create_autospec(LocalizationSet, instance=True)
        tables.get_str.return_value = None
        with Plugin._from_native(0x100) as plugin:
            # when / then
            with pytest.raises(_error.StringTableError, match="absent"):
                list(
                    references._from_snapshot(
                        _snapshot(localized=True), plugin, tables
                    )
                )

    def test_plugin_iteration_is_lazy_and_filters_nontranslatable(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Builds no semantic snapshots until strings are requested."""

        # given
        snapshot = _snapshot()
        field = snapshot.fields[1]
        snapshot = snapshot.model_copy(
            update={
                "fields": (
                    snapshot.fields[0],
                    field.model_copy(
                        update={
                            "value": field.value.model_copy(
                                update={"translatable": False}
                            )
                        }
                    ),
                )
            }
        )
        context = mocker.create_autospec(SemanticContext, instance=True)
        context.strings_snapshot.return_value = snapshot
        mock_lib.bethkit_plugin_is_localized.return_value = False
        mock_lib.bethkit_plugin_group_count.return_value = 1
        mock_lib.bethkit_plugin_group_get.return_value = 0x200
        mock_lib.bethkit_group_child_count.return_value = 1
        mock_lib.bethkit_group_child_is_record.return_value = True
        mock_lib.bethkit_group_child_as_record.return_value = 0x300
        with Plugin._from_native(0x100) as plugin:
            iterator = plugin.iter_strings(context)
            context.strings_snapshot.assert_not_called()

            # when
            result = list(iterator)

        # then
        assert len(result) == 1
        context.strings_snapshot.assert_called_once()
