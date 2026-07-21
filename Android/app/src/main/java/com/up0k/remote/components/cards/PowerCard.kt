package com.up0k.remote.components.cards

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.up0k.remote.components.Up0kContainer

@Composable
fun PowerCard(
    onShutdown: () -> Unit,
    onRestart: () -> Unit
) {

    Up0kContainer() {

        Column {

            Button(
                onClick = onShutdown,
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("🟥 Shutdown PC")
            }

            Spacer(modifier = Modifier.height(12.dp))

            Button(
                onClick = onRestart,
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("🔄 Restart PC")
            }

        }

    }

}