from remote.protocol import encode_packet, decode_packet

packet = {"type": "ping"}

encoded = encode_packet(packet)

print(encoded)

decoded = decode_packet(encoded)

print(decoded)
