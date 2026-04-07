"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-07
                    Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

A palindrome is a string that is the same forward and backward.
If it's not a palindrome, return "none".
"""
def palindrome_locator(s):
    # Check for palindrome
    # if s != s[::-1]:
    #     return "none"
    l = 0 
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return "none"
        l += 1
        r -= 1
        
    mid = len(s) // 2
    return s[mid] if len(s) % 2 == 1 else s[mid-1:mid+1]

print(palindrome_locator("racecar"))       # should return "e".
print(palindrome_locator("level"))         # should return "v".
print(palindrome_locator("freecodecamp"))  # should return "none".
print(palindrome_locator("noon"))          # should return "oo".
print(palindrome_locator("11100111"))      # should return "00".