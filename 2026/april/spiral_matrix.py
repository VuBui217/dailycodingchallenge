"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-12
                    Spiral Matrix
Given a 2D matrix, return a flat array with all of its values in clockwise order.

The returned array should have the top-left value first, move right along the top row, then down the right column, then left along the bottom row, then up the left column. Repeat inward for any remaining layers.

For example, given:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Return [1, 2, 3, 6, 9, 8, 7, 4, 5].
"""
def spiral_matrix(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    output = []
    while top <= bottom and left <= right:
        # top left to right
        for c in range(left, right + 1):
            output.append(matrix[top][c])
        top += 1
        # right top to bottom
        for r in range(top, bottom + 1):
            output.append(matrix[r][right])
        right -= 1
        # bottom right to left
        if top <= bottom:
            for c in range(right, left - 1, -1):
                output.append(matrix[bottom][c])
            bottom -= 1
        # left bottom to top
        if left <= right:
            for r in range(bottom, top - 1, -1):
                output.append(matrix[r][left])
            left += 1
    return output

print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # should return [1, 2, 3, 6, 9, 8, 7, 4, 5].
print(spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]])) # should return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"].
print(spiral_matrix([[True, False, False], [False, True, True], [False, True, False], [True, True, False]])) # should return [True, False, False, True, False, False, True, True, False, False, True, True].
print(spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]])) # should return [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1].