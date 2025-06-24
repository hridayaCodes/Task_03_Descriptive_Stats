import polars as pl
import os
import time

# Define the path where your CSV files are stored
folder_path = "/Users/hridayamurudkar/Downloads/period_03"

# Listing all CSV files from the given folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Looping over each file
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    print(f"\n📄 Analyzing File: {csv_file}")

    # Starting the timer to measure performance
    start_time = time.time()

    # Reading the CSV file using Polars
    df = pl.read_csv(file_path, ignore_errors=True)

    # Displaying the shape of the dataset
    print(f"\n🔹 Descriptive Statistics:\nshape: {df.shape}")

    # Describing the dataset for numeric and categorical fields
    try:
        print(df.describe())
    except Exception as e:
        print("Could not run describe():", e)

    # Calculating unique value count per column
    print("\n🔹 Unique Value Count per Column:")
    for col in df.columns:
        try:
            unique_count = df[col].n_unique()
            print(f"  {col}: {unique_count} unique values")
        except Exception:
            print(f"  {col}: Could not compute")

    # Top 3 most frequent values for string columns
    print("\n🔹 Top 3 Frequent Values (for String Columns):")
    for col in df.columns:
        try:
            if df[col].dtype == pl.Utf8:
                vc = df[col].value_counts().sort("counts", descending=True)
                top_3 = vc.head(3)
                print(f"  {col}: {top_3}")
        except Exception:
            print(f"  {col}: Could not compute frequency")

    # Ending the timer and displaying elapsed time
    end_time = time.time()
    print(f"\n⏱️ Execution Time: {end_time - start_time:.2f} seconds")
