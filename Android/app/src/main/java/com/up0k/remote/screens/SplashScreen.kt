package com.up0k.remote.screens

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.runtime.LaunchedEffect
import androidx.navigation.NavController
import kotlinx.coroutines.delay
import com.up0k.remote.navigation.Routes
import com.up0k.remote.R
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.graphics.graphicsLayer

@Composable
fun SplashScreen(
    navController: NavController
) {

    var startAnimation by remember {
        mutableStateOf(false)
    }

    val alpha by animateFloatAsState(
        targetValue = if (startAnimation) 1f else 0f,
        animationSpec = tween(800),
        label = "alpha"
    )

    val scale by animateFloatAsState(
        targetValue = if (startAnimation) 1f else 0.9f,
        animationSpec = tween(800),
        label = "scale"
    )

    LaunchedEffect(Unit) {

        startAnimation = true

        delay(2000)

        navController.navigate(Routes.Home.route) {
            popUpTo(Routes.Splash.route) {
                inclusive = true
            }
        }
    }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background),
        contentAlignment = Alignment.Center
    ) {

        Column(
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            Image(
                painter = painterResource(id = R.drawable.up0k_logo_v1),
                contentDescription = "Up0k Logo",
                modifier = Modifier
                    .size(80.dp)
                    .graphicsLayer{
                        this.alpha = alpha
                        scaleX = scale
                        scaleY = scale
                    }
            )

            Spacer(modifier = Modifier.height(24.dp))

            Text(
                text = "Up0k Remote",
                fontSize = 34.sp,
                color = MaterialTheme.colorScheme.onBackground
            )

            Spacer(modifier = Modifier.height(12.dp))

            Text(
                text = "Control your PC over your local network.",
                fontSize = 15.sp,
                textAlign = TextAlign.Center,
                color = MaterialTheme.colorScheme.onBackground
            )
        }
    }
}