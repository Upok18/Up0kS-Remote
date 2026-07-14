package com.up0k.remote.network.tcp

/**
 * Up0k Remote
 * TCP Session
 */

data class Session(

    var connected: Boolean = false,
    var authenticated: Boolean = false,

    var app: String = "",
    var version: String = "",
    var protocol: Int = 0,

    var authenticationRequired: Boolean = true,
    var pairingRequired: Boolean = false

)