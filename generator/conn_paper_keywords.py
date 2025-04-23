#!/usr/bin/env python3
import csv
import random
import os

def main():
    # Ensure output directory exists
    os.makedirs("csv", exist_ok=True)

    # Read all paper IDs
    with open("csv/papers.csv", newline="", encoding="utf-8") as pf:
        paper_ids = [row["paper_id"] for row in csv.DictReader(pf)]

    # Read all keywords
    with open("csv/keywords.csv", newline="", encoding="utf-8") as kf:
        keywords = [row["keyword"] for row in csv.DictReader(kf)]

    # Generate paper-keyword relationships
    rows = []
    for paper_id in paper_ids:
        num_keywords = random.randint(1, 5)  # each paper gets 1-5 keywords
        selected = random.sample(keywords, num_keywords)
        for kw in selected:
            rows.append({
                "paper_id": paper_id,
                "keyword": kw
            })

    # Write to CSV
    out_path = "csv/paper_keywords.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["paper_id", "keyword"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} records to {out_path}")

if __name__ == "__main__":
    main()
