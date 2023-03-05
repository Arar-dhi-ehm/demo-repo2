from datetime import datetime

# Input format: task:mm.dd.yyyy
print('\nInput Format: Goal:DD.MM.YYYY\nExample: Presentation:02.15.2023')
user_input = input("\nEnter your goal and deadline: ")
input_list = user_input.split(":")

goal = input_list[0].strip()  # 1st value
deadline = input_list[1].strip()  # 2nd value

# Converts to date format. For parameters check its document
deadline_date = datetime.strptime(deadline, "%m.%d.%Y")
today_date = datetime.today()

# Calculate days now till deadline
remaining_time = deadline_date - today_date

# Calculate the remaining hours and remove the float by using int casting.
remaining_hours = int(remaining_time.total_seconds() / 60 / 60)

# Date Today and Deadline:
today = today_date.strftime('%B %d, %Y')
convert_deadline = deadline_date.strftime('%B %d, %Y')
print(f"Date Today: {today}")
print(f"Deadline: {convert_deadline}")

print(f"\nGoal: {goal}")

# remaining_time.days will only show the date not the hours.
print(f"\tTime remaining: {remaining_time.days:,} days.")

# Calculate the remaining hours and remove the float by using int casting.
print(f"\tTime remaining: {remaining_hours:,} hours.")

# Calculate the remaining hours with total seconds
print(
    f"\tTime remaining: {remaining_time.total_seconds() / 60 / 60:,} hours to be exact.")
