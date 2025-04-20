#!/usr/bin/env python3
import csv
import uuid
import random
import os

# Read journal IDs from previously generated journals.csv
journals = []
with open("csv/journals.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        journals.append(row["journal_id"])

volumes = []
for journal_id in journals:
    # Generate between 3 and 10 volumes per journal
    num_volumes = random.randint(3, 10)
    years = random.sample(range(2000, 2025), k=num_volumes)
    years.sort()
    for vol_num, year in enumerate(years, start=1):
        volumes.append({
            "volume_id": str(uuid.uuid4()),
            "journal_id": journal_id,
            "volume_number": vol_num,
            "year": year
        })

# Ensure output directory exists
os.makedirs("csv", exist_ok=True)

# Write journal_volumes.csv
out_path = "csv/journal_volumes.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["volume_id", "journal_id", "volume_number", "year"])
    writer.writeheader()
    writer.writerows(volumes)


print(f"Generated {len(volumes)} volume records and saved to: {out_path}")
