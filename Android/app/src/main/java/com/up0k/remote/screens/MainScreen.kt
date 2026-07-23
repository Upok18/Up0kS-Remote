package com.up0k.remote.screens

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.Modifier
import com.up0k.remote.components.BottomBar
import androidx.compose.ui.Alignment
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.LaunchedEffect
import com.up0k.remote.viewmodels.DashboardViewModel
import com.up0k.remote.navigation.Routes
import androidx.navigation.NavController
import com.up0k.remote.dialogs.ComingSoonDialog


enum class MainTab {
    Remote,
    Pc,
    Files,
    Settings
}

@Composable
fun MainScreen(
    navController: NavController
) {

    var selectedTab by remember {
        mutableStateOf(MainTab.Pc)
    }

    var showComingSoon by remember {
        mutableStateOf(false)
    }

    val dashboardViewModel: DashboardViewModel = viewModel()

    val connectionLost by dashboardViewModel.connectionLost.collectAsState()

    Box(
        modifier = Modifier.fillMaxSize()
    ) {

        when (selectedTab) {

            MainTab.Remote -> RemoteScreen()

            MainTab.Pc -> PcScreen()

            MainTab.Files -> FilesScreen()

            MainTab.Settings -> SettingsScreen()

        }

        LaunchedEffect(connectionLost) {

            if (connectionLost) {

                navController.navigate(Routes.Home.route) {
                    popUpTo(Routes.Home.route) {
                        inclusive = true
                    }
                }

            }

        }

        BottomBar(
            selectedTab = selectedTab,
            onTabSelected = {

                when (it) {

                    MainTab.Pc -> {
                        selectedTab = MainTab.Pc
                    }

                    else -> {
                        showComingSoon = true
                    }

                }

            },
            modifier = Modifier.align(Alignment.BottomCenter)
        )

        ComingSoonDialog(
            show = showComingSoon,
            onDismiss = {
                showComingSoon = false
            }
        )

    }

}