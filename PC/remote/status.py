"""
Up0k Remote
Status Manager
"""

from __future__ import annotations


class Status:

    WAITING = "🔵 Waiting"

    PAIRING = "🟡 Pairing"

    AUTHENTICATING = "🔐 Authenticating..."

    CONNECTED = "🟢 Connected"

    DISCONNECTED = "🔴 Offline"

    ERROR = "❌ Connection error"