import os
import time
from datetime import datetime, timedelta
import pandas as pd
from sms_utils import (
    ensure_file,
    filter_ready_messages,
    update_statuses_and_save,
)
from java import jclass

# ===== Configuration =====
EXTERNAL_FILE_PATH = "/storage/emulated/0/SMSAutomation/messages.csv"
INTERNAL_FILE_NAME = "messages.csv"
POLL_INTERVAL_SECONDS = 10
DELIVER_AFTER_SECONDS = 30


def get_file_path():
    """Return the external CSV path if it exists, otherwise use internal."""
    if os.path.exists(EXTERNAL_FILE_PATH):
        return EXTERNAL_FILE_PATH
    else:
        return INTERNAL_FILE_NAME


def send_sms_via_java(phone, text):
    """Send an SMS through Android’s SmsManager using Chaquopy’s Java bridge."""
    try:
        SmsManager = jclass("android.telephony.SmsManager")
        sms_manager = SmsManager.getDefault()
        sms_manager.sendTextMessage(phone, None, text, None, None)
        print(f"📨 Sent SMS to {phone}: {text[:40]!r}")
        return True
    except Exception as e:
        print(f"❌ Failed to send SMS to {phone}: {e}")
        return False


def run_once():
    """Perform a single iteration of the scheduler."""
    file_path = get_file_path()
    df = ensure_file(file_path)

    ready = filter_ready_messages(df)
    if ready.empty:
        print("⏳ No messages ready to send.")
        return

    print(f"🚀 Found {len(ready)} message(s) ready to send.")
    for idx, row in ready.iterrows():
        phone = str(row["phone"]).strip()
        text = str(row["text"]).strip()
        sent_ok = send_sms_via_java(phone, text)
        if sent_ok:
            df.loc[idx, "status"] = "sent"
            df.loc[idx, "sent_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Handle delivery simulation after 30 seconds
    cutoff = datetime.now() - timedelta(seconds=DELIVER_AFTER_SECONDS)
    if "sent_time" in df.columns:
        mask = (df["status"] == "sent") & (
            pd.to_datetime(df["sent_time"], errors="coerce") < cutoff
        )
        df.loc[mask, "status"] = "delivered"

    update_statuses_and_save(file_path, df)
    print("✅ Cycle complete.\n")


def main_loop():
    """Continuous loop that checks for messages periodically."""
    file_path = get_file_path()
    print(f"SMS scheduler starting. File: {file_path}")
    print(f"Poll interval: {POLL_INTERVAL_SECONDS}s, deliver-after: {DELIVER_AFTER_SECONDS}s")

    while True:
        run_once()
        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main_loop()
