"""
Up0k Remote
Handshake Manager
"""

from __future__ import annotations

from remote.version import NAME, VERSION, PROTOCOL_VERSION


def create_hello() -> dict:
    """Create the server hello packet."""

    return {
        "version": PROTOCOL_VERSION,
        "action": "hello",
        "data": {
            "app": NAME,
            "server_version": VERSION,
            "protocol_version": PROTOCOL_VERSION,
            "authentication": True,
        },
    }
