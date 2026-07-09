import time

from remote.discovery import DiscoveryServer

discovery = DiscoveryServer()

print("Starting discovery...")
discovery.start()

time.sleep(10)

print("Stopping discovery...")
discovery.stop()
