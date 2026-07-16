"""
Ping Command
"""

from __future__ import annotations

from remote.version import PROTOCOL_VERSION


def ping(remote, data: dict) -> dict:
    """Reply with PONG."""

    return {
        "version": PROTOCOL_VERSION,
        "type": "pong",
        "data": {
            "message": "PONG"
            },
    }
