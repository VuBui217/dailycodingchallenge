"""
Docstring for 2026.january.nth_fibonacci_number
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-02
                            Nth Fibonacci Number
Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
"""
def nth_fibonacci(n):
    if n <= 2:
        return n - 1
    
    res = 0
    first = 0
    second = 1
    for _ in range(n - 2):
        res = first + second
        first = second
        second = res
    return res
print(nth_fibonacci(4) )   # should return 2.
print(nth_fibonacci(10))   # should return 34.
print(nth_fibonacci(15))   # should return 377.
print(nth_fibonacci(40))   # should return 63245986.
print(nth_fibonacci(75))   # should return 1304969544928657.