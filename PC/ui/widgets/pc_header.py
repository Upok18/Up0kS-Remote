"""
Up0k Remote
PC Header Widget
"""

from __future__ import annotations

import customtkinter as ctk

from remote.status import Status


class PcHeader(ctk.CTkFrame):

    def __init__(
        self,
        master,
        name: str,
        os_name: str,
        cpu: str,
        ip: str,
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=16,
            border_width=1,
            border_color=("gray75", "gray25"),
            **kwargs
        )

        self.name = name
        self.os_name = os_name
        self.cpu = cpu
        self.ip = ip

        self.build()

    def build(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.name_label = ctk.CTkLabel(
            self,
            text=f"🖥 {self.name}",
            font=("Segoe UI", 28, "bold")
        )

        self.name_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(22, 6)
        )

        self.info_label = ctk.CTkLabel(
            self,
            text=f"{self.os_name} • {self.cpu} • 🌐 {self.ip}",
            font=("Segoe UI", 13),
            text_color=("gray40", "gray70")
        )

        self.info_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(4, 22)
        )

        self.status_label = ctk.CTkLabel(
            self,
            text="● Waiting",
            font=("Segoe UI", 14, "bold"),
            text_color="#22c55e"
        )

        self.status_label.grid(
            row=0,
            column=1,
            padx=20,
            pady=(22, 6),
            sticky="e"
        )

        self.info_label.bind(
            "<Button-1>",
            self.copy_ip
        )

        self.info_label.configure(
            cursor="hand2"
        )

    def copy_ip(self, event=None):

        self.clipboard_clear()
        self.clipboard_append(self.ip)

        self.info_label.configure(
            text="✅ IP copied!"
        )

        self.after(
            1200,
            lambda: self.info_label.configure(
                text=f"{self.os_name} • {self.cpu} • 🌐 {self.ip}"
            )
        )

    def set_ip(self, ip: str):

        self.ip = ip

        self.info_label.configure(
            text=f"{self.os_name} • {self.cpu} • 🌐 {ip}"
        )

    def set_status(self, status: str):

        colors = {
            Status.WAITING: "#3b82f6",
            Status.PAIRING: "#f59e0b",
            Status.CONNECTED: "#22c55e",
            Status.DISCONNECTED: "#ef4444",
            Status.ERROR: "#ff0000",
        }

        names = {
            Status.WAITING: "Waiting",
            Status.PAIRING: "Pairing",
            Status.CONNECTED: "Connected",
            Status.DISCONNECTED: "Disconnected",
            Status.ERROR: "Error",
        }

        self.status_label.configure(
            text=f"● {names.get(status, status)}",
            text_color=colors.get(status, "#9ca3af")
        )
        
    