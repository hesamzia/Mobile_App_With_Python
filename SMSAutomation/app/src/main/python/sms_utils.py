import os
import pandas as pd
from datetime import datetime

REQUIRED_COLUMNS = ["date", "time", "phone", "text", "status"]


def ensure_file(file_path):
    """Ensure the message file exists and has correct columns."""
    if not os.path.exists(file_path):
        print(f"⚙️ Creating new file: {file_path}")
        df = pd.DataFrame(columns=REQUIRED_COLUMNS)
        df.to_csv(file_path, index=False)
        return df

    df = pd.read_csv(file_path)
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    return df


def _parse_date_time(date_str, time_str):
    """Parse combined date and time into a datetime object."""
    for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%d/%m/%Y %H:%M"]:
        try:
            return datetime.strptime(f"{date_str} {time_str}", fmt)
        except Exception:
            continue
    return None


def filter_ready_messages(df):
    """Return rows where status is 'not sent' and datetime <= now."""
    ready_rows = []
    now = datetime.now()
    for idx, row in df.iterrows():
        if str(row.get("status", "")).strip().lower() != "not sent":
            continue
        dt = _parse_date_time(str(row["date"]), str(row["time"]))
        if dt and dt <= now:
            ready_rows.append(idx)
    return df.loc[ready_rows]


def update_statuses_and_save(file_path, df):
    """Safely save the DataFrame to disk."""
    tmp_path = f"{file_path}.tmp"
    df.to_csv(tmp_path, index=False)
    os.replace(tmp_path, file_path)
    print(f"💾 File updated: {file_path}")
