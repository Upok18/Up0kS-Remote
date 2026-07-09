"""
Up0k Remote
Discovery Manager
"""

from __future__ import annotations

import socket
import threading
import time
import json
from remote.constants import DISCOVERY_PORT, DISCOVERY_INTERVAL, DEFAULT_PORT
from remote.logger import info


class DiscoveryServer:
    """Broadcasts this PC on the local network."""

    def __init__(self) -> None:
        self.running = False
        self.thread: threading.Thread | None = None

    def start(self) -> None:
        """Start broadcasting."""

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.broadcast_loop,
            daemon=True,
        )

        self.thread.start()

        info("Discovery service started.")

    def stop(self) -> None:
        """Stop broadcasting."""

        self.running = False
        info("Discovery service stopped.")

    def broadcast_loop(self) -> None:
        """Discovery thread."""

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        packet = {"name": "Up0k-PC", "port": DEFAULT_PORT, "version": "0.1.0"}

        while self.running:
            message = json.dumps(packet).encode()

            sock.sendto(
                message,
                ("255.255.255.255", DISCOVERY_PORT),
            )

            time.sleep(DISCOVERY_INTERVAL)

        sock.close()
