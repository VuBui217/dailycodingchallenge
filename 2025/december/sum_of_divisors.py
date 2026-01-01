"""
Docstring for december.sum_of_divisors
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-26
                        Sum of Divisors
Given a positive integer, return the sum of all its divisors.

A divisor is any integer that divides the number evenly (the remainder is 0).
Only count each divisor once.
For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.
"""
def sum_divisors(n):
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total
print(sum_divisors(6)   )  # should return 12.
print(sum_divisors(13)  )  # should return 14.
print(sum_divisors(28)  )  # should return 56.
print(sum_divisors(84)  )  # should return 224.
print(sum_divisors(549) )  # should return 806.
print(sum_divisors(9348))  # should return 23520.