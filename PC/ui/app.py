"""
Up0k Remote
Desktop Application
"""

import customtkinter as ctk

from ui.main_window import MainWindow


def run():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = MainWindow()

    app.mainloop()