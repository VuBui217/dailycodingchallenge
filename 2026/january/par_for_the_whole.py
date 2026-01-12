"""
Docstring for 2026.january.par_for_the_whole
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-11
                    Par for the Hole
Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

"Hole in one!" if it took one stroke.
"Eagle" if it took two strokes less than par.
"Birdie" if it took one stroke less than par.
"Par" if it took the same number of strokes as par.
"Bogey" if it took one stroke more than par.
"Double bogey" if took two strokes more than par.
"""
def golf_score(par, strokes):
    if strokes == 1:
        return "Hole in one!"
    diff = par - strokes
    if diff == 2:
        return "Eagle"
    elif diff == 1:
        return "Birdie"
    elif diff == 0:
        return "Par"
    elif diff == -1:
        return "Bogey"
    elif diff == -2:
        return "Double bogey"
    else:
        return "Over par"
    
print(golf_score(3, 3)) # should return "Par".
print(golf_score(4, 3)) # should return "Birdie".
print(golf_score(3, 1)) # should return "Hole in one!".
print(golf_score(5, 7)) # should return "Double bogey".
print(golf_score(4, 5)) # should return "Bogey".
print(golf_score(5, 3)) # should return "Eagle"