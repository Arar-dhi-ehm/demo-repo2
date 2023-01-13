"""
time_till_deadline.py

    Capabilities:
        Countdown App
        Shows time remaining from current day to deadline
        Accept user input of goal and deadline
    Limitations:
        One at a time input
        The program will not save the user input in a list.
            If the user input another goal or task. The program will not remember the previous goal/task.
        Will only show days and hours
"""

from datetime import datetime

# Input format: task:mm.dd.yyyy
print('\nInput Format: Goal:DD.MM.YYYY\nExample: Presentation:02.15.2023')
user_input = input("\nEnter your goal and deadline:  ")
input_list = user_input.split(":")

goal = input_list[0]  # 1st value
deadline = input_list[1]  # 2nd value

# Converts to date format. For parameters check its document
deadline_date = datetime.strptime(deadline.strip(), "%m.%d.%Y")
today_date = datetime.today()

# Calculate days now till deadline
remaining_time = deadline_date - today_date

# Calculate the remaining hours and remove the float by using int casting.
remaining_hours = int(remaining_time.total_seconds() / 60 / 60)

# Date Today and Deadline:
x = today_date; today = x.strftime('%B %d, %Y')
y = deadline_date; convert_deadline = y.strftime('%B %d, %Y')
print(f"Date Today: {today}")
print(f"Deadline: {convert_deadline}")

print(f"\nGoal: {goal.strip()}")

# remaining_time.days will only show the date not the hours.
print(f"\tTime remaining: {remaining_time.days:,} days.")

# Calculate the remaining hours and remove the float by using int casting.
print(f"\tTime remaining: {remaining_hours:,} hours.")

# Calculate the remaining hours with total seconds
print(f"\tTime remaining: {remaining_time.total_seconds() /60 /60:,} hours to be exact.")
