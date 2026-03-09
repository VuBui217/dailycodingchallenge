"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-09
                    Array Sum
Given an array of numbers, return the sum of all the numbers.
"""
def sum_array(numbers):

    return sum(numbers)

print(sum_array([1, 2, 3, 4, 5]))                              # should return 15.
print(sum_array([42]))                                         # should return 42.
print(sum_array([5, -2, 7, -3]))                               # should return 7.
print(sum_array([203, 145, -129, 6293, 523, -919, 845, 2434])) # should return 9395.
print(sum_array([0, 0]))                                       # should return 0.