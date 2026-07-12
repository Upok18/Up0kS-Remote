"""
Up0k Remote
Info Command
"""

from __future__ import annotations

import platform
import socket
from remote.version import PROTOCOL_VERSION


def execute(data: dict) -> dict:
    """Return information about this PC."""

    return {
        "version": PROTOCOL_VERSION,
        "type": "info",
        "data": {
            "device_name": socket.gethostname(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        },
    }
