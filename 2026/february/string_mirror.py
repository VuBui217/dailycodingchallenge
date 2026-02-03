"""
Docstring for 2026.february.string_mirror
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-03
                    String Mirror
Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.
"""
def mirror(s):
    return s + s[::-1]

print(mirror("freeCodeCamp")          )    # should return "freeCodeCamppmaCedoCeerf".
print(mirror("RaceCar")               )    # should return "RaceCarraCecaR".
print(mirror("helloworld")            )    # should return "helloworlddlrowolleh".
print(mirror("The quick brown fox..."))    # should return "The quick brown fox......xof nworb kciuq ehT".