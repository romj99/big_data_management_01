#!/usr/bin/env python3
import csv
import os
import uuid
import random
from datetime import datetime, timedelta

# Ensure output directory exists
os.makedirs("csv", exist_ok=True)

# Read all paper IDs from papers.csv
paper_ids = []
with open("csv/papers.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        paper_ids.append(row["paper_id"])

# Predefined review text templates
review_templates = [
    "Well-written paper with clear contributions.",
    "The methodology is sound but needs more evaluation.",
    "Interesting ideas but the presentation is unclear.",
    "Significant results but lacks comparison with related work.",
    "The paper requires major revisions before acceptance.",
    "Strong theoretical foundations but missing practical validation.",
    "Good discussion but results section is too brief.",
    "Excellent paper; I recommend acceptance.",
    "The work is novel but the writing could be improved.",
    "Relevant topic but the experiments are insufficient."
]

reviews = []
# Generate exactly 3-5 reviews per paper
for paper_id in paper_ids:
    for _ in range(3,5):
        review_id = str(uuid.uuid4())
        review_text = random.choice(review_templates)
        score = random.randint(1, 5)
        # Random review date between paper year and paper year+1
        # First, find paper year from papers.csv
        # For simplicity, use current date offset
        days_ago = random.randint(0, 365)
        review_date = (datetime.now() - timedelta(days=days_ago)).date().isoformat()
        reviews.append({
            "review_id": review_id,
            "review_text": review_text,
            "score": score,
            "date": review_date
        })

# Write reviews.csv
csv_path = "csv/reviews.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["review_id", "review_text", "score", "date"])
    writer.writeheader()
    writer.writerows(reviews)


print(f"Generated {len(reviews)} reviews and saved to: {csv_path}")
