#!/usr/bin/env python3
import csv
import random
import os


# Predefined list of city-country pairs (ensure at least as many as unique venue_ids)
city_country_pairs = [
    ("New York", "United States"), ("London", "United Kingdom"), ("Barcelona", "Spain"),
    ("Tokyo", "Japan"), ("Berlin", "Germany"), ("Paris", "France"),
    ("Stockholm", "Sweden"), ("Sydney", "Australia"), ("Toronto", "Canada"),
    ("Beijing", "China"), ("Amsterdam", "Netherlands"), ("Zurich", "Switzerland"),
    ("Vienna", "Austria"), ("Milan", "Italy"), ("Seoul", "South Korea"),
    ("Bangalore", "India"), ("São Paulo", "Brazil"), ("Cape Town", "South Africa"),
    ("Tel Aviv", "Israel"), ("Dublin", "Ireland"), ("Boston", "United States"),
    ("San Francisco", "United States"), ("Singapore", "Singapore"), ("Munich", "Germany"),
    ("Stockholm", "Sweden"), ("Dubai", "United Arab Emirates"), ("Moscow", "Russia"),
    ("Hong Kong", "China"), ("Geneva", "Switzerland"), ("Lisbon", "Portugal")
]

# Ensure output directory exists
os.makedirs("csv", exist_ok=True)

# Read unique venue IDs from conference_editions.csv
venue_ids = set()
with open("csv/conference_editions.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        venue_ids.add(row["venue_id"])

# Assign a random city-country pair to each venue_id
venue_ids = list(venue_ids)
random.shuffle(city_country_pairs)
venues = []
for vid, (city, country) in zip(venue_ids, city_country_pairs):
    venues.append({
        "venue_id": vid,
        "city": city,
        "country": country
    })

# Write venues.csv
csv_path = "csv/venues.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=["venue_id", "city", "country"])
    writer.writeheader()
    writer.writerows(venues)


print(f"Generated {len(venues)} venue records and saved to: {csv_path}")
