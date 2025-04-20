#!/usr/bin/env python3
import csv
import os

# List of sample journals
journals = [
    {"journal_id": "VLDBJ",      "name": "VLDB Journal"},
    {"journal_id": "TODS",       "name": "ACM Transactions on Database Systems"},
    {"journal_id": "TKDE",       "name": "IEEE Transactions on Knowledge and Data Engineering"},
    {"journal_id": "JDIQ",       "name": "Journal of Data and Information Quality"},
    {"journal_id": "DKE",        "name": "Data & Knowledge Engineering"},
    {"journal_id": "KAIS",       "name": "Knowledge and Information Systems"},
    {"journal_id": "CSUR",       "name": "ACM Computing Surveys"},
    {"journal_id": "COMSON",     "name": "Computer Science Review"},
    {"journal_id": "IJGIS",      "name": "International Journal of Geographic Information Science"},
    {"journal_id": "PLOS",       "name": "PLOS One"}
]

def main():
    # Ensure output directory exists
    os.makedirs("csv", exist_ok=True)

    # Write journals.csv
    out_path = "csv/journals.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["journal_id", "name"])
        writer.writeheader()
        writer.writerows(journals)

    print(f"Wrote {len(journals)} records to: {out_path}")

if __name__ == "__main__":
    main()
