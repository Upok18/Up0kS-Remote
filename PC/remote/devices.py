"""
Up0k Remote
Trusted Device Manager
"""

from __future__ import annotations

from remote.config import (
    get_config,
    set_config,
)


def get_trusted_devices() -> list:

    return get_config("security.trusted_devices")


def add_trusted_device(device: str):

    devices = get_trusted_devices()

    if device not in devices:

        devices.append(device)

        set_config(
            "security.trusted_devices",
            devices
        )


def remove_trusted_device(device: str):

    devices = get_trusted_devices()

    if device in devices:

        devices.remove(device)

        set_config(
            "security.trusted_devices",
            devices
        )


def is_trusted(device: str) -> bool:

    return device in get_trusted_devices()