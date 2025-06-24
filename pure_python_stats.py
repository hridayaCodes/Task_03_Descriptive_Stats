import csv
import os
import math
from collections import defaultdict, Counter
from time import time

# Timing how long the script takes to run
start_time = time()

# Giving the path to the dataset
file_path = '2024_tw_posts_president_scored_anon.csv'

# Creating an empty list to store each row of the dataset
rows = []

# Opening and reading the CSV file using the built-in csv module
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)

# Creating dictionaries to store numeric stats and text value counts
numeric_stats = defaultdict(list)
text_stats = defaultdict(list)

# Looping through each row to separate numeric and text fields
for row in rows:
    for col, val in row.items():
        try:
            num_val = float(val)
            numeric_stats[col].append(num_val)
        except:
            text_stats[col].append(val)

# Function to calculate summary for numeric columns
def summarize_numeric(col, values):
    count = len(values)
    mean = sum(values) / count
    min_val = min(values)
    max_val = max(values)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in values) / count)
    return f"{col}: count={count}, mean={mean:.2f}, min={min_val}, max={max_val}, std={std_dev:.2f}"

# Function to get value counts and most frequent for text columns
def summarize_text(col, values):
    counts = Counter(values)
    unique = len(counts)
    most_common = counts.most_common(1)[0] if counts else (None, 0)
    return f"{col}: unique={unique}, top={most_common[0]}, freq={most_common[1]}"

# Printing numeric summaries
print("\n🔢 Numeric Columns Summary")
for col, values in numeric_stats.items():
    print(summarize_numeric(col, values))

# Printing text summaries
print("\n🔤 Text Columns Summary")
for col, values in text_stats.items():
    print(summarize_text(col, values))

# Calculating script runtime
total_time = time() - start_time
print(f"\n⏱️ Script Execution Time: {total_time:.2f} seconds")