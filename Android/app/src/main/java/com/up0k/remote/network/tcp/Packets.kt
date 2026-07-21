package com.up0k.remote.network.tcp

import org.json.JSONObject

/**
 * Up0k Remote
 * Network Packets
 */

object Packets {

    fun pair(
        code: String,
        device: String,
        deviceId: String
    ): JSONObject {

        return JSONObject().apply {

            put("type", "pair")

            put(
                "data",
                JSONObject().apply {

                    put("code", code)
                    put("device", device)
                    put("id", deviceId)

                }
            )
        }
    }

    fun info(): JSONObject {

        return JSONObject().apply {

            put("type", "info")

            put(
                "data",
                JSONObject()
            )
        }
    }

    fun shutdown(): JSONObject {

        return JSONObject().apply {

            put("type", "shutdown")

            put(
                "data",
                JSONObject()
            )
        }
    }

    fun restart(): JSONObject {

        return JSONObject().apply {

            put("type", "restart")

            put(
                "data",
                JSONObject()
            )
        }
    }

}