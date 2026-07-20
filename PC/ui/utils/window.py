from __future__ import annotations


def center_window(window, width: int, height: int):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def center_dialog(dialog, parent):

    dialog.update_idletasks()

    width = dialog.winfo_width()
    height = dialog.winfo_height()

    x = parent.winfo_rootx() + (parent.winfo_width() - width) // 2
    y = parent.winfo_rooty() + (parent.winfo_height() - height) // 2

    dialog.geometry(f"{width}x{height}+{x}+{y}")