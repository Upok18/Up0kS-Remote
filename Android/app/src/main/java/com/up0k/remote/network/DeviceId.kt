package com.up0k.remote.network

import android.content.Context
import java.util.UUID

object DeviceId {

    private const val PREF = "up0k_remote"
    private const val KEY = "device_id"

    fun get(context: Context): String {

        val prefs = context.getSharedPreferences(PREF, Context.MODE_PRIVATE)

        var id = prefs.getString(KEY, null)

        if (id == null) {

            id = UUID.randomUUID().toString()

            prefs.edit()
                .putString(KEY, id)
                .apply()
        }

        return id
    }
}