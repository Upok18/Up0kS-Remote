package com.up0k.remote.components.cards

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.up0k.remote.models.SystemInfo

@Composable
fun MemoryCard(
    info: SystemInfo?
) {

    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surfaceVariant
        )
    ) {

        Column(
            modifier = Modifier.padding(16.dp)
        ) {

            Text(
                "🧠 Memory",
                fontSize = 20.sp
            )

            Spacer(modifier = Modifier.height(10.dp))

            LinearProgressIndicator(
                progress = {
                    (info?.ramPercent?.toFloat() ?: 0f) / 100f
                },
                modifier = Modifier.fillMaxWidth()
            )

            Spacer(modifier = Modifier.height(8.dp))

            Text(
                "${info?.ramUsed} / ${info?.ramTotal} GB (${info?.ramPercent}%)"
            )

        }

    }

}