package com.up0k.remote.ui.theme

import android.app.Activity
import android.content.res.Configuration
import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.tooling.preview.Preview
import com.up0k.remote.screens.HomeScreen

private val DarkColorScheme = darkColorScheme(
    primary = Lime600,
    secondary = Green400,

    background = Color(0xFF121212),
    surface = Color(0xFF1B1B1B),

    onPrimary = Color.White,
    onBackground = Color.White,
    onSurface = Color.White
)

private val LightColorScheme = lightColorScheme(

    primary = Purple500,
    secondary = Green400,

    background = Color(0xFFD5D5D5),
    surface = Color(0xFFC4C4C4),

    onPrimary = Color.White,
    onBackground = Color.Black,
    onSurface = Color.Black
)

@Composable
fun Up0kRemoteTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    // Dynamic color is available on Android 12+
    dynamicColor: Boolean = false,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        }

        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        content = content
    )
}

//@Preview(name = "Light", showBackground = true)
//@Composable
//fun HomeLightPreview() {
//    Up0kRemoteTheme(
//        darkTheme = false,
//        dynamicColor = false
//    ) {
//        HomeScreen()
//    }
//}
//
//@Preview(
//    name = "Dark",
//    showBackground = true,
//    uiMode = Configuration.UI_MODE_NIGHT_YES
//)
//@Composable
//fun HomeDarkPreview() {
//    Up0kRemoteTheme(
//        darkTheme = true,
//        dynamicColor = false
//    ) {
//        HomeScreen()
//    }
//}