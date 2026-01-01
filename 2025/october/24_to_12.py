"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-13

                                24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
"""
def to_12(time):
    hh_in_24 = int(time[0:2])
    mm_in_24 = time[2:]
    hh_in_12 = 0
    mm_in_12 = mm_in_24
    period = ''

    period = 'AM' if hh_in_24<12 else 'PM'

    if hh_in_24 == 0:
        hh_in_12 = 12
    elif 1<= hh_in_24 <13:
        hh_in_12 = hh_in_24
    else:
        hh_in_12 = hh_in_24 - 12
    return f'{hh_in_12}:{mm_in_12} {period}'

print(to_12("1124"))

print(to_12("0900"))

print(to_12("0030"))