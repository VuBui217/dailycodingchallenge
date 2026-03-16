"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-13
                Parking Fee Calculator
Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
The first string will be the time you parked your car, and the second will be the time you picked it up.
If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:

Each hour parked costs $3.
Partial hours are rounded up to the next full hour.
If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example.
"""
import math
def calculate_parking_fee(park_time, pickup_time):
    cost = 0
    park_h, park_m = map(int, park_time.split(':'))
    pickup_h, pickup_m = map(int, pickup_time.split(':'))
    
    
    park_time_m = park_h * 60 + park_m
    pickup_time_m = pickup_h * 60 + pickup_m

    is_overnight = pickup_time_m < park_time_m

    diff_m = pickup_time_m - park_time_m if not is_overnight else (pickup_time_m + 1440) - park_time_m

    cost = math.ceil(diff_m / 60) * 3 
    cost += 10 if is_overnight else 0
    return f"${cost}" if cost > 5 else "$5"

print(calculate_parking_fee("09:00", "11:00")) # should return "$6".
print(calculate_parking_fee("10:00", "10:30")) # should return "$5".
print(calculate_parking_fee("08:10", "10:45")) # should return "$9".
print(calculate_parking_fee("14:40", "23:10")) # should return "$27".
print(calculate_parking_fee("18:15", "01:30")) # should return "$34".
print(calculate_parking_fee("11:11", "11:10")) # should return "$82".
