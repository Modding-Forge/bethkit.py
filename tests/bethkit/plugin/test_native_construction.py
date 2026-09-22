"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import gc
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

import pytest

from bethkit import (
    Archive,
    ArchiveEntry,
    Ba2Dx10Writer,
    Ba2GnrlWriter,
    Ba2Version,
    BsaVersion,
    BsaWriter,
    Game,
    Group,
    LocalizationSet,
    Plugin,
    PluginCache,
    PluginPatcher,
    PluginWriter,
    Record,
    StringFileKind,
    StringTable,
    SubRecord,
    WritableGroup,
    WritableRecord,
)

if TYPE_CHECKING:
    from unittest.mock import MagicMock

    from pytest_mock import MockerFixture


class _OwnedResource(Protocol):
    """Minimal resource contract used by lifetime regression tests."""

    def close(self) -> None:
        """Releases owned resources exactly once."""

        ...


class TestNativeConstruction:
    """Rejects public adoption of untrusted native addresses."""

    @pytest.mark.parametrize(
        ("owner_type", "factory", "arguments", "allocator", "free_name"),
        [
            (
                Plugin,
                Plugin.open,
                (Path("source.esp"), Game.SKYRIM_SE),
                "bethkit_plugin_open",
                "bethkit_plugin_free",
            ),
            (
                Plugin,
                Plugin.from_bytes,
                (b"", Game.SKYRIM_SE),
                "bethkit_plugin_open_from_bytes",
                "bethkit_plugin_free",
            ),
            (
                Archive,
                Archive.open,
                (Path("source.bsa"),),
                "bethkit_archive_open",
                "bethkit_archive_free",
            ),
            (
                WritableGroup,
                WritableGroup.new,
                (b"NPC_",),
                "bethkit_writable_group_new",
                "bethkit_writable_group_free",
            ),
            (
                WritableRecord,
                WritableRecord.new,
                (b"NPC_",),
                "bethkit_writable_record_new",
                "bethkit_writable_record_free",
            ),
            (
                StringTable,
                StringTable.new,
                (StringFileKind.STRINGS,),
                "bethkit_string_table_new",
                "bethkit_string_table_free",
            ),
            (
                StringTable,
                StringTable.open,
                (Path("source.strings"),),
                "bethkit_string_table_open",
                "bethkit_string_table_free",
            ),
            (
                LocalizationSet,
                LocalizationSet.new,
                (),
                "bethkit_localization_set_new",
                "bethkit_localization_set_free",
            ),
            (
                LocalizationSet,
                LocalizationSet.open,
                (Path("source.esp"), "english"),
                "bethkit_localization_set_open",
                "bethkit_localization_set_free",
            ),
        ],
    )
    def test_wrapper_creation_failure_releases_native_allocation(
        self,
        owner_type: type[object],
        factory: Callable[..., object],
        arguments: tuple[object, ...],
        allocator: str,
        free_name: str,
        mock_lib: MagicMock,
        mocker: MockerFixture,
    ) -> None:
        """Keeps failed Python allocation from leaking the native allocation.

        Args:
            owner_type: Wrapper class whose private adoption will fail.
            factory: Public creation method allocating the native owner.
            arguments: Valid public factory arguments.
            allocator: Native allocation function returning the owned pointer.
            free_name: Matching destructor expected on adoption failure.
            mock_lib: Mock native library used instead of real memory.
            mocker: Fixture injecting the Python allocation failure.
        """

        # given
        getattr(mock_lib, allocator).return_value = 0x100
        mocker.patch.object(
            owner_type,
            "_from_native",
            side_effect=MemoryError("wrapper failed"),
        )

        # when
        with pytest.raises(MemoryError, match="wrapper failed"):
            factory(*arguments)
        gc.collect()

        # then
        getattr(mock_lib, free_name).assert_called_once_with(0x100)

    @pytest.mark.parametrize(
        ("factory", "arguments", "free_name"),
        [
            (Plugin._from_native, (0x100,), "bethkit_plugin_free"),
            (Archive._from_native, (0x100,), "bethkit_archive_free"),
            (
                WritableRecord._from_native,
                (0x100,),
                "bethkit_writable_record_free",
            ),
            (
                WritableGroup._from_native,
                (0x100,),
                "bethkit_writable_group_free",
            ),
            (PluginCache, (), "bethkit_plugin_cache_free"),
            (PluginWriter, (Game.SKYRIM_SE,), "bethkit_plugin_writer_free"),
            (BsaWriter, (BsaVersion.SSE,), "bethkit_bsa_writer_free"),
            (Ba2GnrlWriter, (Ba2Version.V1,), "bethkit_ba2_gnrl_writer_free"),
            (Ba2Dx10Writer, (Ba2Version.V1,), "bethkit_ba2_dx10_writer_free"),
        ],
    )
    def test_failing_destructor_is_never_called_twice(
        self,
        factory: Callable[..., _OwnedResource],
        arguments: tuple[object, ...],
        free_name: str,
        mock_lib: MagicMock,
    ) -> None:
        """Disarms ownership before cleanup that could fail or reenter Python.

        Args:
            factory: Public constructor or private native-adoption method.
            arguments: Valid arguments with mocked native operations.
            free_name: Native free function corresponding to the owner.
            mock_lib: Mock native library reporting the simulated failure.
        """

        # given
        release: MagicMock = getattr(mock_lib, free_name)
        release.side_effect = RuntimeError("destructor failure")
        owner = factory(*arguments)

        # when
        with pytest.raises(RuntimeError, match="destructor failure"):
            owner.close()
        owner.close()
        del owner
        gc.collect()

        # then
        release.assert_called_once()

    def test_patcher_disarms_before_failing_cleanup(
        self, mock_lib: MagicMock
    ) -> None:
        """Keeps the independent patcher closed after its destructor fails.

        Args:
            mock_lib: Mock native library with a failing patcher destructor.
        """

        # given
        mock_lib.bethkit_plugin_patcher_free.side_effect = RuntimeError("free")
        with Plugin._from_native(0x100) as source:
            owner = PluginPatcher(source)

            # when
            with pytest.raises(RuntimeError, match="free"):
                owner.close()
            owner.close()
            del owner
            gc.collect()

        # then
        mock_lib.bethkit_plugin_patcher_free.assert_called_once()

    @pytest.mark.parametrize(
        "constructor",
        [
            Plugin,
            Archive,
            WritableRecord,
            WritableGroup,
            Record,
            Group,
            SubRecord,
            ArchiveEntry,
        ],
    )
    @pytest.mark.parametrize("arguments", [(), (0xDEAD,)])
    def test_public_construction_never_frees_memory(
        self,
        constructor: Callable[..., object],
        arguments: tuple[int, ...],
        mock_lib: MagicMock,
    ) -> None:
        """Rejects construction without adopting or freeing an address.

        Args:
            constructor: Public native-wrapper class under test.
            arguments: Empty arguments or an untrusted raw address.
            mock_lib: Mock native library that detects unsafe cleanup calls.
        """

        # when
        with pytest.raises(TypeError):
            constructor(*arguments)
        gc.collect()

        # then
        mock_lib.bethkit_plugin_free.assert_not_called()
        mock_lib.bethkit_archive_free.assert_not_called()
        mock_lib.bethkit_writable_record_free.assert_not_called()
        mock_lib.bethkit_writable_group_free.assert_not_called()

    @pytest.mark.parametrize(
        "factory",
        [
            Plugin._from_native,
            Archive._from_native,
            WritableRecord._from_native,
            WritableGroup._from_native,
        ],
    )
    def test_private_adoption_rejects_null(
        self, factory: Callable[[int], object], mock_lib: MagicMock
    ) -> None:
        """Rejects absent allocations without calling native functions.

        Args:
            factory: Private allocation-adoption method under test.
            mock_lib: Mock native library that detects accidental FFI calls.
        """

        # when
        with pytest.raises(ValueError, match="null"):
            factory(0)

        # then
        assert not mock_lib.mock_calls
