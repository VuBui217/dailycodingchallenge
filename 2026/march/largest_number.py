"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-18
                    Largest Number
Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").
"""
def largest_number(s):
    res = float('-inf')
    l = 0
    s = s + '!'

    for r in range(len(s)):
        if s[r] in [',', '!', '?', ':', ';']:
            res = max(res, float(s[l:r]))
            l = r + 1
    return res

print(largest_number("1,2")) # should return 2.
print(largest_number("4;15:60,26?52!0")) # should return 60.
print(largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011")) # should return -402.
print(largest_number("12;-50,99.9,49.1!-10.1?88?16")) # should return 99.9.