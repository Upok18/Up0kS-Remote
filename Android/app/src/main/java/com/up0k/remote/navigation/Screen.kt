package com.up0k.remote.navigation

sealed class Screen(val route: String) {

    object Home : Screen("home")

    object Scanning : Screen("scanning")

    object PcList : Screen("pc_list")

    object Dashboard : Screen("dashboard")
}