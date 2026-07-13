"""
Up0k Remote
Remote Service
"""

from __future__ import annotations

from remote.server import RemoteServer
from remote.devices import (
    get_trusted_devices,
    add_trusted_device,
    remove_trusted_device,
)

from remote.pairing import (
    generate_pair_code,
    verify_pair_code,
    clear_pair_code,
)

from remote.system import (
    get_local_ip,
    get_computer_name,
)

class RemoteService:

    def __init__(self):

        self.server = RemoteServer()

        pass

    # ==================================================
    # System
    # ==================================================

    def computer_name(self):

        return get_computer_name()

    def ip_address(self):

        return get_local_ip()

    # ==================================================
    # Pairing
    # ==================================================

    def start_pairing(self):

        return generate_pair_code()

    def verify_pairing(self, code: str):

        return verify_pair_code(code)

    def stop_pairing(self):

        clear_pair_code()

    # ==================================================
    # Devices
    # ==================================================

    def devices(self):

        return get_trusted_devices()

    def trust_device(self, device: str):

        add_trusted_device(device)

    def remove_device(self, device: str):

        remove_trusted_device(device)

    # ==================================================
    # Server
    # ==================================================

    def start_server(self):

        self.server.start()


    def stop_server(self):

        self.server.stop()


    def restart_server(self):

        self.server.restart()


    def server_running(self):

        return self.server.is_running()