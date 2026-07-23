"""
Up0k Remote
Configuration Manager
"""

from __future__ import annotations

import json
from copy import deepcopy
from typing import Any

from remote.constants import (
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_THEME,
    LOCKOUT_MINUTES,
    MAX_CONNECTIONS,
)

from remote.version import VERSION

from remote.paths import CONFIG_PATH, ensure_storage

DEFAULT_CONFIG = {
    "version": VERSION,

    "server": {
        "host": DEFAULT_HOST,
        "port": DEFAULT_PORT,
        "max_connections": MAX_CONNECTIONS,
        "lan_discovery": True,
    },

    "ui": {
        "theme": DEFAULT_THEME,
        "show_timestamps": True,
        "enable_keybinds": True,
        "animations": True,
    },

    "startup": {
        "start_with_windows": False,
        "minimize_to_tray": False,
    },

    "security": {
        "trusted_devices": []
    },
}

def _merge(default: dict, current: dict) -> dict:
    """Merge missing values from the default configuration."""

    for key, value in default.items():
        if key not in current:
            current[key] = deepcopy(value)
        elif isinstance(value, dict) and isinstance(current[key], dict):
            _merge(value, current[key])

    return current


def load_config() -> dict:
    """Load the configuration from disk."""

    ensure_storage()

    if not CONFIG_PATH.exists():
        save_config(deepcopy(DEFAULT_CONFIG))
        return deepcopy(DEFAULT_CONFIG)

    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        config = json.load(file)

    config = _merge(DEFAULT_CONFIG, config)
    config["version"] = VERSION
    save_config(config)

    return config


def save_config(config: dict) -> None:
    """Save the configuration."""

    ensure_storage()

    with CONFIG_PATH.open("w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def get_config(path: str) -> Any:
    """Get a configuration value using dot notation."""

    config = load_config()

    value = config

    for key in path.split("."):
        value = value[key]

    return value


def set_config(path: str, new_value: Any) -> None:
    """Set a configuration value using dot notation."""

    config = load_config()

    value = config
    keys = path.split(".")

    for key in keys[:-1]:
        value = value[key]

    value[keys[-1]] = new_value

    save_config(config)
