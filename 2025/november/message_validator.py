"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-24

                            Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.
"""

def is_valid_message(message, validation):
    word_list = message.split()
    n = len(validation)

    if n != len(word_list):
        return False
        
    for i in range(n):
        if word_list[i][0].lower() != validation[i].lower():
            return False

    return True

print(is_valid_message("hello world", "hw")                                         )  # should return True.
print(is_valid_message("ALL CAPITAL LETTERS", "acl")                                )  # should return True.
print(is_valid_message("Coding challenge are boring.", "cca")                       )  # should return False.
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") )  # should return True.
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))  # should return False.