"""
Up0k Remote
Info Card Widget
"""

from __future__ import annotations

import customtkinter as ctk


class InfoCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title: str,
        value: str,
        value_font=("Segoe UI", 18, "bold"),
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=12,
            border_width=1,
            **kwargs
        )

        self.configure(height=90)
        self.pack_propagate(False)

        self.title = title
        self.value = value
        self.value_font = value_font

        self.build()

    def build(self):

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text=self.title,
            # font=("Segoe UI", 13),
            font=("Segoe UI", 13),
            text_color=("gray40", "gray70")
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(10, 2)
        )

        self.value_label = ctk.CTkLabel(
            self,
            text=self.value,
            font=self.value_font
        )

        self.value_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(0, 10)
        )

    def set_value(self, value: str):

        self.value = value

        self.value_label.configure(
            text=value
        )