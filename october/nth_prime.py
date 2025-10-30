"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-30

Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
"""

def nth_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    num = 2

    while n > 0:
        if is_prime(num):
            n-=1
            print(n, num)
        num+=1

    return num-1

print(nth_prime(5))

"""
num = 2 3 4 5 6 7 8 9 10 11
n = 5 4 3 2 1
"""