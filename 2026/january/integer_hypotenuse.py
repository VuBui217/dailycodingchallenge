"""
Docstring for 2026.january.integer_hypotenuse
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-16
                        Integer Hypotenuse
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total (a2 + b2 = c2).
"""
def is_integer_hypotenuse(a, b):
    import math
    c = math.sqrt(a ** 2 + b ** 2)
    return c.is_integer()

print(is_integer_hypotenuse(3, 4)     )    # should return True.
print(is_integer_hypotenuse(2, 3)     )    # should return False.
print(is_integer_hypotenuse(5, 12)    )    # should return True.
print(is_integer_hypotenuse(10, 10)   )    # should return False.
print(is_integer_hypotenuse(780, 1040))    # should return True.
print(is_integer_hypotenuse(250, 333) )    # should return False.