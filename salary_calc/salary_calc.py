#this is a program to calculate job salaries
print("Welcome to the Salary Calculator!")
print("""
""")

# Get user input for job title and hourly pay
job_title = input("Hey there! What is the job title you're pursuing? ")
print("""
""")

# Get hourly pay from user
hrly_pay = float(input("What is the hourly pay? $"))
print("""
""")

print("Calculating salary information...")
print("""
""")

print("BAM! In 3, 2, 1...")

# Calculate weekly, bi-weekly, and annual pay
weekly_pay = hrly_pay * 40
biweekly_pay = weekly_pay * 2
annual_pay = weekly_pay * 52
print("""
""")

print(f"Great! Here is the salary information as a {job_title} making ${hrly_pay}/hr. The weekly pay is ${weekly_pay:.2f}, the bi-weekly pay is ${biweekly_pay:.2f}, and the annual pay is ${annual_pay:.2f}!")