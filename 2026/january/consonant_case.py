"""
Docstring for 2026.january.consonant_case
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-20
                        Consonant Case
Given a string representing a variable name, convert it to consonant case using the following rules:

All consonants should be converted to uppercase.
All vowels (a, e, i, o, u in any case) should be converted to lowercase.
All hyphens (-) should be converted to underscores (_).
"""
def to_consonant_case(s):
    output = []

    for ch in s:
        if ch.lower() in ["a", "e", "i", "o", "u"]:
            output.append(ch.lower())
        elif ch == "-":
            output.append("_")
        else:
            output.append(ch.upper())
        
    return "".join(output)

print(to_consonant_case("helloworld")                            ) # should return "HeLLoWoRLD".
print(to_consonant_case("HELLOWORLD")                            ) # should return "HeLLoWoRLD".
print(to_consonant_case("_hElLO-WOrlD-")                         ) # should return "_HeLLo_WoRLD_".
print(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_")) # should return "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_".