"""
Docstring for 2026.february.2026_winter_game_day_9
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-14
                    2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment
Each direction change adds 15 points (an "L" followed by an "R" or vice versa).
All other curves add 5 points each (all other "L" or "R" characters).
Straight segments add 0 points.
The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200
"""
def get_difficulty(track):
    total = 0
    # for i in range(0, len(track)):
    #     if (i > 0) and ((track[i] == "L" and track[i-1] == "R") or (track[i] == "R" and track[i-1] == "L")):
    #         total += 15
    #     elif track[i] == "S":
    #         continue
    #     else:
    #         total += 5

    prev = None
    for t in track:
        if t in ("L", "R"):
            if prev and prev != t:
                total += 15
            else:
                total += 5
            prev = t
        else:
            prev = None
    if 0 <= total <= 100:
        return "Easy"
    elif 101 <= total <= 200:
        return "Medium"
    else:
        return "Hard"
print(get_difficulty("SLSLLSRRLSRLRL")               ) # should return "Easy".
print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS")    ) # should return "Hard".
print(get_difficulty("SRRRRLSLLRLRSSRLSRL")          ) # should return "Medium".
print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL")) # should return "Hard".
print(get_difficulty("SLLSSLRLSLSLRSLSSLRL")         ) # should return "Medium".
print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR")   ) # should return "Easy".