import json
import socket

from remote.constants import DISCOVERY_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("", DISCOVERY_PORT))

print(f"Listening on UDP port {DISCOVERY_PORT}...")

while True:
    data, address = sock.recvfrom(4096)

    packet = json.loads(data.decode())

    print(f"\nReceived from {address}")
    print(packet)
