from datetime import datetime


def info(message: str):
    print(f"[{datetime.now():%H:%M:%S}] [INFO] {message}")

def warning(message: str):
    print(f"[{datetime.now():%H:%M:%S}] [WARNING] {message}")


def error(message: str):
    print(f"[{datetime.now():%H:%M:%S}] [ERROR] {message}")

def success(message: str):
    print(f"[{datetime.now():%H:%M:%S}] [SUCCESS] {message}")