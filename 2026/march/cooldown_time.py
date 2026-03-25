"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-25

                    Cooldown Time
Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.
"""
def can_retake(finish_time, current_time):
    from datetime import datetime, timedelta
    format_string = "%Y-%m-%dT%H:%M:%S"
    finish_time_object = datetime.strptime(finish_time, format_string)
    current_time_object = datetime.strptime(current_time, format_string)
    diff = current_time_object - finish_time_object
    return diff >= timedelta(hours=48)

print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00")) # should return True.
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00")) # should return False.
print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00")) # should return True.
print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59")) # should return False.