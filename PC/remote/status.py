"""
Up0k Remote
Status Manager
"""

from __future__ import annotations


class Status:

    WAITING = "🟢 Waiting for connection"

    PAIRING = "🟡 Pairing device"

    AUTHENTICATING = "🔐 Authenticating..."

    CONNECTED = "🟢 Phone connected"

    DISCONNECTED = "🔴 Disconnected"

    ERROR = "❌ Connection error"