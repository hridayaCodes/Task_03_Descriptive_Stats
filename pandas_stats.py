import csv
import pandas as pd
import time
import os

# Starting a timer to measure how long the entire script takes
start_time = time.time()

# Setting the path where my CSV files are stored
data_dir = "/Users/hridayamurudkar/Downloads/period_03"

# Listing the CSV files I want to analyze
csv_files = [
    "2024_fb_ads_president_scored_anon.csv",
    "2024_fb_posts_president_scored_anon.csv",
    "2024_tw_posts_president_scored_anon.csv"
]

# Looping through each file to process them one by one
for filename in csv_files:
    print(f"📄 Analyzing File: {filename}")
    file_path = os.path.join(data_dir, filename)

    # Reading the CSV file using pandas
    df = pd.read_csv(file_path)

    # Showing basic shape of the dataset: how many rows and columns
    print(f"🔹 Dataset Shape: {df.shape}")

    # Showing summary statistics for all columns including text and categorical
    print(f"🔹 Descriptive Statistics (including non-numeric):")
    print(df.describe(include='all'))

    # Counting missing values for each column
    print(f"🔹 Missing Values Per Column:")
    print(df.isnull().sum())

    # Showing how many unique values exist in each column
    print(f"🔹 Unique Value Count Per Column:")
    for col in df.columns:
        unique_count = df[col].nunique()
        print(f"  {col}: {unique_count} unique values")

    # Displaying the top 3 most frequent values for each string column
    print(f"🔹 Top 3 Frequent Values (for String Columns):")
    for col in df.select_dtypes(include='object').columns:
        try:
            top_vals = df[col].value_counts().head(3)
            print(f"  {col}:")
            print(top_vals)
        except Exception as e:
            print(f"  {col}: Could not compute frequency")

    print("⏱️ Done analyzing file")

# Ending the timer and showing total time taken
end_time = time.time()
print(f"✅ Total Time Taken for Script: {round(end_time - start_time, 2)} seconds")
