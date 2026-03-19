"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-19
                    Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
  ["a", "b"],
  ["a", "a"]
]
Return:

[
  ["b", "a"],
  ["b", "b"]
]
"""
def invert_matrix(matrix):
    values_set = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            values_set.add(matrix[r][c])
            if len(values_set) == 2:
                found = True
                break
        if found:
            break

    val1, val2 = list(values_set)
    values_map = {val1: val2, val2: val1}
    output = []

    for r in range(rows):
        curr = []
        for c in range(cols):
            curr.append(values_map[matrix[r][c]])
        output.append(curr)
    return output

print(invert_matrix([["a", "b"], ["a", "a"]])) # should return [["b", "a"], ["b", "b"]].
print(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]])) # should return [[0, 1, 0], [0, 0, 0], [1, 0, 1]].
print(invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]])) # should return [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]].
print(invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]])) # should return [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]].
print(invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]])) # should return [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]].