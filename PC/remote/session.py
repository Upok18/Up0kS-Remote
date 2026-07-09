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
    device_name: str = "Unknown Device"
    platform: str = "Unknown"
    app_version: str = "0.0.0"

    # Session Information
    connected_at: float = field(default_factory=time)
    last_ping: float = field(default_factory=time)
