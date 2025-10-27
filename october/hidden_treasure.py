"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-24

Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.
Each cell in the 2D array will contain one of the following values:

"-": No treasure.
"O": A part of the treasure that has not been found.
"X": A part of the treasure that has already been found.
If the dive location has no treasure, return "Empty".
If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".
If the dive location finds the last unfound part of the treasure, return "Recovered".
For example, given:

Example Code
[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.
"""

def dive(map, coordinates):
    x, y = coordinates[0], coordinates[1]

    if map[x][y] == '-':
        return 'Empty'
    elif map[x][y] == 'X':
        return 'Found'
    else:
        map[x][y] = 'X'
        for row in map:
            if 'O' in row:
                return 'Found'
        return 'Recovered'
print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]))

print(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))

print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]))