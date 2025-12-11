# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculates the date after adding a specified number of days to the current date.
    
    Parameters:
        days_to_add (int): Number of days to add
    
    Returns:
        future_date (datetime.date): Future date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} days will be: {formatted_future_date}")
    return future_date.date()

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    while True:
        try:
            days_input = int(input("Enter the number of days to add: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    future_date = calculate_future_date(days_input)

if __name__ == "__main__":
    main()


