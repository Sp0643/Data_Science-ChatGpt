Certainly! You can achieve this by writing a Python code that determines the last working day based on the current day of the week. Here's a sample code to do that:

```python
import datetime

# Get the current date
current_date = datetime.datetime.now()

# Calculate the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
day_of_week = current_date.weekday()

# Define a dictionary to map days of the week to their respective previous working days
working_days = {
    0: 4,  # Monday maps to Friday
    1: 0,  # Tuesday maps to Monday
    2: 1,  # Wednesday maps to Tuesday
    3: 2,  # Thursday maps to Wednesday
    4: 3,  # Friday maps to Thursday
    5: 4,  # Saturday maps to Friday
    6: 4   # Sunday maps to Friday
}

# Get the last working day based on the current day
last_working_day = current_date - datetime.timedelta(days=day_of_week - working_days[day_of_week])

# Print the last working day
print("Last working day is:", last_working_day.strftime("%A"))
```

This code first calculates the current day of the week (0 for Monday, 1 for Tuesday, etc.) and then uses a dictionary to map each day to its corresponding previous working day. Finally, it calculates and prints the last working day based on the current day. can create a Python function to select the last working date (Monday to Friday) by checking the current date and going back in time until a working day is found. Here's a sample function that does this:

```python
import datetime

def last_working_date():
    today = datetime.date.today()
    while today.weekday() > 4:  # Check if it's Saturday or Sunday (0 = Monday, 6 = Sunday)
        today -= datetime.timedelta(days=1)  # Go back one day
    return today

# Test the function
last_work_day = last_working_date()
print("Last working date:", last_work_day)
```

This function uses the `datetime` module to get the current date and then subtracts days from it until it finds a weekday (Monday to Friday). It stops when it finds the last working day and returns that date.

Keep in mind that this code assumes a standard working week from Monday to Friday. If your workweek is different, you may need to adjust the code accordingly.




@code 3



I understand your requirement now. You want to find the date of the last Friday regardless of the current day of the week. Here's a Python code that does that:

```python
import datetime

# Get the current date
current_date = datetime.datetime.now()

# Calculate the days to subtract to get to the last Friday (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
days_to_subtract = (current_date.weekday() - 4) % 7

# Calculate the last Friday's date
last_friday = current_date - datetime.timedelta(days=days_to_subtract)

# Print the date of the last Friday
print("Date of the last Friday:", last_friday.strftime("%Y-%m-%d"))
```

This code calculates the number of days to subtract from the current date to reach the last Friday and then calculates the date of the last Friday accordingly.

