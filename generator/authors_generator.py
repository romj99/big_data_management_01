#!/usr/bin/env python3
import csv
import uuid
import random
from datetime import datetime, timedelta

# Predefined data for random generation
first_names = ["James","Mary","John","Patricia","Robert","Jennifer",
               "Michael","Linda","William","Elizabeth"]
last_names  = ["Smith","Johnson","Williams","Brown","Jones",
               "Garcia","Miller","Davis","Rodriguez","Martinez"]
countries   = ["United States","United Kingdom","Canada","Australia",
               "Germany","France","Spain","Italy","Netherlands","Sweden"]

def random_date(start_year=1950, end_year=1995):
    start = datetime(start_year, 1, 1)
    end   = datetime(end_year, 12, 31)
    delta = end - start
    return (start + timedelta(days=random.randrange(delta.days))).date()

def main():
    authors = []
    for _ in range(2000):
        authors.append({
            "author_id": str(uuid.uuid4()),
            "full_name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "country_of_birth": random.choice(countries),
            "date_of_birth": random_date().isoformat(),
            "is_phd": random.choice([True, False])
        })

    # Write out authors.csv
    with open("csv/authors.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["author_id","full_name",
                                               "country_of_birth","date_of_birth","is_phd"])
        writer.writeheader()
        writer.writerows(authors)

    print("Wrote 2000 records to authors.csv")

if __name__ == "__main__":
    main()
