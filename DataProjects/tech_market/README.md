# Tech Layoffs ETL & Analytics Pipeline

## Overview

This project is a beginner data engineering and analytics project focused on analyzing tech industry layoff trends from 2024–2026 using Python and Pandas.

The pipeline extracts raw layoff data from a CSV dataset, performs data cleaning and transformations, exports a cleaned dataset, and generates analytical insights that were later visualized in a Looker Studio dashboard.

**INTERACTIVE DASHBOARD LINK IS IN DASHBOARD SECTION ⬇️**

---

## Why I Built This Project

I built this project for several reasons: to gain beginner-level experience with ETL pipelines, practice data visualization, and better understand the current state of the tech job market.

As a recent college graduate pursuing a transition into data engineering and machine learning engineering, I became interested in the ongoing discussion surrounding layoffs, hiring slowdowns, and the overall competitiveness of entry-level tech roles. I wanted to explore the data myself rather than rely entirely on headlines, social media discussions, or influencer opinions.

Through this project, I found that the current tech market is more nuanced than many online discussions suggest. While factors such as restructuring, cost cutting, overhiring corrections, and AI automation appear throughout the dataset, the market conditions are influenced by multiple overlapping economic and business factors rather than a single cause.

In addition to learning ETL and analytics workflows, this project helped me better understand how data can be used to investigate real-world trends and support more informed conclusions.

---

# Objectives

- Practice building a basic ETL pipeline
- Learn real-world data cleaning workflows
- Perform exploratory data analysis using Pandas
- Create business-focused metrics and summaries
- Visualize cleaned data in Looker Studio

---

# Technologies Used

- Python
- Pandas
- Google Looker (Data) Studio

---

# ETL Pipeline Stages

## Extract

The dataset was imported from a CSV file using Pandas. I retrieved the CSV file from Kaggle. Here is the link: https://www.kaggle.com/datasets/amaymishra11/tech-layoffs-and-hiring-trends-2026

Example:

```python
df = pd.read_csv("tech_layoffs_hiring_trends_elite_v2.csv")
```

---

## Transform

Data cleaning and transformation steps included:

- Removing duplicate records
- Stripping whitespace from text columns
- Standardizing company names using title casing
- Standardizing industry names using uppercase formatting
- Inspecting null values and data types
- Generating summary statistics

Example transformations:

```python
df = df.drop_duplicates()

df["company_name"] = df["company_name"].str.strip().str.title()

df["industry"] = df["industry"].str.strip().str.upper()
```

---

## Load

The cleaned dataset was exported into a new CSV file.

Example:

```python
df.to_csv("cleaned_tech_layoffs.csv", index=False)
```

---

# Data Analysis

The pipeline also included exploratory analysis such as:

- Mean layoffs count
- Mean layoff percentage
- Most common reasons for layoffs

Example:

```python
layoff_reason = df["reason_for_layoffs"].value_counts()

mean_layoff_percentage = df["layoff_percentage"].mean()

layoff_reason = df["reason_for_layoffs"].value_counts()
```

---

# Dashboard

The cleaned dataset was visualized using Google Looker Studio to create an interactive dashboard showing:

- Layoff percentages
- Layoff reasons breakdown
- Layoffs by country
- Industry trends
- Hiring trend summaries

Link: https://datastudio.google.com/reporting/ee998ec8-77c3-4489-8bca-e307182e9096

Screenshots:

<img width="1898" height="1422" alt="image" src="https://github.com/user-attachments/assets/0394f699-695f-4851-a844-7d277eacd4d0" />

<img width="1900" height="1424" alt="image" src="https://github.com/user-attachments/assets/ce2d6be2-3294-48a1-b4a7-55d4191b9ef8" />

<img width="1896" height="1426" alt="image" src="https://github.com/user-attachments/assets/242502a9-3aea-4147-ac15-4dbe28e8a9ff" />

---

# Key Skills Demonstrated

- ETL pipeline development
- Data cleaning and preprocessing
- Exploratory data analysis
- Pandas DataFrames
- Data validation
- Dashboard visualization
- Python scripting

---

# Future Improvements

Planned improvements for future projects include:

- SQL database integration
- Modular pipeline functions
- Data visualizations using Matplotlib (or alternative)
- API-based data extraction
- Logging and error handling

---

# Project Structure

```text
project/
├── tech_layoffs_hiring_trends_elite_v2.csv
├── cleaned_tech_layoffs.csv
├── etl_practice.py
├── README.md
```

---

# Author

Emmanuel Ruffin

Aspiring Data Engineer / ML Engineer with a background in Cybersecurity.
