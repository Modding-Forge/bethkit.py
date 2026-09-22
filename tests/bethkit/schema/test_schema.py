"""
Copyright (c) Modding Forge
"""

# Tests for owned ABI-v2 schema handles and immutable models.

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest
from pydantic import ValidationError

from bethkit import (
    Diagnostic,
    Game,
    RecordEditor,
    SchemaCatalog,
    SchemaPackage,
    SemanticContext,
)


class _Record:
    """Minimal record handle used by editor/view wrapper tests."""

    def _native_pointer(self) -> int:
        """Returns an always-live mocked native record pointer."""

        return 404


class TestSchema:
    """Checks schema ownership, factories, and immutable result models."""

    def test_catalog_embedded_is_owned(self, mock_lib: MagicMock) -> None:
        """Checks that the embedded catalog releases its owned handle.

        Args:
            mock_lib: Patched native functions.
        """

        mock_lib.bethkit_schema_catalog_embedded.return_value = 101

        catalog = SchemaCatalog.embedded()
        catalog.close()

        mock_lib.bethkit_schema_catalog_free.assert_called_once_with(101)

    def test_catalog_package_uses_all_game_enum_values(
        self, mock_lib: MagicMock
    ) -> None:
        """Checks that every public game can be requested from the catalog.

        Args:
            mock_lib: Patched native functions.
        """

        mock_lib.bethkit_schema_catalog_embedded.return_value = 101
        mock_lib.bethkit_schema_catalog_package.return_value = 202

        with SchemaCatalog.embedded() as catalog:
            packages = [catalog.package(game) for game in Game]
            for package in packages:
                package.close()

        requested = {
            call.args[1]
            for call in mock_lib.bethkit_schema_catalog_package.call_args_list
        }
        assert requested == set(range(11))

    def test_semantic_context_owns_native_handle(
        self, mock_lib: MagicMock
    ) -> None:
        """Checks that the semantic context outlives its source package.

        Args:
            mock_lib: Patched native functions.
        """

        mock_lib.bethkit_schema_package_open.return_value = 202
        mock_lib.bethkit_semantic_context_new.return_value = 303

        package = SchemaPackage.open(Path("candidate.bkschema"))
        context = SemanticContext(package)
        package.close()
        context.close()

        mock_lib.bethkit_semantic_context_new.assert_called_once_with(202)
        mock_lib.bethkit_semantic_context_free.assert_called_once_with(303)

    def test_diagnostic_is_immutable(self) -> None:
        """Reader-facing result models reject mutation."""

        diagnostic = Diagnostic(
            severity="error",
            code="invalid_payload",
            message="bad payload",
            record_signature=b"NPC_",
            form_id=1,
        )

        with pytest.raises(ValidationError):
            setattr(diagnostic, "message", "changed")

    def test_record_editor_sets_and_finishes(self, mock_lib: MagicMock) -> None:
        """Checks native edit dispatch and transfer into a writable record.

        Args:
            mock_lib: Patched native functions.
        """

        mock_lib.bethkit_schema_package_open.return_value = 202
        mock_lib.bethkit_semantic_context_new.return_value = 303
        mock_lib.bethkit_record_editor_new.return_value = 505
        mock_lib.bethkit_record_editor_set_u64.return_value = 0
        mock_lib.bethkit_record_editor_finish.return_value = 606

        with SchemaPackage.open(Path("candidate.bkschema")) as package:
            with SemanticContext(package) as context:
                editor = RecordEditor.new(context, _Record())
                editor.set("NPC_.DATA.level", 12)
                writable = editor.finish()
                writable.close()

        mock_lib.bethkit_record_editor_set_u64.assert_called_once_with(
            505,
            b"NPC_.DATA.level",
            0,
            12,
        )
        mock_lib.bethkit_writable_record_free.assert_called_once_with(606)
        mock_lib.bethkit_record_editor_free.assert_called_once_with(505)
