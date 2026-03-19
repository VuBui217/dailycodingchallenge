"""
Given a matrix that is monotonically increasing along all rows and columns, as well as a value, k, 
return true if the value exists in the matrix and false otherwise.
[]function findInMonotonic(matrix, k) {
  /* your code here */
}
"""

# def binary_search(array, k):
#     l = 0
#     r = len(array) - 1

#     while l <= r:
#         mid = l + (r - l) // 2

#         if array[mid] == k:
#             return True
#         elif array[mid] > k:
#             r = mid - 1
#         else:
#             l = mid + 1
#     return False
# def findInMonotonic(matrix, k):
#     for row in matrix:
#         if row[0] <= k <= row[-1] and binary_search(row, k):
#             return True
    
#     return False

# Optimal solution

def findInMonotonic(matrix, k):
    if not matrix:
        return False
    r, c = 0, len(matrix[0]) - 1

    while r < len(matrix) and c >= 0:
        if matrix[r][c] == k:
            return True
        elif matrix[r][c] > k:
            c -= 1
        else:
            r += 1
    return False
matrix1 =  [[0, 0, 0, 1],
            [1, 1, 1, 2],
            [2, 3, 4, 5]]

print(findInMonotonic(matrix1, 6))