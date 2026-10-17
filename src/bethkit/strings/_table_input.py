"""
Copyright (c) Modding Forge
"""

from io import BytesIO
from typing import BinaryIO


def require_bytes(data: object) -> bytes:
    """Validates untrusted bytes supplied directly or by a binary stream.

    Args:
        data: Value crossing the public input boundary.

    Returns:
        The original immutable byte sequence without copying it.

    Raises:
        TypeError: Input is not bytes.
    """

    if not isinstance(data, bytes):
        raise TypeError("String table input must be bytes.")
    return data


def read_stream(stream: BinaryIO) -> bytes:
    """Reads a caller-owned binary stream without seeking or closing it.

    Args:
        stream: Blocking binary stream positioned at the table header.

    Returns:
        All remaining serialized bytes, including header and directory.

    Raises:
        TypeError: A read returns text or another non-byte value.
        OSError: The source cannot be read.
        ValueError: The source stream is closed.
    """

    with BytesIO() as output:
        while True:
            chunk = require_bytes(stream.read(1024 * 1024))
            if not chunk:
                return output.getvalue()
            output.write(chunk)
