"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-03

P@ssw0rd Str3ngth!
Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

It is at least 8 characters long.
It contains both uppercase and lowercase letters.
It contains at least one number.
It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.

"""

def is_at_least_8_character_long(password):
    return len(password)>=8

def contain_uppercase_lowercase(password):
    isUpper = False
    isLower = False
    for ch in password:
        if ch.isupper():
            isUpper = True
        elif ch.islower():
            isLower = True
    return isUpper and isLower
def contain_at_least_one_number(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False

def contain_special_character(password):
    for ch in password:
        if ch in '!@#$%^&*':
            return True
    return False


def check_strength(password):
    rule1 = is_at_least_8_character_long(password)
    rule2 = contain_uppercase_lowercase(password)
    rule3 = contain_at_least_one_number(password)
    rule4 = contain_special_character(password)

    passed_rules = sum([rule1, rule2, rule3, rule4])

    if passed_rules < 2:
        return 'weak'
    elif passed_rules ==2 or passed_rules == 3:
        return 'medium'
    else:
        return 'strong'