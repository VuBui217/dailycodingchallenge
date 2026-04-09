"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-08
                FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.
"""
def is_fizz_buzz(arr):
    first_int = None
    first_int_idx = None
    for i, num in enumerate(arr):
        if isinstance(num, int):
            first_int = num
            first_int_idx = i
            break
    if first_int is None:
        return False

    n = len(arr)
    min_range = first_int - first_int_idx
    max_range = first_int + n - first_int_idx - 1

    idx = 0

    for num in range(min_range, max_range + 1):
        if num % 15 == 0:
            if arr[idx] == "FizzBuzz":
                idx += 1
                continue
            else:
                return False
        elif num % 3 == 0:
            if arr[idx] == "Fizz":
                idx += 1
                continue
            else:
                return False
        elif num % 5 == 0:
            if arr[idx] == "Buzz":
                idx += 1
                continue
            else:
                return False
        elif num == arr[idx]:
            idx += 1
            continue
        else:
            return False
    return True

print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"])) # should return True.
print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17])) # should return True.
print(is_fizz_buzz([1, 2, "Fizz", 4, 5])) # should return False.
print(is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"])) # should return True.
print(is_fizz_buzz([1, 2, "Fizz", "Buzz", 5])) # should return False.
print(is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103])) # should return False.
print(is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"])) # should return True.