"""
Command Dispatcher
"""

from __future__ import annotations

from remote.version import PROTOCOL_VERSION
from remote.commands.power import shutdown, restart
from remote.commands.system import ping
from remote.commands.info import execute as info
from remote.commands.media import (
    toggle_mute,
    volume_up,
    volume_down,
    play_pause,
    next_track,
    previous_track,
)
from remote.commands.pairing import execute as pair
from typing import Any, Callable


COMMANDS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "shutdown": shutdown,
    "restart": restart,
    "ping": ping,
    "info": info,

    "pair": pair,
    
    # "mute": mute,
    # "unmute": unmute,
    "toggle_mute": toggle_mute,
    "volume_up": volume_up,
    "volume_down": volume_down,
    "play_pause": play_pause,
    "next_track": next_track,
    "previous_track": previous_track,
}


def dispatch(packet: dict[str, Any]) -> dict[str, Any]:
    """Dispatch an incoming command."""

    packet_type = packet.get("type")

    if not isinstance(packet_type, str):
        return {
            "version": PROTOCOL_VERSION,
            "type": "error",
            "data": {
                "message": "Invalid action."
                },
        }

    command = COMMANDS.get(packet_type)

    if command is None:
        return {
            "version": PROTOCOL_VERSION,
            "type": "error",
            "data": {
                "message": "Unknown packet command."
                },
        }

    return command(packet.get("data", {}))
