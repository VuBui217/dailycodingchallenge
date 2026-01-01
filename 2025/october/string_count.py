"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-14

String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
"""



def count(text, parameter):
    count = 0
    n = len(text)
    k = len(parameter)

    if k>n:
        return count
    
    for i in range(n-k+1):
        curr = text[i:i+k]
        if curr == parameter:
            count+=1
    return count