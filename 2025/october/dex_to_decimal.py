"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-11


                                            Hex to Decimal
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

0-9 represent values 0 through 9.
A-F represent values 10 through 15.
Here's a partial conversion table:

Hexadecimal	Decimal
0	0
1	1
...	...
9	9
A	10
...	...
F	15
10	16
...	...
9F	159
A0	160
...	...
FF	255
100	256
The string will only contain characters 0–9 and A–F.
"""

def hex_to_decimal(hex):
    decimal = 0

    hex_dict = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }

    power = 0

    for i in range(len(hex)-1,-1,-1):
        decimal+= hex_dict[hex[i]]* pow(16,power)
        power+=1
    

    return decimal