"""
Docstring for december.game_of_life
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-13
                                        Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
"""
def is_live_cell(curr_pos, grid, direction):
    r, c = curr_pos
    dr, dc = direction
    nr, nc = r + dr, c + dc

    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
        return False

    return grid[nr][nc] == 1
def game_of_life(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                directions.append((i, j))
    prev = [row[:] for row in grid] # The output is based on the orginal map, not based on the updated map after updating cell -> we need a snap shot of the original one
    for r in range(rows):
        for c in range(cols):
            curr_pos = (r, c)
            live_cell_count = sum([1 if is_live_cell(curr_pos, prev, direction) else 0 for direction in directions])
            if grid[r][c] == 1:
                grid[r][c] = 0 if live_cell_count < 2 or live_cell_count > 3 else 1
            else:
                grid[r][c] = 1 if live_cell_count == 3 else 0
    return grid

print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]])) # should return [[0, 1, 1], [0, 0, 1], [1, 1, 1]].
print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]])) # should return [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]].
print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]])) # should return [[0, 0, 0], [0, 1, 0], [0, 0, 0]].
print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]])) # should return [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]].