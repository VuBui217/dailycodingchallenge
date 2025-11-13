"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-13

                                        Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
"""
def shift_array(arr, n):
    shift_steps = n % len(arr)
    return arr[shift_steps:] + arr[:shift_steps]
    

print(shift_array([1,2,3], 1))

# arr = [1,2,3]
# print(arr[-1])
# print(arr[-2])
# print(arr[-3])
# print(-1%3)