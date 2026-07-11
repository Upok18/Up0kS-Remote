package com.up0k.remote

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.Modifier
import com.up0k.remote.screens.HomeScreen
import com.up0k.remote.ui.theme.Up0kRemoteTheme
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import com.up0k.remote.navigation.AppNavigation

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        enableEdgeToEdge()

        setContent {

            var darkTheme by rememberSaveable {
                mutableStateOf(true)
            }

            Up0kRemoteTheme(
                darkTheme = darkTheme,
                dynamicColor = false
            ) {

                AppNavigation(
                    darkTheme = darkTheme,
                    onToggleTheme = {
                        darkTheme = !darkTheme
                    }
                )

            }
        }

    }

}