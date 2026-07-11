package com.up0k.remote.components

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun Up0kCard(
    name: String,
    ip: String,
    online: Boolean,
    onConnect: () -> Unit
) {

    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surface
        )
    ) {

        Column(
            modifier = Modifier.padding(16.dp)
        ) {

            Text(
                text = "💻 $name",
                fontSize = 22.sp
            )

            Spacer(modifier = Modifier.height(8.dp))

            Text(
                text = if (online) "🟢 Online" else "🔴 Offline"
            )

            Text(ip)

            Spacer(modifier = Modifier.height(16.dp))

            Up0kButton(
                text = "Connect",
                onClick = onConnect
            )

        }
    }
}