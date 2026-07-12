import customtkinter as ctk

from ui.widgets.info_card import InfoCard
from ui.widgets.section import Section
from ui.widgets.sidebar import Sidebar
from remote.system import get_computer_name, get_local_ip


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Up0k Remote")

        self.geometry("1100x700")

        self.minsize(1000, 650)

        self.create_layout()

        self.create_content()

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

    # ==================================================
    # Sidebar
    # ==================================================

    def create_sidebar(self):

        title = ctk.CTkLabel(
            self.sidebar,
            text="Up0k Remote",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(
            pady=(30, 10)
        )

        version = ctk.CTkLabel(
            self.sidebar,
            text="v0.1.0-alpha.1"
        )

        version.pack()

        status = ctk.CTkLabel(
            self.sidebar,
            text="🟢 Waiting for connection..."
        )

        status.pack(
            pady=30
        )

    # ==================================================
    # Main Content
    # ==================================================

    def create_content(self):

        self.computer_section = Section(
            self.content,
            title="Computer Information"
        )

        self.devices_section = Section(
            self.content,
            title="Trusted Devices"
        )

        self.actions_section = Section(
            self.content,
            title="Quick Actions"
        )

        self.actions_section.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.devices_section.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.devices_section.add(
            InfoCard(
                self.devices_section,
                "Devices",
                "No trusted devices"
            )
        )

        self.computer_section.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.computer_name_card = InfoCard(
            self.computer_section,
            "Computer Name",
            get_computer_name()
        )

        self.computer_section.add(
            self.computer_name_card
        )

        self.ip_card = InfoCard(
            self.computer_section,
            "IP Address",
            get_local_ip()
        )

        self.computer_section.add(
            self.ip_card
        )

        self.status_card = InfoCard(
            self.computer_section,
            "Status",
            "🟢 Waiting for connection"
        )

        self.computer_section.add(
            self.status_card
        )

        self.devices_section = Section(
            self.content,
            title="Trusted Devices"
        )

        self.devices_section.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.devices_section.add(
            InfoCard(
                self.devices_section,
                "Devices",
                "No trusted devices"
            )
        )

        copy_button = ctk.CTkButton(
            self.actions_section,
            text="📋 Copy IP Address"
        )

        copy_button.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=8
        )

        refresh_button = ctk.CTkButton(
            self.actions_section,
            text="🔄 Refresh IP"
        )

        refresh_button.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=8
        )