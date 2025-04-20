#!/usr/bin/env python3
import csv
import os
import pandas as pd

# List of sample conferences and workshops
conferences = [
    {"conf_id": "SIGMOD",    "name": "ACM SIGMOD International Conference on Management of Data",                             "type": "Conference"},
    {"conf_id": "VLDB",      "name": "International Conference on Very Large Data Bases",                                      "type": "Conference"},
    {"conf_id": "ICDE",      "name": "IEEE International Conference on Data Engineering",                                      "type": "Conference"},
    {"conf_id": "KDD",       "name": "ACM SIGKDD Conference on Knowledge Discovery and Data Mining",                         "type": "Conference"},
    {"conf_id": "WWW",       "name": "The Web Conference (formerly WWW)",                                                    "type": "Conference"},
    {"conf_id": "ISWC",      "name": "International Semantic Web Conference",                                                 "type": "Conference"},
    {"conf_id": "EDBT",      "name": "International Conference on Extending Database Technology",                              "type": "Conference"},
    {"conf_id": "CIKM",      "name": "ACM International Conference on Information and Knowledge Management",                  "type": "Conference"},
    {"conf_id": "PODS",      "name": "Symposium on Principles of Database Systems",                                             "type": "Conference"},
    {"conf_id": "ICDT",      "name": "International Conference on Database Theory",                                              "type": "Conference"},
    {"conf_id": "WSDM",      "name": "ACM International Conference on Web Search and Data Mining",                             "type": "Conference"},
    {"conf_id": "SIGSPATIAL","name": "ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems","type": "Conference"},
    {"conf_id": "EDM",       "name": "International Conference on Educational Data Mining",                                    "type": "Workshop"},
    {"conf_id": "SEBD",      "name": "Symposium on Advances in Database Systems",                                               "type": "Workshop"}
]

# Ensure the output directory exists
os.makedirs("csv", exist_ok=True)

# Write conferences.csv
csv_path = "csv/conferences.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["conf_id", "name", "type"])
    writer.writeheader()
    writer.writerows(conferences)

print(f"Generated {len(conferences)} records and saved to: {csv_path}")
