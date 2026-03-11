"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-10
                    Array Insertion
Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.
"""
def insert_into_array(arr, value, index):
    return arr[:index] + [value] + arr[index:]

print(insert_into_array([2, 4, 8, 10], 6, 2)) # should return [2, 4, 6, 8, 10].
print(insert_into_array(["the", "quick", "fox"], "brown", 2)) # should return ["the", "quick", "brown", "fox"].
print(insert_into_array([], 0, 0)) # should return [0].
print(insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5)) # should return [0, 1, 1, 2, 3, 5, 8, 13].