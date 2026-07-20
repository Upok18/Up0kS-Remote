"""
Up0k Remote
Devices Page
"""

from __future__ import annotations

import customtkinter as ctk

from ui.widgets.device_card import DeviceCard
from ui.dialogs.remove_device import RemoveDeviceDialog


class DevicesPage(ctk.CTkFrame):

    def __init__(
        self,
        master,
        remote,
        **kwargs
    ):

        super().__init__(master, **kwargs)

        self.remote = remote

        ctk.CTkLabel(
            self,
            text="📱 Devices",
            font=("Segoe UI", 26, "bold")
        ).pack(
            pady=(20, 10)
        )

        self.device_container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.device_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.load_devices()

    def load_devices(self):

        for widget in self.device_container.winfo_children():
            widget.destroy()

        devices = self.remote.devices()

        if not devices:

            ctk.CTkLabel(
                self.device_container,
                text="No trusted devices.",
                font=("Segoe UI", 16)
            ).pack(pady=20)

            return

        for device in devices:

            card = DeviceCard(
                self.device_container,
                name=device["name"],
                device_id=device["id"],
                remove_callback=self.confirm_remove
            )

            card.pack(
                fill="x",
                pady=8
            )

    def confirm_remove(self, device_id):

        device_name = ""

        for device in self.remote.devices():
            if device["id"] == device_id:
                device_name = device["name"]
                break

        RemoveDeviceDialog(
            self,
            device_name=device_name,
            callback=lambda: self.remove_device(device_id)
        )

    def remove_device(self, device_id):

        print("Removing:", device_id)

        self.remote.remove_device(device_id)

        self.load_devices()