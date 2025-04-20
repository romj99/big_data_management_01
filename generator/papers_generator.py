import csv
import uuid
import random
import os
from datetime import datetime
import pandas as pd

# Predefined lists for generating titles and topics
topics = [
    "Graph Processing", "Data Quality", "Property Graph", "Machine Learning",
    "Big Data", "Data Mining", "Distributed Systems", "Knowledge Graph",
    "Semantic Web", "Data Integration"
]
prefixes = [
    "A Study on", "An Analysis of", "Towards", "Improving",
    "Evaluating", "A Survey of", "Understanding", "Challenges in"
]

# Ensure output directory exists
os.makedirs('csv', exist_ok=True)

# Generate 100 paper records
papers = []
for _ in range(20000):
    paper_id = str(uuid.uuid4())
    topic = random.choice(topics)
    title = f"{random.choice(prefixes)} {topic}"
    year = random.randint(2000, 2024)
    start_page = random.randint(1, 200)
    length = random.randint(5, 15)
    pages = f"{start_page}-{start_page + length}"
    abstract = (
        f"In this paper, we explore {topic.lower()} and present "
        "methodology and results to advance the state of the art."
    )
    papers.append({
        "paper_id": paper_id,
        "title": title,
        "year": year,
        "pages": pages,
        "abstract": abstract
    })

# Write to CSV
csv_path = 'csv/papers.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["paper_id", "title", "year", "pages", "abstract"])
    writer.writeheader()
    writer.writerows(papers)

# Preview first 10 rows
df = pd.DataFrame(papers)

print(f"Generated 100 paper records and saved to: {csv_path}")
