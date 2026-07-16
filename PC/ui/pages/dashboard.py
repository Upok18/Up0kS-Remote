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

        self.grid_columnconfigure(0, weight=1)

        self.create_pc_header()
        
        self.create_pair_section()

        self.update_status(Status.WAITING)

        if self.remote.pairing_active():

            self.show_pair_code(
                self.remote.pairing_code()
            )

            self.update_status(
                Status.PAIRING
            )

            self.pair_button.configure(
                text="⏳ Pairing..."
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

        self.pair_button = ctk.CTkButton(
            self.pair_frame,
            text="🔗 Pair",
            width=120,
            command=self.start_pairing
        )

        self.pair_button.grid(
            row=0,
            column=1,
            padx=(10, 0)
        )

    def show_pair_code(self, code: str):

        self.pair_card.set_value(code)


    def clear_pair_code(self):

        self.pair_card.set_value("------")

    def start_pairing(self):

        if self.remote.pairing_active():
            return

        code = self.remote.start_pairing()

        self.show_pair_code(code)

        self.update_status(
            Status.PAIRING
        )

        self.update_pair_timer()

    def update_pair_timer(self):

        if not self.remote.pairing_active():
            return

        remaining = self.remote.pairing_time_left()

        if remaining <= 0:

            self.remote.stop_pairing()

            self.clear_pair_code()

            self.update_status(
                Status.WAITING
            )

            self.pair_button.configure(
                text="🔗 Pair"
            )

            return

        self.pair_button.configure(
            text=f"⏳ {remaining}s"
        )

        self.after(
            1000,
            self.update_pair_timer
        )

    