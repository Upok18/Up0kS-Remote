"""
Up0k Remote
Section Widget
"""

from __future__ import annotations

import customtkinter as ctk


class Section(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title: str,
        **kwargs
    ):

        super().__init__(
            master,
            fg_color="transparent",
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 24, "bold")
        )

        self.title.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 15)
        )

        self.content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        self.content.grid_columnconfigure(
            0,
            weight=1
        )