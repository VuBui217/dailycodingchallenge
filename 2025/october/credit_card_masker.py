"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-17

                                        Credit Card Masker
Given a string of credit card numbers, return a masked version of it using the following constraints:

The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
Replace all numbers, except the last four, with an asterisk (*).
Leave the remaining characters unchanged.
For example, given "4012-8888-8888-1881" return "****-****-****-1881".
"""

def mask(card):
    output = []

    n = len(card)

    for i in range(n):
        if i < (n-4):
            if card[i].isdigit():
                output.append('*')
            else:
                output.append(card[i])
        else:
            output.append(card[i])
        print(output)
    return ''.join(output)

def mask1(card):
    output = []
    digit_count = 0

    for ch in reversed(card):
        if ch.isdigit():
            digit_count +=1

            if digit_count <=4:
                output.append(ch)
            else:
                output.append('*')
        else:
            output.append(ch)
    return ''.join(reversed(output))

card ='1234 1111 1111 1111'
print(mask1(card))