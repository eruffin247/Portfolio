#this is a program to calculate job salaries
job_title = input("Hey there! What is the job title you're pursuing? ")
print("""
""")

hrly_pay = float(input("What is the hourly pay? $"))
print("""
""")

print("Calculating salary information...")
print("""
""")

print("BAM! In 3, 2, 1...")

weekly_pay = hrly_pay * 40
biweekly_pay = weekly_pay * 2
annual_pay = weekly_pay * 52
print("""
""")

print(f"Great! Here is the salary information as a {job_title} making ${hrly_pay}/hr. The weekly pay is ${weekly_pay:.2f}, the bi-weekly pay is ${biweekly_pay:.2f}, and the annual pay is ${annual_pay:.2f}!")