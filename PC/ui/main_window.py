import customtkinter as ctk

from remote.system import (
    copy_ip_address,
    get_computer_name,
    get_local_ip,
)

from ui.widgets.info_card import InfoCard
from ui.widgets.section import Section
from ui.widgets.sidebar import Sidebar
from ui.utils.window import center_window
from remote.devices import get_trusted_devices
from remote.status import Status
from remote.service import RemoteService
from remote.pairing import (
    generate_pair_code,
    clear_pair_code
)


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.remote = RemoteService()

        self.title("Up0k Remote")

        center_window(self, 1080, 700)

        self.minsize(1000, 650)

        self.create_layout()

        self.create_content()

        self.remote.start_server()

    # ==================================================
    # Layout
    # ==================================================

    def create_layout(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=20
        )

        self.content = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=20
        )

        self.content.grid_columnconfigure(0, weight=1)

    # ==================================================
    # Content
    # ==================================================

    def create_content(self):

        self.create_computer_section()

        self.create_devices_section()

        self.create_actions_section()

    # ==================================================
    # Computer Information
    # ==================================================

    def create_computer_section(self):

        self.computer_section = Section(
            self.content,
            title="Computer Information"
        )

        self.computer_section.pack(
            fill="x",
            padx=20,
            pady=(12, 8)
        )

        self.computer_name_card = InfoCard(
            self.computer_section.content,
            "Computer Name",
            self.remote.computer_name()
        )

        self.computer_name_card.pack(
            fill="x",
            pady=5
        )

        self.ip_card = InfoCard(
            self.computer_section.content,
            "IP Address",
            self.remote.ip_address()
        )

        self.ip_card.pack(
            fill="x",
            pady=5
        )

        self.status_card = InfoCard(
            self.computer_section.content,
            "Status",
            Status.WAITING
        )

        self.status_card.pack(
            fill="x",
            pady=5
        )

        self.pair_code_card = InfoCard(
            self.computer_section.content,
            "Pairing Code",
            "------"
        )

        self.pair_code_card.pack(
            fill="x",
            pady=5
        )

    # ==================================================
    # Trusted Devices
    # ==================================================

    def create_devices_section(self):

        self.devices_section = Section(
            self.content,
            title="Trusted Devices"
        )

        self.devices_section.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        devices = get_trusted_devices()

        if devices:

            value = "\n".join(devices)

        else:

            value = "No trusted devices"

        self.devices_card = InfoCard(
            self.devices_section.content,
            "Devices",
            value
        )

        self.devices_card.pack(
            fill="x",
            pady=5
        )

    # ==================================================
    # Quick Actions
    # ==================================================

    def create_actions_section(self):

        self.actions_section = Section(
            self.content,
            title="Quick Actions"
        )

        self.actions_section.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.pair_button = ctk.CTkButton(
            self.actions_section.content,
            text="🔗 Pair Device",
            command=self.start_pairing
        )

        self.pair_button.pack(
            fill="x",
            pady=(0, 5)
        )

        self.refresh_button = ctk.CTkButton(
            self.actions_section.content,
            text="🔄 Refresh IP",
            command=self.refresh_ip
        )

        self.refresh_button.pack(
            fill="x"
        )

    # ==================================================
    # Actions
    # ==================================================

    def refresh_ip(self):

        self.ip_card.set_value(
            get_local_ip()
        )

    # ==================================================
    # Status
    # ==================================================

    def update_status(self, status: str):

        self.status_card.set_value(status)

    # ==================================================
    # Pairing
    # ==================================================

    def show_pair_code(self, code: str):

        self.pair_code_card.set_value(code)


    def clear_pair_code(self):

        self.pair_code_card.set_value("------")

    def start_pairing(self):

        if self.pair_button.cget("state") == "disabled":
            return

        code = self.remote.start_pairing()

        self.pair_button.configure(
            state="disabled"
        )

        self.show_pair_code(code)

        self.update_status(
            Status.PAIRING
        )

        self.after(
            60000,
            self.end_pairing
        )

    def end_pairing(self):

        self.remote.stop_pairing()

        self.clear_pair_code()

        self.update_status(
            Status.WAITING
        )

        self.pair_button.configure(
            state="normal"
        )