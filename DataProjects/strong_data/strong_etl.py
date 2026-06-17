# Writing an ETL pipeline to transform my exported exercise/health data from my Strong app.
import pandas as pd

# ====================
# EXTRACT
# ====================

exercise_df = pd.read_csv("exported_strong_sessions.csv")    # Exported CSV file containing training data
bodycomp_df = pd.read_csv("exported_body_comp.csv")  # Exported CSV file containing body composition data

print(exercise_df.info)
print()
print(bodycomp_df.info)
print()

# ====================
# TRANSFORM
# ====================

# Changing the name of the Time column to Date
bodycomp_df = bodycomp_df.rename(columns= {"Time" : "Date"})

# Removing duplicates
def remove_duplicates(df):
    return df.drop_duplicates()

exercise_df = remove_duplicates(exercise_df)
bodycomp_df = remove_duplicates(bodycomp_df)

# Removing Distance, Seconds, and Workout Notes columns from exported_strong_sessions.csv
# Removing Fat-Free Body Weight, Subcutaneous Fat, Visceral Fat, Skeletal Muscles, Bone Mass, and Protein columns from exported_body_comp.csv
# Removing rows that contain "Rest Timer" from exported_strong_sessions.csv
exercise_df = exercise_df.drop(columns = ["Distance", "Seconds", "Workout Notes"])
bodycomp_df = bodycomp_df.drop(columns = ["Fat-Free Body Weight", "Subcutaneous Fat", "Visceral Fat", "Skeletal Muscles", "Bone Mass", "Protein"])
exercise_df = exercise_df[exercise_df["Set Order"] != "Rest Timer"]

# Formatting and removing data before 3/18/26, the day I started my twelve week bulk
def date_format(df):
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    return df

exercise_df = date_format(exercise_df)
bodycomp_df = date_format(bodycomp_df)

def date_filter(df):
    df["Date"] = pd.to_datetime(df["Date"])

    start_date = "2026-03-16" # The start date of my twelve week bulk.
    end_date = "2026-06-03" # The end date of my twelve week bulk.

    df = df[df["Date"].between(start_date, end_date)]
    return df

exercise_df = date_filter(exercise_df)
bodyfat_df = date_filter(bodycomp_df)

# ====================
# LOAD
# ====================

exercise_df.to_csv("cleaned_strong_sessions.csv", index = False)
bodycomp_df.to_csv("cleaned_body_comp.csv", index = False)

# Making a Parquet file for practice
exercise_df.to_parquet("cleaned_exercises.parquet", engine = "pyarrow")

print(exercise_df.shape)
print()
print(bodycomp_df.shape)
print()

print("#########################")
print("PIPELINE IS COMPLETE!")
print("#########################")