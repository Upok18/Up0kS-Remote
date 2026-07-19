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

}