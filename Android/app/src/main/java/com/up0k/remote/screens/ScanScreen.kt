package com.up0k.remote.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.sp
import androidx.compose.foundation.background
import androidx.compose.material3.MaterialTheme
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.runtime.*

import kotlinx.coroutines.delay

import com.up0k.remote.models.PcDevice
import com.up0k.remote.components.DevBanner
import com.up0k.remote.components.Up0kCard

@Composable
fun ScanScreen() {

    var scanning by remember {
        mutableStateOf(true)
    }

    var devices by remember {
        mutableStateOf(listOf<PcDevice>())
    }

    LaunchedEffect(Unit) {
        delay(2000)

        devices = listOf(
            PcDevice(
                name = "Up0k-PC",
                ip = "167.136.99.67",
                online = true
            )
        )

        scanning = false
    }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
    ) {

        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(24.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {

            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {

                if (scanning) {

                    Text(
                        text = "🔍 Scanning for PCs...",
                        fontSize = 26.sp,
                        color = MaterialTheme.colorScheme.onBackground
                    )

                } else {

                    Up0kCard(
                        name = devices.first().name,
                        ip = devices.first().ip,
                        online = devices.first().online,
                        onConnect = {
                            // Coming soon...

                        }
                    )
                }

            }

        }

        DevBanner(
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .padding(bottom = 40.dp)
        )
    }
}