"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-05
                    Smallest Gap
Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).

There will always be at least one pair of matching characters.
The returned substring should exclude the matching characters.
If two or more gaps are the same length, return the characters from the first one.
For example, given "ABCDAC", return "DA".

Only "A" and "C" repeat in the string.
The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
So return the string between the two "C" characters.
"""
def smallest_gap(s):
    min_len = float(float('infinity'))
    res_str = [-1, -1]
    
    # Brute force
    # for l in range(len(s) - 1):
    #     for r in range(l + 1, len(s)):
    #         if s[r] == s[l] and (r - l + 1) < min_len:
    #             min_len = r - l + 1
    #             res_str = [l, r]
    # l, r = res_str
    # return s[l+1:r]

    # Optimal solution
    # Using a hashmap to store the the character and its index that last time we've seen it in s. If we encounter a character in hashmap, we will process the gap, and update the index for that charater

    last_seen = {}

    for i, ch in enumerate(s):
        if ch in last_seen:
            if i - last_seen[ch] + 1 < min_len:
                min_len = i - last_seen[ch] + 1
                res_str = [last_seen[ch], i]
        last_seen[ch] = i
    l, r = res_str
    return s[l+1:r]

print(smallest_gap("ABCDAC")) # should return "DA".
print(smallest_gap("racecar")) # should return "e".
print(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4")) # should return "#q6e&rkf(p".
print(smallest_gap("Hello World")) # should return "".
print(smallest_gap("The quick brown fox jumps over the lazy dog.")) # should return "fox".
