package com.up0k.remote.navigation

sealed class Screen(val route: String) {

    // Connection Flow
    object Home : Screen("home")
    object Scanning : Screen("scanning")
    object PcList : Screen("pc_list")

    // Main App
    object Main : Screen("main")

}