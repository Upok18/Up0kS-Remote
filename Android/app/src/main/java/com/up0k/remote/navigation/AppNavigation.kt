package com.up0k.remote.navigation

import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController

import com.up0k.remote.screens.HomeScreen
import com.up0k.remote.screens.SplashScreen
import com.up0k.remote.screens.DashboardScreen
import com.up0k.remote.screens.PairScreen

@Composable
fun AppNavigation(
    darkTheme: Boolean,
    onToggleTheme: () -> Unit
) {

    val navController = rememberNavController()

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = MaterialTheme.colorScheme.background
    ) {

        NavHost(
            navController = navController,
            startDestination = Routes.Splash.route
        ) {

            composable(Routes.Splash.route) {

                SplashScreen(
                    navController = navController
                )

            }

            composable(Routes.Home.route) {

                HomeScreen(
                    navController = navController,
                    darkTheme = darkTheme,
                    onToggleTheme = onToggleTheme
                )

            }

            composable(Routes.Dashboard.route) {

                DashboardScreen(
                    navController = navController,
                )

            }

            composable(Routes.Pair.route) {

                PairScreen(
                    navController = navController
                )

            }

        }

    }

}