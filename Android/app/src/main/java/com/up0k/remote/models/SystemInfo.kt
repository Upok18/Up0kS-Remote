package com.up0k.remote.models

data class SystemInfo(

    val deviceName: String,

    val system: String,

    val release: String,

    val version: String,

    val machine: String,

    val processor: String,

    val ramTotal: Double,

    val ramUsed: Double,

    val ramPercent: Double

)