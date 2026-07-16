"""
Up0k Remote
Pairing Command
"""

from __future__ import annotations

from remote.devices import add_trusted_device
from remote.version import PROTOCOL_VERSION
from remote.pairing import verify_pair_code, get_pair_code, clear_pair_code

def execute(remote, data: dict) -> dict:

    code = data.get("code", "")
    device = data.get("device", "Unknown Device")

    print("===== PAIR REQUEST =====")
    print(data)
    print(f"Received code : {data.get('code')}")
    print(f"Expected code : {get_pair_code()}")
    print("========================")

    if not verify_pair_code(code):
        return {
            "version": PROTOCOL_VERSION,
            "type": "pair_failed",
            "data": {
                "reason": "Invalid or expired pairing code."
            },
        }

    add_trusted_device(device)
    clear_pair_code()

    return {
        "version": PROTOCOL_VERSION,
        "type": "pair_ok",
        "data": {},
    }