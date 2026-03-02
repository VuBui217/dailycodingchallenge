"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-02
                    Sum the Letters
Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.
"""
def sum_letters(s):
    return sum((ord(ch.lower()) - ord('a') + 1) if ch.isalpha() else 0 for ch in s)

print(sum_letters("Hello")) # should return 52.
print(sum_letters("freeCodeCamp")) # should return 94.
print(sum_letters("The quick brown fox jumps over the lazy dog.")) # should return 473.
print(sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.")) # should return 1681.
print(sum_letters("</404>")) # should return 0.