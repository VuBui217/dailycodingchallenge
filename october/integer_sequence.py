"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-27

Integer Sequence
Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

For example, given 5, return "12345".
"""

def sequence(n):

    return ''.join(str(num) for num in range(1,n+1,1))


print(sequence(5))