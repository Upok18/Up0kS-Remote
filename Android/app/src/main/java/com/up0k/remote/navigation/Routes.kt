package com.up0k.remote.navigation

sealed class Routes(val route: String) {

    object Splash : Routes("splash")

    object Home : Routes("home")

    object Pair : Routes("pair")

    object Dashboard : Routes("dashboard")
}