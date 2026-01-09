"""
Docstring for 2026.january.circular_prime
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-09
                        Circular Prime
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.             
"""
def rotate(n):
    output = []
    digits = list(str(n))
    for i in range(len(digits)):
        curr = digits[i:] + digits[:i]
        output.append(int("".join(curr)))
    return output

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_circular_prime(n):
    rotations = rotate(n)
    for num in rotations:
        if is_prime(num):
            continue
        else:
            return False
    return True
print(is_circular_prime(197) ) # should return True.
print(is_circular_prime(23)  ) # should return False.
print(is_circular_prime(13)  ) # should return True.
print(is_circular_prime(89)  ) # should return False.
print(is_circular_prime(1193)) # should return True.