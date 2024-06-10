mikiCertainly! You can achieve this by writing a Python code that determines the last working day based on the current day of the week. Here's a sample code to do that:

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




@code 4


Sure, you can achieve this in Python by using the `datetime` module. Here's a code snippet that will give you the last working day:

```python
import datetime

def find_last_working_day(today):
    while True:
        today -= datetime.timedelta(days=1)
        if today.weekday() < 5:  # Monday to Friday (0 to 4 are weekdays)
            return today

# Get the current date
current_date = datetime.date(2023, 9, 11)  # Change this to the current date

# Find the last working day
last_working_day = find_last_working_day(current_date)
print("Last working day:", last_working_day)
```

This code defines a function `find_last_working_day` that takes a date and iterates backward until it finds a weekday (Monday to Friday). You can change the `current_date` variable to any date you want, and it will return the last working day for that date.




Certainly! You can use Python to download files using Selenium and check if the downloaded file already exists in a folder. If it doesn't exist, you can proceed with the download. Here's an example of how you can achieve this:

```python
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the folder where you want to save the downloaded files
download_folder = '/path/to/your/download/folder/'

# Set up Chrome WebDriver with download options
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_folder,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': False,
    'safebrowsing.disable_download_protection': True
})

# Initialize the WebDriver
chromedriver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Navigate to the webpage where the file download link is
driver.get('https://example.com')

# Locate and click the download link (you'll need to adjust this based on your webpage)
download_link = driver.find_element(By.XPATH, '//*[@id="downloadButton"]')
download_link.click()

# Wait for the download to complete (you can adjust the timeout as needed)
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="downloadCompleteIndicator"]')))

# List files in the download folder
downloaded_files = os.listdir(download_folder)

# Check if the file you want to download is not already in the folder
file_to_download = 'file_to_download.zip'
if file_to_download not in downloaded_files:
    print(f"Downloading {file_to_download}")
    # Perform the download here

# Close the WebDriver
driver.quit()
```

In this code, replace `'/path/to/your/download/folder/'` with the path to the folder where you want to save the downloaded files, and adjust the URL and element location code to match your specific webpage.

This code first checks if the file you want to download already exists in the specified folder. If it doesn't, it initiates the download. This way, you can avoid downloading duplicate files.



To create a new column in your dataset based on existing columns and apply different logic depending on the values in those columns, you can use a programming language like Python and its popular data manipulation library, pandas. Here's a general outline of the steps you can follow:

1. Import the necessary libraries:
```python
import pandas as pd
```

2. Load your dataset into a pandas DataFrame:
```python
# Replace 'your_dataset.csv' with your dataset file path
df = pd.read_csv('your_dataset.csv')
```

3. Define your logic for the new column. You mentioned two scenarios:
   - Renaming elements based on one column.
   - Applying conditions and fetching information from a third column.

Let's assume you have a DataFrame with columns 'Column1', 'Column2', and 'Column3'. You can create a new column 'NewColumn' like this:

```python
# Define a function to apply custom logic
def custom_logic(row):
    if row['Column1'] == 'ValueToRename':
        return 'NewName'
    elif row['Column2'] == 'SomeCondition' and row['Column3'] > 5:
        return 'Result1'
    else:
        return 'Result2'

# Apply the custom_logic function to create the new column
df['NewColumn'] = df.apply(custom_logic, axis=1)
```

In this example, 'custom_logic' is a function that checks conditions based on 'Column1', 'Column2', and 'Column3' and returns the appropriate value for 'NewColumn'.

4. After applying this logic, your DataFrame will have a new column 'NewColumn' that contains the values based on your specified conditions.

5. You can save the updated DataFrame back to a file if needed:
```python
# Save the DataFrame to a new CSV file
df.to_csv('updated_dataset.csv', index=False)
```

Replace the column names, conditions, and logic in the example above with your actual dataset and requirements. This should give you a starting point to create a new column based on existing columns with custom logic.



To create a new column in a DataFrame using existing columns and apply different logic based on conditions, you can use Python libraries like Pandas. Here's an example of how you can do it:

Assuming you have a DataFrame `df` and want to create a new column `new_column` based on your logic:

```python
import pandas as pd

# Define your logic using conditions
condition1 = (df['column1'] == 'case1')
condition2 = (df['column1'] == 'case2')
condition3 = (df['column1'] == 'case3')
condition4 = (df['column1'] == 'case4') & (df['column4'] == df['column7'])

# Apply logic and assign values to the new column
df.loc[condition1, 'new_column'] = 'value_for_case1'
df.loc[condition2, 'new_column'] = 'value_for_case2'
df.loc[condition3, 'new_column'] = 'value_for_case3'
df.loc[condition4, 'new_column'] = df.loc[condition4, 'column9']

# For cases that don't match any condition, you can set a default value
df['new_column'].fillna('default_value', inplace=True)
```

This code defines four conditions based on the values in `column1`, and for the fourth condition, it checks if `column4` and `column7` are equal. It then assigns values to the new column based on these conditions, with a default value for cases that don't match any condition.

You can adjust the conditions and values as needed for your specific DataFrame and logic.




To modify the query to display the data for the last 6 months, you can use a `UNION ALL` clause to combine the results for each of the past 6 months. Here's the revised query:

```sql
SELECT TO_CHAR(TRUNC(TASK_CREATED_DATE, 'MM'), 'Mon YYYY') AS MONTH,
       COUNT(DISTINCT TASK_NUMBER) AS TASK_COUNT,
       TASK_TYPE
FROM wdm_consumption.VW_GSSC_TASKS_DTL
WHERE TRUNC(TASK_CREATED_DATE) BETWEEN ADD_MONTHS(TRUNC(SYSDATE, 'MM'), -5) AND LAST_DAY(ADD_MONTHS(TRUNC(SYSDATE), -1))
GROUP BY TO_CHAR(TRUNC(TASK_CREATED_DATE, 'MM'), 'Mon YYYY'), TASK_TYPE
ORDER BY MONTH, TASK_TYPE;
```

### Explanation:

1. **TO_CHAR(TRUNC(TASK_CREATED_DATE, 'MM'), 'Mon YYYY')**: This converts the truncated task creation date to a string representing the month and year in the format 'Mon YYYY'.

2. **COUNT(DISTINCT TASK_NUMBER)**: This counts the distinct task numbers.

3. **TRUNC(TASK_CREATED_DATE)**: This truncates the task creation date to remove the time portion, considering only the date.

4. **ADD_MONTHS(TRUNC(SYSDATE, 'MM'), -5)**: This calculates the start date, which is the first day of the month 5 months ago.

5. **LAST_DAY(ADD_MONTHS(TRUNC(SYSDATE), -1))**: This calculates the end date, which is the last day of the previous month.

6. **GROUP BY TO_CHAR(TRUNC(TASK_CREATED_DATE, 'MM'), 'Mon YYYY'), TASK_TYPE**: This groups the results by month and task type.

7. **ORDER BY MONTH, TASK_TYPE**: This orders the results by month and task type.

This query will give you a table with the count of distinct task numbers for each task type for each of the last 6 months.