package com.up0k.remote.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Icon
import androidx.compose.material3.Surface
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.ui.draw.clip

import com.up0k.remote.R
import com.up0k.remote.screens.MainTab

@Composable
fun BottomBar(
    selectedTab: MainTab,
    onTabSelected: (MainTab) -> Unit,
    modifier: Modifier = Modifier
) {

    Surface(
        modifier = modifier
            .fillMaxWidth()
            .navigationBarsPadding()
            .padding(horizontal = 16.dp, vertical = 12.dp),
        shape = RoundedCornerShape(24.dp),
        shadowElevation = 10.dp,
        tonalElevation = 6.dp
    ) {

        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 16.dp),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {

            BottomIcon(
                R.drawable.remote,
                selectedTab == MainTab.Remote
            ) {
                onTabSelected(MainTab.Remote)
            }

            BottomIcon(
                R.drawable.pc,
                selectedTab == MainTab.Pc
            ) {
                onTabSelected(MainTab.Pc)
            }

            BottomIcon(
                R.drawable.files,
                selectedTab == MainTab.Files
            ) {
                onTabSelected(MainTab.Files)
            }

            BottomIcon(
                R.drawable.settings,
                selectedTab == MainTab.Settings
            ) {
                onTabSelected(MainTab.Settings)
            }

        }

    }

}

@Composable
private fun BottomIcon(
    icon: Int,
    selected: Boolean,
    onClick: () -> Unit
) {

    Surface(
        shape = RoundedCornerShape(16.dp),
        color =
            if (selected)
                MaterialTheme.colorScheme.primaryContainer
            else
                MaterialTheme.colorScheme.surface,
        onClick = onClick
    ) {

        Icon(
            painter = painterResource(icon),
            contentDescription = null,
            modifier = Modifier
                .padding(12.dp)
                .size(26.dp),

            tint =
                if (selected)
                    MaterialTheme.colorScheme.primary
                else
                    MaterialTheme.colorScheme.onSurfaceVariant
        )

    }

}