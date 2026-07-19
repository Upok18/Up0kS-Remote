"""
Up0k Remote
Session Manager
"""

from __future__ import annotations

from dataclasses import dataclass, field
from socket import socket
from time import time


@dataclass
class Session:
    """Represents one connected client."""

    # Network
    client: socket
    address: tuple[str, int]

    # Authentication
    authenticated: bool = False

    # Device Information
    uuid: str = ""
    device_name: str = "Unknown Device"
    model: str = "Unknown Model"
    platform: str = "Unknown"
    android_version: str = "Unknown"
    app_version: str = "0.0.0"
    uuid: str = ""
    trusted: bool = False

    # Session Information
    connected_at: float = field(default_factory=time)
    last_ping: float = field(default_factory=time)