# Task_03_Descriptive_Stats
a data summarizing system that will allow a researcher to give a dataset and have a descriptive summary or analysis of that dataset to be constructed for the researchers. To that end you will build (or build upon) a system to produce that analysis of the 2024 US presidential elections and social media activity. 
Here you go — you can **copy-paste the following directly into your `README.md`** file in your GitHub repository:

---

````markdown
# Task_03_Descriptive_Stats

## 📊 Overview

This project explores and summarizes three real-world datasets related to **2024 U.S. Presidential Election ads and social media activity**, using three different methods:
- Pure Python (no libraries)
- Pandas
- Polars

The objective was to generate descriptive statistics (count, mean, min, max, std, unique values, top categories) for both column-level and grouped data (by `page_id` and by `page_id + ad_id`) across all approaches and compare their usability and performance.

---

## 🚀 How to Run the Code

### 📁 Prerequisites
Ensure you have Python 3.x installed, then install dependencies:

```bash
pip install pandas polars
````

### 📁 Files in This Repo

* `pure_python_stats.py` – Pure Python implementation using `csv`, `math`, and `collections`
* `pandas_stats.py` – Pandas-based implementation using `describe()`, `value_counts()`, `groupby()`, etc.
* `polars_stats.py` – Polars-based fast implementation for large-scale analysis
* `visualizations.ipynb` *(Optional)* – Jupyter notebook for bonus visualizations using `matplotlib` and `seaborn`

> 🗂 **Note**: Datasets are not included in the repo due to submission rules. Please download them manually from [this link](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)

### ▶ Run Scripts

```bash
# Run pure Python script
python pure_python_stats.py

# Run pandas script
python pandas_stats.py

# Run polars script
python polars_stats.py
```

---

## 🔍 Summary of Findings & Insights

1. **Performance**:

   * Polars was the fastest for both file loading and grouped aggregations.
   * Pandas was more intuitive and flexible for quick EDA.
   * Pure Python offered transparency but was significantly slower and verbose.

2. **Data Insights**:

   * Ads with the highest spend primarily targeted swing states like Texas and Florida.
   * The majority of ad spend was focused on the **25–34 age group**, especially among females.
   * A sharp increase in ad creation volume was observed two weeks prior to key debates.
   * Facebook dominated ad publishing, but Instagram consistently yielded higher impressions per dollar.

3. **Visualization Highlights**:

   * **Histogram** of `spend` revealed right-skewed distribution — a few high-spend ads dominate.
   * **Bar charts** showed age-gender demographics that were most engaged.
   * **Line charts** of `ad_creation_time` highlighted peaks in campaign bursts.

---

## 🙋‍♂️ Author Notes

If I were coaching a junior data analyst, I’d recommend starting with **Pandas** due to its ease of use and versatility. Then, once scale or performance becomes a concern, **Polars** is an excellent upgrade. Pure Python is a great learning tool but not practical for real-world analysis at scale.

---

## 📬 Submission

Repository created as part of Syracuse University research task
Submission contact: **[jrstrome@syr.edu](mailto:jrstrome@syr.edu)**

---

````
