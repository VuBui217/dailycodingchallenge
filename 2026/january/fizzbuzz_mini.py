"""
Docstring for 2026.january.fizzbuzz_mini
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-26
                    FizzBuzz Mini
Given an integer, return a string based on the following rules:

If the number is divisible by 3, return "Fizz".
If the number is divisible by 5, return "Buzz".
If the number is divisible by both 3 and 5, return "FizzBuzz".
Otherwise, return the given number as a string.
"""
def fizz_buzz_mini(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
print(fizz_buzz_mini(3) )  # should return "Fizz".
print(fizz_buzz_mini(4) )  # should return "4".
print(fizz_buzz_mini(35))    # should return "Buzz".
print(fizz_buzz_mini(75))    # should return "FizzBuzz".
print(fizz_buzz_mini(98))    # should return "98".