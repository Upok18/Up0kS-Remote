"""
Shutdown Command
"""

from __future__ import annotations

import subprocess

from remote.version import PROTOCOL_VERSION


def shutdown(remote, data):

    subprocess.run(
        ["shutdown", "/s", "/f", "/t", "500"],
        check=False,
    )

    return {
        "version": PROTOCOL_VERSION,
        "type": "success",
        "data": {
            "message": "Shutdown started."
        },
    }

def restart(remote, data):

    subprocess.run(
        ["shutdown", "/r", "/f", "/t", "500"],
        check=False,
    )

    return {
        "version": PROTOCOL_VERSION,
        "type": "success",
        "data": {
            "message": "Restart started."
        },
    }
