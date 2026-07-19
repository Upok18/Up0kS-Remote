"""
Up0k Remote
Dashboard Page
"""

from __future__ import annotations

import customtkinter as ctk

from remote.system import (
    get_os_name,
    get_cpu_name,
)

from remote.status import Status
from ui.widgets.pc_header import PcHeader
from ui.widgets.section import Section
from ui.widgets.info_card import InfoCard


class DashboardPage(ctk.CTkFrame):

    def __init__(
        self,
        master,
        remote,
        **kwargs
    ):

        super().__init__(master, **kwargs)

        self.remote = remote

        self.remote.on_status_changed = self.update_status
        self.remote.on_pairing_changed = self.on_pairing_changed

        self.grid_columnconfigure(0, weight=1)

        self.create_pc_header()
        self.create_pair_section()

        self.update_status(self.remote.status)

        if self.remote.pairing_active():

            self.show_pair_code(
                self.remote.pairing_code()
            )

            self.remote.set_status(
                Status.PAIRING
            )

            self.update_pair_timer()

        self.pair_seconds = 0

    def create_pc_header(self):

        self.pc_header = PcHeader(
            self,
            name=self.remote.computer_name(),
            os_name=get_os_name(),
            cpu=get_cpu_name(),
            ip=self.remote.ip_address()
        )

        self.pc_header.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

    def update_status(self, status: str):

        self.pc_header.set_status(status)

    def create_pair_section(self):

        self.pair_section = Section(
            self,
            title="Pair Your Phone"
        )

        self.pair_section.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.pair_frame = ctk.CTkFrame(
            self.pair_section.content,
            fg_color="transparent"
        )

        self.pair_frame.pack(
            fill="x",
            pady=5
        )

        self.pair_frame.grid_columnconfigure(0, weight=1)

        self.pair_card = InfoCard(
            self.pair_frame,
            title="Pairing Code",
            value="------",
            value_font=("Consolas", 30, "bold")
        )

        self.pair_card.grid(
            row=0,
            column=0,
            sticky="ew"
        )

    def show_pair_code(self, code: str):

        self.pair_card.set_value(code)


    def clear_pair_code(self):

        self.pair_card.set_value("------")

    def update_pair_timer(self):

        if not self.remote.pairing_active():
            return

        remaining = self.remote.pairing_time_left()

        if remaining <= 0:

            self.remote.stop_pairing()

            self.clear_pair_code()

            return

        self.after(
            1000,
            self.update_pair_timer
        )

    def on_pairing_changed(
        self,
        code: str,
        expires: float
    ):

        if code == "------":
            self.clear_pair_code()
            return

        self.show_pair_code(code)

        self.update_pair_timer()