"""
Up0k Remote
Pairing Manager
"""

from __future__ import annotations

import json
import random

from pathlib import Path

PAIR_FILE = Path(__file__).parent.parent / "storage" / "paired_devices.json"


PAIR_CODE: str | None = None

def load_devices() -> dict:

    if not PAIR_FILE.exists():
        return {"devices": []}

    try:
        with PAIR_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except Exception:
        return {"devices": []}


def save_devices(data: dict) -> None:

    PAIR_FILE.parent.mkdir(parents=True, exist_ok=True)

    with PAIR_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


PAIR_CODE: str | None = None


def generate_pair_code() -> str:
    global PAIR_CODE

    PAIR_CODE = f"{random.randint(0, 999999):06d}"

    return PAIR_CODE


def get_pair_code() -> str | None:
    return PAIR_CODE


def verify_pair_code(code: str) -> bool:
    return code == PAIR_CODE


def clear_pair_code() -> None:
    global PAIR_CODE
    PAIR_CODE = None