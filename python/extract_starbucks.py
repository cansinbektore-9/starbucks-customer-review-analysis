import json

business_file = "../data/yelp_academic_dataset_business.json"

starbucks_businesses = []

with open(business_file, "r", encoding="utf-8") as file:
    for line in file:
        business = json.loads(line)

        if "Starbucks" in business["name"]:
            starbucks_businesses.append(business)

print("Number of Starbucks businesses:", len(starbucks_businesses))

starbucks_ids = {business["business_id"] for business in starbucks_businesses}

print("Number of Starbucks business IDs:", len(starbucks_ids))

import csv

review_file = "../data/yelp_academic_dataset_review.json"
output_file = "../data/starbucks_reviews.csv"

fields = [
    "review_id",
    "business_id",
    "stars",
    "date",
    "text",
    "useful",
    "funny",
    "cool"
]

with open(review_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    writer = csv.DictWriter(outfile, fieldnames=fields)
    writer.writeheader()

    count = 0

    for line in infile:
        review = json.loads(line)

        if review["business_id"] in starbucks_ids:
            writer.writerow({
                field: review.get(field)
                for field in fields
            })
            count += 1

print("Number of Starbucks reviews:", count)

business_output_file = "../data/starbucks_businesses.csv"

business_fields = [
    "business_id",
    "name",
    "city",
    "state",
    "stars",
    "review_count",
    "categories"
]

with open(business_output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=business_fields)
    writer.writeheader()

    for business in starbucks_businesses:
        writer.writerow({
            field: business.get(field)
            for field in business_fields
        })

print("Starbucks business information saved.")