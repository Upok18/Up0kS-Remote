"""
Action Card
"""

from __future__ import annotations

import customtkinter as ctk


class ActionCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        icon: str,
        title: str,
        subtitle: str,
        command,
        **kwargs
    ):

        super().__init__(
            master,
            corner_radius=15,
            border_width=1,
            cursor="hand2",
            **kwargs
        )

        self.command = command
        self.enabled = True

        self.grid_columnconfigure(0, weight=1)

        self.icon = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 28)
        )

        self.icon.pack(
            pady=(18, 8)
        )

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 16, "bold")
        )

        self.title.pack()

        self.subtitle = ctk.CTkLabel(
            self,
            text=subtitle,
            font=("Segoe UI", 12),
            text_color=("gray45", "gray65")
        )

        self.subtitle.pack(
            pady=(2, 18)
        )

        # Make the whole card clickable
        for widget in (
            self,
            self.icon,
            self.title,
            self.subtitle,
        ):
            widget.bind("<Button-1>", self._clicked)
            widget.bind("<Enter>", self._hover_enter)
            widget.bind("<Leave>", self._hover_leave)

    def _clicked(self, event):

        if self.enabled:
            self.command()

    def disable(self):

        self.enabled = False

        self.configure(
            border_width=0
        )

    def enable(self):

        self.enabled = True

        self.configure(
            border_width=1
        )

    def _hover_enter(self, event):

        if not self.enabled:
            return

        self.configure(
            border_width=8
        )


    def _hover_leave(self, event):

        if not self.enabled:
            return

        self.configure(
            border_width=1
        )