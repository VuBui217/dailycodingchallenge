"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-23

                No Consecutive Repeats
Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.
"""
def has_no_repeats(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True

print(has_no_repeats("hi world")) # should return True.
print(has_no_repeats("hello world")) # should return False.
print(has_no_repeats("abcdefghijklmnopqrstuvwxyz")) # should return True.
print(has_no_repeats("freeCodeCamp")) # should return False.
print(has_no_repeats("The quick brown fox jumped over the lazy dog.")) # should return True.
print(has_no_repeats("Mississippi")) # should return False.