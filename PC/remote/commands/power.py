"""
Shutdown Command
"""

from __future__ import annotations

import subprocess


def shutdown():

    subprocess.run(
        ["shutdown", "/s", "/f", "/t", "500"],
        check=False,
    )

def restart():

    subprocess.run(
        ["shutdown", "/r", "/f", "/t", "500"],
        check=False,
    )
