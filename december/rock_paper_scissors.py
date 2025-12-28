"""
Docstring for december.rock_paper_scissors
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-27
                        Rock, Paper, Scissors
Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

The input strings will always be "Rock", "Paper", or "Scissors".
"Rock" beats "Scissors".
"Paper" beats "Rock".
"Scissors" beats "Paper".
Return:

"Player 1 wins" if Player 1 wins.
"Player 2 wins" if Player 2 wins.
"Tie" if both players choose the same option.
"""
def rock_paper_scissors(player1, player2):
    win_set = {("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")}
    if player1 == player2:
        return "Tie"
    elif (player1, player2) in win_set:
        return "Player 1 wins"
    else:
        return "Player 2 wins"
print(rock_paper_scissors("Rock", "Rock")        ) # should return "Tie".
print(rock_paper_scissors("Rock", "Paper")       ) # should return "Player 2 wins".
print(rock_paper_scissors("Scissors", "Paper")   ) # should return "Player 1 wins".
print(rock_paper_scissors("Rock", "Scissors")    ) # should return "Player 1 wins".
print(rock_paper_scissors("Scissors", "Scissors")) # should return "Tie".
print(rock_paper_scissors("Scissors", "Rock")    ) # should return "Player 2 wins".