package com.up0k.remote.network.discovery

import com.up0k.remote.models.PcDevice
import java.net.DatagramPacket
import java.net.DatagramSocket
import java.net.InetAddress

object DiscoveryClient {

    private const val DISCOVERY_PORT = 5001
    private const val DISCOVERY_MESSAGE = "WHO_IS_UP0K_REMOTE"

    suspend fun scan(): List<PcDevice> {

        val devices = mutableListOf<PcDevice>()

        val socket = DatagramSocket()

        socket.broadcast = true

        socket.soTimeout = 2000

        try {

            val data = DISCOVERY_MESSAGE.toByteArray()

            val request = DatagramPacket(
                data,
                data.size,
                InetAddress.getByName("255.255.255.255"),
                DISCOVERY_PORT
            )

            socket.send(request)

            while (true) {

                try {

                    val buffer = ByteArray(1024)

                    val response = DatagramPacket(
                        buffer,
                        buffer.size
                    )

                    socket.receive(response)

                    val json = String(
                        response.data,
                        0,
                        response.length
                    )

                    val packet = DiscoveryPacket.fromJson(json)

                    devices.add(
                        packet.toDevice(
                            response.address.hostAddress
                        )
                    )

                } catch (_: Exception) {
                    break
                }
            }

        } finally {

            socket.close()

        }

        return devices
    }
}