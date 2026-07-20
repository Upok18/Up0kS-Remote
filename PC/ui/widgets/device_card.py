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
        device_id: str,
        status: str = "Trusted",
        remove_callback=None,
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=12,
            border_width=1,
            **kwargs
        )

        self.device_id = device_id
        self.remove_callback = remove_callback

        self.grid_columnconfigure(0, weight=1)

        self.name_label = ctk.CTkLabel(
            self,
            text=f"📱 {name}",
            font=("Segoe UI", 20, "bold"),
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
            text_color="#00FF5E",
            anchor="w"
        )

        self.status_label.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 2)
        )

        self.id_label = ctk.CTkLabel(
            self,
            text=f"ID: {device_id[:8]}...{device_id[-4:]}",
            font=("Segoe UI", 11),
            anchor="w"
        )

        self.id_label.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 12)
        )

        self.remove_button = ctk.CTkButton(
            self,
            text="Remove",
            fg_color="#dc2626",
            hover_color="#ff0101",
            text_color="white",
            width=90,
            command=self.on_remove
        )

        self.remove_button.grid(
            row=0,
            column=1,
            rowspan=3,
            padx=15,
            pady=15
        )

    def on_remove(self):

        if self.remove_callback:
            self.remove_callback(self.device_id)