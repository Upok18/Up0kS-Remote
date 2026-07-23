from remote.version import PROTOCOL_VERSION

def execute(remote, data):

    return {
        "version": PROTOCOL_VERSION,
        "type": "trusted_devices",
        "data": {
            "devices": remote.get_trusted_devices_info()
        }
    }