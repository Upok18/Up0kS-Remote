package com.up0k.remote.network.tcp

import org.json.JSONObject

/**
 * Up0k Remote
 * Network Packets
 */

object Packets {

    fun login(password: String): JSONObject {

        return JSONObject().apply {

            put("type", "login")

            put(
                "data",
                JSONObject().apply {
                    put("password", password)
                }
            )

        }

    }

}