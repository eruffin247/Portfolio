import pandas as pd

# Where to load data
tax_df = pd.read_csv("tax_data.csv")

# This is a program to calculate job salaries
print("Welcome to the Salary Calculator! What is your name?")
print("""
""")

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("""
""")


# Get user input for job title and hourly pay
job_title = input(f"Hey there {first_name}! What is the job title you're pursuing? ")
hrly_pay = float(input("What is the hourly pay? $"))
print("""
""")

# Get filing status and state of residency
filing_status = input("What is your filing status? ")
state_code = input("What state do you reside in? ")
print("""
""")

# Calculate weekly, bi-weekly, and annual pay
weekly_pay = hrly_pay * 40
biweekly_pay = weekly_pay * 2
annual_pay = weekly_pay * 52

federal_table = tax_df[
    (tax_df["tax_type"] == "federal") &
    (tax_df["filing_status"] == filing_status)
]

state_table = tax_df[
    (tax_df["tax_type"] == "state") &
    (tax_df["state"] == state_code)
]

print("Calculating salary information...")
print("""
""")

print("BAM! In 3, 2, 1...")
print("""
""")

print(f"Great! Here is the salary information as a {job_title} making ${hrly_pay}/hr. The weekly pay is ${weekly_pay:.2f}, the bi-weekly pay is ${biweekly_pay:.2f}, and the annual pay is ${annual_pay:.2f}!")