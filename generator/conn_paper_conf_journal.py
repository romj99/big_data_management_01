#!/usr/bin/env python3
import csv
import random
import os


# Ensure output directory exists
os.makedirs("csv", exist_ok=True)

# Load all paper IDs
with open("csv/papers.csv", newline="", encoding="utf-8") as pf:
    paper_ids = [row["paper_id"] for row in csv.DictReader(pf)]

# Load all conference edition IDs
with open("csv/conference_editions.csv", newline="", encoding="utf-8") as cf:
    edition_ids = [row["edition_id"] for row in csv.DictReader(cf)]

# Load all journal volume IDs
with open("csv/journal_volumes.csv", newline="", encoding="utf-8") as jf:
    volume_ids = [row["volume_id"] for row in csv.DictReader(jf)]

paper_in_conf = []
paper_in_journ = []

# Assign each paper randomly to conference (70%) or journal (30%)
for pid in paper_ids:
    if random.random() < 0.7:
        paper_in_conf.append({
            "paper_id": pid,
            "edition_id": random.choice(edition_ids)
        })
    else:
        paper_in_journ.append({
            "paper_id": pid,
            "volume_id": random.choice(volume_ids)
        })

# Write paper_in_conference.csv
conf_path = "csv/paper_in_conference.csv"
with open(conf_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["paper_id", "edition_id"])
    writer.writeheader()
    writer.writerows(paper_in_conf)

# Write paper_in_journal.csv
journ_path = "csv/paper_in_journal.csv"
with open(journ_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["paper_id", "volume_id"])
    writer.writeheader()
    writer.writerows(paper_in_journ)


print(f"Generated {len(paper_in_conf)} conference assignments and saved to: {conf_path}")
print(f"Generated {len(paper_in_journ)} journal assignments and saved to: {journ_path}")
