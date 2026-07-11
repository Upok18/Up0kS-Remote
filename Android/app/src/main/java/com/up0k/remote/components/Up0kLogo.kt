package com.up0k.remote.components

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun Up0kLogo() {

    Column(
        horizontalAlignment = Alignment.CenterHorizontally
    ) {

        Text(
            text = "🖥",
            fontSize = 72.sp
        )

        Spacer(modifier = androidx.compose.ui.Modifier.height(12.dp))

        Text(
            text = "Up0k Remote",
            fontSize = 34.sp,
            color = MaterialTheme.colorScheme.onBackground
        )

        Spacer(modifier = androidx.compose.ui.Modifier.height(8.dp))

        Text(
            text = "Control your PC over your local network.",
            fontSize = 16.sp,
            color = MaterialTheme.colorScheme.onBackground,
            textAlign = TextAlign.Center
        )
    }
}