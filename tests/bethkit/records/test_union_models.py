"""
Copyright (c) Modding Forge
"""

# Regression cases for exact union selection and schema-provided field names.

from __future__ import annotations

from typing import Literal

import pytest

from bethkit.records import _base, _wire
from bethkit.records.skyrim_se import acti, info, refr

_PROPERTY_VALUE: str = (
    "ACTI/1:Virtual Machine Adapter/payload/2:Scripts/element"
    "/2:Properties/element/3:Value"
)


def _address(path: str) -> _wire.FieldAddress:
    """Builds immutable provenance without loading a native library.

    Args:
        path: Schema path of the tested value.

    Returns:
        Synthetic address used only by pure model conversion tests.
    """

    return _wire.FieldAddress(
        schema_payload_sha256=acti.ActivatorRecord.schema_sha256,
        structure_hash="test structure",
        record_signature=(65, 67, 84, 73),
        form_id=0x800,
        subrecord_index=0,
        subrecord_path=path,
    )


class TestUnionModelRegression:
    """Uses exact native-selected paths for union alternatives."""

    @pytest.mark.parametrize(
        ("variant", "kind", "values"),
        [
            ("7:Array of String", "string", ("hello", "world")),
            ("8:Array of Int32", "int", (-7, 42)),
        ],
    )
    def test_vmad_arrays_select_native_element_type(
        self,
        variant: str,
        kind: Literal["string", "int"],
        values: tuple[str, ...] | tuple[int, ...],
    ) -> None:
        """Does not decode string or integer arrays as VMAD object arrays.

        Args:
            variant: Native-selected schema alternative.
            kind: Scalar kind of all array elements.
            values: Homogeneous native array payload.
        """

        # given
        selected_path = f"{_PROPERTY_VALUE}/variants/{variant}"
        address = _address(_PROPERTY_VALUE)
        wire = _wire.WireArray(
            kind="array",
            address=address,
            items=tuple(
                _wire.WireScalar(kind=kind, address=address, value=value)
                for value in values
            ),
        )
        annotation = acti.Property174.model_fields["value"].annotation
        # when
        decoded = _base._payload(annotation, wire, selected_path)
        # then
        assert decoded == values

    def test_condition_scalar_union_retains_selected_enum(self) -> None:
        """Retains the selected Sex enum type for a condition parameter."""

        # given
        path = (
            "INFO/10:Conditions/repeat/0:Condition/0:CTDA/payload"
            "/5:Parameter #1/variants/5:Sex"
        )
        wire = _wire.WireScalar(
            kind="enum", address=_address(path), value=1, names=("Female",)
        )
        annotation = info.Structure9471.model_fields["parameter_1"].annotation
        # when
        decoded = _base._payload(annotation, wire, path)
        # then
        assert isinstance(decoded, info.Sex9485)
        assert decoded is info.Sex9485.FEMALE

    def test_struct_names_preserve_slashes_in_schema_labels(self) -> None:
        """Does not derive field labels from ambiguous path delimiters."""

        # given
        light = refr.Structure15752(
            fov_90=90.0,
            fade_1_35=1.35,
            end_distance_cap=100.0,
            shadow_depth_bias=0.0,
        )
        # when
        encoded = _base._encode(light)
        # then
        fields = encoded["fields"]
        assert isinstance(fields, list)
        first, second = fields[:2]
        assert isinstance(first, dict) and isinstance(second, dict)
        assert first["name"] == "FOV 90+/-"
        assert second["name"] == "Fade 1.35+/-"
