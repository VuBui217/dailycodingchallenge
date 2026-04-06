"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-06
                    What Day Is It?
Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
"""
from datetime import datetime, timezone
def get_day_of_week(timestamp):
    # convert timestamp to seconds
    ts_s = timestamp / 1000

    # Create date object in UTC to ignore time zones
    date_obj = datetime.fromtimestamp(ts_s, tz=timezone.utc)

    return date_obj.strftime("%A")

print(get_day_of_week(1775492249000))  # should return "Monday".
print(get_day_of_week(1766246400000))  # should return "Saturday".
print(get_day_of_week(33791256000000)) # should return "Tuesday".
print(get_day_of_week(1773576000000))  # should return "Sunday".
print(get_day_of_week(0))              # should return "Thursday".