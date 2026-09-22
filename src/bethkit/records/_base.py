"""
Copyright (c) Modding Forge
"""

# Lazy immutable record models and their typed structural field references.

from __future__ import annotations

import enum
import math
import types
from typing import (
    Annotated,
    ClassVar,
    Generic,
    Optional,
    Protocol,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
)

import pydantic

from .._error import (
    RecordDecodeError,
    SchemaMismatchError,
    UnsupportedEditError,
)
from . import _values, _wire

_T = TypeVar("_T")
_Model = TypeVar("_Model", bound="RecordModel")


class Binding(pydantic.BaseModel, frozen=True):
    """Generated connection between a Python attribute and a grammar node."""

    path: str
    """Authoritative schema path."""
    kind: str
    """Schema grammar or payload node kind."""
    name: str = ""
    """Original field label, which may itself contain path separators."""
    repeated_path: Optional[str] = None
    """Native repetition scope path for repeated children."""
    child_kind: Optional[str] = None
    """Repeated child's grammar kind."""


class Variant(str):
    """Immutable annotation token, not a Pydantic value or schema provider."""

    def __new__(cls, *, path: str) -> Variant:
        """Creates a hashable native-path token without validation hooks.

        Args:
            path: Exact native schema path identifying one union alternative.

        Returns:
            Immutable metadata that Pydantic leaves out of value validation.
        """

        return super().__new__(cls, path)

    @property
    def path(self) -> str:
        """Returns the schema identity represented by this metadata token."""

        return str(self)


class FieldReference(pydantic.BaseModel, frozen=True):
    """Address-bearing base for dynamically selected fields."""

    address: Optional[_wire.FieldAddress] = None
    """Native edit address, absent for multi-subrecord grammar groups."""
    _wire_value: Optional[_wire.WireValue] = pydantic.PrivateAttr(default=None)
    _annotation: object = pydantic.PrivateAttr(default=object)


class FieldRef(FieldReference, Generic[_T], frozen=True):
    """An immutable value paired with its exact, typed editing position."""

    value: _T
    """Decoded snapshot value; modifying it never modifies a plugin."""


class StructModel(pydantic.BaseModel, frozen=True):
    """Base of generated, immutable payload and grammar models."""

    model_config = pydantic.ConfigDict(
        extra="forbid", protected_namespaces=("model_validate", "model_dump")
    )
    _schema_path: ClassVar[str] = ""
    _grammar: ClassVar[bool] = False
    _bindings: ClassVar[dict[str, Binding]] = {}
    _references: dict[str, FieldReference] = pydantic.PrivateAttr(
        default_factory=dict
    )

    def field(self, name: str) -> FieldReference:
        """Returns an addressed field from a native snapshot.

        Args:
            name: Python attribute name from this generated model.

        Returns:
            The field reference; generated overloads retain its concrete type.

        Raises:
            KeyError: The name is unknown or the model was constructed manually.
        """

        return self._references[name]


class RecordModel(StructModel, frozen=True):
    """Base of schema-pinned, lazily materialized record snapshots."""

    signature: ClassVar[str] = ""
    schema_sha256: ClassVar[str] = ""
    _snapshot: Optional[_wire.RecordSnapshot] = pydantic.PrivateAttr(
        default=None
    )

    @classmethod
    def from_snapshot(
        cls: type[_Model], snapshot: _wire.RecordSnapshot
    ) -> _Model:
        """Materializes this record type from one native-owned snapshot.

        Args:
            snapshot: Complete native semantic snapshot of one record.

        Returns:
            A typed view independent of the source plugin's lifetime.

        Raises:
            SchemaMismatchError: Signature or exact schema identity differs.
            RecordDecodeError: Native values do not match the generated model.
        """

        if snapshot.record_signature != cls.signature:
            raise SchemaMismatchError(
                f"Expected {cls.signature}, "
                f"received {snapshot.record_signature}."
            )
        if snapshot.projection != "full":
            raise RecordDecodeError(
                "Typed models require a full record snapshot."
            )
        if snapshot.schema_payload_sha256 != cls.schema_sha256:
            raise SchemaMismatchError(
                "Generated models and loaded schema differ."
            )
        try:
            model = cast(_Model, _grammar_model(cls, snapshot.fields))
        except (ValueError, TypeError, KeyError) as exc:
            raise RecordDecodeError(
                f"Cannot decode {cls.signature}: {exc}"
            ) from exc
        _set_private(model, "_snapshot", snapshot)
        return model

    @classmethod
    def from_record(
        cls: type[_Model],
        record: _RecordHandle,
        context: _SnapshotContext,
        *,
        localized: bool = False,
    ) -> _Model:
        """Decodes only the requested record through its native context.

        Args:
            record: Borrowed source record whose plugin is still open.
            context: Semantic runtime using the matching schema package.
            localized: Whether the source plugin uses external string tables.

        Returns:
            An independently owned immutable model.

        Raises:
            SchemaMismatchError: The generated and loaded schemas differ.
            RecordDecodeError: Values cannot be represented by this model.
        """

        return cls.from_snapshot(context.snapshot(record, localized=localized))


class _RecordHandle(Protocol):
    """A private lifetime-checked borrowed record contract."""

    def _native_pointer(self) -> int:
        """Checks the complete owner chain and returns a borrowed pointer."""

        ...


class _SnapshotContext(Protocol):
    """Native snapshot service without a runtime import cycle."""

    def snapshot(
        self,
        record: _RecordHandle,
        *,
        localized: bool = False,
    ) -> _wire.RecordSnapshot:
        """Copies one record into a validated, independently owned snapshot."""

        ...


def _alternatives(annotation: object) -> tuple[object, ...]:
    """Unwraps typing metadata without guessing any record grammar."""

    origin = get_origin(annotation)
    if origin is Annotated:
        return _alternatives(get_args(annotation)[0])
    if origin in (Union, types.UnionType):
        return tuple(
            member
            for item in get_args(annotation)
            if item is not type(None)
            for member in _alternatives(item)
        )
    return (annotation,)


def _selected_annotation(annotation: object, path: Optional[str]) -> object:
    """Uses native union provenance instead of guessing from scalar values."""

    if path is None:
        return annotation
    if get_origin(annotation) is Annotated:
        base, *metadata = get_args(annotation)
        if any(isinstance(item, Variant) for item in metadata):
            return _selected_annotation(base, path)
        return annotation
    if get_origin(annotation) not in (Union, types.UnionType):
        return annotation
    candidates: list[tuple[int, object]] = []
    tagged = False
    for alternative in get_args(annotation):
        if get_origin(alternative) is not Annotated:
            continue
        base, *metadata = get_args(alternative)
        for item in metadata:
            if isinstance(item, Variant):
                tagged = True
                if _under(path, item.path):
                    candidates.append((len(item.path), base))
    if candidates:
        selected = max(candidates, key=lambda item: item[0])[1]
        return _selected_annotation(selected, path)
    if tagged:
        raise ValueError(f"Native union selection is not declared: {path}")
    return annotation


def _models(annotation: object) -> tuple[type[StructModel], ...]:
    """Finds concrete generated model alternatives in an annotation."""

    return tuple(
        item
        for item in _alternatives(annotation)
        if isinstance(item, type) and issubclass(item, StructModel)
    )


def _element(annotation: object) -> object:
    """Returns the statically declared element type of a tuple."""

    for alternative in _alternatives(annotation):
        if get_origin(alternative) is tuple:
            return get_args(alternative)[0]
    raise ValueError("A repeated schema node must have a tuple annotation.")


def _under(path: str, parent: str) -> bool:
    """Checks a schema subtree using segment boundaries, not label prefixes."""

    return path == parent or path.startswith(parent + "/")


def _attach(
    model: StructModel,
    sources: dict[str, Optional[_wire.WireValue]],
) -> StructModel:
    """Attaches private provenance after Pydantic validates public values."""

    for name in type(model)._bindings:
        wire = sources.get(name)
        value: object = getattr(model, name)
        reference = FieldRef[object](
            value=value,
            address=wire.address if wire is not None else None,
        )
        _set_private(reference, "_wire_value", wire)
        _set_private(
            reference, "_annotation", type(model).model_fields[name].annotation
        )
        model._references[name] = reference
    return model


def _set_private(model: pydantic.BaseModel, name: str, value: object) -> None:
    """Sets construction-only provenance without changing frozen public data."""

    private = model.__pydantic_private__
    if private is None:
        raise TypeError("Expected a model with declared private provenance.")
    private[name] = value


def _grammar_model(
    cls: type[StructModel],
    fields: tuple[_wire.WireField, ...],
) -> StructModel:
    """Groups fields exclusively by native paths and repetition scopes."""

    values: dict[str, object] = {}
    sources: dict[str, Optional[_wire.WireValue]] = {}
    for name, binding in cls._bindings.items():
        annotation: object = cls.model_fields[name].annotation
        selected = tuple(
            field for field in fields if _under(field.path, binding.path)
        )
        if binding.kind == "repeat":
            scope_path = binding.repeated_path
            groups: dict[int, list[_wire.WireField]] = {}
            for field in selected:
                matched = False
                for scope in field.address.repeat_scopes:
                    if scope.path == scope_path:
                        groups.setdefault(scope.occurrence, []).append(field)
                        matched = True
                        break
                if not matched:
                    raise ValueError(
                        f"Missing native repeat scope: {scope_path}"
                    )
            items: list[object] = []
            for occurrence in sorted(groups):
                group = tuple(groups[occurrence])
                items.append(_grammar_value(_element(annotation), group))
            values[name] = tuple(items)
        elif not selected:
            continue
        elif binding.kind == "subrecord":
            if len(selected) != 1:
                raise ValueError(
                    f"Ambiguous non-repeated schema field {binding.path}"
                )
            field = selected[0]
            values[name] = _payload(
                annotation, field.value, field.effective_path
            )
            sources[name] = field.value
        else:
            values[name] = _grammar_value(annotation, selected)
    return _attach(cls.model_validate(values), sources)


def _grammar_value(
    annotation: object, fields: tuple[_wire.WireField, ...]
) -> object:
    """Selects grammar alternatives from actual matched native paths."""

    matching = tuple(
        model
        for model in _models(annotation)
        if model._grammar
        and any(_under(f.path, model._schema_path) for f in fields)
    )
    if len(matching) == 1:
        return _grammar_model(matching[0], fields)
    if not matching and len(fields) == 1:
        return _payload(annotation, fields[0].value, fields[0].effective_path)
    raise ValueError("Native grammar selection is missing or ambiguous.")


def _payload(
    annotation: object,
    wire: _wire.WireValue,
    effective_path: Optional[str] = None,
) -> object:
    """Materializes packed payloads without flattening their structure."""

    if isinstance(wire, _wire.WireScalar) and wire.kind == "absent":
        return None
    effective_path = wire.schema_path or effective_path
    annotation = _selected_annotation(annotation, effective_path)
    if isinstance(wire, _wire.WireArray):
        return tuple(
            _payload(_element(annotation), item) for item in wire.items
        )
    if isinstance(wire, _wire.WireStruct):
        candidates = _models(annotation)
        selected = tuple(
            model
            for model in candidates
            if (
                effective_path is not None
                and model._schema_path == effective_path
            )
            or any(_under(f.path, model._schema_path) for f in wire.fields)
        )
        if len(selected) != 1:
            if len(candidates) != 1:
                raise ValueError(
                    "Cannot identify the selected payload structure."
                )
            selected = candidates
        cls = selected[0]
        fields = {field.path: field for field in wire.fields}
        values: dict[str, object] = {}
        sources: dict[str, Optional[_wire.WireValue]] = {}
        for name, binding in cls._bindings.items():
            field = fields.get(binding.path)
            if field is not None:
                values[name] = _payload(
                    cls.model_fields[name].annotation,
                    field.value,
                    field.effective_path,
                )
                sources[name] = field.value
        return _attach(cls.model_validate(values), sources)
    value: object = wire.value
    if wire.kind == "form_id":
        value = _values.FormId(
            raw=cast(int, wire.value),
            allowed_signatures=tuple(
                bytes(sig).decode("ascii") for sig in wire.allowed_signatures
            ),
        )
    elif wire.kind == "bytes":
        value = bytes(cast(tuple[int, ...], wire.value))
    elif wire.kind == "float" and isinstance(wire.value, str):
        value = float(wire.value)
    return pydantic.TypeAdapter[object](annotation).validate_python(value)


def encode_replacement(
    reference: FieldRef[_T], value: _T
) -> dict[str, pydantic.JsonValue]:
    """Validates a replacement against its exact generated field type.

    Args:
        reference: Typed snapshot reference to an existing native field.
        value: Replacement value matching the generated field type.

    Returns:
        A tagged JSON value suitable for the authoritative native editor.

    Raises:
        UnsupportedEditError: This is a multi-subrecord grammar group.
        pydantic.ValidationError: The value violates the generated type.
    """

    if reference.address is None or reference._wire_value is None:
        raise UnsupportedEditError(
            "Edit individual fields within a grammar group."
        )
    checked = pydantic.TypeAdapter[object](
        reference._annotation
    ).validate_python(value)
    return _encode(checked, reference._wire_value)


def _encode(
    value: object,
    template: Optional[_wire.WireValue] = None,
) -> dict[str, pydantic.JsonValue]:
    """Converts validated values while retaining native signedness and paths."""

    if isinstance(value, StructModel):
        existing = (
            {field.path: field.value for field in template.fields}
            if isinstance(template, _wire.WireStruct)
            else {}
        )
        fields: list[pydantic.JsonValue] = []
        for name, binding in type(value)._bindings.items():
            member: object = getattr(value, name)
            fields.append(
                {
                    "name": binding.name,
                    "path": binding.path,
                    "value": _encode(member, existing.get(binding.path)),
                }
            )
        return {"kind": "struct", "fields": fields}
    if isinstance(value, tuple):
        items = cast(tuple[object, ...], value)
        templates = (
            template.items if isinstance(template, _wire.WireArray) else ()
        )
        return {
            "kind": "array",
            "items": [
                _encode(
                    item, templates[index] if index < len(templates) else None
                )
                for index, item in enumerate(items)
            ],
        }
    if isinstance(value, _values.FormId):
        return {"kind": "form_id", "value": value.raw}
    if isinstance(value, bytes):
        return {"kind": "bytes", "value": list(value)}
    if value is None:
        return {"kind": "absent", "value": None}
    if isinstance(value, bool):
        raise TypeError("Booleans are not native integer fields.")
    if isinstance(value, enum.IntFlag):
        return {"kind": "flags", "value": int(value)}
    if isinstance(value, enum.IntEnum):
        return {"kind": "enum", "value": int(value)}
    if isinstance(value, float) and not math.isfinite(value):
        special = (
            "NaN"
            if math.isnan(value)
            else "Infinity"
            if value > 0
            else "-Infinity"
        )
        return {"kind": "float", "value": special}
    if isinstance(value, (int, float, str)):
        kind = (
            template.kind
            if isinstance(template, _wire.WireScalar)
            else "string"
            if isinstance(value, str)
            else "float"
            if isinstance(value, float)
            else "int"
            if value < 0
            else "uint"
        )
        return {"kind": kind, "value": value}
    raise TypeError(
        f"Unsupported semantic replacement type: {type(value).__name__}"
    )
