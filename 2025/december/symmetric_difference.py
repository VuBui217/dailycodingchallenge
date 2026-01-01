"""
Docstring for december.symmetric_difference
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-05
                        Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.
"""
def difference(arr1, arr2):
    output = []
    arr1_set = set(arr1)
    arr2_set = set(arr2)
    for num in arr1:
        if num not in arr2_set:
            output.append(num)
    for num in arr2:
        if num not in arr1_set:
            output.append(num)
    return output
print(difference([1, 2, 3], [3, 4, 5])                        )   # should return [1, 2, 4, 5].
print(difference(["a", "b"], ["c", "b"])                      )   # should return ["a", "c"].
print(difference([1, "a", 2], [2, "b", "a"])                  )   # should return [1, "b"].
print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))   # should return [2, 4, 6, 8].