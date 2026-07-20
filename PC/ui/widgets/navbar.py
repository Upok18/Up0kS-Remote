"""
Up0k Remote
Navigation Bar
"""

from __future__ import annotations

import customtkinter as ctk


class Navbar(ctk.CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            height=55,
            corner_radius=0,
            **kwargs
        )

        self.pack_propagate(False)

        self.callback = None

        self.build()

    def build(self):

        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.dashboard_btn = ctk.CTkButton(
            self,
            text="🏠 Dashboard",
            fg_color="transparent",
            hover_color="#7b3dff",
            command=lambda: self.select("dashboard")
        )

        self.dashboard_btn.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.devices_btn = ctk.CTkButton(
            self,
            text="📱 Devices",
            fg_color="transparent",
            hover_color="#7b3dff",
            command=lambda: self.select("devices")
        )

        self.devices_btn.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.settings_btn = ctk.CTkButton(
            self,
            text="⚙ Settings",
            fg_color="transparent",
            hover_color="#7b3dff",
            command=lambda: self.select("settings")
        )

        self.settings_btn.grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.select("dashboard")

    def set_callback(self, callback):

        self.callback = callback

    def select(self, page):

        buttons = {
            "dashboard": self.dashboard_btn,
            "devices": self.devices_btn,
            "settings": self.settings_btn,
        }

        for btn in buttons.values():
            btn.configure(fg_color="transparent")

        buttons[page].configure(
            fg_color=("#7b3dff", "#84c200")
        )

        if self.callback:
            self.callback(page)