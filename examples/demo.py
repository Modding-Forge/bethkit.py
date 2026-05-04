"""
Copyright (c) Modding Forge

Demo script — showcases the core bethkit.py API against a real Skyrim SE plugin.

Usage:
    uv run examples/demo.py <path-to-plugin.esp>

The script prints:
  - Plugin kind and masters
  - First 20 records with their FormID, signature, and EditorID
  - A schema-decoded view of the first NPC_ record found
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

from bethkit import Game, Plugin, RecordView, SchemaRegistry
from bethkit.plugin.plugin import Group, Record


def _iter_records(group: Group) -> list[Record]:
    """
    Collect all Record children from a group (non-recursive).

    Args:
        group (Group): The group to iterate.

    Returns:
        list[Record]: All direct Record children.
    """
    result: list[Record] = []
    for child in group:
        if isinstance(child, Record):
            result.append(child)
    return result


def print_plugin_info(plugin: Plugin) -> None:
    """
    Print basic plugin metadata.

    Args:
        plugin (Plugin): The loaded plugin.
    """
    print(f"Kind   : {plugin.kind.name}")
    print(f"Masters: {plugin.masters or '(none)'}")
    print(f"Groups : {plugin.group_count}")
    print()


def print_records(plugin: Plugin, limit: int = 20) -> None:
    """
    Print the first *limit* records found across all top-level groups.

    Args:
        plugin (Plugin): The loaded plugin.
        limit (int): Maximum number of records to print.
    """
    count: int = 0
    for group in plugin:
        for record in _iter_records(group):
            sig = record.signature.decode("ascii", errors="replace")
            eid: Optional[str] = record.editor_id
            fid: int = record.form_id
            print(f"  [{sig}] 0x{fid:08X}  {eid or '—'}")
            count += 1
            if count >= limit:
                return


def demo_schema(plugin: Plugin) -> None:
    """
    Find the first NPC_ record and decode it via the SSE schema registry.

    Args:
        plugin (Plugin): The loaded plugin.
    """
    registry = SchemaRegistry.sse()
    for group in plugin:
        for record in _iter_records(group):
            if record.signature == b"NPC_":
                with RecordView.new(record, b"NPC_") as view:
                    print(
                        f"Schema view for NPC_ 0x{record.form_id:08X}"
                        f" ({record.editor_id or 'no EditorID'}):"
                    )
                    for field in view.fields():
                        print(f"  {field.name:20s} = {field.value}")
                return
    print("No NPC_ record found in plugin.")


def main() -> None:
    """Entry point for the demo script."""
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <plugin.esp|esm|esl>")
        sys.exit(1)

    plugin_path = Path(sys.argv[1])
    if not plugin_path.exists():
        print(f"File not found: {plugin_path}")
        sys.exit(1)

    print(f"Loading: {plugin_path.name}")
    print()

    with Plugin.open(plugin_path, Game.SKYRIM_SE) as plugin:
        print_plugin_info(plugin)

        print(f"First records (up to 20):")
        print_records(plugin)
        print()

        print("Schema demo (first NPC_ record):")
        demo_schema(plugin)


if __name__ == "__main__":
    main()
