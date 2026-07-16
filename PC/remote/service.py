"""
Up0k Remote
Remote Service
"""

from __future__ import annotations

import time

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

        self.pairing = False
        self.pair_code = "------"
        self.pair_expires = 0

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

        self.pair_code = generate_pair_code()
        self.pairing = True
        self.pair_expires = time.time() + 60

        return self.pair_code

    def verify_pairing(self, code: str):

        return verify_pair_code(code)

    def stop_pairing(self):

        clear_pair_code()

        self.pairing = False
        self.pair_code = "------"
        self.pair_expires = 0

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
    
    def pairing_active(self):

        return self.pairing


    def pairing_code(self):

        return self.pair_code
    
    def pairing_time_left(self):

        if not self.pairing:
            return 0

        return max(
            0,
            int(self.pair_expires - time.time())
        )


    def pairing_expired(self):

        return self.pairing_time_left() <= 0