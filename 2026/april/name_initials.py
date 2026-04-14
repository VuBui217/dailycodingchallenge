"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-13
                Name Initials
Given a full name as a string, return their initials.

Names to initialize are separated by a space.
Initials should be made uppercase.
Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.".
"""
def get_initials(name):
    return ".".join(word[0].upper() for word in name.split()) + "."
    
print(get_initials("Tommy Millwood")) # should return "T.M.".
print(get_initials("Savanna Puddlesplash")) # should return "S.P.".
print(get_initials("Frances Cowell Conrad")) # should return "F.C.C.".
print(get_initials("Dragon")) # should return "D.".
print(get_initials("Dorothy Vera Clump Haverstock Norris")) # should return "D.V.C.H.N.".