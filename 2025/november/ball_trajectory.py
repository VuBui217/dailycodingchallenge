"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-29

                                    Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.
"""
"""
    0 0 0 0             
    0 0 0 0
    0 1 2 0
    0 0 0 0 
    curr = (2, 2)
    prev = (2, 1)
    next = (2, 3)

    0 0 0 0
    0 0 1 0
    0 2 0 0 
    0 0 0 0 

    0 2 0 0
    1 0 0 0
    0 0 0 0 
    0 0 0 0

    0 0 0 0
    0 0 0 0 
    2 0 0 0 
    0 1 0 0

    0 0 0 0 
    0 0 0 0 
    0 0 1 0
    0 0 0 2
    """
def get_next_location(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    prev_row = prev_col = None
    curr_row = curr_col = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                continue
            elif matrix[r][c] == 1:
                prev_row = r
                prev_col = c
            else:
                curr_row = r
                curr_col = c
    # next move direction
    dr = curr_row - prev_row
    dc = curr_col - prev_col

    # next location
    next_row = curr_row + dr
    next_col = curr_col + dc
    if next_row < 0 or next_row >= rows:
        dr = -dr
        next_row = curr_row + dr
    if next_col < 0 or next_col >= cols:
        dc = -dc
        next_col = curr_col + dc
    return [next_row, next_col]


get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) # should return [2, 3].
get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) # should return [3, 0].
get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) # should return [1, 2].
get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) # should return [1, 1].
get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) # should return [2, 2]