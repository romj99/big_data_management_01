#!/usr/bin/env python3
import csv
import random
import os

def main():
    os.makedirs("csv", exist_ok=True)

    # Load all authors
    authors = []
    with open("csv/authors.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            authors.append(row["author_id"])

    # Load all papers
    papers = []
    with open("csv/papers.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            papers.append(row["paper_id"])

    rows = []
    for paper_id in papers:
        # pick a corresponding author
        corr = random.choice(authors)
        rows.append({
            "author_id": corr,
            "paper_id": paper_id,
            "is_corresponding": True
        })
        # pick 1–3 additional coauthors, distinct from corresponding
        coauthors = random.sample(
            [a for a in authors if a != corr],
            k=random.randint(1, 99)
        )
        for co in coauthors:
            rows.append({
                "author_id": co,
                "paper_id": paper_id,
                "is_corresponding": False
            })

    # Write CSV
    with open("csv/authorship.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["author_id","paper_id","is_corresponding"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} records to csv/authorship.csv")

if __name__ == "__main__":
    main()
