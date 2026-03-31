"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-31
                        Wake-Up Alarm
Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.
Return:

"early" if you woke up before your alarm time.
"on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
"late" if you woke up more than 10 minutes after your alarm time.
Both times are on the same day.
"""
def alarm_check(alarm_time, wake_time):
    alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    wake_hour, wake_minute = map(int, wake_time.split(":"))

    alarm_total = alarm_hour * 60 + alarm_minute
    wake_total = wake_hour * 60 + wake_minute

    diff = wake_total - alarm_total

    if diff < 0:
        return "early"
    elif diff <= 10:
        return "on time"
    else:
        return "late"
    
print(alarm_check("07:00", "06:45")) # should return "early".
print(alarm_check("06:30", "06:30")) # should return "on time".
print(alarm_check("08:10", "08:15")) # should return "on time".
print(alarm_check("09:30", "09:45")) # should return "late".
print(alarm_check("08:15", "08:25")) # should return "on time".
print(alarm_check("05:45", "05:56")) # should return "late".
print(alarm_check("04:30", "04:00")) # should return "early".
    
