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
import android.os.Build
import android.provider.Settings
import android.content.Context
import com.up0k.remote.network.DeviceId
import com.up0k.remote.models.SystemInfo

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

            val line = reader?.readLine()

            if (line == null) {

                println("UP0K: Connection lost.")

                disconnect()

                return null
            }

            Protocol.decode(line)

        } catch (e: Exception) {

            println("UP0K: Connection lost.")

            e.printStackTrace()

            disconnect()

            null

        }

    }

    // --------------------------------------------------
    // Commands
    // --------------------------------------------------

    fun info(): SystemInfo? {

        send(Packets.info())

        val packet = receive() ?: return null

        val data = packet.getJSONObject("data")

        return SystemInfo(

            deviceName = data.getString("device_name"),

            system = data.getString("system"),

            release = data.getString("release"),

            version = data.getString("version"),

            machine = data.getString("machine"),

            processor = data.getString("processor"),

            ramTotal = data.getDouble("ram_total"),

            ramUsed = data.getDouble("ram_used"),

            ramPercent = data.getDouble("ram_percent")

        )
    }

    fun shutdown(): Boolean {

        send(Packets.shutdown())

        val packet = receive() ?: return false

        return packet.optString("type") == "success"
    }

    fun restart(): Boolean {

        send(Packets.restart())

        val packet = receive() ?: return false

        return packet.optString("type") == "success"
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

    fun sendClientInfo(
        context: Context,
        deviceName: String
    ) {

//        val uuid = Settings.Secure.getString(
//            context.contentResolver,
//            Settings.Secure.ANDROID_ID
//        )

        val uuid = DeviceId.get(context)

        send(
            JSONObject().apply {

                put("type", "client_info")

                put(
                    "data",
                    JSONObject().apply {

                        put("uuid", uuid)
                        put("device", deviceName)
                        put("model", Build.MODEL)
                        put("platform", "Android")
                        put("android_version", Build.VERSION.RELEASE)
                        put("app_version", session.version)
                    }
                )
            }
        )
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

    fun pair(
        code: String,
        device: String,
        deviceId: String
    ): Boolean {

        println("===== PAIR =====")
        println(
            Packets.pair(
                code,
                device,
                deviceId
            ).toString(2)
        )
        println("================")

        send(
            Packets.pair(
                code,
                device,
                deviceId
            )
        )

        val packet = receive() ?: return false

        return packet.optString("type") == "pair_ok"
    }

}