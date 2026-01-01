"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-07

Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array.

"""
def find_landing_spot(matrix):
    min_danger = float('inf')
    min_spot = None
    directions= [(-1,0), (1,0), (0,-1), (0,1)] # up, down, left, right
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            
            if matrix[r][c] == 0:
                curr = 0
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        curr+= matrix[nr][nc]
                if curr < min_danger:
                    min_danger = curr
                    min_spot = [r,c]
    return min_spot

print(find_landing_spot([[1, 0], [2, 0]]))