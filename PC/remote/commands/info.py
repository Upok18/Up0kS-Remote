"""
Up0k Remote
Info Command
"""

from __future__ import annotations

import platform
import socket
import getpass
import psutil
import time
from remote.version import PROTOCOL_VERSION


def execute(remote, data: dict) -> dict:
    """Return information about this PC."""

    vm = psutil.virtual_memory()

    uptime = int(time.time() - psutil.boot_time())

    return {
        "version": PROTOCOL_VERSION,
        "type": "info",
        "data": {
            "device_name": socket.gethostname(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "ram_total": round(vm.total / (1024 ** 3), 1),
            "ram_used": round(vm.used / (1024 ** 3), 1),
            "ram_percent": vm.percent,
        },
    }
