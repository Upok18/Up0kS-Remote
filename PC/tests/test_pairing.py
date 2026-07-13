"""
Up0k Remote
Pairing Test Client
"""

from __future__ import annotations

from pathlib import Path
import socket
import sys

# Allow imports from the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from remote.constants import BUFFER_SIZE, DEFAULT_HOST, DEFAULT_PORT
from remote.protocol import decode_packet, encode_packet


def main() -> None:

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    print("Connecting...")

    client.connect(
        ("127.0.0.1", DEFAULT_PORT)
    )

    print("Connected!")

    # Receive HELLO packet
    hello = decode_packet(
        client.recv(BUFFER_SIZE)
    )

    print("\nHELLO")
    print(hello)

    # Login
    password = input("\nPassword: ")

    login_packet = {
        "type": "login",
        "data": {
            "password": password
        }
    }

    client.send(
        encode_packet(login_packet)
    )

    response = decode_packet(
        client.recv(BUFFER_SIZE)
    )

    print("\nAUTH RESPONSE")
    print(response)

    if response["type"] != "auth_ok":
        print("\nAuthentication failed.")
        client.close()
        return

    # Pair
    code = input("\nPair Code: ")
    device = input("Device Name: ")

    pair_packet = {
        "type": "pair",
        "data": {
            "code": code,
            "device": device,
        },
    }

    client.send(
        encode_packet(pair_packet)
    )

    response = decode_packet(
        client.recv(BUFFER_SIZE)
    )

    print("\nPAIR RESPONSE")
    print(response)

    client.close()


if __name__ == "__main__":
    main()