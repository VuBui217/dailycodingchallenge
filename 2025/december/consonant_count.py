"""
Docstring for december.consonant_count
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-16
                        Consonant Count
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.
"""
def has_consonant_count(text, target):
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in "aeiou":
            count += 1
    return count == target

print(has_consonant_count("helloworld", 7)                                   ) # should return True.
print(has_consonant_count("eieio", 5)                                        ) # should return False.
print(has_consonant_count("freeCodeCamp Rocks!", 11)                         ) # should return True.
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24)) # should return False.
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23)) # should return True.