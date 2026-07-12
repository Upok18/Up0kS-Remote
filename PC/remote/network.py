"""
Up0k Remote
Network Manager
"""

from __future__ import annotations

import socket
import threading

from typing import Any
from remote.auth import authenticate
from remote.constants import BUFFER_SIZE, DEFAULT_HOST, DEFAULT_PORT
from remote.protocol import decode_packet, encode_packet
from remote.session import Session
from remote.commands.dispatcher import dispatch
from remote.logger import error
# from remote.session import
from remote.handshake import create_hello

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

    def start(self) -> None:
        """Start the server."""

        self.server.bind((DEFAULT_HOST, DEFAULT_PORT))
        self.server.listen()

        self.running = True

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

    def send_packet(self, client, packet: dict[str, Any]) -> None:
        """Send one packet."""

        client.send(encode_packet(packet))

    def remove_session(self, session: Session) -> None:
        """Remove a client session."""

        if session in self.sessions:
            self.sessions.remove(session)

        session.client.close()

    def handle_client(self, client, address) -> None:
        session = Session(client, address)

        try:
            self.sessions.append(session)

            print(f"Connected: {session.address}")

            self.send_packet(session.client, create_hello())

            packet = self.receive_packet(session.client)

            if packet is None:
                 print(f"Disconnected during authentication: {session.address}")
                 return

            response = authenticate(packet)

            self.send_packet(session.client, response)

            if response["type"] != "auth_ok":
                return

            session.authenticated = True

            while True:
                command_packet = self.receive_packet(session.client)

                if command_packet is None:
                    print(f"Disconnected: {session.address}")
                    break

                result = dispatch(command_packet)

                self.send_packet(session.client, result)

        except Exception as e:
            error(f"Client error ({session.address}): {e}")

        finally:
            self.remove_session(session)
