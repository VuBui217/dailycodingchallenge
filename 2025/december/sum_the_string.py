"""
Docstring for december.sum_the_string
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-30
                                Sum the String
Given a string containing digits and other characters, return the sum of all numbers in the string.

Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
Ignore any non-digit characters.
"""
def string_sum(s):
    total = 0
    curr = 0
    for i in range(len(s)):
        if s[i].isdigit():
            curr = curr * 10 + (ord(s[i]) - ord("0"))
        else:
            total += curr
            curr = 0
    total += curr
    return total

print(string_sum("3apples2bananas")                        )   # should return 5.
print(string_sum("10cats5dogs2birds")                      )   # should return 17.
print(string_sum("125344")                                 )   # should return 125344.
print(string_sum("a1b20c300")                              )   # should return 321.
print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))   # should return 1653.