package com.up0k.remote.screens

import androidx.compose.runtime.rememberCoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController

import com.up0k.remote.components.Up0kButton
import com.up0k.remote.network.discovery.DiscoveryClient
import com.up0k.remote.network.tcp.RemoteClient
import com.up0k.remote.navigation.Routes

@Composable
fun PairScreen(
    navController: NavController
) {

    var code by remember {
        mutableStateOf("")
    }

    var error by remember {
        mutableStateOf("")
    }

    val scope = rememberCoroutineScope()

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),

        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {

        Text(
            text = "Pair Device",
            style = MaterialTheme.typography.headlineMedium
        )

        Spacer(modifier = Modifier.height(24.dp))

        OutlinedTextField(
            value = code,
            onValueChange = {
                code = it
            },
            label = {
                Text("Pairing Code")
            }
        )

        Spacer(modifier = Modifier.height(16.dp))

        Up0kButton(
            text = "Pair",
            onClick = {

                scope.launch {


                    error = ""

                    val paired = withContext(Dispatchers.IO) {
                        RemoteClient.pair(
                            code,
                            android.os.Build.MODEL
                        )
                    }

                    if (paired) {
                        navController.navigate(Routes.Dashboard.route)
                    } else {
                        error = "Invalid pairing code."
                    }
                }
            }
        )

        if (error.isNotEmpty()) {

            Spacer(modifier = Modifier.height(16.dp))

            Text(
                text = error,
                color = MaterialTheme.colorScheme.error
            )

        }

    }

}