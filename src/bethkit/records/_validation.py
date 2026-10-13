"""
Copyright (c) Modding Forge
"""

from __future__ import annotations

from typing import cast

import pydantic


def validate_annotation(annotation: object, value: object) -> object:
    """Validates data against a trusted generated runtime annotation.

    Args:
        annotation: Runtime schema type, including unions and Annotated forms.
        value: External value to validate without bypassing Pydantic.

    Returns:
        Validated value with the generated annotation's runtime constraints.

    Raises:
        pydantic.ValidationError: Data does not satisfy the generated type.
        pydantic.PydanticSchemaGenerationError: The annotation is unsupported.
    """

    # Python 3.10 cannot express TypeForm for dynamically generated annotations.
    # The cast adapts static typing only; Pydantic receives the original object.
    adapter = pydantic.TypeAdapter[object](cast(type[object], annotation))
    return adapter.validate_python(value)
