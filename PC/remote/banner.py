"""
Up0k Remote
Banner
"""

from __future__ import annotations

from remote.version import NAME, VERSION


def show() -> None:
    print("=" * 46)
    print(f"{NAME:^46}")
    print(f"{'v' + VERSION:^46}")
    print("=" * 46)
    print()
