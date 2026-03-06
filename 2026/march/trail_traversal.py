"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-06
                    Trail Traversal
Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

"C": Your current location
"G": Your goal
"T": Traversable parts of the trail
"-": Untraversable parts of the map
Return a string with the moves needed to follow the trail from your location to your goal where:

"R" is a move right
"D" is a move down
"L" is a move left
"U" is a move up
There will always be a single continuous trail, without any branching, from your current location to your goal.
Each trail location will have a maximum of two traversable locations touching it.
For example, given:

[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
Return "RDDRDD".
"""
def navigate_trail(map):
    
    start = [-1, -1]
    rows = len(map)
    cols = len(map[0])

    # Find starting point
    for r in range(rows):
        for c in range(cols):
            if map[r][c] == 'C':
                start = [r, c]
    path = []
    directions = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
    visited = set()
    curr_r, curr_c = start

    while map[curr_r][curr_c] != 'G':
        for move, (r, c) in directions.items():
            next_r, next_c = curr_r + r, curr_c + c
            if 0 <= next_r < rows and 0 <= next_c < cols and (next_r, next_c) not in visited:
                if map[next_r][next_c] in ['T', 'G']:
                    path.append(move)
                    visited.add((curr_r, curr_c))
                    curr_r, curr_c = next_r, next_c
                    break

    return ''.join(path)

print(navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"])) # should return "RDDRDD".
print(navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"])) # should return "RRUUURR".
print(navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"])) # should return "DLDDRRRRD".
print(navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"])) # should return "RRRDDL".
print(navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"])) # should return "ULLLUUURRRRRRDDDR".