"""
Up0k Remote
Protocol Utilities
"""

from __future__ import annotations

import json


def encode_packet(data: dict) -> bytes:
    """Convert a dictionary into bytes."""

    return json.dumps(data).encode("utf-8")


def decode_packet(data: bytes) -> dict:
    """Convert bytes into a dictionary."""

    return json.loads(data.decode("utf-8"))
