"""
Docstring for 2026.january.is_sorted_array
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-08
                        Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

In ascending order (lowest to highest), return "Ascending".
In descending order (highest to lowest), return "Descending".
Not sorted in ascending or descending order, return "Not sorted".
"""
def is_sorted(arr):
    if len(arr) < 2:
        return "Ascending"
    is_asc = True
    is_des = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            is_asc = False
        if arr[i] > arr[i-1]:
            is_des = False
    
    if is_asc:
        return "Ascending"
    elif is_des:
        return "Descending"
    else:
        return "Not sorted"
    
print(is_sorted([1, 2, 3, 4, 5])                           )  # should return "Ascending".
print(is_sorted([10, 8, 6, 4, 2])                          )  # should return "Descending".
print(is_sorted([1, 3, 2, 4, 5])                           )  # should return "Not sorted".
print(is_sorted([3.14, 2.71, 1.61, 0.57])                  )  # should return "Descending".
print(is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]))  # should return "Ascending".
print(is_sorted([0.4, 0.5, 0.3])                           )  # should return "Not sorted".