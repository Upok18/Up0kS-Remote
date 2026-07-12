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

        self.columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 24, "bold")
        )

        title_label.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 15)
        )

    def add(self, widget):

        row = len(self.grid_slaves())

        widget.grid(
            row=row,
            column=0,
            sticky="ew",
            pady=8
        )