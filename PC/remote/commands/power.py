"""
Shutdown Command
"""

from __future__ import annotations

import subprocess
from remote.logger import info
from remote.version import PROTOCOL_VERSION


def shutdown(data: dict) -> dict:
    """Shutdown the PC."""

    info("Shutdown command received.")

    subprocess.run(
        ["shutdown", "/s", "/f", "/t", "500"],
        check=False,
    )

    return {
        "version": PROTOCOL_VERSION,
        "type": "success",
        "data": {
            "message": "PC will shut down in 30 seconds."
            },
    }


def restart(data: dict) -> dict:
    """Restart the PC."""

    info("Restart command received.")

    subprocess.run(
        ["shutdown", "/r", "/f", "/t", "500"],
        check=False,
    )

    return {
        "version": PROTOCOL_VERSION,
        "type": "success",
        "data": {
            "message": "PC will restart in 30 seconds."
            },
    }
