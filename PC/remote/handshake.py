"""
Up0k Remote
Handshake Manager
"""

from __future__ import annotations

from remote.version import NAME, VERSION, PROTOCOL_VERSION


def create_hello():
    return {
        "type": "hello",
        "data": {
            "app": NAME,
            "version": VERSION,
            "protocol": PROTOCOL_VERSION,
            "authentication": True,
        },
    }
