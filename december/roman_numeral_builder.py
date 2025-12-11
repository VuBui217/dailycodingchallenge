"""
Docstring for december.roman_numeral_builder
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-11
                                Roman Numeral Builder
Given an integer, return its equivalent value in Roman numerals.
Roman numerals use these symbols:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are written from largest to smallest, left to right using the following rules:

Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a symbol more than three times in a row. So the largest number you can write is 3999.
Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).
"""
def to_roman(num):
    digits = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    output = []
    for symbol, val in digits.items():
        if val > num:
            continue
        count = num // val
        output.append(symbol * count)
        num = num % val
    return "".join(output)

print(to_roman(18)  )  # should return "XVIII".
print(to_roman(19)  )  # should return "XIX".
print(to_roman(1464))  # should return "MCDLXIV".
print(to_roman(2025))  # should return "MMXXV".
print(to_roman(3999))  # should return "MMMCMXCIX".