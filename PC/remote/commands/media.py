"""
Up0k Remote
Media Commands
"""

from __future__ import annotations

import ctypes
import comtypes

from typing import Any
from pycaw.pycaw import AudioUtilities
from remote.version import PROTOCOL_VERSION


VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1

KEYEVENTF_KEYUP = 0x0002


def _volume():
    """Return the Windows master volume interface."""

    comtypes.CoInitialize()

    speakers = AudioUtilities.GetSpeakers()

    return speakers.EndpointVolume


def _press_key(key: int) -> None:
    """Press and release a multimedia key."""

    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    ctypes.windll.user32.keybd_event(
        key,
        0,
        KEYEVENTF_KEYUP,
        0,
    )


def mute(data: dict[str, Any]) -> dict[str, Any]:
    """Toggle mute."""

    volume = _volume()

    muted = bool(volume.GetMute())

    volume.SetMute(not muted, None)

    return {
        "version": PROTOCOL_VERSION,
        "type": "mute",
        "data": {
            "muted": not muted,
        },
    }


def unmute(data: dict[str, Any]) -> dict[str, Any]:
    """Unmute system audio."""

    volume = _volume()

    volume.SetMute(False, None)

    return {
        "version": PROTOCOL_VERSION,
        "type": "unmute",
        "data": {
            "muted": False,
        },
    }


def toggle_mute(data: dict[str, Any]) -> dict[str, Any]:
    """Toggle mute state."""

    volume = _volume()

    muted = bool(volume.GetMute())

    volume.SetMute(not muted, None)

    return {
        "version": PROTOCOL_VERSION,
        "type": "toggle_mute",
        "data": {
            "muted": not muted,
        },
    }


def volume_up(data: dict[str, Any]) -> dict[str, Any]:
    """Increase master volume by 10%."""

    volume = _volume()

    current = volume.GetMasterVolumeLevelScalar()
    current = min(1.0, current + 0.10)

    volume.SetMasterVolumeLevelScalar(current, None)

    return {
        "version": PROTOCOL_VERSION,
        "type": "volume_up",
        "data": {
            "volume": round(current * 100),
        },
    }


def volume_down(data: dict[str, Any]) -> dict[str, Any]:
    """Decrease master volume by 10%."""

    volume = _volume()

    current = volume.GetMasterVolumeLevelScalar()
    current = max(0.0, current - 0.10)

    volume.SetMasterVolumeLevelScalar(current, None)

    return {
        "version": PROTOCOL_VERSION,
        "type": "volume_down",
        "data": {
            "volume": round(current * 100),
        },
    }


def play_pause(data: dict[str, Any]) -> dict[str, Any]:
    """Toggle play/pause."""

    _press_key(VK_MEDIA_PLAY_PAUSE)

    return {
        "version": PROTOCOL_VERSION,
        "type": "play_pause",
        "data": {},
    }


def next_track(data: dict[str, Any]) -> dict[str, Any]:
    """Skip to the next track."""

    _press_key(VK_MEDIA_NEXT_TRACK)

    return {
        "version": PROTOCOL_VERSION,
        "type": "next_track",
        "data": {},
    }


def previous_track(data: dict[str, Any]) -> dict[str, Any]:
    """Go to the previous track."""

    _press_key(VK_MEDIA_PREV_TRACK)

    return {
        "version": PROTOCOL_VERSION,
        "type": "previous_track",
        "data": {},
    }
