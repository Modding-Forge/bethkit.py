"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from pydantic import BaseModel

from .decoder_requirement import DecoderRequirement
from .handler_requirement import HandlerRequirement


class SchemaManifest(BaseModel, frozen=True):
    """Immutable release provenance for one schema package."""

    format_version: int
    """Binary schema package format version."""

    game: str
    """Canonical game mode name."""

    package_version: str
    """Semantic version of the generated schema package."""

    source_repository: str
    """Repository containing the pinned xEdit source."""

    source_tag: str
    """Pinned xEdit release tag."""

    source_commit: str
    """Full pinned xEdit source commit."""

    source_archive_sha256: str
    """SHA-256 of the pinned xEdit source archive."""

    exporter_version: str
    """Version of the Bethkit xEdit exporter contract."""

    exporter_binary_sha256: str
    """SHA-256 of the exporter executable."""

    exporter_map_sha256: str
    """SHA-256 of the detailed Delphi MAP file."""

    exporter_patch_sha256: str
    """SHA-256 of the applied Bethkit exporter patch series."""

    exporter_build_sha256: str
    """SHA-256 of the reproducible exporter build inputs."""

    conversion_rules_sha256: str
    """SHA-256 of the reviewed callback conversion rules."""

    minimum_bethkit_version: str
    """Minimum compatible Bethkit library version."""

    minimum_abi_version: int
    """Minimum compatible Bethkit C ABI version."""

    validation_status: str
    """Release validation state for this package."""

    corpus_sha256: str
    """SHA-256 identifying the protected differential corpus."""

    validated_records: int
    """Number of records covered by differential validation."""

    byte_coverage: float
    """Fraction of validated payload bytes accounted for by the schema."""

    callbacks_total: int
    """Number of exported semantic callback bindings."""

    callbacks_classified: int
    """Number of reviewed and implemented callback bindings."""

    required_decoders: tuple[DecoderRequirement, ...]
    """Payload decoders required to open the package."""

    required_handlers: tuple[HandlerRequirement, ...]
    """Semantic callback handlers required to open the package."""
