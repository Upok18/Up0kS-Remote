"""
Up0k Remote
System Information
"""

from __future__ import annotations

import platform
import socket
import pyperclip
import platform


def get_computer_name() -> str:
    """Return the current computer name."""

    return platform.node()

def get_os_name() -> str:
    """Return the OS"""

    return f"{platform.system()} {platform.release()}"

def get_cpu_name() -> str:
    """Return the CPU model."""

    return platform.processor()

def get_local_ip() -> str:
    """Return the local IPv4 address."""

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

            s.connect(("8.8.8.8", 80))

            return s.getsockname()[0]

    except OSError:

        return "127.0.0.1"
    
def copy_ip_address() -> None:
    """Copy the local IP address."""

    pyperclip.copy(
        get_local_ip()
    )


