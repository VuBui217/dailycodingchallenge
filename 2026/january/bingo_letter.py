"""
Docstring for 2026.january.bingo_letter
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-24
                        Bingo! Letter
Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:

Letter	Number Range
"B"	    1-15
"I"	    16-30
"N"	    31-45
"G"	    46-60
"O"	    61-75
"""
def get_bingo_letter(n):
    if 1 <= n <= 15:
        return "B"
    elif 16 <= n <= 30:
        return "I"
    elif 31 <= n <= 45:
        return "N"
    elif 46 <= n <= 60:
        return "G"
    elif 61 <= n <= 75:
        return "O"
    else:
        return "Invalid input"
print(get_bingo_letter(75)) # should return "O".
print(get_bingo_letter(54)) # should return "G".
print(get_bingo_letter(25)) # should return "I".
print(get_bingo_letter(38)) # should return "N".
print(get_bingo_letter(11)) # should return "11".