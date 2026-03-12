"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-12
                    Domino Chain Validator
Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
For the chain to be valid, the second number of each domino must match the first number of the next domino.
The first number of the first domino and the last number of the last domino don't need to match anything.
"""
def is_valid_domino_chain(dominoes):
    for i in range(1, len(dominoes)):
        if dominoes[i][0] != dominoes[i-1][-1]:
            return False
    return True

print(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]])) # should return True.
print(is_valid_domino_chain([[6, 2], [3, 4], [4, 1]])) # should return False.
print(is_valid_domino_chain([[2, 5], [5, 6], [5, 1]])) # should return False.
print(is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]])) # should return True.
print(is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]])) # should return False.