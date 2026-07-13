"""
Up0k Remote
Remote Server
"""

from __future__ import annotations

import threading

from remote.banner import show
from remote.config import load_config
from remote.discovery import DiscoveryServer
from remote.logger import info
from remote.network import NetworkServer


class RemoteServer:

    def __init__(self):

        self.running = False

        self.discovery = DiscoveryServer()
        self.network = NetworkServer()

    # ==================================================
    # Server
    # ==================================================

    def start(self) -> None:

        if self.running:
            return

        config = load_config()

        show()

        info("Starting Up0k Remote...")
        info(
            f"Listening on "
            f"{config['server']['host']}:"
            f"{config['server']['port']}"
        )

        self.discovery.start()

        threading.Thread(
            target=self.network.start,
            daemon=True,
        ).start()

        self.running = True

    def stop(self) -> None:

        if not self.running:
            return

        self.discovery.stop()
        self.network.stop()

        self.running = False

    def restart(self) -> None:

        self.stop()
        self.start()

    def is_running(self) -> bool:

        return self.running