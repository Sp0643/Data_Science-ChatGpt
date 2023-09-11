You can create a Python function to select the last working date (Monday to Friday) by checking the current date and going back in time until a working day is found. Here's a sample function that does this:

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
