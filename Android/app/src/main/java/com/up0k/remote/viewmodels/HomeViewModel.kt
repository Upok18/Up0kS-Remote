package com.up0k.remote.viewmodels

import androidx.lifecycle.ViewModel
import android.app.Application
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.AndroidViewModel
import com.up0k.remote.models.PcDevice
import com.up0k.remote.network.discovery.DiscoveryClient
import com.up0k.remote.network.tcp.RemoteClient
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

class HomeViewModel(
    application: Application
) : AndroidViewModel(application) {

    private val _devices = MutableStateFlow<List<PcDevice>>(emptyList())
    val devices: StateFlow<List<PcDevice>> = _devices

    private val _scanning = MutableStateFlow(false)
    val scanning: StateFlow<Boolean> = _scanning

    fun scan() {

        viewModelScope.launch {

            _scanning.value = true

            val result = withContext(Dispatchers.IO) {
                DiscoveryClient.scan()
            }

            _devices.value = result

            _scanning.value = false
        }
    }

    fun connect(device: PcDevice): Boolean {

        println("========== CONNECT ==========")
        println("Connecting to ${device.ip}")

        if (!RemoteClient.connect(device.ip)) {
            println("❌ TCP connection failed")
            return false
        }

        println("✅ TCP connected")

        RemoteClient.sendClientInfo(
            getApplication(),
            device.name
        )

        if (!RemoteClient.handshake()) {
            println("❌ Handshake failed")
            RemoteClient.disconnect()
            return false
        }

        println("✅ Handshake OK")

        println("===== HANDSHAKE =====")
        println("App: ${RemoteClient.session.app}")
        println("Version: ${RemoteClient.session.version}")
        println("Protocol: ${RemoteClient.session.protocol}")
        println("Authentication: ${RemoteClient.session.authenticationRequired}")
        println("Pairing: ${RemoteClient.session.pairingRequired}")
        println("=====================")

        return true
    }
}