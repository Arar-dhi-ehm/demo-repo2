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
        
    Improvements:
        Ambiguous output
            [done] How can the user know what to type?
                - Give an example: Task:MM.DD.YYYY
            [done] Improve the grammatical output
                Hi, there are {days} days remaining to finish {goal}.
            Insert an if else message:
                If the user is 1 hour near deadline. "Are you finished? If not, focus! You can finish it!"
        Handle Errors:
            IndexError
                - if the user entered integer or float it will show this
                    - Please type a valid input format like this 'Gaol:DD.MM.YYYY'
            [done] When user input a space for the date, it shows Error.
                - Try to put as strip for excluding spaces
            ValueError
        Make a while with exit function
        [done] Add current date and deadline
            Show only date not time
        Show calculation of months, weeks, year(if year, use if condition)
        Convert exact date(2022-12-27 14:04:43.335977) into word(December 27, 2022)

    Pros:
        By using this, the user will have an idea on how many days a project should be done.
        The user can assess the risks of a project and will be able to plan ahead of time.
"""

from datetime import datetime

# Input format: task:mm.dd.yyyy
print('\nInput Format: Goal:DD.MM.YYYY\nExample: Learn Python:01.25.2023')
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

# Date Today: and Deadline:
print(f"Date Today: {today_date.date()}\nDeadline: {deadline_date.date()}")

print(f"\nGoal: {goal.strip()}")

#  remaining_time.days will only show the date not the hours.
print(f"\tTime remaining: {remaining_time.days:,} days.")

# Calculate the remaining hours and remove the float by using int casting.
print(f"\tTime remaining: {remaining_hours:,} hours.")

# Calculate the remaining hours with total seconds
print(f"\tTime remaining: {remaining_time.total_seconds() /60 /60:,} hours to be exact.")
