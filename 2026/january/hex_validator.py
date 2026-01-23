"""
Docstring for 2026.january.hex_validator
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-23
                    Hex Validator
Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

Start with a #, and
be followed by either 3 or 6 hexadecimal characters.
Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).
"""
def is_valid_hex(s):
    # Start with s "#"
    if not s.startswith("#"):
        return False
    # 3 or 6 chars after "#"
    hexa_len = len(s[1:])
    if hexa_len not in (3, 6):
        return False
    
    # Hex char are 0 to 9 or a through f
    for i in range(1, len(s), 1):
        curr = s[i].lower()
        if not ('0' <= curr <= '9' or 'a' <= curr <= 'f'):
            return False
    return True

print(is_valid_hex("#123")     )         # should return True.
print(is_valid_hex("#123abc")  )       # should return True.
print(is_valid_hex("#ABCDEF")  )       # should return True.
print(is_valid_hex("#0a1B2c")  )       # should return True.
print(is_valid_hex("#12G")     )         # should return False.
print(is_valid_hex("#1234567") )         # should return False.
print(is_valid_hex("#12 3")    )         # should return False.
print(is_valid_hex("fff")      )         # should return False.