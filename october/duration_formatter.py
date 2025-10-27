"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-26

                                Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.
"""

def format(seconds):
    """
    1 hour = 3600 seconds
    1 min = 60 seconds

    1 second = 1/60 minutes = 1/3600 hour

    """
    
    hh = seconds // 3600
    mm = (seconds % 3600) // 60
    ss = seconds % 60

    ss_str = f"{ss:02}"

    if hh > 0:
        mm_str = str(mm) if mm > 9 else '0' + str(mm)
        return f"{hh}:{mm_str}:{ss_str}"
    else:
        return f"{mm}:{ss_str}"

print(format(500))  # should return "8:20"
print(format(4000)) # should return "1:06:40"