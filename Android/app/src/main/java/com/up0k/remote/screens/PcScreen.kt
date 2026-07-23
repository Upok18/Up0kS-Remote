package com.up0k.remote.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.ui.unit.dp
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.draw.alpha
import androidx.lifecycle.viewmodel.compose.viewModel
import com.up0k.remote.components.DevBanner
import com.up0k.remote.viewmodels.DashboardViewModel
import com.up0k.remote.components.cards.MemoryCard
import com.up0k.remote.components.cards.InfoCard
import com.up0k.remote.components.cards.PowerCard

@Composable
fun PcScreen() {

    val dashboardViewModel: DashboardViewModel = viewModel()

    val info by dashboardViewModel.systemInfo.collectAsState()

    LaunchedEffect(Unit) {
        dashboardViewModel.loadSystemInfo()
    }

    Box(
        modifier = Modifier.fillMaxSize()
    ) {

        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(
                    start = 24.dp,
                    top = 24.dp,
                    end = 24.dp,
                    bottom = 120.dp
                ),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            Spacer(modifier = Modifier.height(14.dp))

            Text(
                text = "My PC",
                fontSize = 32.sp,
                color = MaterialTheme.colorScheme.onBackground
            )

            InfoCard(info)

            Spacer(modifier = Modifier.height(16.dp))

            MemoryCard(info)

            Spacer(modifier = Modifier.height(40.dp))

            PowerCard(
                onShutdown = {
                    dashboardViewModel.shutdown()
                },
                onRestart = {
                    dashboardViewModel.restart()
                }
            )
        }
    }
}