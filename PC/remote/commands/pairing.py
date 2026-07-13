"""
Up0k Remote
Pairing Command
"""

from __future__ import annotations

from remote.devices import add_trusted_device
from remote.pairing import verify_pair_code
from remote.version import PROTOCOL_VERSION


def execute(data: dict) -> dict:

    code = data.get("code", "")
    device = data.get("device", "Unknown Device")

    if not verify_pair_code(code):
        return {
            "version": PROTOCOL_VERSION,
            "type": "pair_failed",
            "data": {
                "reason": "Invalid or expired pairing code."
            },
        }

    add_trusted_device(device)

    return {
        "version": PROTOCOL_VERSION,
        "type": "pair_ok",
        "data": {},
    }