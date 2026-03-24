"""
Given a string, return true if the letters can be re-arranged to make a palindrome using every letter. Otherwise, return false.
def isPalindromeAnagram(word):
    pass
"""

def isPalindromeAnagram(word):
    count = {}
    odd_freq = 0

    for ch in word:
        count[ch] = 1 + count.get(ch, 0)

    for _, freq in count.items():
        if freq % 2 == 1:
            odd_freq += 1
        if odd_freq > 1:
            return False
    
    return True