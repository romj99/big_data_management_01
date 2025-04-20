#!/usr/bin/env python3
import csv
import os
import random

def main():
    os.makedirs("csv", exist_ok=True)

    # --- 1. conference_has_edition.csv ---
    with open("csv/conference_editions.csv", newline="", encoding="utf-8") as f:
        editions = list(csv.DictReader(f))
    with open("csv/conference_has_edition.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["conf_id", "edition_id"])
        for e in editions:
            writer.writerow([e["conf_id"], e["edition_id"]])

    # --- 2. edition_held_at.csv ---
    with open("csv/edition_held_at.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["edition_id", "venue_id"])
        for e in editions:
            writer.writerow([e["edition_id"], e["venue_id"]])

    # --- 3. journal_has_volume.csv ---
    with open("csv/journal_volumes.csv", newline="", encoding="utf-8") as f:
        volumes = list(csv.DictReader(f))
    with open("csv/journal_has_volume.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["journal_id", "volume_id"])
        for v in volumes:
            writer.writerow([v["journal_id"], v["volume_id"]])

    # --- 4. review_assignments.csv ---
    # load papers
    with open("csv/papers.csv", newline="", encoding="utf-8") as f:
        papers = [r["paper_id"] for r in csv.DictReader(f)]
    # load authorship map
    auth_map = {}
    with open("csv/authorship.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            auth_map.setdefault(r["paper_id"], []).append(r["author_id"])
    # load all authors
    with open("csv/authors.csv", newline="", encoding="utf-8") as f:
        all_authors = [r["author_id"] for r in csv.DictReader(f)]
    # load reviews
    with open("csv/reviews.csv", newline="", encoding="utf-8") as f:
        reviews = [r["review_id"] for r in csv.DictReader(f)]

    assignments = []
    idx = 0
    # assume exactly 3 reviews per paper, in order
    for paper in papers:
        group = reviews[idx:idx+3]
        idx += 3
        for rev in group:
            # pick reviewer not among paper’s authors
            possible = [a for a in all_authors if a not in auth_map.get(paper,[])]
            reviewer = random.choice(possible) if possible else random.choice(all_authors)
            assignments.append({
                "review_id": rev,
                "paper_id": paper,
                "reviewer_id": reviewer
            })

    with open("csv/review_assignments.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=["review_id", "paper_id", "reviewer_id"])
        writer.writeheader()
        writer.writerows(assignments)

    print("✅ Generated:")
    print(f" - conference_has_edition.csv ({len(editions)} rows)")
    print(f" - edition_held_at.csv         ({len(editions)} rows)")
    print(f" - journal_has_volume.csv      ({len(volumes)} rows)")
    print(f" - review_assignments.csv      ({len(assignments)} rows)")

if __name__ == "__main__":
    main()
