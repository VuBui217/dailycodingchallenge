"""
Docstring for december.purge_most_frequent
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-20\
                        Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order.     
"""
def purge_most_frequent(arr):
    from collections import Counter
    arr_count = Counter(arr)
    most_frequent = max(arr_count.values())
    most_frequent_items = {item for item, value in arr_count.items() if value == most_frequent}
    return [item for item in arr if item not in most_frequent_items]
print(purge_most_frequent([1, 2, 2, 3])                                            )   # should return [1, 3].
print(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"])      )   # should return ["a", "b", "b", "c", "c", "c"].
print(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]))   # should return ["red", "green", "red", "green"].
print(purge_most_frequent([5, 5, 5, 5])                                            )   # should return [].