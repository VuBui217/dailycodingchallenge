"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-30
                    Due Date
Given a date string, return the date 9 months in the future.

The given and return strings have the format "YYYY-MM-DD".
If the month nine months into the future doesn't contain the original day number, return the last day of that month.
"""
from datetime import datetime
import calendar
def get_due_date(date_str):
    # Convert date_str to date object
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Add 9 months to the date object
    new_month = (date_object.month - 1 + 9) % 12 + 1
    new_year = date_object.year + (date_object.month - 1 + 9) // 12
    # Check the date future object contain the original day number
    # If so, return that date
    last_day = calendar.monthrange(new_year, new_month)[1] # last day of new month
    if date_object.day <= last_day:
        return f"{new_year}-{new_month:02d}-{date_object.day:02d}"
    # If not, return the last date of the future month
    else:
        return f"{new_year}-{new_month:02d}-{last_day:02d}"

print(get_due_date("2025-03-30")) # should return "2025-12-30".
print(get_due_date("2025-04-27")) # should return "2026-01-27".
print(get_due_date("2025-05-29")) # should return "2026-02-28".
print(get_due_date("2026-06-30")) # should return "2027-03-30".
print(get_due_date("2026-10-11")) # should return "2027-07-11".

