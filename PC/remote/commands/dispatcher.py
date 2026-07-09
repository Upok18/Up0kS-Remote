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
from typing import Any, Callable


COMMANDS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "shutdown": shutdown,
    "restart": restart,
    "ping": ping,
    "info": info,
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

    action = packet.get("action")

    if not isinstance(action, str):
        return {
            "version": PROTOCOL_VERSION,
            "action": "error",
            "data": {"message": "Invalid action."},
        }

    command = COMMANDS.get(action)

    if command is None:
        return {
            "version": PROTOCOL_VERSION,
            "action": "error",
            "data": {"message": "Unknown command."},
        }

    return command(packet.get("data", {}))
