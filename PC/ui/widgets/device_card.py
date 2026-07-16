"""
Trusted Device Card
"""

from __future__ import annotations

import customtkinter as ctk


class DeviceCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        name: str,
        status: str = "Trusted",
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=12,
            border_width=1,
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)

        self.name_label = ctk.CTkLabel(
            self,
            text=f"📱 {name}",
            font=("Segoe UI", 16, "bold"),
            anchor="w"
        )

        self.name_label.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=15,
            pady=(12, 2)
        )

        self.status_label = ctk.CTkLabel(
            self,
            text=f"🟢 {status}",
            font=("Segoe UI", 12),
            width=150,
            anchor="center"
        )

        self.status_label.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 12)
        )