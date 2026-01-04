"""
Docstring for 2026.january.leap_year_calculator
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-04
                    Leap Year Calculator
Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

The year is evenly divisible by 4, and
The year is not evenly divisible by 100, unless
The year is evenly divisible by 400.
"""
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
print(is_leap_year(2024)) # should return True.
print(is_leap_year(2023)) # should return False.
print(is_leap_year(2100)) # should return False.
print(is_leap_year(2000)) # should return True.
print(is_leap_year(1999)) # should return False.
print(is_leap_year(2040)) # should return True.
print(is_leap_year(2026)) # should return False.