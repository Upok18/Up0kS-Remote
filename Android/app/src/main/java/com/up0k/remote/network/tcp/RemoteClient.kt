package com.up0k.remote.network.tcp

import com.up0k.remote.network.NetworkConstants
import org.json.JSONObject
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.InetSocketAddress
import java.net.Socket
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

/**
 * Up0k Remote
 * TCP Remote Client
 */

object RemoteClient {

    val session = Session()

    private var socket: Socket? = null

    private var reader: BufferedReader? = null

    private var writer: PrintWriter? = null

    // --------------------------------------------------
    // Connection
    // --------------------------------------------------

    fun connect(ip: String): Boolean {

        return try {

            socket = Socket()

            val client = socket ?: return false

            client.connect(
                InetSocketAddress(
                    ip,
                    NetworkConstants.DEFAULT_PORT
                ),
                NetworkConstants.CONNECTION_TIMEOUT
            )

            reader = BufferedReader(
                InputStreamReader(client.getInputStream())
            )

            writer = PrintWriter(
                client.getOutputStream(),
                true
            )

            true

        } catch (e: Exception) {

            android.util.Log.e("UP0K", "CONNECT ERROR", e)

            disconnect()

            false
        }
    }

    fun isConnected(): Boolean {

        return socket?.isConnected == true &&
                socket?.isClosed == false

    }

    // --------------------------------------------------
    // Communication
    // --------------------------------------------------

    fun send(packet: JSONObject) {

        writer?.println(
            Protocol.encode(packet)
        )

    }

    fun receive(): JSONObject? {

        return try {

            val line = reader?.readLine() ?: return null

            Protocol.decode(line)

        } catch (e: Exception) {

            e.printStackTrace()

            null

        }

    }

    // --------------------------------------------------
    // Cleanup
    // --------------------------------------------------

    fun disconnect() {

        reader?.close()
        writer?.close()
        socket?.close()

        reader = null
        writer = null
        socket = null

    }

    fun handshake(): Boolean {

        val packet = receive() ?: return false

        if (packet.optString("type") != "hello") {
            return false
        }

        val data = packet.getJSONObject("data")

        session.connected = true
        session.app = data.optString("app")
        session.version = data.optString("version")
        session.protocol = data.optInt("protocol")

        session.authenticationRequired =
            data.optBoolean("authentication", true)

        session.pairingRequired =
            data.optBoolean("pairing", false)

        return true

    }

    // --------------------------------------------------
    // Login
    // --------------------------------------------------

    fun pair(code: String, device: String): Boolean {

        println("===== PAIR =====")
        println(Packets.pair(code, device).toString(2))
        println("================")

        send(
            Packets.pair(
                code,
                device
            )
        )

        val packet = receive() ?: return false

        return packet.optString("type") == "pair_ok"
    }

}