import tkinter as tk
import us

#window = tk.Tk()
#window.title("Salary Calculator")
#window.geometry("500x300")
#window.configure(bg = "#FFFFFF")

#def user_info():
#    first_name = input("Welcome to the Salary Calculator! What is your first name? ")
#    last_name = input(f"{first_name}")
#    location = input("Where are you located? ")


#first_name = input("Welcome to the Salary Calculator! What is your first name? ")
#last_name = input(f"{first_name}, what is your last name? ")
city = input("Where city are you located in? ")
state = us.states.lookup(input("What state are you located in? "))


def job_info():
    job_title = input(f"Hey there {first_name} What is the job title you're pursuing?")
    hrly_pay = int(input(f"What is the hourly pay for the {job_title} role?"))
    weekly_hrs = int(input("How many hours do you work each week? "))
    weekly_pay = hrly_pay * weekly_hrs
    biweekly_pay = weekly_pay * 2
    annual_pay = weekly_pay * 52

print(f"{city}, {state.abbr}")

#window.mainloop