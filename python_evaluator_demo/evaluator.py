import os
import csv
from datetime import datetime

SUBMISSIONS_DIR = "submissions"
REPORT_FILE = "reports/scores.csv"
POINTS_PER_SUBMISSION = 10

# Load already evaluated files
evaluated_files = set()
with open(REPORT_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        evaluated_files.add(row[1])  # filename

# Scan submissions folder
new_files = [f for f in os.listdir(SUBMISSIONS_DIR) if os.path.isfile(os.path.join(SUBMISSIONS_DIR, f))]

if not new_files:
    print("No files found in submissions folder.")
else:
    count = 0
    for filename in new_files:
        if filename in evaluated_files:
            continue  # skip already evaluated

        # Extract username from filename before first underscore, fallback if none
        if "_" in filename:
            username = filename.split("_")[0]
        else:
            username = filename

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append to CSV
        with open(REPORT_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, filename, POINTS_PER_SUBMISSION, timestamp])

        print(f"Added points for: {filename}")
        count += 1

    if count == 0:
        print("No new submissions found.")
    else:
        print(f"Evaluation complete! Scores updated in {REPORT_FILE}")
