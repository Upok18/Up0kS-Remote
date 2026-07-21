package com.up0k.remote.components

import androidx.compose.foundation.layout.Spacer
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.sp
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.ui.unit.dp

@Composable
fun DevBanner(
    modifier: Modifier = Modifier
) {

    Text(
        text = "⚠️ Currently in active development. ❗Preview Version 0.3.1-alpha.2              📱More features Coming soon..",
        color = MaterialTheme.colorScheme.onBackground.copy(alpha = 0.25f),
        fontSize = 8.sp,
        textAlign = TextAlign.Center,
        modifier = modifier
    )

}