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

    # Generate citations: each paper cites 0-5 other papers
    citations = []
    for paper_id in paper_ids:
        num_cites = random.randint(0, 5)
        # choose distinct papers excluding self
        possible = [pid for pid in paper_ids if pid != paper_id]
        cited = random.sample(possible, min(num_cites, len(possible)))
        for cited_id in cited:
            citations.append({
                "citing_paper_id": paper_id,
                "cited_paper_id": cited_id
            })

    # Write to CSV
    out_path = "csv/paper_cites.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["citing_paper_id", "cited_paper_id"])
        writer.writeheader()
        writer.writerows(citations)

    # Preview first 10 rows
    import pandas as pd
    df = pd.DataFrame(citations)
    print(df.head(10).to_string(index=False))

    print(f"\nWrote {len(citations)} citations to {out_path}")

if __name__ == "__main__":
    main()
