"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-05

Matrix Builder
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]
"""

def build_matrix(rows, cols):

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    return matrix