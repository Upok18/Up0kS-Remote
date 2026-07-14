package com.up0k.remote.network.discovery

import org.json.JSONObject

data class DiscoveryPacket(
    val name: String,
    val port: Int,
    val version: String
) {

    companion object {

        fun fromJson(json: String): DiscoveryPacket {

            val obj = JSONObject(json)

            return DiscoveryPacket(
                name = obj.getString("name"),
                port = obj.getInt("port"),
                version = obj.getString("version")
            )
        }
    }
}