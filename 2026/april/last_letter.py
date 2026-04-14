"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-14
                    Last Letter
Given a string, return the letter from the string that appears last in the alphabet.

If two or more letters tie for the last in the alphabet, return the first one.
Ignore all non-letter characters.
"""
def get_last_letter(s):
    output = None

    for ch in s:
        if ch.isalpha():
            if output is None or ch.lower() > output.lower():
                output = ch
    return output

print(get_last_letter("world")) # should return "w".
print(get_last_letter("Hello World")) # should return "W".
print(get_last_letter("The quick brown fox jumped over the lazy dog.")) # should return "z".
print(get_last_letter("HeLl0")) # should return "L".
print(get_last_letter("!#$ er@R asd fT.,> 2t0e9")) # should return "T".