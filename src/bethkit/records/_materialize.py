"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

import types
from typing import Annotated, Optional, Union, cast, get_args, get_origin

import pydantic

from . import _values, _wire
from ._field_ref import FieldRef
from ._struct_model import StructModel
from ._variant import Variant


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
        set_private(reference, "_wire_value", wire)
        set_private(
            reference, "_annotation", type(model).model_fields[name].annotation
        )
        model._references[name] = reference
    return model


def set_private(model: pydantic.BaseModel, name: str, value: object) -> None:
    """Sets construction-only provenance without changing frozen public data."""

    private = model.__pydantic_private__
    if private is None:
        raise TypeError("Expected a model with declared private provenance.")
    private[name] = value


def grammar_model(
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
        return grammar_model(matching[0], fields)
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
