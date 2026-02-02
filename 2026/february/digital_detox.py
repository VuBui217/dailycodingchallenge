"""
Docstring for 2026.february.digital_detox
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-01
                    Digital Detox
Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.
"""
from datetime import datetime, timedelta

def digital_detox(logs):
    if not logs:
        return True

    dts = [datetime.strptime(log, "%Y-%m-%d %H:%M:%S") for log in logs]
    dts.sort()

    four_hours = timedelta(hours=4)

    prev_dt = dts[0]
    current_day = prev_dt.date()
    day_count = 1

    for dt in dts[1:]:
        # Rule 1: any 4-hour window (can cross midnight)
        if dt - prev_dt < four_hours:
            return False

        # Rule 2: max 2 per calendar day
        if dt.date() == current_day:
            day_count += 1
            if day_count > 2:
                return False
        else:
            current_day = dt.date()
            day_count = 1

        prev_dt = dt

    return True

print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"])) # should return True.
print(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"])) # should return False.
print(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"])) # should return True.
print(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"])) # should return False.
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])) # should return True.
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])) # should return False.