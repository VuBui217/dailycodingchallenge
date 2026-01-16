"""
Docstring for 2026.january.arr_swap
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-15
                Array Swap
Given an array with two values, return an array with the values swapped.
For example, given ["A", "B"] return ["B", "A"].
"""
def array_swap(arr):
    return arr[::-1]

print(array_swap(["A", "B"])   )   # should return ["B", "A"].
print(array_swap([25, 20])     )   # should return [20, 25].
print(array_swap([True, False]))   # should return [False, True].
print(array_swap(["1", 1])     )   # should return [1, "1"].