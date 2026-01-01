"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-16

                                    Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
"""

def validate(email):
    #must contain exactly one @ symbol.
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    if not local or not domain:
        return False

    #validate local

    #Cannot start or end with a dot.
    if local[0] == '.' or local[-1]=='.':
        return False
    
    #Cannot have 2 dots in a row:
    if '..' in local:
        return False
    #Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
    for ch in local:
        if not (ch.isalnum() or ch in '._-'):
            return False


    #validate domain:
    if '.' not in domain:
        return False
    if '..' in domain:
        return False
    parts = domain.split('.')
    if len(parts[-1]) <2 or not parts[-1].isalpha():
        return False
    
    return True

print(validate("a@b.cd")) #return Trues