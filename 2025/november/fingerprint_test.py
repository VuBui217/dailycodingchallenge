"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-17

                                            Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.
"""
def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return False
    n = len(fingerprint_a)
    
    diff_count = 0
    for i in range(n):
        if fingerprint_a[i] != fingerprint_b[i]:
            diff_count += 1
    return diff_count <= int(0.1 * n)

print(is_match("helloworld", "helloworld")                                                  )  #should return True.
print(is_match("helloworld", "helloworlds")                                                 )  #should return False.
print(is_match("helloworld", "jelloworld")                                                  )  #should return True.
print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog"))  #should return True.
print(is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog"))  #should return True.
print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat"))  #should return False.