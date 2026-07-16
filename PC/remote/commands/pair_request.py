"""
Pair Request Command
"""

from __future__ import annotations

from remote.version import PROTOCOL_VERSION


def execute(remote, data):

    if not remote.pairing_active():

        return {
            "version": PROTOCOL_VERSION,
            "type": "error",
            "data": {
                "message": "Pairing is not active."
            },
        }

    return {
        "version": PROTOCOL_VERSION,
        "type": "pair_code",
        "data": {
            "code": remote.pairing_code()
        },
    }