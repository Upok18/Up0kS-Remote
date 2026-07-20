"""
Up0k Remote
Remote Service
"""

from __future__ import annotations

import time

from remote.server import RemoteServer
from remote.status import Status
from remote.devices import (
    get_trusted_devices,
    add_trusted_device,
    remove_trusted_device,
    is_trusted,
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

        self.server = RemoteServer(self)

        self.pairing = False
        self.pair_code = "------"
        self.pair_expires = 0

        self.status = Status.WAITING

        self.on_status_changed = None
        self.on_devices_changed = None
        self.on_pairing_changed = None

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

        self.set_status(Status.PAIRING)

        return self.pair_code

    def verify_pairing(self, code: str):

        return verify_pair_code(code)

    def stop_pairing(self):

        clear_pair_code()

        if self.on_pairing_changed:
            self.on_pairing_changed(
                "------",
                0
            )

        self.pairing = False
        self.pair_code = "------"
        self.pair_expires = 0

        self.set_status(Status.WAITING)

    # ==================================================
    # Devices
    # ==================================================

    def devices(self):

        return get_trusted_devices()

    def trust_device(
        self,
        device_name: str,
        device_id: str,
    ):

        add_trusted_device(
            device_name,
            device_id,
        )

    def is_trusted(self, device_id: str) -> bool:

        return is_trusted(device_id)

    def remove_device(self, device: str):

        print("Service removing:", device)

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
    
    def set_status(self, status):

        self.status = status

        if self.on_status_changed:
            self.on_status_changed(status)

    def request_pairing(self):

        if self.pairing_active():
            return

        self.start_pairing()

        if self.on_pairing_changed:
            self.on_pairing_changed(
                self.pair_code,
                self.pair_expires
            )