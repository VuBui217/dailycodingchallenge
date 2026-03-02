"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-01
Flattened
Given an array, determine if it is flat.

An array is flat if none of its elements are arrays.
"""
def is_flat(arr):
    for item in arr:
        if isinstance(item, list):
            return False

    return True

print(is_flat([1, 2, 3, 4]))                   # should return True.
print(is_flat([1, [2, 3], 4]))                 # should return False.
print(is_flat([1, 0, False, True, "a", "b"]))  # should return True.
print(is_flat(["a", [0], "b", True]))          # should return False.
print(is_flat([1, [2, [3, [4, [5]]]], 6]))     # should return False.