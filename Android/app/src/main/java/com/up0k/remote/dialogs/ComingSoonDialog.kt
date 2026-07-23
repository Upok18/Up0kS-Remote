package com.up0k.remote.dialogs

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.Alignment

import com.up0k.remote.R
import com.up0k.remote.components.Up0kButton

@Composable
fun ComingSoonDialog(
    show: Boolean,
    onDismiss: () -> Unit
) {

    if (!show) return

    AlertDialog(

        onDismissRequest = onDismiss,

        icon = {

            Image(
                painter = painterResource(R.drawable.coming_soon),
                contentDescription = null,
                modifier = Modifier.size(120.dp)
            )

        },

        title = {

            Text(
                text = "We tried..."
            )

        },

        text = {

            Text(
                text =
                    "This feature isn't ready yet.\n\nSee you in the next update! \uD83D\uDE80",
                color = MaterialTheme.colorScheme.onSurface
            )

        },

        confirmButton = {

            Up0kButton(
                text = "Got it 👍",
                onClick = onDismiss
            )

        }

    )

}