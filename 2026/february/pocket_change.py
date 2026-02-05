"""
Docstring for 2026.february.pocket_change
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-05
                    Pocket Change
Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".

100 cents equals 1 dollar.
In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents.
"""
def count_change(change):
    total = sum(change)
    d = total // 100
    cc = total % 100
    
    return f"{d}:{cc:02d}"

print(count_change([25, 10, 5, 1])                             )   # should return "$0.41".
print(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]))   # should return "$1.43".
print(count_change([100, 25, 100, 1000, 5, 500, 2000, 25])     )   # should return "$37.55".
print(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10])      )   # should return "$0.70".
print(count_change([1])                                        )   # should return "$0.01".
print(count_change([25, 25, 25, 25])                           )   # should return "$1.00".