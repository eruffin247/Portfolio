# Writing an ETL Pipeline on tech layoff trends in 2026.
# Importing Pandas. Pandas is a fast open source Python Data Analysis Library designed for data manipulation and analysis.
import pandas as pd
import matplotlib as plt

# ====================
# EXTRACT
# ====================

df = pd.read_csv("tech_layoffs_hiring_trends_elite_v2.csv") # Created a dataframe (df), which is a two-dimensional data structure, meaning columns and rows.
print(df.info())
print(df.isnull().sum())
print(df.describe())
print()

# ====================
# TRANSFORM
# ====================

df = df.drop_duplicates()
df["company_name"] = df["company_name"].str.strip().str.title()
df["industry"] = df["industry"].str.strip().str.upper()

# ====================
# LOAD
# ====================

df.to_csv("cleaned_tech_layoffs.csv", index=False)
print("PIPELINE IS COMPLETE.")
print()

# ====================
# ANALYZE
# ====================

# Using this pipeline to analyze the data
print("#####################")
print("Data Analysis")
print("#####################")
print()
mean_layoffs_count = df["layoffs_count"].mean() # Finding mean number of layoff count
mean_layoff_percentage = df["layoff_percentage"].mean() # Finding mean of layoff percentage
layoff_reason = df["reason_for_layoffs"].value_counts()
print(f"The mean layoff count based on trends in the tech industry from 2024 - now: {mean_layoffs_count:,.0f}.")
print(f"The mean layoff percentage based on trends in the tech industry from 2024 - now: {mean_layoff_percentage:.1f}%.")
print(f"The top five most common layoff reasons are:\n{layoff_reason.head(5)}")