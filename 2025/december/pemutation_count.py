"""
Docstring for december.pemutation_count
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-04

                                    Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".
"""
def count_permutations(s):
    import math
    n = len(s)
    count = {}
    for ch in s:
        count[ch] = 1 + count.get(ch, 0)
    result = math.factorial(n)
    for freq in count.values():
        result //= math.factorial(freq)
    return result
print(count_permutations("abb")         )  # should return 3.
print(count_permutations("abc")         )  # should return 6.
print(count_permutations("racecar")     )  # should return 630.
print(count_permutations("freecodecamp"))  # should return 39916800.