"""
A Toeplitz Matrix is one where the values on every diagonal are the same: Given a 2d matrix (multidimensional array), return true if the input is a Toeplitz matrix and false otherwise.
 
Example of a valid Toeplitz matrix:
1 2 3 4
5 1 2 3
6 5 1 2
7 6 5 1
function isToeplitz(m) {
  /* your code here */
}
"""
def isToeplitz(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows-1):
        for c in range(cols-1):
            if matrix[r][c] != matrix[r+1][c+1]:
                return False
    return True
