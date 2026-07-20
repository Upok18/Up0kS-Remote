"""
Up0k Remote
Remove Device Dialog
"""

from __future__ import annotations

import customtkinter as ctk

from ui.utils.window import center_dialog

class RemoveDeviceDialog(ctk.CTkToplevel):

    def __init__(self, master, device_name, callback):

        super().__init__(master)

        self.callback = callback

        self.title("Remove Device")
        self.geometry("380x180")
        self.resizable(False, False)

        self.grab_set()

        center_dialog(self, master)

        ctk.CTkLabel(
            self,
            text="Remove Trusted Device?",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            self,
            text=f"📱 {device_name}",
            font=("Segoe UI", 16)
        ).pack()

        ctk.CTkLabel(
            self,
            text="This device will need to pair again.",
            text_color="gray"
        ).pack(pady=(5, 20))

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack()

        ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=self.destroy
        ).pack(
            side="left",
            padx=8
        )

        ctk.CTkButton(
            button_frame,
            text="Remove",
            fg_color="#dc2626",
            hover_color="#b91c1c",
            command=self.remove
        ).pack(
            side="left",
            padx=8
        )

    def remove(self):

        print("Dialog Remove clicked")

        self.callback()

        self.destroy()