package com.up0k.remote.navigation

sealed class Routes(val route: String) {

    object Splash : Screen("splash")
    object Home : Routes("home")
    object Scan : Routes("scan")
}