package com.up0k.remote.storage

import android.content.Context
import java.util.UUID

object DeviceManager {

    private const val PREFS = "up0k_remote"
    private const val DEVICE_ID = "device_id"

    fun getDeviceId(context: Context): String {

        val prefs = context.getSharedPreferences(
            PREFS,
            Context.MODE_PRIVATE
        )

        var id = prefs.getString(DEVICE_ID, null)

        if (id == null) {

            id = UUID.randomUUID().toString()

            prefs.edit()
                .putString(DEVICE_ID, id)
                .apply()
        }

        return id
    }
}