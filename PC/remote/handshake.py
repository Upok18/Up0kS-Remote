"""
Up0k Remote
Handshake Manager
"""

from __future__ import annotations

# from remote.pairing import generate_pair_code
from remote.version import NAME, VERSION, PROTOCOL_VERSION


def create_hello(pairing_required: bool):

    # if pairing_required:
    #     code = generate_pair_code()

    #     print()
    #     print("========== PAIR CODE ==========")
    #     print(code)
    #     print("===============================")
    #     print()

    return {
        "type": "hello",
        "data": {
            "app": NAME,
            "version": VERSION,
            "protocol": PROTOCOL_VERSION,
            "authentication": False,
            "pairing": pairing_required,
        },
    }