"""
Shutdown Command
"""

from __future__ import annotations

import subprocess

from remote.version import PROTOCOL_VERSION


def shutdown(remote, data):

    response = {
        "version": PROTOCOL_VERSION,
        "type": "success",
        "data": {
            "message": "Shutdown started."
        },
    }

    subprocess.run(
        ["shutdown", "/s", "/f", "/t", "30"],
        check=False,
    )

    return response


def restart(remote, data):

    response = {
        "version": PROTOCOL_VERSION,
        "type": "success",
        "data": {
            "message": "Restart started."
        },
    }

    subprocess.run(
        ["shutdown", "/r", "/f", "/t", "30"],
        check=False,
    )

    return response