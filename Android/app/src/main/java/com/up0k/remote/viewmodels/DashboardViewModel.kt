package com.up0k.remote.viewmodels

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import com.up0k.remote.models.SystemInfo
import com.up0k.remote.network.tcp.RemoteClient

class DashboardViewModel : ViewModel() {

    private val _systemInfo = MutableStateFlow<SystemInfo?>(null)
    val systemInfo: StateFlow<SystemInfo?> = _systemInfo

    fun loadSystemInfo() {
        viewModelScope.launch {
            while (isActive) {

                val info = withContext(Dispatchers.IO) {
                    RemoteClient.info()
                }

                _systemInfo.value = info

                delay(800)
            }
        }
    }

    fun shutdown() {
        viewModelScope.launch(Dispatchers.IO) {
            RemoteClient.shutdown()
        }
    }

    fun restart() {
        viewModelScope.launch(Dispatchers.IO) {
            RemoteClient.restart()
        }
    }
}