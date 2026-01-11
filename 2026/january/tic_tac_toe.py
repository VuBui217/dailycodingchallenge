"""
Docstring for 2026.january.tic_tac_toe
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-10
                        Tic-Tac-Toe
Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row.
"""
def tic_tac_toe(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return f"{row[0]} wins"
    # Check cols
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            return f"{board[0][c]} wins"
    # Check diagonals
    # d1 = 00 11 22
    # d2 = 20 11 02
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        return f"{board[1][1]} wins"
    return "Draw"
print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]])) # should return "X wins".
print(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]])) # should return "O wins".
print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])) # should return "Draw".
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]])) # should return "O wins".
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]])) # should return "X wins".
print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]])) # should return "Draw".