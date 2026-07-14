"""
Up0k Remote
Network Manager
"""

from __future__ import annotations

import socket
import threading

from typing import Any
from remote.constants import BUFFER_SIZE, DEFAULT_HOST, DEFAULT_PORT
from remote.protocol import decode_packet, encode_packet
from remote.session import Session
from remote.commands.dispatcher import dispatch
from remote.logger import error
# from remote.session import
from remote.handshake import create_hello
from remote.pairing import generate_pair_code

class NetworkServer:
    """TCP server for Up0k Remote."""

    def __init__(self) -> None:

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1,
        )

        self.running = False

        self.sessions: list[Session] = []

        self.thread: threading.Thread | None = None

    def start(self) -> None:
        """Start the server."""

        if self.running:
            return

        self.server.bind((DEFAULT_HOST, DEFAULT_PORT))
        self.server.listen()

        self.running = True

        self.thread = threading.Thread(
            target=self.listen,
            daemon=True,
        )

        self.thread.start()

    def listen(self) -> None:
        """Listen for incoming clients."""

        while self.running:

            client, address = self.accept_client()

            thread = threading.Thread(
                target=self.handle_client,
                args=(client, address),
                daemon=True,
            )

            thread.start()

    def stop(self) -> None:
        """Stop the server."""

        self.running = False

        self.server.close()

    def accept_client(self) -> tuple[socket.socket, tuple[str, int]]:
        """Accept a client connection."""

        return self.server.accept()

    def receive_packet(self, client) -> dict[str, Any] | None:
        """Receive one packet."""

        try:
            data = client.recv(BUFFER_SIZE)

            print("RAW", repr(data))

            if not data:
                return None

            return decode_packet(data)

        except ConnectionResetError:
            return None

        except OSError:
            return None

    def send_packet(self, client, packet: dict) -> None:
        """Send one packet."""

        encoded = encode_packet(packet)

        print("SEND_PACKET:", packet)
        print("RAW BYTES:", repr(encoded))

        client.sendall(encoded)

        print("SEND COMPLETE")

    def remove_session(self, session: Session) -> None:
        """Remove a client session."""

        if session in self.sessions:
            self.sessions.remove(session)

        session.client.close()

    def handle_client(self, client, address) -> None:

        print("1 - handle_client called")

        session = Session(client, address)

        try:

            print("2 - session created")

            self.sessions.append(session)

            print(f"Connected: {session.address}")

            print("3 - creating hello packet")
            hello = create_hello()

            print("4 - hello packet:", hello)

            print("5 - sending hello")
            self.send_packet(session.client, hello)

            print("6 - hello sent")

            print("Authentication removed.")
            session.authenticated = True

            while True:

                print("15 - waiting for command")

                command_packet = self.receive_packet(session.client)

                print("16 - command:", command_packet)

                if command_packet is None:
                    print(f"Disconnected: {session.address}")
                    break

                result = dispatch(command_packet)

                print("17 - result:", result)

                self.send_packet(session.client, result)

                print("18 - result sent")

        except Exception as e:

            error(f"Client error ({session.address}): {e}")

            import traceback
            traceback.print_exc()

        finally:

            print("19 - removing session")
            self.remove_session(session)
