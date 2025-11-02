"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-01

                                            Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:
"""

# def verify(message, key, signature):
#     computed_signature = 0
#     for ch in message:
#         if ch.isalpha():
#             computed_signature += ord(ch) - ord('A') + 1 if ch.isupper() else ord(ch) - ord('a') + 1 #Repeated work -> helper function

#     for ch in key:
#         if ch.isalpha():
#             computed_signature += ord(ch) - ord('A') + 1 if ch.isupper() else ord(ch) - ord('a') + 1 #Repeated work -> helper function

#     print(computed_signature)
#     return computed_signature == signature


def ch_value(ch):
    if not ch.isalpha():
        return 0
    return ord(ch) - ord('A') + 27 if ch.isupper() else ord(ch) - ord('a') + 1

def verify(message, key, signature):

    computed_signature = sum(ch_value(ch) for ch in (message + key))

    return computed_signature == signature

print(verify("freeCodeCamp", "Rocks", 238))

verify("foo", "bar", 54)

verify("foo", "bar", 57)