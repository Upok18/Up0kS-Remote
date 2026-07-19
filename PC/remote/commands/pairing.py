"""
Up0k Remote
Pairing Command
"""

from __future__ import annotations

from remote.version import PROTOCOL_VERSION
from remote.pairing import verify_pair_code, get_pair_code, clear_pair_code
from remote.status import Status

def execute(remote, data: dict) -> dict:

    code = data.get("code", "")
    device = data.get("device", "Unknown Device")
    device_id = data.get("id", "")

    # print("===== PAIR REQUEST =====")
    # print(data)
    # print(f"Received code : {data.get('code')}")
    # print(f"Expected code : {get_pair_code()}")
    # print("========================")

    if not verify_pair_code(code):
        return {
            "version": PROTOCOL_VERSION,
            "type": "pair_failed",
            "data": {
                "reason": "Invalid or expired pairing code."
            },
        }

    remote.trust_device(
        device_name=device,
        device_id=device_id,
    )

    remote.stop_pairing()
    remote.set_status(Status.CONNECTED)

    return {
        "version": PROTOCOL_VERSION,
        "type": "pair_ok",
        "data": {},
    }