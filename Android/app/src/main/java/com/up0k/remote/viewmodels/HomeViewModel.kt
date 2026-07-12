package com.up0k.remote.viewmodels

import androidx.lifecycle.ViewModel
import com.up0k.remote.models.PcDevice
import com.up0k.remote.network.tcp.RemoteClient

class HomeViewModel : ViewModel() {

    fun connect(ip: String): Boolean {

        if (!RemoteClient.connect(ip)) {
            return false
        }

        if (!RemoteClient.handshake()) {
            RemoteClient.disconnect()
            return false
        }

        println("===== HANDSHAKE =====")
        println("App: ${RemoteClient.session.app}")
        println("Version: ${RemoteClient.session.version}")
        println("Protocol: ${RemoteClient.session.protocol}")
        println("Authentication: ${RemoteClient.session.authenticationRequired}")
        println("=====================")

        return true
    }
}