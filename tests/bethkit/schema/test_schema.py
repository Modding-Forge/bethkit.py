"""Tests for owned ABI-v2 schema handles and immutable models."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest
from pydantic import ValidationError

from bethkit import (
    Diagnostic,
    Game,
    SchemaCatalog,
    SchemaPackage,
    SemanticContext,
)


def test_catalog_embedded_is_owned(mock_lib: MagicMock) -> None:
    """The embedded factory returns a handle that is released on close."""
    mock_lib.bethkit_schema_catalog_embedded.return_value = 101

    catalog = SchemaCatalog.embedded()
    catalog.close()

    mock_lib.bethkit_schema_catalog_free.assert_called_once_with(101)


def test_catalog_package_uses_all_game_enum_values(mock_lib: MagicMock) -> None:
    """Every public game can be requested from the catalog."""
    mock_lib.bethkit_schema_catalog_embedded.return_value = 101
    mock_lib.bethkit_schema_catalog_package.return_value = 202

    with SchemaCatalog.embedded() as catalog:
        packages = [catalog.package(game) for game in Game]
        for package in packages:
            package.close()

    requested = {
        call.args[1] for call in mock_lib.bethkit_schema_catalog_package.call_args_list
    }
    assert requested == set(range(11))


def test_semantic_context_owns_native_handle(mock_lib: MagicMock) -> None:
    """A semantic context is independent from its package handle."""
    mock_lib.bethkit_schema_package_open.return_value = 202
    mock_lib.bethkit_semantic_context_new.return_value = 303

    package = SchemaPackage.open(Path("candidate.bkschema"))
    context = SemanticContext(package)
    package.close()
    context.close()

    mock_lib.bethkit_semantic_context_new.assert_called_once_with(202)
    mock_lib.bethkit_semantic_context_free.assert_called_once_with(303)


def test_diagnostic_is_immutable() -> None:
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
