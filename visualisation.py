import pandas as pd
import ast

# Load CSV
df = pd.read_csv("2024_fb_ads_president_scored_anon.csv")

# Clean: ad_creation_time
df['ad_creation_time'] = pd.to_datetime(df['ad_creation_time'], errors='coerce', dayfirst=True)

# Clean: publisher_platforms
df['publisher_platforms'] = df['publisher_platforms'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])

# Derive: main_platform (first entry of publisher_platforms list)
df['main_platform'] = df['publisher_platforms'].apply(lambda x: x[0] if x else 'unknown')

# Clean: illuminating_mentions
df['illuminating_mentions'] = df['illuminating_mentions'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])

# Clean: delivery_by_region
df['delivery_by_region'] = df['delivery_by_region'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) and x != '{}' else {})

# Clean: demographic_distribution
df['demographic_distribution'] = df['demographic_distribution'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) and x != '{}' else {})

# Optional: Check for rows where datetime parsing failed
invalid_dates = df[df['ad_creation_time'].isna()]
print(f"Rows with invalid ad_creation_time: {len(invalid_dates)}")

# Preview cleaned data
print(df[['ad_creation_time', 'publisher_platforms', 'main_platform', 'illuminating_mentions']].head(15))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

# Load CSV with proper converters
df = pd.read_csv("2024_fb_ads_president_scored_anon.csv", converters={
    'publisher_platforms': eval,
    'illuminating_mentions': eval,
    'delivery_by_region': eval,
    'demographic_distribution': eval
})

# Clean date
df["ad_creation_time"] = pd.to_datetime(df["ad_creation_time"], errors='coerce')

# Add main platform
df["main_platform"] = df["publisher_platforms"].apply(lambda x: x[0] if isinstance(x, list) and x else "unknown")

# -----------------------
# 1. Spend vs Impressions
# -----------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="estimated_spend", y="estimated_impressions", hue="main_platform")
plt.title("Spend vs Impressions by Platform")
plt.xlabel("Estimated Spend (USD)")
plt.ylabel("Estimated Impressions")
plt.tight_layout()
plt.show()

# -----------------------
# 2. Ad Volume Over Time
# -----------------------
ads_per_day = df.groupby("ad_creation_time").size()
ads_per_day.plot(kind='line', marker='o', figsize=(10, 5), title="Ad Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Ads")
plt.tight_layout()
plt.show()

# -----------------------
# 3. Platform Usage
# -----------------------
platform_counts = df["main_platform"].value_counts()
sns.barplot(x=platform_counts.index, y=platform_counts.values)
plt.title("Ad Count per Platform")
plt.ylabel("Number of Ads")
plt.tight_layout()
plt.show()

# -----------------------
# 4. Mentions Bar Chart
# -----------------------
mention_counts = defaultdict(int)
for mentions in df["illuminating_mentions"]:
    for mention in mentions:
        mention_counts[mention] += 1

mention_df = pd.DataFrame(mention_counts.items(), columns=["Name", "Count"]).sort_values(by="Count", ascending=False)
sns.barplot(data=mention_df, x="Name", y="Count")
plt.title("Top Illuminating Mentions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------
# 5. Region Spend
# -----------------------
region_spend = defaultdict(int)
for region_dict in df["delivery_by_region"]:
    for region, values in region_dict.items():
        region_spend[region] += values.get("spend", 0)

region_df = pd.DataFrame(region_spend.items(), columns=["Region", "Total Spend"]).sort_values(by="Total Spend", ascending=False)
sns.barplot(data=region_df, x="Region", y="Total Spend")
plt.title("Total Spend by Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------
# 6. Demographics Heatmap
# -----------------------
demo_data = defaultdict(lambda: defaultdict(int))
for demo_dict in df["demographic_distribution"]:
    for k, v in demo_dict.items():
        gender, age = k.split('_')
        demo_data[age][gender] += v.get("spend", 0)

demo_df = pd.DataFrame(demo_data).T.fillna(0)
sns.heatmap(demo_df, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Demographic Spend Heatmap")
plt.xlabel("Gender")
plt.ylabel("Age Group")
plt.tight_layout()
plt.show()
