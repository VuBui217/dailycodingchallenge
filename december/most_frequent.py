"""
Docstring for december.most_frequent
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-09

                        Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.
"""
def most_frequent(arr):
    count = {}
    max_count = 0
    max_item = None
    for item in arr:
        count[item] = 1 + count.get(item, 0)
        if count[item] > max_count:
            max_count = count[item]
            max_item = item
    return max_item

print(most_frequent(["a", "b", "a", "c"])                    ) # should return "a".
print(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9])          ) # should return 2.
print(most_frequent([True, False, "False", "True", False])   ) # should return False.
print(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60])) # should return 40.