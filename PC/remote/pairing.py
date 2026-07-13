"""
Up0k Remote
Pairing Manager
"""

from __future__ import annotations

import secrets
import time


_current_code = None
_created_at = None

PAIR_TIMEOUT = 60


def generate_pair_code() -> str:

    global _current_code
    global _created_at

    _current_code = f"{secrets.randbelow(1000000):06}"
    _created_at = time.time()

    return _current_code


def get_pair_code():

    return _current_code


def verify_pair_code(code: str) -> bool:

    if expired():
        return False

    return code == _current_code


def clear_pair_code():

    global _current_code
    global _created_at

    _current_code = None
    _created_at = None


def expired() -> bool:

    if _created_at is None:
        return True

    return time.time() - _created_at > PAIR_TIMEOUT