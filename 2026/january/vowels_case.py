"""
Docstring for 2026.january.vowels_case
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-06
                        vOwElcAsE
Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

Vowels are "a", "e", "i", "o", and "u" in any case.
Non-alphabetical characters should remain unchanged.
"""
def vowel_case(s):
    lower_s = s.lower()
    output = []
    for ch in lower_s:
        if ch in ["a", "e", "i", "o", "u"]:
            output.append(ch.upper())
        else:
            output.append(ch)
    return "".join(output)
print(vowel_case("vowelcase")      )   # should return "vOwElcAsE".
print(vowel_case("coding is fun")  )   # should return "cOdIng Is fUn".
print(vowel_case("HELLO, world!")  )   # should return "hEllO, wOrld!".
print(vowel_case("git cherry-pick"))   # should return "gIt chErry-pIck".
print(vowel_case("HEAD~1")         )   # should return "hEAd~1".
