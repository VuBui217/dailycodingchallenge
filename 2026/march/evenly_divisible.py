"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-16
Evenly Divisible
Given two integers, determine if you can evenly divide the first one by the second one.
"""
def is_evenly_divisible(a, b):

    return b != 0 and a % b == 0

print(is_evenly_divisible(4, 2))       # should return True.
print(is_evenly_divisible(7, 3))       # should return False.
print(is_evenly_divisible(5, 10))      # should return False.
print(is_evenly_divisible(48, 6))      # should return True.
print(is_evenly_divisible(3186, 9))    # should return True.
print(is_evenly_divisible(4192, 11))   # should return False.
print(is_evenly_divisible(2, 0))       # should return False.