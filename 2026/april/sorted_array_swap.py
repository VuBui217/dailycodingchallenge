"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-15
                    Sorted Array Swap
Given an array of integers, return a new array using the following rules:

Sort the integers in ascending order
Then swap all values whose index is a multiple of 3 with the value before it.
"""
def sort_and_swap(arr):
    output = sorted(arr)

    for i in range(1, len(output)):
        if i % 3 == 0:
            output[i], output[i-1] = output[i-1], output[i]
    return output

print(sort_and_swap([3, 1, 2, 4, 6, 5])) # should return [1, 2, 4, 3, 5, 6].
print(sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8])) # should return [1, 2, 4, 3, 5, 7, 6, 8, 9].
print(sort_and_swap([1, 2, 3, 4, 5, 6, 7, 8, 9])) # should return [1, 2, 4, 3, 5, 7, 6, 8, 9].
print(sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11])) # should return [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12].
print(sort_and_swap([100, -50, 0, 75, -25, 50, -75, 25])) # should return [-75, -50, 0, -25, 25, 75, 50, 100].
print(sort_and_swap([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2])) # should return [-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313].

