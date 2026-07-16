"""
Up0k Remote
Settings Page
"""

from __future__ import annotations

import customtkinter as ctk


class SettingsPage(ctk.CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)

        ctk.CTkLabel(
            self,
            text="⚙ Settings",
            font=("Segoe UI", 26, "bold")
        ).pack(
            pady=30
        )