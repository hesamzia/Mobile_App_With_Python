import os
import pandas as pd
from datetime import datetime, timedelta

# ===== Ensure file =====
def ensure_file(file_path):
    if not os.path.exists(file_path):
        print(f"⚠️ File not found, creating new one: {file_path}")
        df = pd.DataFrame(columns=["date", "time", "phone", "text", "status", "sent_time"])
        df.to_csv(file_path, index=False)
    else:
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            df = pd.DataFrame(columns=["date", "time", "phone", "text", "status", "sent_time"])

    # Make sure all required columns exist
    for col in ["date", "time", "phone", "text", "status", "sent_time"]:
        if col not in df.columns:
            df[col] = ""
    return df


# ===== Date and time parsing =====
def _parse_datetime(row):
    """Safely combine date and time strings into a datetime object."""
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(f"{row['date']} {row['time']}", fmt)
        except Exception:
            continue
    return datetime.min  # Fallback if parsing fails


# ===== Filter ready messages =====
def filter_ready_messages(df):
    """Return messages with status='not sent' and date/time <= now."""
    now = datetime.now()
    ready_rows = []

    for idx, row in df.iterrows():
        try:
            msg_time = _parse_datetime(row)
            if (row["status"].strip().lower() == "not sent") and (msg_time <= now):
                ready_rows.append(idx)
        except Exception as e:
            print(f"⚠️ Skipping invalid row {idx}: {e}")

    return df.loc[ready_rows]


# ===== Update statuses and save =====
def update_statuses_and_save(df, file_path):
    """Save the updated DataFrame safely to CSV."""
    try:
        tmp_path = file_path + ".tmp"
        df.to_csv(tmp_path, index=False)
        os.replace(tmp_path, file_path)
        print(f"💾 Saved updates to {file_path}")
    except Exception as e:
        print(f"❌ Error saving file {file_path}: {e}")
