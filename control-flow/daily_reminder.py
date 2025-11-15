# daily_reminder.py 
# Prompt the user for a single task
task = input("Enter your task: ")
# Prompt for the task's priority 
priority = input("Enter the priority level (high/medium/low):").lower()
# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()
# use match-case to handle different priorities
match priority:
    case "high":
        reminder = f" '{task}' is a high priority task"
    case "medium":
        reminder = f" '{task}' is a medium priority task"
    case "low":
        reminder = f" '{task}' is a low priority task"
    case _:
        reminder = f" '{task}' has an unspecified priority level"
# use if statement to modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
# Print the customized reminder
print("\nReminder:", reminder)

