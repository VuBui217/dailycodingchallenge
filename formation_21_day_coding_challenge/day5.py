"""
Given a rectangular 2D array of integers, return true if all rows and all columns are monotonically increasing. This means that every successive value along all rows and columns must be AT LEAST as large as what came before.
 
Example:
[[0, 0, 0, 1],
 [1, 1, 1, 2],
 [2, 3, 4, 5]]
Returns true but this next one returns false.
[[0, 0, 0, 1],
 [1, 1, 3, 2],
 [2, 3, 4, 5]] 

def isMatrixMonotonic(matrix):
    # /* your code here */
    pass
"""

def isMatrixMonotonic(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Check monotonic for rows
    # for r in range(rows):
    #     for c in range(cols - 1):
    #         if matrix[r][c] > matrix[r][c + 1]:
    #             return False
            
    # Check monotonic for cols
    # for c in range(cols):
    #     for r in range(rows - 1):
    #         if matrix[r][c] > matrix[r + 1][c]:
    #             return False
    
    # This solution is still O(mxn) time complexity 
    # but only using one pass
    for r in range(rows):
        for c in range(cols):
            if r > 0 and matrix[r - 1][c] > matrix[r][c]:
                return False
            if c > 0 and matrix[r][c - 1] > matrix[r][c]:
                return False
    return True

matrix1 =  [[0, 0, 0, 1],
            [1, 1, 1, 2],
            [2, 3, 4, 5]]
matrix2 =  [[0, 0, 0, 1],
            [1, 1, 3, 2],
            [2, 3, 4, 5]] 

print(isMatrixMonotonic(matrix1))
print(isMatrixMonotonic(matrix2))

