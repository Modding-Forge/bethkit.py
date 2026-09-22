"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from bethkit import (
    BethkitClosedError,
    BethkitNativeError,
    Game,
    RecordEditor,
    RecordView,
    SchemaCatalog,
    SchemaPackage,
    SemanticContext,
)

_HandleType = (
    type[SchemaCatalog]
    | type[SchemaPackage]
    | type[RecordView]
    | type[RecordEditor]
)
"""Factory-only schema wrapper classes covered by ownership checks."""


class _Record:
    """Supplies a borrowed record pointer without loading native code."""

    def _native_pointer(self) -> int:
        """Returns the fake record pointer for mocked decoder calls."""

        return 404


class TestSchemaOwnership:
    """Checks factory-only adoption and failure-safe native lifetimes."""

    @pytest.mark.parametrize(
        "handle_type", [SchemaCatalog, SchemaPackage, RecordView, RecordEditor]
    )
    def test_rejects_public_pointer_adoption(
        self, mock_lib: MagicMock, handle_type: _HandleType
    ) -> None:
        """Rejects caller-supplied pointers without freeing arbitrary memory.

        Args:
            mock_lib: Patched native functions.
            handle_type: Factory-only owner class being tested.
        """

        # when
        with pytest.raises(TypeError, match="factory"):
            handle_type()
        constructor = cast(Callable[[int], object], handle_type)
        with pytest.raises(TypeError):
            constructor(123)

        # then
        mock_lib.bethkit_schema_catalog_free.assert_not_called()
        mock_lib.bethkit_schema_package_free.assert_not_called()
        mock_lib.bethkit_record_view_free.assert_not_called()
        mock_lib.bethkit_record_editor_free.assert_not_called()

    @pytest.mark.parametrize(
        "handle_type", [SchemaCatalog, SchemaPackage, RecordView, RecordEditor]
    )
    def test_private_factory_rejects_null(
        self, handle_type: _HandleType
    ) -> None:
        """Rejects null handles before creating a native owner.

        Args:
            handle_type: Factory-only owner class being tested.
        """

        with pytest.raises(ValueError, match="null"):
            handle_type._from_native(0)

    @pytest.mark.parametrize(
        "handle_type", [SchemaCatalog, SchemaPackage, RecordView, RecordEditor]
    )
    def test_closed_handle_cannot_reenter(
        self, mock_lib: MagicMock, handle_type: _HandleType
    ) -> None:
        """Rejects a closed owner's context before a native call is attempted.

        Args:
            mock_lib: Patched native functions.
            handle_type: Factory-only owner class being tested.
        """

        # given
        handle = handle_type._from_native(101)
        handle.close()
        handle.close()
        mock_lib.reset_mock()

        # when
        with pytest.raises(BethkitClosedError):
            with handle:
                pytest.fail("A closed handle entered its context.")

        # then
        assert not mock_lib.mock_calls

    @pytest.mark.parametrize("from_disk", [False, True])
    def test_catalog_adoption_failure_frees_allocation(
        self, mock_lib: MagicMock, mocker: MockerFixture, from_disk: bool
    ) -> None:
        """Releases an embedded catalog when its Python owner cannot be created.

        Args:
            mock_lib: Patched native functions.
            mocker: Mock manager replacing only the private adoption factory.
            from_disk: Exercise the file factory instead of the embedded one.
        """

        mock_lib.bethkit_schema_catalog_embedded.return_value = 101
        mock_lib.bethkit_schema_catalog_open.return_value = 101
        mocker.patch.object(
            SchemaCatalog, "_from_native", side_effect=MemoryError("adoption")
        )
        with pytest.raises(MemoryError, match="adoption"):
            if from_disk:
                SchemaCatalog.open(Path("candidate.bkschemas"))
            else:
                SchemaCatalog.embedded()
        mock_lib.bethkit_schema_catalog_free.assert_called_once_with(101)

    def test_package_adoption_failure_frees_allocation(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Releases a package when its Python owner cannot be created.

        Args:
            mock_lib: Patched native functions.
            mocker: Mock manager replacing only the private adoption factory.
        """

        mock_lib.bethkit_schema_package_open.return_value = 202
        mocker.patch.object(
            SchemaPackage, "_from_native", side_effect=MemoryError("adoption")
        )
        with pytest.raises(MemoryError, match="adoption"):
            SchemaPackage.open(Path("candidate.bkschema"))
        mock_lib.bethkit_schema_package_free.assert_called_once_with(202)

    def test_catalog_package_adoption_failure_frees_allocation(
        self, mock_lib: MagicMock, mocker: MockerFixture
    ) -> None:
        """Releases a catalog-derived package when adoption fails.

        Args:
            mock_lib: Patched native functions.
            mocker: Mock manager replacing only the package adoption factory.
        """

        mock_lib.bethkit_schema_catalog_embedded.return_value = 101
        mock_lib.bethkit_schema_catalog_package.return_value = 202
        mocker.patch.object(
            SchemaPackage, "_from_native", side_effect=MemoryError("adoption")
        )
        with SchemaCatalog.embedded() as catalog:
            with pytest.raises(MemoryError, match="adoption"):
                catalog.package(Game.SKYRIM_SE)
        mock_lib.bethkit_schema_package_free.assert_called_once_with(202)

    @pytest.mark.parametrize("handle_type", [RecordView, RecordEditor])
    def test_record_adoption_failure_frees_allocation(
        self,
        mock_lib: MagicMock,
        mocker: MockerFixture,
        handle_type: type[RecordView] | type[RecordEditor],
    ) -> None:
        """Releases an independently decoded record when adoption fails.

        Args:
            mock_lib: Patched native functions.
            mocker: Mock manager replacing only the result adoption factory.
            handle_type: View or editor factory being tested.
        """

        mock_lib.bethkit_schema_package_open.return_value = 202
        mock_lib.bethkit_semantic_context_new.return_value = 303
        mock_lib.bethkit_record_view_new.return_value = 505
        mock_lib.bethkit_record_editor_new.return_value = 505
        mocker.patch.object(
            handle_type, "_from_native", side_effect=MemoryError("adoption")
        )
        with SchemaPackage.open(Path("candidate.bkschema")) as package:
            with SemanticContext(package) as context:
                with pytest.raises(MemoryError, match="adoption"):
                    handle_type.new(context, _Record())
        free = (
            mock_lib.bethkit_record_view_free
            if handle_type is RecordView
            else mock_lib.bethkit_record_editor_free
        )
        free.assert_called_once_with(505)

    def test_context_failure_does_not_free_uninitialized_handle(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps a failed runtime construction in an inert closed state.

        Args:
            mock_lib: Patched native functions.
        """

        mock_lib.bethkit_schema_package_open.return_value = 202
        mock_lib.bethkit_semantic_context_new.return_value = 0
        mock_lib.bethkit_last_error.return_value = b"cannot create context"
        with SchemaPackage.open(Path("candidate.bkschema")) as package:
            with pytest.raises(BethkitNativeError, match="cannot create"):
                SemanticContext(package)
        mock_lib.bethkit_semantic_context_free.assert_not_called()

    @pytest.mark.parametrize(
        ("handle_type", "free_name"),
        [
            (SchemaCatalog, "bethkit_schema_catalog_free"),
            (SchemaPackage, "bethkit_schema_package_free"),
            (RecordView, "bethkit_record_view_free"),
            (RecordEditor, "bethkit_record_editor_free"),
        ],
    )
    def test_failed_cleanup_disarms_owner(
        self, mock_lib: MagicMock, handle_type: _HandleType, free_name: str
    ) -> None:
        """Avoids a second free attempt after native cleanup raises.

        Args:
            mock_lib: Patched native functions.
            handle_type: Factory-only owner class being tested.
            free_name: Matching native destructor on the mocked library.
        """

        # given
        handle = handle_type._from_native(101)
        free = cast(MagicMock, getattr(mock_lib, free_name))
        free.side_effect = RuntimeError("cleanup failed")

        # when
        with pytest.raises(RuntimeError, match="cleanup failed"):
            handle.close()
        handle.close()

        # then
        free.assert_called_once_with(101)
        with pytest.raises(BethkitClosedError):
            handle.__enter__()

    def test_failed_context_cleanup_disarms_owner(
        self, mock_lib: MagicMock
    ) -> None:
        """Avoids a second runtime free after its destructor raises.

        Args:
            mock_lib: Patched native functions.
        """

        # given
        mock_lib.bethkit_schema_package_open.return_value = 202
        mock_lib.bethkit_semantic_context_new.return_value = 303
        mock_lib.bethkit_semantic_context_free.side_effect = RuntimeError(
            "cleanup failed"
        )
        with SchemaPackage.open(Path("candidate.bkschema")) as package:
            context = SemanticContext(package)

        # when
        with pytest.raises(RuntimeError, match="cleanup failed"):
            context.close()
        context.close()

        # then
        mock_lib.bethkit_semantic_context_free.assert_called_once_with(303)
        with pytest.raises(BethkitClosedError):
            context.__enter__()
