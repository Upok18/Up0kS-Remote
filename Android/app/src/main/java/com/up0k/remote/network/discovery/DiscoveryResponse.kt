package com.up0k.remote.network.discovery

import com.up0k.remote.models.PcDevice

fun DiscoveryPacket.toDevice(ip: String): PcDevice {

    return PcDevice(
        name = name,
        ip = ip,
        online = true
    )
}