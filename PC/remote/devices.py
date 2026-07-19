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


def add_trusted_device(
    device_name: str,
    device_id: str
):

    devices = get_trusted_devices()

    for device in devices:

        if device["id"] == device_id:
            return

    devices.append(
        {
            "name": device_name,
            "id": device_id,
        }
    )

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


def is_trusted(device_id: str) -> bool:

    devices = get_trusted_devices()

    return any(
        device["id"] == device_id
        for device in devices
    )

def has_trusted_devices() -> bool:
    """Return True if at least one trusted device exists."""

    return len(get_trusted_devices()) > 0