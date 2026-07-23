"""
Up0k Remote
Paths
"""

from pathlib import Path
import os

APP_NAME = "Up0k Remote"

APPDATA_DIR = Path(os.environ["APPDATA"]) / APP_NAME

STORAGE_DIR = APPDATA_DIR / "storage"

CONFIG_PATH = STORAGE_DIR / "settings.json"


def ensure_storage() -> None:

    STORAGE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )