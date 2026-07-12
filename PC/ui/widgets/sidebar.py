"""
Up0k Remote
Sidebar Widget
"""

from __future__ import annotations

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=15
        )

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Up0k Remote",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(
            pady=(30, 10)
        )

        version = ctk.CTkLabel(
            self,
            text="v0.1.0-alpha.1"
        )

        version.pack(
            pady=(0, 25)
        )

        self.dashboard_btn = ctk.CTkButton(
            self,
            text="🏠 Dashboard"
        )

        self.dashboard_btn.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.devices_btn = ctk.CTkButton(
            self,
            text="📱 Devices"
        )

        self.devices_btn.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.settings_btn = ctk.CTkButton(
            self,
            text="⚙ Settings"
        )

        self.settings_btn.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.about_btn = ctk.CTkButton(
            self,
            text="ℹ About"
        )

        self.about_btn.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.status = ctk.CTkLabel(
            self,
            text="🟢 Waiting for connection..."
        )

        self.status.pack(
            side="bottom",
            pady=25
        )