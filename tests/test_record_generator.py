"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import ast
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest

from bethkit.records import _schema
from scripts import _generation_names, generate_records
from scripts._record_generator import RecordGenerator

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def _record(signature: bytes = b"TEST") -> _schema.RecordDefinition:
    """Builds a minimal supported record definition without native code.

    Args:
        signature: Four-byte signature used for the record and root name.

    Returns:
        An immutable grammar with one primitive string child.
    """

    name = signature.decode("ascii")
    text = _schema.SchemaNode(
        id=2,
        path=f"/{name}/text",
        name="Text",
        kind="primitive",
        primitive=_schema.PrimitiveSpec(type="string"),
    )
    root = _schema.SchemaNode(
        id=1, path=f"/{name}", name=name, kind="sequence", children=(text,)
    )
    return _schema.RecordDefinition(
        signature=cast(tuple[int, int, int, int], tuple(signature)),
        name=name,
        root=root,
    )


def _graph(*records: _schema.RecordDefinition) -> _schema.SchemaGraph:
    """Wraps record fixtures in a versioned Skyrim SE schema graph.

    Args:
        *records: Definitions to expose in their supplied order.

    Returns:
        An immutable graph with a stable synthetic schema identity.
    """

    return _schema.SchemaGraph(
        format_version=1,
        payload_sha256="a" * 64,
        manifest={"game": "skyrim_se"},
        records=records,
    )


class TestRecordGenerator:
    """Validates deterministic generation and malformed-schema rejection."""

    def test_order_and_repeated_render_are_deterministic(
        self, mocker: MockerFixture
    ) -> None:
        """Keeps generated sources stable without loading the native library.

        Args:
            mocker: Fixture replacing native loading with a failure sentinel.
        """

        # given
        native_loader = mocker.patch("bethkit._ffi.load_lib")
        first, second = _record(), _record(b"ABCD")

        # when
        expected = generate_records.generate(_graph(first, second))
        actual = generate_records.generate(_graph(second, first))
        compiler = RecordGenerator(first, "a" * 64)

        # then
        assert list(actual) == list(expected)
        assert actual == expected
        assert compiler.render() == compiler.render()
        assert "Optional[str]" in actual["test.py"]
        for filename, source in actual.items():
            ast.parse(source, filename=filename)
        native_loader.assert_not_called()

    @pytest.mark.parametrize(
        "node",
        [
            _schema.SchemaNode(id=3, path="/bad", name="Bad", kind="array"),
            _schema.SchemaNode(id=3, path="/bad", name="Bad", kind="union"),
            _schema.SchemaNode(id=3, path="/bad", name="Bad", kind="primitive"),
            _schema.SchemaNode(
                id=3,
                path="/bad",
                name="Bad",
                kind="primitive",
                primitive=_schema.PrimitiveSpec(type="integer"),
            ),
            _schema.SchemaNode(
                id=3, path="/bad", name="Bad", kind="reference", target="/lost"
            ),
            _schema.SchemaNode(
                id=3, path="/bad", name="Bad", kind="unsupported"
            ),
        ],
    )
    def test_malformed_nodes_fail(self, node: _schema.SchemaNode) -> None:
        """Rejects incomplete definitions instead of emitting generic values.

        Args:
            node: Invalid structural or primitive definition.
        """

        # given
        compiler = RecordGenerator(_record(), "a" * 64)

        # when / then
        with pytest.raises(ValueError, match="/bad"):
            compiler.annotation(node)

    def test_duplicate_modules_fail(self) -> None:
        """Rejects duplicate signatures before overwriting generated output."""

        record = _record()
        with pytest.raises(ValueError, match="Duplicate.*module"):
            generate_records.generate(_graph(record, record))

    def test_unsafe_signature_fails(self) -> None:
        """Rejects a schema signature that could escape the output directory."""

        with pytest.raises(ValueError, match="Invalid record signature"):
            generate_records.generate(_graph(_record(b"../A")))

    def test_empty_game_fails(self) -> None:
        """Rejects an empty game package instead of emitting invalid Python."""

        with pytest.raises(ValueError, match="at least one record"):
            generate_records.generate(_graph())

    def test_different_game_fails(self) -> None:
        """Rejects a graph that is not intended for the Skyrim SE package."""

        graph = _graph(_record()).model_copy(
            update={"manifest": {"game": "fo4"}}
        )
        with pytest.raises(ValueError, match="Skyrim SE"):
            generate_records.generate(graph)

    def test_names_and_literals_are_stable(self) -> None:
        """Preserves awkward source labels and long Unicode string contents."""

        value = "A quoted 'path' \\ value with Unicode: ä" * 6
        name = _generation_names.identifier("9 model " + "x" * 90)
        assert name == _generation_names.identifier("9 model " + "x" * 90)
        assert name.isidentifier() and len(name) <= 54
        assert _generation_names.identifier("class") == "class_value"
        assert ast.literal_eval(_generation_names.literal(value)) == value


class TestGeneratedFileVerification:
    """Verifies exact output trees, including obsolete generated modules."""

    def test_matching_sources_pass(self, tmp_path: Path) -> None:
        """Accepts matching source while ignoring bytecode cache files.

        Args:
            tmp_path: Isolated output package directory.
        """

        sources = {"test.py": "value = 1\n"}
        (tmp_path / "test.py").write_text(sources["test.py"], encoding="utf-8")
        (tmp_path / "test.pyc").write_bytes(b"ignored")
        generate_records.verify_files(sources, tmp_path)

    @pytest.mark.parametrize("relative", ["obsolete.py", "nested/stale.py"])
    def test_extra_modules_fail(self, tmp_path: Path, relative: str) -> None:
        """Rejects unexpected Python modules even in nested directories.

        Args:
            tmp_path: Isolated output package directory.
            relative: Unexpected module path below that directory.
        """

        extra = tmp_path / relative
        extra.parent.mkdir(parents=True, exist_ok=True)
        extra.write_text("value = 1\n", encoding="utf-8")
        with pytest.raises(SystemExit, match="Unexpected generated models"):
            generate_records.verify_files({}, tmp_path)

    @pytest.mark.parametrize("present", [False, True])
    def test_missing_or_changed_sources_fail(
        self, tmp_path: Path, present: bool
    ) -> None:
        """Rejects absent files and stale contents with a precise path.

        Args:
            tmp_path: Isolated output package directory.
            present: Whether a stale file should exist instead of being absent.
        """

        if present:
            (tmp_path / "test.py").write_text("old = 1\n", encoding="utf-8")
        with pytest.raises(SystemExit, match="Generated model differs"):
            generate_records.verify_files({"test.py": "new = 2\n"}, tmp_path)
