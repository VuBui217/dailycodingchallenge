"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-15
                    Captured Chess Pieces
Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.

In chess, you start with 16 pieces:

Piece	Abbreviation	Quantity	Value
Pawn	"P"	8	1
Rook	"R"	2	5
Knight	"N"	2	3
Bishop	"B"	2	3
Queen	"Q"	1	9
King	"K"	1	0
The given array will only contain the abbreviations above.
Any of the 16 pieces not included in the given array have been captured.
Return the total value of all captured pieces, unless...
If the King has been captured, return "Checkmate".
"""
def get_captured_value(pieces):
    chess_map = {'P': (8, 1), 'R': (2, 5), 'N': (2, 3), 'B': (2, 3), 'Q': (1, 9), 'K': (1, 0)}

    count = {}

    for p in pieces:
        count[p] = 1 + count.get(p, 0)
    
    if 'K' not in count:
        return 'Checkmate'
    
    total = 0

    for p in chess_map:
        total += (chess_map[p][0] - count.get(p, 0)) * chess_map[p][1]

    return total

print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"])) # should return 8.
print(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"])) # should return 26.
print(get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"])) # should return 16.
print(get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"])) # should return 4.
print(get_captured_value(["P", "K"])) # should return 38.
print(get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"])) # should return 0.
print(get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"])) # should return "Checkmate".