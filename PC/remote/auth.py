"""
Up0k Remote
Authentication Manager
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from remote.version import PROTOCOL_VERSION
from typing import Any

import bcrypt

PASSWORD_PATH = Path(__file__).parent.parent / "storage" / "password.json"


def _load_password_data() -> dict:
    """Load password data safely."""

    if not PASSWORD_PATH.exists():
        return {}

    try:
        with PASSWORD_PATH.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def _save_password_data(data: dict) -> None:
    """Save password data."""

    PASSWORD_PATH.parent.mkdir(parents=True, exist_ok=True)

    with PASSWORD_PATH.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def password_exists() -> bool:
    """Return True if a password has been created."""

    data = _load_password_data()
    return "password" in data


def setup_password(password: str) -> None:
    """Create the initial password."""

    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    data = {
        "version": PROTOCOL_VERSION,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "password": password_hash,
    }

    _save_password_data(data)


def verify_password(password: str) -> bool:
    """Verify the password."""

    data = _load_password_data()

    if "password" not in data:
        return False

    return bcrypt.checkpw(
        password.encode(),
        data["password"].encode(),
    )


def change_password(old_password: str, new_password: str) -> bool:
    """Change the current password."""

    if not verify_password(old_password):
        return False

    setup_password(new_password)
    return True


def delete_password() -> None:
    """Delete the password (development only)."""

    _save_password_data({})


def get_password_info() -> dict:
    """Return password metadata."""

    data = _load_password_data()

    return {
        "exists": "password" in data,
        "created_at": data.get("created_at"),
        "version": data.get("version"),
    }


"""
Up0k Remote
Authentication
"""


def authenticate(packet: dict[str, Any]) -> dict[str, Any]:
    """Authenticate a client."""

    if packet.get("type") != "login":
        return {
            "version": PROTOCOL_VERSION,
            "type": "auth_failed",
            "data": {
                "reason": "Invalid packet."
            },
        }

    password = packet.get("data", {}).get("password", "")

    if verify_password(password):
        return {
            "version": PROTOCOL_VERSION,
            "type": "auth_ok",
            "data": {},
        }

    return {
        "version": PROTOCOL_VERSION,
        "type": "auth_failed",
        "data": {
            "reason": "Wrong password."
        },
    }