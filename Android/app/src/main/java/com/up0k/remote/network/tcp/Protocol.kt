package com.up0k.remote.network.tcp

import org.json.JSONObject

/**
 * Up0k Remote
 * Network Protocol
 */

object Protocol {

    fun encode(packet: JSONObject): String {
        return packet.toString()
    }

    fun decode(data: String): JSONObject {
        return JSONObject(data)
    }

}