"""
Up0k Remote
PC Header Widget
"""

from __future__ import annotations

import customtkinter as ctk


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
            corner_radius=12,
            border_width=1,
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
            font=("Segoe UI", 24, "bold")
        )

        self.name_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(18, 4)
        )

        self.status_label = ctk.CTkLabel(
            self,
            text="🟡 Waiting",
            font=("Segoe UI", 14, "bold")
        )

        self.status_label.grid(
            row=0,
            column=1,
            sticky="e",
            padx=20,
            pady=(18, 4)
        )

        self.os_label = ctk.CTkLabel(
            self,
            text=self.os_name,
            font=("Segoe UI", 14)
        )

        self.os_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=20
        )

        self.cpu_label = ctk.CTkLabel(
            self,
            text=self.cpu,
            font=("Segoe UI", 14)
        )

        self.cpu_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=20,
            pady=(2, 0)
        )

        self.ip_label = ctk.CTkLabel(
            self,
            text=f"🌐 {self.ip}",
            font=("Segoe UI", 14)
        )

        self.ip_label.grid(
            row=3,
            column=0,
            sticky="w",
            padx=20,
            pady=(8, 18)
        )

    def set_ip(self, ip: str):

        self.ip = ip

        self.ip_label.configure(
            text=f"🌐 {ip}"
        )

    def set_status(self, status: str):

        self.status_label.configure(
            text=status
        )