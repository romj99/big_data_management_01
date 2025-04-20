#!/usr/bin/env python3
import csv
import uuid
import random
import os
from datetime import datetime, timedelta

def main():
    # Ensure output directory exists
    os.makedirs("csv", exist_ok=True)

    # Read conference IDs from previously generated conferences.csv
    conf_ids = []
    with open("csv/conferences.csv", newline="", encoding="utf-8") as conf_file:
        reader = csv.DictReader(conf_file)
        for row in reader:
            conf_ids.append(row["conf_id"])

    editions = []
    for conf_id in conf_ids:
        # Generate between 2 and 5 editions per conference
        num_editions = random.randint(2, 5)
        years = random.sample(range(2000, 2025), k=num_editions)
        for year in years:
            # Random start date in March, June, September, or December
            month = random.choice([3, 6, 9, 12])
            day = random.randint(1, 28)
            start_date = datetime(year, month, day).date()
            end_date = start_date + timedelta(days=3)
            editions.append({
                "edition_id": str(uuid.uuid4()),
                "conf_id": conf_id,
                "year": year,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                # Placeholder venue_id: will use real IDs once venues.csv is generated
                "venue_id": str(uuid.uuid4())
            })

    # Write conference_editions.csv
    out_path = "csv/conference_editions.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=[
            "edition_id", "conf_id", "year", "start_date", "end_date", "venue_id"
        ])
        writer.writeheader()
        writer.writerows(editions)

    print(f"Wrote {len(editions)} records to: {out_path}")

if __name__ == "__main__":
    main()
