"""
Given a 2D rectangular matrix, return all of the values in a single, linear array in spiral order. Start at (0, 0) and first include everything in the first row. Then down the last column, back the last row (in reverse), and finally up the first column before turning right and continuing into the interior of the matrix.
 
For example:
 1  2  3  4
 5  6  7  8
 9 10 11 12
 13 14 15 16
Returns:
 
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
function spiralTraversal(matrix) {
  /* your code here */
}
"""
"""
Scratch

1 2 3 4 (0, 1)
c == cols - 1
Change direction
8 12 16 (1, 0)
r == rows - 1
Change direction
15 14 13 (0, -1)
c == 0
change direction
9 5
"""
def spiralTraversal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    output = []

    while top <= bottom and left <= right:
        #Top: left to right
        for i in range(left, right + 1):
            output.append(matrix[top][i])
        top += 1
        #Right: top to bottom
        for i in range(top, bottom + 1):
            output.append(matrix[i][right])
        right -= 1

        #Bottom: right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                output.append(matrix[bottom][i])
            bottom -= 1
        #Left: bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
    return output

matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[1, 2, 3, 4]]
print(spiralTraversal(matrix1))
print(spiralTraversal(matrix2))

