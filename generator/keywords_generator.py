#!/usr/bin/env python3
import csv
import os

# Predefined list of keywords
keywords = [
    "Graph Processing",
    "Data Quality",
    "Property Graph",
    "Machine Learning",
    "Big Data",
    "Data Mining",
    "Distributed Systems",
    "Knowledge Graph",
    "Semantic Web",
    "Data Integration",
    "Stream Processing",
    "Graph Databases",
    "Query Optimization",
    "Parallel Computing",
    "Data Visualization",
    "Graph Algorithms",
    "Data Cleaning",
    "Network Analysis",
    "Ontologies",
    "Metadata Management"
]

def main():
    # Ensure the output directory exists
    os.makedirs("csv", exist_ok=True)

    # Write keywords.csv
    with open("csv/keywords.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["keyword"])
        for kw in keywords:
            writer.writerow([kw])

    print("Wrote {} keywords to csv/keywords.csv".format(len(keywords)))

if __name__ == "__main__":
    main()
