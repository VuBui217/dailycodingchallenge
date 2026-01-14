"""
Docstring for 2026.january.odd_or_even
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-13
                        Odd or Even?
Given a positive integer, return "Odd" if it's an odd number, and "Even" if it's even.
"""
def odd_or_even(n):
    return "Even" if n % 2 == 0 else "Odd"

print(odd_or_even(1)        )  # should return "Odd".
print(odd_or_even(2)        )  # should return "Even".
print(odd_or_even(13)       )  # should return "Odd".
print(odd_or_even(196)      )  # should return "Even".
print(odd_or_even(123456789))  # should return "Odd".