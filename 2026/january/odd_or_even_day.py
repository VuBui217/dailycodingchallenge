"""
Docstring for 2026.january.odd_or_even_day
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-27
                    Odd or Even Day
Given a timestamp (number of milliseconds since the Unix epoch), return:

"odd" if the day of the month for that timestamp is odd.
"even" if the day of the month for that timestamp is even.
For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.
"""
def odd_or_even_day(timestamp):
    from datetime import datetime, timezone
    secs = timestamp / 1000
    date = datetime.fromtimestamp(secs, tz = timezone.utc)
    day = date.day

    return "even" if day % 2 == 0 else "odd"

print(odd_or_even_day(1769472000000))  # should return "odd".
print(odd_or_even_day(1769444440000))  # should return "even".
print(odd_or_even_day(6739456780000))  # should return "odd".
print(odd_or_even_day(1)            )  # should return "odd".
print(odd_or_even_day(86400000)     )  # should return "even"