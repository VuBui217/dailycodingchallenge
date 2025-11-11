"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-11

Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
"""

def count(s):
    low_s = s.lower()
    vow_count = 0
    con_count = 0

    for ch in low_s:
        if ch in "aeiou":
            vow_count += 1
        elif ch.isalpha():
            con_count += 1

    return [vow_count, con_count]