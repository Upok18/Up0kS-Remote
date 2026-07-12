package com.up0k.remote.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.MaterialTheme
import androidx.compose.foundation.background
import androidx.navigation.NavController
import androidx.compose.ui.tooling.preview.Preview

import android.content.res.Configuration
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.compose.runtime.collectAsState

import com.up0k.remote.components.Up0kButton
import com.up0k.remote.models.PcDevice
import com.up0k.remote.components.DevBanner
import com.up0k.remote.components.Up0kCard
import com.up0k.remote.dialogs.ComingSoonDialog
import com.up0k.remote.viewmodels.HomeViewModel
import com.up0k.remote.ui.theme.Up0kRemoteTheme
import com.up0k.remote.navigation.Routes

@Composable
fun HomeScreen(
    navController: NavController,
    darkTheme: Boolean,
    onToggleTheme: () -> Unit
) {

    val viewModel: HomeViewModel = viewModel()

    val devices by viewModel.devices.collectAsState()
    val scanning by viewModel.scanning.collectAsState()

    var showComingSoon by remember {
        mutableStateOf(false)
    }

    Box(
        modifier = Modifier.fillMaxSize()
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .background(MaterialTheme.colorScheme.background)
                .padding(24.dp),

            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Top
        ) {

//            Text(
//                text = "🖥 Up0k Remote",
//                color = MaterialTheme.colorScheme.onBackground,
//                fontSize = 32.sp,
//                textAlign = TextAlign.Center,
//                modifier = Modifier.fillMaxWidth()
//            )
//
//            Spacer(modifier = Modifier.height(20.dp))
//
//            Text(
//                text = "Control your PC over your local network.",
//                color = MaterialTheme.colorScheme.onBackground,
//                textAlign = TextAlign.Center,
//                modifier = Modifier
//                    .fillMaxWidth(0.8f)
//            )
//
            Spacer(modifier = Modifier.height(20.dp))

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {

                Text(
                    text = "Devices",
                    fontSize = 24.sp,
                    color = MaterialTheme.colorScheme.onBackground
                )

                Up0kButton(
                    text = if (scanning) "Scanning..." else "🔄 Scan",
                    onClick = {
                        viewModel.scan()
                    }
                )

            }

            Spacer(modifier = Modifier.height(20.dp))

            LazyColumn(
                modifier = Modifier.fillMaxWidth(),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {

                items(devices) { device ->

                    Up0kCard(
                        name = device.name,
                        ip = device.ip,
                        online = device.online,
                        onConnect = {
                            val connected = viewModel.connect(device)

                            if (connected) {
                                showComingSoon = true
                            }
                        }
                    )

                }

            }

            if (!scanning && devices.isEmpty()) {

                Spacer(modifier = Modifier.height(24.dp))

                Text(
                    text = "No devices found.\nTap Scan to search.",
                    color = MaterialTheme.colorScheme.onBackground,
                    textAlign = TextAlign.Center
                )
            }

            Spacer(modifier = Modifier.height(20.dp))

            Button(
                onClick = onToggleTheme
            ) {
                Text(
                    if (darkTheme)
                    "☀️ Light Mode"
                    else
                    "🌙 Dark Mode"
                )
            }
        }

        DevBanner(
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .padding(bottom = 40.dp)
        )

        ComingSoonDialog(
            show = showComingSoon,
            onDismiss = {
                showComingSoon = false
            }
        )
   }
}



//@Preview(name = "Light", showBackground = true)
//@Composable
//fun HomeLightPreview() {
//    Up0kRemoteTheme(
//        darkTheme = false,
//        dynamicColor = false
//    ) {
//        HomeScreen()
//    }
//}
//
//@Preview(
//    name = "Dark",
//    showBackground = true,
//    uiMode = Configuration.UI_MODE_NIGHT_YES
//)
//@Composable
//fun HomeDarkPreview() {
//    Up0kRemoteTheme(
//        darkTheme = true,
//        dynamicColor = false
//    ) {
//        HomeScreen()
//    }
//}