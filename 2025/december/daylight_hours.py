"""
Docstring for december.daylight_hours
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-21
                            Daylight Hours
December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.

Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:

Latitude	Daylight Hours
-90	        24
-75	        23
-60	        21
-45	        15
-30	        13
-15	        12
0	        12
15	        11
30	        10
45	        9
60	        6
75	        2
90	        0
If the given latitude does not exactly match a table entry, use the value of the closest latitude.
"""
def daylight_hours(latitude):
    table = [(-90, 24), (-75, 23), (-60, 21), (-45, 15), (-30, 13), (-15, 12), (0, 12), (15, 11), (30, 10), (45, 9), (60, 6), (75, 2), (90, 0)]
    left = 0
    right = len(table) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if latitude == table[mid][0]:
            return table[mid][1]
        if latitude > table[mid][0]:
            left = mid + 1
        else:
            right = mid - 1
    l1, h1 = table[left]
    l2, h2 = table[right]

    if abs(latitude - l1) < abs(latitude - l2):
        return h1
    else:
        return h2
print(daylight_hours(45) ) # should return 9.
print(daylight_hours(0)  ) # should return 12.
print(daylight_hours(-90)) # should return 24.
print(daylight_hours(-10)) # should return 12.
print(daylight_hours(23) ) # should return 10.
print(daylight_hours(88) ) # should return 0.
print(daylight_hours(-33)) # should return 13.
print(daylight_hours(70) ) # should return 2.