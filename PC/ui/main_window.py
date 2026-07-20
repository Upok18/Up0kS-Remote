"""
Up0k Remote
Main Window
"""

from __future__ import annotations

import customtkinter as ctk

from ui.utils.window import center_window
from ui.widgets.navbar import Navbar

from ui.pages.dashboard import DashboardPage
from ui.pages.devices import DevicesPage
from ui.pages.settings import SettingsPage

from remote.service import RemoteService


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.remote = RemoteService()

        self.title("Up0k Remote")

        center_window(self, 1080, 700)

        self.minsize(1000, 650)

        self.create_layout()

        self.create_pages()

        self.remote.start_server()

    # ==================================================
    # Layout
    # ==================================================

    def create_layout(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.navbar = Navbar(self)

        self.navbar.set_callback(
            self.show_page
        )

        self.navbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

        self.page_container = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.page_container.grid_columnconfigure(0, weight=1)
        self.page_container.grid_rowconfigure(0, weight=1)

        self.page_container.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.after(
            10,
            lambda: self.show_page("dashboard")
        )

    # ==================================================
    # Pages
    # ==================================================

    def show_page(self, page: str):

        self.pages[page].tkraise()

    def create_pages(self):

        self.pages = {

            "dashboard": DashboardPage(
                self.page_container,
                self.remote
            ),

            "devices": DevicesPage(
                self.page_container,
                self.remote
            ),

            "settings": SettingsPage(
                self.page_container
            ),
        }

        self.remote.on_status_changed = (
            self.pages["dashboard"].update_status
        )

        for page in self.pages.values():

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )