## Overview

This project demonstrates a beginner-level ETL (Extract, Transform, Load) pipeline built with Python and Pandas. The pipeline processes exported workout and body composition data from the Strong fitness tracking application, cleans and transforms the data, and prepares it for future analysis and visualization.

The project tracks my twelve-week bulking phase from March 16, 2026 through June 3, 2026. The pipeline creates clean datasets that can later be used for dashboarding, trend analysis, and performance tracking.

---

## Project Objectives

* Extract workout and body composition data from exported CSV files
* Remove duplicate records
* Remove unnecessary columns
* Remove non-exercise records
* Standardize date formats
* Filter records to a specific training period
* Export cleaned datasets for analysis
* Practice working with both CSV and Parquet file formats

---

## Dataset

### Source

Data was exported from the Strong Workout Tracker application.

### Files

| File                             | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| exported_strong_sessions.csv     | Raw workout and exercise data                  |
| exported_body_comp.csv           | Raw body composition measurements              |
| cleaned_strong_sessions.csv      | Cleaned workout dataset                        |
| cleaned_body_comp.csv            | Cleaned body composition dataset               |
| cleaned_exercises.parquet        | Parquet version of the cleaned workout dataset |

---

## ETL Process

### Extract

The pipeline imports two datasets:

* Workout data
* Body composition data

```python
exercise_df = pd.read_csv("strong_workouts.csv")
body_comp_df = pd.read_csv("exported_body_comp.csv")
```

---

### Transform

Several cleaning and transformation steps are applied to both datasets:

#### 1. Remove Duplicate Records

Duplicate records are removed from each dataset to improve data quality.

#### 2. Remove Unnecessary Columns

The following columns are removed from the **exercise** dataset:

* Distance
* Seconds
* Workout Notes

The following columns are removed from the **body composition** dataset:

* Fat-Free Body Weight
* Subcutaneous Fat
* Visceral Fat
* Skeletal Muscles
* Bone Mass
* Protein

#### 3. Remove Non-Exercise Entries

Rows containing Strong's built-in rest timer entries are removed from the workout dataset.

#### 4. Standardize Date Formatting

Date columns are converted into a consistent datetime format for filtering and future analysis.

#### 5. Filter Training Period

Both datasets are filtered to include only records collected during my twelve-week bulking phase.

**Date Range**

* Start Date: March 16, 2026
* End Date: June 3, 2026

---

## Load

The cleaned datasets are exported as CSV files for future analysis.

### Workout Data

```python
exercise_df.to_csv("cleaned_strong_exercise_data.csv", index = False)
```

### Body Composition Data

```python
body_comp_df.to_csv("cleaned_body_comp.csv", index = False)
```

### Parquet Export

The cleaned workout dataset is also exported to Parquet format for practice working with analytics-friendly storage formats.

```python
exercise_df.to_parquet("cleaned_exercises.parquet", engine = "pyarrow")
```

---

## Technologies Used

* Python
* Pandas
* PyArrow
* CSV
* Parquet
* Git
* GitHub

---

## Skills Demonstrated

### Data Engineering

* ETL Pipeline Development
* Data Cleaning
* Data Transformation
* Data Filtering
* Data Validation
* Data Exporting

### Python

* Functions
* DataFrame Operations
* Datetime Handling
* File Processing

### Data Formats

* CSV
* Parquet

---

## Future Improvements

Potential enhancements include:

* Loading cleaned data into PostgreSQL
* Creating automated ETL workflows
* Building interactive dashboards in Looker Studio
* Tracking strength progression
* Analyzing training frequency by muscle group
* Correlating body composition changes with training performance
* Creating a complete analytics pipeline using SQL and BI tools

---

## Why I Built This Project

As I transition into data engineering, I wanted to build projects using real-world data that I personally generate and understand.

This project allowed me to practice core ETL concepts while working with exercise and body composition data collected during a twelve-week bulk. It demonstrates foundational data engineering skills including extraction, cleaning, transformation, filtering, and exporting data into multiple formats.

The project also establishes a foundation for future analytics and visualization projects focused on fitness performance, training trends, and body composition changes over time.
