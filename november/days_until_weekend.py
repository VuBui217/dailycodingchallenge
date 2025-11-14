"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-14

                                    Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.
"""
def days_until_weekend(date_string):
    import datetime
    # Extract yearm month, date
    year, month, date = map(int, date_string.split('-'))
    # Parse input into a date object
    date_obj = datetime.date(year, month, date)
    # Get the date index (Monday = 0, Sunday = 6)
    date_idx = date_obj.weekday()
    
    if date_idx >= 5:
        return "It's the weekend!"
    
    days_left = 5 - date_idx

    unit = "day" if days_left == 1 else "days"

    return f"{days_left} {unit} until the weekend."

print(days_until_weekend("2025-11-14"))        # should return "1 day until the weekend.".
print(days_until_weekend("2025-01-01"))        # should return "3 days until the weekend.".
print(days_until_weekend("2025-12-06"))        # should return "It's the weekend!".
print(days_until_weekend("2026-01-27"))        # should return "4 days until the weekend.".
print(days_until_weekend("2026-09-07"))        # should return "5 days until the weekend.".
print(days_until_weekend("2026-11-29"))        # should return "It's the weekend!"