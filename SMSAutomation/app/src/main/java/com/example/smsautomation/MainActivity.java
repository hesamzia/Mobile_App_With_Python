package com.example.smsautomation;

import androidx.appcompat.app.AppCompatActivity;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "SMSAutomation";
    private static final int INTERVAL = 15 * 60 * 1000; // 15 minutes

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Intent serviceIntent = new Intent(this, SchedulerService.class);
        startForegroundService(serviceIntent);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Log.i(TAG, "✅ onCreate() reached");

        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        scheduleRepeatingAlarm();
    }

    private void scheduleRepeatingAlarm() {
        AlarmManager alarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);
        Intent intent = new Intent(this, SchedulerReceiver.class);
        PendingIntent pendingIntent = PendingIntent.getBroadcast(
                this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
        );

        long triggerAtMillis = System.currentTimeMillis() + INTERVAL;

        // Wake up even during Doze
        alarmManager.setExactAndAllowWhileIdle(
                AlarmManager.RTC_WAKEUP,
                triggerAtMillis,
                pendingIntent
        );

        Log.i(TAG, "✅ Alarm scheduled for Python scheduler");
    }

    public static class SchedulerReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            try {
                if (!Python.isStarted()) {
                    Python.start(new AndroidPlatform(context));
                }
                Python py = Python.getInstance();
                py.getModule("scheduler").callAttr("run_once");
                Log.i(TAG, "✅ Python scheduler executed via AlarmManager");
            } catch (Exception e) {
                Log.e(TAG, "❌ Error running scheduler", e);
            }

            // Reschedule next run
            AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
            Intent newIntent = new Intent(context, SchedulerReceiver.class);
            PendingIntent newPendingIntent = PendingIntent.getBroadcast(
                    context, 0, newIntent, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
            );
            long nextTrigger = System.currentTimeMillis() + INTERVAL;
            alarmManager.setExactAndAllowWhileIdle(
                    AlarmManager.RTC_WAKEUP,
                    nextTrigger,
                    newPendingIntent
            );
        }
    }
}
