package com.up0k.remote.network.discovery

import com.up0k.remote.models.PcDevice

object DiscoveryClient {

    suspend fun scan(): List<PcDevice> {

        // Discovery temporarily disabled.
        return emptyList()

    }

}