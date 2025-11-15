# daily_reminder.py 
# Prompt the user for a single task
Task = input("Enter your task:")
# Prompt for the task's priority 
Priority = input("Priority(high/medium/low):").lower()
# Ask if the task is time-bound
Time_Bound = input("Is it time-bound?(yes/no):").lower()
# use match-case to handle different priorities
match Priority:
    case "high":
        reminder = f" '{Task}' is a high priority task"
    case "medium":
        reminder = f" '{Task}' is a medium priority task"
    case "low":
        reminder = f" '{Task}' is a low priority task"
    case _:
        reminder = f" '{Task}' has an unspecified priority level"
# use if statement to modify reminder if task is time-bound
if Time_Bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
# Print the customized reminder
print(f"Reminder: {reminder}")

