import socket
import os

from remote.protocol import encode_packet, decode_packet
from remote.version import PROTOCOL_VERSION

HOST = "127.0.0.1"
PORT = 5000
PASSWORD = "654321"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("=" * 55)
    print("           Up0k Remote Developer Console")
    print("=" * 55)
    print(f"Server : {HOST}:{PORT}")
    print("Status : Connected")
    print("Type 'help' for available commands.")
    print("=" * 55)


client = socket.socket()
client.connect((HOST, PORT))

# Receive HELLO
hello = decode_packet(client.recv(4096))

# Login
client.send(
    encode_packet(
        {"version": PROTOCOL_VERSION, "action": "login", "data": {"password": PASSWORD}}
    )
)

response = decode_packet(client.recv(4096))

if response["type"] != "auth_ok":
    print("Authentication failed.")
    client.close()
    exit()

clear()
banner()

while True:
    command = input("\nUp0k Remote > ").strip()

    if not command:
        continue

    command = command.lower()

    if command == "exit":
        break

    if command == "clear":
        clear()
        banner()
        continue

    if command == "help":
        print("""
=========================================
Power
=========================================
shutdown
restart
cancel
=========================================
Media
=========================================
play_pause
next_track
previous_track
volume_up
volume_down
mute

=========================================
Developer
=========================================
help
clear
ping
info
exit
""")
        continue

    packet = {"version": PROTOCOL_VERSION, "action": command, "data": {}}

    client.send(encode_packet(packet))

    try:
        result = decode_packet(client.recv(4096))

    except Exception as e:
        print(f"\nDisconnected: {e}")
        break

client.close()

print("\nDisconnected.")
