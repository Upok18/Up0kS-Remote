"""
Up0k Remote
Discovery Manager
"""

from __future__ import annotations

import socket
import threading
import json
from remote.constants import DISCOVERY_PORT, DEFAULT_PORT
from remote.logger import info, error
from remote.version import VERSION


class DiscoveryServer:
    """Responds to LAN discovery requests."""

    def __init__(self) -> None:
        self.running = False
        self.thread: threading.Thread | None = None

    def start(self) -> None:
        """Start broadcasting."""

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.listen,
            daemon=True,
        )

        self.thread.start()

        # info("Discovery service started.")

    def stop(self) -> None:
        """Stop broadcasting."""

        self.running = False
        info("Discovery service stopped.")

    def listen(self) -> None:
        """Listen for discovery requests."""

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1,
        )

        sock.bind(("", DISCOVERY_PORT))

        while self.running:

            data, address = sock.recvfrom(1024)

            try:
                message = data.decode()

                if message != "WHO_IS_UP0K_REMOTE":
                    continue

                packet = {
                    "name": socket.gethostname(),
                    "port": DEFAULT_PORT,
                    "version": VERSION,
                }

                sock.sendto(
                    json.dumps(packet).encode(),
                    address,
                )

            except Exception as e:
                print(f"Discovery error: {e}")
                # continue
                

        sock.close()
