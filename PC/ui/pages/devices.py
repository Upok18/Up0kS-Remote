"""
Up0k Remote
Devices Page
"""

from __future__ import annotations

import customtkinter as ctk


class DevicesPage(ctk.CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)

        ctk.CTkLabel(
            self,
            text="📱 Devices",
            font=("Segoe UI", 26, "bold")
        ).pack(
            pady=30
        )