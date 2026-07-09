from remote.config import load_config
from remote.discovery import DiscoveryServer
from remote.logger import info
from remote.network import NetworkServer
from remote.banner import show


def start_server() -> None:
    config = load_config()

    show()

    info("Starting Up0k Remote...")
    info(f"Listening on {config['server']['host']}:{config['server']['port']}")

    discovery = DiscoveryServer()
    discovery.start()

    network = NetworkServer()
    network.start()
