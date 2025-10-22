package com.example.smsautomation;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.Service;
import android.content.Intent;
import android.os.Build;
import android.os.IBinder;
import android.util.Log;

import androidx.core.app.NotificationCompat;

import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class SchedulerService extends Service {

    private static final String TAG = "SMSAutomationService";
    private static final String CHANNEL_ID = "smsautomation_channel";

    @Override
    public void onCreate() {
        super.onCreate();
        Log.i(TAG, "Service created");

        // Start Python once
        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        createNotificationChannel();
        Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
                .setContentTitle("SMSAutomation running")
                .setContentText("Scheduler active")
                .setSmallIcon(R.drawable.ic_launcher_foreground)
                .build();
        startForeground(1, notification);

        new Thread(() -> {
            try {
                Log.i(TAG, "Running Python scheduler loop");
                Python py = Python.getInstance();
                py.getModule("scheduler").callAttr("main_loop");
            } catch (Exception e) {
                Log.e(TAG, "Scheduler error", e);
            }
        }).start();

        // Keep service alive until user stops it
        return START_STICKY;
    }

    private void createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(
                    CHANNEL_ID, "SMSAutomation", NotificationManager.IMPORTANCE_LOW);
            NotificationManager manager = getSystemService(NotificationManager.class);
            if (manager != null) manager.createNotificationChannel(channel);
        }
    }

    @Override
    public IBinder onBind(Intent intent) { return null; }
}
